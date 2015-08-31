begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'import'
name|'mock'
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
name|'import'
name|'admin_password'
name|'as'
name|'admin_password_v21'
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
name|'legacy_v2'
name|'import'
name|'servers'
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
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
name|'want_objects'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_set_admin_password
dedent|''
name|'def'
name|'fake_set_admin_password'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'password'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminPasswordTestV21
dedent|''
name|'class'
name|'AdminPasswordTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|validiation_error
indent|'    '
name|'validiation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'AdminPasswordTestV21'
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
string|"'set_admin_password'"
op|','
nl|'\n'
name|'fake_set_admin_password'
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
name|'fake_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_req'
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
nl|'\n'
DECL|member|_get_action
dedent|''
name|'def'
name|'_get_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'admin_password_v21'
op|'.'
name|'AdminPasswordController'
op|'('
op|')'
op|'.'
name|'change_password'
newline|'\n'
nl|'\n'
DECL|member|_check_status
dedent|''
name|'def'
name|'_check_status'
op|'('
name|'self'
op|','
name|'expected_status'
op|','
name|'res'
op|','
name|'controller_method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_status'
op|','
name|'controller_method'
op|'.'
name|'wsgi_code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password
dedent|''
name|'def'
name|'test_change_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'test'"
op|'}'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_status'
op|'('
number|'202'
op|','
name|'res'
op|','
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_empty_string
dedent|''
name|'def'
name|'test_change_password_empty_string'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_status'
op|'('
number|'202'
op|','
name|'res'
op|','
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.set_admin_password'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'NotImplementedError'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_change_password_with_non_implement
name|'def'
name|'test_change_password_with_non_implement'
op|'('
name|'self'
op|','
name|'mock_set_admin_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'test'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'1'"
op|')'
op|')'
newline|'\n'
DECL|member|test_change_password_with_non_existed_instance
name|'def'
name|'test_change_password_with_non_existed_instance'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'test'"
op|'}'
op|'}'
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
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_with_non_string_password
dedent|''
name|'def'
name|'test_change_password_with_non_string_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
number|'1234'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validiation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.set_admin_password'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstancePasswordSetFailed'
op|'('
name|'instance'
op|'='
string|'"1"'
op|','
nl|'\n'
name|'reason'
op|'='
string|"''"
op|')'
op|')'
newline|'\n'
DECL|member|test_change_password_failed
name|'def'
name|'test_change_password_failed'
op|'('
name|'self'
op|','
name|'mock_set_admin_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'test'"
op|'}'
op|'}'
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
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_without_admin_password
dedent|''
name|'def'
name|'test_change_password_without_admin_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changPassword'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validiation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_none
dedent|''
name|'def'
name|'test_change_password_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validiation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_adminpass_none
dedent|''
name|'def'
name|'test_change_password_adminpass_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validiation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_password_bad_request
dedent|''
name|'def'
name|'test_change_password_bad_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'pass'"
op|':'
string|"'12345'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validiation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_change_password_pass_disabled
dedent|''
name|'def'
name|'test_server_change_password_pass_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# run with enable_instance_password disabled to verify adminPass'
nl|'\n'
comment|'# is missing from response. See lp bug 921814'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_instance_password'
op|'='
name|'False'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'1234pass'"
op|'}'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_status'
op|'('
number|'202'
op|','
name|'res'
op|','
name|'self'
op|'.'
name|'_get_action'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.set_admin_password'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake'"
op|','
name|'attr'
op|'='
string|"'vm_state'"
op|','
name|'state'
op|'='
string|"'stopped'"
op|','
nl|'\n'
name|'method'
op|'='
string|"'set_admin_password'"
op|')'
op|')'
newline|'\n'
DECL|member|test_change_password_invalid_state
name|'def'
name|'test_change_password_invalid_state'
op|'('
name|'self'
op|','
name|'mock_set_admin_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'test'"
op|'}'
op|'}'
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
name|'_get_action'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
string|"'fake'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminPasswordTestV2
dedent|''
dedent|''
name|'class'
name|'AdminPasswordTestV2'
op|'('
name|'AdminPasswordTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|validiation_error
indent|'    '
name|'validiation_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|_get_action
name|'def'
name|'_get_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeExtManager
indent|'        '
name|'class'
name|'FakeExtManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|is_loaded
indent|'            '
name|'def'
name|'is_loaded'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'servers'
op|'.'
name|'Controller'
op|'('
name|'ext_mgr'
op|'='
name|'FakeExtManager'
op|'('
op|')'
op|')'
op|'.'
name|'_action_change_password'
newline|'\n'
nl|'\n'
DECL|member|_check_status
dedent|''
name|'def'
name|'_check_status'
op|'('
name|'self'
op|','
name|'expected_status'
op|','
name|'res'
op|','
name|'controller_method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_status'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminPasswordPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'AdminPasswordPolicyEnforcementV21'
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
name|'AdminPasswordPolicyEnforcementV21'
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
name|'admin_password_v21'
op|'.'
name|'AdminPasswordController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
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
nl|'\n'
DECL|member|test_change_password_policy_failed
dedent|''
name|'def'
name|'test_change_password_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-admin-password"'
newline|'\n'
name|'rule'
op|'='
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rule'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'changePassword'"
op|':'
op|'{'
string|"'adminPass'"
op|':'
string|"'1234pass'"
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'change_password'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
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