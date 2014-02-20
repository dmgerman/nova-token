begin_unit
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
string|'"""VIF drivers for VMware."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'network_util'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|vmwareapi_vif_opts
name|'vmwareapi_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vlan_interface'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'vmnic0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Physical ethernet adapter name for vlan networking'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'vmwareapi_vif_opts'
op|','
string|"'vmware'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_associated_vswitch_for_interface
name|'def'
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
name|'interface'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# Check if the physical network adapter exists on the host.'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'network_util'
op|'.'
name|'check_if_vlan_interface_exists'
op|'('
name|'session'
op|','
nl|'\n'
name|'interface'
op|','
name|'cluster'
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
name|'interface'
op|')'
newline|'\n'
comment|'# Get the vSwitch associated with the Physical Adapter'
nl|'\n'
dedent|''
name|'vswitch_associated'
op|'='
name|'network_util'
op|'.'
name|'get_vswitch_for_vlan_interface'
op|'('
nl|'\n'
name|'session'
op|','
name|'interface'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'vswitch_associated'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SwitchNotFoundForNetworkAdapter'
op|'('
name|'adapter'
op|'='
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vswitch_associated'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_bridge
dedent|''
name|'def'
name|'ensure_vlan_bridge'
op|'('
name|'session'
op|','
name|'vif'
op|','
name|'cluster'
op|'='
name|'None'
op|','
name|'create_vlan'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan and bridge unless they already exist."""'
newline|'\n'
name|'vlan_num'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get_meta'
op|'('
string|"'vlan'"
op|')'
newline|'\n'
name|'bridge'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'vlan_interface'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'vlan_interface'
newline|'\n'
nl|'\n'
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
name|'bridge'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
name|'and'
name|'network_ref'
op|'['
string|"'type'"
op|']'
op|'=='
string|"'DistributedVirtualPortgroup'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'network_ref'
op|':'
newline|'\n'
comment|'# Create a port group on the vSwitch associated with the'
nl|'\n'
comment|'# vlan_interface corresponding physical network adapter on the ESX'
nl|'\n'
comment|'# host.'
nl|'\n'
indent|'        '
name|'vswitch_associated'
op|'='
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'network_util'
op|'.'
name|'create_port_group'
op|'('
name|'session'
op|','
name|'bridge'
op|','
nl|'\n'
name|'vswitch_associated'
op|','
nl|'\n'
name|'vlan_num'
name|'if'
name|'create_vlan'
name|'else'
number|'0'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
name|'session'
op|','
nl|'\n'
name|'bridge'
op|','
nl|'\n'
name|'cluster'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'create_vlan'
op|':'
newline|'\n'
comment|'# Get the vSwitch associated with the Physical Adapter'
nl|'\n'
indent|'        '
name|'vswitch_associated'
op|'='
name|'_get_associated_vswitch_for_interface'
op|'('
name|'session'
op|','
nl|'\n'
name|'vlan_interface'
op|','
name|'cluster'
op|')'
newline|'\n'
comment|'# Get the vlan id and vswitch corresponding to the port group'
nl|'\n'
name|'_get_pg_info'
op|'='
name|'network_util'
op|'.'
name|'get_vlanid_and_vswitch_for_portgroup'
newline|'\n'
name|'pg_vlanid'
op|','
name|'pg_vswitch'
op|'='
name|'_get_pg_info'
op|'('
name|'session'
op|','
name|'bridge'
op|','
name|'cluster'
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
nl|'\n'
name|'bridge'
op|'='
name|'bridge'
op|','
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
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_valid_opaque_network_id
dedent|''
name|'def'
name|'_is_valid_opaque_network_id'
op|'('
name|'opaque_id'
op|','
name|'bridge_id'
op|','
name|'integration_bridge'
op|','
nl|'\n'
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
name|'opaque_id'
op|'=='
name|'bridge_id'
name|'or'
nl|'\n'
op|'('
name|'num_networks'
op|'=='
number|'1'
name|'and'
nl|'\n'
name|'opaque_id'
op|'=='
name|'integration_bridge'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_network_ref_from_opaque
dedent|''
name|'def'
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
name|'integration_bridge'
op|','
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'num_networks'
op|'='
name|'len'
op|'('
name|'opaque_networks'
op|')'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'opaque_networks'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'_is_valid_opaque_network_id'
op|'('
name|'network'
op|'['
string|"'opaqueNetworkId'"
op|']'
op|','
name|'bridge'
op|','
nl|'\n'
name|'integration_bridge'
op|','
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'type'"
op|':'
string|"'OpaqueNetwork'"
op|','
nl|'\n'
string|"'network-id'"
op|':'
name|'network'
op|'['
string|"'opaqueNetworkId'"
op|']'
op|','
nl|'\n'
string|"'network-name'"
op|':'
name|'network'
op|'['
string|"'opaqueNetworkName'"
op|']'
op|','
nl|'\n'
string|"'network-type'"
op|':'
name|'network'
op|'['
string|"'opaqueNetworkType'"
op|']'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"No valid network found in %(opaque)s, from %(bridge)s "'
nl|'\n'
string|'"or %(integration_bridge)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'opaque'"
op|':'
name|'opaque_networks'
op|','
string|"'bridge'"
op|':'
name|'bridge'
op|','
nl|'\n'
string|"'integration_bridge'"
op|':'
name|'integration_bridge'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_neutron_network
dedent|''
name|'def'
name|'get_neutron_network'
op|'('
name|'session'
op|','
name|'network_name'
op|','
name|'cluster'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'opaque'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
name|'host'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
nl|'\n'
string|'"config.network.opaqueNetwork"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'InvalidPropertyException'
op|':'
newline|'\n'
indent|'        '
name|'opaque'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'opaque'
op|':'
newline|'\n'
indent|'        '
name|'bridge'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'opaque_networks'
op|'='
name|'opaque'
op|'.'
name|'HostOpaqueNetworkInfo'
newline|'\n'
name|'network_ref'
op|'='
name|'_get_network_ref_from_opaque'
op|'('
name|'opaque_networks'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
op|','
name|'bridge'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'bridge'
op|'='
name|'network_name'
newline|'\n'
name|'network_ref'
op|'='
name|'network_util'
op|'.'
name|'get_network_with_the_name'
op|'('
nl|'\n'
name|'session'
op|','
name|'network_name'
op|','
name|'cluster'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'network_ref'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFoundForBridge'
op|'('
name|'bridge'
op|'='
name|'bridge'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_network_ref
dedent|''
name|'def'
name|'get_network_ref'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'vif'
op|','
name|'is_neutron'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'is_neutron'
op|':'
newline|'\n'
indent|'        '
name|'network_name'
op|'='
op|'('
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'bridge'"
op|']'
name|'or'
nl|'\n'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'integration_bridge'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'get_neutron_network'
op|'('
name|'session'
op|','
name|'network_name'
op|','
name|'cluster'
op|','
name|'vif'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'create_vlan'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'.'
name|'get_meta'
op|'('
string|"'should_create_vlan'"
op|','
name|'False'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'ensure_vlan_bridge'
op|'('
name|'session'
op|','
name|'vif'
op|','
name|'cluster'
op|'='
name|'cluster'
op|','
nl|'\n'
name|'create_vlan'
op|'='
name|'create_vlan'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_ref'
newline|'\n'
dedent|''
endmarker|''
end_unit
