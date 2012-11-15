begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Bare-metal test utils."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
name|'as'
name|'bm_models'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|new_bm_node
name|'def'
name|'new_bm_node'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'h'
op|'='
name|'bm_models'
op|'.'
name|'BareMetalNode'
op|'('
op|')'
newline|'\n'
name|'h'
op|'.'
name|'id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'service_host'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'service_host'"
op|','
name|'None'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'instance_uuid'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'instance_uuid'"
op|','
name|'None'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'cpus'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'cpus'"
op|','
number|'1'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'memory_mb'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'memory_mb'"
op|','
number|'1024'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'local_gb'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'local_gb'"
op|','
number|'64'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'pm_address'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'pm_address'"
op|','
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'h'
op|'.'
name|'pm_user'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'pm_user'"
op|','
string|"'ipmi_user'"
op|')'
newline|'\n'
name|'h'
op|'.'
name|'pm_password'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'pm_password'"
op|','
string|"'ipmi_password'"
op|')'
newline|'\n'
name|'h'
op|'.'
name|'prov_mac_address'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'prov_mac_address'"
op|','
string|"'12:34:56:78:90:ab'"
op|')'
newline|'\n'
name|'h'
op|'.'
name|'registration_status'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'registration_status'"
op|','
string|"'done'"
op|')'
newline|'\n'
name|'h'
op|'.'
name|'task_state'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'task_state'"
op|','
name|'None'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'prov_vlan_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'prov_vlan_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'h'
op|'.'
name|'terminal_port'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'terminal_port'"
op|','
number|'8000'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"unknown field: %s"'
nl|'\n'
op|'%'
string|"','"
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'h'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|new_bm_pxe_ip
dedent|''
name|'def'
name|'new_bm_pxe_ip'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'x'
op|'='
name|'bm_models'
op|'.'
name|'BareMetalPxeIp'
op|'('
op|')'
newline|'\n'
name|'x'
op|'.'
name|'id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'address'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'address'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'server_address'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'server_address'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'bm_node_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'bm_node_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"unknown field: %s"'
nl|'\n'
op|'%'
string|"','"
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'x'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|new_bm_interface
dedent|''
name|'def'
name|'new_bm_interface'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'x'
op|'='
name|'bm_models'
op|'.'
name|'BareMetalInterface'
op|'('
op|')'
newline|'\n'
name|'x'
op|'.'
name|'id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'bm_node_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'bm_node_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'address'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'address'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'datapath_id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'datapath_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'port_no'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'port_no'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'vif_uuid'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'vif_uuid'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"unknown field: %s"'
nl|'\n'
op|'%'
string|"','"
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'x'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|new_bm_deployment
dedent|''
name|'def'
name|'new_bm_deployment'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'x'
op|'='
name|'bm_models'
op|'.'
name|'BareMetalDeployment'
op|'('
op|')'
newline|'\n'
name|'x'
op|'.'
name|'id'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'key'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'key'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'image_path'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'image_path'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'pxe_config_path'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'pxe_config_path'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'root_mb'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'root_mb'"
op|','
name|'None'
op|')'
newline|'\n'
name|'x'
op|'.'
name|'swap_mb'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'swap_mb'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"unknown field: %s"'
nl|'\n'
op|'%'
string|"','"
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'x'
newline|'\n'
dedent|''
endmarker|''
end_unit
