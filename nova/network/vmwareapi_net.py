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
string|'"""Implements vlans for vmwareapi."""'
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
name|'import'
name|'network_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.network.vmwareapi_net"'
op|')'
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
DECL|function|ensure_vlan_bridge
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
string|'"""Create a vlan and bridge unless they already exist."""'
newline|'\n'
comment|'# Open vmwareapi session'
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
string|"'Must specify vmwareapi_host_ip, '"
nl|'\n'
string|"'vmwareapi_host_username '"
nl|'\n'
string|"'and vmwareapi_host_password to use '"
nl|'\n'
string|"'connection_type=vmwareapi'"
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
comment|'# Check if the vlan_interface physical network adapter exists on the host'
nl|'\n'
name|'if'
name|'not'
name|'network_utils'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NetworkAdapterNotFound'
op|'('
name|'adapter'
op|'='
name|'vlan_interface'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get the vSwitch associated with the Physical Adapter'
nl|'\n'
dedent|''
name|'vswitch_associated'
op|'='
name|'network_utils'
op|'.'
name|'get_vswitch_for_vlan_interface'
op|'('
nl|'\n'
name|'session'
op|','
name|'vlan_interface'
op|')'
newline|'\n'
name|'if'
name|'vswitch_associated'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SwicthNotFoundForNetworkAdapter'
op|'('
name|'adapter'
op|'='
name|'vlan_interface'
op|')'
newline|'\n'
comment|'# Check whether bridge already exists and retrieve the the ref of the'
nl|'\n'
comment|'# network whose name_label is "bridge"'
nl|'\n'
dedent|''
name|'network_ref'
op|'='
name|'network_utils'
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
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# Create a port group on the vSwitch associated with the vlan_interface'
nl|'\n'
comment|'# corresponding physical network adapter on the ESX host'
nl|'\n'
indent|'        '
name|'network_utils'
op|'.'
name|'create_port_group'
op|'('
name|'session'
op|','
name|'bridge'
op|','
name|'vswitch_associated'
op|','
nl|'\n'
name|'vlan_num'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Get the vlan id and vswitch corresponding to the port group'
nl|'\n'
indent|'        '
name|'pg_vlanid'
op|','
name|'pg_vswitch'
op|'='
name|'network_utils'
op|'.'
name|'get_vlanid_and_vswitch_for_portgroup'
op|'('
name|'session'
op|','
name|'bridge'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the vswitch associated is proper'
nl|'\n'
name|'if'
name|'pg_vswitch'
op|'!='
name|'vswitch_associated'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVLANPortGroup'
op|'('
name|'bridge'
op|'='
name|'bridge'
op|','
nl|'\n'
name|'expected'
op|'='
name|'vswitch_associated'
op|','
nl|'\n'
name|'actual'
op|'='
name|'pg_vswitch'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the vlan id is proper for the port group'
nl|'\n'
dedent|''
name|'if'
name|'pg_vlanid'
op|'!='
name|'vlan_num'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVLANTag'
op|'('
name|'bridge'
op|'='
name|'bridge'
op|','
name|'tag'
op|'='
name|'vlan_num'
op|','
nl|'\n'
name|'pgroup'
op|'='
name|'pg_vlanid'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
