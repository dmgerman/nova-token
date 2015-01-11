begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'floating_ips_bulk'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'default_floating_pool'"
op|','
string|"'nova.network.floating_ips'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'public_interface'"
op|','
string|"'nova.network.linux_net'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-floating-ips-bulk'"
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPBulkController
name|'class'
name|'FloatingIPBulkController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
string|'"""Return a list of all floating ips."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_floating_ip_info'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
string|'"""Return a list of all floating ips for a given host."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_floating_ip_info'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_floating_ip_info
dedent|''
name|'def'
name|'_get_floating_ip_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip_info'
op|'='
op|'{'
string|'"floating_ip_info"'
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'floating_ips'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoFloatingIpsDefined'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'floating_ip_info'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'floating_ips'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpNotFoundForHost'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
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
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'floating_ip'
name|'in'
name|'floating_ips'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'None'
newline|'\n'
name|'fixed_ip'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'floating_ip'
op|'.'
name|'fixed_ip'
op|':'
newline|'\n'
indent|'                '
name|'instance_uuid'
op|'='
name|'floating_ip'
op|'.'
name|'fixed_ip'
op|'.'
name|'instance_uuid'
newline|'\n'
name|'fixed_ip'
op|'='
name|'str'
op|'('
name|'floating_ip'
op|'.'
name|'fixed_ip'
op|'.'
name|'address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'{'
string|"'address'"
op|':'
name|'str'
op|'('
name|'floating_ip'
op|'.'
name|'address'
op|')'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'floating_ip'
op|'.'
name|'pool'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'floating_ip'
op|'.'
name|'interface'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'floating_ip'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'fixed_ip'
op|'}'
newline|'\n'
name|'floating_ip_info'
op|'['
string|"'floating_ip_info'"
op|']'
op|'.'
name|'append'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'floating_ip_info'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'floating_ips_bulk'
op|'.'
name|'create'
op|')'
newline|'\n'
DECL|member|create
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
string|'"""Bulk create floating ips."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
name|'body'
op|'['
string|"'floating_ips_bulk_create'"
op|']'
newline|'\n'
name|'ip_range'
op|'='
name|'params'
op|'['
string|"'ip_range'"
op|']'
newline|'\n'
nl|'\n'
name|'pool'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'pool'"
op|','
name|'CONF'
op|'.'
name|'default_floating_pool'
op|')'
newline|'\n'
name|'interface'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'interface'"
op|','
name|'CONF'
op|'.'
name|'public_interface'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'='
op|'['
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'make_ip_info'
op|'('
name|'addr'
op|','
name|'pool'
op|','
name|'interface'
op|')'
nl|'\n'
name|'for'
name|'addr'
name|'in'
name|'self'
op|'.'
name|'_address_to_hosts'
op|'('
name|'ip_range'
op|')'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'ips'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpExists'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|'"floating_ips_bulk_create"'
op|':'
op|'{'
string|'"ip_range"'
op|':'
name|'ip_range'
op|','
nl|'\n'
string|'"pool"'
op|':'
name|'pool'
op|','
nl|'\n'
string|'"interface"'
op|':'
name|'interface'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'floating_ips_bulk'
op|'.'
name|'delete'
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
string|'"""Bulk delete floating IPs."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
op|'!='
string|'"delete"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unknown action"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'ip_range'
op|'='
name|'body'
op|'['
string|"'ip_range'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ips'
op|'='
op|'('
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'make_ip_info'
op|'('
name|'address'
op|','
name|'None'
op|','
name|'None'
op|')'
nl|'\n'
name|'for'
name|'address'
name|'in'
name|'self'
op|'.'
name|'_address_to_hosts'
op|'('
name|'ip_range'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'destroy'
op|'('
name|'context'
op|','
name|'ips'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|'"floating_ips_bulk_delete"'
op|':'
name|'ip_range'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_address_to_hosts
dedent|''
name|'def'
name|'_address_to_hosts'
op|'('
name|'self'
op|','
name|'addresses'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Iterate over hosts within an address range.\n\n        If an explicit range specifier is missing, the parameter is\n        interpreted as a specific individual address.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'addresses'
op|')'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'addresses'
op|')'
newline|'\n'
name|'if'
name|'net'
op|'.'
name|'size'
op|'<'
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'reason'
op|'='
name|'_'
op|'('
string|'"/%s should be specified as single address(es) "'
nl|'\n'
string|'"not in cidr format"'
op|')'
op|'%'
name|'net'
op|'.'
name|'prefixlen'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'net'
op|'.'
name|'iter_hosts'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpsBulk
dedent|''
dedent|''
dedent|''
name|'class'
name|'FloatingIpsBulk'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bulk handling of Floating IPs."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FloatingIpsBulk"'
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
name|'resource'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'FloatingIPBulkController'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resource'
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
string|'"""It\'s an abstract function V3APIExtensionBase and the extension\n        will not be loaded without it.\n        """'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
