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
string|'"""\nTornado REST API Request Handlers for Nova functions\nMost calls are proxied into the responsible controller.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'multiprocessing'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
comment|'# TODO(termie): replace minidom with etree'
nl|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
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
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'cc_port'"
op|','
number|'8773'
op|','
string|"'cloud controller port'"
op|')'
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
DECL|variable|_c2u
name|'_c2u'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_camelcase_to_underscore
name|'def'
name|'_camelcase_to_underscore'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_c2u'
op|'.'
name|'sub'
op|'('
string|"r'_\\1'"
op|','
name|'str'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
string|"'_'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_underscore_to_camelcase
dedent|''
name|'def'
name|'_underscore_to_camelcase'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'x'
op|'['
op|':'
number|'1'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
name|'x'
op|'['
number|'1'
op|':'
op|']'
name|'for'
name|'x'
name|'in'
name|'str'
op|'.'
name|'split'
op|'('
string|"'_'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_underscore_to_xmlcase
dedent|''
name|'def'
name|'_underscore_to_xmlcase'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'res'
op|'='
name|'_underscore_to_camelcase'
op|'('
name|'str'
op|')'
newline|'\n'
name|'return'
name|'res'
op|'['
op|':'
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
name|'res'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRequestContext
dedent|''
name|'class'
name|'APIRequestContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'handler'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'user'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'project'
newline|'\n'
name|'self'
op|'.'
name|'request_id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
nl|'\n'
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
string|"'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-'"
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'20'
op|')'
op|']'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRequest
dedent|''
dedent|''
name|'class'
name|'APIRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'controller'
newline|'\n'
name|'self'
op|'.'
name|'action'
op|'='
name|'action'
newline|'\n'
nl|'\n'
DECL|member|send
dedent|''
name|'def'
name|'send'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'_camelcase_to_underscore'
op|'('
name|'self'
op|'.'
name|'action'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'_error'
op|'='
op|'('
string|"'Unsupported API request: controller = %s,'"
nl|'\n'
string|"'action = %s'"
op|')'
op|'%'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'self'
op|'.'
name|'action'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'warning'
op|'('
name|'_error'
op|')'
newline|'\n'
comment|'# TODO: Raise custom exception, trap in apiserver,'
nl|'\n'
comment|'#       and reraise as 400 error.'
nl|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_error'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'kwargs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
newline|'\n'
name|'key'
op|'='
name|'_camelcase_to_underscore'
op|'('
name|'parts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'args'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'d'
op|'['
name|'parts'
op|'['
number|'1'
op|']'
op|']'
op|'='
name|'value'
op|'['
number|'0'
op|']'
newline|'\n'
name|'value'
op|'='
name|'d'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'value'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'args'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'args'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'args'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'args'
op|'['
name|'key'
op|']'
op|'!='
op|'{'
op|'}'
name|'and'
name|'args'
op|'['
name|'key'
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'isdigit'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'s'
op|'='
name|'args'
op|'['
name|'key'
op|']'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'s'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'args'
op|'['
name|'key'
op|']'
op|'='
op|'['
name|'v'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'s'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'d'
op|'='
name|'defer'
op|'.'
name|'maybeDeferred'
op|'('
name|'method'
op|','
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_render_response'
op|','
name|'context'
op|'.'
name|'request_id'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|_render_response
dedent|''
name|'def'
name|'_render_response'
op|'('
name|'self'
op|','
name|'response_data'
op|','
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
name|'self'
op|'.'
name|'action'
op|'+'
string|"'Response'"
op|')'
newline|'\n'
name|'response_el'
op|'.'
name|'setAttribute'
op|'('
string|"'xmlns'"
op|','
nl|'\n'
string|"'http://ec2.amazonaws.com/doc/2009-11-30/'"
op|')'
newline|'\n'
name|'request_id_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
string|"'requestId'"
op|')'
newline|'\n'
name|'request_id_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'request_id'
op|')'
op|')'
newline|'\n'
name|'response_el'
op|'.'
name|'appendChild'
op|'('
name|'request_id_el'
op|')'
newline|'\n'
name|'if'
op|'('
name|'response_data'
op|'=='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'response_el'
op|','
op|'{'
string|"'return'"
op|':'
string|"'true'"
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'response_el'
op|','
name|'response_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'xml'
op|'.'
name|'appendChild'
op|'('
name|'response_el'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'xml'
op|'.'
name|'toxml'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'.'
name|'unlink'
op|'('
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'debug'
op|'('
name|'response'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_render_dict
dedent|''
name|'def'
name|'_render_dict'
op|'('
name|'self'
op|','
name|'xml'
op|','
name|'el'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'val'
op|'='
name|'data'
op|'['
name|'key'
op|']'
newline|'\n'
name|'el'
op|'.'
name|'appendChild'
op|'('
name|'self'
op|'.'
name|'_render_data'
op|'('
name|'xml'
op|','
name|'key'
op|','
name|'val'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
name|'data'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_render_data
dedent|''
dedent|''
name|'def'
name|'_render_data'
op|'('
name|'self'
op|','
name|'xml'
op|','
name|'el_name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'el_name'
op|'='
name|'_underscore_to_xmlcase'
op|'('
name|'el_name'
op|')'
newline|'\n'
name|'data_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
name|'el_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'self'
op|'.'
name|'_render_data'
op|'('
name|'xml'
op|','
string|"'item'"
op|','
name|'item'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'data_el'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'hasattr'
op|'('
name|'data'
op|','
string|"'__dict__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'data_el'
op|','
name|'data'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'bool'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'data'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data_el'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RootRequestHandler
dedent|''
dedent|''
name|'class'
name|'RootRequestHandler'
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
op|')'
op|':'
newline|'\n'
comment|'# available api versions'
nl|'\n'
indent|'        '
name|'versions'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
string|"'%s\\n'"
op|'%'
name|'version'
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
nl|'\n'
DECL|class|MetadataRequestHandler
dedent|''
dedent|''
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'RequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|print_data
indent|'    '
name|'def'
name|'print_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
op|'=='
string|"'_name'"
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'output'
op|'+='
name|'key'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'_name'"
name|'in'
name|'data'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'='"
op|'+'
name|'str'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|'['
string|"'_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'output'
op|'+='
string|"'\\n'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'write'
op|'('
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
comment|'# cut off last \\n'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'write'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookup
dedent|''
dedent|''
name|'def'
name|'lookup'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'data'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'data'
op|'['
name|'item'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
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
name|'meta_data'
op|'='
name|'cc'
op|'.'
name|'get_metadata'
op|'('
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
op|')'
newline|'\n'
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'error'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'remote_ip'
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
name|'data'
op|'='
name|'self'
op|'.'
name|'lookup'
op|'('
name|'path'
op|','
name|'meta_data'
op|')'
newline|'\n'
name|'if'
name|'data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
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
name|'self'
op|'.'
name|'print_data'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|APIRequestHandler
dedent|''
dedent|''
name|'class'
name|'APIRequestHandler'
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
name|'controller_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'execute'
op|'('
name|'controller_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'asynchronous'
newline|'\n'
DECL|member|execute
name|'def'
name|'execute'
op|'('
name|'self'
op|','
name|'controller_name'
op|')'
op|':'
newline|'\n'
comment|'# Obtain the appropriate controller for this request.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'self'
op|'.'
name|'application'
op|'.'
name|'controllers'
op|'['
name|'controller_name'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error'
op|'('
string|"'unhandled'"
op|','
string|"'no controller named %s'"
op|'%'
name|'controller_name'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
name|'self'
op|'.'
name|'request'
op|'.'
name|'arguments'
newline|'\n'
nl|'\n'
comment|'# Read request signature.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'signature'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Signature'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'400'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make a copy of args for authentication and signature verification.'
nl|'\n'
dedent|''
name|'auth_params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'args'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'auth_params'
op|'['
name|'key'
op|']'
op|'='
name|'value'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Get requested action and remove authentication args for final request.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Action'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'access'
op|'='
name|'args'
op|'.'
name|'pop'
op|'('
string|"'AWSAccessKeyId'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'SignatureMethod'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'SignatureVersion'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Version'"
op|')'
newline|'\n'
name|'args'
op|'.'
name|'pop'
op|'('
string|"'Timestamp'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'400'
op|')'
newline|'\n'
nl|'\n'
comment|'# Authenticate the request.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'user'
op|','
name|'project'
op|')'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'authenticate'
op|'('
nl|'\n'
name|'access'
op|','
nl|'\n'
name|'signature'
op|','
nl|'\n'
name|'auth_params'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'method'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request'
op|'.'
name|'path'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Error'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Authentication Failure: %s"'
op|'%'
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'HTTPError'
op|'('
number|'403'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'action: %s'"
op|'%'
name|'action'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'args'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'arg: %s\\t\\tval: %s'"
op|'%'
op|'('
name|'key'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'='
name|'APIRequest'
op|'('
name|'controller'
op|','
name|'action'
op|')'
newline|'\n'
name|'context'
op|'='
name|'APIRequestContext'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'d'
op|'='
name|'request'
op|'.'
name|'send'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
comment|'# d.addCallback(utils.debug)'
nl|'\n'
nl|'\n'
comment|'# TODO: Wrap response in AWS XML format'
nl|'\n'
name|'d'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'_write_callback'
op|','
name|'self'
op|'.'
name|'_error_callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_write_callback
dedent|''
name|'def'
name|'_write_callback'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'set_header'
op|'('
string|"'Content-Type'"
op|','
string|"'text/xml'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_error_callback
dedent|''
name|'def'
name|'_error_callback'
op|'('
name|'self'
op|','
name|'failure'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'failure'
op|'.'
name|'raiseException'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ApiError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error'
op|'('
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|'+'
string|'"."'
op|'+'
name|'ex'
op|'.'
name|'code'
op|','
name|'ex'
op|'.'
name|'message'
op|')'
newline|'\n'
comment|'# TODO(vish): do something more useful with unknown exceptions'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error'
op|'('
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|post
dedent|''
dedent|''
name|'def'
name|'post'
op|'('
name|'self'
op|','
name|'controller_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'execute'
op|'('
name|'controller_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_error
dedent|''
name|'def'
name|'_error'
op|'('
name|'self'
op|','
name|'code'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_status_code'
op|'='
number|'400'
newline|'\n'
name|'self'
op|'.'
name|'set_header'
op|'('
string|"'Content-Type'"
op|','
string|"'text/xml'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
string|'\'<?xml version="1.0"?>\\n\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
string|"'<Response><Errors><Error><Code>%s</Code>'"
nl|'\n'
string|"'<Message>%s</Message></Error></Errors>'"
nl|'\n'
string|"'<RequestID>?</RequestID></Response>'"
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'finish'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIServerApplication
dedent|''
dedent|''
name|'class'
name|'APIServerApplication'
op|'('
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'user_manager'
op|','
name|'controllers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tornado'
op|'.'
name|'web'
op|'.'
name|'Application'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'['
nl|'\n'
op|'('
string|"r'/'"
op|','
name|'RootRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/cloudpipe/(.*)'"
op|','
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
op|'.'
name|'CloudPipeRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/cloudpipe'"
op|','
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'api'
op|'.'
name|'CloudPipeRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/services/([A-Za-z0-9]+)/'"
op|','
name|'APIRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/latest/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2009-04-04/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2008-09-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2008-02-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-12-15/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-10-10/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-08-29/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-03-01/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/2007-01-19/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|'('
string|"r'/1.0/([-A-Za-z0-9/]*)'"
op|','
name|'MetadataRequestHandler'
op|')'
op|','
nl|'\n'
op|']'
op|','
name|'pool'
op|'='
name|'multiprocessing'
op|'.'
name|'Pool'
op|'('
number|'4'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user_manager'
op|'='
name|'user_manager'
newline|'\n'
name|'self'
op|'.'
name|'controllers'
op|'='
name|'controllers'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
