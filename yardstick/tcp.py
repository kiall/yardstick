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
import eventlet
from yardstick.openstack.common import log as logging
from yardstick.openstack.common import service

LOG = logging.getLogger(__name__)


class Service(service.Service):
    def __init__(self, host, port, threads=1000):
        super(Service, self).__init__(threads)

        self.sock = eventlet.listen((host, port))

