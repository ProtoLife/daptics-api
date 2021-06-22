"""
Copyright (c) 2021 Daptics Inc.

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

from websockets.exceptions import ConnectionClosed

ConnectionClosed = ConnectionClosed


class InvalidMessage(Exception):
    pass


class InvalidSubscribeMessage(InvalidMessage):
    pass


class InvalidSubscriptionDataMessage(InvalidMessage):
    pass


class NotAllowedEventName(Exception):
    def __init__(self, event):
        super().__init__('{} is a predefined Phoenix event'.format(event))


class UnexpectedEvent(Exception):
    def __init__(self, event):
        super().__init__('Unexpected event: {}'.format(event))


class CommunicationError(Exception):
    pass
