begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright 2011 NTT'
nl|'\r\n'
comment|'# All Rights Reserved.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'# a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'# under the License.'
nl|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\r\n'
nl|'\r\n'
name|'import'
name|'mox'
newline|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
nl|'\r\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|HOST
name|'HOST'
op|'='
string|'"testhost"'
newline|'\r\n'
nl|'\r\n'
DECL|variable|instances
name|'instances'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'host'"
op|':'
string|"'fake_instance00'"
op|','
nl|'\r\n'
string|"'hostname'"
op|':'
string|"'fake_instance00'"
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'host'"
op|':'
string|"'fake_instance01'"
op|','
nl|'\r\n'
string|"'hostname'"
op|':'
string|"'fake_instance01'"
op|'}'
op|']'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|addresses
name|'addresses'
op|'='
op|'['
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.1"'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.2"'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.3"'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.4"'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.5"'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|'"address"'
op|':'
string|'"10.0.0.6"'
op|'}'
op|']'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|networks
name|'networks'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|'"aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"'
op|','
nl|'\r\n'
string|"'label'"
op|':'
string|"'test0'"
op|','
nl|'\r\n'
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\r\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\r\n'
string|"'cidr'"
op|':'
string|"'192.168.0.0/24'"
op|','
nl|'\r\n'
string|"'cidr_v6'"
op|':'
string|"'2001:db8::/64'"
op|','
nl|'\r\n'
string|"'gateway_v6'"
op|':'
string|"'2001:db8::1'"
op|','
nl|'\r\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\r\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\r\n'
string|"'bridge'"
op|':'
string|"'fa0'"
op|','
nl|'\r\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa0'"
op|','
nl|'\r\n'
string|"'gateway'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\r\n'
string|"'broadcast'"
op|':'
string|"'192.168.0.255'"
op|','
nl|'\r\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\r\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
op|','
nl|'\r\n'
string|"'dhcp_server'"
op|':'
string|"'0.0.0.0'"
op|','
nl|'\r\n'
string|"'dhcp_start'"
op|':'
string|"'192.168.100.1'"
op|','
nl|'\r\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\r\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\r\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\r\n'
string|"'vpn_public_address'"
op|':'
string|"'192.168.0.2'"
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|'"bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb"'
op|','
nl|'\r\n'
string|"'label'"
op|':'
string|"'test1'"
op|','
nl|'\r\n'
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\r\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\r\n'
string|"'cidr'"
op|':'
string|"'192.168.1.0/24'"
op|','
nl|'\r\n'
string|"'cidr_v6'"
op|':'
string|"'2001:db9::/64'"
op|','
nl|'\r\n'
string|"'gateway_v6'"
op|':'
string|"'2001:db9::1'"
op|','
nl|'\r\n'
string|"'netmask_v6'"
op|':'
string|"'64'"
op|','
nl|'\r\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\r\n'
string|"'bridge'"
op|':'
string|"'fa1'"
op|','
nl|'\r\n'
string|"'bridge_interface'"
op|':'
string|"'fake_fa1'"
op|','
nl|'\r\n'
string|"'gateway'"
op|':'
string|"'192.168.1.1'"
op|','
nl|'\r\n'
string|"'broadcast'"
op|':'
string|"'192.168.1.255'"
op|','
nl|'\r\n'
string|"'dns1'"
op|':'
string|"'192.168.0.1'"
op|','
nl|'\r\n'
string|"'dns2'"
op|':'
string|"'192.168.0.2'"
op|','
nl|'\r\n'
string|"'dhcp_server'"
op|':'
string|"'0.0.0.0'"
op|','
nl|'\r\n'
string|"'dhcp_start'"
op|':'
string|"'192.168.100.1'"
op|','
nl|'\r\n'
string|"'vlan'"
op|':'
name|'None'
op|','
nl|'\r\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\r\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\r\n'
string|"'vpn_public_address'"
op|':'
string|"'192.168.1.2'"
op|'}'
op|']'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|fixed_ips
name|'fixed_ips'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.0.100'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.1.100'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.0.101'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'2'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'2'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.1.101'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'3'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'3'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'4'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.0.102'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'4'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'4'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'5'
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'192.168.1.102'"
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\r\n'
string|"'virtual_interface_id'"
op|':'
number|'5'
op|','
nl|'\r\n'
string|"'virtual_interface'"
op|':'
name|'addresses'
op|'['
number|'5'
op|']'
op|','
nl|'\r\n'
string|"'instance'"
op|':'
name|'instances'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'floating_ips'"
op|':'
op|'['
op|']'
op|'}'
op|']'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|variable|vifs
name|'vifs'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:00'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000000'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:01'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000001'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:02'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000002'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:03'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000003'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'4'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:04'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000004'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'0'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'0'
op|'}'
op|','
nl|'\r\n'
op|'{'
string|"'id'"
op|':'
number|'5'
op|','
nl|'\r\n'
string|"'address'"
op|':'
string|"'DE:AD:BE:EF:00:05'"
op|','
nl|'\r\n'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-0000000000000005'"
op|','
nl|'\r\n'
string|"'network_id'"
op|':'
number|'1'
op|','
nl|'\r\n'
string|"'network'"
op|':'
name|'networks'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
string|"'instance_id'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|LinuxNetworkTestCase
name|'class'
name|'LinuxNetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\r\n'
nl|'\r\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'super'
op|'('
name|'LinuxNetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\r\n'
name|'network_driver'
op|'='
name|'FLAGS'
op|'.'
name|'network_driver'
newline|'\r\n'
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
newline|'\r\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_update_dhcp_for_nw00
dedent|''
name|'def'
name|'test_update_dhcp_for_nw00'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_single_default_gateway'
op|'='
name|'True'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'3'
op|']'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'3'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'0'
op|']'
op|','
name|'vifs'
op|'['
number|'1'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'2'
op|']'
op|','
name|'vifs'
op|'['
number|'3'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'update_dhcp'
op|'('
name|'None'
op|','
string|'"eth0"'
op|','
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_update_dhcp_for_nw01
dedent|''
name|'def'
name|'test_update_dhcp_for_nw01'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_single_default_gateway'
op|'='
name|'True'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'2'
op|']'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'2'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'0'
op|']'
op|','
name|'vifs'
op|'['
number|'1'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'2'
op|']'
op|','
name|'vifs'
op|'['
number|'3'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'update_dhcp'
op|'('
name|'None'
op|','
string|'"eth0"'
op|','
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_dhcp_hosts_for_nw00
dedent|''
name|'def'
name|'test_get_dhcp_hosts_for_nw00'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_single_default_gateway'
op|'='
name|'True'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'3'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'expected'
op|'='
string|'"10.0.0.1,fake_instance00.novalocal,"'
string|'"192.168.0.100,net:NW-i00000000-0\\n"'
string|'"10.0.0.4,fake_instance01.novalocal,"'
string|'"192.168.1.101,net:NW-i00000001-0"'
newline|'\r\n'
name|'actual_hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_dhcp_hosts'
op|'('
name|'None'
op|','
name|'networks'
op|'['
number|'1'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual_hosts'
op|','
name|'expected'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_dhcp_hosts_for_nw01
dedent|''
name|'def'
name|'test_get_dhcp_hosts_for_nw01'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_single_default_gateway'
op|'='
name|'True'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'2'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'expected'
op|'='
string|'"10.0.0.2,fake_instance00.novalocal,"'
string|'"192.168.1.100,net:NW-i00000000-1\\n"'
string|'"10.0.0.3,fake_instance01.novalocal,"'
string|'"192.168.0.101,net:NW-i00000001-1"'
newline|'\r\n'
name|'actual_hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_dhcp_hosts'
op|'('
name|'None'
op|','
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual_hosts'
op|','
name|'expected'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_dhcp_opts_for_nw00
dedent|''
name|'def'
name|'test_get_dhcp_opts_for_nw00'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'3'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'4'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'4'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'2'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'3'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'5'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'expected_opts'
op|'='
string|"'NW-i00000001-0,3'"
newline|'\r\n'
name|'actual_opts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_dhcp_opts'
op|'('
name|'None'
op|','
name|'networks'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual_opts'
op|','
name|'expected_opts'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_get_dhcp_opts_for_nw01
dedent|''
name|'def'
name|'test_get_dhcp_opts_for_nw01'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'network_get_associated_fixed_ips'"
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fixed_ips'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'2'
op|']'
op|','
nl|'\r\n'
name|'fixed_ips'
op|'['
number|'5'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'0'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'1'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'4'
op|']'
op|']'
op|')'
newline|'\r\n'
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
nl|'\r\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'vifs'
op|'['
number|'2'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'3'
op|']'
op|','
nl|'\r\n'
name|'vifs'
op|'['
number|'5'
op|']'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'expected_opts'
op|'='
string|'"NW-i00000000-1,3"'
newline|'\r\n'
name|'actual_opts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_dhcp_opts'
op|'('
name|'None'
op|','
name|'networks'
op|'['
number|'1'
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual_opts'
op|','
name|'expected_opts'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_dhcp_opts_not_default_gateway_network
dedent|''
name|'def'
name|'test_dhcp_opts_not_default_gateway_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'expected'
op|'='
string|'"NW-i00000000-0,3"'
newline|'\r\n'
name|'actual'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_host_dhcp_opts'
op|'('
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|test_host_dhcp_without_default_gateway_network
dedent|''
name|'def'
name|'test_host_dhcp_without_default_gateway_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'expected'
op|'='
op|'('
string|'"10.0.0.1,fake_instance00.novalocal,192.168.0.100"'
op|')'
newline|'\r\n'
name|'actual'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_host_dhcp'
op|'('
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
