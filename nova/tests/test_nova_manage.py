begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
nl|'\n'
comment|'#    Copyright 2011 Ilya Alekseyev'
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
name|'gettext'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
DECL|variable|TOPDIR
name|'TOPDIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|')'
op|')'
newline|'\n'
DECL|variable|NOVA_MANAGE_PATH
name|'NOVA_MANAGE_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TOPDIR'
op|','
string|"'bin'"
op|','
string|"'nova-manage'"
op|')'
newline|'\n'
nl|'\n'
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|','
name|'unicode'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'dont_write_bytecode'
op|'='
name|'True'
newline|'\n'
name|'import'
name|'imp'
newline|'\n'
DECL|variable|nova_manage
name|'nova_manage'
op|'='
name|'imp'
op|'.'
name|'load_source'
op|'('
string|"'nova_manage.py'"
op|','
name|'NOVA_MANAGE_PATH'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'dont_write_bytecode'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'import'
name|'exception'
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
nl|'\n'
DECL|class|FixedIpCommandsTestCase
name|'class'
name|'FixedIpCommandsTestCase'
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
name|'FixedIpCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'cidr'
op|'='
string|"'10.0.0.0/24'"
newline|'\n'
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'net_info'
op|'='
op|'{'
string|"'bridge'"
op|':'
string|"'fakebr'"
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
string|"'fakeeth'"
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'FLAGS'
op|'.'
name|'flat_network_dns'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'cidr'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'str'
op|'('
name|'net'
op|'.'
name|'netmask'
op|')'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'str'
op|'('
name|'net'
op|'['
number|'1'
op|']'
op|')'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'str'
op|'('
name|'net'
op|'.'
name|'broadcast'
op|')'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
name|'str'
op|'('
name|'net'
op|'['
number|'2'
op|']'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'db'
op|'.'
name|'network_create_safe'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'net_info'
op|')'
newline|'\n'
name|'num_ips'
op|'='
name|'len'
op|'('
name|'net'
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
name|'net'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
name|'reserved'
op|'='
op|'('
name|'index'
op|'=='
number|'1'
name|'or'
name|'index'
op|'=='
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'network_id'"
op|':'
name|'self'
op|'.'
name|'network'
op|'['
string|"'id'"
op|']'
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
dedent|''
name|'self'
op|'.'
name|'commands'
op|'='
name|'nova_manage'
op|'.'
name|'FixedIpCommands'
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
name|'db'
op|'.'
name|'network_delete_safe'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'super'
op|'('
name|'FixedIpCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserve
dedent|''
name|'def'
name|'test_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'commands'
op|'.'
name|'reserve'
op|'('
string|"'10.0.0.100'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'10.0.0.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|'['
string|"'reserved'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unreserve
dedent|''
name|'def'
name|'test_unreserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
string|"'10.0.0.100'"
op|','
nl|'\n'
op|'{'
string|"'reserved'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'unreserve'
op|'('
string|"'10.0.0.100'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'10.0.0.100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|'['
string|"'reserved'"
op|']'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|class|NetworkCommandsTestCase
dedent|''
dedent|''
name|'class'
name|'NetworkCommandsTestCase'
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
comment|"#        print 'piyo'"
nl|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkCommandsTestCase'
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
name|'commands'
op|'='
name|'nova_manage'
op|'.'
name|'NetworkCommands'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'nets'
op|'='
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'nets'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'network_delete_safe'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'net'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
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
name|'NetworkCommandsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'commands'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'label'
op|'='
string|"'Test'"
op|','
nl|'\n'
name|'fixed_range_v4'
op|'='
string|"'10.2.0.0/24'"
op|','
nl|'\n'
name|'fixed_range_v6'
op|'='
string|"'fd00:2::/120'"
op|','
nl|'\n'
name|'num_networks'
op|'='
number|'1'
op|','
nl|'\n'
name|'network_size'
op|'='
number|'256'
op|','
nl|'\n'
name|'vlan_start'
op|'='
number|'200'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
string|"'eth0'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'net'
op|'='
name|'db'
op|'.'
name|'network_get_by_cidr'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'label'"
op|']'
op|','
string|"'Test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'cidr'"
op|']'
op|','
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'netmask'"
op|']'
op|','
string|"'255.255.255.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'cidr_v6'"
op|']'
op|','
string|"'fd00:2::/120'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'bridge_interface'"
op|']'
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net'
op|'['
string|"'vlan'"
op|']'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list
dedent|''
name|'def'
name|'test_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_create'
op|'('
op|')'
newline|'\n'
name|'net'
op|'='
name|'db'
op|'.'
name|'network_get_by_cidr'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
name|'output'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'output'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'list'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'sys'
op|'.'
name|'__stdout__'
newline|'\n'
name|'result'
op|'='
name|'output'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'_fmt'
op|'='
string|'"%-5s\\t%-18s\\t%-15s\\t%-15s\\t%-15s\\t%-15s\\t%-15s\\t%-15s\\t%-15s"'
newline|'\n'
name|'head'
op|'='
name|'_fmt'
op|'%'
op|'('
name|'_'
op|'('
string|"'id'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'IPv4'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'IPv6'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'start address'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'DNS1'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'DNS2'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'VlanID'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|"'project'"
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|'"uuid"'
op|')'
op|')'
newline|'\n'
name|'body'
op|'='
name|'_fmt'
op|'%'
op|'('
nl|'\n'
name|'net'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'10.2.0.0/24'"
op|','
nl|'\n'
string|"'fd00:2::/120'"
op|','
nl|'\n'
string|"'10.2.0.3'"
op|','
nl|'\n'
string|"'None'"
op|','
nl|'\n'
string|"'None'"
op|','
nl|'\n'
string|"'200'"
op|','
nl|'\n'
string|"'None'"
op|','
nl|'\n'
name|'net'
op|'['
string|"'uuid'"
op|']'
op|','
op|')'
newline|'\n'
name|'answer'
op|'='
string|"'%s\\n%s\\n'"
op|'%'
op|'('
name|'head'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'answer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'commands'
op|'.'
name|'delete'
op|'('
name|'fixed_range'
op|'='
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
name|'net_exist'
op|'='
name|'True'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'='
name|'db'
op|'.'
name|'network_get_by_cidr'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'10.2.0.0/24'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFoundForCidr'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'net_exist'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net_exist'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
