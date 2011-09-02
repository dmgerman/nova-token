begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Rackspace'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
name|'import'
name|'itertools'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HOST
name|'HOST'
op|'='
string|'"testhost"'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represent a model from the db"""'
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
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|__getattr__
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_network'
op|'('
name|'network_id'
op|','
name|'ipv6'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'ipv6'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ipv6'
op|'='
name|'FLAGS'
op|'.'
name|'use_ipv6'
newline|'\n'
dedent|''
name|'fake_network'
op|'='
op|'{'
string|"'id'"
op|':'
name|'network_id'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.%d.0/24'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'fake_br%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_eth%d'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.%d.1'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.%d.255'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.%d.3'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.%d.4'"
op|'%'
name|'network_id'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
string|"'192.168.%d.2'"
op|'%'
name|'network_id'
op|'}'
newline|'\n'
name|'if'
name|'ipv6'
op|':'
newline|'\n'
indent|'        '
name|'fake_network'
op|'['
string|"'cidr_v6'"
op|']'
op|'='
string|"'2001:db8:0:%x::/64'"
op|'%'
name|'network_id'
newline|'\n'
name|'fake_network'
op|'['
string|"'gateway_v6'"
op|']'
op|'='
string|"'2001:db8:0:%x::1'"
op|'%'
name|'network_id'
newline|'\n'
name|'fake_network'
op|'['
string|"'netmask_v6'"
op|']'
op|'='
string|"'64'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fake_network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ips
dedent|''
name|'def'
name|'fixed_ips'
op|'('
name|'num_networks'
op|','
name|'num_ips'
op|','
name|'num_floating_ips'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'network_index'
name|'in'
name|'xrange'
op|'('
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'ip_index'
name|'in'
name|'xrange'
op|'('
name|'num_ips'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_id'
op|'='
name|'network_index'
op|'*'
name|'num_ips'
op|'+'
name|'ip_index'
newline|'\n'
name|'f_ips'
op|'='
op|'['
name|'FakeModel'
op|'('
op|'**'
name|'floating_ips'
op|'('
name|'fixed_ip_id'
op|')'
op|'.'
name|'next'
op|'('
op|')'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'num_floating_ips'
op|')'
op|']'
newline|'\n'
name|'yield'
op|'{'
string|"'id'"
op|':'
name|'fixed_ip_id'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_index'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.%d.1%02d'"
op|'%'
op|'('
name|'network_index'
op|','
name|'ip_index'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'False'
op|','
nl|'\n'
comment|'# and since network_id and vif_id happen to be equivalent'
nl|'\n'
string|"'virtual_interface_id'"
op|':'
name|'network_index'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
name|'f_ips'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|flavor
dedent|''
dedent|''
dedent|''
name|'flavor'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake_flavor'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'flavor_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_quota'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
number|'3'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ips
name|'def'
name|'floating_ips'
op|'('
name|'fixed_ip_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'154'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.%d'"
op|'%'
op|'('
name|'i'
op|'+'
number|'100'
op|')'
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'fixed_ip_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'auto_assigned'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vifs
dedent|''
dedent|''
name|'def'
name|'vifs'
op|'('
name|'n'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'n'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'{'
string|"'id'"
op|':'
name|'x'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:%02x'"
op|'%'
name|'x'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000%02d'"
op|'%'
name|'x'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'x'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'FakeModel'
op|'('
op|'**'
name|'fake_network'
op|'('
name|'x'
op|')'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ipv4_like
dedent|''
dedent|''
name|'def'
name|'ipv4_like'
op|'('
name|'ip'
op|','
name|'match_string'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ip'
op|'='
name|'ip'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'match_octets'
op|'='
name|'match_string'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'octet'
name|'in'
name|'enumerate'
op|'('
name|'match_octets'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'octet'
op|'=='
string|"'*'"
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'octet'
op|'!='
name|'ip'
op|'['
name|'i'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance_nw_info
dedent|''
name|'def'
name|'fake_get_instance_nw_info'
op|'('
name|'stubs'
op|','
name|'num_networks'
op|'='
number|'1'
op|','
name|'ips_per_vif'
op|'='
number|'2'
op|')'
op|':'
newline|'\n'
comment|'# stubs is the self.stubs from the test'
nl|'\n'
comment|'# ips_per_vif is the number of ips each vif will have'
nl|'\n'
comment|'# num_floating_ips is number of float ips for each fixed ip'
nl|'\n'
indent|'    '
name|'network'
op|'='
name|'network_manager'
op|'.'
name|'FlatManager'
op|'('
name|'host'
op|'='
name|'HOST'
op|')'
newline|'\n'
name|'network'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
DECL|function|fixed_ips_fake
name|'def'
name|'fixed_ips_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'list'
op|'('
name|'fixed_ips'
op|'('
name|'num_networks'
op|','
name|'ips_per_vif'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|virtual_interfaces_fake
dedent|''
name|'def'
name|'virtual_interfaces_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'vif'
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|'('
name|'num_networks'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_type_fake
dedent|''
name|'def'
name|'instance_type_fake'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'flavor'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
name|'fixed_ips_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'virtual_interface_get_by_instance'"
op|','
name|'virtual_interfaces_fake'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get'"
op|','
name|'instance_type_fake'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'network'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'None'
op|','
number|'0'
op|','
number|'0'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
