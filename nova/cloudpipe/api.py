begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
nl|'\n'
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
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_project_id_from_ip
dedent|''
name|'def'
name|'get_project_id_from_ip'
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
name|'instance'
op|'['
string|"'project_id'"
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
name|'project_id'
op|'='
name|'self'
op|'.'
name|'get_project_id_from_ip'
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
name|'project_id'
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
name|'project_id'
op|'='
name|'self'
op|'.'
name|'get_project_id_from_ip'
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
name|'crypto'
op|'.'
name|'sign_csr'
op|'('
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'cert'
op|')'
op|','
name|'project_id'
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
