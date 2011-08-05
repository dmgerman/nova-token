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
name|'log'
name|'as'
name|'logging'
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
name|'import'
name|'mox'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HOST
name|'HOST'
op|'='
string|'"testhost"'
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
DECL|variable|networks
dedent|''
dedent|''
dedent|''
name|'networks'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test0'"
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
string|"'192.168.0.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:db8::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:db8::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'fa0'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa0'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
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
string|"'192.168.0.2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test1'"
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
string|"'192.168.1.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:db9::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'2001:db9::1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'fa1'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa1'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.1.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'192.168.1.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
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
string|"'192.168.1.2'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fixed_ips
name|'fixed_ips'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.0.100'"
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
string|"'virtual_interface_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.1.100'"
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
string|"'virtual_interface_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|flavor
name|'flavor'
op|'='
op|'{'
string|"'id'"
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
DECL|variable|floating_ip_fields
name|'floating_ip_fields'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.10.100'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
number|'0'
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
DECL|variable|vifs
name|'vifs'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'FakeModel'
op|'('
op|'**'
name|'networks'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:01'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'FakeModel'
op|'('
op|'**'
name|'networks'
op|'['
number|'1'
op|']'
op|')'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlatNetworkTestCase
name|'class'
name|'FlatNetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FlatNetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'network'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_nw_info
dedent|''
name|'def'
name|'test_get_instance_nw_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'virtual_interface_get_by_instance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_type_get'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'fixed_ip_get_by_instance'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fixed_ips'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'virtual_interface_get_by_instance'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vifs'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'flavor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
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
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'nw'
name|'in'
name|'enumerate'
op|'('
name|'nw_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'i8'
op|'='
name|'i'
op|'+'
number|'8'
newline|'\n'
name|'check'
op|'='
op|'{'
string|"'bridge'"
op|':'
string|"'fa%s'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.%s.0/24'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'2001:db%s::/64'"
op|'%'
name|'i8'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'i'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'injected'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa%s'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'nw'
op|'['
number|'0'
op|']'
op|','
name|'check'
op|')'
newline|'\n'
nl|'\n'
name|'check'
op|'='
op|'{'
string|"'broadcast'"
op|':'
string|"'192.168.%s.255'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
string|"'192.168.%s.1'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'192.168.%s.1'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'gateway6'"
op|':'
string|"'2001:db%s::1'"
op|'%'
name|'i8'
op|','
nl|'\n'
string|"'ip6s'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'ips'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'test%s'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'mac'"
op|':'
string|"'DE:AD:BE:EF:00:0%s'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'should_create_vlan'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'should_create_bridge'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'nw'
op|'['
number|'1'
op|']'
op|','
name|'check'
op|')'
newline|'\n'
nl|'\n'
name|'check'
op|'='
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'2001:db%s::dcad:beff:feef:%s'"
op|'%'
op|'('
name|'i8'
op|','
name|'i'
op|')'
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'64'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDictListMatch'
op|'('
name|'nw'
op|'['
number|'1'
op|']'
op|'['
string|"'ip6s'"
op|']'
op|','
name|'check'
op|')'
newline|'\n'
nl|'\n'
name|'check'
op|'='
op|'['
op|'{'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'192.168.%s.100'"
op|'%'
name|'i'
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDictListMatch'
op|'('
name|'nw'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|','
name|'check'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VlanNetworkTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'VlanNetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VlanNetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'network_manager'
op|'.'
name|'VlanManager'
op|'('
name|'host'
op|'='
name|'HOST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
DECL|member|test_vpn_allocate_fixed_ip
dedent|''
name|'def'
name|'test_vpn_allocate_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'fixed_ip_associate'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'fixed_ip_update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
nl|'\n'
string|"'virtual_interface_get_by_instance_and_network'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'fixed_ip_associate'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'192.168.0.1'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'virtual_interface_get_by_instance_and_network'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
string|"'id'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'network'
op|'='
name|'dict'
op|'('
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'vpn_private_address'"
op|']'
op|'='
string|"'192.168.0.2'"
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'None'
op|','
number|'0'
op|','
name|'network'
op|','
name|'vpn'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_fixed_ip
dedent|''
name|'def'
name|'test_allocate_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'fixed_ip_associate_pool'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'fixed_ip_update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
nl|'\n'
string|"'virtual_interface_get_by_instance_and_network'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'fixed_ip_associate_pool'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'192.168.0.1'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'virtual_interface_get_by_instance_and_network'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
string|"'id'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'network'
op|'='
name|'dict'
op|'('
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'vpn_private_address'"
op|']'
op|'='
string|"'192.168.0.2'"
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'None'
op|','
number|'0'
op|','
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks_too_big
dedent|''
name|'def'
name|'test_create_networks_too_big'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'self'
op|'.'
name|'network'
op|'.'
name|'create_networks'
op|','
name|'None'
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'4094'
op|','
name|'vlan_start'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks_too_many
dedent|''
name|'def'
name|'test_create_networks_too_many'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'self'
op|'.'
name|'network'
op|'.'
name|'create_networks'
op|','
name|'None'
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'100'
op|','
name|'vlan_start'
op|'='
number|'1'
op|','
nl|'\n'
name|'cidr'
op|'='
string|"'192.168.0.1/24'"
op|','
name|'network_size'
op|'='
number|'100'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommonNetworkTestCase
dedent|''
dedent|''
name|'class'
name|'CommonNetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|FakeNetworkManager
indent|'    '
name|'class'
name|'FakeNetworkManager'
op|'('
name|'network_manager'
op|'.'
name|'NetworkManager'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This NetworkManager doesn\'t call the base class so we can bypass all\n        inherited service cruft and just perform unit tests.\n        """'
newline|'\n'
nl|'\n'
DECL|class|FakeDB
name|'class'
name|'FakeDB'
op|':'
newline|'\n'
DECL|member|fixed_ip_get_by_instance
indent|'            '
name|'def'
name|'fixed_ip_get_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.0'"
op|')'
op|','
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.0.0.2'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|network_get_by_cidr
dedent|''
name|'def'
name|'network_get_by_cidr'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForCidr'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_create_safe
dedent|''
name|'def'
name|'network_create_safe'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'net'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'fakenet'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakenet'
op|'['
string|"'id'"
op|']'
op|'='
number|'999'
newline|'\n'
name|'return'
name|'fakenet'
newline|'\n'
nl|'\n'
DECL|member|network_get_all
dedent|''
name|'def'
name|'network_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NoNetworksFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'='
name|'self'
op|'.'
name|'FakeDB'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deallocate_called'
op|'='
name|'None'
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
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deallocate_called'
op|'='
name|'address'
newline|'\n'
nl|'\n'
DECL|member|fake_create_fixed_ips
dedent|''
dedent|''
name|'def'
name|'fake_create_fixed_ips'
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
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'test_remove_fixed_ip_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'remove_fixed_ip_from_instance'
op|'('
name|'None'
op|','
number|'99'
op|','
string|"'10.0.0.1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'manager'
op|'.'
name|'deallocate_called'
op|','
string|"'10.0.0.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_from_instance_bad_input
dedent|''
name|'def'
name|'test_remove_fixed_ip_from_instance_bad_input'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'FixedIpNotFoundForSpecificInstance'
op|','
nl|'\n'
name|'manager'
op|'.'
name|'remove_fixed_ip_from_instance'
op|','
nl|'\n'
name|'None'
op|','
number|'99'
op|','
string|"'bad input'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs
dedent|''
name|'def'
name|'test__validate_cidrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'1'
op|','
number|'256'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'nets'
op|')'
op|')'
newline|'\n'
name|'cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'192.168.0.0/24'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_exact_in_half
dedent|''
name|'def'
name|'test__validate_cidrs_split_exact_in_half'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'2'
op|','
number|'128'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'nets'
op|')'
op|')'
newline|'\n'
name|'cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'192.168.0.0/25'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'192.168.0.128/25'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_cidr_in_use_middle_of_range
dedent|''
name|'def'
name|'test__validate_cidrs_split_cidr_in_use_middle_of_range'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.2.0/24'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.0.0/16'"
op|','
number|'4'
op|','
number|'256'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'nets'
op|')'
op|')'
newline|'\n'
name|'cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'exp_cidrs'
op|'='
op|'['
string|"'192.168.0.0'"
op|','
string|"'192.168.1.0'"
op|','
string|"'192.168.3.0'"
op|','
nl|'\n'
string|"'192.168.4.0'"
op|']'
newline|'\n'
name|'for'
name|'exp_cidr'
name|'in'
name|'exp_cidrs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'exp_cidr'
op|'+'
string|"'/24'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'192.168.2.0/24'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_smaller_subnet_in_use
dedent|''
name|'def'
name|'test__validate_cidrs_smaller_subnet_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.2.9/25'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
comment|'# ValueError: requested cidr (192.168.2.0/24) conflicts with'
nl|'\n'
comment|'#             existing smaller cidr'
nl|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.2.0/24'"
op|','
number|'1'
op|','
number|'256'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_smaller_cidr_in_use
dedent|''
name|'def'
name|'test__validate_cidrs_split_smaller_cidr_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.2.0/25'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.0.0/16'"
op|','
number|'4'
op|','
number|'256'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'nets'
op|')'
op|')'
newline|'\n'
name|'cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'exp_cidrs'
op|'='
op|'['
string|"'192.168.0.0'"
op|','
string|"'192.168.1.0'"
op|','
string|"'192.168.3.0'"
op|','
nl|'\n'
string|"'192.168.4.0'"
op|']'
newline|'\n'
name|'for'
name|'exp_cidr'
name|'in'
name|'exp_cidrs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'exp_cidr'
op|'+'
string|"'/24'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'192.168.2.0/24'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_smaller_cidr_in_use2
dedent|''
name|'def'
name|'test__validate_cidrs_split_smaller_cidr_in_use2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.2.9/29'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.2.0/24'"
op|','
number|'3'
op|','
number|'32'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'nets'
op|')'
op|')'
newline|'\n'
name|'cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'exp_cidrs'
op|'='
op|'['
string|"'192.168.2.32'"
op|','
string|"'192.168.2.64'"
op|','
string|"'192.168.2.96'"
op|']'
newline|'\n'
name|'for'
name|'exp_cidr'
name|'in'
name|'exp_cidrs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'exp_cidr'
op|'+'
string|"'/27'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'192.168.2.0/27'"
name|'in'
name|'cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_all_in_use
dedent|''
name|'def'
name|'test__validate_cidrs_split_all_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'in_use'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'cidr'"
op|':'
string|"'192.168.2.9/29'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'cidr'"
op|':'
string|"'192.168.2.64/26'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
string|"'cidr'"
op|':'
string|"'192.168.2.128/26'"
op|'}'
nl|'\n'
op|']'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'in_use'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.2.0/24'"
op|','
number|'3'
op|','
number|'64'
op|']'
newline|'\n'
comment|'# ValueError: Not enough subnets avail to satisfy requested num_'
nl|'\n'
comment|'#             networks - some subnets in requested range already'
nl|'\n'
comment|'#             in use'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_one_in_use
dedent|''
name|'def'
name|'test__validate_cidrs_one_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'2'
op|','
number|'256'
op|']'
newline|'\n'
comment|'# ValueError: network_size * num_networks exceeds cidr size'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_already_used
dedent|''
name|'def'
name|'test__validate_cidrs_already_used'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|'}'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
comment|'# ValueError: cidr already in use'
nl|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'1'
op|','
number|'256'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_too_many
dedent|''
name|'def'
name|'test__validate_cidrs_too_many'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'200'
op|','
number|'256'
op|']'
newline|'\n'
comment|'# ValueError: Not enough subnets avail to satisfy requested'
nl|'\n'
comment|'#             num_networks'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_split_partial
dedent|''
name|'def'
name|'test__validate_cidrs_split_partial'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'manager'
op|'.'
name|'_validate_cidrs'
op|'('
name|'None'
op|','
string|"'192.168.0.0/16'"
op|','
number|'2'
op|','
number|'256'
op|')'
newline|'\n'
name|'returned_cidrs'
op|'='
op|'['
name|'str'
op|'('
name|'net'
op|')'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'192.168.0.0/24'"
name|'in'
name|'returned_cidrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'192.168.1.0/24'"
name|'in'
name|'returned_cidrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__validate_cidrs_conflict_existing_supernet
dedent|''
name|'def'
name|'test__validate_cidrs_conflict_existing_supernet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'fakecidr'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'cidr'"
op|':'
string|"'192.168.0.0/8'"
op|'}'
op|']'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fakecidr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'192.168.0.0/24'"
op|','
number|'1'
op|','
number|'256'
op|']'
newline|'\n'
comment|'# ValueError: requested cidr (192.168.0.0/24) conflicts'
nl|'\n'
comment|'#             with existing supernet'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'_validate_cidrs'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks
dedent|''
name|'def'
name|'test_create_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cidr'
op|'='
string|"'192.168.0.0/24'"
newline|'\n'
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'manager'
op|','
string|"'_create_fixed_ips'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_create_fixed_ips'
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'foo'"
op|','
name|'cidr'
op|','
name|'None'
op|','
number|'1'
op|','
number|'256'
op|','
string|"'fd00::/48'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|']'
newline|'\n'
name|'result'
op|'='
name|'manager'
op|'.'
name|'create_networks'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'manager'
op|'.'
name|'create_networks'
op|'('
op|'*'
name|'args'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks_cidr_already_used
dedent|''
name|'def'
name|'test_create_networks_cidr_already_used'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'manager'
op|'.'
name|'db'
op|','
string|"'network_get_all'"
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
newline|'\n'
name|'fakecidr'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|'}'
op|']'
newline|'\n'
name|'manager'
op|'.'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fakecidr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'foo'"
op|','
string|"'192.168.0.0/24'"
op|','
name|'None'
op|','
number|'1'
op|','
number|'256'
op|','
nl|'\n'
string|"'fd00::/48'"
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'manager'
op|'.'
name|'create_networks'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_networks_many
dedent|''
name|'def'
name|'test_create_networks_many'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cidr'
op|'='
string|"'192.168.0.0/16'"
newline|'\n'
name|'manager'
op|'='
name|'self'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'manager'
op|','
string|"'_create_fixed_ips'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_create_fixed_ips'
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
name|'None'
op|','
string|"'foo'"
op|','
name|'cidr'
op|','
name|'None'
op|','
number|'10'
op|','
number|'256'
op|','
string|"'fd00::/48'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'manager'
op|'.'
name|'create_networks'
op|'('
op|'*'
name|'args'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
