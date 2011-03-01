begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nImplements vlans for vmwareapi\n"""'
newline|'\n'
nl|'\n'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi_conn'
name|'import'
name|'VMWareAPISession'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
op|'.'
name|'network_utils'
name|'import'
name|'NetworkHelper'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.vmwareapi_net"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vlan_interface'"
op|','
string|"'vmnic0'"
op|','
nl|'\n'
string|"'Physical network adapter name in VMware ESX host for '"
nl|'\n'
string|"'vlan networking'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|metadata_forward
name|'def'
name|'metadata_forward'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bind_floating_ip
dedent|''
name|'def'
name|'bind_floating_ip'
op|'('
name|'floating_ip'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unbind_floating_ip
dedent|''
name|'def'
name|'unbind_floating_ip'
op|'('
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_forward
dedent|''
name|'def'
name|'ensure_vlan_forward'
op|'('
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_floating_forward
dedent|''
name|'def'
name|'ensure_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_floating_forward
dedent|''
name|'def'
name|'remove_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_bridge
dedent|''
name|'def'
name|'ensure_vlan_bridge'
op|'('
name|'vlan_num'
op|','
name|'bridge'
op|','
name|'net_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan and bridge unless they already exist"""'
newline|'\n'
comment|'#open vmwareapi session'
nl|'\n'
name|'host_ip'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_ip'
newline|'\n'
name|'host_username'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_username'
newline|'\n'
name|'host_password'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_host_password'
newline|'\n'
name|'if'
name|'not'
name|'host_ip'
name|'or'
name|'host_username'
name|'is'
name|'None'
name|'or'
name|'host_password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify vmwareapi_host_ip,"'
nl|'\n'
string|'"vmwareapi_host_username "'
nl|'\n'
string|'"and vmwareapi_host_password to use"'
nl|'\n'
string|'"connection_type=vmwareapi"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'session'
op|'='
name|'VMWareAPISession'
op|'('
name|'host_ip'
op|','
name|'host_username'
op|','
name|'host_password'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'vmwareapi_api_retry_count'
op|')'
newline|'\n'
name|'vlan_interface'
op|'='
name|'FLAGS'
op|'.'
name|'vlan_interface'
newline|'\n'
comment|'#check whether bridge already exists'
nl|'\n'
comment|'#retrieve network whose name_label is "bridge"'
nl|'\n'
name|'network_ref'
op|'='
name|'NetworkHelper'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
name|'bridge'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|'=='
name|'None'
op|':'
newline|'\n'
comment|'#Create a port group on the vSwitch associated with the vlan_interface'
nl|'\n'
comment|'#corresponding physical network adapter on the ESX host'
nl|'\n'
indent|'        '
name|'vswitches'
op|'='
name|'NetworkHelper'
op|'.'
name|'get_vswitches_for_vlan_interface'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'vswitches'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"There is no virtual switch connected "'
nl|'\n'
string|'"to the physical network adapter with name %s"'
op|')'
op|'%'
nl|'\n'
name|'vlan_interface'
op|')'
newline|'\n'
comment|'#Assuming physical network interface is associated with only one'
nl|'\n'
comment|'#virtual switch'
nl|'\n'
dedent|''
name|'NetworkHelper'
op|'.'
name|'create_port_group'
op|'('
name|'session'
op|','
name|'bridge'
op|','
name|'vswitches'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'vlan_num'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'#check VLAN tag is appropriate'
nl|'\n'
indent|'        '
name|'is_vlan_proper'
op|','
name|'ret_vlan_id'
op|'='
name|'NetworkHelper'
op|'.'
name|'check_if_vlan_id_is_proper'
op|'('
nl|'\n'
name|'session'
op|','
name|'bridge'
op|','
name|'vlan_num'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'is_vlan_proper'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"VLAN tag not appropriate for the port group "'
nl|'\n'
string|'"%(bridge)s. Expected VLAN tag is %(vlan_num)s, "'
nl|'\n'
string|'"but the one associated with the port group is"'
nl|'\n'
string|'" %(ret_vlan_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan
dedent|''
dedent|''
dedent|''
name|'def'
name|'ensure_vlan'
op|'('
name|'vlan_num'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_bridge
dedent|''
name|'def'
name|'ensure_bridge'
op|'('
name|'bridge'
op|','
name|'interface'
op|','
name|'net_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dhcp_hosts
dedent|''
name|'def'
name|'get_dhcp_hosts'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_dhcp
dedent|''
name|'def'
name|'update_dhcp'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_ra
dedent|''
name|'def'
name|'update_ra'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
