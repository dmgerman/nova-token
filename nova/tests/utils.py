begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
comment|'#'
nl|'\n'
nl|'\n'
name|'import'
name|'platform'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'minidns'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_test_admin_context
name|'def'
name|'get_test_admin_context'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_test_image_info
dedent|''
name|'def'
name|'get_test_image_info'
op|'('
name|'context'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_ref'
op|'='
name|'instance_ref'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
name|'image_service'
op|','
name|'image_id'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
name|'context'
op|','
nl|'\n'
name|'image_ref'
op|')'
newline|'\n'
name|'return'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_test_instance_type
dedent|''
name|'def'
name|'get_test_instance_type'
op|'('
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'test_instance_type'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'kinda.big'"
op|','
nl|'\n'
string|"'flavorid'"
op|':'
string|"'someid'"
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'40'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'80'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'1024'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'instance_type_ref'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_type_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'test_instance_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceTypeExists'
op|':'
newline|'\n'
indent|'        '
name|'instance_type_ref'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_type_get_by_name'
op|'('
name|'context'
op|','
nl|'\n'
string|"'kinda.big'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_type_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_test_instance
dedent|''
name|'def'
name|'get_test_instance'
op|'('
name|'context'
op|'='
name|'None'
op|','
name|'instance_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'get_test_instance_type'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance_types'
op|'.'
name|'save_instance_type_info'
op|'('
name|'metadata'
op|','
name|'instance_type'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'test_instance'
op|'='
op|'{'
string|"'memory_kb'"
op|':'
string|"'2048000'"
op|','
nl|'\n'
string|"'basepath'"
op|':'
string|"'/some/path'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
string|"'br100'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'40'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'br101'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'5'"
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'metadata'
op|'}'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|','
name|'test_instance'
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_test_network_info
dedent|''
name|'def'
name|'get_test_network_info'
op|'('
name|'count'
op|'='
number|'1'
op|','
name|'legacy_model'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ipv6'
op|'='
name|'CONF'
op|'.'
name|'use_ipv6'
newline|'\n'
name|'fake'
op|'='
string|"'fake'"
newline|'\n'
name|'fake_ip'
op|'='
string|"'0.0.0.0/0'"
newline|'\n'
name|'fake_ip_2'
op|'='
string|"'0.0.0.1/0'"
newline|'\n'
name|'fake_ip_3'
op|'='
string|"'0.0.0.1/0'"
newline|'\n'
name|'fake_netmask'
op|'='
string|"'255.255.255.255'"
newline|'\n'
name|'fake_vlan'
op|'='
number|'100'
newline|'\n'
name|'fake_bridge_interface'
op|'='
string|"'eth0'"
newline|'\n'
nl|'\n'
DECL|function|legacy
name|'def'
name|'legacy'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'='
op|'{'
string|"'bridge'"
op|':'
name|'fake'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'fake_ip'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'fake_ip'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'fake_vlan'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'fake_bridge_interface'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'mapping'
op|'='
op|'{'
string|"'mac'"
op|':'
name|'fake'
op|','
nl|'\n'
string|"'vif_type'"
op|':'
name|'network_model'
op|'.'
name|'VIF_TYPE_BRIDGE'
op|','
nl|'\n'
string|"'vif_uuid'"
op|':'
string|"'vif-xxx-yyy-zzz'"
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'fake'
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
string|"'fake1'"
op|','
string|"'fake2'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'fake'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'fake'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
op|'{'
string|"'ip'"
op|':'
name|'fake_ip'
op|','
string|"'netmask'"
op|':'
name|'fake_netmask'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'ip'"
op|':'
name|'fake_ip'
op|','
string|"'netmask'"
op|':'
name|'fake_netmask'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'if'
name|'ipv6'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'['
string|"'ip6s'"
op|']'
op|'='
op|'['
op|'{'
string|"'ip'"
op|':'
name|'fake_ip'
op|','
string|"'netmask'"
op|':'
name|'fake_netmask'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'ip'"
op|':'
name|'fake_ip_2'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'ip'"
op|':'
name|'fake_ip_3'
op|'}'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'network'
op|','
name|'mapping'
newline|'\n'
nl|'\n'
DECL|function|current
dedent|''
name|'def'
name|'current'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_ip'
op|'='
string|"'0.0.0.0'"
newline|'\n'
name|'subnet_4'
op|'='
name|'network_model'
op|'.'
name|'Subnet'
op|'('
name|'cidr'
op|'='
name|'fake_ip'
op|','
nl|'\n'
name|'dns'
op|'='
op|'['
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|']'
op|','
nl|'\n'
name|'gateway'
op|'='
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'ips'
op|'='
op|'['
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|']'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|','
nl|'\n'
name|'dhcp_server'
op|'='
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|')'
newline|'\n'
name|'subnet_6'
op|'='
name|'network_model'
op|'.'
name|'Subnet'
op|'('
name|'cidr'
op|'='
name|'fake_ip'
op|','
nl|'\n'
name|'gateway'
op|'='
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'ips'
op|'='
op|'['
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|','
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'fake_ip'
op|')'
op|']'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|','
nl|'\n'
name|'version'
op|'='
number|'6'
op|')'
newline|'\n'
name|'subnets'
op|'='
op|'['
name|'subnet_4'
op|']'
newline|'\n'
name|'if'
name|'ipv6'
op|':'
newline|'\n'
indent|'            '
name|'subnets'
op|'.'
name|'append'
op|'('
name|'subnet_6'
op|')'
newline|'\n'
dedent|''
name|'network'
op|'='
name|'network_model'
op|'.'
name|'Network'
op|'('
name|'id'
op|'='
name|'None'
op|','
nl|'\n'
name|'bridge'
op|'='
name|'fake'
op|','
nl|'\n'
name|'label'
op|'='
name|'None'
op|','
nl|'\n'
name|'subnets'
op|'='
name|'subnets'
op|','
nl|'\n'
name|'vlan'
op|'='
name|'fake_vlan'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'fake_bridge_interface'
op|','
nl|'\n'
name|'injected'
op|'='
name|'False'
op|')'
newline|'\n'
name|'vif'
op|'='
name|'network_model'
op|'.'
name|'VIF'
op|'('
name|'id'
op|'='
string|"'vif-xxx-yyy-zzz'"
op|','
nl|'\n'
name|'address'
op|'='
name|'fake'
op|','
nl|'\n'
name|'network'
op|'='
name|'network'
op|','
nl|'\n'
name|'type'
op|'='
name|'network_model'
op|'.'
name|'VIF_TYPE_BRIDGE'
op|','
nl|'\n'
name|'devname'
op|'='
name|'None'
op|','
nl|'\n'
name|'ovs_interfaceid'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'vif'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'legacy_model'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'legacy'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
name|'count'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
name|'current'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
name|'count'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_osx
dedent|''
dedent|''
name|'def'
name|'is_osx'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'platform'
op|'.'
name|'mac_ver'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'!='
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|test_dns_managers
dedent|''
name|'test_dns_managers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dns_manager
name|'def'
name|'dns_manager'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'test_dns_managers'
newline|'\n'
name|'manager'
op|'='
name|'minidns'
op|'.'
name|'MiniDNS'
op|'('
op|')'
newline|'\n'
name|'test_dns_managers'
op|'.'
name|'append'
op|'('
name|'manager'
op|')'
newline|'\n'
name|'return'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup_dns_managers
dedent|''
name|'def'
name|'cleanup_dns_managers'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'test_dns_managers'
newline|'\n'
name|'for'
name|'manager'
name|'in'
name|'test_dns_managers'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'.'
name|'delete_dns_file'
op|'('
op|')'
newline|'\n'
dedent|''
name|'test_dns_managers'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
