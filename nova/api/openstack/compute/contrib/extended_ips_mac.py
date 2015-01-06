begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
string|'"""The Extended Ips API extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'extended_ips_mac'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedIpsMacController
name|'class'
name|'ExtendedIpsMacController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ExtendedIpsMacController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extend_server
dedent|''
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"%s:mac_addr"'
op|'%'
name|'Extended_ips_mac'
op|'.'
name|'alias'
newline|'\n'
name|'networks'
op|'='
name|'common'
op|'.'
name|'get_networks_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'for'
name|'label'
op|','
name|'network'
name|'in'
name|'networks'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): ips are hidden in some states via the'
nl|'\n'
comment|'#             hide_server_addresses extension.'
nl|'\n'
indent|'            '
name|'if'
name|'label'
name|'in'
name|'server'
op|'['
string|"'addresses'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'all_ips'
op|'='
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'network'
op|'['
string|'"ips"'
op|']'
op|','
nl|'\n'
name|'network'
op|'['
string|'"floating_ips"'
op|']'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'ip'
name|'in'
name|'enumerate'
op|'('
name|'all_ips'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'server'
op|'['
string|"'addresses'"
op|']'
op|'['
name|'label'
op|']'
op|'['
name|'i'
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'ip'
op|'['
string|"'mac_address'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'show' method."
nl|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'detail' method."
nl|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Extended_ips_mac
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Extended_ips_mac'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds mac address parameter to the ip list."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ExtendedIpsMac"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"OS-EXT-IPS-MAC"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"extended_ips_mac/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-03-07T00:00:00Z"'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'ExtendedIpsMacController'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
dedent|''
dedent|''
endmarker|''
end_unit
