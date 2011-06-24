begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 Eldar Nugaev, Kirill Shileev, Ilya Alekseyev'
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
comment|'#    under the License'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
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
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ip_view
name|'def'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
string|"'id'"
op|':'
name|'floating_ip'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'ip'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
newline|'\n'
name|'if'
string|"'fixed_ip'"
name|'in'
name|'floating_ip'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
string|"'instance'"
name|'in'
name|'floating_ip'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'floating_ip'
op|'['
string|"'instance'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'floating_ip'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_floating_ips_view
dedent|''
name|'def'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'floating_ips'"
op|':'
op|'['
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'floating_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPController
dedent|''
name|'class'
name|'FloatingIPController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Floating IPs API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"floating_ip"'
op|':'
op|'['
nl|'\n'
string|'"id"'
op|','
nl|'\n'
string|'"ip"'
op|','
nl|'\n'
string|'"instance_id"'
op|','
nl|'\n'
string|'"fixed_ip"'
op|','
nl|'\n'
op|']'
op|'}'
op|'}'
op|'}'
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
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIPController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
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
string|'"""Return data about the given floating ip."""'
newline|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
name|'floating_ips'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'list'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_floating_ips_view'
op|'('
name|'floating_ips'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'context'
op|')'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip_by_ip'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ex'
op|'.'
name|'exc_type'
op|'=='
string|"'NoMoreAddresses'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NoMoreFloatingIps'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
string|"'allocated'"
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'ip'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
name|'ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
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
nl|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'release_floating_ip'
op|'('
name|'context'
op|','
name|'address'
op|'='
name|'ip'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'released'"
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'ip'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
name|'ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|associate
dedent|''
name|'def'
name|'associate'
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
string|'""" /floating_ips/{id}/associate  fixed ip in body """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'_get_ip_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ip'
op|'='
name|'body'
op|'['
string|"'associate_address'"
op|']'
op|'['
string|"'fixed_ip'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate_floating_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'associated'"
op|':'
nl|'\n'
op|'{'
nl|'\n'
string|'"floating_ip_id"'
op|':'
name|'id'
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
name|'floating_ip'
op|','
nl|'\n'
string|'"fixed_ip"'
op|':'
name|'fixed_ip'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|disassociate
dedent|''
name|'def'
name|'disassociate'
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
string|'""" POST /floating_ips/{id}/disassociate """'
newline|'\n'
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
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'_get_ip_by_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'context'
op|','
name|'floating_ip'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'disassociated'"
op|':'
name|'floating_ip'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_ip_by_id
dedent|''
name|'def'
name|'_get_ip_by_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks that value is id and then returns its address."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'value'
op|')'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Floating_ips
dedent|''
dedent|''
name|'class'
name|'Floating_ips'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
DECL|member|get_name
indent|'    '
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Floating_ips"'
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
string|'"FLOATING_IPS"'
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
string|'"Floating IPs support"'
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
string|'"http://docs.openstack.org/ext/floating_ips/api/v1.1"'
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
string|'"2011-06-16T00:00:00+00:00"'
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
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'floating_ips'"
op|','
nl|'\n'
name|'FloatingIPController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
nl|'\n'
string|"'associate'"
op|':'
string|"'POST'"
op|','
nl|'\n'
string|"'disassociate'"
op|':'
string|"'POST'"
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
