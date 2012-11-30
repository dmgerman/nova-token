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
name|'nova'
name|'import'
name|'context'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'firewall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Dom0IptablesFirewallDriver
name|'class'
name|'Dom0IptablesFirewallDriver'
op|'('
name|'firewall'
op|'.'
name|'IptablesFirewallDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Dom0IptablesFirewallDriver class\n\n    This class provides an implementation for nova.virt.Firewall\n    using iptables. This class is meant to be used with the xenapi\n    backend and uses xenapi plugin to enforce iptables rules in dom0\n\n    """'
newline|'\n'
DECL|member|_plugin_execute
name|'def'
name|'_plugin_execute'
op|'('
name|'self'
op|','
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Prepare arguments for plugin call'
nl|'\n'
indent|'        '
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'.'
name|'update'
op|'('
name|'map'
op|'('
name|'lambda'
name|'x'
op|':'
op|'('
name|'x'
op|','
name|'str'
op|'('
name|'kwargs'
op|'['
name|'x'
op|']'
op|')'
op|')'
op|','
name|'kwargs'
op|')'
op|')'
newline|'\n'
name|'args'
op|'['
string|"'cmd_args'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_plugin'
op|'('
string|"'xenhost'"
op|','
string|"'iptables_config'"
op|','
name|'args'
op|')'
newline|'\n'
name|'json_ret'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
name|'return'
op|'('
name|'json_ret'
op|'['
string|"'out'"
op|']'
op|','
name|'json_ret'
op|'['
string|"'err'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|','
name|'xenapi_session'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
name|'super'
op|'('
name|'Dom0IptablesFirewallDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'xenapi_session'
newline|'\n'
comment|'# Create IpTablesManager with executor through plugin'
nl|'\n'
name|'self'
op|'.'
name|'iptables'
op|'='
name|'linux_net'
op|'.'
name|'IptablesManager'
op|'('
name|'self'
op|'.'
name|'_plugin_execute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'sg-fallback'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'sg-fallback'"
op|','
string|"'-j DROP'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'sg-fallback'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'sg-fallback'"
op|','
string|"'-j DROP'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_tcp_udp_rule
dedent|''
name|'def'
name|'_build_tcp_udp_rule'
op|'('
name|'self'
op|','
name|'rule'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|'=='
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
string|"'--dport'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'#  No multiport needed for XS!'
nl|'\n'
indent|'            '
name|'return'
op|'['
string|"'--dport'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
nl|'\n'
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_provider_rules
dedent|''
dedent|''
name|'def'
name|'_provider_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generate a list of rules from provider for IP4 & IP6.\n        Note: We could not use the common code from virt.firewall because\n        XS doesn\'t accept the \'-m multiport\' option"""'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ipv4_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'ipv6_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'rules'
op|'='
name|'self'
op|'.'
name|'_virtapi'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'rules'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Adding provider rule: %s'"
op|')'
op|','
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'version'
op|'='
name|'netutils'
op|'.'
name|'get_ip_version'
op|'('
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'fw_rules'
op|'='
name|'ipv4_rules'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'fw_rules'
op|'='
name|'ipv6_rules'
newline|'\n'
nl|'\n'
dedent|''
name|'protocol'
op|'='
name|'rule'
op|'['
string|"'protocol'"
op|']'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'6'
name|'and'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                '
name|'protocol'
op|'='
string|"'icmpv6'"
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
op|'['
string|"'-p'"
op|','
name|'protocol'
op|','
string|"'-s'"
op|','
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'protocol'
name|'in'
op|'['
string|"'udp'"
op|','
string|"'tcp'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|'=='
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
op|'['
string|"'--dport'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
op|'['
string|"'--dport'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
nl|'\n'
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                '
name|'icmp_type'
op|'='
name|'rule'
op|'['
string|"'from_port'"
op|']'
newline|'\n'
name|'icmp_code'
op|'='
name|'rule'
op|'['
string|"'to_port'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'icmp_type'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'icmp_type_arg'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'icmp_type_arg'
op|'='
string|"'%s'"
op|'%'
name|'icmp_type'
newline|'\n'
name|'if'
name|'not'
name|'icmp_code'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'icmp_type_arg'
op|'+='
string|"'/%s'"
op|'%'
name|'icmp_code'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'icmp_type_arg'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                        '
name|'args'
op|'+='
op|'['
string|"'-m'"
op|','
string|"'icmp'"
op|','
string|"'--icmp-type'"
op|','
nl|'\n'
name|'icmp_type_arg'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'                        '
name|'args'
op|'+='
op|'['
string|"'-m'"
op|','
string|"'icmp6'"
op|','
string|"'--icmpv6-type'"
op|','
nl|'\n'
name|'icmp_type_arg'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'args'
op|'+='
op|'['
string|"'-j DROP'"
op|']'
newline|'\n'
name|'fw_rules'
op|'+='
op|'['
string|"' '"
op|'.'
name|'join'
op|'('
name|'args'
op|')'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
