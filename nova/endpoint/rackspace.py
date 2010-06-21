begin_unit
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
string|'"""\nRackspace API\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'multiprocessing'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
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
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'storage'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'cloud_topic'"
op|','
string|"'cloud'"
op|','
string|"'the topic clouds listen on'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_gen_key
name|'def'
name|'_gen_key'
op|'('
name|'user_id'
op|','
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Tuck this into UserManager """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
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
name|'private_key'
op|','
name|'fingerprint'
op|'='
name|'manager'
op|'.'
name|'generate_key_pair'
op|'('
name|'user_id'
op|','
name|'key_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'exception'"
op|':'
name|'ex'
op|'}'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'private_key'"
op|':'
name|'private_key'
op|','
string|"'fingerprint'"
op|':'
name|'fingerprint'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Api
dedent|''
name|'class'
name|'Api'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'rpc_mechanism'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controllers'
op|'='
op|'{'
nl|'\n'
string|'"v1.0"'
op|':'
name|'RackspaceAuthenticationApi'
op|'('
op|')'
op|','
nl|'\n'
string|'"server"'
op|':'
name|'RackspaceCloudServerApi'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'rpc_mechanism'
op|'='
name|'rpc_mechanism'
newline|'\n'
nl|'\n'
DECL|member|handler
dedent|''
name|'def'
name|'handler'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'responder'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
string|'"*** %s"'
op|'%'
name|'environ'
op|')'
newline|'\n'
name|'controller'
op|','
name|'path'
op|'='
name|'wsgi'
op|'.'
name|'Util'
op|'.'
name|'route'
op|'('
name|'environ'
op|'['
string|"'PATH_INFO'"
op|']'
op|','
name|'self'
op|'.'
name|'controllers'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'controller'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Missing Controller"'
op|')'
newline|'\n'
dedent|''
name|'rv'
op|'='
name|'controller'
op|'.'
name|'process'
op|'('
name|'path'
op|','
name|'environ'
op|')'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'rv'
op|')'
name|'is'
name|'tuple'
op|':'
newline|'\n'
indent|'            '
name|'responder'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|','
name|'rv'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'rv'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'responder'
op|'('
string|'"200 OK"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
DECL|class|RackspaceApiEndpoint
dedent|''
dedent|''
name|'class'
name|'RackspaceApiEndpoint'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|process
indent|'    '
name|'def'
name|'process'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'path'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'index'
op|'('
name|'env'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'action'
op|'='
name|'path'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'self'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'action'
op|')'
newline|'\n'
name|'return'
name|'method'
op|'('
name|'path'
op|','
name|'env'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Missing method %s"'
op|'%'
name|'path'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RackspaceAuthenticationApi
dedent|''
dedent|''
dedent|''
name|'class'
name|'RackspaceAuthenticationApi'
op|'('
name|'RackspaceApiEndpoint'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
string|"'204 No Content'"
newline|'\n'
name|'headers'
op|'='
op|'['
nl|'\n'
op|'('
string|"'X-Server-Management-Url'"
op|','
string|"'http://localhost:8773/server'"
op|')'
op|','
nl|'\n'
op|'('
string|"'X-Storage-Url'"
op|','
string|"'http://localhost:8773/server'"
op|')'
op|','
nl|'\n'
op|'('
string|"'X-CDN-Managment-Url'"
op|','
string|"'http://localhost:8773/server'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'body'
op|'='
string|'""'
newline|'\n'
name|'return'
op|'('
name|'response'
op|','
name|'headers'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RackspaceCloudServerApi
dedent|''
dedent|''
name|'class'
name|'RackspaceCloudServerApi'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"IDX"'
newline|'\n'
nl|'\n'
DECL|member|list
dedent|''
name|'def'
name|'list'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s"'
op|'%'
name|'args'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
