begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
op|'.'
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
name|'extensions'
newline|'\n'
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
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_ext
name|'def'
name|'make_ext'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'namespace'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'alias'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'version'"
op|')'
newline|'\n'
nl|'\n'
name|'desc'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'description'"
op|')'
newline|'\n'
name|'desc'
op|'.'
name|'text'
op|'='
string|"'description'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ext_nsmap
dedent|''
name|'ext_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_COMMON_V10'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionTemplate
name|'class'
name|'ExtensionTemplate'
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
string|"'extension'"
op|','
name|'selector'
op|'='
string|"'extension'"
op|')'
newline|'\n'
name|'make_ext'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'ext_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsTemplate
dedent|''
dedent|''
name|'class'
name|'ExtensionsTemplate'
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
string|"'extensions'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'extension'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'extensions'"
op|')'
newline|'\n'
name|'make_ext'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'ext_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfoController
dedent|''
dedent|''
name|'class'
name|'ExtensionInfoController'
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
name|'extension_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extension_info'
op|'='
name|'extension_info'
newline|'\n'
nl|'\n'
DECL|member|_translate
dedent|''
name|'def'
name|'_translate'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'ext_data'
op|'['
string|"'name'"
op|']'
op|'='
name|'ext'
op|'.'
name|'name'
newline|'\n'
name|'ext_data'
op|'['
string|"'alias'"
op|']'
op|'='
name|'ext'
op|'.'
name|'alias'
newline|'\n'
name|'ext_data'
op|'['
string|"'description'"
op|']'
op|'='
name|'ext'
op|'.'
name|'__doc__'
newline|'\n'
name|'ext_data'
op|'['
string|"'namespace'"
op|']'
op|'='
name|'ext'
op|'.'
name|'namespace'
newline|'\n'
name|'ext_data'
op|'['
string|"'version'"
op|']'
op|'='
name|'ext'
op|'.'
name|'version'
newline|'\n'
name|'return'
name|'ext_data'
newline|'\n'
nl|'\n'
DECL|member|_get_extensions
dedent|''
name|'def'
name|'_get_extensions'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter extensions list based on policy."""'
newline|'\n'
nl|'\n'
name|'discoverable_extensions'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'alias'
op|','
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extension_info'
op|'.'
name|'get_extensions'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
nl|'\n'
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'alias'
op|')'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'discoverable'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'discoverable_extensions'
op|'['
name|'alias'
op|']'
op|'='
name|'ext'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filter out extension %s from discover list"'
op|')'
op|','
nl|'\n'
name|'alias'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'discoverable_extensions'
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
name|'ExtensionsTemplate'
op|')'
newline|'\n'
DECL|member|index
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
name|'sorted_ext_list'
op|'='
name|'sorted'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_extensions'
op|'('
name|'context'
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'_alias'
op|','
name|'ext'
name|'in'
name|'sorted_ext_list'
op|':'
newline|'\n'
indent|'            '
name|'extensions'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extensions'
op|'='
name|'extensions'
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
name|'ExtensionTemplate'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|"# NOTE(dprince): the extensions alias is used as the 'id' for show"
nl|'\n'
indent|'            '
name|'ext'
op|'='
name|'self'
op|'.'
name|'_get_extensions'
op|'('
name|'context'
op|')'
op|'['
name|'id'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'extension'
op|'='
name|'self'
op|'.'
name|'_translate'
op|'('
name|'ext'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfo
dedent|''
dedent|''
name|'class'
name|'ExtensionInfo'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extension information."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"extensions"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"extensions"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/core/extension_info/api/v3"'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
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
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'extensions'"
op|','
name|'ExtensionInfoController'
op|'('
name|'self'
op|'.'
name|'extension_info'
op|')'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'extension'"
op|')'
op|']'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
