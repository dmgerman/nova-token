begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
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
string|'"""\nUnit Tests for remote procedure calls using kombu\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
name|'impl_kombu'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'rpc'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
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
DECL|class|MyException
name|'class'
name|'MyException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_raise_exc_stub
dedent|''
name|'def'
name|'_raise_exc_stub'
op|'('
name|'stubs'
op|','
name|'times'
op|','
name|'obj'
op|','
name|'method'
op|','
name|'exc_msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'info'
op|'='
op|'{'
string|"'called'"
op|':'
number|'0'
op|'}'
newline|'\n'
name|'orig_method'
op|'='
name|'getattr'
op|'('
name|'obj'
op|','
name|'method'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_raise_stub
name|'def'
name|'_raise_stub'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'['
string|"'called'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'info'
op|'['
string|"'called'"
op|']'
op|'<='
name|'times'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'MyException'
op|'('
name|'exc_msg'
op|')'
newline|'\n'
dedent|''
name|'orig_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'obj'
op|','
name|'method'
op|','
name|'_raise_stub'
op|')'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcKombuTestCase
dedent|''
name|'class'
name|'RpcKombuTestCase'
op|'('
name|'common'
op|'.'
name|'_BaseRpcTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'rpc'
op|'='
name|'impl_kombu'
newline|'\n'
name|'super'
op|'('
name|'RpcKombuTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'impl_kombu'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'RpcKombuTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reusing_connection
dedent|''
name|'def'
name|'test_reusing_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that reusing a connection returns same one."""'
newline|'\n'
name|'conn_context'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'False'
op|')'
newline|'\n'
name|'conn1'
op|'='
name|'conn_context'
op|'.'
name|'connection'
newline|'\n'
name|'conn_context'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'conn_context'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'False'
op|')'
newline|'\n'
name|'conn2'
op|'='
name|'conn_context'
op|'.'
name|'connection'
newline|'\n'
name|'conn_context'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conn1'
op|','
name|'conn2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_topic_send_receive
dedent|''
name|'def'
name|'test_topic_send_receive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test sending to a topic exchange/queue"""'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
string|"'topic test message'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'received_message'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_callback
name|'def'
name|'_callback'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'received_message'
op|'='
name|'message'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'.'
name|'declare_topic_consumer'
op|'('
string|"'a_topic'"
op|','
name|'_callback'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'topic_send'
op|'('
string|"'a_topic'"
op|','
name|'message'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'consume'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'received_message'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_direct_send_receive
dedent|''
name|'def'
name|'test_direct_send_receive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test sending to a direct exchange/queue"""'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
string|"'direct test message'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'received_message'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_callback
name|'def'
name|'_callback'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'received_message'
op|'='
name|'message'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'.'
name|'declare_direct_consumer'
op|'('
string|"'a_direct'"
op|','
name|'_callback'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'direct_send'
op|'('
string|"'a_direct'"
op|','
name|'message'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'consume'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'received_message'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cast_interface_uses_default_options
dedent|''
name|'def'
name|'test_cast_interface_uses_default_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test kombu rpc.cast"""'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|MyConnection
name|'class'
name|'MyConnection'
op|'('
name|'impl_kombu'
op|'.'
name|'Connection'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'myself'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'super'
op|'('
name|'MyConnection'
op|','
name|'myself'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'myself'
op|'.'
name|'params'
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'FLAGS'
op|'.'
name|'rabbit_host'
op|','
nl|'\n'
string|"'userid'"
op|':'
name|'FLAGS'
op|'.'
name|'rabbit_userid'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'FLAGS'
op|'.'
name|'rabbit_password'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'FLAGS'
op|'.'
name|'rabbit_port'
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
name|'FLAGS'
op|'.'
name|'rabbit_virtual_host'
op|','
nl|'\n'
string|"'transport'"
op|':'
string|"'memory'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|topic_send
dedent|''
name|'def'
name|'topic_send'
op|'('
name|'_context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'MyConnection'
op|'.'
name|'pool'
op|'='
name|'rpc_amqp'
op|'.'
name|'Pool'
op|'('
name|'connection_cls'
op|'='
name|'MyConnection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'impl_kombu'
op|','
string|"'Connection'"
op|','
name|'MyConnection'
op|')'
newline|'\n'
nl|'\n'
name|'impl_kombu'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'fake_topic'"
op|','
op|'{'
string|"'msg'"
op|':'
string|"'fake'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cast_to_server_uses_server_params
dedent|''
name|'def'
name|'test_cast_to_server_uses_server_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test kombu rpc.cast"""'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
name|'server_params'
op|'='
op|'{'
string|"'username'"
op|':'
string|"'fake_username'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'fake_password'"
op|','
nl|'\n'
string|"'hostname'"
op|':'
string|"'fake_hostname'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'31337'
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
string|"'fake_virtual_host'"
op|'}'
newline|'\n'
nl|'\n'
DECL|class|MyConnection
name|'class'
name|'MyConnection'
op|'('
name|'impl_kombu'
op|'.'
name|'Connection'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'myself'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'super'
op|'('
name|'MyConnection'
op|','
name|'myself'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'myself'
op|'.'
name|'params'
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'server_params'
op|'['
string|"'hostname'"
op|']'
op|','
nl|'\n'
string|"'userid'"
op|':'
name|'server_params'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'server_params'
op|'['
string|"'password'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'server_params'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
name|'server_params'
op|'['
string|"'virtual_host'"
op|']'
op|','
nl|'\n'
string|"'transport'"
op|':'
string|"'memory'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|topic_send
dedent|''
name|'def'
name|'topic_send'
op|'('
name|'_context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'MyConnection'
op|'.'
name|'pool'
op|'='
name|'rpc_amqp'
op|'.'
name|'Pool'
op|'('
name|'connection_cls'
op|'='
name|'MyConnection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'impl_kombu'
op|','
string|"'Connection'"
op|','
name|'MyConnection'
op|')'
newline|'\n'
nl|'\n'
name|'impl_kombu'
op|'.'
name|'cast_to_server'
op|'('
name|'ctxt'
op|','
name|'server_params'
op|','
nl|'\n'
string|"'fake_topic'"
op|','
op|'{'
string|"'msg'"
op|':'
string|"'fake'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"kombu memory transport seems buggy with fanout queues "'
nl|'\n'
string|'"as this test passes when you use rabbit (fake_rabbit=False)"'
op|')'
newline|'\n'
DECL|member|test_fanout_send_receive
name|'def'
name|'test_fanout_send_receive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test sending to a fanout exchange and consuming from 2 queues"""'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'conn2'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
string|"'fanout test message'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'received_message'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_callback
name|'def'
name|'_callback'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'received_message'
op|'='
name|'message'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'.'
name|'declare_fanout_consumer'
op|'('
string|"'a_fanout'"
op|','
name|'_callback'
op|')'
newline|'\n'
name|'conn2'
op|'.'
name|'declare_fanout_consumer'
op|'('
string|"'a_fanout'"
op|','
name|'_callback'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'fanout_send'
op|'('
string|"'a_fanout'"
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'.'
name|'consume'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'received_message'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'received_message'
op|'='
name|'None'
newline|'\n'
name|'conn2'
op|'.'
name|'consume'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'conn2'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'received_message'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_declare_consumer_errors_will_reconnect
dedent|''
name|'def'
name|'test_declare_consumer_errors_will_reconnect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Test that any exception with 'timeout' in it causes a"
nl|'\n'
comment|'# reconnection'
nl|'\n'
indent|'        '
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'2'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|','
nl|'\n'
string|"'__init__'"
op|','
string|"'foo timeout foo'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'declare_consumer'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|','
nl|'\n'
string|"'test_topic'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'result'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test that any exception in transport.connection_errors causes'
nl|'\n'
comment|'# a reconnection'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|','
nl|'\n'
string|"'__init__'"
op|','
string|"'meow'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'connection_errors'
op|'='
op|'('
name|'MyException'
op|','
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'declare_consumer'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|','
nl|'\n'
string|"'test_topic'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'result'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectConsumer'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_publishing_errors_will_reconnect
dedent|''
name|'def'
name|'test_publishing_errors_will_reconnect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Test that any exception with 'timeout' in it causes a"
nl|'\n'
comment|'# reconnection when declaring the publisher class and when'
nl|'\n'
comment|'# calling send()'
nl|'\n'
indent|'        '
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'2'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
nl|'\n'
string|"'__init__'"
op|','
string|"'foo timeout foo'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'publisher_send'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
string|"'test_topic'"
op|','
string|"'msg'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'2'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
nl|'\n'
string|"'send'"
op|','
string|"'foo timeout foo'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'publisher_send'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
string|"'test_topic'"
op|','
string|"'msg'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test that any exception in transport.connection_errors causes'
nl|'\n'
comment|'# a reconnection when declaring the publisher class and when'
nl|'\n'
comment|'# calling send()'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
nl|'\n'
string|"'__init__'"
op|','
string|"'meow'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'connection_errors'
op|'='
op|'('
name|'MyException'
op|','
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'.'
name|'publisher_send'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
string|"'test_topic'"
op|','
string|"'msg'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
nl|'\n'
string|"'send'"
op|','
string|"'meow'"
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'connection_errors'
op|'='
op|'('
name|'MyException'
op|','
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'.'
name|'publisher_send'
op|'('
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'DirectPublisher'
op|','
string|"'test_topic'"
op|','
string|"'msg'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_iterconsume_errors_will_reconnect
dedent|''
name|'def'
name|'test_iterconsume_errors_will_reconnect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'self'
op|'.'
name|'rpc'
op|'.'
name|'Connection'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
string|"'reconnect test message'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'received_message'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_callback
name|'def'
name|'_callback'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'received_message'
op|'='
name|'message'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'.'
name|'declare_direct_consumer'
op|'('
string|"'a_direct'"
op|','
name|'_callback'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'direct_send'
op|'('
string|"'a_direct'"
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'_raise_exc_stub'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
name|'conn'
op|'.'
name|'connection'
op|','
nl|'\n'
string|"'drain_events'"
op|','
string|"'foo timeout foo'"
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'consume'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'received_message'
op|','
name|'message'
op|')'
newline|'\n'
comment|'# Only called once, because our stub goes away during reconnection'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
