begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'middleware'
name|'import'
name|'request_id'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNovaKeystoneContextMiddleware
name|'class'
name|'TestNovaKeystoneContextMiddleware'
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
name|'TestNovaKeystoneContextMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
op|')'
newline|'\n'
DECL|function|fake_app
name|'def'
name|'fake_app'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'middleware'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'NovaKeystoneContext'
op|'('
name|'fake_app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_TENANT_ID'"
op|']'
op|'='
string|"'testtenantid'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_AUTH_TOKEN'"
op|']'
op|'='
string|"'testauthtoken'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_SERVICE_CATALOG'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_user_or_user_id
dedent|''
name|'def'
name|'test_no_user_or_user_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_id_only
dedent|''
name|'def'
name|'test_user_id_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER_ID'"
op|']'
op|'='
string|"'testuserid'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 OK'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'testuserid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_only
dedent|''
name|'def'
name|'test_user_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER'"
op|']'
op|'='
string|"'testuser'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 OK'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'testuser'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_id_trumps_user
dedent|''
name|'def'
name|'test_user_id_trumps_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER_ID'"
op|']'
op|'='
string|"'testuserid'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER'"
op|']'
op|'='
string|"'testuser'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 OK'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
string|"'testuserid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_service_catalog
dedent|''
name|'def'
name|'test_invalid_service_catalog'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER'"
op|']'
op|'='
string|"'testuser'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_SERVICE_CATALOG'"
op|']'
op|'='
string|'"bad json"'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'500 Internal Server Error'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_request_id_extracted_from_env
dedent|''
name|'def'
name|'test_request_id_extracted_from_env'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req_id'
op|'='
string|"'dummy-request-id'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_PROJECT_ID'"
op|']'
op|'='
string|"'testtenantid'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER_ID'"
op|']'
op|'='
string|"'testuserid'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'environ'
op|'['
name|'request_id'
op|'.'
name|'ENV_REQUEST_ID'
op|']'
op|'='
name|'req_id'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'req_id'
op|','
name|'self'
op|'.'
name|'context'
op|'.'
name|'request_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestKeystoneMiddlewareRoles
dedent|''
dedent|''
name|'class'
name|'TestKeystoneMiddlewareRoles'
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
name|'TestKeystoneMiddlewareRoles'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
op|')'
newline|'\n'
DECL|function|role_check_app
name|'def'
name|'role_check_app'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
string|'"knight"'
name|'in'
name|'context'
op|'.'
name|'roles'
name|'and'
string|'"bad"'
name|'not'
name|'in'
name|'context'
op|'.'
name|'roles'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status'
op|'='
string|'"200 Role Match"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'context'
op|'.'
name|'roles'
op|'=='
op|'['
string|"''"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status'
op|'='
string|'"200 No Roles"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
string|'"unexpected role header"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'middleware'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'NovaKeystoneContext'
op|'('
name|'role_check_app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_USER'"
op|']'
op|'='
string|"'testuser'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_TENANT_ID'"
op|']'
op|'='
string|"'testtenantid'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_AUTH_TOKEN'"
op|']'
op|'='
string|"'testauthtoken'"
newline|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_SERVICE_CATALOG'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'roles'
op|'='
string|'"pawn, knight, rook"'
newline|'\n'
nl|'\n'
DECL|member|test_roles
dedent|''
name|'def'
name|'test_roles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_ROLES'"
op|']'
op|'='
string|"'pawn,knight,rook'"
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 Role Match'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_roles_empty
dedent|''
name|'def'
name|'test_roles_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'X_ROLES'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 No Roles'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_role_headers
dedent|''
name|'def'
name|'test_no_role_headers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test with no role headers set.'
nl|'\n'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'middleware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
string|"'200 No Roles'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestPipeLineFactory
dedent|''
dedent|''
name|'class'
name|'TestPipeLineFactory'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|FakeFilter
indent|'    '
name|'class'
name|'FakeFilter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'obj'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'obj'
op|'='
name|'obj'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|class|FakeApp
dedent|''
dedent|''
name|'class'
name|'FakeApp'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|class|FakeLoader
dedent|''
dedent|''
name|'class'
name|'FakeLoader'
op|'('
op|')'
op|':'
newline|'\n'
DECL|member|get_filter
indent|'        '
name|'def'
name|'get_filter'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'TestPipeLineFactory'
op|'.'
name|'FakeFilter'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_app
dedent|''
name|'def'
name|'get_app'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'TestPipeLineFactory'
op|'.'
name|'FakeApp'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_pipeline
dedent|''
dedent|''
name|'def'
name|'_test_pipeline'
op|'('
name|'self'
op|','
name|'pipeline'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'p'
name|'in'
name|'pipeline'
op|'.'
name|'split'
op|'('
op|')'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'app'
op|'.'
name|'name'
op|','
name|'p'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'app'
op|','
name|'TestPipeLineFactory'
op|'.'
name|'FakeFilter'
op|')'
newline|'\n'
name|'app'
op|'='
name|'app'
op|'.'
name|'obj'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'app'
op|'.'
name|'name'
op|','
name|'pipeline'
op|'.'
name|'split'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'app'
op|','
name|'TestPipeLineFactory'
op|'.'
name|'FakeApp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory
dedent|''
name|'def'
name|'test_pipeline_factory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_pipeline'
op|'='
string|"'test1 test2 test3'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
name|'noauth'
op|'='
name|'fake_pipeline'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
name|'fake_pipeline'
op|','
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory_v21
dedent|''
name|'def'
name|'test_pipeline_factory_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_pipeline'
op|'='
string|"'test1 test2 test3'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory_v21'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
name|'noauth'
op|'='
name|'fake_pipeline'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
name|'fake_pipeline'
op|','
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory_with_rate_limits
dedent|''
name|'def'
name|'test_pipeline_factory_with_rate_limits'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_rate_limit'"
op|','
name|'True'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'auth_strategy'"
op|','
string|"'keystone'"
op|')'
newline|'\n'
name|'fake_pipeline'
op|'='
string|"'test1 test2 test3'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
name|'keystone'
op|'='
name|'fake_pipeline'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
name|'fake_pipeline'
op|','
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory_without_rate_limits
dedent|''
name|'def'
name|'test_pipeline_factory_without_rate_limits'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'auth_strategy'"
op|','
string|"'keystone'"
op|')'
newline|'\n'
name|'fake_pipeline1'
op|'='
string|"'test1 test2 test3'"
newline|'\n'
name|'fake_pipeline2'
op|'='
string|"'test4 test5 test6'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
nl|'\n'
name|'keystone_nolimit'
op|'='
name|'fake_pipeline1'
op|','
nl|'\n'
name|'keystone'
op|'='
name|'fake_pipeline2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
name|'fake_pipeline1'
op|','
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory_missing_nolimits_pipeline
dedent|''
name|'def'
name|'test_pipeline_factory_missing_nolimits_pipeline'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_rate_limit'"
op|','
name|'False'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'auth_strategy'"
op|','
string|"'keystone'"
op|')'
newline|'\n'
name|'fake_pipeline'
op|'='
string|"'test1 test2 test3'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
name|'keystone'
op|'='
name|'fake_pipeline'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
name|'fake_pipeline'
op|','
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pipeline_factory_compatibility_with_v3
dedent|''
name|'def'
name|'test_pipeline_factory_compatibility_with_v3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'api_rate_limit'"
op|','
name|'True'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'auth_strategy'"
op|','
string|"'keystone'"
op|')'
newline|'\n'
name|'fake_pipeline'
op|'='
string|"'test1 ratelimit_v3 test3'"
newline|'\n'
name|'app'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'pipeline_factory'
op|'('
nl|'\n'
name|'TestPipeLineFactory'
op|'.'
name|'FakeLoader'
op|'('
op|')'
op|','
name|'None'
op|','
name|'keystone'
op|'='
name|'fake_pipeline'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_pipeline'
op|'('
string|"'test1 test3'"
op|','
name|'app'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
