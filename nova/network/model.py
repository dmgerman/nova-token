begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'netaddr'
newline|'\n'
nl|'\n'
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
name|'jsonutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_string_keys
name|'def'
name|'ensure_string_keys'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
comment|'# http://bugs.python.org/issue4978'
nl|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
op|'['
op|'('
name|'str'
op|'('
name|'k'
op|')'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'d'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# Constants for the 'vif_type' field in VIF class"
nl|'\n'
DECL|variable|VIF_TYPE_OVS
dedent|''
name|'VIF_TYPE_OVS'
op|'='
string|"'ovs'"
newline|'\n'
DECL|variable|VIF_TYPE_BRIDGE
name|'VIF_TYPE_BRIDGE'
op|'='
string|"'bridge'"
newline|'\n'
DECL|variable|VIF_TYPE_802_QBG
name|'VIF_TYPE_802_QBG'
op|'='
string|"'802.1qbg'"
newline|'\n'
DECL|variable|VIF_TYPE_802_QBH
name|'VIF_TYPE_802_QBH'
op|'='
string|"'802.1qbh'"
newline|'\n'
DECL|variable|VIF_TYPE_OTHER
name|'VIF_TYPE_OTHER'
op|'='
string|"'other'"
newline|'\n'
nl|'\n'
comment|'# Constant for max length of network interface names'
nl|'\n'
comment|"# eg 'bridge' in the Network class or 'devname' in"
nl|'\n'
comment|'# the VIF class'
nl|'\n'
DECL|variable|NIC_NAME_LEN
name|'NIC_NAME_LEN'
op|'='
number|'14'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Model
name|'class'
name|'Model'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Defines some necessary structures for most of the network models."""'
newline|'\n'
DECL|member|__repr__
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'+'
string|"'('"
op|'+'
name|'dict'
op|'.'
name|'__repr__'
op|'('
name|'self'
op|')'
op|'+'
string|"')'"
newline|'\n'
nl|'\n'
DECL|member|_set_meta
dedent|''
name|'def'
name|'_set_meta'
op|'('
name|'self'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# pull meta out of kwargs if it's there"
nl|'\n'
indent|'        '
name|'self'
op|'['
string|"'meta'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'meta'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|'# update meta with any additional kwargs that may exist'
nl|'\n'
name|'self'
op|'['
string|"'meta'"
op|']'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_meta
dedent|''
name|'def'
name|'get_meta'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""calls get(key, default) on self[\'meta\']."""'
newline|'\n'
name|'return'
name|'self'
op|'['
string|"'meta'"
op|']'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IP
dedent|''
dedent|''
name|'class'
name|'IP'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents an IP address in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'type'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IP'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'address'"
op|']'
op|'='
name|'address'
newline|'\n'
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
name|'type'
newline|'\n'
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# determine version from address if not passed in'
nl|'\n'
name|'if'
name|'self'
op|'['
string|"'address'"
op|']'
name|'and'
name|'not'
name|'self'
op|'['
string|"'version'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'self'
op|'['
string|"'address'"
op|']'
op|')'
op|'.'
name|'version'
newline|'\n'
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidIpAddressError'
op|'('
name|'self'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
string|"'address'"
op|']'
op|'=='
name|'other'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|is_in_subnet
dedent|''
name|'def'
name|'is_in_subnet'
op|'('
name|'self'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'['
string|"'address'"
op|']'
name|'and'
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'self'
op|'['
string|"'address'"
op|']'
op|')'
name|'in'
nl|'\n'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ip'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'IP'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'ip'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIP
dedent|''
dedent|''
name|'class'
name|'FixedIP'
op|'('
name|'IP'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Fixed IP address in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'floating_ips'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FixedIP'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|'='
name|'floating_ips'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'['
string|"'type'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
string|"'fixed'"
newline|'\n'
nl|'\n'
DECL|member|add_floating_ip
dedent|''
dedent|''
name|'def'
name|'add_floating_ip'
op|'('
name|'self'
op|','
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'floating_ip'
name|'not'
name|'in'
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|'.'
name|'append'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|floating_ip_addresses
dedent|''
dedent|''
name|'def'
name|'floating_ip_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'FixedIP'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'fixed_ip'
op|')'
op|')'
newline|'\n'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|'='
op|'['
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'floating_ip'
op|')'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Route
dedent|''
dedent|''
name|'class'
name|'Route'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents an IP Route in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cidr'
op|'='
name|'None'
op|','
name|'gateway'
op|'='
name|'None'
op|','
name|'interface'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Route'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'self'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'gateway'
newline|'\n'
name|'self'
op|'['
string|"'interface'"
op|']'
op|'='
name|'interface'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'route'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'route'
op|'='
name|'Route'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'route'
op|')'
op|')'
newline|'\n'
name|'route'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'route'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'route'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Subnet
dedent|''
dedent|''
name|'class'
name|'Subnet'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Subnet in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cidr'
op|'='
name|'None'
op|','
name|'dns'
op|'='
name|'None'
op|','
name|'gateway'
op|'='
name|'None'
op|','
name|'ips'
op|'='
name|'None'
op|','
nl|'\n'
name|'routes'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Subnet'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
name|'self'
op|'['
string|"'dns'"
op|']'
op|'='
name|'dns'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'gateway'
newline|'\n'
name|'self'
op|'['
string|"'ips'"
op|']'
op|'='
name|'ips'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'routes'"
op|']'
op|'='
name|'routes'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'['
string|"'cidr'"
op|']'
name|'and'
name|'not'
name|'self'
op|'['
string|"'version'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'version'"
op|']'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'self'
op|'['
string|"'cidr'"
op|']'
op|')'
op|'.'
name|'version'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
string|"'cidr'"
op|']'
op|'=='
name|'other'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|add_route
dedent|''
name|'def'
name|'add_route'
op|'('
name|'self'
op|','
name|'new_route'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'new_route'
name|'not'
name|'in'
name|'self'
op|'['
string|"'routes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'routes'"
op|']'
op|'.'
name|'append'
op|'('
name|'new_route'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_dns
dedent|''
dedent|''
name|'def'
name|'add_dns'
op|'('
name|'self'
op|','
name|'dns'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'dns'
name|'not'
name|'in'
name|'self'
op|'['
string|"'dns'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'dns'"
op|']'
op|'.'
name|'append'
op|'('
name|'dns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_ip
dedent|''
dedent|''
name|'def'
name|'add_ip'
op|'('
name|'self'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ip'
name|'not'
name|'in'
name|'self'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'ips'"
op|']'
op|'.'
name|'append'
op|'('
name|'ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|as_netaddr
dedent|''
dedent|''
name|'def'
name|'as_netaddr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convience function to get cidr as a netaddr object."""'
newline|'\n'
name|'return'
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'self'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subnet'
op|'='
name|'Subnet'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'subnet'
op|')'
op|')'
newline|'\n'
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|'='
op|'['
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'dns'
op|')'
name|'for'
name|'dns'
name|'in'
name|'subnet'
op|'['
string|"'dns'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|'='
op|'['
name|'FixedIP'
op|'.'
name|'hydrate'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|'='
op|'['
name|'Route'
op|'.'
name|'hydrate'
op|'('
name|'route'
op|')'
name|'for'
name|'route'
name|'in'
name|'subnet'
op|'['
string|"'routes'"
op|']'
op|']'
newline|'\n'
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'IP'
op|'.'
name|'hydrate'
op|'('
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'subnet'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Network
dedent|''
dedent|''
name|'class'
name|'Network'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Network in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'bridge'
op|'='
name|'None'
op|','
name|'label'
op|'='
name|'None'
op|','
nl|'\n'
name|'subnets'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Network'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'['
string|"'bridge'"
op|']'
op|'='
name|'bridge'
newline|'\n'
name|'self'
op|'['
string|"'label'"
op|']'
op|'='
name|'label'
newline|'\n'
name|'self'
op|'['
string|"'subnets'"
op|']'
op|'='
name|'subnets'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_subnet
dedent|''
name|'def'
name|'add_subnet'
op|'('
name|'self'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'subnet'
name|'not'
name|'in'
name|'self'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'subnets'"
op|']'
op|'.'
name|'append'
op|'('
name|'subnet'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'network'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'Network'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'network'
op|')'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'='
op|'['
name|'Subnet'
op|'.'
name|'hydrate'
op|'('
name|'subnet'
op|')'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIF
dedent|''
dedent|''
name|'class'
name|'VIF'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Virtual Interface in Nova."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'network'
op|'='
name|'None'
op|','
name|'type'
op|'='
name|'None'
op|','
nl|'\n'
name|'devname'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VIF'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'['
string|"'address'"
op|']'
op|'='
name|'address'
newline|'\n'
name|'self'
op|'['
string|"'network'"
op|']'
op|'='
name|'network'
name|'or'
name|'None'
newline|'\n'
name|'self'
op|'['
string|"'type'"
op|']'
op|'='
name|'type'
newline|'\n'
name|'self'
op|'['
string|"'devname'"
op|']'
op|'='
name|'devname'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_meta'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'['
string|"'id'"
op|']'
op|'=='
name|'other'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|fixed_ips
dedent|''
name|'def'
name|'fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'fixed_ip'
name|'for'
name|'subnet'
name|'in'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
nl|'\n'
name|'for'
name|'fixed_ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|floating_ips
dedent|''
name|'def'
name|'floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'floating_ip'
name|'for'
name|'fixed_ip'
name|'in'
name|'self'
op|'.'
name|'fixed_ips'
op|'('
op|')'
nl|'\n'
name|'for'
name|'floating_ip'
name|'in'
name|'fixed_ip'
op|'['
string|"'floating_ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|labeled_ips
dedent|''
name|'def'
name|'labeled_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of all IPs\n\n        The return value looks like this flat structure::\n\n            {\'network_label\': \'my_network\',\n             \'network_id\': \'n8v29837fn234782f08fjxk3ofhb84\',\n             \'ips\': [{\'address\': \'123.123.123.123\',\n                      \'version\': 4,\n                      \'type: \'fixed\',\n                      \'meta\': {...}},\n                     {\'address\': \'124.124.124.124\',\n                      \'version\': 4,\n                      \'type\': \'floating\',\n                      \'meta\': {...}},\n                     {\'address\': \'fe80::4\',\n                      \'version\': 6,\n                      \'type\': \'fixed\',\n                      \'meta\': {...}}]\n        """'
newline|'\n'
name|'if'
name|'self'
op|'['
string|"'network'"
op|']'
op|':'
newline|'\n'
comment|'# remove unecessary fields on fixed_ips'
nl|'\n'
indent|'            '
name|'ips'
op|'='
op|'['
name|'IP'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'ip'
op|')'
op|')'
name|'for'
name|'ip'
name|'in'
name|'self'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|']'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|':'
newline|'\n'
comment|'# remove floating ips from IP, since this is a flat structure'
nl|'\n'
comment|'# of all IPs'
nl|'\n'
indent|'                '
name|'del'
name|'ip'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
comment|'# add floating ips to list (if any)'
nl|'\n'
dedent|''
name|'ips'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'network_label'"
op|':'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'self'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
name|'ips'
op|'}'
newline|'\n'
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vif'
op|'='
name|'VIF'
op|'('
op|'**'
name|'ensure_string_keys'
op|'('
name|'vif'
op|')'
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'='
name|'Network'
op|'.'
name|'hydrate'
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'vif'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkInfo
dedent|''
dedent|''
name|'class'
name|'NetworkInfo'
op|'('
name|'list'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stores and manipulates network information for a Nova instance."""'
newline|'\n'
nl|'\n'
comment|'# NetworkInfo is a list of VIFs'
nl|'\n'
nl|'\n'
DECL|member|fixed_ips
name|'def'
name|'fixed_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all fixed_ips without floating_ips attached."""'
newline|'\n'
name|'return'
op|'['
name|'ip'
name|'for'
name|'vif'
name|'in'
name|'self'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|floating_ips
dedent|''
name|'def'
name|'floating_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all floating_ips."""'
newline|'\n'
name|'return'
op|'['
name|'ip'
name|'for'
name|'vif'
name|'in'
name|'self'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|hydrate
name|'def'
name|'hydrate'
op|'('
name|'cls'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'network_info'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_info'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'network_info'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'NetworkInfo'
op|'('
op|'['
name|'VIF'
op|'.'
name|'hydrate'
op|'('
name|'vif'
op|')'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|json
dedent|''
name|'def'
name|'json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|legacy
dedent|''
name|'def'
name|'legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the legacy network_info representation of self\n        """'
newline|'\n'
DECL|function|get_ip
name|'def'
name|'get_ip'
op|'('
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ip'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|fixed_ip_dict
dedent|''
name|'def'
name|'fixed_ip_dict'
op|'('
name|'ip'
op|','
name|'subnet'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'netmask'
op|'='
name|'str'
op|'('
name|'subnet'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'netmask'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'netmask'
op|'='
name|'subnet'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'_prefixlen'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'ip'"
op|':'
name|'ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'enabled'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'netmask'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'get_ip'
op|'('
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|convert_routes
dedent|''
name|'def'
name|'convert_routes'
op|'('
name|'routes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'routes_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'route'
name|'in'
name|'routes'
op|':'
newline|'\n'
indent|'                '
name|'r'
op|'='
op|'{'
string|"'route'"
op|':'
name|'str'
op|'('
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'route'
op|'['
string|"'cidr'"
op|']'
op|')'
op|'.'
name|'network'
op|')'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'str'
op|'('
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'route'
op|'['
string|"'cidr'"
op|']'
op|')'
op|'.'
name|'netmask'
op|')'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'get_ip'
op|'('
name|'route'
op|'['
string|"'gateway'"
op|']'
op|')'
op|'}'
newline|'\n'
name|'routes_list'
op|'.'
name|'append'
op|'('
name|'r'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'routes_list'
newline|'\n'
nl|'\n'
dedent|''
name|'network_info'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'self'
op|':'
newline|'\n'
comment|"# if vif doesn't have network or that network has no subnets, quit"
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'vif'
op|'['
string|"'network'"
op|']'
name|'or'
name|'not'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'network'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(jkoelker) The legacy format only supports one subnet per'
nl|'\n'
comment|'#                network, so we only use the 1st one of each type'
nl|'\n'
comment|'# NOTE(tr3buchet): o.O'
nl|'\n'
name|'v4_subnets'
op|'='
op|'['
op|']'
newline|'\n'
name|'v6_subnets'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'subnet'
name|'in'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'subnet'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                    '
name|'v4_subnets'
op|'.'
name|'append'
op|'('
name|'subnet'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'v6_subnets'
op|'.'
name|'append'
op|'('
name|'subnet'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'subnet_v4'
op|'='
name|'None'
newline|'\n'
name|'subnet_v6'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'if'
name|'v4_subnets'
op|':'
newline|'\n'
indent|'                '
name|'subnet_v4'
op|'='
name|'v4_subnets'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'v6_subnets'
op|':'
newline|'\n'
indent|'                '
name|'subnet_v6'
op|'='
name|'v6_subnets'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'subnet_v4'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'v4 subnets are required for legacy nw_info'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'message'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'routes'
op|'='
name|'convert_routes'
op|'('
name|'subnet_v4'
op|'['
string|"'routes'"
op|']'
op|')'
newline|'\n'
name|'should_create_bridge'
op|'='
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'should_create_bridge'"
op|','
nl|'\n'
name|'False'
op|')'
newline|'\n'
name|'should_create_vlan'
op|'='
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'should_create_vlan'"
op|','
name|'False'
op|')'
newline|'\n'
name|'gateway'
op|'='
name|'get_ip'
op|'('
name|'subnet_v4'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
name|'dhcp_server'
op|'='
name|'subnet_v4'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|','
name|'gateway'
op|')'
newline|'\n'
nl|'\n'
name|'network_dict'
op|'='
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'network'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'cidr'"
op|':'
name|'subnet_v4'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'cidr_v6'"
op|':'
name|'subnet_v6'
op|'['
string|"'cidr'"
op|']'
name|'if'
name|'subnet_v6'
name|'else'
name|'None'
op|','
nl|'\n'
string|"'vlan'"
op|':'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'vlan'"
op|')'
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'injected'"
op|','
name|'False'
op|')'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'multi_host'"
op|','
name|'False'
op|')'
op|','
nl|'\n'
string|"'bridge_interface'"
op|':'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'bridge_interface'"
op|')'
nl|'\n'
op|'}'
newline|'\n'
comment|"# NOTE(tr3buchet): 'ips' bit here is tricky, we support a single"
nl|'\n'
comment|'#                  subnet but we want all the IPs to be there'
nl|'\n'
comment|'#                  so use the v4_subnets[0] and its IPs are first'
nl|'\n'
comment|'#                  so that eth0 will be from subnet_v4, the rest of'
nl|'\n'
comment|'#                  the IPs will be aliased eth0:1 etc and the'
nl|'\n'
comment|'#                  gateways from their subnets will not be used'
nl|'\n'
name|'info_dict'
op|'='
op|'{'
string|"'label'"
op|':'
name|'network'
op|'['
string|"'label'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'str'
op|'('
name|'subnet_v4'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'broadcast'
op|')'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'vif_type'"
op|':'
name|'vif'
op|'['
string|"'type'"
op|']'
op|','
nl|'\n'
string|"'vif_devname'"
op|':'
name|'vif'
op|'.'
name|'get'
op|'('
string|"'devname'"
op|')'
op|','
nl|'\n'
string|"'vif_uuid'"
op|':'
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'rxtx_cap'"
op|':'
name|'vif'
op|'.'
name|'get_meta'
op|'('
string|"'rxtx_cap'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'dns'"
op|':'
op|'['
name|'get_ip'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'subnet_v4'
op|'['
string|"'dns'"
op|']'
op|']'
op|','
nl|'\n'
string|"'ips'"
op|':'
op|'['
name|'fixed_ip_dict'
op|'('
name|'ip'
op|','
name|'subnet'
op|')'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'v4_subnets'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|']'
op|','
nl|'\n'
string|"'should_create_bridge'"
op|':'
name|'should_create_bridge'
op|','
nl|'\n'
string|"'should_create_vlan'"
op|':'
name|'should_create_vlan'
op|','
nl|'\n'
string|"'dhcp_server'"
op|':'
name|'dhcp_server'
op|'}'
newline|'\n'
name|'if'
name|'routes'
op|':'
newline|'\n'
indent|'                '
name|'info_dict'
op|'['
string|"'routes'"
op|']'
op|'='
name|'routes'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'gateway'
op|':'
newline|'\n'
indent|'                '
name|'info_dict'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'gateway'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'v6_subnets'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'info_dict'
op|'['
string|"'gateway_v6'"
op|']'
op|'='
name|'get_ip'
op|'('
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|')'
newline|'\n'
comment|'# NOTE(tr3buchet): only supporting single v6 subnet here'
nl|'\n'
dedent|''
name|'info_dict'
op|'['
string|"'ip6s'"
op|']'
op|'='
op|'['
name|'fixed_ip_dict'
op|'('
name|'ip'
op|','
name|'subnet_v6'
op|')'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'subnet_v6'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'network_info'
op|'.'
name|'append'
op|'('
op|'('
name|'network_dict'
op|','
name|'info_dict'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_info'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
