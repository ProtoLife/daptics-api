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
"""

import asyncio
from async_timeout import timeout as atimeout

from .message import AbsintheEvent
from .channel import ChannelTopic
from .exceptions import InvalidSubscribeMessage, InvalidSubscriptionDataMessage, UnexpectedEvent

class Subscription:
    """
    Binds a subscription channel and a coroutine. When run,
    listen for incoming `subscription:data` messages on the channel
    and pass them to the coroutine. The coroutine should return
    `True` to continue receiving data, or `False` when it is no longer
    interested.
    """
    def __init__(self, channel, coroutine, timeout, **kwargs):
        self.channel = channel
        self.coroutine = coroutine
        self.timeout = timeout
        self.kwargs = kwargs

    def __repr__(self):
        return {'channel': self.channel, 'timeout': self.timeout}

    def __str__(self):
        return 'Subscription on {0!s} with timeout {1}'.format(self.channel, self.timeout)

    async def run(self):
        """
        This can stop with a TimeoutError if a timeout was specified.
        If a coroutine was not specified, the message queue is read
        once, and the last message is returned.
        """
        last_message = None
        loop_count = 0
        # print('Running {0!s}'.format(self))

        while True:
            loop_count = loop_count + 1
            # print('Waiting for messages ({})'.format(loop_count))

            async with atimeout(self.timeout, loop=self.channel.socket.loop):
                last_message = await self.channel.receive()
            if last_message.event != AbsintheEvent.subscription_data.value:
                continue
            if 'result' not in last_message.payload:
                raise InvalidSubscriptionDataMessage(str(last_message))
            if self.coroutine is None:
                break
            keep_going = await self.coroutine(last_message, **self.kwargs)
            if not keep_going:
                break

        # print('Returning {}'.format(last_message))
        return last_message

class Absinthe:
    """
    A context manager that wraps a Phoenix socket. It joins the
    `__absinthe__:control` Phoenix channel on entry, and manages a list
    of subscriptions. On exit, subcriptions are automatically unsubscribed,
    and the manager leaves the Absinthe control channel.
    """
    def __init__(self, socket):
        self.socket = socket
        self._control = socket.channel(ChannelTopic.absinthe.value)
        self._subscriptions = {}

    async def join(self):
        await self._control.join()

    async def leave(self):
        await self.unsubscribe_all()
        await self._control.leave()

    async def push_doc(self, doc, variables=None, timeout=3):
        if variables is None:
            variables = {}
        payload = {
            'query': doc,
            'variables': variables
        }
        return await self._control.push(AbsintheEvent.doc.value, payload, timeout=timeout)

    async def subscribe(self, coroutine, doc, variables=None, timeout=10, start=False, **kwargs):
        await self.join()
        response = await self.push_doc(doc, variables=variables, timeout=10)
        sub_id = self._get_subscription_id(response)
        sub_channel = self.socket.channel(sub_id)
        self._subscriptions[sub_id] = Subscription(sub_channel, coroutine, timeout, **kwargs)
        if start:
            await self.run_subscription(sub_id)
        return sub_id

    async def run_subscription(self, sub_id):
        if sub_id in self._subscriptions:
            sub = self._subscriptions[sub_id]
            await sub.run()

    async def unsubscribe(self, sub_id):
        if sub_id in self._subscriptions:
            del self._subscriptions[sub_id]
            await self._do_unsubscribe(sub_id)

    async def unsubscribe_all(self):
        subs = self._subscriptions.keys()
        self._subscriptions = {}
        for sub_id in subs:
            await self._do_unsubscribe(sub_id)

    async def _do_unsubscribe(self, sub_id):
        await self._control.push(AbsintheEvent.unsubscribe.value,
            {'subscriptionId': sub_id})

    async def __aenter__(self):
        await self.join()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.leave()

    def _get_subscription_id(self, response):
        if isinstance(response, dict) and \
            response.get('status') == 'ok' and \
            isinstance(response.get('response'), dict):
            sub_id = response['response'].get('subscriptionId')
            if sub_id:
                return sub_id
        raise InvalidSubscribeMessage(str(response))
