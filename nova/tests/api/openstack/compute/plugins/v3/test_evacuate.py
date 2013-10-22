begin_unit
comment|'#   Copyright 2013 OpenStack Foundation'
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
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
string|"'password_length'"
op|','
string|"'nova.utils'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api
name|'def'
name|'fake_compute_api'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api_get
dedent|''
name|'def'
name|'fake_compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|','
string|"'host'"
op|':'
string|"'host1'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_get_by_compute_host
dedent|''
name|'def'
name|'fake_service_get_by_compute_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'host'
op|'=='
string|"'bad_host'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'host_name'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'service'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EvacuateTest
dedent|''
dedent|''
name|'class'
name|'EvacuateTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_methods
indent|'    '
name|'_methods'
op|'='
op|'('
string|"'resize'"
op|','
string|"'evacuate'"
op|')'
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
name|'EvacuateTest'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_api_get'
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
name|'HostAPI'
op|','
string|"'service_get_by_compute_host'"
op|','
nl|'\n'
name|'fake_service_get_by_compute_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'UUID'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
name|'for'
name|'_method'
name|'in'
name|'self'
op|'.'
name|'_methods'
op|':'
newline|'\n'
indent|'            '
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
name|'_method'
op|','
name|'fake_compute_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_update
dedent|''
dedent|''
name|'def'
name|'_fake_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'task_state'
op|','
name|'expected_task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|_gen_request_with_app
dedent|''
name|'def'
name|'_gen_request_with_app'
op|'('
name|'self'
op|','
name|'json_load'
op|','
name|'is_admin'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'ctxt'
op|'.'
name|'is_admin'
op|'='
name|'is_admin'
newline|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
name|'fake_auth_context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'base_json_load'
op|'='
op|'{'
string|"'evacuate'"
op|':'
name|'json_load'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'base_json_load'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'return'
name|'req'
op|','
name|'app'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_instance_with_no_target
dedent|''
name|'def'
name|'test_evacuate_instance_with_no_target'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'on_shared_storage'"
op|':'
string|"'False'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_instance_without_on_shared_storage
dedent|''
name|'def'
name|'test_evacuate_instance_without_on_shared_storage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_instance_with_bad_host
dedent|''
name|'def'
name|'test_evacuate_instance_with_bad_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'bad_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'False'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_instance_with_target
dedent|''
name|'def'
name|'test_evacuate_instance_with_target'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'False'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
string|"'update'"
op|','
name|'self'
op|'.'
name|'_fake_update'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_json'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"MyNewPass"'
op|','
name|'resp_json'
op|'['
string|"'admin_password'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_shared_and_pass
dedent|''
name|'def'
name|'test_evacuate_shared_and_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'True'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
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
string|"'update'"
op|','
name|'self'
op|'.'
name|'_fake_update'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_not_shared_pass_generated
dedent|''
name|'def'
name|'test_evacuate_not_shared_pass_generated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'False'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
string|"'update'"
op|','
name|'self'
op|'.'
name|'_fake_update'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_json'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'password_length'
op|','
nl|'\n'
name|'len'
op|'('
name|'resp_json'
op|'['
string|"'admin_password'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_shared
dedent|''
name|'def'
name|'test_evacuate_shared'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'True'"
op|'}'
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
string|"'update'"
op|','
name|'self'
op|'.'
name|'_fake_update'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_json'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'resp_json'
op|'['
string|"'admin_password'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate_with_active_service
dedent|''
name|'def'
name|'test_evacuate_with_active_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'false'"
op|','
nl|'\n'
string|"'admin_password'"
op|':'
string|"'MyNewPass'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_evacuate
name|'def'
name|'fake_evacuate'
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
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceInUse'
op|'('
string|'"Service still in use"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
string|"'evacuate'"
op|','
name|'fake_evacuate'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_admin
dedent|''
name|'def'
name|'test_not_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|','
name|'app'
op|'='
name|'self'
op|'.'
name|'_gen_request_with_app'
op|'('
op|'{'
string|"'host'"
op|':'
string|"'my_host'"
op|','
nl|'\n'
string|"'on_shared_storage'"
op|':'
string|"'True'"
op|'}'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
