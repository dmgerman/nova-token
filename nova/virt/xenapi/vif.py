begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\n'
comment|'# Copyright (C) 2011 Nicira, Inc'
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
string|'"""VIF drivers for XenAPI."""'
newline|'\n'
nl|'\n'
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
op|'.'
name|'virt'
op|'.'
name|'vif'
name|'import'
name|'VIFDriver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'network_utils'
name|'import'
name|'NetworkHelper'
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
string|"'xenapi_ovs_integration_bridge'"
op|','
string|"'xapi1'"
op|','
nl|'\n'
string|"'Name of Integration Bridge used by Open vSwitch'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi.vif"'
op|')'
newline|'\n'
nl|'\n'
DECL|class|XenAPIBridgeDriver
name|'class'
name|'XenAPIBridgeDriver'
op|'('
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Combined VIF and Bridge class for XenAPI."""'
newline|'\n'
nl|'\n'
DECL|member|get_vif_rec
name|'def'
name|'get_vif_rec'
op|'('
name|'self'
op|','
name|'xenapi_session'
op|','
name|'vm_ref'
op|','
name|'instance'
op|','
name|'device'
op|','
name|'network'
op|','
nl|'\n'
name|'network_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"bridge = \'%s\'"'
op|'%'
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'NetworkHelper'
op|'.'
name|'find_network_with_bridge'
op|'('
name|'xenapi_session'
op|','
nl|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
name|'rxtx_cap'
op|'='
name|'network_mapping'
op|'.'
name|'pop'
op|'('
string|"'rxtx_cap'"
op|')'
newline|'\n'
name|'vif_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'device'"
op|']'
op|'='
name|'str'
op|'('
name|'device'
op|')'
newline|'\n'
name|'vif_rec'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MAC'"
op|']'
op|'='
name|'network_mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MTU'"
op|']'
op|'='
string|"'1500'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|'"ratelimit"'
name|'if'
name|'rxtx_cap'
name|'else'
string|"''"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
string|'"kbps"'
op|':'
name|'str'
op|'('
name|'rxtx_cap'
op|'*'
number|'1024'
op|')'
op|'}'
name|'if'
name|'rxtx_cap'
name|'else'
op|'{'
op|'}'
newline|'\n'
name|'return'
name|'vif_rec'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'xenapi_session'
op|','
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that the bridge exists, if using VLANs"""'
newline|'\n'
nl|'\n'
name|'vlan_num'
op|'='
name|'network'
op|'['
string|"'vlan'"
op|']'
newline|'\n'
name|'if'
name|'vlan_num'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
comment|'# no plugging done for non-VLAN networks'
newline|'\n'
name|'bridge'
op|'='
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
dedent|''
name|'bridge_interface'
op|'='
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
nl|'\n'
name|'print'
string|'"in plug with bridge = %s and bridge_interface = %s"'
op|'%'
op|'('
name|'bridge'
op|','
name|'bridge_interface'
op|')'
newline|'\n'
comment|'# Check whether bridge already exists'
nl|'\n'
comment|'# Retrieve network whose name_label is "bridge"'
nl|'\n'
name|'network_ref'
op|'='
name|'network_utils'
op|'.'
name|'NetworkHelper'
op|'.'
name|'find_network_with_name_label'
op|'('
nl|'\n'
name|'xenapi_session'
op|','
nl|'\n'
name|'bridge'
op|')'
newline|'\n'
name|'print'
string|'"got network_ref = %s"'
op|'%'
name|'network_ref'
newline|'\n'
name|'if'
name|'network_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# If bridge does not exists'
nl|'\n'
comment|'# 1 - create network'
nl|'\n'
indent|'        \t'
name|'description'
op|'='
string|"'network for nova bridge %s'"
op|'%'
name|'bridge'
newline|'\n'
name|'network_rec'
op|'='
op|'{'
string|"'name_label'"
op|':'
name|'bridge'
op|','
nl|'\n'
string|"'name_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'xenapi_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.create'"
op|','
name|'network_rec'
op|')'
newline|'\n'
comment|'# 2 - find PIF for VLAN NOTE(salvatore-orlando): using double'
nl|'\n'
comment|'# quotes inside single quotes as xapi filter only support'
nl|'\n'
comment|'# tokens in double quotes'
nl|'\n'
name|'expr'
op|'='
string|'\'field "device" = "%s" and \\\n                field "VLAN" = "-1"\''
op|'%'
name|'bridge_interface'
newline|'\n'
name|'pifs'
op|'='
name|'xenapi_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'PIF.get_all_records_where'"
op|','
name|'expr'
op|')'
newline|'\n'
name|'pif_ref'
op|'='
name|'None'
newline|'\n'
comment|'# Multiple PIF are ok: we are dealing with a pool'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'pifs'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            \t\t'
name|'raise'
name|'Exception'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Found no PIF for device %s'"
op|')'
op|'%'
name|'bridge_interface'
op|')'
newline|'\n'
comment|'# 3 - create vlan for network'
nl|'\n'
end_unit
