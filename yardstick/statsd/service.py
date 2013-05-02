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
from yardstick.openstack.common import log as logging
from yardstick import udp
from yardstick.statsd import protocol


LOG = logging.getLogger(__name__)


class Service(udp.Service):
    def __init__(self, **kwargs):
        super(Service, self).__init__(host=cfg.CONF['service:statsd'].host,
                                      port=cfg.CONF['service:statsd'].port,
                                      **kwargs)

        self.protocol = protocol.Protocol()

    def start(self):
        super(Service, self).start()

        self.tg.add_thread(self._consumer_thread)

    def _consumer_thread(self):
        while True:
            payload, address = self.sock.recvfrom(512)

            metrics = self.protocol.unpack(payload)

            print metrics
