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

import collections
import json
import time
from enum import Enum

from .exceptions import InvalidMessage


class PhoenixEvent(Enum):
    close = 'phx_close'
    error = 'phx_error'
    join = 'phx_join'
    reply = 'phx_reply'
    leave = 'phx_leave'


class AbsintheEvent(Enum):
    doc = 'doc'
    unsubscribe = 'unsubscribe'
    subscription_data = 'subscription:data'


class Message(collections.namedtuple('Message', ['join_ref', 'ref', 'topic', 'event', 'payload'])):
    pass


def str_to_msg(str):
    resp = json.loads(str)
    try:
        message = Message(resp.get('join_ref', None),
                          resp.get('ref', None),
                          resp.get('topic', None),
                          resp.get('event', None),
                          resp.get('payload', None))
    except json.decoder.JSONDecodeError:
        raise InvalidMessage(str)
    return message
