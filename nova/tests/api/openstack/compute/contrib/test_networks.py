begin_unit
comment|'# Copyright 2011 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'networks'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_NETWORKS
name|'FAKE_NETWORKS'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
string|"'br100'"
op|','
string|"'vpn_public_port'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
string|"'10.0.0.3'"
op|','
string|"'bridge_interface'"
op|':'
string|"'eth0'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|"'2011-08-16 09:26:13.048257'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
string|"'20c8acc0-f747-4d71-a389-46d078ebf047'"
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'None'
op|','
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
string|"'label'"
op|':'
string|"'mynet_0'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'1234'"
op|','
string|"'rxtx_base'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vpn_private_address'"
op|':'
string|"'10.0.0.2'"
op|','
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'vlan'"
op|':'
number|'100'
op|','
string|"'broadcast'"
op|':'
string|"'10.0.0.7'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.248'"
op|','
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'10.0.0.0/29'"
op|','
nl|'\n'
string|"'vpn_public_address'"
op|':'
string|"'127.0.0.1'"
op|','
string|"'multi_host'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'dns1'"
op|':'
name|'None'
op|','
string|"'dns2'"
op|':'
name|'None'
op|','
string|"'host'"
op|':'
string|"'nsokolov-desktop'"
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'None'
op|','
string|"'netmask_v6'"
op|':'
name|'None'
op|','
string|"'priority'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'2011-08-15 06:19:19.387525'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
string|"'br101'"
op|','
string|"'vpn_public_port'"
op|':'
number|'1001'
op|','
nl|'\n'
string|"'dhcp_start'"
op|':'
string|"'10.0.0.11'"
op|','
string|"'bridge_interface'"
op|':'
string|"'eth0'"
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
string|"'id'"
op|':'
number|'2'
op|','
string|"'cidr_v6'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
string|"'gateway'"
op|':'
string|"'10.0.0.9'"
op|','
nl|'\n'
string|"'label'"
op|':'
string|"'mynet_1'"
op|','
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vpn_private_address'"
op|':'
string|"'10.0.0.10'"
op|','
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'vlan'"
op|':'
number|'101'
op|','
string|"'broadcast'"
op|':'
string|"'10.0.0.15'"
op|','
string|"'rxtx_base'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.248'"
op|','
string|"'injected'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'10.0.0.10/29'"
op|','
string|"'vpn_public_address'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'False'
op|','
string|"'dns1'"
op|':'
name|'None'
op|','
string|"'dns2'"
op|':'
name|'None'
op|','
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'None'
op|','
string|"'netmask_v6'"
op|':'
name|'None'
op|','
string|"'priority'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'2011-08-15 06:19:19.885495'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_USER_NETWORKS
name|'FAKE_USER_NETWORKS'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
string|"'cidr'"
op|':'
string|"'10.0.0.0/29'"
op|','
string|"'netmask'"
op|':'
string|"'255.255.255.248'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
string|"'broadcast'"
op|':'
string|"'10.0.0.7'"
op|','
string|"'dns1'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'None'
op|','
string|"'cidr_v6'"
op|':'
name|'None'
op|','
string|"'gateway_v6'"
op|':'
name|'None'
op|','
string|"'label'"
op|':'
string|"'mynet_0'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'None'
op|','
string|"'uuid'"
op|':'
string|"'20c8acc0-f747-4d71-a389-46d078ebf047'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
string|"'cidr'"
op|':'
string|"'10.0.0.10/29'"
op|','
string|"'netmask'"
op|':'
string|"'255.255.255.248'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.9'"
op|','
string|"'broadcast'"
op|':'
string|"'10.0.0.15'"
op|','
string|"'dns1'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'dns2'"
op|':'
name|'None'
op|','
string|"'cidr_v6'"
op|':'
name|'None'
op|','
string|"'gateway_v6'"
op|':'
name|'None'
op|','
string|"'label'"
op|':'
string|"'mynet_1'"
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNetworkAPI
name|'class'
name|'FakeNetworkAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'networks'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
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
name|'for'
name|'i'
op|','
name|'network'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'network'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForUUID'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#NOTE(bcwaldon): this does nothing other than check for existance'
nl|'\n'
DECL|member|disassociate
dedent|''
name|'def'
name|'disassociate'
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
name|'for'
name|'i'
op|','
name|'network'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'network'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|'=='
name|'network_id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'networks'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
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
name|'for'
name|'network'
name|'in'
name|'self'
op|'.'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'network'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|'=='
name|'network_id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'network'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworksTest
dedent|''
dedent|''
name|'class'
name|'NetworksTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'NetworksTest'
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
name|'fake_network_api'
op|'='
name|'FakeNetworkAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'networks'
op|'.'
name|'NetworkController'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_list_all_as_user
dedent|''
name|'def'
name|'test_network_list_all_as_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'maxDiff'
op|'='
name|'None'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'FAKE_USER_NETWORKS'
op|')'
newline|'\n'
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'del'
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'res_dict'
op|','
op|'{'
string|"'networks'"
op|':'
name|'expected'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_list_all_as_admin
dedent|''
name|'def'
name|'test_network_list_all_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'del'
name|'expected'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'res_dict'
op|','
op|'{'
string|"'networks'"
op|':'
name|'expected'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_disassociate
dedent|''
name|'def'
name|'test_network_disassociate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/%s/action'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|'('
name|'req'
op|','
name|'uuid'
op|','
op|'{'
string|"'disassociate'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_disassociate_not_found
dedent|''
name|'def'
name|'test_network_disassociate_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/100/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'action'
op|','
nl|'\n'
name|'req'
op|','
number|'100'
op|','
op|'{'
string|"'disassociate'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_get_as_user
dedent|''
name|'def'
name|'test_network_get_as_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'FAKE_USER_NETWORKS'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'network'"
op|':'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'FAKE_USER_NETWORKS'
op|'['
number|'0'
op|']'
op|')'
op|'}'
newline|'\n'
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'del'
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_get_as_admin
dedent|''
name|'def'
name|'test_network_get_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'is_admin'
op|'='
name|'True'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'network'"
op|':'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|')'
op|'}'
newline|'\n'
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'del'
name|'expected'
op|'['
string|"'network'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_get_not_found
dedent|''
name|'def'
name|'test_network_get_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_delete
dedent|''
name|'def'
name|'test_network_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_delete_not_found
dedent|''
name|'def'
name|'test_network_delete_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/1234/os-networks/100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'req'
op|','
number|'100'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
