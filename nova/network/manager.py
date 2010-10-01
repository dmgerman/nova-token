begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nNetwork Hosts are responsible for allocating ips and setting up network\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'math'
newline|'\n'
nl|'\n'
name|'import'
name|'IPy'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
name|'DEFINE_string'
op|'('
string|"'flat_network_bridge'"
op|','
string|"'br100'"
op|','
nl|'\n'
string|"'Bridge for simple network instances'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_dns'"
op|','
string|"'8.8.4.4'"
op|','
nl|'\n'
string|"'Dns for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'vlan_start'"
op|','
number|'100'
op|','
string|"'First VLAN for private networks'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'num_networks'"
op|','
number|'1000'
op|','
string|"'Number of networks to support'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vpn_ip'"
op|','
name|'utils'
op|'.'
name|'get_my_ip'
op|'('
op|')'
op|','
nl|'\n'
string|"'Public IP for the cloudpipe VPN servers'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'vpn_start'"
op|','
number|'1000'
op|','
string|"'First Vpn port for private networks'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'network_size'"
op|','
number|'256'
op|','
nl|'\n'
string|"'Number of addresses in each private subnet'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'floating_range'"
op|','
string|"'4.4.4.0/24'"
op|','
string|"'Floating IP address block'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'fixed_range'"
op|','
string|"'10.0.0.0/8'"
op|','
string|"'Fixed IP address block'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'cnt_vpn_clients'"
op|','
number|'5'
op|','
nl|'\n'
string|"'Number of addresses reserved for vpn clients'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'network_driver'"
op|','
string|"'nova.network.linux_net'"
op|','
nl|'\n'
string|"'Driver to use for network creation'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'update_dhcp_on_disassociate'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Whether to update dhcp when fixed_ip is disassociated'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'fixed_ip_disassociate_timeout'"
op|','
number|'600'
op|','
nl|'\n'
string|"'Seconds after which a deallocated ip is disassociated'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AddressAlreadyAllocated
name|'class'
name|'AddressAlreadyAllocated'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Address was already allocated"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkManager
dedent|''
name|'class'
name|'NetworkManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements common network manager functionality\n\n    This class must be subclassed.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'network_driver'
op|'='
name|'None'
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
name|'if'
name|'not'
name|'network_driver'
op|':'
newline|'\n'
indent|'            '
name|'network_driver'
op|'='
name|'FLAGS'
op|'.'
name|'network_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'network_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'NetworkManager'
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
DECL|member|set_network_host
dedent|''
name|'def'
name|'set_network_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Safely sets the host of the network"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"setting network host"'
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_set_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'network_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_on_set_network_host'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'return'
name|'host'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
string|'"""Gets a fixed ip from the pool"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
string|'"""Returns a fixed ip to the pool"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_fixed_ip
dedent|''
name|'def'
name|'setup_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up rules for fixed ip"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_set_network_host
dedent|''
name|'def'
name|'_on_set_network_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when this host becomes the host for a network"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_compute_network
dedent|''
name|'def'
name|'setup_compute_network'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
dedent|''
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets an floating ip from the pool"""'
newline|'\n'
comment|'# TODO(vish): add floating ips through manage command'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_floating_ip
dedent|''
name|'def'
name|'associate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates an floating ip to a fixed ip"""'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_address'
op|','
nl|'\n'
name|'fixed_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'bind_floating_ip'
op|'('
name|'floating_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_floating_forward'
op|'('
name|'floating_address'
op|','
name|'fixed_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_floating_ip
dedent|''
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociates a floating ip"""'
newline|'\n'
name|'fixed_address'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_disassociate'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'unbind_floating_ip'
op|'('
name|'floating_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'remove_floating_forward'
op|'('
name|'floating_address'
op|','
name|'fixed_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_floating_ip
dedent|''
name|'def'
name|'deallocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an floating ip to the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'floating_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network
dedent|''
name|'def'
name|'get_network'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the network for the current context"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_networks
dedent|''
name|'def'
name|'create_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'num_networks'
op|','
name|'network_size'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create networks based on parameters"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_bottom_reserved_ips
name|'def'
name|'_bottom_reserved_ips'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'"""Number of reserved ips at the bottom of the range"""'
newline|'\n'
name|'return'
number|'2'
comment|'# network, gateway'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_top_reserved_ips
name|'def'
name|'_top_reserved_ips'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=R0201'
newline|'\n'
indent|'        '
string|'"""Number of reserved ips at the top of the range"""'
newline|'\n'
name|'return'
number|'1'
comment|'# broadcast'
newline|'\n'
nl|'\n'
DECL|member|_create_fixed_ips
dedent|''
name|'def'
name|'_create_fixed_ips'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create all fixed ips for network"""'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
comment|'# NOTE(vish): Should these be properties of the network as opposed'
nl|'\n'
comment|'#             to properties of the manager class?'
nl|'\n'
name|'bottom_reserved'
op|'='
name|'self'
op|'.'
name|'_bottom_reserved_ips'
newline|'\n'
name|'top_reserved'
op|'='
name|'self'
op|'.'
name|'_top_reserved_ips'
newline|'\n'
name|'project_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'network_ref'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'num_ips'
op|'='
name|'len'
op|'('
name|'project_net'
op|')'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'range'
op|'('
name|'num_ips'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
name|'if'
name|'index'
op|'<'
name|'bottom_reserved'
name|'or'
name|'num_ips'
op|'-'
name|'index'
op|'<'
name|'top_reserved'
op|':'
newline|'\n'
indent|'                '
name|'reserved'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'reserved'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'context'
op|','
op|'{'
string|"'network_id'"
op|':'
name|'network_id'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'reserved'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlatManager
dedent|''
dedent|''
dedent|''
name|'class'
name|'FlatManager'
op|'('
name|'NetworkManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Basic network where no vlans are used"""'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
string|'"""Gets a fixed ip from the pool"""'
newline|'\n'
comment|'# TODO(vish): when this is called by compute, we can associate compute'
nl|'\n'
comment|'#             with a network, or a cluster of computes with a network'
nl|'\n'
comment|'#             and use that network here with a method like'
nl|'\n'
comment|'#             network_get_by_compute_host'
nl|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_get_by_bridge'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_associate_pool'
op|'('
name|'context'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'address'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
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
string|'"""Returns a fixed ip to the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_compute_network
dedent|''
name|'def'
name|'setup_compute_network'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Network is created manually"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|setup_fixed_ip
dedent|''
name|'def'
name|'setup_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Currently no setup"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_networks
dedent|''
name|'def'
name|'create_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|','
name|'num_networks'
op|','
name|'network_size'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create networks based on parameters"""'
newline|'\n'
name|'fixed_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'range'
op|'('
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'start'
op|'='
name|'index'
op|'*'
name|'network_size'
newline|'\n'
name|'significant_bits'
op|'='
number|'32'
op|'-'
name|'int'
op|'('
name|'math'
op|'.'
name|'log'
op|'('
name|'network_size'
op|','
number|'2'
op|')'
op|')'
newline|'\n'
name|'cidr'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'fixed_net'
op|'['
name|'start'
op|']'
op|','
name|'significant_bits'
op|')'
newline|'\n'
name|'project_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'net'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'net'
op|'['
string|"'netmask'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'netmask'
op|'('
op|')'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'broadcast'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'broadcast'
op|'('
op|')'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'dhcp_start'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
name|'context'
op|','
name|'net'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_network'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the network for the current context"""'
newline|'\n'
comment|'# NOTE(vish): To support mutilple network hosts, This could randomly'
nl|'\n'
comment|'#             select from multiple networks instead of just'
nl|'\n'
comment|'#             returning the one. It could also potentially be done'
nl|'\n'
comment|'#             in the scheduler.'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_get_by_bridge'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_set_network_host
dedent|''
name|'def'
name|'_on_set_network_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when this host becomes the host for a network"""'
newline|'\n'
name|'net'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net'
op|'['
string|"'injected'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'net'
op|'['
string|"'bridge'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
newline|'\n'
name|'net'
op|'['
string|"'dns'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_dns'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'net'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|VlanManager
dedent|''
dedent|''
name|'class'
name|'VlanManager'
op|'('
name|'NetworkManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Vlan network with dhcp"""'
newline|'\n'
nl|'\n'
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|periodic_tasks
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval"""'
newline|'\n'
name|'yield'
name|'super'
op|'('
name|'VlanManager'
op|','
name|'self'
op|')'
op|'.'
name|'periodic_tasks'
op|'('
name|'context'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeout'
op|'='
name|'FLAGS'
op|'.'
name|'fixed_ip_disassociate_timeout'
newline|'\n'
name|'time'
op|'='
name|'now'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'timeout'
op|')'
newline|'\n'
name|'num'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_disassociate_all_by_timeout'
op|'('
name|'self'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'time'
op|')'
newline|'\n'
name|'if'
name|'num'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Dissassociated %s stale fixed ip(s)"'
op|','
name|'num'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do any initialization that needs to be run if this is a\n           standalone service.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
string|'"""Gets a fixed ip from the pool"""'
newline|'\n'
comment|'# TODO(vish): This should probably be getting project_id from'
nl|'\n'
comment|'#             the instance, but it is another trip to the db.'
nl|'\n'
comment|'#             Perhaps this method should take an instance_ref.'
nl|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'if'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'vpn'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'network_ref'
op|'['
string|"'vpn_private_address'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_associate_pool'
op|'('
name|'context'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'address'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
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
string|'"""Returns a fixed ip to the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'address'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setup_fixed_ip
dedent|''
name|'def'
name|'setup_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets forwarding rules and dhcp for fixed ip"""'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_is_vpn'
op|'('
name|'context'
op|','
name|'fixed_ip_ref'
op|'['
string|"'instance_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_vlan_forward'
op|'('
name|'network_ref'
op|'['
string|"'vpn_public_address'"
op|']'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'vpn_public_port'"
op|']'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'vpn_private_address'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'update_dhcp'
op|'('
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lease_fixed_ip
dedent|''
name|'def'
name|'lease_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'mac'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by dhcp-bridge when ip is leased"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Leasing IP %s"'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'fixed_ip_ref'
op|'['
string|"'instance'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'instance_ref'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"IP %s leased that isn\'t associated"'
op|'%'
nl|'\n'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|'!='
name|'mac'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"IP %s leased to bad mac %s vs %s"'
op|'%'
nl|'\n'
op|'('
name|'address'
op|','
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
name|'mac'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'fixed_ip_ref'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'leased'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"IP %s leased that was already deallocated"'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_fixed_ip
dedent|''
dedent|''
name|'def'
name|'release_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'mac'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by dhcp-bridge when ip is released"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Releasing IP %s"'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'fixed_ip_ref'
op|'['
string|"'instance'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'instance_ref'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"IP %s released that isn\'t associated"'
op|'%'
nl|'\n'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|'!='
name|'mac'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"IP %s released from bad mac %s vs %s"'
op|'%'
nl|'\n'
op|'('
name|'address'
op|','
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
name|'mac'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'fixed_ip_ref'
op|'['
string|"'leased'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"IP %s released that was not leased"'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'fixed_ip_ref'
op|'['
string|"'str_id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'leased'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
comment|"# NOTE(vish): dhcp server isn't updated until next setup, this"
nl|'\n'
comment|'#             means there will stale entries in the conf file'
nl|'\n'
comment|'#             the code below will update the file if necessary'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'update_dhcp_on_disassociate'
op|':'
newline|'\n'
indent|'                '
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'update_dhcp'
op|'('
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_compute_network
dedent|''
dedent|''
dedent|''
name|'def'
name|'setup_compute_network'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'network_ref'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|restart_nets
dedent|''
name|'def'
name|'restart_nets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the network for each user is enabled"""'
newline|'\n'
comment|'# TODO(vish): Implement this'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_networks
dedent|''
name|'def'
name|'create_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|','
name|'num_networks'
op|','
name|'network_size'
op|','
nl|'\n'
name|'vlan_start'
op|','
name|'vpn_start'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create networks based on parameters"""'
newline|'\n'
name|'fixed_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'range'
op|'('
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vlan'
op|'='
name|'vlan_start'
op|'+'
name|'index'
newline|'\n'
name|'start'
op|'='
name|'index'
op|'*'
name|'network_size'
newline|'\n'
name|'significant_bits'
op|'='
number|'32'
op|'-'
name|'int'
op|'('
name|'math'
op|'.'
name|'log'
op|'('
name|'network_size'
op|','
number|'2'
op|')'
op|')'
newline|'\n'
name|'cidr'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'fixed_net'
op|'['
name|'start'
op|']'
op|','
name|'significant_bits'
op|')'
newline|'\n'
name|'project_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'net'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'net'
op|'['
string|"'netmask'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'netmask'
op|'('
op|')'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'broadcast'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'broadcast'
op|'('
op|')'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'vpn_private_address'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'dhcp_start'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'vlan'"
op|']'
op|'='
name|'vlan'
newline|'\n'
name|'net'
op|'['
string|"'bridge'"
op|']'
op|'='
string|"'br%s'"
op|'%'
name|'vlan'
newline|'\n'
comment|'# NOTE(vish): This makes ports unique accross the cloud, a more'
nl|'\n'
comment|'#             robust solution would be to make them unique per ip'
nl|'\n'
name|'net'
op|'['
string|"'vpn_public_port'"
op|']'
op|'='
name|'vpn_start'
op|'+'
name|'index'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
name|'context'
op|','
name|'net'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_network
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_network'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the network for the current context"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_set_network_host
dedent|''
name|'def'
name|'_on_set_network_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when this host becomes the host for a network"""'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'net'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net'
op|'['
string|"'vpn_public_address'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_ip'
newline|'\n'
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'net'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'network_ref'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_bottom_reserved_ips
name|'def'
name|'_bottom_reserved_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Number of reserved ips at the bottom of the range"""'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'VlanManager'
op|','
name|'self'
op|')'
op|'.'
name|'_bottom_reserved_ips'
op|'+'
number|'1'
comment|'# vpn server'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_top_reserved_ips
name|'def'
name|'_top_reserved_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Number of reserved ips at the top of the range"""'
newline|'\n'
name|'parent_reserved'
op|'='
name|'super'
op|'('
name|'VlanManager'
op|','
name|'self'
op|')'
op|'.'
name|'_top_reserved_ips'
newline|'\n'
name|'return'
name|'parent_reserved'
op|'+'
name|'FLAGS'
op|'.'
name|'cnt_vpn_clients'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
