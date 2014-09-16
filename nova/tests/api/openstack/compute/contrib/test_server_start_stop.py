begin_unit
comment|'# Copyright (c) 2012 Midokura Japan K.K.'
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
name|'mox'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'server_start_stop'
name|'as'
name|'server_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'plugins'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'servers'
name|'as'
name|'server_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'policy'
name|'as'
name|'common_policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get
name|'def'
name|'fake_instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'uuid'
op|'='
name|'instance_id'
op|')'
newline|'\n'
name|'result'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'result'
op|'['
string|"'deleted_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'result'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'result'
op|'['
string|"'deleted'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'result'
op|'['
string|"'info_cache'"
op|']'
op|'='
op|'{'
string|"'network_info'"
op|':'
string|"'[]'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'result'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_start_stop_not_ready
dedent|''
name|'def'
name|'fake_start_stop_not_ready'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotReady'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_start_stop_locked_server
dedent|''
name|'def'
name|'fake_start_stop_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_start_stop_invalid_state
dedent|''
name|'def'
name|'fake_start_stop_invalid_state'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerStartStopTestV21
dedent|''
name|'class'
name|'ServerStartStopTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|start_policy
indent|'    '
name|'start_policy'
op|'='
string|'"compute:v3:servers:start"'
newline|'\n'
DECL|variable|stop_policy
name|'stop_policy'
op|'='
string|'"compute:v3:servers:stop"'
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
name|'ServerStartStopTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_controller'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
dedent|''
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'server_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start
dedent|''
name|'def'
name|'test_start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'start'"
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'start'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|'('
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_policy_failed
dedent|''
name|'def'
name|'test_start_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
nl|'\n'
name|'self'
op|'.'
name|'start_policy'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|'"project_id:non_fake"'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|','
nl|'\n'
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'self'
op|'.'
name|'start_policy'
op|','
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_not_ready
dedent|''
name|'def'
name|'test_start_not_ready'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'start'"
op|','
name|'fake_start_stop_not_ready'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_locked_server
dedent|''
name|'def'
name|'test_start_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'start'"
op|','
name|'fake_start_stop_locked_server'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_invalid_state
dedent|''
name|'def'
name|'test_start_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'start'"
op|','
name|'fake_start_stop_invalid_state'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop
dedent|''
name|'def'
name|'test_stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'stop'"
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'stop'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'stop'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|'('
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_policy_failed
dedent|''
name|'def'
name|'test_stop_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
nl|'\n'
name|'self'
op|'.'
name|'stop_policy'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|'"project_id:non_fake"'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'stop'
op|'='
string|'""'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|','
nl|'\n'
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'self'
op|'.'
name|'stop_policy'
op|','
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_not_ready
dedent|''
name|'def'
name|'test_stop_not_ready'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'stop'"
op|','
name|'fake_start_stop_not_ready'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'stop'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_locked_server
dedent|''
name|'def'
name|'test_stop_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'stop'"
op|','
name|'fake_start_stop_locked_server'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'stop'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_invalid_state
dedent|''
name|'def'
name|'test_stop_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'stop'"
op|','
name|'fake_start_stop_invalid_state'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_with_bogus_id
dedent|''
name|'def'
name|'test_start_with_bogus_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'start'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_start_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_with_bogus_id
dedent|''
name|'def'
name|'test_stop_with_bogus_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'stop'
op|'='
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_stop_server'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerStartStopTestV2
dedent|''
dedent|''
name|'class'
name|'ServerStartStopTestV2'
op|'('
name|'ServerStartStopTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|start_policy
indent|'    '
name|'start_policy'
op|'='
string|'"compute:start"'
newline|'\n'
DECL|variable|stop_policy
name|'stop_policy'
op|'='
string|'"compute:stop"'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'server_v2'
op|'.'
name|'ServerStartStopActionController'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
