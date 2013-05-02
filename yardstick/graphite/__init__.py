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

cfg.CONF.register_group(cfg.OptGroup(
    name='service:graphite', title="Configuration for Graphite Service"
))

cfg.CONF.register_opts([
    cfg.StrOpt('host', default='0.0.0.0',
               help='Host'),
    cfg.IntOpt('text-port', default=2003,
               help='Text Protocol Port Number'),
    cfg.IntOpt('pickle-port', default=2004,
               help='Pickle Protocol Port Number'),
], group='service:graphite')
