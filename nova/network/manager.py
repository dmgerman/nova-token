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
name|'logging'
newline|'\n'
name|'import'
name|'math'
newline|'\n'
nl|'\n'
name|'import'
name|'IPy'
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
name|'DEFINE_list'
op|'('
string|"'flat_network_ips'"
op|','
nl|'\n'
op|'['
string|"'192.168.0.2'"
op|','
string|"'192.168.0.3'"
op|','
string|"'192.168.0.4'"
op|']'
op|','
nl|'\n'
string|"'Available ips for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_network'"
op|','
string|"'192.168.0.0'"
op|','
nl|'\n'
string|"'Network for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_netmask'"
op|','
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'Netmask for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_gateway'"
op|','
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'Broadcast for simple network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'flat_network_broadcast'"
op|','
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'Broadcast for simple network'"
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
string|"'public_range'"
op|','
string|"'4.4.4.0/24'"
op|','
string|"'Public IP address block'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'private_range'"
op|','
string|"'10.0.0.0/8'"
op|','
string|"'Private IP address block'"
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
string|"'Whether to update dhcp when fixed_ip is disassocated'"
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
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Safely sets the host of the projects network"""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"setting network host"'
op|')'
newline|'\n'
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
name|'project_id'
op|')'
newline|'\n'
comment|'# TODO(vish): can we minimize db access by just getting the'
nl|'\n'
comment|'#             id here instead of the ref?'
nl|'\n'
name|'network_id'
op|'='
name|'network_ref'
op|'['
string|"'id'"
op|']'
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
string|'"""Called when this host becomes the host for a project"""'
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
name|'project_id'
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
comment|'# NOTE(vish): should these be properties of the network as opposed'
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
name|'project_id'
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
string|'"""Called when this host becomes the host for a project"""'
newline|'\n'
comment|'# NOTE(vish): should there be two types of network objects'
nl|'\n'
comment|'#             in the datastore?'
nl|'\n'
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
string|"'network_str'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_network'
newline|'\n'
name|'net'
op|'['
string|"'netmask'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_netmask'
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
string|"'gateway'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_gateway'
newline|'\n'
name|'net'
op|'['
string|"'broadcast'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'flat_network_broadcast'
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
comment|'# NOTE(vish): Rignt now we are putting  all of the fixed ips in'
nl|'\n'
comment|'#             one large pool, but ultimately it may be better to'
nl|'\n'
comment|'#             have each network manager have its own network that'
nl|'\n'
comment|'#             it is responsible for and its own pool of ips.'
nl|'\n'
name|'for'
name|'address'
name|'in'
name|'FLAGS'
op|'.'
name|'flat_network_ips'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'context'
op|','
op|'{'
string|"'address'"
op|':'
name|'address'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VlanManager
dedent|''
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
name|'if'
name|'not'
name|'fixed_ip_ref'
op|'['
string|"'leased'"
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
nl|'\n'
DECL|member|setup_fixed_ip
dedent|''
dedent|''
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
name|'return'
newline|'\n'
dedent|''
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
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
string|"'str_id'"
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
nl|'\n'
DECL|member|release_fixed_ip
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
name|'return'
newline|'\n'
dedent|''
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|','
name|'address'
op|')'
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
DECL|member|allocate_network
dedent|''
dedent|''
dedent|''
name|'def'
name|'allocate_network'
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
string|'"""Set up the network"""'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_indexes'
op|'('
name|'context'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_create'
op|'('
name|'context'
op|','
op|'{'
string|"'project_id'"
op|':'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'network_id'
op|'='
name|'network_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'private_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'FLAGS'
op|'.'
name|'private_range'
op|')'
newline|'\n'
name|'index'
op|'='
name|'db'
op|'.'
name|'network_get_index'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'vlan'
op|'='
name|'FLAGS'
op|'.'
name|'vlan_start'
op|'+'
name|'index'
newline|'\n'
name|'start'
op|'='
name|'index'
op|'*'
name|'FLAGS'
op|'.'
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
name|'FLAGS'
op|'.'
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
name|'private_net'
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
nl|'\n'
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
comment|'# NOTE(vish): we could turn these into properties'
nl|'\n'
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
name|'net'
op|'['
string|"'vpn_public_address'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_ip'
newline|'\n'
name|'net'
op|'['
string|"'vpn_public_port'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_start'
op|'+'
name|'index'
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
name|'_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'return'
name|'network_id'
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
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
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
name|'project_id'
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
DECL|member|_ensure_indexes
dedent|''
name|'def'
name|'_ensure_indexes'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the indexes for the network exist\n\n        This could use a manage command instead of keying off of a flag"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_index_count'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'index'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'network_index_create_safe'
op|'('
name|'context'
op|','
op|'{'
string|"'index'"
op|':'
name|'index'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_set_network_host
dedent|''
dedent|''
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
string|'"""Called when this host becomes the host for a project"""'
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
