begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nHelper methods for operations related to the management of network\nrecords and their attributes like bridges, PIFs, QoS, as well as\ntheir lookup functions.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'xenapi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkHelper
name|'class'
name|'NetworkHelper'
op|'('
name|'xenapi'
op|'.'
name|'HelperBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The class that wraps the helper methods together.\n    """'
newline|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_network_with_name_label
name|'def'
name|'find_network_with_name_label'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.get_by_name_label'"
op|','
name|'name_label'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'networks'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'networks'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'networks'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Found non-unique network'"
nl|'\n'
string|"' for name_label %s'"
op|')'
op|'%'
name|'name_label'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_network_with_bridge
name|'def'
name|'find_network_with_bridge'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the network on which the bridge is attached, if found.\n        The bridge is defined in the nova db and can be found either in the\n        \'bridge\' or \'name_label\' fields of the XenAPI network record.\n        """'
newline|'\n'
name|'expr'
op|'='
op|'('
string|'\'field "name__label" = "%s" or field "bridge" = "%s"\''
op|'%'
nl|'\n'
op|'('
name|'bridge'
op|','
name|'bridge'
op|')'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.get_all_records_where'"
op|','
name|'expr'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'networks'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'networks'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'networks'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Found non-unique network'"
nl|'\n'
string|"' for bridge %s'"
op|')'
op|'%'
name|'bridge'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Found no network for bridge %s'"
op|')'
op|'%'
name|'bridge'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
