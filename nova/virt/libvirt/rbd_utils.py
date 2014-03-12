begin_unit
comment|'# Copyright 2012 Grid Dynamics'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'rados'
newline|'\n'
name|'import'
name|'rbd'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|rados
indent|'    '
name|'rados'
op|'='
name|'None'
newline|'\n'
DECL|variable|rbd
name|'rbd'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RBDVolumeProxy
name|'class'
name|'RBDVolumeProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context manager for dealing with an existing rbd volume.\n\n    This handles connecting to rados and opening an ioctx automatically, and\n    otherwise acts like a librbd Image object.\n\n    The underlying librados client and ioctx can be accessed as the attributes\n    \'client\' and \'ioctx\'.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'driver'
op|','
name|'name'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'client'
op|','
name|'ioctx'
op|'='
name|'driver'
op|'.'
name|'_connect_to_rados'
op|'('
name|'pool'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'='
name|'driver'
op|'.'
name|'rbd'
op|'.'
name|'Image'
op|'('
name|'ioctx'
op|','
name|'str'
op|'('
name|'name'
op|')'
op|','
name|'snapshot'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'driver'
op|'.'
name|'rbd'
op|'.'
name|'Error'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"error opening rbd image %s"'
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'client'
op|','
name|'ioctx'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'client'
newline|'\n'
name|'self'
op|'.'
name|'ioctx'
op|'='
name|'ioctx'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'type_'
op|','
name|'value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'self'
op|'.'
name|'client'
op|','
name|'self'
op|'.'
name|'ioctx'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attrib'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'volume'
op|','
name|'attrib'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ascii_str
dedent|''
dedent|''
name|'def'
name|'ascii_str'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a string to ascii, or return None if the input is None.\n\n    This is useful when a parameter is None by default, or a string. LibRBD\n    only accepts ascii, hence the need for conversion.\n    """'
newline|'\n'
name|'if'
name|'s'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'s'
newline|'\n'
dedent|''
name|'return'
name|'str'
op|'('
name|'s'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RBDDriver
dedent|''
name|'class'
name|'RBDDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'pool'
op|','
name|'ceph_conf'
op|','
name|'rbd_user'
op|','
nl|'\n'
name|'rbd_lib'
op|'='
name|'None'
op|','
name|'rados_lib'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pool'
op|'='
name|'pool'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ceph_conf'
op|'='
name|'ceph_conf'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
name|'if'
name|'ceph_conf'
name|'else'
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'rbd_user'
op|'='
name|'rbd_user'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
name|'if'
name|'rbd_user'
name|'else'
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'rbd'
op|'='
name|'rbd_lib'
name|'or'
name|'rbd'
newline|'\n'
name|'self'
op|'.'
name|'rados'
op|'='
name|'rados_lib'
name|'or'
name|'rados'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'rbd'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'rbd python libraries not found'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_connect_to_rados
dedent|''
dedent|''
name|'def'
name|'_connect_to_rados'
op|'('
name|'self'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'client'
op|'='
name|'self'
op|'.'
name|'rados'
op|'.'
name|'Rados'
op|'('
name|'rados_id'
op|'='
name|'self'
op|'.'
name|'rbd_user'
op|','
nl|'\n'
name|'conffile'
op|'='
name|'self'
op|'.'
name|'ceph_conf'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'client'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'pool_to_open'
op|'='
name|'str'
op|'('
name|'pool'
name|'or'
name|'self'
op|'.'
name|'pool'
op|')'
newline|'\n'
name|'ioctx'
op|'='
name|'client'
op|'.'
name|'open_ioctx'
op|'('
name|'pool_to_open'
op|')'
newline|'\n'
name|'return'
name|'client'
op|','
name|'ioctx'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'rados'
op|'.'
name|'Error'
op|':'
newline|'\n'
comment|'# shutdown cannot raise an exception'
nl|'\n'
indent|'            '
name|'client'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_disconnect_from_rados
dedent|''
dedent|''
name|'def'
name|'_disconnect_from_rados'
op|'('
name|'self'
op|','
name|'client'
op|','
name|'ioctx'
op|')'
op|':'
newline|'\n'
comment|'# closing an ioctx cannot raise an exception'
nl|'\n'
indent|'        '
name|'ioctx'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'client'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|supports_layering
dedent|''
name|'def'
name|'supports_layering'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'rbd'
op|','
string|"'RBD_FEATURE_LAYERING'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|ceph_args
dedent|''
name|'def'
name|'ceph_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'rbd_user'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'--id'"
op|','
name|'self'
op|'.'
name|'rbd_user'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'ceph_conf'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'--conf'"
op|','
name|'self'
op|'.'
name|'ceph_conf'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'args'
newline|'\n'
nl|'\n'
DECL|member|get_mon_addrs
dedent|''
name|'def'
name|'get_mon_addrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
string|"'ceph'"
op|','
string|"'mon'"
op|','
string|"'dump'"
op|','
string|"'--format=json'"
op|']'
op|'+'
name|'self'
op|'.'
name|'ceph_args'
op|'('
op|')'
newline|'\n'
name|'out'
op|','
name|'_'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'lines'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'if'
name|'lines'
op|'['
number|'0'
op|']'
op|'.'
name|'startswith'
op|'('
string|"'dumped monmap epoch'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'='
name|'lines'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'monmap'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
op|')'
newline|'\n'
name|'addrs'
op|'='
op|'['
name|'mon'
op|'['
string|"'addr'"
op|']'
name|'for'
name|'mon'
name|'in'
name|'monmap'
op|'['
string|"'mons'"
op|']'
op|']'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'addr'
name|'in'
name|'addrs'
op|':'
newline|'\n'
indent|'            '
name|'host_port'
op|'='
name|'addr'
op|'['
op|':'
name|'addr'
op|'.'
name|'rindex'
op|'('
string|"'/'"
op|')'
op|']'
newline|'\n'
name|'host'
op|','
name|'port'
op|'='
name|'host_port'
op|'.'
name|'rsplit'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|'.'
name|'strip'
op|'('
string|"'[]'"
op|')'
op|')'
newline|'\n'
name|'ports'
op|'.'
name|'append'
op|'('
name|'port'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hosts'
op|','
name|'ports'
newline|'\n'
nl|'\n'
DECL|member|size
dedent|''
name|'def'
name|'size'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'RBDVolumeProxy'
op|'('
name|'self'
op|','
name|'name'
op|')'
name|'as'
name|'vol'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vol'
op|'.'
name|'size'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|resize
dedent|''
dedent|''
name|'def'
name|'resize'
op|'('
name|'self'
op|','
name|'volume_name'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'size'
op|'='
name|'int'
op|'('
name|'size'
op|')'
op|'*'
name|'units'
op|'.'
name|'Ki'
newline|'\n'
nl|'\n'
name|'with'
name|'RBDVolumeProxy'
op|'('
name|'self'
op|','
name|'volume_name'
op|')'
name|'as'
name|'vol'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'.'
name|'resize'
op|'('
name|'size'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
