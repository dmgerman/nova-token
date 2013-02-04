begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Nicira Networks, Inc'
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
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|L3Driver
name|'class'
name|'L3Driver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstract class that defines a generic L3 API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'l3_lib'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize
dedent|''
name|'def'
name|'initialize'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set up basic L3 networking functionality."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize_network
dedent|''
name|'def'
name|'initialize_network'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Enable rules for a specific network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize_gateway
dedent|''
name|'def'
name|'initialize_gateway'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set up a gateway on this network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_gateway
dedent|''
name|'def'
name|'remove_gateway'
op|'('
name|'self'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove an existing gateway on this network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_initialized
dedent|''
name|'def'
name|'is_initialized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""":returns: True/False (whether the driver is initialized)."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_floating_ip
dedent|''
name|'def'
name|'add_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a floating IP bound to the fixed IP with an optional\n           l3_interface_id.  Some drivers won\'t care about the\n           l3_interface_id so just pass None in that case. Network\n           is also an optional parameter."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_floating_ip
dedent|''
name|'def'
name|'remove_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_vpn
dedent|''
name|'def'
name|'add_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_vpn
dedent|''
name|'def'
name|'remove_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LinuxNetL3
dedent|''
dedent|''
name|'class'
name|'LinuxNetL3'
op|'('
name|'L3Driver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""L3 driver that uses linux_net as the backend."""'
newline|'\n'
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
name|'initialized'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|initialize
dedent|''
name|'def'
name|'initialize'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'initialized'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Initializing linux_net L3 driver"'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'ensure_metadata_ip'
op|'('
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'metadata_forward'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'initialized'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|is_initialized
dedent|''
name|'def'
name|'is_initialized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'initialized'
newline|'\n'
nl|'\n'
DECL|member|initialize_network
dedent|''
name|'def'
name|'initialize_network'
op|'('
name|'self'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'linux_net'
op|'.'
name|'add_snat_rule'
op|'('
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize_gateway
dedent|''
name|'def'
name|'initialize_gateway'
op|'('
name|'self'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac_address'
op|'='
name|'utils'
op|'.'
name|'generate_mac_address'
op|'('
op|')'
newline|'\n'
name|'dev'
op|'='
name|'linux_net'
op|'.'
name|'plug'
op|'('
name|'network_ref'
op|','
name|'mac_address'
op|','
nl|'\n'
name|'gateway'
op|'='
op|'('
name|'network_ref'
op|'['
string|"'gateway'"
op|']'
name|'is'
name|'not'
name|'None'
op|')'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'initialize_gateway_device'
op|'('
name|'dev'
op|','
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_gateway
dedent|''
name|'def'
name|'remove_gateway'
op|'('
name|'self'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'linux_net'
op|'.'
name|'unplug'
op|'('
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_floating_ip
dedent|''
name|'def'
name|'add_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'linux_net'
op|'.'
name|'ensure_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
nl|'\n'
name|'l3_interface_id'
op|','
name|'network'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'bind_floating_ip'
op|'('
name|'floating_ip'
op|','
name|'l3_interface_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_floating_ip
dedent|''
name|'def'
name|'remove_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'linux_net'
op|'.'
name|'unbind_floating_ip'
op|'('
name|'floating_ip'
op|','
name|'l3_interface_id'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'remove_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
nl|'\n'
name|'l3_interface_id'
op|','
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_vpn
dedent|''
name|'def'
name|'add_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'linux_net'
op|'.'
name|'ensure_vpn_forward'
op|'('
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_vpn
dedent|''
name|'def'
name|'remove_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
comment|"# Linux net currently doesn't implement any way of removing"
nl|'\n'
comment|'# the VPN forwarding rules'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullL3
dedent|''
dedent|''
name|'class'
name|'NullL3'
op|'('
name|'L3Driver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The L3 driver that doesn\'t do anything.  This class can be used when\n       nova-network shuld not manipulate L3 forwarding at all (e.g., in a Flat\n       or FlatDHCP scenario"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|initialize
dedent|''
name|'def'
name|'initialize'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|is_initialized
dedent|''
name|'def'
name|'is_initialized'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|initialize_network
dedent|''
name|'def'
name|'initialize_network'
op|'('
name|'self'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|initialize_gateway
dedent|''
name|'def'
name|'initialize_gateway'
op|'('
name|'self'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|remove_gateway
dedent|''
name|'def'
name|'remove_gateway'
op|'('
name|'self'
op|','
name|'network_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|add_floating_ip
dedent|''
name|'def'
name|'add_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|remove_floating_ip
dedent|''
name|'def'
name|'remove_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
name|'l3_interface_id'
op|','
nl|'\n'
name|'network'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|add_vpn
dedent|''
name|'def'
name|'add_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|remove_vpn
dedent|''
name|'def'
name|'remove_vpn'
op|'('
name|'self'
op|','
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
