begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Citrix Systems, Inc.'
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
string|'"""\nThis script is used to configure base openvswitch flows for XenServer hosts.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'novalib'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
name|'command'
op|','
name|'phys_dev_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ovs_ofctl'
op|'='
name|'lambda'
op|'*'
name|'rule'
op|':'
name|'novalib'
op|'.'
name|'execute'
op|'('
string|"'/usr/bin/ovs-ofctl'"
op|','
op|'*'
name|'rule'
op|')'
newline|'\n'
nl|'\n'
name|'bridge_name'
op|'='
name|'novalib'
op|'.'
name|'execute_get_output'
op|'('
string|"'/usr/bin/ovs-vsctl'"
op|','
nl|'\n'
string|"'iface-to-br'"
op|','
name|'phys_dev_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# always clear all flows first'
nl|'\n'
name|'ovs_ofctl'
op|'('
string|"'del-flows'"
op|','
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'command'
name|'in'
op|'('
string|"'online'"
op|','
string|"'reset'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pnic_ofport'
op|'='
name|'novalib'
op|'.'
name|'execute_get_output'
op|'('
string|"'/usr/bin/ovs-vsctl'"
op|','
string|"'get'"
op|','
nl|'\n'
string|"'Interface'"
op|','
name|'phys_dev_name'
op|','
string|"'ofport'"
op|')'
newline|'\n'
nl|'\n'
comment|'# these flows are lower priority than all VM-specific flows.'
nl|'\n'
nl|'\n'
comment|'# allow all traffic from the physical NIC, as it is trusted (i.e.,'
nl|'\n'
comment|'# from a filtered vif, or from the physical infrastructure)'
nl|'\n'
name|'ovs_ofctl'
op|'('
string|"'add-flow'"
op|','
name|'bridge_name'
op|','
nl|'\n'
string|'"priority=2,in_port=%s,actions=normal"'
op|'%'
name|'pnic_ofport'
op|')'
newline|'\n'
nl|'\n'
comment|'# Allow traffic from dom0 if there is a management interface'
nl|'\n'
comment|'# present (its IP address is on the bridge itself)'
nl|'\n'
name|'bridge_addr'
op|'='
name|'novalib'
op|'.'
name|'execute_get_output'
op|'('
string|"'/sbin/ip'"
op|','
string|"'-o'"
op|','
string|"'-f'"
op|','
string|"'inet'"
op|','
string|"'addr'"
op|','
nl|'\n'
string|"'show'"
op|','
name|'bridge_name'
op|')'
newline|'\n'
name|'if'
name|'bridge_addr'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'ovs_ofctl'
op|'('
string|"'add-flow'"
op|','
name|'bridge_name'
op|','
nl|'\n'
string|'"priority=2,in_port=LOCAL,actions=normal"'
op|')'
newline|'\n'
nl|'\n'
comment|'# default drop'
nl|'\n'
dedent|''
name|'ovs_ofctl'
op|'('
string|"'add-flow'"
op|','
name|'bridge_name'
op|','
string|"'priority=1,actions=drop'"
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
op|'!='
number|'3'
name|'or'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
name|'not'
name|'in'
op|'('
string|"'online'"
op|','
string|"'offline'"
op|','
string|"'reset'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'sys'
op|'.'
name|'argv'
newline|'\n'
DECL|variable|script_name
name|'script_name'
op|'='
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
name|'print'
string|'"This script configures base ovs flows."'
newline|'\n'
name|'print'
string|'"usage: %s [online|offline|reset] phys-dev-name"'
op|'%'
name|'script_name'
newline|'\n'
name|'print'
string|'"   ex: %s online eth0"'
op|'%'
name|'script_name'
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
name|'command'
op|','
name|'phys_dev_name'
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
name|'main'
op|'('
name|'command'
op|','
name|'phys_dev_name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
