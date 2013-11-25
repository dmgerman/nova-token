begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
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
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
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
name|'import'
name|'fake_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommonMixin
name|'class'
name|'CommonMixin'
op|'('
name|'object'
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
name|'CommonMixin'
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
name|'compute_api'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_request
dedent|''
name|'def'
name|'_make_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3'"
op|'+'
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_instance_get
dedent|''
name|'def'
name|'_stub_instance_get'
op|'('
name|'self'
op|','
name|'uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'uuid'
op|'='
name|'uuid'
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'None'
op|','
name|'launched_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|_stub_instance_get_failure
dedent|''
name|'def'
name|'_stub_instance_get_failure'
op|'('
name|'self'
op|','
name|'exc_info'
op|','
name|'uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'uuid'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exc_info'
op|')'
newline|'\n'
name|'return'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|_test_non_existing_instance
dedent|''
name|'def'
name|'_test_non_existing_instance'
op|'('
name|'self'
op|','
name|'action'
op|','
name|'body_map'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'uuidutils'
op|'.'
name|'generate_uuid'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_instance_get_failure'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'uuid'
op|')'
op|','
name|'uuid'
op|'='
name|'uuid'
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
name|'uuid'
op|','
nl|'\n'
op|'{'
name|'action'
op|':'
name|'body_map'
op|'.'
name|'get'
op|'('
name|'action'
op|')'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
comment|'# Do these here instead of tearDown because this method is called'
nl|'\n'
comment|'# more than once for the same test case'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_action
dedent|''
name|'def'
name|'_test_action'
op|'('
name|'self'
op|','
name|'action'
op|','
name|'body'
op|'='
name|'None'
op|','
name|'method'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'method'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'action'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'method'
op|')'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
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
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
name|'action'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
comment|'# Do these here instead of tearDown because this method is called'
nl|'\n'
comment|'# more than once for the same test case'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommonTests
dedent|''
dedent|''
name|'class'
name|'CommonTests'
op|'('
name|'CommonMixin'
op|','
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_test_actions
indent|'    '
name|'def'
name|'_test_actions'
op|'('
name|'self'
op|','
name|'actions'
op|','
name|'method_translations'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'action'
name|'in'
name|'actions'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'method_translations'
op|'.'
name|'get'
op|'('
name|'action'
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
name|'method'
name|'or'
name|'action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_action'
op|'('
name|'action'
op|','
name|'method'
op|'='
name|'method'
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
DECL|member|_test_actions_with_non_existed_instance
dedent|''
dedent|''
name|'def'
name|'_test_actions_with_non_existed_instance'
op|'('
name|'self'
op|','
name|'actions'
op|','
name|'body_map'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'action'
name|'in'
name|'actions'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_test_non_existing_instance'
op|'('
name|'action'
op|','
nl|'\n'
name|'body_map'
op|'='
name|'body_map'
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
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
