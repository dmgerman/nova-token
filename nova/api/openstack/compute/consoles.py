begin_unit
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'api'
name|'as'
name|'console_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_keys
name|'def'
name|'_translate_keys'
op|'('
name|'cons'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Coerces a console instance into proper dictionary format."""'
newline|'\n'
name|'pool'
op|'='
name|'cons'
op|'['
string|"'pool'"
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'id'"
op|':'
name|'cons'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'pool'
op|'['
string|"'console_type'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'console'
op|'='
name|'info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_detail_keys
dedent|''
name|'def'
name|'_translate_detail_keys'
op|'('
name|'cons'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Coerces a console instance into proper dictionary format with\n    correctly mapped attributes.\n    """'
newline|'\n'
name|'pool'
op|'='
name|'cons'
op|'['
string|"'pool'"
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'id'"
op|':'
name|'cons'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'pool'
op|'['
string|"'console_type'"
op|']'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'cons'
op|'['
string|"'password'"
op|']'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'cons'
op|'['
string|"'instance_name'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'cons'
op|'['
string|"'port'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'pool'
op|'['
string|"'public_hostname'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'console'
op|'='
name|'info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleTemplate
dedent|''
name|'class'
name|'ConsoleTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'console'"
op|','
name|'selector'
op|'='
string|"'console'"
op|')'
newline|'\n'
nl|'\n'
name|'id_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'id'"
op|','
name|'selector'
op|'='
string|"'id'"
op|')'
newline|'\n'
name|'id_elem'
op|'.'
name|'text'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'port_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'port'"
op|','
name|'selector'
op|'='
string|"'port'"
op|')'
newline|'\n'
name|'port_elem'
op|'.'
name|'text'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'host_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'host'"
op|','
name|'selector'
op|'='
string|"'host'"
op|')'
newline|'\n'
name|'host_elem'
op|'.'
name|'text'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'passwd_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'password'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'password'"
op|')'
newline|'\n'
name|'passwd_elem'
op|'.'
name|'text'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'constype_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'console_type'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'console_type'"
op|')'
newline|'\n'
name|'constype_elem'
op|'.'
name|'text'
op|'='
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesTemplate
dedent|''
dedent|''
name|'class'
name|'ConsolesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'consoles'"
op|')'
newline|'\n'
name|'console'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'console'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'consoles'"
op|')'
newline|'\n'
name|'console'
op|'.'
name|'append'
op|'('
name|'ConsoleTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Consoles controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'console_api'
op|'='
name|'console_api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ConsolesTemplate'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of consoles for this instance."""'
newline|'\n'
name|'consoles'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_consoles'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'consoles'
op|'='
op|'['
name|'_translate_keys'
op|'('
name|'console'
op|')'
nl|'\n'
name|'for'
name|'console'
name|'in'
name|'consoles'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new console."""'
newline|'\n'
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'create_console'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ConsoleTemplate'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shows in-depth information on a specific console."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'console'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_console'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_translate_detail_keys'
op|'('
name|'console'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a console."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'delete_console'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
