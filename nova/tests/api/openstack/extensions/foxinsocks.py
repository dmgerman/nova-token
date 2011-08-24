begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FoxInSocksController
name|'class'
name|'FoxInSocksController'
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
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Try to say this Mr. Knox, sir..."'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Foxinsocks
dedent|''
dedent|''
name|'class'
name|'Foxinsocks'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_name
dedent|''
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Fox In Socks"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"FOXNSOX"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"The Fox In Socks Extension"'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://www.fox.in.socks/api/ext/pie/v1.0"'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"2011-01-22T13:25:27-06:00"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'foxnsocks'"
op|','
nl|'\n'
name|'FoxInSocksController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
name|'actions'
op|'.'
name|'append'
op|'('
name|'extensions'
op|'.'
name|'ActionExtension'
op|'('
string|"'servers'"
op|','
string|"'add_tweedle'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_add_tweedle'
op|')'
op|')'
newline|'\n'
name|'actions'
op|'.'
name|'append'
op|'('
name|'extensions'
op|'.'
name|'ActionExtension'
op|'('
string|"'servers'"
op|','
string|"'delete_tweedle'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_delete_tweedle'
op|')'
op|')'
newline|'\n'
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
DECL|member|get_request_extensions
dedent|''
name|'def'
name|'get_request_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_exts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_goose_handler
name|'def'
name|'_goose_handler'
op|'('
name|'req'
op|','
name|'res'
op|')'
op|':'
newline|'\n'
comment|'#NOTE: This only handles JSON responses.'
nl|'\n'
comment|'# You can use content type header to test for XML.'
nl|'\n'
indent|'            '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'googoose'"
op|']'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'chewing'"
op|')'
newline|'\n'
name|'res'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
dedent|''
name|'req_ext1'
op|'='
name|'extensions'
op|'.'
name|'RequestExtension'
op|'('
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.1/:(project_id)/flavors/:(id)'"
op|','
nl|'\n'
name|'_goose_handler'
op|')'
newline|'\n'
name|'request_exts'
op|'.'
name|'append'
op|'('
name|'req_ext1'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_bands_handler
name|'def'
name|'_bands_handler'
op|'('
name|'req'
op|','
name|'res'
op|')'
op|':'
newline|'\n'
comment|'#NOTE: This only handles JSON responses.'
nl|'\n'
comment|'# You can use content type header to test for XML.'
nl|'\n'
indent|'            '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'big_bands'"
op|']'
op|'='
string|"'Pig Bands!'"
newline|'\n'
name|'res'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
dedent|''
name|'req_ext2'
op|'='
name|'extensions'
op|'.'
name|'RequestExtension'
op|'('
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.1/:(project_id)/flavors/:(id)'"
op|','
nl|'\n'
name|'_bands_handler'
op|')'
newline|'\n'
name|'request_exts'
op|'.'
name|'append'
op|'('
name|'req_ext2'
op|')'
newline|'\n'
name|'return'
name|'request_exts'
newline|'\n'
nl|'\n'
DECL|member|_add_tweedle
dedent|''
name|'def'
name|'_add_tweedle'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'return'
string|'"Tweedle Beetle Added."'
newline|'\n'
nl|'\n'
DECL|member|_delete_tweedle
dedent|''
name|'def'
name|'_delete_tweedle'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'return'
string|'"Tweedle Beetle Deleted."'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
