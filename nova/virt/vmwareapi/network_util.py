begin_unit
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nUtility functions for ESX Networking.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
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
DECL|function|get_network_with_the_name
name|'def'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
name|'network_name'
op|'='
string|'"vmnet0"'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets reference to the network whose name is passed as the\n    argument.\n    """'
newline|'\n'
name|'host'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'cluster'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'vm_networks_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'cluster'
op|','
nl|'\n'
string|'"ClusterComputeResource"'
op|','
nl|'\n'
string|'"network"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'vm_networks_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'host'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
string|'"network"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Meaning there are no networks on the host. suds responds with a ""'
nl|'\n'
comment|'# in the parent property field rather than a [] in the'
nl|'\n'
comment|'# ManagedObjectReference property field of the parent'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'vm_networks_ret'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"No networks configured on host!"'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'vm_networks'
op|'='
name|'vm_networks_ret'
op|'.'
name|'ManagedObjectReference'
newline|'\n'
name|'network_obj'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Configured networks: %s"'
op|','
name|'vm_networks'
op|')'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'vm_networks'
op|':'
newline|'\n'
comment|'# Get network properties'
nl|'\n'
indent|'        '
name|'if'
name|'network'
op|'.'
name|'_type'
op|'=='
string|"'DistributedVirtualPortgroup'"
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'network'
op|','
nl|'\n'
string|'"DistributedVirtualPortgroup"'
op|','
string|'"config"'
op|')'
newline|'\n'
comment|'# NOTE(asomya): This only works on ESXi if the port binding is'
nl|'\n'
comment|'# set to ephemeral'
nl|'\n'
comment|'# For a VLAN the network name will be the UUID. For a VXLAN'
nl|'\n'
comment|'# network this will have a VXLAN prefix and then the network name.'
nl|'\n'
name|'if'
name|'network_name'
name|'in'
name|'props'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'network_obj'
op|'['
string|"'type'"
op|']'
op|'='
string|"'DistributedVirtualPortgroup'"
newline|'\n'
name|'network_obj'
op|'['
string|"'dvpg'"
op|']'
op|'='
name|'props'
op|'.'
name|'key'
newline|'\n'
name|'dvs_props'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
nl|'\n'
name|'props'
op|'.'
name|'distributedVirtualSwitch'
op|','
nl|'\n'
string|'"VmwareDistributedVirtualSwitch"'
op|','
string|'"uuid"'
op|')'
newline|'\n'
name|'network_obj'
op|'['
string|"'dvsw'"
op|']'
op|'='
name|'dvs_props'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'network'
op|','
nl|'\n'
string|'"Network"'
op|','
string|'"summary.name"'
op|')'
newline|'\n'
name|'if'
name|'props'
op|'=='
name|'network_name'
op|':'
newline|'\n'
indent|'                '
name|'network_obj'
op|'['
string|"'type'"
op|']'
op|'='
string|"'Network'"
newline|'\n'
name|'network_obj'
op|'['
string|"'name'"
op|']'
op|'='
name|'network_name'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
op|'('
name|'len'
op|'('
name|'network_obj'
op|')'
op|'>'
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network_obj'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Network %s not found on host!"'
op|','
name|'network_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vswitch_for_vlan_interface
dedent|''
name|'def'
name|'get_vswitch_for_vlan_interface'
op|'('
name|'session'
op|','
name|'vlan_interface'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the vswitch associated with the physical network adapter\n    with the name supplied.\n    """'
newline|'\n'
comment|'# Get the list of vSwicthes on the Host System'
nl|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'vswitches_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'host_mor'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
string|'"config.network.vswitch"'
op|')'
newline|'\n'
comment|"# Meaning there are no vSwitches on the host. Shouldn't be the case,"
nl|'\n'
comment|'# but just doing code check'
nl|'\n'
name|'if'
name|'not'
name|'vswitches_ret'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'vswitches'
op|'='
name|'vswitches_ret'
op|'.'
name|'HostVirtualSwitch'
newline|'\n'
comment|'# Get the vSwitch associated with the network adapter'
nl|'\n'
name|'for'
name|'elem'
name|'in'
name|'vswitches'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'nic_elem'
name|'in'
name|'elem'
op|'.'
name|'pnic'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'str'
op|'('
name|'nic_elem'
op|')'
op|'.'
name|'split'
op|'('
string|"'-'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'find'
op|'('
name|'vlan_interface'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'elem'
op|'.'
name|'name'
newline|'\n'
comment|'# Catching Attribute error as a vSwitch may not be associated with a'
nl|'\n'
comment|'# physical NIC.'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_if_vlan_interface_exists
dedent|''
dedent|''
dedent|''
name|'def'
name|'check_if_vlan_interface_exists'
op|'('
name|'session'
op|','
name|'vlan_interface'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks if the vlan_interface exists on the esx host."""'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'physical_nics_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'host_mor'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
string|'"config.network.pnic"'
op|')'
newline|'\n'
comment|'# Meaning there are no physical nics on the host'
nl|'\n'
name|'if'
name|'not'
name|'physical_nics_ret'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'physical_nics'
op|'='
name|'physical_nics_ret'
op|'.'
name|'PhysicalNic'
newline|'\n'
name|'for'
name|'pnic'
name|'in'
name|'physical_nics'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vlan_interface'
op|'=='
name|'pnic'
op|'.'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vlanid_and_vswitch_for_portgroup
dedent|''
name|'def'
name|'get_vlanid_and_vswitch_for_portgroup'
op|'('
name|'session'
op|','
name|'pg_name'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the vlan id and vswicth associated with the port group."""'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'port_grps_on_host_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'host_mor'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
string|'"config.network.portgroup"'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'port_grps_on_host_ret'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"ESX SOAP server returned an empty port group "'
nl|'\n'
string|'"for the host system in its response"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'port_grps_on_host'
op|'='
name|'port_grps_on_host_ret'
op|'.'
name|'HostPortGroup'
newline|'\n'
name|'for'
name|'p_gp'
name|'in'
name|'port_grps_on_host'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'p_gp'
op|'.'
name|'spec'
op|'.'
name|'name'
op|'=='
name|'pg_name'
op|':'
newline|'\n'
indent|'            '
name|'p_grp_vswitch_name'
op|'='
name|'p_gp'
op|'.'
name|'vswitch'
op|'.'
name|'split'
op|'('
string|'"-"'
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'return'
name|'p_gp'
op|'.'
name|'spec'
op|'.'
name|'vlanId'
op|','
name|'p_grp_vswitch_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_port_group
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_port_group'
op|'('
name|'session'
op|','
name|'pg_name'
op|','
name|'vswitch_name'
op|','
name|'vlan_id'
op|'='
number|'0'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a port group on the host system with the vlan tags\n    supplied. VLAN id 0 means no vlan id association.\n    """'
newline|'\n'
name|'client_factory'
op|'='
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'add_prt_grp_spec'
op|'='
name|'vm_util'
op|'.'
name|'get_add_vswitch_port_group_spec'
op|'('
nl|'\n'
name|'client_factory'
op|','
nl|'\n'
name|'vswitch_name'
op|','
nl|'\n'
name|'pg_name'
op|','
nl|'\n'
name|'vlan_id'
op|')'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'network_system_mor'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'host_mor'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
string|'"configManager.networkSystem"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating Port Group with name %s on "'
nl|'\n'
string|'"the ESX host"'
op|','
name|'pg_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"AddPortGroup"'
op|','
name|'network_system_mor'
op|','
nl|'\n'
name|'portgrp'
op|'='
name|'add_prt_grp_spec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'AlreadyExistsException'
op|':'
newline|'\n'
comment|'# There can be a race condition when two instances try'
nl|'\n'
comment|'# adding port groups at the same time. One succeeds, then'
nl|'\n'
comment|'# the other one will get an exception. Since we are'
nl|'\n'
comment|'# concerned with the port group being created, which is done'
nl|'\n'
comment|'# by the other call, we can ignore the exception.'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Port Group %s already exists."'
op|','
name|'pg_name'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Created Port Group with name %s on "'
nl|'\n'
string|'"the ESX host"'
op|','
name|'pg_name'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
