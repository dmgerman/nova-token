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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
nl|'\n'
string|'"""Network-related utilities for supporting libvirt connection code."""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'injected_network_template'"
op|','
string|"'nova.virt.disk.api'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|Template
name|'Template'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_late_load_cheetah
name|'def'
name|'_late_load_cheetah'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'Template'
newline|'\n'
name|'if'
name|'Template'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'t'
op|'='
name|'__import__'
op|'('
string|"'Cheetah.Template'"
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
op|'['
string|"'Template'"
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'Template'
op|'='
name|'t'
op|'.'
name|'Template'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_net_and_mask
dedent|''
dedent|''
name|'def'
name|'get_net_and_mask'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'net'
op|'.'
name|'ip'
op|')'
op|','
name|'str'
op|'('
name|'net'
op|'.'
name|'netmask'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_net_and_prefixlen
dedent|''
name|'def'
name|'get_net_and_prefixlen'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'net'
op|'.'
name|'ip'
op|')'
op|','
name|'str'
op|'('
name|'net'
op|'.'
name|'_prefixlen'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_version
dedent|''
name|'def'
name|'get_ip_version'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'net'
op|'.'
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_injected_network_template
dedent|''
name|'def'
name|'get_injected_network_template'
op|'('
name|'network_info'
op|','
name|'use_ipv6'
op|'='
name|'CONF'
op|'.'
name|'use_ipv6'
op|','
nl|'\n'
name|'template'
op|'='
name|'CONF'
op|'.'
name|'injected_network_template'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a rendered network template for the given network_info.\n\n    :param network_info:\n        :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n    :param use_ipv6: If False, do not return IPv6 template information\n        even if an IPv6 subnet is present in network_info.\n    :param template: Path to the interfaces template file.\n    """'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'network_info'
name|'and'
name|'template'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'nets'
op|'='
op|'['
op|']'
newline|'\n'
name|'ifc_num'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'ipv6_is_available'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
newline|'\n'
comment|'# NOTE(bnemec): The template only supports a single subnet per'
nl|'\n'
comment|"# interface and I'm not sure how/if that can be fixed, so this"
nl|'\n'
comment|'# code only takes the first subnet of the appropriate type.'
nl|'\n'
name|'subnet_v4'
op|'='
op|'['
name|'i'
name|'for'
name|'i'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
name|'if'
name|'i'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'subnet_v6'
op|'='
op|'['
name|'i'
name|'for'
name|'i'
name|'in'
name|'network'
op|'['
string|"'subnets'"
op|']'
name|'if'
name|'i'
op|'['
string|"'version'"
op|']'
op|'=='
number|'6'
op|']'
newline|'\n'
name|'if'
name|'subnet_v6'
op|':'
newline|'\n'
indent|'            '
name|'subnet_v6'
op|'='
name|'subnet_v6'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ifc_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'not'
name|'network'
op|'.'
name|'get_meta'
op|'('
string|"'injected'"
op|')'
name|'or'
name|'not'
name|'subnet_v4'
op|'['
string|"'ips'"
op|']'
name|'or'
nl|'\n'
name|'subnet_v4'
op|'.'
name|'get_meta'
op|'('
string|"'dhcp_server'"
op|')'
name|'is'
name|'not'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'ip'
op|'='
name|'subnet_v4'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'address'
op|'='
name|'ip'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask'
op|'='
name|'model'
op|'.'
name|'get_netmask'
op|'('
name|'ip'
op|','
name|'subnet_v4'
op|')'
newline|'\n'
name|'gateway'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'subnet_v4'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'gateway'
op|'='
name|'subnet_v4'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'broadcast'
op|'='
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
newline|'\n'
name|'dns'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
op|'['
name|'i'
op|'['
string|"'address'"
op|']'
name|'for'
name|'i'
name|'in'
name|'subnet_v4'
op|'['
string|"'dns'"
op|']'
op|']'
op|')'
newline|'\n'
comment|"# NOTE(bnemec): I don't think this code would handle a pure IPv6"
nl|'\n'
comment|"# environment properly, but I don't have such an environment in"
nl|'\n'
comment|'# which to test/fix that.'
nl|'\n'
name|'address_v6'
op|'='
name|'None'
newline|'\n'
name|'gateway_v6'
op|'='
name|'None'
newline|'\n'
name|'netmask_v6'
op|'='
name|'None'
newline|'\n'
name|'have_ipv6'
op|'='
op|'('
name|'use_ipv6'
name|'and'
name|'subnet_v6'
op|')'
newline|'\n'
name|'if'
name|'have_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'subnet_v6'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'ipv6_is_available'
op|'='
name|'True'
newline|'\n'
name|'ip_v6'
op|'='
name|'subnet_v6'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'address_v6'
op|'='
name|'ip_v6'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask_v6'
op|'='
name|'model'
op|'.'
name|'get_netmask'
op|'('
name|'ip_v6'
op|','
name|'subnet_v6'
op|')'
newline|'\n'
name|'gateway_v6'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'gateway_v6'
op|'='
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'net_info'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'eth%d'"
op|'%'
name|'ifc_num'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'netmask'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'gateway'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'broadcast'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'dns'
op|','
nl|'\n'
string|"'address_v6'"
op|':'
name|'address_v6'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'gateway_v6'
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'netmask_v6'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'nets'
op|'.'
name|'append'
op|'('
name|'net_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'nets'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'build_template'
op|'('
name|'template'
op|','
name|'nets'
op|','
name|'ipv6_is_available'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_template
dedent|''
name|'def'
name|'build_template'
op|'('
name|'template'
op|','
name|'nets'
op|','
name|'ipv6_is_available'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_late_load_cheetah'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ifc_template'
op|'='
name|'open'
op|'('
name|'template'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'Template'
op|'('
name|'ifc_template'
op|','
nl|'\n'
name|'searchList'
op|'='
op|'['
op|'{'
string|"'interfaces'"
op|':'
name|'nets'
op|','
nl|'\n'
string|"'use_ipv6'"
op|':'
name|'ipv6_is_available'
op|'}'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
