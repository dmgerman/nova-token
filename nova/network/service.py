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
name|'from'
name|'nova'
name|'import'
name|'datastore'
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
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'exception'
name|'as'
name|'network_exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'vpn'
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
name|'network_type'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets up the network on a compute host"""'
newline|'\n'
name|'srv'
op|'='
name|'type_to_class'
op|'('
name|'network_type'
op|')'
newline|'\n'
name|'srv'
op|'.'
name|'setup_compute_network'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'security_group'
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
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'return'
name|'redis'
op|'.'
name|'get'
op|'('
name|'_host_key'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_host_key
dedent|''
name|'def'
name|'_host_key'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns redis host key for network"""'
newline|'\n'
name|'return'
string|'"networkhost:%s"'
op|'%'
name|'project_id'
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
name|'self'
op|'.'
name|'network'
op|'='
name|'model'
op|'.'
name|'PublicNetworkController'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'BaseNetworkService'
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
name|'user_id'
op|','
name|'project_id'
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
string|'"""Safely sets the host of the projects network"""'
newline|'\n'
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'_host_key'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'redis'
op|'.'
name|'setnx'
op|'('
name|'key'
op|','
name|'FLAGS'
op|'.'
name|'node_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_on_set_network_host'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'redis'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
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
string|'"""Subclass implements getting fixed ip from the pool"""'
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
name|'fixed_ip'
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
string|'"""Subclass implements return of ip to the pool"""'
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
name|'user_id'
op|','
name|'project_id'
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
name|'user_id'
op|','
name|'project_id'
op|','
name|'security_group'
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
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_elastic_ip
dedent|''
name|'def'
name|'allocate_elastic_ip'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets a elastic ip from the pool"""'
newline|'\n'
comment|"# NOTE(vish): Replicating earlier decision to use 'public' as"
nl|'\n'
comment|'#             mac address name, although this should probably'
nl|'\n'
comment|'#             be done inside of the PublicNetworkController'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_ip'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
string|"'public'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_elastic_ip
dedent|''
name|'def'
name|'associate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|','
name|'fixed_ip'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates an elastic ip to a fixed ip"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'associate_address'
op|'('
name|'elastic_ip'
op|','
name|'fixed_ip'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_elastic_ip
dedent|''
name|'def'
name|'disassociate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociates a elastic ip"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'disassociate_address'
op|'('
name|'elastic_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_elastic_ip
dedent|''
name|'def'
name|'deallocate_elastic_ip'
op|'('
name|'self'
op|','
name|'elastic_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a elastic ip to the pool"""'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'elastic_ip'
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
name|'user_id'
op|','
name|'project_id'
op|','
name|'security_group'
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
string|'"""Network is created manually"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|allocate_fixed_ip
dedent|''
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
nl|'\n'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
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
string|'"""Gets a fixed ip from the pool\n\n        Flat network just grabs the next available ip from the pool\n        """'
newline|'\n'
comment|'# NOTE(vish): Some automation could be done here.  For example,'
nl|'\n'
comment|'#             creating the flat_network_bridge and setting up'
nl|'\n'
comment|'#             a gateway.  This is all done manually atm.'
nl|'\n'
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'redis'
op|'.'
name|'exists'
op|'('
string|"'ips'"
op|')'
name|'and'
name|'not'
name|'len'
op|'('
name|'redis'
op|'.'
name|'keys'
op|'('
string|"'instances:*'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'fixed_ip'
name|'in'
name|'FLAGS'
op|'.'
name|'flat_network_ips'
op|':'
newline|'\n'
indent|'                '
name|'redis'
op|'.'
name|'sadd'
op|'('
string|"'ips'"
op|','
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'fixed_ip'
op|'='
name|'redis'
op|'.'
name|'spop'
op|'('
string|"'ips'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'network_exception'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
comment|'# TODO(vish): some sort of dns handling for hostname should'
nl|'\n'
comment|'#             probably be done here.'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'inject_network'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'network_type'"
op|':'
name|'FLAGS'
op|'.'
name|'network_type'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|','
nl|'\n'
string|"'private_dns_name'"
op|':'
name|'str'
op|'('
name|'fixed_ip'
op|')'
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_bridge'
op|','
nl|'\n'
string|"'network_network'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_network'
op|','
nl|'\n'
string|"'network_netmask'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_netmask'
op|','
nl|'\n'
string|"'network_gateway'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_gateway'
op|','
nl|'\n'
string|"'network_broadcast'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_broadcast'
op|','
nl|'\n'
string|"'network_dns'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_dns'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
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
string|'"""Returns an ip to the pool"""'
newline|'\n'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
string|"'ips'"
op|','
name|'fixed_ip'
op|')'
newline|'\n'
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
comment|'# NOTE(vish): A lot of the interactions with network/model.py can be'
nl|'\n'
comment|'#             simplified and improved.  Also there it may be useful'
nl|'\n'
comment|'#             to support vlans separately from dhcp, instead of having'
nl|'\n'
comment|'#             both of them together in this class.'
nl|'\n'
comment|'# pylint: disable-msg=W0221'
nl|'\n'
DECL|member|allocate_fixed_ip
name|'def'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|','
nl|'\n'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
name|'is_vpn'
op|'='
name|'False'
op|','
nl|'\n'
name|'hostname'
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
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'net'
op|'='
name|'model'
op|'.'
name|'get_project_network'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'is_vpn'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'net'
op|'.'
name|'allocate_vpn_ip'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'mac'
op|','
nl|'\n'
name|'hostname'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'net'
op|'.'
name|'allocate_ip'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'mac'
op|','
nl|'\n'
name|'hostname'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'network_type'"
op|':'
name|'FLAGS'
op|'.'
name|'network_type'
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
name|'net'
op|'['
string|"'bridge_name'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mac'
op|','
nl|'\n'
string|"'private_dns_name'"
op|':'
name|'fixed_ip'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|deallocate_fixed_ip
dedent|''
name|'def'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
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
string|'"""Returns an ip to the pool"""'
newline|'\n'
name|'return'
name|'model'
op|'.'
name|'get_network_by_address'
op|'('
name|'fixed_ip'
op|')'
op|'.'
name|'deallocate_ip'
op|'('
name|'fixed_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lease_ip
dedent|''
name|'def'
name|'lease_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by bridge when ip is leased"""'
newline|'\n'
name|'return'
name|'model'
op|'.'
name|'get_network_by_address'
op|'('
name|'fixed_ip'
op|')'
op|'.'
name|'lease_ip'
op|'('
name|'fixed_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_ip
dedent|''
name|'def'
name|'release_ip'
op|'('
name|'self'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by bridge when ip is released"""'
newline|'\n'
name|'return'
name|'model'
op|'.'
name|'get_network_by_address'
op|'('
name|'fixed_ip'
op|')'
op|'.'
name|'release_ip'
op|'('
name|'fixed_ip'
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
name|'for'
name|'project'
name|'in'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_projects'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'model'
op|'.'
name|'get_project_network'
op|'('
name|'project'
op|'.'
name|'id'
op|')'
op|'.'
name|'express'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_set_network_host
dedent|''
dedent|''
name|'def'
name|'_on_set_network_host'
op|'('
name|'self'
op|','
name|'user_id'
op|','
name|'project_id'
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
string|'"""Called when this host becomes the host for a project"""'
newline|'\n'
name|'vpn'
op|'.'
name|'NetworkData'
op|'.'
name|'create'
op|'('
name|'project_id'
op|')'
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
name|'user_id'
op|','
name|'project_id'
op|','
name|'security_group'
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
string|'"""Sets up matching network for compute hosts"""'
newline|'\n'
comment|'# NOTE(vish): Use BridgedNetwork instead of DHCPNetwork because'
nl|'\n'
comment|"#             we don't want to run dnsmasq on the client machines"
nl|'\n'
name|'net'
op|'='
name|'model'
op|'.'
name|'BridgedNetwork'
op|'.'
name|'get_network_for_project'
op|'('
nl|'\n'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'security_group'
op|')'
newline|'\n'
name|'net'
op|'.'
name|'express'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
