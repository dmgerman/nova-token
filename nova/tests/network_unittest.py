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
name|'import'
name|'IPy'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'exception'
name|'import'
name|'NoMoreAddresses'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|class|NetworkTestCase
name|'class'
name|'NetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'NetworkTestCase'
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
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'fake_storage'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_network'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_size'
op|'='
number|'32'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'='
name|'FakeDNSMasq'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'netuser'"
op|','
string|"'netuser'"
op|','
string|"'netuser'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
number|'6'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'project%s'"
op|'%'
name|'i'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
name|'name'
op|','
string|"'netuser'"
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'network'
op|'='
name|'network'
op|'.'
name|'PublicNetworkController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
number|'6'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'project%s'"
op|'%'
name|'i'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
string|"'netuser'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_public_network_allocation
dedent|''
name|'def'
name|'test_public_network_allocation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pubnet'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'public_range'
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_ip'
op|'('
string|'"netuser"'
op|','
string|'"project0"'
op|','
string|'"public"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'address'
op|')'
name|'in'
name|'pubnet'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'address'
op|')'
name|'in'
name|'self'
op|'.'
name|'network'
op|'.'
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_deallocate_ip
dedent|''
name|'def'
name|'test_allocate_deallocate_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
string|'"project0"'
op|','
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Was allocated %s"'
op|'%'
op|'('
name|'address'
op|')'
op|')'
newline|'\n'
name|'net'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
string|'"project0"'
op|','
string|'"default"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'hostname'
op|'='
string|'"test-host"'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'issue_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
comment|"# Doesn't go away until it's dhcp released"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_range_allocation
dedent|''
name|'def'
name|'test_range_allocation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'secondmac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'hostname'
op|'='
string|'"test-host"'
newline|'\n'
name|'address'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
string|'"project0"'
op|','
name|'mac'
op|')'
newline|'\n'
name|'secondaddress'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
string|'"project1"'
op|','
name|'secondmac'
op|')'
newline|'\n'
name|'net'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
string|'"project0"'
op|','
string|'"default"'
op|')'
newline|'\n'
name|'secondnet'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
string|'"project1"'
op|','
string|'"default"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'is_in_project'
op|'('
name|'secondaddress'
op|','
string|'"project1"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# Addresses are allocated before they're issued"
nl|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'issue_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'issue_ip'
op|'('
name|'secondmac'
op|','
name|'secondaddress'
op|','
nl|'\n'
name|'hostname'
op|','
name|'secondnet'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# First address release shouldn't affect the second"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'is_in_project'
op|'('
name|'secondaddress'
op|','
string|'"project1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'secondaddress'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'secondmac'
op|','
name|'secondaddress'
op|','
nl|'\n'
name|'hostname'
op|','
name|'secondnet'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'secondaddress'
op|','
string|'"project1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_subnet_edge
dedent|''
name|'def'
name|'test_subnet_edge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'secondaddress'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
string|'"netuser"'
op|','
string|'"project0"'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
name|'hostname'
op|'='
string|'"toomany-hosts"'
newline|'\n'
name|'for'
name|'project'
name|'in'
name|'range'
op|'('
number|'1'
op|','
number|'5'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'project_id'
op|'='
string|'"project%s"'
op|'%'
op|'('
name|'project'
op|')'
newline|'\n'
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'mac2'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'mac3'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'address'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
name|'project_id'
op|','
name|'mac'
op|')'
newline|'\n'
name|'address2'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
name|'project_id'
op|','
name|'mac2'
op|')'
newline|'\n'
name|'address3'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
string|'"netuser"'
op|','
name|'project_id'
op|','
name|'mac3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address2'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'is_in_project'
op|'('
name|'address3'
op|','
string|'"project0"'
op|')'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'address2'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'address3'
op|')'
newline|'\n'
name|'net'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
name|'project_id'
op|','
string|'"default"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac2'
op|','
name|'address2'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac3'
op|','
name|'address3'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
dedent|''
name|'net'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
string|'"project0"'
op|','
string|'"default"'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'secondaddress'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'mac'
op|','
name|'address'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_release_before_deallocate
dedent|''
name|'def'
name|'test_release_before_deallocate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_deallocate_before_issued
dedent|''
name|'def'
name|'test_deallocate_before_issued'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_addresses
dedent|''
name|'def'
name|'test_too_many_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Here, we test that a proper NoMoreAddresses exception is raised.\n\n        However, the number of available IP addresses depends on the test\n        environment\'s setup.\n\n        Network size is set in test fixture\'s setUp method.\n            \n        There are FLAGS.cnt_vpn_clients addresses reserved for VPN (NUM_RESERVED_VPN_IPS)\n\n        And there are NUM_STATIC_IPS that are always reserved by Nova for the necessary\n        services (gateway, CloudPipe, etc)\n\n        So we should get flags.network_size - (NUM_STATIC_IPS + \n                                               NUM_PREALLOCATED_IPS + \n                                               NUM_RESERVED_VPN_IPS)\n        usable addresses\n        """'
newline|'\n'
name|'net'
op|'='
name|'network'
op|'.'
name|'get_project_network'
op|'('
string|'"project0"'
op|','
string|'"default"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Determine expected number of available IP addresses'
nl|'\n'
name|'num_static_ips'
op|'='
name|'net'
op|'.'
name|'num_static_ips'
newline|'\n'
name|'num_preallocated_ips'
op|'='
name|'len'
op|'('
name|'net'
op|'.'
name|'hosts'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'num_reserved_vpn_ips'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'cnt_vpn_clients'
newline|'\n'
name|'num_available_ips'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'network_size'
op|'-'
op|'('
name|'num_static_ips'
op|'+'
name|'num_preallocated_ips'
op|'+'
name|'num_reserved_vpn_ips'
op|')'
newline|'\n'
nl|'\n'
name|'hostname'
op|'='
string|'"toomany-hosts"'
newline|'\n'
name|'macs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'addresses'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
op|'('
name|'num_available_ips'
op|'-'
number|'1'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'macs'
op|'['
name|'i'
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'addresses'
op|'['
name|'i'
op|']'
op|'='
name|'network'
op|'.'
name|'allocate_ip'
op|'('
string|'"netuser"'
op|','
string|'"project0"'
op|','
name|'macs'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'issue_ip'
op|'('
name|'macs'
op|'['
name|'i'
op|']'
op|','
name|'addresses'
op|'['
name|'i'
op|']'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NoMoreAddresses'
op|','
name|'network'
op|'.'
name|'allocate_ip'
op|','
string|'"netuser"'
op|','
string|'"project0"'
op|','
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
op|'('
name|'num_available_ips'
op|'-'
number|'1'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'network'
op|'.'
name|'deallocate_ip'
op|'('
name|'addresses'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dnsmasq'
op|'.'
name|'release_ip'
op|'('
name|'macs'
op|'['
name|'i'
op|']'
op|','
name|'addresses'
op|'['
name|'i'
op|']'
op|','
name|'hostname'
op|','
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|is_in_project
dedent|''
dedent|''
dedent|''
name|'def'
name|'is_in_project'
op|'('
name|'address'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'address'
name|'in'
name|'network'
op|'.'
name|'get_project_network'
op|'('
name|'project_id'
op|')'
op|'.'
name|'list_addresses'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_get_project_addresses
dedent|''
name|'def'
name|'_get_project_addresses'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'project_addresses'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'addr'
name|'in'
name|'network'
op|'.'
name|'get_project_network'
op|'('
name|'project_id'
op|')'
op|'.'
name|'list_addresses'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_addresses'
op|'.'
name|'append'
op|'('
name|'addr'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'project_addresses'
newline|'\n'
nl|'\n'
DECL|function|binpath
dedent|''
name|'def'
name|'binpath'
op|'('
name|'script'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'__file__'
op|','
string|'"../../../bin"'
op|','
name|'script'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeDNSMasq
dedent|''
name|'class'
name|'FakeDNSMasq'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|issue_ip
indent|'    '
name|'def'
name|'issue_ip'
op|'('
name|'self'
op|','
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
string|'"%s add %s %s %s"'
op|'%'
op|'('
name|'binpath'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|')'
newline|'\n'
name|'env'
op|'='
op|'{'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'interface'
op|','
nl|'\n'
string|"'TESTING'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|'}'
newline|'\n'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"ISSUE_IP: %s, %s "'
op|'%'
op|'('
name|'out'
op|','
name|'err'
op|')'
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
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
string|'"%s del %s %s %s"'
op|'%'
op|'('
name|'binpath'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|')'
newline|'\n'
name|'env'
op|'='
op|'{'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'interface'
op|','
nl|'\n'
string|"'TESTING'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|'}'
newline|'\n'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"RELEASE_IP: %s, %s "'
op|'%'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
