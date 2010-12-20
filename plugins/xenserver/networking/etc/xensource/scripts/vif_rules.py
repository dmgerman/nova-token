begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nThis script is used to configure iptables, ebtables, and arptables rules for\nXenServer instances.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
comment|'# This is written to Python 2.4, since that is what is available on XenServer'
nl|'\n'
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
name|'dom_id'
op|','
name|'command'
op|','
name|'only_this_vif'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'xsls'
op|'='
name|'execute'
op|'('
string|'"/usr/bin/xenstore-ls /local/domain/%s/vm-data/networking"'
op|'%'
name|'dom_id'
op|','
name|'True'
op|')'
newline|'\n'
name|'macs'
op|'='
op|'['
name|'line'
op|'.'
name|'split'
op|'('
string|'"="'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'line'
name|'in'
name|'xsls'
op|'.'
name|'splitlines'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'        '
name|'xsr'
op|'='
string|'"/usr/bin/xenstore-read /local/domain/%s/vm-data/networking/%s"'
newline|'\n'
name|'xsread'
op|'='
name|'execute'
op|'('
name|'xsr'
op|'%'
op|'('
name|'dom_id'
op|','
name|'mac'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'xsread'
op|')'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'data'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'data'
op|'['
string|'"label"'
op|']'
op|'=='
string|'"public"'
op|':'
newline|'\n'
indent|'                '
name|'vif'
op|'='
string|'"vif%s.0"'
op|'%'
name|'dom_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'vif'
op|'='
string|'"vif%s.1"'
op|'%'
name|'dom_id'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'only_this_vif'
name|'is'
name|'None'
op|')'
name|'or'
op|'('
name|'vif'
op|'=='
name|'only_this_vif'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'dict'
op|'('
name|'IP'
op|'='
name|'ip'
op|'['
string|"'ip'"
op|']'
op|','
name|'VIF'
op|'='
name|'vif'
op|','
name|'MAC'
op|'='
name|'data'
op|'['
string|"'mac'"
op|']'
op|')'
newline|'\n'
name|'apply_ebtables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
newline|'\n'
name|'apply_arptables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
newline|'\n'
name|'apply_iptables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'execute'
op|'('
name|'command'
op|','
name|'return_stdout'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'devnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'proc'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'command'
op|','
name|'shell'
op|'='
name|'True'
op|','
name|'close_fds'
op|'='
name|'True'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'stderr'
op|'='
name|'devnull'
op|')'
newline|'\n'
name|'if'
name|'return_stdout'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'proc'
op|'.'
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# A note about adding rules:'
nl|'\n'
comment|'#   Whenever we add any rule to iptables, arptables or ebtables we first'
nl|'\n'
comment|'#   delete the same rule to ensure the rule only exists once.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|apply_iptables_rules
dedent|''
dedent|''
name|'def'
name|'apply_iptables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'iptables'
op|'='
name|'lambda'
name|'rule'
op|':'
name|'execute'
op|'('
string|'"/sbin/iptables %s"'
op|'%'
name|'rule'
op|')'
newline|'\n'
nl|'\n'
name|'iptables'
op|'('
string|'"-D FORWARD -m physdev --physdev-in %(VIF)s -s %(IP)s \\\n              -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'command'
op|'=='
string|"'online'"
op|':'
newline|'\n'
indent|'        '
name|'iptables'
op|'('
string|'"-A FORWARD -m physdev --physdev-in %(VIF)s -s %(IP)s \\\n                  -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|apply_arptables_rules
dedent|''
dedent|''
name|'def'
name|'apply_arptables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'arptables'
op|'='
name|'lambda'
name|'rule'
op|':'
name|'execute'
op|'('
string|'"/sbin/arptables %s"'
op|'%'
name|'rule'
op|')'
newline|'\n'
nl|'\n'
name|'arptables'
op|'('
string|'"-D FORWARD --opcode Request --in-interface %(VIF)s \\\n               --source-ip %(IP)s --source-mac %(MAC)s -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'arptables'
op|'('
string|'"-D FORWARD --opcode Reply --in-interface %(VIF)s \\\n               --source-ip %(IP)s --source-mac %(MAC)s -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'command'
op|'=='
string|"'online'"
op|':'
newline|'\n'
indent|'        '
name|'arptables'
op|'('
string|'"-A FORWARD --opcode Request --in-interface %(VIF)s \\\n                  --source-ip %(IP)s --source-mac %(MAC)s -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'arptables'
op|'('
string|'"-A FORWARD --opcode Reply --in-interface %(VIF)s \\\n                  --source-ip %(IP)s --source-mac %(MAC)s -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|apply_ebtables_rules
dedent|''
dedent|''
name|'def'
name|'apply_ebtables_rules'
op|'('
name|'command'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ebtables'
op|'='
name|'lambda'
name|'rule'
op|':'
name|'execute'
op|'('
string|'"/sbin/ebtables %s"'
op|'%'
name|'rule'
op|')'
newline|'\n'
nl|'\n'
name|'ebtables'
op|'('
string|'"-D FORWARD -p 0806 -o %(VIF)s --arp-ip-dst %(IP)s -j ACCEPT"'
op|'%'
nl|'\n'
name|'params'
op|')'
newline|'\n'
name|'ebtables'
op|'('
string|'"-D FORWARD -p 0800 -o %(VIF)s --ip-dst %(IP)s -j ACCEPT"'
op|'%'
nl|'\n'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'command'
op|'=='
string|"'online'"
op|':'
newline|'\n'
indent|'        '
name|'ebtables'
op|'('
string|'"-A FORWARD -p 0806 -o %(VIF)s --arp-ip-dst %(IP)s \\\n                  -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'ebtables'
op|'('
string|'"-A FORWARD -p 0800 -o %(VIF)s --ip-dst %(IP)s \\\n                  -j ACCEPT"'
op|'%'
name|'params'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ebtables'
op|'('
string|'"-D FORWARD -s ! %(MAC)s -i %(VIF)s -j DROP"'
op|'%'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'command'
op|'=='
string|"'online'"
op|':'
newline|'\n'
indent|'        '
name|'ebtables'
op|'('
string|'"-I FORWARD 1 -s ! %(MAC)s -i %(VIF)s -j DROP"'
op|'%'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'<'
number|'3'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"usage: %s dom_id online|offline [vif]"'
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'dom_id'
op|','
name|'command'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
number|'3'
op|']'
newline|'\n'
DECL|variable|vif
name|'vif'
op|'='
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'=='
number|'4'
name|'and'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'3'
op|']'
name|'or'
name|'None'
newline|'\n'
name|'main'
op|'('
name|'dom_id'
op|','
name|'command'
op|','
name|'vif'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
