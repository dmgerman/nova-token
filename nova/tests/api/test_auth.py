begin_unit
comment|'# Copyright (c) 2012 OpenStack, LLC'
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
name|'webob'
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
nl|'\n'
DECL|class|TestNovaKeystoneContextMiddleware
name|'class'
name|'TestNovaKeystoneContextMiddleware'
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
dedent|''
dedent|''
endmarker|''
end_unit
