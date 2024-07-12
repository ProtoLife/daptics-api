"""
Copyright (c) 2024 Daptics Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), the
rights to use, copy, modify, merge, publish, and/or distribute, copies of
the Software, and to permit persons to whom the Software is furnished to do
so.

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.

This file contains minor modifications by Daptics.

Major portions of this file are:

Copyright (c) 2018 Daybit

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import asyncio
import json
import logging
import re
import sys
import urllib

import websockets
from async_timeout import timeout as atimeout

from .channel import Channel
from .exceptions import ConnectionClosed, CommunicationError
from .message import PhoenixEvent, str_to_msg

"""
The logger's name is 'phoenix.phoenix'
"""
logger = logging.getLogger(__name__)


class Phoenix:
    def __init__(self, url, params=None, loop=None, heartbeat_secs=30, timeout_secs=3, ssl=None):
        if loop is None:
            loop = asyncio.get_event_loop()
        self.loop = loop
        self.url = url
        self.params = params
        self._socket = None
        self._ref = 0
        self._channels = {}
        self._waited_messages = {}
        self._heartbeat_secs = heartbeat_secs
        self._coroutines = []
        self._reconnect_tries = 0
        self.connected = False
        self._phoenix = Channel(self, 'phoenix')
        self._connection_lost = False
        self._timeout_secs = timeout_secs
        self._ssl = ssl

    async def connect(self):
        if self.connected:
            return
        try:
            url_parts = [self.url]
            if self.params:
                qs = urllib.parse.urlencode(self.params)
                if len(qs) > 0:
                    url_parts.append(qs)
            url_with_params = '?'.join(url_parts)
            logger.info('connect to {}'.format(url_with_params))
            self.connected = True
            # Python <3.10 has deprecated loop=self.loop
            async with atimeout(self._timeout_secs * 2):
                self._socket = await websockets.connect(url_with_params,
                                                        ssl=self._ssl,
                                                        loop=self.loop)
            self._coroutines = [asyncio.ensure_future(self.recv(), loop=self.loop),
                                asyncio.ensure_future(self.heartbeat(), loop=self.loop),
                                asyncio.ensure_future(self.wait_for_disconnection(), loop=self.loop)]
        except OSError as e:
            if re.compile(r'.*Errno 61.*').match(str(e)):
                raise ConnectionRefusedError('server is not responding')
            raise e
        except asyncio.TimeoutError:
            raise TimeoutError('timeout in opening a websocket')

    async def disconnect(self):
        if not self.connected:
            return

        for ch in self._channels:
            await self._channels[ch].leave()
        self._remove_all_channels()
        self._connection_lost = self._socket.connection_lost_waiter.done()

        self.connected = False
        await self._socket.close()
        if self._socket.close_reason:
            logger.info('disconnected {} {}'.format(self._socket.close_code, self._socket.close_reason))
        else:
            logger.info('disconnected {}'.format(self._socket.close_code))

        for co in self._coroutines:
            co.cancel()
        self._coroutines = []

    def channel(self, topic, params=None, channel_t=Channel, **kwargs):
        try:
            if 'timeout_secs' not in kwargs:
                kwargs['timeout_secs'] = self._timeout_secs
            channel = self._channels[topic]
        except KeyError:
            channel = channel_t(self, topic, params, **kwargs)
            self._channels[topic] = channel
        return channel

    def remove_channel(self, topic):
        self._channels.pop(topic, None)

    def _remove_all_channels(self):
        self._channels.clear()

    async def push(self, channel, event, payload, timeout=None, retry=3, wait_response=True):
        if not self.connected:
            raise CommunicationError('attempting to send a message before connection')
        if timeout is None:
            timeout = self._timeout_secs

        msg_response = None
        ref = None
        if retry <= 0:
            retry = 0
        retry += 1

        for i in range(retry):
            try:
                # Python <3.10 has deprecated loop=self.loop
                async with atimeout(timeout):
                    ref = self.make_ref()
                    if PhoenixEvent.join.value == event:
                        channel.join_ref = ref
                    if payload is None:
                        payload = {}
                    message_data = {
                        'topic': channel.topic,
                        'event': event,
                        'payload': payload,
                        'ref': ref,
                        'join_ref': channel.join_ref
                    }
                    msg = json.dumps(message_data)
                    logger.debug('> {}'.format(msg))
                    await self._send(msg)

                    if wait_response:
                        msg_response = asyncio.Future(loop=self.loop)
                        if ref in self._waited_messages:
                            self._waited_messages[ref].cancel()
                        self._waited_messages[ref] = msg_response

                        try:
                            await msg_response
                        except asyncio.CancelledError:
                            raise asyncio.TimeoutError

            except asyncio.TimeoutError:
                retry_str = ''
                if i > 0:
                    retry_str = ' retry {}/{}'.format(i, retry - 1)
                logger.warning(('{}/{} - failed to get a response' + retry_str).format(channel.topic, event))

                if wait_response and ref is not None:
                    self._waited_messages.pop(ref, None)
            else:
                if msg_response is None:
                    return
                return msg_response.result()
        raise CommunicationError('failed to send a message')

    def make_ref(self):
        if self._ref == sys.maxsize:
            new_ref = self._ref = 0
        else:
            new_ref = self._ref = self._ref + 1
        return str(new_ref)

    async def _send(self, message):
        await self._socket.send(message)

    async def heartbeat(self):
        while True:
            await asyncio.sleep(self._heartbeat_secs, loop=self.loop)
            await self.push(self._phoenix, 'heartbeat', {})

    async def recv(self):
        try:
            while True:
                try:
                    recv_msg = await self._socket.recv()
                    logger.debug('< {}'.format(recv_msg))
                    message = str_to_msg(recv_msg)
                except json.decoder.JSONDecodeError:
                    logger.warning('ignore a invalid message: {}'.format(recv_msg))
                else:
                    if message.event == PhoenixEvent.reply.value:
                        if message.ref in self._waited_messages:
                            future = self._waited_messages.pop(message.ref)
                            if future.cancelled():
                                logger.warning('{} ref future already canceled'.format(message.ref))
                            else:
                                future.set_result(message.payload)
                        else:
                            logger.warning('received not waiting message. {}'.format(recv_msg))
                    else:
                        if message.topic not in self._channels:
                            logger.warning('{}/{} message arrived for unknown topic'.format(message.topic, message.event))
                            unkown_channel = self.channel(message.topic)
                        await self._channels[message.topic].messages.put(message)
        except ConnectionClosed:
            pass
        except Exception:
            logger.error('Error in data transfer', exc_info=True)
            await asyncio.shield(self.disconnect(), loop=self.loop)

    async def wait_for_disconnection(self):
        await self._socket.connection_lost_waiter
        await self.disconnect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._do_exit(exc_type)

    async def __aenter__(self):
        await self.__await__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()
        self._do_exit()

    def _do_exit(self):
        if self._connection_lost:
            raise ConnectionClosed(self._socket.close_code, self._socket.close_reason)

    def __await__(self):
        return self.__await_impl__()

    async def __await_impl__(self):
        await self.connect()
        return self
