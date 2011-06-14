begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'auth'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
DECL|class|Test
name|'class'
name|'Test'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'Test'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fakes'
op|'.'
name|'fake_auth_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'context'
op|','
string|"'RequestContext'"
op|','
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'clear_fakes'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'fake_data_store'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'Test'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_user
dedent|''
name|'def'
name|'test_authorize_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|')'
op|','
number|'40'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-CDN-Management-Url'"
op|']'
op|','
nl|'\n'
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Storage-Url'"
op|']'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_token
dedent|''
name|'def'
name|'test_authorize_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user1_project'"
op|','
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|','
op|'{'
string|"'HTTP_HOST'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|')'
op|','
number|'40'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Server-Management-Url'"
op|']'
op|','
nl|'\n'
string|'"http://foo/v1.0/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-CDN-Management-Url'"
op|']'
op|','
nl|'\n'
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Storage-Url'"
op|']'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|','
string|"'APIRouterV10'"
op|','
name|'fakes'
op|'.'
name|'FakeRouter'
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
string|"'/v1.0/fake'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
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
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Test-Success'"
op|']'
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_token_expiry
dedent|''
name|'def'
name|'test_token_expiry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'destroy_called'
op|'='
name|'False'
newline|'\n'
name|'token_hash'
op|'='
string|"'token_hash'"
newline|'\n'
nl|'\n'
DECL|function|destroy_token_mock
name|'def'
name|'destroy_token_mock'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'destroy_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|bad_token
dedent|''
name|'def'
name|'bad_token'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'token_hash'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fakes'
op|'.'
name|'FakeToken'
op|'('
nl|'\n'
name|'token_hash'
op|'='
name|'token_hash'
op|','
nl|'\n'
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1990'
op|','
number|'1'
op|','
number|'1'
op|')'
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
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|','
string|"'auth_token_destroy'"
op|','
nl|'\n'
name|'destroy_token_mock'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|','
string|"'auth_token_get'"
op|','
nl|'\n'
name|'bad_token'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
string|"'token_hash'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'destroy_called'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_project
dedent|''
name|'def'
name|'test_authorize_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user1_project'"
op|','
name|'user'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user2_project'"
op|','
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|','
op|'{'
string|"'HTTP_HOST'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|','
string|"'APIRouterV10'"
op|','
name|'fakes'
op|'.'
name|'FakeRouter'
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
string|"'/v1.0/fake'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'user2_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
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
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Test-Success'"
op|']'
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_user_bad_key
dedent|''
name|'def'
name|'test_bad_user_bad_key'
op|'('
name|'self'
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
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'unknown_user'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'unknown_user_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_user_good_key
dedent|''
name|'def'
name|'test_bad_user_good_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'unknown_user'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_user
dedent|''
name|'def'
name|'test_no_user'
op|'('
name|'self'
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
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_token
dedent|''
name|'def'
name|'test_bad_token'
op|'('
name|'self'
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
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
string|"'unknown_token'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_project
dedent|''
name|'def'
name|'test_bad_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user1'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'user2'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id2'"
op|','
string|"'user2'"
op|','
string|"'user2_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user1'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user2'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user1_project'"
op|','
name|'user1'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user2_project'"
op|','
name|'user2'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|','
op|'{'
string|"'HTTP_HOST'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|','
string|"'APIRouterV10'"
op|','
name|'fakes'
op|'.'
name|'FakeRouter'
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
string|"'/v1.0/fake'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'user2_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_existing_project
dedent|''
name|'def'
name|'test_not_existing_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user1'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user1'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'user1_project'"
op|','
name|'user1'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|','
op|'{'
string|"'HTTP_HOST'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'204 No Content'"
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|','
string|"'APIRouterV10'"
op|','
name|'fakes'
op|'.'
name|'FakeRouter'
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
string|"'/v1.0/fake'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Project-Id'"
op|']'
op|'='
string|"'unknown_project'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFunctional
dedent|''
dedent|''
name|'class'
name|'TestFunctional'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_token_expiry
indent|'    '
name|'def'
name|'test_token_expiry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'tok'
op|'='
name|'db'
op|'.'
name|'auth_token_create'
op|'('
name|'ctx'
op|','
name|'dict'
op|'('
nl|'\n'
name|'token_hash'
op|'='
string|"'test_token_hash'"
op|','
nl|'\n'
name|'cdn_management_url'
op|'='
string|"''"
op|','
nl|'\n'
name|'server_management_url'
op|'='
string|"''"
op|','
nl|'\n'
name|'storage_url'
op|'='
string|"''"
op|','
nl|'\n'
name|'user_id'
op|'='
string|"'user1'"
op|','
nl|'\n'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'auth_token_update'
op|'('
name|'ctx'
op|','
name|'tok'
op|'.'
name|'token_hash'
op|','
name|'dict'
op|'('
nl|'\n'
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2000'
op|','
number|'1'
op|','
number|'1'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
string|"'test_token_hash'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_token_doesnotexist
dedent|''
name|'def'
name|'test_token_doesnotexist'
op|'('
name|'self'
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
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
string|"'nonexistant_token_hash'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'status'
op|','
string|"'401 Unauthorized'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLimiter
dedent|''
dedent|''
name|'class'
name|'TestLimiter'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestLimiter'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fakes'
op|'.'
name|'fake_auth_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'context'
op|','
string|"'RequestContext'"
op|','
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'clear_fakes'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'fake_data_store'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'TestLimiter'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_token
dedent|''
name|'def'
name|'test_authorize_token'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
op|'.'
name|'User'
op|'('
string|"'id1'"
op|','
string|"'user1'"
op|','
string|"'user1_key'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'add_user'
op|'('
name|'user'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'create_project'
op|'('
string|"'test'"
op|','
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Key'"
op|']'
op|'='
string|"'user1_key'"
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|')'
op|','
number|'40'
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|','
string|"'APIRouterV10'"
op|','
name|'fakes'
op|'.'
name|'FakeRouter'
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
string|"'/v1.0/fake'"
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
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
name|'token'
newline|'\n'
name|'result'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
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
name|'result'
op|'.'
name|'headers'
op|'['
string|"'X-Test-Success'"
op|']'
op|','
string|"'True'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
