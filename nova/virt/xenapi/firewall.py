begin_unit
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'firewall'
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
string|'"""Dom0IptablesFirewallDriver class\n\n    This class provides an implementation for nova.virt.Firewall\n    using iptables. This class is meant to be used with the xenapi\n    backend and uses xenapi plugin to enforce iptables rules in dom0.\n    """'
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
op|'.'
name|'from_port'
op|'=='
name|'rule'
op|'.'
name|'to_port'
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
op|'.'
name|'from_port'
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
op|'.'
name|'from_port'
op|','
nl|'\n'
name|'rule'
op|'.'
name|'to_port'
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
