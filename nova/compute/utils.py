begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""Compute-related Utilities and helpers."""'
newline|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
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
name|'network'
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
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
nl|'\n'
nl|'\n'
DECL|function|notify_usage_exists
name|'def'
name|'notify_usage_exists'
op|'('
name|'instance_ref'
op|','
name|'current_period'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Generates \'exists\' notification for an instance for usage auditing\n        purposes.\n\n        Generates usage for last completed period, unless \'current_period\'\n        is True."""'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
newline|'\n'
name|'begin'
op|','
name|'end'
op|'='
name|'utils'
op|'.'
name|'last_completed_audit_period'
op|'('
op|')'
newline|'\n'
name|'bw'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'current_period'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'end'
newline|'\n'
name|'audit_end'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'begin'
newline|'\n'
name|'audit_end'
op|'='
name|'end'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'info_cache'"
op|')'
name|'and'
nl|'\n'
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'cached_info'
op|'='
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'network_info'"
op|']'
newline|'\n'
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'cached_info'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'macs'
op|'='
op|'['
name|'vif'
op|'['
string|"'address'"
op|']'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|']'
newline|'\n'
name|'for'
name|'b'
name|'in'
name|'db'
op|'.'
name|'bw_usage_get_by_macs'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'macs'
op|','
nl|'\n'
name|'audit_start'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'label'
op|'='
string|"'net-name-not-found-%s'"
op|'%'
name|'b'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'vif'
op|'['
string|"'address'"
op|']'
op|'=='
name|'b'
op|'['
string|"'mac'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'label'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bw'
op|'['
name|'label'
op|']'
op|'='
name|'dict'
op|'('
name|'bw_in'
op|'='
name|'b'
op|'.'
name|'bw_in'
op|','
name|'bw_out'
op|'='
name|'b'
op|'.'
name|'bw_out'
op|')'
newline|'\n'
dedent|''
name|'usage_info'
op|'='
name|'utils'
op|'.'
name|'usage_from_instance'
op|'('
name|'instance_ref'
op|','
nl|'\n'
name|'audit_period_beginning'
op|'='
name|'str'
op|'('
name|'audit_start'
op|')'
op|','
nl|'\n'
name|'audit_period_ending'
op|'='
name|'str'
op|'('
name|'audit_end'
op|')'
op|','
nl|'\n'
name|'bandwidth'
op|'='
name|'bw'
op|')'
newline|'\n'
name|'notifier_api'
op|'.'
name|'notify'
op|'('
string|"'compute.%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'compute.instance.exists'"
op|','
nl|'\n'
name|'notifier_api'
op|'.'
name|'INFO'
op|','
nl|'\n'
name|'usage_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|legacy_network_info
dedent|''
name|'def'
name|'legacy_network_info'
op|'('
name|'network_model'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return the legacy network_info representation of the network_model\n    """'
newline|'\n'
DECL|function|get_ip
name|'def'
name|'get_ip'
op|'('
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'ip'
op|':'
newline|'\n'
indent|'            '
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
indent|'        '
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'            '
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
indent|'            '
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
DECL|function|get_meta
dedent|''
name|'def'
name|'get_meta'
op|'('
name|'model'
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
name|'if'
string|"'meta'"
name|'in'
name|'model'
name|'and'
name|'key'
name|'in'
name|'model'
op|'['
string|"'meta'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'model'
op|'['
string|"'meta'"
op|']'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'default'
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
indent|'        '
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
indent|'            '
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
name|'network_model'
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
indent|'            '
name|'if'
name|'subnet'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                '
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
indent|'                '
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
indent|'            '
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
indent|'            '
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
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'message'
op|'='
name|'_'
op|'('
string|"'v4 subnets are required for legacy nw_info'"
op|')'
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
nl|'\n'
name|'should_create_bridge'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
string|"'should_create_bridge'"
op|','
nl|'\n'
name|'False'
op|')'
newline|'\n'
name|'should_create_vlan'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
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
name|'get_meta'
op|'('
name|'subnet_v4'
op|','
string|"'dhcp_server'"
op|','
name|'gateway'
op|')'
newline|'\n'
name|'network_dict'
op|'='
name|'dict'
op|'('
name|'bridge'
op|'='
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'id'
op|'='
name|'network'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'cidr'
op|'='
name|'subnet_v4'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
name|'cidr_v6'
op|'='
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
name|'vlan'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
string|"'vlan'"
op|')'
op|','
nl|'\n'
name|'injected'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
string|"'injected'"
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'multi_host'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
string|"'multi_host'"
op|','
nl|'\n'
name|'False'
op|')'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
nl|'\n'
string|"'bridge_interface'"
op|')'
op|')'
newline|'\n'
comment|"# NOTE(tr3buchet): the 'ips' bit here is tricky, we support a single"
nl|'\n'
comment|'#                  subnet but we want all the IPs to be there'
nl|'\n'
comment|'#                  so we use the v4_subnets[0] and its IPs are first'
nl|'\n'
comment|'#                  so that eth0 will be from subnet_v4, the rest of the'
nl|'\n'
comment|'#                  IPs will be aliased eth0:1 etc and the gateways from'
nl|'\n'
comment|'#                  their subnets will not be used'
nl|'\n'
name|'info_dict'
op|'='
name|'dict'
op|'('
name|'label'
op|'='
name|'network'
op|'['
string|"'label'"
op|']'
op|','
nl|'\n'
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
op|','
nl|'\n'
name|'mac'
op|'='
name|'vif'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'vif_uuid'
op|'='
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'rxtx_cap'
op|'='
name|'get_meta'
op|'('
name|'network'
op|','
string|"'rxtx_cap'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'dns'
op|'='
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
name|'ips'
op|'='
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
name|'should_create_bridge'
op|'='
name|'should_create_bridge'
op|','
nl|'\n'
name|'should_create_vlan'
op|'='
name|'should_create_vlan'
op|','
nl|'\n'
name|'dhcp_server'
op|'='
name|'dhcp_server'
op|')'
newline|'\n'
name|'if'
name|'routes'
op|':'
newline|'\n'
indent|'            '
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
indent|'            '
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
indent|'            '
name|'if'
name|'subnet_v6'
op|'['
string|"'gateway'"
op|']'
op|':'
newline|'\n'
indent|'                '
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
endmarker|''
end_unit
