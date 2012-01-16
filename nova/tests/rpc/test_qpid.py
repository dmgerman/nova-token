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
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nUnit Tests for remote procedure calls using qpid\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
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
name|'log'
name|'as'
name|'logging'
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
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'qpid'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'impl_qpid'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|qpid
indent|'    '
name|'qpid'
op|'='
name|'None'
newline|'\n'
DECL|variable|impl_qpid
name|'impl_qpid'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
dedent|''
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
DECL|class|RpcQpidTestCase
name|'class'
name|'RpcQpidTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Exercise the public API of impl_qpid utilizing mox.\n\n    This set of tests utilizes mox to replace the Qpid objects and ensures\n    that the right operations happen on them when the various public rpc API\n    calls are exercised.  The API calls tested here include:\n\n        nova.rpc.create_connection()\n        nova.rpc.common.Connection.create_consumer()\n        nova.rpc.common.Connection.close()\n        nova.rpc.cast()\n        nova.rpc.fanout_cast()\n        nova.rpc.call()\n        nova.rpc.multicall()\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'mocker'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mock_sender'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'if'
name|'qpid'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'orig_connection'
op|'='
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Connection'
newline|'\n'
name|'self'
op|'.'
name|'orig_session'
op|'='
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Session'
newline|'\n'
name|'self'
op|'.'
name|'orig_sender'
op|'='
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Sender'
newline|'\n'
name|'self'
op|'.'
name|'orig_receiver'
op|'='
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Receiver'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Connection'
op|'='
name|'lambda'
op|'*'
name|'_x'
op|','
op|'**'
name|'_y'
op|':'
name|'self'
op|'.'
name|'mock_connection'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Session'
op|'='
name|'lambda'
op|'*'
name|'_x'
op|','
op|'**'
name|'_y'
op|':'
name|'self'
op|'.'
name|'mock_session'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Sender'
op|'='
name|'lambda'
op|'*'
name|'_x'
op|','
op|'**'
name|'_y'
op|':'
name|'self'
op|'.'
name|'mock_sender'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Receiver'
op|'='
name|'lambda'
op|'*'
name|'_x'
op|','
op|'**'
name|'_y'
op|':'
name|'self'
op|'.'
name|'mock_receiver'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'RpcQpidTestCase'
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
name|'if'
name|'qpid'
op|':'
newline|'\n'
indent|'            '
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Connection'
op|'='
name|'self'
op|'.'
name|'orig_connection'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Session'
op|'='
name|'self'
op|'.'
name|'orig_session'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Sender'
op|'='
name|'self'
op|'.'
name|'orig_sender'
newline|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Receiver'
op|'='
name|'self'
op|'.'
name|'orig_receiver'
newline|'\n'
dedent|''
name|'if'
name|'impl_qpid'
op|':'
newline|'\n'
comment|'# Need to reset this in case we changed the connection_cls'
nl|'\n'
comment|'# in self._setup_to_server_tests()'
nl|'\n'
indent|'            '
name|'impl_qpid'
op|'.'
name|'Connection'
op|'.'
name|'pool'
op|'.'
name|'connection_cls'
op|'='
name|'impl_qpid'
op|'.'
name|'Connection'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'RpcQpidTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_create_connection
name|'def'
name|'test_create_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_connection'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_session'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'opened'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'open'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'connection'
op|'='
name|'impl_qpid'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_consumer
dedent|''
name|'def'
name|'_test_create_consumer'
op|'('
name|'self'
op|','
name|'fanout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_connection'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_receiver'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'opened'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'open'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
name|'if'
name|'fanout'
op|':'
newline|'\n'
comment|'# The link name includes a UUID, so match it with a regex.'
nl|'\n'
indent|'            '
name|'expected_address'
op|'='
name|'mox'
op|'.'
name|'Regex'
op|'('
string|"r'^impl_qpid_test_fanout ; '"
nl|'\n'
string|'\'{"node": {"x-declare": {"auto-delete": true, "durable": \''
nl|'\n'
string|'\'false, "type": "fanout"}, "type": "topic"}, "create": \''
nl|'\n'
string|'\'"always", "link": {"x-declare": {"auto-delete": true, \''
nl|'\n'
string|'\'"exclusive": true, "durable": false}, "durable": true, \''
nl|'\n'
string|'\'"name": "impl_qpid_test_fanout_.*"}}$\''
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'expected_address'
op|'='
op|'('
string|'\'nova/impl_qpid_test ; {"node": {"x-declare": \''
nl|'\n'
string|'\'{"auto-delete": true, "durable": true}, "type": "topic"}, \''
nl|'\n'
string|'\'"create": "always", "link": {"x-declare": {"auto-delete": \''
nl|'\n'
string|'\'true, "exclusive": false, "durable": false}, "durable": \''
nl|'\n'
string|'\'true, "name": "impl_qpid_test"}}\''
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'receiver'
op|'('
name|'expected_address'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'capacity'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'connection'
op|'='
name|'impl_qpid'
op|'.'
name|'create_connection'
op|'('
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'create_consumer'
op|'('
string|'"impl_qpid_test"'
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'_x'
op|','
op|'**'
name|'_y'
op|':'
name|'None'
op|','
nl|'\n'
name|'fanout'
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_create_consumer
name|'def'
name|'test_create_consumer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_consumer'
op|'('
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_create_consumer_fanout
name|'def'
name|'test_create_consumer_fanout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_consumer'
op|'('
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_cast
dedent|''
name|'def'
name|'_test_cast'
op|'('
name|'self'
op|','
name|'fanout'
op|','
name|'server_params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_connection'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_sender'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_sender'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'opened'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'open'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
name|'if'
name|'fanout'
op|':'
newline|'\n'
indent|'            '
name|'expected_address'
op|'='
op|'('
string|"'impl_qpid_test_fanout ; '"
nl|'\n'
string|'\'{"node": {"x-declare": {"auto-delete": true, \''
nl|'\n'
string|'\'"durable": false, "type": "fanout"}, \''
nl|'\n'
string|'\'"type": "topic"}, "create": "always"}\''
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'expected_address'
op|'='
op|'('
string|'\'nova/impl_qpid_test ; {"node": {"x-declare": \''
nl|'\n'
string|'\'{"auto-delete": true, "durable": false}, "type": "topic"}, \''
nl|'\n'
string|'\'"create": "always"}\''
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'sender'
op|'('
name|'expected_address'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_sender'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_sender'
op|'.'
name|'send'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'server_params'
op|':'
newline|'\n'
comment|'# This is a pooled connection, so instead of closing it, it'
nl|'\n'
comment|'# gets reset, which is just creating a new session on the'
nl|'\n'
comment|'# connection.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|'"user"'
op|','
string|'"project"'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'['
name|'ctx'
op|','
string|'"impl_qpid_test"'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"test_method"'
op|','
string|'"args"'
op|':'
op|'{'
op|'}'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'server_params'
op|':'
newline|'\n'
indent|'                '
name|'args'
op|'.'
name|'insert'
op|'('
number|'1'
op|','
name|'server_params'
op|')'
newline|'\n'
name|'if'
name|'fanout'
op|':'
newline|'\n'
indent|'                    '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'fanout_cast_to_server'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'cast_to_server'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'fanout'
op|':'
newline|'\n'
indent|'                    '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'fanout_cast'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'cast'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'method'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'impl_qpid'
op|'.'
name|'Connection'
op|'.'
name|'pool'
op|'.'
name|'free_items'
op|':'
newline|'\n'
comment|'# Pull the mock connection object out of the connection pool so'
nl|'\n'
comment|"# that it doesn't mess up other test cases."
nl|'\n'
indent|'                '
name|'impl_qpid'
op|'.'
name|'Connection'
op|'.'
name|'pool'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_cast
name|'def'
name|'test_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_cast'
op|'('
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_fanout_cast
name|'def'
name|'test_fanout_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_cast'
op|'('
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_to_server_tests
dedent|''
name|'def'
name|'_setup_to_server_tests'
op|'('
name|'self'
op|','
name|'server_params'
op|')'
op|':'
newline|'\n'
DECL|class|MyConnection
indent|'        '
name|'class'
name|'MyConnection'
op|'('
name|'impl_qpid'
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
name|'connection'
op|'.'
name|'username'
op|','
nl|'\n'
name|'server_params'
op|'['
string|"'username'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'myself'
op|'.'
name|'connection'
op|'.'
name|'password'
op|','
nl|'\n'
name|'server_params'
op|'['
string|"'password'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'myself'
op|'.'
name|'broker'
op|','
nl|'\n'
name|'server_params'
op|'['
string|"'hostname'"
op|']'
op|'+'
string|"':'"
op|'+'
nl|'\n'
name|'str'
op|'('
name|'server_params'
op|'['
string|"'port'"
op|']'
op|')'
op|')'
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
name|'impl_qpid'
op|','
string|"'Connection'"
op|','
name|'MyConnection'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_cast_to_server
name|'def'
name|'test_cast_to_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_setup_to_server_tests'
op|'('
name|'server_params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_cast'
op|'('
name|'fanout'
op|'='
name|'False'
op|','
name|'server_params'
op|'='
name|'server_params'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_fanout_cast_to_server
name|'def'
name|'test_fanout_cast_to_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_setup_to_server_tests'
op|'('
name|'server_params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_cast'
op|'('
name|'fanout'
op|'='
name|'True'
op|','
name|'server_params'
op|'='
name|'server_params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_call
dedent|''
name|'def'
name|'_test_call'
op|'('
name|'self'
op|','
name|'multi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_connection'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_sender'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_sender'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'='
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'CreateMock'
op|'('
name|'self'
op|'.'
name|'orig_receiver'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'opened'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'open'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
name|'rcv_addr'
op|'='
name|'mox'
op|'.'
name|'Regex'
op|'('
string|'r\'^.*/.* ; {"node": {"x-declare": {"auto-delete":\''
nl|'\n'
string|'\' true, "durable": true, "type": "direct"}, "type": \''
nl|'\n'
string|'\'"topic"}, "create": "always", "link": {"x-declare": \''
nl|'\n'
string|'\'{"auto-delete": true, "exclusive": true, "durable": \''
nl|'\n'
string|'\'false}, "durable": true, "name": ".*"}}\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'receiver'
op|'('
name|'rcv_addr'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'capacity'
op|'='
number|'1'
newline|'\n'
name|'send_addr'
op|'='
op|'('
string|'\'nova/impl_qpid_test ; {"node": {"x-declare": \''
nl|'\n'
string|'\'{"auto-delete": true, "durable": false}, "type": "topic"}, \''
nl|'\n'
string|'\'"create": "always"}\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'sender'
op|'('
name|'send_addr'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_sender'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_sender'
op|'.'
name|'send'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'next_receiver'
op|'('
name|'timeout'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'int'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'fetch'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Message'
op|'('
nl|'\n'
op|'{'
string|'"result"'
op|':'
string|'"foo"'
op|','
string|'"failure"'
op|':'
name|'False'
op|','
string|'"ending"'
op|':'
name|'False'
op|'}'
op|')'
op|')'
newline|'\n'
name|'if'
name|'multi'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'next_receiver'
op|'('
name|'timeout'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'int'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'fetch'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Message'
op|'('
nl|'\n'
op|'{'
string|'"result"'
op|':'
string|'"bar"'
op|','
string|'"failure"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"ending"'
op|':'
name|'False'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'next_receiver'
op|'('
name|'timeout'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'int'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'fetch'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Message'
op|'('
nl|'\n'
op|'{'
string|'"result"'
op|':'
string|'"baz"'
op|','
string|'"failure"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"ending"'
op|':'
name|'False'
op|'}'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'next_receiver'
op|'('
name|'timeout'
op|'='
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'int'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_receiver'
op|'.'
name|'fetch'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'qpid'
op|'.'
name|'messaging'
op|'.'
name|'Message'
op|'('
nl|'\n'
op|'{'
string|'"failure"'
op|':'
name|'False'
op|','
string|'"ending"'
op|':'
name|'True'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_session'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_connection'
op|'.'
name|'session'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'mock_session'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|'"user"'
op|','
string|'"project"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'multi'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'multicall'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|'='
name|'impl_qpid'
op|'.'
name|'call'
newline|'\n'
nl|'\n'
dedent|''
name|'res'
op|'='
name|'method'
op|'('
name|'ctx'
op|','
string|'"impl_qpid_test"'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"test_method"'
op|','
string|'"args"'
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'multi'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'list'
op|'('
name|'res'
op|')'
op|','
op|'['
string|'"foo"'
op|','
string|'"bar"'
op|','
string|'"baz"'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'res'
op|','
string|'"foo"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mocker'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'impl_qpid'
op|'.'
name|'Connection'
op|'.'
name|'pool'
op|'.'
name|'free_items'
op|':'
newline|'\n'
comment|'# Pull the mock connection object out of the connection pool so'
nl|'\n'
comment|"# that it doesn't mess up other test cases."
nl|'\n'
indent|'                '
name|'impl_qpid'
op|'.'
name|'Connection'
op|'.'
name|'pool'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_call
name|'def'
name|'test_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_call'
op|'('
name|'multi'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'qpid'
name|'is'
name|'None'
op|','
string|'"Test requires qpid"'
op|')'
newline|'\n'
DECL|member|test_multicall
name|'def'
name|'test_multicall'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_call'
op|'('
name|'multi'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#from nova.tests.rpc import common'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# Qpid does not have a handy in-memory transport like kombu, so it's not"
nl|'\n'
comment|'# terribly straight forward to take advantage of the common unit tests.'
nl|'\n'
comment|'# However, at least at the time of this writing, the common unit tests all pass'
nl|'\n'
comment|'# with qpidd running.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# class RpcQpidCommonTestCase(common._BaseRpcTestCase):'
nl|'\n'
comment|'#     def setUp(self):'
nl|'\n'
comment|'#         self.rpc = impl_qpid'
nl|'\n'
comment|'#         super(RpcQpidCommonTestCase, self).setUp()'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     def tearDown(self):'
nl|'\n'
comment|'#         super(RpcQpidCommonTestCase, self).tearDown()'
nl|'\n'
comment|'#'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
