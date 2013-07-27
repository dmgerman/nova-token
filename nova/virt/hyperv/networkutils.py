begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
string|'"""\nUtility class for network related operations.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'wmi'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkUtils
name|'class'
name|'NetworkUtils'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
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
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
name|'moniker'
op|'='
string|"'//./root/virtualization'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_external_vswitch
dedent|''
dedent|''
name|'def'
name|'get_external_vswitch'
op|'('
name|'self'
op|','
name|'vswitch_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vswitch_name'
op|':'
newline|'\n'
indent|'            '
name|'vswitches'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSwitch'
op|'('
name|'ElementName'
op|'='
name|'vswitch_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Find the vswitch that is connected to the first physical nic.'
nl|'\n'
indent|'            '
name|'ext_port'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ExternalEthernetPort'
op|'('
name|'IsBound'
op|'='
string|"'TRUE'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'port'
op|'='
name|'ext_port'
op|'.'
name|'associators'
op|'('
name|'wmi_result_class'
op|'='
string|"'Msvm_SwitchPort'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vswitches'
op|'='
name|'port'
op|'.'
name|'associators'
op|'('
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSwitch'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'len'
op|'('
name|'vswitches'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'\'vswitch "%s" not found\''
op|')'
nl|'\n'
op|'%'
name|'vswitch_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vswitches'
op|'['
number|'0'
op|']'
op|'.'
name|'path_'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_vswitch_port
dedent|''
name|'def'
name|'create_vswitch_port'
op|'('
name|'self'
op|','
name|'vswitch_path'
op|','
name|'port_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'switch_svc'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualSwitchManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'#Create a port on the vswitch.'
nl|'\n'
op|'('
name|'new_port'
op|','
name|'ret_val'
op|')'
op|'='
name|'switch_svc'
op|'.'
name|'CreateSwitchPort'
op|'('
nl|'\n'
name|'Name'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'FriendlyName'
op|'='
name|'port_name'
op|','
nl|'\n'
name|'ScopeOfResidence'
op|'='
string|'""'
op|','
nl|'\n'
name|'VirtualSwitch'
op|'='
name|'vswitch_path'
op|')'
newline|'\n'
name|'if'
name|'ret_val'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Failed to create vswitch port "'
nl|'\n'
string|'"%(port_name)s on switch "'
nl|'\n'
string|'"%(vswitch_path)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'port_name'"
op|':'
name|'port_name'
op|','
nl|'\n'
string|"'vswitch_path'"
op|':'
name|'vswitch_path'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'new_port'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
