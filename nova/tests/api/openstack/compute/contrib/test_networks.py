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
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'math'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'import'
name|'uuid'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'networks_associate'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
string|"'uuid'"
op|':'
string|"'20c8acc0-f747-4d71-a389-46d078ebf000'"
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
string|"'uuid'"
op|':'
string|"'20c8acc0-f747-4d71-a389-46d078ebf000'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|NEW_NETWORK
name|'NEW_NETWORK'
op|'='
op|'{'
nl|'\n'
string|'"network"'
op|':'
op|'{'
nl|'\n'
string|'"bridge_interface"'
op|':'
string|'"eth0"'
op|','
nl|'\n'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 111"'
op|','
nl|'\n'
string|'"vlan_start"'
op|':'
number|'111'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
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
DECL|variable|_sentinel
indent|'    '
name|'_sentinel'
op|'='
name|'object'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'uuid'
op|'='
name|'network_id'
op|')'
newline|'\n'
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
name|'network_uuid'
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
name|'network_uuid'
op|':'
newline|'\n'
indent|'                '
name|'network'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'None'
newline|'\n'
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
name|'network_id'
op|'='
name|'network_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate
dedent|''
name|'def'
name|'associate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|','
name|'host'
op|'='
name|'_sentinel'
op|','
nl|'\n'
name|'project'
op|'='
name|'_sentinel'
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
name|'network_uuid'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'host'
name|'is'
name|'not'
name|'FakeNetworkAPI'
op|'.'
name|'_sentinel'
op|':'
newline|'\n'
indent|'                    '
name|'network'
op|'['
string|"'host'"
op|']'
op|'='
name|'host'
newline|'\n'
dedent|''
name|'if'
name|'project'
name|'is'
name|'not'
name|'FakeNetworkAPI'
op|'.'
name|'_sentinel'
op|':'
newline|'\n'
indent|'                    '
name|'network'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project'
newline|'\n'
dedent|''
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
name|'network_id'
op|'='
name|'network_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_network_to_project
dedent|''
name|'def'
name|'add_network_to_project'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'project_id'
op|','
name|'network_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'network_uuid'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'network'
name|'in'
name|'self'
op|'.'
name|'networks'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'network'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|','
name|'None'
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'network'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'return'
newline|'\n'
dedent|''
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
name|'network_uuid'
op|':'
newline|'\n'
indent|'                '
name|'network'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
dedent|''
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
name|'network_id'
op|'='
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet_bits'
op|'='
name|'int'
op|'('
name|'math'
op|'.'
name|'ceil'
op|'('
name|'math'
op|'.'
name|'log'
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'network_size'"
op|','
name|'CONF'
op|'.'
name|'network_size'
op|')'
op|','
number|'2'
op|')'
op|')'
op|')'
newline|'\n'
name|'fixed_net_v4'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'kwargs'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'prefixlen_v4'
op|'='
number|'32'
op|'-'
name|'subnet_bits'
newline|'\n'
name|'subnets_v4'
op|'='
name|'list'
op|'('
name|'fixed_net_v4'
op|'.'
name|'subnet'
op|'('
nl|'\n'
name|'prefixlen_v4'
op|','
nl|'\n'
name|'count'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'num_networks'"
op|','
name|'CONF'
op|'.'
name|'num_networks'
op|')'
op|')'
op|')'
newline|'\n'
name|'new_networks'
op|'='
op|'['
op|']'
newline|'\n'
name|'new_id'
op|'='
name|'max'
op|'('
op|'('
name|'net'
op|'['
string|"'id'"
op|']'
name|'for'
name|'net'
name|'in'
name|'self'
op|'.'
name|'networks'
op|')'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'subnet_v4'
name|'in'
name|'enumerate'
op|'('
name|'subnets_v4'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_id'
op|'+='
number|'1'
newline|'\n'
name|'net'
op|'='
op|'{'
string|"'id'"
op|':'
name|'new_id'
op|','
string|"'uuid'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'net'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'str'
op|'('
name|'subnet_v4'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'netmask'"
op|']'
op|'='
name|'str'
op|'('
name|'subnet_v4'
op|'.'
name|'netmask'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'gateway'"
op|')'
name|'or'
name|'str'
op|'('
name|'subnet_v4'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'broadcast'"
op|']'
op|'='
name|'str'
op|'('
name|'subnet_v4'
op|'.'
name|'broadcast'
op|')'
newline|'\n'
name|'net'
op|'['
string|"'dhcp_start'"
op|']'
op|'='
name|'str'
op|'('
name|'subnet_v4'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|'.'
name|'iterkeys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'net'
op|'.'
name|'setdefault'
op|'('
name|'key'
op|','
name|'kwargs'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
name|'new_networks'
op|'.'
name|'append'
op|'('
name|'net'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'networks'
op|'+='
name|'new_networks'
newline|'\n'
name|'return'
name|'new_networks'
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
name|'self'
op|'.'
name|'associate_controller'
op|'='
name|'networks_associate'
op|'.'
name|'NetworkAssociateActionController'
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
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|network_uuid_to_id
name|'def'
name|'network_uuid_to_id'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'['
string|"'id'"
op|']'
op|'='
name|'network'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'del'
name|'network'
op|'['
string|"'uuid'"
op|']'
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
name|'for'
name|'network'
name|'in'
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_uuid_to_id'
op|'('
name|'network'
op|')'
newline|'\n'
dedent|''
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
name|'for'
name|'network'
name|'in'
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_uuid_to_id'
op|'('
name|'network'
op|')'
newline|'\n'
dedent|''
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
name|'_disassociate_host_and_project'
op|'('
nl|'\n'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'project_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_disassociate_host_only
dedent|''
name|'def'
name|'test_network_disassociate_host_only'
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
name|'associate_controller'
op|'.'
name|'_disassociate_host_only'
op|'('
nl|'\n'
name|'req'
op|','
name|'uuid'
op|','
op|'{'
string|"'disassociate_host'"
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
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_disassociate_project_only
dedent|''
name|'def'
name|'test_network_disassociate_project_only'
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
name|'associate_controller'
op|'.'
name|'_disassociate_project_only'
op|'('
nl|'\n'
name|'req'
op|','
name|'uuid'
op|','
op|'{'
string|"'disassociate_project'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'project_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'self'
op|'.'
name|'fake_network_api'
op|'.'
name|'networks'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|','
name|'None'
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
name|'_disassociate_host_and_project'
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
name|'self'
op|'.'
name|'network_uuid_to_id'
op|'('
name|'expected'
op|'['
string|"'network'"
op|']'
op|')'
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
name|'self'
op|'.'
name|'network_uuid_to_id'
op|'('
name|'expected'
op|'['
string|"'network'"
op|']'
op|')'
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
nl|'\n'
DECL|member|test_network_add
dedent|''
name|'def'
name|'test_network_add'
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
number|'1'
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
string|"'/v2/1234/os-networks/add'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'add'
op|'('
name|'req'
op|','
op|'{'
string|"'id'"
op|':'
name|'uuid'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'network'"
op|']'
op|'['
string|"'project_id'"
op|']'
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_associate_with_host
dedent|''
name|'def'
name|'test_network_associate_with_host'
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
number|'1'
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
name|'associate_controller'
op|'.'
name|'_associate_host'
op|'('
nl|'\n'
name|'req'
op|','
name|'uuid'
op|','
op|'{'
string|"'associate_host'"
op|':'
string|'"TestHost"'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'network'"
op|']'
op|'['
string|"'host'"
op|']'
op|','
string|"'TestHost'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create
dedent|''
name|'def'
name|'test_network_create'
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'NEW_NETWORK'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'network'"
name|'in'
name|'res_dict'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'res_dict'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'res_dict'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
op|'.'
nl|'\n'
name|'startswith'
op|'('
name|'NEW_NETWORK'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_large
dedent|''
name|'def'
name|'test_network_create_large'
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
name|'large_network'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'NEW_NETWORK'
op|')'
newline|'\n'
name|'large_network'
op|'['
string|"'network'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|'='
string|"'128.0.0.0/4'"
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'large_network'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'network'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
name|'large_network'
op|'['
string|"'network'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
