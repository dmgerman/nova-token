begin_unit
comment|'# Copyright 2011 Nicira Networks, Inc'
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
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'ipv6'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ipam_lib
name|'def'
name|'get_ipam_lib'
op|'('
name|'net_man'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'NeutronNovaIPAMLib'
op|'('
name|'net_man'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NeutronNovaIPAMLib
dedent|''
name|'class'
name|'NeutronNovaIPAMLib'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements Neutron IP Address Management (IPAM) interface\n       using the local Nova database.  This implementation is inline\n       with how IPAM is used by other NetworkManagers.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'net_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Holds a reference to the "parent" network manager, used\n           to take advantage of various FlatManager methods to avoid\n           code duplication.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'net_manager'
op|'='
name|'net_manager'
newline|'\n'
nl|'\n'
DECL|member|get_subnets_by_net_id
dedent|''
name|'def'
name|'get_subnets_by_net_id'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|','
name|'_vif_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns information about the IPv4 and IPv6 subnets\n           associated with a Neutron Network UUID.\n        """'
newline|'\n'
name|'n'
op|'='
name|'objects'
op|'.'
name|'Network'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'subnet_v4'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
name|'n'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'n'
op|'.'
name|'cidr'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'n'
op|'.'
name|'gateway'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'getattr'
op|'('
name|'n'
op|','
string|"'dhcp_server'"
op|')'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'n'
op|'.'
name|'broadcast'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'n'
op|'.'
name|'netmask'
op|','
nl|'\n'
string|"'version'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'n'
op|'.'
name|'dns1'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'n'
op|'.'
name|'dns2'
op|'}'
newline|'\n'
comment|"# TODO(tr3buchet): I'm noticing we've assumed here that all dns is v4."
nl|'\n'
comment|'#                  this is probably bad as there is no way to add v6'
nl|'\n'
comment|'#                  dns to nova'
nl|'\n'
name|'subnet_v6'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
name|'n'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'n'
op|'.'
name|'cidr_v6'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'n'
op|'.'
name|'gateway_v6'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'n'
op|'.'
name|'netmask_v6'
op|','
nl|'\n'
string|"'version'"
op|':'
number|'6'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|ips_to_strs
name|'def'
name|'ips_to_strs'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'net'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'netaddr'
op|'.'
name|'ip'
op|'.'
name|'BaseIP'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'net'
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
dedent|''
name|'return'
name|'net'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'ips_to_strs'
op|'('
name|'subnet_v4'
op|')'
op|','
name|'ips_to_strs'
op|'('
name|'subnet_v6'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_routes_by_ip_block
dedent|''
name|'def'
name|'get_routes_by_ip_block'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'block_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of routes for the IP block."""'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_v4_ips_by_interface
dedent|''
name|'def'
name|'get_v4_ips_by_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of IPv4 address strings associated with\n           the specified virtual interface, based on the fixed_ips table.\n        """'
newline|'\n'
comment|'# TODO(tr3buchet): link fixed_ips to vif by uuid so only 1 db call'
nl|'\n'
name|'vif_rec'
op|'='
name|'objects'
op|'.'
name|'VirtualInterface'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'vif_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vif_rec'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'fixed_ips'
op|'='
name|'objects'
op|'.'
name|'FixedIPList'
op|'.'
name|'get_by_virtual_interface_id'
op|'('
nl|'\n'
name|'context'
op|','
name|'vif_rec'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'return'
op|'['
name|'str'
op|'('
name|'fixed_ip'
op|'.'
name|'address'
op|')'
name|'for'
name|'fixed_ip'
name|'in'
name|'fixed_ips'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_v6_ips_by_interface
dedent|''
name|'def'
name|'get_v6_ips_by_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net_id'
op|','
name|'vif_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list containing a single IPv6 address strings\n           associated with the specified virtual interface.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'objects'
op|'.'
name|'Network'
op|'.'
name|'get_by_uuid'
op|'('
name|'admin_context'
op|','
name|'net_id'
op|')'
newline|'\n'
name|'vif_rec'
op|'='
name|'objects'
op|'.'
name|'VirtualInterface'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'vif_id'
op|')'
newline|'\n'
name|'if'
name|'network'
op|'.'
name|'cidr_v6'
name|'and'
name|'vif_rec'
name|'and'
name|'vif_rec'
op|'.'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'ipv6'
op|'.'
name|'to_global'
op|'('
name|'network'
op|'.'
name|'cidr_v6'
op|','
nl|'\n'
name|'vif_rec'
op|'.'
name|'address'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ip'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_fixed_address'
op|'('
nl|'\n'
name|'context'
op|','
name|'fixed_address'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
