begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
nl|'\n'
comment|'#    Copyright 2011 - 2012, Red Hat, Inc.'
nl|'\n'
comment|'#'
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
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'greenlet'
newline|'\n'
name|'import'
name|'qpid'
op|'.'
name|'messaging'
newline|'\n'
name|'import'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'amqp'
name|'as'
name|'rpc_amqp'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
op|'.'
name|'common'
name|'import'
name|'LOG'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|qpid_opts
name|'qpid_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_hostname'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'localhost'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Qpid broker hostname'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'5672'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Qpid broker port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_username'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Username for qpid connection'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for qpid connection'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_sasl_mechanisms'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Space separated list of SASL mechanisms to use for auth'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'qpid_reconnect'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Automatically reconnect'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_reconnect_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Reconnection timeout in seconds'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_reconnect_limit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Max reconnections before giving up'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_reconnect_interval_min'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Minimum seconds between reconnection attempts'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_reconnect_interval_max'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum seconds between reconnection attempts'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_reconnect_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Equivalent to setting max and min to the same value'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'qpid_heartbeat'"
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
string|"'Seconds between connection keepalive heartbeats'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qpid_protocol'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'tcp'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Transport to use, either \'tcp\' or \'ssl\'"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'qpid_tcp_nodelay'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Disable Nagle algorithm'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'qpid_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsumerBase
name|'class'
name|'ConsumerBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumer base class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'callback'
op|','
name|'node_name'
op|','
name|'node_opts'
op|','
nl|'\n'
name|'link_name'
op|','
name|'link_opts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Declare a queue on an amqp session.\n\n        \'session\' is the amqp session to use\n        \'callback\' is the callback to call when messages are received\n        \'node_name\' is the first part of the Qpid address string, before \';\'\n        \'node_opts\' will be applied to the "x-declare" section of "node"\n                    in the address string.\n        \'link_name\' goes into the "name" field of the "link" in the address\n                    string\n        \'link_opts\' will be applied to the "x-declare" section of "link"\n                    in the address string.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'callback'
op|'='
name|'callback'
newline|'\n'
name|'self'
op|'.'
name|'receiver'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'addr_opts'
op|'='
op|'{'
nl|'\n'
string|'"create"'
op|':'
string|'"always"'
op|','
nl|'\n'
string|'"node"'
op|':'
op|'{'
nl|'\n'
string|'"type"'
op|':'
string|'"topic"'
op|','
nl|'\n'
string|'"x-declare"'
op|':'
op|'{'
nl|'\n'
string|'"durable"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"auto-delete"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
name|'link_name'
op|','
nl|'\n'
string|'"durable"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"x-declare"'
op|':'
op|'{'
nl|'\n'
string|'"durable"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"auto-delete"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"exclusive"'
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'addr_opts'
op|'['
string|'"node"'
op|']'
op|'['
string|'"x-declare"'
op|']'
op|'.'
name|'update'
op|'('
name|'node_opts'
op|')'
newline|'\n'
name|'addr_opts'
op|'['
string|'"link"'
op|']'
op|'['
string|'"x-declare"'
op|']'
op|'.'
name|'update'
op|'('
name|'link_opts'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'address'
op|'='
string|'"%s ; %s"'
op|'%'
op|'('
name|'node_name'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'addr_opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'reconnect'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reconnect
dedent|''
name|'def'
name|'reconnect'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Re-declare the receiver after a qpid reconnect"""'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'receiver'
op|'='
name|'session'
op|'.'
name|'receiver'
op|'('
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'receiver'
op|'.'
name|'capacity'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|consume
dedent|''
name|'def'
name|'consume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch the message and pass it to the callback object"""'
newline|'\n'
name|'message'
op|'='
name|'self'
op|'.'
name|'receiver'
op|'.'
name|'fetch'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'callback'
op|'('
name|'message'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_receiver
dedent|''
name|'def'
name|'get_receiver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'receiver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectConsumer
dedent|''
dedent|''
name|'class'
name|'DirectConsumer'
op|'('
name|'ConsumerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Queue/consumer class for \'direct\'"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'msg_id'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init a \'direct\' queue.\n\n        \'session\' is the amqp session to use\n        \'msg_id\' is the msg_id to listen on\n        \'callback\' is the callback to call when messages are received\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'DirectConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
name|'callback'
op|','
nl|'\n'
string|'"%s/%s"'
op|'%'
op|'('
name|'msg_id'
op|','
name|'msg_id'
op|')'
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"direct"'
op|'}'
op|','
nl|'\n'
name|'msg_id'
op|','
nl|'\n'
op|'{'
string|'"exclusive"'
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicConsumer
dedent|''
dedent|''
name|'class'
name|'TopicConsumer'
op|'('
name|'ConsumerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumer class for \'topic\'"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'topic'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init a \'topic\' queue.\n\n        \'session\' is the amqp session to use\n        \'topic\' is the topic to listen on\n        \'callback\' is the callback to call when messages are received\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'TopicConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
name|'callback'
op|','
nl|'\n'
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'control_exchange'
op|','
name|'topic'
op|')'
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'topic'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutConsumer
dedent|''
dedent|''
name|'class'
name|'FanoutConsumer'
op|'('
name|'ConsumerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumer class for \'fanout\'"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'topic'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init a \'fanout\' queue.\n\n        \'session\' is the amqp session to use\n        \'topic\' is the topic to listen on\n        \'callback\' is the callback to call when messages are received\n        """'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'FanoutConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
name|'callback'
op|','
nl|'\n'
string|'"%s_fanout"'
op|'%'
name|'topic'
op|','
nl|'\n'
op|'{'
string|'"durable"'
op|':'
name|'False'
op|','
string|'"type"'
op|':'
string|'"fanout"'
op|'}'
op|','
nl|'\n'
string|'"%s_fanout_%s"'
op|'%'
op|'('
name|'topic'
op|','
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
op|')'
op|','
nl|'\n'
op|'{'
string|'"exclusive"'
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Publisher
dedent|''
dedent|''
name|'class'
name|'Publisher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Publisher class"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'node_name'
op|','
name|'node_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init the Publisher class with the exchange_name, routing_key,\n        and other options\n        """'
newline|'\n'
name|'self'
op|'.'
name|'sender'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
nl|'\n'
name|'addr_opts'
op|'='
op|'{'
nl|'\n'
string|'"create"'
op|':'
string|'"always"'
op|','
nl|'\n'
string|'"node"'
op|':'
op|'{'
nl|'\n'
string|'"type"'
op|':'
string|'"topic"'
op|','
nl|'\n'
string|'"x-declare"'
op|':'
op|'{'
nl|'\n'
string|'"durable"'
op|':'
name|'False'
op|','
nl|'\n'
comment|"# auto-delete isn't implemented for exchanges in qpid,"
nl|'\n'
comment|'# but put in here anyway'
nl|'\n'
string|'"auto-delete"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'node_opts'
op|':'
newline|'\n'
indent|'            '
name|'addr_opts'
op|'['
string|'"node"'
op|']'
op|'['
string|'"x-declare"'
op|']'
op|'.'
name|'update'
op|'('
name|'node_opts'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'address'
op|'='
string|'"%s ; %s"'
op|'%'
op|'('
name|'node_name'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'addr_opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'reconnect'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reconnect
dedent|''
name|'def'
name|'reconnect'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Re-establish the Sender after a reconnection"""'
newline|'\n'
name|'self'
op|'.'
name|'sender'
op|'='
name|'session'
op|'.'
name|'sender'
op|'('
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|send
dedent|''
name|'def'
name|'send'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a message"""'
newline|'\n'
name|'self'
op|'.'
name|'sender'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectPublisher
dedent|''
dedent|''
name|'class'
name|'DirectPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publisher class for \'direct\'"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'msg_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Init a \'direct\' publisher."""'
newline|'\n'
name|'super'
op|'('
name|'DirectPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
name|'msg_id'
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"Direct"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicPublisher
dedent|''
dedent|''
name|'class'
name|'TopicPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publisher class for \'topic\'"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""init a \'topic\' publisher.\n        """'
newline|'\n'
name|'super'
op|'('
name|'TopicPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
nl|'\n'
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'control_exchange'
op|','
name|'topic'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutPublisher
dedent|''
dedent|''
name|'class'
name|'FanoutPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publisher class for \'fanout\'"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""init a \'fanout\' publisher.\n        """'
newline|'\n'
name|'super'
op|'('
name|'FanoutPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
nl|'\n'
string|'"%s_fanout"'
op|'%'
name|'topic'
op|','
op|'{'
string|'"type"'
op|':'
string|'"fanout"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotifyPublisher
dedent|''
dedent|''
name|'class'
name|'NotifyPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publisher class for notifications"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""init a \'topic\' publisher.\n        """'
newline|'\n'
name|'super'
op|'('
name|'NotifyPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'session'
op|','
nl|'\n'
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'control_exchange'
op|','
name|'topic'
op|')'
op|','
nl|'\n'
op|'{'
string|'"durable"'
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
dedent|''
dedent|''
name|'class'
name|'Connection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Connection object."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'consumers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'consumer_thread'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'broker'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_hostname'
op|'+'
string|'":"'
op|'+'
name|'FLAGS'
op|'.'
name|'qpid_port'
newline|'\n'
comment|'# Create the connection - this does not open the connection'
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Connection'
op|'('
name|'self'
op|'.'
name|'broker'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if flags are set and if so set them for the connection'
nl|'\n'
comment|'# before we call open'
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'username'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_username'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_password'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'sasl_mechanisms'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_sasl_mechanisms'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect_timeout'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect_timeout'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect_limit'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect_limit'
newline|'\n'
name|'_qpid_reconnect_interval_max'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect_interval_max'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect_interval_max'
op|'='
name|'_qpid_reconnect_interval_max'
newline|'\n'
name|'_qpid_reconnect_interval_min'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect_interval_min'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect_interval_min'
op|'='
name|'_qpid_reconnect_interval_min'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'reconnect_interval'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_reconnect_interval'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'hearbeat'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_heartbeat'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'protocol'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_protocol'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'tcp_nodelay'
op|'='
name|'FLAGS'
op|'.'
name|'qpid_tcp_nodelay'
newline|'\n'
nl|'\n'
comment|'# Open is part of reconnect -'
nl|'\n'
comment|'# NOTE(WGH) not sure we need this with the reconnect flags'
nl|'\n'
name|'self'
op|'.'
name|'reconnect'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_register_consumer
dedent|''
name|'def'
name|'_register_consumer'
op|'('
name|'self'
op|','
name|'consumer'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'consumers'
op|'['
name|'str'
op|'('
name|'consumer'
op|'.'
name|'get_receiver'
op|'('
op|')'
op|')'
op|']'
op|'='
name|'consumer'
newline|'\n'
nl|'\n'
DECL|member|_lookup_consumer
dedent|''
name|'def'
name|'_lookup_consumer'
op|'('
name|'self'
op|','
name|'receiver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'consumers'
op|'['
name|'str'
op|'('
name|'receiver'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|reconnect
dedent|''
name|'def'
name|'reconnect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Handles reconnecting and re-establishing sessions and queues"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'opened'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
op|'.'
name|'ConnectionError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'open'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
op|'.'
name|'ConnectionError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Unable to connect to AMQP server: %s '"
op|'%'
name|'str'
op|'('
name|'e'
op|')'
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'FLAGS'
op|'.'
name|'qpid_reconnect_interval'
name|'or'
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Connected to AMQP server on %s'"
op|'%'
name|'self'
op|'.'
name|'broker'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'consumer'
name|'in'
name|'self'
op|'.'
name|'consumers'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'consumer'
op|'.'
name|'reconnect'
op|'('
name|'self'
op|'.'
name|'session'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'consumers'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Re-established AMQP queues"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ensure
dedent|''
dedent|''
name|'def'
name|'ensure'
op|'('
name|'self'
op|','
name|'error_callback'
op|','
name|'method'
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
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
op|'.'
name|'Empty'
op|','
nl|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
op|'.'
name|'ConnectionError'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'error_callback'
op|':'
newline|'\n'
indent|'                    '
name|'error_callback'
op|'('
name|'e'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'reconnect'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
dedent|''
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Close/release this connection"""'
newline|'\n'
name|'self'
op|'.'
name|'cancel_consumer_thread'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|reset
dedent|''
name|'def'
name|'reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reset a connection so it can be used again"""'
newline|'\n'
name|'self'
op|'.'
name|'cancel_consumer_thread'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'session'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'consumers'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|declare_consumer
dedent|''
name|'def'
name|'declare_consumer'
op|'('
name|'self'
op|','
name|'consumer_cls'
op|','
name|'topic'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a Consumer using the class that was passed in and\n        add it to our list of consumers\n        """'
newline|'\n'
DECL|function|_connect_error
name|'def'
name|'_connect_error'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'log_info'
op|'='
op|'{'
string|"'topic'"
op|':'
name|'topic'
op|','
string|"'err_str'"
op|':'
name|'str'
op|'('
name|'exc'
op|')'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to declare consumer for topic \'%(topic)s\': "'
nl|'\n'
string|'"%(err_str)s"'
op|')'
op|'%'
name|'log_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_declare_consumer
dedent|''
name|'def'
name|'_declare_consumer'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'consumer'
op|'='
name|'consumer_cls'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'topic'
op|','
name|'callback'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_register_consumer'
op|'('
name|'consumer'
op|')'
newline|'\n'
name|'return'
name|'consumer'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'ensure'
op|'('
name|'_connect_error'
op|','
name|'_declare_consumer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|iterconsume
dedent|''
name|'def'
name|'iterconsume'
op|'('
name|'self'
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return an iterator that will consume from all queues/consumers"""'
newline|'\n'
nl|'\n'
DECL|function|_error_callback
name|'def'
name|'_error_callback'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'exceptions'
op|'.'
name|'Empty'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Timed out waiting for RPC response: %s'"
op|')'
op|'%'
nl|'\n'
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'rpc_common'
op|'.'
name|'Timeout'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to consume message from queue: %s'"
op|')'
op|'%'
nl|'\n'
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_consume
dedent|''
dedent|''
name|'def'
name|'_consume'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'nxt_receiver'
op|'='
name|'self'
op|'.'
name|'session'
op|'.'
name|'next_receiver'
op|'('
name|'timeout'
op|'='
name|'timeout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_lookup_consumer'
op|'('
name|'nxt_receiver'
op|')'
op|'.'
name|'consume'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'iteration'
name|'in'
name|'itertools'
op|'.'
name|'count'
op|'('
number|'0'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'limit'
name|'and'
name|'iteration'
op|'>='
name|'limit'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'StopIteration'
newline|'\n'
dedent|''
name|'yield'
name|'self'
op|'.'
name|'ensure'
op|'('
name|'_error_callback'
op|','
name|'_consume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cancel_consumer_thread
dedent|''
dedent|''
name|'def'
name|'cancel_consumer_thread'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cancel a consumer thread"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'consumer_thread'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'consumer_thread'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'consumer_thread'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'consumer_thread'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|publisher_send
dedent|''
dedent|''
name|'def'
name|'publisher_send'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send to a publisher based on the publisher class"""'
newline|'\n'
nl|'\n'
DECL|function|_connect_error
name|'def'
name|'_connect_error'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'log_info'
op|'='
op|'{'
string|"'topic'"
op|':'
name|'topic'
op|','
string|"'err_str'"
op|':'
name|'str'
op|'('
name|'exc'
op|')'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to publish message to topic "'
nl|'\n'
string|'"\'%(topic)s\': %(err_str)s"'
op|')'
op|'%'
name|'log_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_publisher_send
dedent|''
name|'def'
name|'_publisher_send'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'publisher'
op|'='
name|'cls'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'ensure'
op|'('
name|'_connect_error'
op|','
name|'_publisher_send'
op|')'
newline|'\n'
nl|'\n'
DECL|member|declare_direct_consumer
dedent|''
name|'def'
name|'declare_direct_consumer'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a \'direct\' queue.\n        In nova\'s use, this is generally a msg_id queue used for\n        responses for call/multicall\n        """'
newline|'\n'
name|'self'
op|'.'
name|'declare_consumer'
op|'('
name|'DirectConsumer'
op|','
name|'topic'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|declare_topic_consumer
dedent|''
name|'def'
name|'declare_topic_consumer'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a \'topic\' consumer."""'
newline|'\n'
name|'self'
op|'.'
name|'declare_consumer'
op|'('
name|'TopicConsumer'
op|','
name|'topic'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|declare_fanout_consumer
dedent|''
name|'def'
name|'declare_fanout_consumer'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a \'fanout\' consumer"""'
newline|'\n'
name|'self'
op|'.'
name|'declare_consumer'
op|'('
name|'FanoutConsumer'
op|','
name|'topic'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|direct_send
dedent|''
name|'def'
name|'direct_send'
op|'('
name|'self'
op|','
name|'msg_id'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a \'direct\' message"""'
newline|'\n'
name|'self'
op|'.'
name|'publisher_send'
op|'('
name|'DirectPublisher'
op|','
name|'msg_id'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|topic_send
dedent|''
name|'def'
name|'topic_send'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a \'topic\' message"""'
newline|'\n'
name|'self'
op|'.'
name|'publisher_send'
op|'('
name|'TopicPublisher'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fanout_send
dedent|''
name|'def'
name|'fanout_send'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a \'fanout\' message"""'
newline|'\n'
name|'self'
op|'.'
name|'publisher_send'
op|'('
name|'FanoutPublisher'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|notify_send
dedent|''
name|'def'
name|'notify_send'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'msg'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send a notify message on a topic"""'
newline|'\n'
name|'self'
op|'.'
name|'publisher_send'
op|'('
name|'NotifyPublisher'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|consume
dedent|''
name|'def'
name|'consume'
op|'('
name|'self'
op|','
name|'limit'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consume from all queues/consumers"""'
newline|'\n'
name|'it'
op|'='
name|'self'
op|'.'
name|'iterconsume'
op|'('
name|'limit'
op|'='
name|'limit'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'it'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|consume_in_thread
dedent|''
dedent|''
dedent|''
name|'def'
name|'consume_in_thread'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consumer from all queues/consumers in a greenthread"""'
newline|'\n'
DECL|function|_consumer_thread
name|'def'
name|'_consumer_thread'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'consume'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'consumer_thread'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'consumer_thread'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'_consumer_thread'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'consumer_thread'
newline|'\n'
nl|'\n'
DECL|member|create_consumer
dedent|''
name|'def'
name|'create_consumer'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'proxy'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a consumer that calls a method in a proxy object"""'
newline|'\n'
name|'if'
name|'fanout'
op|':'
newline|'\n'
indent|'            '
name|'consumer'
op|'='
name|'FanoutConsumer'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'topic'
op|','
nl|'\n'
name|'rpc_amqp'
op|'.'
name|'ProxyCallback'
op|'('
name|'proxy'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'consumer'
op|'='
name|'TopicConsumer'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'topic'
op|','
nl|'\n'
name|'rpc_amqp'
op|'.'
name|'ProxyCallback'
op|'('
name|'proxy'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_register_consumer'
op|'('
name|'consumer'
op|')'
newline|'\n'
name|'return'
name|'consumer'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'Connection'
op|'.'
name|'pool'
op|'='
name|'rpc_amqp'
op|'.'
name|'Pool'
op|'('
name|'connection_cls'
op|'='
name|'Connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_connection
name|'def'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a connection"""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|multicall
dedent|''
name|'def'
name|'multicall'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a call that returns multiple times."""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'multicall'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call
dedent|''
name|'def'
name|'call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic and wait for a response."""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast
dedent|''
name|'def'
name|'cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic without waiting for a response."""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast
dedent|''
name|'def'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a fanout exchange without waiting for a response."""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a notification event on a topic."""'
newline|'\n'
name|'return'
name|'rpc_amqp'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'rpc_amqp'
op|'.'
name|'cleanup'
op|'('
name|'Connection'
op|'.'
name|'pool'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
