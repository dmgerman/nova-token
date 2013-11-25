begin_unit
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
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'lock_server'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
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
name|'admin_only_action_common'
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
DECL|class|LockServerTests
name|'class'
name|'LockServerTests'
op|'('
name|'admin_only_action_common'
op|'.'
name|'CommonTests'
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
name|'super'
op|'('
name|'LockServerTests'
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
name|'lock_server'
op|'.'
name|'LockServerController'
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
name|'lock_server'
op|','
string|"'LockServerController'"
op|','
nl|'\n'
name|'_fake_controller'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-lock-server'"
op|')'
op|','
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'context'
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
DECL|member|test_lock_unlock
dedent|''
name|'def'
name|'test_lock_unlock'
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
string|"'lock'"
op|','
string|"'unlock'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lock_unlock_with_non_existed_instance
dedent|''
name|'def'
name|'test_lock_unlock_with_non_existed_instance'
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
string|"'lock'"
op|','
string|"'unlock'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlock_not_authorized
dedent|''
name|'def'
name|'test_unlock_not_authorized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'unlock'"
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unlock'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
name|'action'
op|'='
string|"'unlock'"
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
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
string|"'/servers/%s/action'"
op|'%'
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
op|'{'
string|"'unlock'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'403'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
