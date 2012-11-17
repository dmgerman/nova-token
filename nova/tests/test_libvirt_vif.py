begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2012 Nicira, Inc'
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
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
name|'as'
name|'vconfig'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'vif'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVifTestCase
name|'class'
name|'LibvirtVifTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|net
indent|'    '
name|'net'
op|'='
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'101.168.1.0/24'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
string|"'101:1db9::/64'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
string|"'101:1db9::1'"
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
string|"'br0'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'eth0'"
op|','
nl|'\n'
string|"'vlan'"
op|':'
number|'99'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'101.168.1.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'101.168.1.255'"
op|','
nl|'\n'
string|"'dns1'"
op|':'
string|"'8.8.8.8'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'network-id-xxx-yyy-zzz'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|mapping
name|'mapping'
op|'='
op|'{'
nl|'\n'
string|"'mac'"
op|':'
string|"'ca:fe:de:ad:be:ef'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'net'
op|'['
string|"'gateway_v6'"
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
op|'{'
string|"'ip'"
op|':'
string|"'101.168.1.9'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
string|"'191.168.1.1'"
op|','
nl|'\n'
string|"'vif_uuid'"
op|':'
string|"'vif-xxx-yyy-zzz'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|instance
name|'instance'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'instance-name'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'instance-uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'LibvirtVifTestCase'
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
name|'flags'
op|'('
name|'allow_same_net_traffic'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_xml
dedent|''
name|'def'
name|'_get_instance_xml'
op|'('
name|'self'
op|','
name|'driver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuest'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'virt_type'
op|'='
string|'"qemu"'
newline|'\n'
name|'conf'
op|'.'
name|'name'
op|'='
string|'"fake-name"'
newline|'\n'
name|'conf'
op|'.'
name|'uuid'
op|'='
string|'"fake-uuid"'
newline|'\n'
name|'conf'
op|'.'
name|'memory'
op|'='
number|'100'
op|'*'
number|'1024'
newline|'\n'
name|'conf'
op|'.'
name|'vcpus'
op|'='
number|'4'
newline|'\n'
nl|'\n'
name|'nic'
op|'='
name|'driver'
op|'.'
name|'plug'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_device'
op|'('
name|'nic'
op|')'
newline|'\n'
name|'return'
name|'conf'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_nics
dedent|''
name|'def'
name|'test_multiple_nics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuest'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'virt_type'
op|'='
string|'"qemu"'
newline|'\n'
name|'conf'
op|'.'
name|'name'
op|'='
string|'"fake-name"'
newline|'\n'
name|'conf'
op|'.'
name|'uuid'
op|'='
string|'"fake-uuid"'
newline|'\n'
name|'conf'
op|'.'
name|'memory'
op|'='
number|'100'
op|'*'
number|'1024'
newline|'\n'
name|'conf'
op|'.'
name|'vcpus'
op|'='
number|'4'
newline|'\n'
nl|'\n'
comment|'# Tests multiple nic configuration and that target_dev is'
nl|'\n'
comment|'# set for each'
nl|'\n'
name|'nics'
op|'='
op|'['
op|'{'
string|"'net_type'"
op|':'
string|"'bridge'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'00:00:00:00:00:0b'"
op|','
nl|'\n'
string|"'source_dev'"
op|':'
string|"'b_source_dev'"
op|','
nl|'\n'
string|"'target_dev'"
op|':'
string|"'b_target_dev'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'net_type'"
op|':'
string|"'ethernet'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'00:00:00:00:00:0e'"
op|','
nl|'\n'
string|"'source_dev'"
op|':'
string|"'e_source_dev'"
op|','
nl|'\n'
string|"'target_dev'"
op|':'
string|"'e_target_dev'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'net_type'"
op|':'
string|"'direct'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'00:00:00:00:00:0d'"
op|','
nl|'\n'
string|"'source_dev'"
op|':'
string|"'d_source_dev'"
op|','
nl|'\n'
string|"'target_dev'"
op|':'
string|"'d_target_dev'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'nic'
name|'in'
name|'nics'
op|':'
newline|'\n'
indent|'            '
name|'nic_conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'nic_conf'
op|'.'
name|'net_type'
op|'='
name|'nic'
op|'['
string|"'net_type'"
op|']'
newline|'\n'
name|'nic_conf'
op|'.'
name|'target_dev'
op|'='
name|'nic'
op|'['
string|"'target_dev'"
op|']'
newline|'\n'
name|'nic_conf'
op|'.'
name|'mac_addr'
op|'='
name|'nic'
op|'['
string|"'mac_addr'"
op|']'
newline|'\n'
name|'nic_conf'
op|'.'
name|'source_dev'
op|'='
name|'nic'
op|'['
string|"'source_dev'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'add_device'
op|'('
name|'nic_conf'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'xml'
op|'='
name|'conf'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'for'
name|'nic'
name|'in'
name|'nics'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
string|'"./devices/interface/[@type=\'%s\']"'
op|'%'
name|'nic'
op|'['
string|"'net_type'"
op|']'
newline|'\n'
name|'node'
op|'='
name|'doc'
op|'.'
name|'find'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'nic'
op|'['
string|"'net_type'"
op|']'
op|','
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'nic'
op|'['
string|"'mac_addr'"
op|']'
op|','
nl|'\n'
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'nic'
op|'['
string|"'target_dev'"
op|']'
op|','
nl|'\n'
name|'node'
op|'.'
name|'find'
op|'('
string|'"target"'
op|')'
op|'.'
name|'get'
op|'('
string|'"dev"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bridge_driver
dedent|''
dedent|''
name|'def'
name|'test_bridge_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'vif'
op|'.'
name|'LibvirtBridgeDriver'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'_get_instance_xml'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'doc'
op|'.'
name|'findall'
op|'('
string|"'./devices/interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ret'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'node'
op|'='
name|'ret'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"bridge"'
op|')'
newline|'\n'
name|'br_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"source"'
op|')'
op|'.'
name|'get'
op|'('
string|'"bridge"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'br_name'
op|','
name|'self'
op|'.'
name|'net'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mac'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'unplug'
op|'('
name|'None'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ovs_ethernet_driver
dedent|''
name|'def'
name|'test_ovs_ethernet_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'vif'
op|'.'
name|'LibvirtOpenVswitchDriver'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'_get_instance_xml'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'doc'
op|'.'
name|'findall'
op|'('
string|"'./devices/interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ret'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'node'
op|'='
name|'ret'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"ethernet"'
op|')'
newline|'\n'
name|'dev_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"target"'
op|')'
op|'.'
name|'get'
op|'('
string|'"dev"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'dev_name'
op|'.'
name|'startswith'
op|'('
string|'"tap"'
op|')'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mac'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
name|'script'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"script"'
op|')'
op|'.'
name|'get'
op|'('
string|'"path"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'script'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'unplug'
op|'('
name|'None'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ovs_virtualport_driver
dedent|''
name|'def'
name|'test_ovs_virtualport_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'vif'
op|'.'
name|'LibvirtOpenVswitchVirtualPortDriver'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'_get_instance_xml'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'doc'
op|'.'
name|'findall'
op|'('
string|"'./devices/interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ret'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'node'
op|'='
name|'ret'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"bridge"'
op|')'
newline|'\n'
nl|'\n'
name|'br_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"source"'
op|')'
op|'.'
name|'get'
op|'('
string|'"bridge"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'br_name'
op|','
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mac'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
name|'vp'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"virtualport"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vp'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"openvswitch"'
op|')'
newline|'\n'
name|'iface_id_found'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'p_elem'
name|'in'
name|'vp'
op|'.'
name|'findall'
op|'('
string|'"parameters"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'iface_id'
op|'='
name|'p_elem'
op|'.'
name|'get'
op|'('
string|'"interfaceid"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'iface_id'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'iface_id'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
name|'iface_id_found'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'iface_id_found'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'unplug'
op|'('
name|'None'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quantum_bridge_ethernet_driver
dedent|''
name|'def'
name|'test_quantum_bridge_ethernet_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'vif'
op|'.'
name|'QuantumLinuxBridgeVIFDriver'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'_get_instance_xml'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'doc'
op|'.'
name|'findall'
op|'('
string|"'./devices/interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ret'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'node'
op|'='
name|'ret'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"bridge"'
op|')'
newline|'\n'
name|'dev_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"target"'
op|')'
op|'.'
name|'get'
op|'('
string|'"dev"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'dev_name'
op|'.'
name|'startswith'
op|'('
string|'"tap"'
op|')'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mac'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
name|'br_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"source"'
op|')'
op|'.'
name|'get'
op|'('
string|'"bridge"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'br_name'
op|'.'
name|'startswith'
op|'('
string|'"brq"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'unplug'
op|'('
name|'None'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quantum_hybrid_driver
dedent|''
name|'def'
name|'test_quantum_hybrid_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
name|'vif'
op|'.'
name|'LibvirtHybridOVSBridgeDriver'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'_get_instance_xml'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'doc'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'doc'
op|'.'
name|'findall'
op|'('
string|"'./devices/interface'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ret'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'node'
op|'='
name|'ret'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|','
string|'"bridge"'
op|')'
newline|'\n'
name|'br_name'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"source"'
op|')'
op|'.'
name|'get'
op|'('
string|'"bridge"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'br_name'
op|','
name|'self'
op|'.'
name|'net'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'node'
op|'.'
name|'find'
op|'('
string|'"mac"'
op|')'
op|'.'
name|'get'
op|'('
string|'"address"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mac'
op|','
name|'self'
op|'.'
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'.'
name|'unplug'
op|'('
name|'None'
op|','
op|'('
name|'self'
op|'.'
name|'net'
op|','
name|'self'
op|'.'
name|'mapping'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
