begin_unit
comment|'#!/usr/bin/python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""\nTornado REST API Request Handlers for CloudPipe\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'import'
name|'tornado'
op|'.'
name|'web'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
nl|'\n'
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"api"'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudPipeRequestHandler
name|'class'
name|'CloudPipeRequestHandler'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'RequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'path'
newline|'\n'
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"Cloudpipe path is %s"'
op|'%'
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'path'
op|'.'
name|'endswith'
op|'('
string|'"/getca/"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'send_root_ca'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'path'
op|'.'
name|'endswith'
op|'('
string|'"/getcert/"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"Getting zip for %s"'
op|'%'
op|'('
name|'path'
op|'['
number|'9'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'send_signed_zip'
op|'('
name|'self'
op|'.'
name|'path'
op|'['
number|'9'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'ERROR: %s\\n'"
op|'%'
name|'str'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'404'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_username_from_ip
dedent|''
name|'def'
name|'get_username_from_ip'
op|'('
name|'self'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cc'
op|'='
name|'self'
op|'.'
name|'application'
op|'.'
name|'controllers'
op|'['
string|"'Cloud'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'cc'
op|'.'
name|'get_instance_by_ip'
op|'('
name|'ip'
op|')'
newline|'\n'
name|'return'
name|'instance'
op|'['
string|"'owner_id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|send_root_ca
dedent|''
name|'def'
name|'send_root_ca'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'debug'
op|'('
string|'"Getting root ca"'
op|')'
newline|'\n'
name|'username'
op|'='
name|'self'
op|'.'
name|'get_username_from_ip'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Content-Type"'
op|','
string|'"text/plain"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'username'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|send_signed_zip
dedent|''
name|'def'
name|'send_signed_zip'
op|'('
name|'self'
op|','
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'set_header'
op|'('
string|'"Content-Type"'
op|','
string|'"application/zip"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_signed_zip'
op|'('
name|'username'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post
dedent|''
name|'def'
name|'post'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'username'
op|'='
name|'self'
op|'.'
name|'get_username_from_ip'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
op|')'
newline|'\n'
name|'cert'
op|'='
name|'self'
op|'.'
name|'get_argument'
op|'('
string|"'cert'"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'sign_cert'
op|'('
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'cert'
op|')'
op|','
name|'username'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
