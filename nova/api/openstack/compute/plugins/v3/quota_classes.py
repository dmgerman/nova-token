begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'quota_classes'
newline|'\n'
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
name|'import'
name|'validation'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-quota-class-sets"'
newline|'\n'
nl|'\n'
comment|'# Quotas that are only enabled by specific extensions'
nl|'\n'
DECL|variable|EXTENDED_QUOTAS
name|'EXTENDED_QUOTAS'
op|'='
op|'{'
string|"'server_groups'"
op|':'
string|"'os-server-group-quotas'"
op|','
nl|'\n'
string|"'server_group_members'"
op|':'
string|"'os-server-group-quotas'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClassSetsController
name|'class'
name|'QuotaClassSetsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|supported_quotas
indent|'    '
name|'supported_quotas'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'supported_quotas'
op|'='
name|'QUOTAS'
op|'.'
name|'resources'
newline|'\n'
name|'extension_info'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'extension_info'"
op|')'
op|'.'
name|'get_extensions'
op|'('
op|')'
newline|'\n'
name|'for'
name|'resource'
op|','
name|'extension'
name|'in'
name|'EXTENDED_QUOTAS'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'extension'
name|'not'
name|'in'
name|'extension_info'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'supported_quotas'
op|'.'
name|'remove'
op|'('
name|'resource'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_quota_set
dedent|''
dedent|''
dedent|''
name|'def'
name|'_format_quota_set'
op|'('
name|'self'
op|','
name|'quota_class'
op|','
name|'quota_set'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the quota object to a result dict."""'
newline|'\n'
nl|'\n'
name|'if'
name|'quota_class'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'str'
op|'('
name|'quota_class'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'resource'
name|'in'
name|'self'
op|'.'
name|'supported_quotas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'resource'
name|'in'
name|'quota_set'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'resource'
op|']'
op|'='
name|'quota_set'
op|'['
name|'resource'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'dict'
op|'('
name|'quota_class_set'
op|'='
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'show'"
op|','
name|'target'
op|'='
op|'{'
string|"'quota_class'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_class_quotas'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'quota_classes'
op|'.'
name|'update'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'update'"
op|','
name|'target'
op|'='
op|'{'
string|"'quota_class'"
op|':'
name|'id'
op|'}'
op|')'
newline|'\n'
name|'quota_class'
op|'='
name|'id'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'body'
op|'['
string|"'quota_class_set'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'quota_class_update'
op|'('
name|'context'
op|','
name|'quota_class'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'QuotaClassNotFound'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'quota_class_create'
op|'('
name|'context'
op|','
name|'quota_class'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_class_quotas'
op|'('
name|'context'
op|','
name|'quota_class'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'None'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClasses
dedent|''
dedent|''
name|'class'
name|'QuotaClasses'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quota classes management support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"QuotaClasses"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
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
op|']'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'ALIAS'
op|','
nl|'\n'
name|'QuotaClassSetsController'
op|'('
name|'extension_info'
op|'='
name|'self'
op|'.'
name|'extension_info'
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
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
