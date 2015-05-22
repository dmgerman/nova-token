begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""\nTests For Cells RPC Communication Driver\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'oslo_messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'rpc_driver'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'cells'
name|'import'
name|'fakes'
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
name|'import_opt'
op|'('
string|"'rpc_driver_queue_base'"
op|','
string|"'nova.cells.rpc_driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsRPCDriverTestCase
name|'class'
name|'CellsRPCDriverTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Cells communication via RPC."""'
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
name|'super'
op|'('
name|'CellsRPCDriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'init'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'rpc_driver'
op|'.'
name|'CellsRPCDriver'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_servers
dedent|''
name|'def'
name|'test_start_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'rpc_driver_queue_base'
op|'='
string|"'cells.intercell42'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'fake_msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeInterCellRPCDispatcher
name|'class'
name|'FakeInterCellRPCDispatcher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'_self'
op|','
name|'msg_runner'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_msg_runner'
op|','
name|'msg_runner'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc_driver'
op|','
string|"'InterCellRPCDispatcher'"
op|','
nl|'\n'
name|'FakeInterCellRPCDispatcher'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'get_server'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'message_type'
name|'in'
name|'messaging'
op|'.'
name|'MessageRunner'
op|'.'
name|'get_message_types'
op|'('
op|')'
op|':'
newline|'\n'
DECL|variable|topic
indent|'            '
name|'topic'
op|'='
string|"'cells.intercell42.'"
op|'+'
name|'message_type'
newline|'\n'
DECL|variable|target
name|'target'
op|'='
name|'oslo_messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'topic'
op|','
name|'server'
op|'='
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
DECL|variable|endpoints
name|'endpoints'
op|'='
op|'['
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'FakeInterCellRPCDispatcher'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|rpcserver
name|'rpcserver'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'get_server'
op|'('
name|'target'
op|','
name|'endpoints'
op|'='
name|'endpoints'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcserver'
op|')'
newline|'\n'
name|'rpcserver'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'start_servers'
op|'('
name|'fake_msg_runner'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_servers
dedent|''
name|'def'
name|'test_stop_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'call_info'
op|'='
op|'{'
string|"'stopped'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|FakeRPCServer
name|'class'
name|'FakeRPCServer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|stop
indent|'            '
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'call_info'
op|'['
string|"'stopped'"
op|']'
op|'.'
name|'append'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'fake_servers'
op|'='
op|'['
name|'FakeRPCServer'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'rpc_servers'
op|'='
name|'fake_servers'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'stop_servers'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_servers'
op|','
name|'call_info'
op|'['
string|"'stopped'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_transport_once
dedent|''
name|'def'
name|'test_create_transport_once'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# should only construct each Transport once'
nl|'\n'
indent|'        '
name|'rpcapi'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'intercell_rpcapi'
newline|'\n'
nl|'\n'
name|'transport_url'
op|'='
string|"'amqp://fakeurl'"
newline|'\n'
name|'next_hop'
op|'='
name|'fakes'
op|'.'
name|'FakeCellState'
op|'('
string|"'cellname'"
op|')'
newline|'\n'
name|'next_hop'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
op|'='
name|'transport_url'
newline|'\n'
nl|'\n'
comment|'# first call to _get_transport creates a oslo.messaging.Transport obj'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'oslo_messaging'
op|','
string|"'get_transport'"
op|')'
name|'as'
name|'get_trans'
op|':'
newline|'\n'
indent|'            '
name|'transport'
op|'='
name|'rpcapi'
op|'.'
name|'_get_transport'
op|'('
name|'next_hop'
op|')'
newline|'\n'
name|'get_trans'
op|'.'
name|'assert_called_once_with'
op|'('
name|'rpc_driver'
op|'.'
name|'CONF'
op|','
name|'transport_url'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'TRANSPORT_ALIASES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'transport_url'
op|','
name|'rpcapi'
op|'.'
name|'transports'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'transport'
op|','
name|'rpcapi'
op|'.'
name|'transports'
op|'['
name|'transport_url'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# subsequent calls should return the pre-created Transport obj'
nl|'\n'
dedent|''
name|'transport2'
op|'='
name|'rpcapi'
op|'.'
name|'_get_transport'
op|'('
name|'next_hop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'transport'
op|','
name|'transport2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_message_to_cell_cast
dedent|''
name|'def'
name|'test_send_message_to_cell_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
name|'cell_state'
op|'='
name|'fakes'
op|'.'
name|'get_cell_state'
op|'('
string|"'api-cell'"
op|','
string|"'child-cell2'"
op|')'
newline|'\n'
name|'message'
op|'='
name|'messaging'
op|'.'
name|'_TargetedMessage'
op|'('
name|'msg_runner'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake'"
op|','
op|'{'
op|'}'
op|','
string|"'down'"
op|','
name|'cell_state'
op|','
name|'fanout'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'expected_server_params'
op|'='
op|'{'
string|"'hostname'"
op|':'
string|"'rpc_host2'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'password2'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'3092'
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'username2'"
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
string|"'rpc_vhost2'"
op|'}'
newline|'\n'
name|'expected_url'
op|'='
op|'('
string|"'rabbit://%(username)s:%(password)s@'"
nl|'\n'
string|"'%(hostname)s:%(port)d/%(virtual_host)s'"
op|'%'
nl|'\n'
name|'expected_server_params'
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_transport_url
name|'def'
name|'check_transport_url'
op|'('
name|'cell_state'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cell_state'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
op|'=='
name|'expected_url'
newline|'\n'
nl|'\n'
dedent|''
name|'rpcapi'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'intercell_rpcapi'
newline|'\n'
name|'rpcclient'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpcapi'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
name|'rpcapi'
op|'.'
name|'_get_client'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'Func'
op|'('
name|'check_transport_url'
op|')'
op|','
nl|'\n'
string|"'cells.intercell.targeted'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcclient'
op|')'
newline|'\n'
nl|'\n'
name|'rpcclient'
op|'.'
name|'cast'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'process_message'"
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'send_message_to_cell'
op|'('
name|'cell_state'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_message_to_cell_fanout_cast
dedent|''
name|'def'
name|'test_send_message_to_cell_fanout_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
name|'cell_state'
op|'='
name|'fakes'
op|'.'
name|'get_cell_state'
op|'('
string|"'api-cell'"
op|','
string|"'child-cell2'"
op|')'
newline|'\n'
name|'message'
op|'='
name|'messaging'
op|'.'
name|'_TargetedMessage'
op|'('
name|'msg_runner'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake'"
op|','
op|'{'
op|'}'
op|','
string|"'down'"
op|','
name|'cell_state'
op|','
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'expected_server_params'
op|'='
op|'{'
string|"'hostname'"
op|':'
string|"'rpc_host2'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'password2'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'3092'
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'username2'"
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
string|"'rpc_vhost2'"
op|'}'
newline|'\n'
name|'expected_url'
op|'='
op|'('
string|"'rabbit://%(username)s:%(password)s@'"
nl|'\n'
string|"'%(hostname)s:%(port)d/%(virtual_host)s'"
op|'%'
nl|'\n'
name|'expected_server_params'
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_transport_url
name|'def'
name|'check_transport_url'
op|'('
name|'cell_state'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cell_state'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
op|'=='
name|'expected_url'
newline|'\n'
nl|'\n'
dedent|''
name|'rpcapi'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'intercell_rpcapi'
newline|'\n'
name|'rpcclient'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpcapi'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
name|'rpcapi'
op|'.'
name|'_get_client'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'Func'
op|'('
name|'check_transport_url'
op|')'
op|','
nl|'\n'
string|"'cells.intercell.targeted'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcclient'
op|')'
newline|'\n'
nl|'\n'
name|'rpcclient'
op|'.'
name|'prepare'
op|'('
name|'fanout'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcclient'
op|')'
newline|'\n'
name|'rpcclient'
op|'.'
name|'cast'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'process_message'"
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'send_message_to_cell'
op|'('
name|'cell_state'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rpc_topic_uses_message_type
dedent|''
name|'def'
name|'test_rpc_topic_uses_message_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'rpc_driver_queue_base'
op|'='
string|"'cells.intercell42'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
name|'cell_state'
op|'='
name|'fakes'
op|'.'
name|'get_cell_state'
op|'('
string|"'api-cell'"
op|','
string|"'child-cell2'"
op|')'
newline|'\n'
name|'message'
op|'='
name|'messaging'
op|'.'
name|'_BroadcastMessage'
op|'('
name|'msg_runner'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake'"
op|','
op|'{'
op|'}'
op|','
string|"'down'"
op|','
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
name|'message'
op|'.'
name|'message_type'
op|'='
string|"'fake-message-type'"
newline|'\n'
nl|'\n'
name|'expected_server_params'
op|'='
op|'{'
string|"'hostname'"
op|':'
string|"'rpc_host2'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'password2'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'3092'
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'username2'"
op|','
nl|'\n'
string|"'virtual_host'"
op|':'
string|"'rpc_vhost2'"
op|'}'
newline|'\n'
name|'expected_url'
op|'='
op|'('
string|"'rabbit://%(username)s:%(password)s@'"
nl|'\n'
string|"'%(hostname)s:%(port)d/%(virtual_host)s'"
op|'%'
nl|'\n'
name|'expected_server_params'
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_transport_url
name|'def'
name|'check_transport_url'
op|'('
name|'cell_state'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cell_state'
op|'.'
name|'db_info'
op|'['
string|"'transport_url'"
op|']'
op|'=='
name|'expected_url'
newline|'\n'
nl|'\n'
dedent|''
name|'rpcapi'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'intercell_rpcapi'
newline|'\n'
name|'rpcclient'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpcapi'
op|','
string|"'_get_client'"
op|')'
newline|'\n'
name|'rpcapi'
op|'.'
name|'_get_client'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'Func'
op|'('
name|'check_transport_url'
op|')'
op|','
nl|'\n'
string|"'cells.intercell42.fake-message-type'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcclient'
op|')'
newline|'\n'
nl|'\n'
name|'rpcclient'
op|'.'
name|'prepare'
op|'('
name|'fanout'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcclient'
op|')'
newline|'\n'
name|'rpcclient'
op|'.'
name|'cast'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'process_message'"
op|','
nl|'\n'
name|'message'
op|'='
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'send_message_to_cell'
op|'('
name|'cell_state'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_process_message
dedent|''
name|'def'
name|'test_process_message'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg_runner'
op|'='
name|'fakes'
op|'.'
name|'get_message_runner'
op|'('
string|"'api-cell'"
op|')'
newline|'\n'
name|'dispatcher'
op|'='
name|'rpc_driver'
op|'.'
name|'InterCellRPCDispatcher'
op|'('
name|'msg_runner'
op|')'
newline|'\n'
name|'message'
op|'='
name|'messaging'
op|'.'
name|'_BroadcastMessage'
op|'('
name|'msg_runner'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
string|"'fake'"
op|','
op|'{'
op|'}'
op|','
string|"'down'"
op|','
name|'fanout'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'call_info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_fake_message_from_json
name|'def'
name|'_fake_message_from_json'
op|'('
name|'json_message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'call_info'
op|'['
string|"'json_message'"
op|']'
op|'='
name|'json_message'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|','
name|'json_message'
op|')'
newline|'\n'
name|'return'
name|'message'
newline|'\n'
nl|'\n'
DECL|function|_fake_process
dedent|''
name|'def'
name|'_fake_process'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'call_info'
op|'['
string|"'process_called'"
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'msg_runner'
op|','
string|"'message_from_json'"
op|','
nl|'\n'
name|'_fake_message_from_json'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'message'
op|','
string|"'process'"
op|','
name|'_fake_process'
op|')'
newline|'\n'
nl|'\n'
name|'dispatcher'
op|'.'
name|'process_message'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'message'
op|'.'
name|'to_json'
op|'('
op|')'
op|','
name|'call_info'
op|'['
string|"'json_message'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'call_info'
op|'['
string|"'process_called'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
