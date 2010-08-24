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
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
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
string|"'network_type'"
op|','
nl|'\n'
string|"'flat'"
op|','
nl|'\n'
string|"'Service Class for Networking'"
op|')'
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
nl|'\n'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AddressNotAllocated
dedent|''
name|'class'
name|'AddressNotAllocated'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(vish): some better type of dependency injection?'
nl|'\n'
DECL|variable|_driver
dedent|''
name|'_driver'
op|'='
name|'linux_net'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|type_to_class
name|'def'
name|'type_to_class'
op|'('
name|'network_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a network_type string into an actual Python class"""'
newline|'\n'
name|'if'
name|'not'
name|'network_type'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Network type couldn\'t be determined, using %s"'
op|'%'
nl|'\n'
name|'FLAGS'
op|'.'
name|'network_type'
op|')'
newline|'\n'
name|'network_type'
op|'='
name|'FLAGS'
op|'.'
name|'network_type'
newline|'\n'
dedent|''
name|'if'
name|'network_type'
op|'=='
string|"'flat'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FlatNetworkService'
newline|'\n'
dedent|''
name|'elif'
name|'network_type'
op|'=='
string|"'vlan'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'VlanNetworkService'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Couldn\'t find %s network type"'
op|'%'
name|'network_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup_compute_network
dedent|''
name|'def'
name|'setup_compute_network'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets up the network on a compute host"""'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'srv'
op|'='
name|'type_to_class'
op|'('
name|'network'
op|'.'
name|'kind'
op|')'
newline|'\n'
name|'srv'
op|'.'
name|'setup_compute_network'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_host_for_project
dedent|''
name|'def'
name|'get_host_for_project'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get host allocated to project from datastore"""'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
name|'project_id'
op|')'
op|'.'
name|'node_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseNetworkService
dedent|''
name|'class'
name|'BaseNetworkService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements common network service functionality\n\n    This class must be subclassed.\n    """'
newline|'\n'
nl|'\n'
DECL|member|set_network_host
name|'def'
name|'set_network_host'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Safely sets the host of the projects network"""'
newline|'\n'
name|'network_ref'
op|'='
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
name|'FLAGS'
op|'.'
name|'node_name'
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
name|'project_id'
op|','
name|'instance_id'
op|','
name|'context'
op|'='
name|'None'
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
string|'"""Gets fixed ip from the pool"""'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_allocate_address'
op|'('
name|'context'
op|','
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_instance_associate'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
op|','
nl|'\n'
name|'instance_id'
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
name|'address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a fixed ip to the pool"""'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_instance_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|setup_compute_network
name|'def'
name|'setup_compute_network'
op|'('
name|'cls'
op|','
name|'network'
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
name|'project_id'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets an floating ip from the pool"""'
newline|'\n'
comment|'# TODO(vish): add floating ips through manage command'
nl|'\n'
name|'return'
name|'db'
op|'.'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'node_name'
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
name|'floating_address'
op|','
name|'fixed_address'
op|','
nl|'\n'
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates an floating ip to a fixed ip"""'
newline|'\n'
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
name|'_driver'
op|'.'
name|'bind_floating_ip'
op|'('
name|'floating_address'
op|')'
newline|'\n'
name|'_driver'
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
name|'floating_address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociates a floating ip"""'
newline|'\n'
name|'fixed_address'
op|'='
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
name|'_driver'
op|'.'
name|'unbind_floating_ip'
op|'('
name|'floating_address'
op|')'
newline|'\n'
name|'_driver'
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
name|'floating_address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an floating ip to the pool"""'
newline|'\n'
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
nl|'\n'
DECL|class|FlatNetworkService
dedent|''
dedent|''
name|'class'
name|'FlatNetworkService'
op|'('
name|'BaseNetworkService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Basic network where no vlans are used"""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|setup_compute_network
name|'def'
name|'setup_compute_network'
op|'('
name|'cls'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Network is created manually"""'
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
comment|'#             in the database?'
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
string|"'kind'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'network_type'
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
comment|'# TODO(vish): add public ips from flags to the datastore'
nl|'\n'
nl|'\n'
DECL|class|VlanNetworkService
dedent|''
dedent|''
name|'class'
name|'VlanNetworkService'
op|'('
name|'BaseNetworkService'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Vlan network with dhcp"""'
newline|'\n'
DECL|member|__init__
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
name|'VlanNetworkService'
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
comment|'# NOTE(vish): this should probably be removed and added via'
nl|'\n'
comment|'#             admin command or fixtures'
nl|'\n'
name|'db'
op|'.'
name|'network_ensure_indexes'
op|'('
name|'None'
op|','
name|'FLAGS'
op|'.'
name|'num_networks'
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
name|'project_id'
op|','
name|'instance_id'
op|','
name|'context'
op|'='
name|'None'
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
string|'"""Gets a fixed ip from the pool"""'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'db'
op|'.'
name|'instance_is_vpn'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address'
op|'='
name|'db'
op|'.'
name|'network_get_vpn_ip_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Allocating vpn IP %s"'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_instance_associate'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'_driver'
op|'.'
name|'ensure_vlan_forward'
op|'('
name|'network_ref'
op|'['
string|"'vpn_public_ip_str'"
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
string|"'vpn_private_ip_str'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'parent'
op|'='
name|'super'
op|'('
name|'VlanNetworkService'
op|','
name|'self'
op|')'
newline|'\n'
name|'address'
op|'='
name|'parent'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'project_id'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'context'
op|')'
newline|'\n'
dedent|''
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
name|'address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an ip to the pool"""'
newline|'\n'
name|'fixed_ip_ref'
op|'='
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
name|'fixed_ip_ref'
op|'['
string|"'leased'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Deallocating IP %s"'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
comment|'# NOTE(vish): we keep instance id until release occurs'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'release_fixed_ip'
op|'('
name|'address'
op|','
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lease_fixed_ip
dedent|''
dedent|''
name|'def'
name|'lease_fixed_ip'
op|'('
name|'self'
op|','
name|'address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by bridge when ip is leased"""'
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
name|'db'
op|'.'
name|'fixed_ip_lease'
op|'('
name|'context'
op|','
name|'address'
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
name|'address'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by bridge when ip is released"""'
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
name|'db'
op|'.'
name|'fixed_ip_release'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_instance_disassociate'
op|'('
name|'context'
op|','
name|'address'
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
comment|'# FIXME'
nl|'\n'
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
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'network_id'
op|')'
newline|'\n'
name|'_driver'
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
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|setup_compute_network
name|'def'
name|'setup_compute_network'
op|'('
name|'cls'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
name|'_driver'
op|'.'
name|'ensure_vlan_bridge'
op|'('
name|'network'
op|'.'
name|'vlan'
op|','
name|'network'
op|'.'
name|'bridge'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
