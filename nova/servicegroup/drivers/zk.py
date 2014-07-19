begin_unit
comment|'# Copyright (c) AT&T 2012-2013 Yun Mao <yunmao@gmail.com>'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or'
nl|'\n'
comment|'# implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
name|'importutils'
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
name|'loopingcall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
name|'import'
name|'api'
newline|'\n'
nl|'\n'
DECL|variable|evzookeeper
name|'evzookeeper'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|"'evzookeeper'"
op|')'
newline|'\n'
DECL|variable|membership
name|'membership'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|"'evzookeeper.membership'"
op|')'
newline|'\n'
DECL|variable|zookeeper
name|'zookeeper'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|"'zookeeper'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|zk_driver_opts
name|'zk_driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'address'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The ZooKeeper addresses for servicegroup service in the '"
nl|'\n'
string|"'format of host1:port,host2:port,host3:port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'recv_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'4000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The recv_timeout parameter for the zk session'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sg_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"/servicegroups"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The prefix used in ZooKeeper to store ephemeral nodes'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'sg_retry_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds to wait until retrying to join the '"
nl|'\n'
string|"'session'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'zk_driver_opts'
op|','
name|'group'
op|'='
string|'"zookeeper"'
op|')'
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
DECL|class|ZooKeeperDriver
name|'class'
name|'ZooKeeperDriver'
op|'('
name|'api'
op|'.'
name|'ServiceGroupDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""ZooKeeper driver for the service group API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the zk session object."""'
newline|'\n'
name|'if'
name|'not'
name|'all'
op|'('
op|'['
name|'evzookeeper'
op|','
name|'membership'
op|','
name|'zookeeper'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ImportError'
op|'('
string|"'zookeeper module not found'"
op|')'
newline|'\n'
dedent|''
name|'null'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'evzookeeper'
op|'.'
name|'ZKSession'
op|'('
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'address'
op|','
nl|'\n'
name|'recv_timeout'
op|'='
nl|'\n'
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'recv_timeout'
op|','
nl|'\n'
name|'zklog_fd'
op|'='
name|'null'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_memberships'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_monitors'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|'# Make sure the prefix exists'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_session'
op|'.'
name|'create'
op|'('
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'sg_prefix'
op|','
string|'""'
op|','
nl|'\n'
name|'acl'
op|'='
op|'['
name|'evzookeeper'
op|'.'
name|'ZOO_OPEN_ACL_UNSAFE'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'zookeeper'
op|'.'
name|'NodeExistsException'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'ZooKeeperDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Join the given service with its group."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'ZooKeeperDriver: join new member %(id)s to the '"
nl|'\n'
string|"'%(gr)s group, service=%(sr)s'"
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'member_id'
op|','
string|"'gr'"
op|':'
name|'group'
op|','
string|"'sr'"
op|':'
name|'service'
op|'}'
op|')'
newline|'\n'
name|'member'
op|'='
name|'self'
op|'.'
name|'_memberships'
op|'.'
name|'get'
op|'('
op|'('
name|'group'
op|','
name|'member_id'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'member'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# the first time to join. Generate a new object'
nl|'\n'
indent|'            '
name|'path'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'sg_prefix'
op|','
name|'group'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'member'
op|'='
name|'membership'
op|'.'
name|'Membership'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'path'
op|','
name|'member_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Unable to join. It is possible that either "'
nl|'\n'
string|'"another node exists with the same name, or "'
nl|'\n'
string|'"this node just restarted. We will try "'
nl|'\n'
string|'"again in a short while to make sure."'
op|')'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'sg_retry_interval'
op|')'
newline|'\n'
name|'member'
op|'='
name|'membership'
op|'.'
name|'Membership'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'path'
op|','
name|'member_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_memberships'
op|'['
op|'('
name|'group'
op|','
name|'member_id'
op|')'
op|']'
op|'='
name|'member'
newline|'\n'
dedent|''
name|'return'
name|'FakeLoopingCall'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|leave
dedent|''
name|'def'
name|'leave'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove the given member from the service group."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'ZooKeeperDriver.leave: %(member)s from group %(group)s'"
op|','
nl|'\n'
op|'{'
string|"'member'"
op|':'
name|'member_id'
op|','
string|"'group'"
op|':'
name|'group'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
op|'('
name|'group'
op|','
name|'member_id'
op|')'
newline|'\n'
name|'member'
op|'='
name|'self'
op|'.'
name|'_memberships'
op|'['
name|'key'
op|']'
newline|'\n'
name|'member'
op|'.'
name|'leave'
op|'('
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'_memberships'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'ZooKeeperDriver.leave: %(id)s has not joined to the '"
nl|'\n'
string|"'%(gr)s group'"
op|')'
op|','
op|'{'
string|"'id'"
op|':'
name|'member_id'
op|','
string|"'gr'"
op|':'
name|'group'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_up
dedent|''
dedent|''
name|'def'
name|'is_up'
op|'('
name|'self'
op|','
name|'service_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_id'
op|'='
name|'service_ref'
op|'['
string|"'topic'"
op|']'
newline|'\n'
name|'member_id'
op|'='
name|'service_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'all_members'
op|'='
name|'self'
op|'.'
name|'get_all'
op|'('
name|'group_id'
op|')'
newline|'\n'
name|'return'
name|'member_id'
name|'in'
name|'all_members'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all members in a list, or a ServiceGroupUnavailable\n        exception.\n        """'
newline|'\n'
name|'monitor'
op|'='
name|'self'
op|'.'
name|'_monitors'
op|'.'
name|'get'
op|'('
name|'group_id'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'monitor'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'CONF'
op|'.'
name|'zookeeper'
op|'.'
name|'sg_prefix'
op|','
name|'group_id'
op|')'
newline|'\n'
name|'monitor'
op|'='
name|'membership'
op|'.'
name|'MembershipMonitor'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_monitors'
op|'['
name|'group_id'
op|']'
op|'='
name|'monitor'
newline|'\n'
comment|'# Note(maoy): When initialized for the first time, it takes a'
nl|'\n'
comment|'# while to retrieve all members from zookeeper. To prevent'
nl|'\n'
comment|'# None to be returned, we sleep 5 sec max to wait for data to'
nl|'\n'
comment|'# be ready.'
nl|'\n'
name|'for'
name|'_retry'
name|'in'
name|'range'
op|'('
number|'50'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'all_members'
op|'='
name|'monitor'
op|'.'
name|'get_all'
op|'('
op|')'
newline|'\n'
name|'if'
name|'all_members'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'all_members'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'all_members'
op|'='
name|'monitor'
op|'.'
name|'get_all'
op|'('
op|')'
newline|'\n'
name|'if'
name|'all_members'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ServiceGroupUnavailable'
op|'('
name|'driver'
op|'='
string|'"ZooKeeperDriver"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'all_members'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLoopingCall
dedent|''
dedent|''
name|'class'
name|'FakeLoopingCall'
op|'('
name|'loopingcall'
op|'.'
name|'LoopingCallBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The fake Looping Call implementation, created for backward\n    compatibility with a membership based on DB.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'driver'
op|','
name|'host'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'_group'
op|'='
name|'group'
newline|'\n'
name|'self'
op|'.'
name|'_host'
op|'='
name|'host'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_driver'
op|'.'
name|'leave'
op|'('
name|'self'
op|'.'
name|'_host'
op|','
name|'self'
op|'.'
name|'_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'interval'
op|','
name|'initial_delay'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
