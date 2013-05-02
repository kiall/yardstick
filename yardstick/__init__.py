# Copyright 2012 Managed I.T.
#
# Author: Kiall Mac Innes <kiall@managedit.ie>
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
import os
import socket
from oslo.config import cfg

cfg.CONF.register_opts([
    cfg.StrOpt('config-file', default='yardstick'),
    cfg.StrOpt('host', default=socket.gethostname(),
               help='Name of this node'),
    cfg.StrOpt('pybasedir',
               default=os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    '../')),
               help='Directory where the yardstick python module is '
                    'installed'),
    cfg.StrOpt('state-path', default='$pybasedir',
               help='Top-level directory for maintaining yardstick\'s state'),
])
