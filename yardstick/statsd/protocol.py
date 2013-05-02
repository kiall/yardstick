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
from oslo.config import cfg
from yardstick.openstack.common import timeutils


class Protocol(object):
    def __init__(self):
        self.host = cfg.CONF['host']

    def unpack(self, payload):
        lines = payload.splitlines()
        metrics = []

        for line in lines:
            name, remainder = line.split(':', 2)
            remainder = remainder.split('|')
            value = int(remainder.pop(0))
            type_ = remainder.pop(0)

            if type_ == 'g':
                metrics.append(self.unpack_gauge(name, value))
            elif type_ == 'c':
                metrics.append(self.unpack_counter(name, value, remainder))
            elif type_ == 'ms':
                metrics.append(self.unpack_timer(name, value))
            elif type_ == 'h':
                metrics.append(self.unpack_histogram(name, value))
            elif type_ == 'm':
                metrics.append(self.unpack_meter(name, value))

        return metrics

    def unpack_gauge(self, name, value):
        ts = timeutils.utcnow_ts()

        return ('stats.%s.%s' % (self.host, name), (ts, value))

    def unpack_counter(self, name, value, remainder):
        ts = timeutils.utcnow_ts()

        sample_rate = 1

        if len(remainder) >= 1:
            sample_rate = float(remainder.pop(0).strip('@'))

        value = value * sample_rate

        return ('stats.%s.%s' % (self.host, name), (ts, value))

    def unpack_timer(self, name, value):
        ts = timeutils.utcnow_ts()
        return ('stats.%s.%s' % (self.host, name), (ts, value))

    def unpack_histogram(self, name, value):
        ts = timeutils.utcnow_ts()
        return ('stats.%s.%s' % (self.host, name), (ts, value))

    def unpack_meter(self, name, value):
        ts = timeutils.utcnow_ts()
        return ('stats.%s.%s' % (self.host, name), (ts, value))
