begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'pause_server'
name|'as'
name|'pause_server_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'admin_only_action_common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PauseServerTestsV21
name|'class'
name|'PauseServerTestsV21'
op|'('
name|'admin_only_action_common'
op|'.'
name|'CommonTests'
op|')'
op|':'
newline|'\n'
DECL|variable|pause_server
indent|'    '
name|'pause_server'
op|'='
name|'pause_server_v21'
newline|'\n'
DECL|variable|controller_name
name|'controller_name'
op|'='
string|"'PauseServerController'"
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'2.1'"
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
name|'PauseServerTestsV21'
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
name|'controller'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'pause_server'
op|','
name|'self'
op|'.'
name|'controller_name'
op|')'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
newline|'\n'
nl|'\n'
DECL|function|_fake_controller
name|'def'
name|'_fake_controller'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'pause_server'
op|','
name|'self'
op|'.'
name|'controller_name'
op|','
nl|'\n'
name|'_fake_controller'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_unpause
dedent|''
name|'def'
name|'test_pause_unpause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_actions'
op|'('
op|'['
string|"'_pause'"
op|','
string|"'_unpause'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_actions_raise_on_not_implemented
dedent|''
name|'def'
name|'test_actions_raise_on_not_implemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'action'
name|'in'
op|'['
string|"'_pause'"
op|','
string|"'_unpause'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
name|'action'
op|'.'
name|'replace'
op|'('
string|"'_'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_not_implemented_state'
op|'('
name|'action'
op|')'
newline|'\n'
comment|'# Re-mock this.'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_unpause_with_non_existed_instance
dedent|''
dedent|''
name|'def'
name|'test_pause_unpause_with_non_existed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_actions_with_non_existed_instance'
op|'('
op|'['
string|"'_pause'"
op|','
string|"'_unpause'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_unpause_with_non_existed_instance_in_compute_api
dedent|''
name|'def'
name|'test_pause_unpause_with_non_existed_instance_in_compute_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_actions_instance_not_found_in_compute_api'
op|'('
op|'['
string|"'_pause'"
op|','
nl|'\n'
string|"'_unpause'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_unpause_raise_conflict_on_invalid_state
dedent|''
name|'def'
name|'test_pause_unpause_raise_conflict_on_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_actions_raise_conflict_on_invalid_state'
op|'('
op|'['
string|"'_pause'"
op|','
nl|'\n'
string|"'_unpause'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_actions_with_locked_instance
dedent|''
name|'def'
name|'test_actions_with_locked_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_actions_with_locked_instance'
op|'('
op|'['
string|"'_pause'"
op|','
string|"'_unpause'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PauseServerPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'PauseServerPolicyEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'super'
op|'('
name|'PauseServerPolicyEnforcementV21'
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
name|'controller'
op|'='
name|'pause_server_v21'
op|'.'
name|'PauseServerController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_policy_failed
dedent|''
name|'def'
name|'test_pause_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-pause-server:pause"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
string|"''"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_pause'
op|','
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'pause'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unpause_policy_failed
dedent|''
name|'def'
name|'test_unpause_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-pause-server:unpause"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
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
string|"''"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unpause'
op|','
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'unpause'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
