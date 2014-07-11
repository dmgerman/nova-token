begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
DECL|variable|network_opts
name|'network_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'share_dhcp_address'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: THIS VALUE SHOULD BE SET WHEN CREATING THE '"
nl|'\n'
string|"'NETWORK. If True in multi_host mode, all compute hosts '"
nl|'\n'
string|"'share the same dhcp address. The same IP address used '"
nl|'\n'
string|"'for DHCP will be added on each nova-network node which '"
nl|'\n'
string|"'is only visible to the vms on the same host.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'network_device_mtu'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: THIS VALUE SHOULD BE SET WHEN CREATING THE '"
nl|'\n'
string|"'NETWORK. MTU setting for network interface.'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'network_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Network
name|'class'
name|'Network'
op|'('
name|'obj_base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added in_use_on_host()'
nl|'\n'
comment|'# Version 1.2: Added mtu, dhcp_server, enable_dhcp, share_address'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'label'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'fields'
op|'.'
name|'IPV4NetworkField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'fields'
op|'.'
name|'IPV6NetworkField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'fields'
op|'.'
name|'IPV6AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'fields'
op|'.'
name|'IPV6AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'vpn_public_port'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'vpn_private_address'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'rxtx_base'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'priority'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'mtu'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'enable_dhcp'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'share_address'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_convert_legacy_ipv6_netmask
name|'def'
name|'_convert_legacy_ipv6_netmask'
op|'('
name|'netmask'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Handle netmask_v6 possibilities from the database.\n\n        Historically, this was stored as just an integral CIDR prefix,\n        but in the future it should be stored as an actual netmask.\n        Be tolerant of either here.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'prefix'
op|'='
name|'int'
op|'('
name|'netmask'
op|')'
newline|'\n'
name|'return'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
string|"'1::/%i'"
op|'%'
name|'prefix'
op|')'
op|'.'
name|'netmask'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'netmask'
op|')'
op|'.'
name|'netmask'
newline|'\n'
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
string|'\'IPv6 netmask "%s" must be a netmask \''
nl|'\n'
string|"'or integral prefix'"
op|'%'
name|'netmask'
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
dedent|''
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_version'
op|'='
name|'tuple'
op|'('
name|'int'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'target_version'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'mtu'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'primitive'
op|'['
string|"'mtu'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'enable_dhcp'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'primitive'
op|'['
string|"'enable_dhcp'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'dhcp_server'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'primitive'
op|'['
string|"'dhcp_server'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'share_address'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'primitive'
op|'['
string|"'share_address'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'network'
op|','
name|'db_network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'network'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'db_value'
op|'='
name|'db_network'
op|'['
name|'field'
op|']'
newline|'\n'
name|'if'
name|'field'
name|'is'
string|"'netmask_v6'"
name|'and'
name|'db_value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'db_value'
op|'='
name|'network'
op|'.'
name|'_convert_legacy_ipv6_netmask'
op|'('
name|'db_value'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'field'
name|'is'
string|"'mtu'"
name|'and'
name|'db_value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'db_value'
op|'='
name|'CONF'
op|'.'
name|'network_device_mtu'
newline|'\n'
dedent|''
name|'if'
name|'field'
name|'is'
string|"'dhcp_server'"
name|'and'
name|'db_value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'db_value'
op|'='
name|'db_network'
op|'['
string|"'gateway'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'field'
name|'is'
string|"'share_address'"
name|'and'
name|'CONF'
op|'.'
name|'share_dhcp_address'
op|':'
newline|'\n'
indent|'                '
name|'db_value'
op|'='
name|'CONF'
op|'.'
name|'share_dhcp_address'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'['
name|'field'
op|']'
op|'='
name|'db_value'
newline|'\n'
dedent|''
name|'network'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'network'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_id'
op|','
name|'project_only'
op|'='
string|"'allow_none'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|','
nl|'\n'
name|'project_only'
op|'='
name|'project_only'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_network'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_get_by_uuid'
op|'('
name|'context'
op|','
name|'network_uuid'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_network'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_cidr
name|'def'
name|'get_by_cidr'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_get_by_cidr'
op|'('
name|'context'
op|','
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_network'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|associate
name|'def'
name|'associate'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'network_id'
op|'='
name|'None'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'network_associate'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'network_id'
op|'='
name|'network_id'
op|','
nl|'\n'
name|'force'
op|'='
name|'force'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|disassociate
name|'def'
name|'disassociate'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_id'
op|','
name|'host'
op|'='
name|'False'
op|','
name|'project'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'network_disassociate'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host'
op|','
name|'project'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|in_use_on_host
name|'def'
name|'in_use_on_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'network_in_use_on_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_primitive_changes
dedent|''
name|'def'
name|'_get_primitive_changes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'changes'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'changes'
op|'['
name|'key'
op|']'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'changes'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'changes'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'_get_primitive_changes'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'id'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_create_safe'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_network'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'network_delete_safe'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deleted'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'deleted'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'_get_primitive_changes'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'netmask_v6'"
name|'in'
name|'updates'
op|':'
newline|'\n'
comment|'# NOTE(danms): For some reason, historical code stores the'
nl|'\n'
comment|'# IPv6 netmask as just the CIDR mask length, so convert that'
nl|'\n'
comment|'# back here before saving for now.'
nl|'\n'
indent|'            '
name|'updates'
op|'['
string|"'netmask_v6'"
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
nl|'\n'
name|'updates'
op|'['
string|"'netmask_v6'"
op|']'
op|')'
op|'.'
name|'netmask'
newline|'\n'
dedent|''
name|'set_host'
op|'='
string|"'host'"
name|'in'
name|'updates'
newline|'\n'
name|'if'
name|'set_host'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'network_set_host'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'host'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'set_host'
op|':'
newline|'\n'
indent|'            '
name|'db_network'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'db_network'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'db_network'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_network'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkList
dedent|''
dedent|''
dedent|''
name|'class'
name|'NetworkList'
op|'('
name|'obj_base'
op|'.'
name|'ObjectListBase'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added get_by_project()'
nl|'\n'
comment|'# Version 1.2: Network <= version 1.2'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Network'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.2'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_only'
op|'='
string|"'allow_none'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_networks'
op|'='
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'context'
op|','
name|'project_only'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Network'
op|','
nl|'\n'
name|'db_networks'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuids
name|'def'
name|'get_by_uuids'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'network_uuids'
op|','
name|'project_only'
op|'='
string|"'allow_none'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_networks'
op|'='
name|'db'
op|'.'
name|'network_get_all_by_uuids'
op|'('
name|'context'
op|','
name|'network_uuids'
op|','
nl|'\n'
name|'project_only'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Network'
op|','
nl|'\n'
name|'db_networks'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host
name|'def'
name|'get_by_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_networks'
op|'='
name|'db'
op|'.'
name|'network_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Network'
op|','
nl|'\n'
name|'db_networks'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_project
name|'def'
name|'get_by_project'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'associate'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_networks'
op|'='
name|'db'
op|'.'
name|'project_get_networks'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'associate'
op|'='
name|'associate'
op|')'
newline|'\n'
name|'return'
name|'obj_base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Network'
op|','
nl|'\n'
name|'db_networks'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
