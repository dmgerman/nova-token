begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
name|'from'
name|'nova'
op|'.'
name|'consoleauth'
name|'import'
name|'rpcapi'
name|'as'
name|'consoleauth_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
nl|'\n'
DECL|variable|_FAKE_CONNECT_INFO
name|'_FAKE_CONNECT_INFO'
op|'='
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake_instance_uuid'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'port'"
op|':'
string|"'fake_port'"
op|','
nl|'\n'
string|"'internal_access_path'"
op|':'
string|"'fake_access_path'"
op|','
nl|'\n'
string|"'console_type'"
op|':'
string|"'rdp-html5'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_check_token
name|'def'
name|'_fake_check_token'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_FAKE_CONNECT_INFO'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_check_token_not_found
dedent|''
name|'def'
name|'_fake_check_token_not_found'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_check_token_unauthorized
dedent|''
name|'def'
name|'_fake_check_token_unauthorized'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'connect_info'
op|'='
name|'_FAKE_CONNECT_INFO'
newline|'\n'
name|'connect_info'
op|'['
string|"'console_type'"
op|']'
op|'='
string|"'unauthorized_console_type'"
newline|'\n'
name|'return'
name|'connect_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthTokensExtensionTest
dedent|''
name|'class'
name|'ConsoleAuthTokensExtensionTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_URL
indent|'    '
name|'_FAKE_URL'
op|'='
string|"'/v3/os-console-auth-tokens/1'"
newline|'\n'
nl|'\n'
DECL|variable|_EXPECTED_OUTPUT
name|'_EXPECTED_OUTPUT'
op|'='
op|'{'
string|"'console'"
op|':'
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake_instance_uuid'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'port'"
op|':'
string|"'fake_port'"
op|','
nl|'\n'
string|"'internal_access_path'"
op|':'
nl|'\n'
string|"'fake_access_path'"
op|'}'
op|'}'
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
name|'ConsoleAuthTokensExtensionTest'
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
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|','
string|"'check_token'"
op|','
nl|'\n'
name|'_fake_check_token'
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'_get_admin_context'
op|'('
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
string|"'os-console-auth-tokens'"
op|')'
op|','
nl|'\n'
name|'fake_auth_context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_admin_context
dedent|''
name|'def'
name|'_get_admin_context'
op|'('
name|'self'
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
name|'return'
name|'ctxt'
newline|'\n'
nl|'\n'
DECL|member|_create_request
dedent|''
name|'def'
name|'_create_request'
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
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_FAKE_URL'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"GET"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_connect_info
dedent|''
name|'def'
name|'test_get_console_connect_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_EXPECTED_OUTPUT'
op|','
name|'output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_connect_info_token_not_found
dedent|''
name|'def'
name|'test_get_console_connect_info_token_not_found'
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
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|','
string|"'check_token'"
op|','
nl|'\n'
name|'_fake_check_token_not_found'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
nl|'\n'
DECL|member|test_get_console_connect_info_unauthorized_console_type
dedent|''
name|'def'
name|'test_get_console_connect_info_unauthorized_console_type'
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
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|','
string|"'check_token'"
op|','
nl|'\n'
name|'_fake_check_token_unauthorized'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'401'
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
