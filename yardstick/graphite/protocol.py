# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
try:
    import cPickle as pickle
except ImportError:
    import pickle as pickle


class Protocol(object):
    def unpack(self, payload):
        raise NotImplemented()


class PickleProtocol(Protocol):
    def unpack(self, payload):
        metrics = pickle.loads(payload)

        return metrics


class TextProtocol(Protocol):
    def unpack(self, payload):
        lines = payload.splitlines()
        metrics = []

        for line in lines:
            name, timestamp, value = line.split(' ', 3)
            metrics.append((name, (timestamp, value)))

        return metrics
