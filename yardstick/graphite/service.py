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
from yardstick import tcp
from yardstick.graphite import protocol


LOG = logging.getLogger(__name__)


class Service(tcp.Service):
    def __init__(self, **kwargs):
        super(Service, self).__init__(host=self.host,
                                      port=self.port,
                                      **kwargs)

    @property
    def host(self):
        return cfg.CONF['service:graphite'].host

    @property
    def port(self):
        raise NotImplemented()

    def start(self):
        super(Service, self).start()

        self.tg.add_thread(self._consume)

    def _consume(self):
        raise NotImplemented()


class PickleService(Service):
    def __init__(self, **kwargs):
        super(PickleService, self).__init__(**kwargs)

        self.protocol = protocol.PickleProtocol()

    @property
    def port(self):
        return cfg.CONF['service:graphite'].pickle_port

    def _consume(self):
        while True:
            connection, address = self.sock.accept()
            payload = ""

            while True:
                data = connection.recv(65535)
                if data == "":
                   break
                payload += data

            metrics = self.protocol.unpack(payload)

            print metrics

            connection.close()


class TextService(Service):
    def __init__(self, **kwargs):
        super(TextService, self).__init__(**kwargs)

        self.protocol = protocol.TextProtocol()

    @property
    def port(self):
        return cfg.CONF['service:graphite'].text_port

    def _consume(self):
        while True:
            connection, address = self.sock.accept()
            payload = ""

            while True:
                data = connection.recv(65535)
                if data == "":
                   break
                payload += data

            metrics = self.protocol.unpack(payload)

            print metrics

            connection.close()
