"""
Copyright (c) 2020 Daptics Inc.

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

This file contains minor modifications by Daptics to add support for
Absinthe Phoenix Channels.

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
import enum

from .exceptions import NotAllowedEventName, CommunicationError
from .message import PhoenixEvent


class ChannelTopic(enum.Enum):
    absinthe = '__absinthe__:control'


class State(enum.IntEnum):
    CONNECTING, OPEN, CLOSING, CLOSED = range(4)


class Channel:
    def __init__(self, socket, topic, params=None, max_queue=2 ** 5, timeout_secs=3, num_retry=3):
        self.socket = socket
        self.topic = topic
        self.params = params
        self.join_ref = None
        self.status = State.CLOSED
        self.messages = asyncio.queues.Queue(max_queue, loop=self.socket.loop)
        self.timeout_secs = timeout_secs
        self.num_retry = num_retry

    def __repr__(self):
        return {'topic': self.topic, 'status': self.status}

    def __str__(self):
        return 'Channel \'{0}\', status {1}'.format(self.topic, self.status)

    async def join(self, payload=None, wait_response=True):
        def failed_to_connect(reason):
            self.status = State.CLOSED
            raise CommunicationError('{} JOIN FAILED: {}'.format(self.topic, reason))

        if self.status == State.CLOSED:
            self.status = State.CONNECTING

            try:
                msg = await self._push(PhoenixEvent.join.value, payload, timeout=self.timeout_secs, retry=self.num_retry,
                                       wait_response=wait_response, _internal_use=True)
            except CommunicationError:
                failed_to_connect('No response from server')
            else:
                if msg['status'].lower() == 'ok':
                    self.status = State.OPEN
                else:
                    if 'response' in msg:
                        if 'message' in msg['response'] and 'error_code' in msg['response']:
                            failed_to_connect(reason=msg['response']['message'])
                        elif 'reason' in msg['response']:
                            failed_to_connect(reason=msg['response']['reason'])
                    else:
                        failed_to_connect('Unknown reason')
            return msg

    async def leave(self, wait_response=True):
        if self.status == State.OPEN:
            self.status = State.CLOSING

            try:
                msg = await self._push(PhoenixEvent.leave.value, timeout=self.timeout_secs, retry=self.num_retry,
                                       wait_response=wait_response, _internal_use=True)
            except CommunicationError:
                pass

            self.join_ref = None
            self.status = State.CLOSED
            return msg

    async def push(self, event, payload={}, timeout=3, retry=3, wait_response=True):
        return await self._push(event=event,
                                payload=payload,
                                timeout=timeout,
                                retry=retry,
                                wait_response=wait_response)

    async def _push(self, event, payload=None, timeout=3, retry=3, wait_response=True, _internal_use=False):
        if not _internal_use:
            if event in map(str, PhoenixEvent):
                raise NotAllowedEventName(event)

        return await self.socket.push(self,
                                     event=event,
                                     payload=payload,
                                     wait_response=wait_response,
                                     timeout=timeout,
                                     retry=retry)

    async def receive(self):
        return await self.messages.get()

    async def __aenter__(self):
        await self.join()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.leave()
