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
string|'"""Implements vlans, bridges, and iptables rules using linux utilities."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
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
name|'import'
name|'xenapi_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
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
string|'"nova.xenapi_net"'
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
comment|'# Open xenapi session'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'ENTERING ensure_vlan_bridge in xenapi net'"
op|')'
newline|'\n'
name|'url'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
newline|'\n'
name|'username'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
newline|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
newline|'\n'
name|'session'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
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
name|'session'
op|','
nl|'\n'
name|'bridge'
op|')'
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
indent|'        '
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
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.create'"
op|','
name|'network_rec'
op|')'
newline|'\n'
comment|'# 2 - find PIF for VLAN'
nl|'\n'
comment|'# Note using double quotes inside single quotes as xapi filter'
nl|'\n'
comment|'# only support tokens in double quotes'
nl|'\n'
name|'expr'
op|'='
string|'\'field "device" = "%s" and \\\n                field "VLAN" = "-1"\''
op|'%'
name|'FLAGS'
op|'.'
name|'vlan_interface'
newline|'\n'
name|'pifs'
op|'='
name|'session'
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
indent|'            '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Found no PIF for device %s'"
op|')'
op|'%'
name|'FLAGS'
op|'.'
name|'vlan_interface'
op|')'
newline|'\n'
comment|'# 3 - create vlan for network'
nl|'\n'
dedent|''
name|'for'
name|'pif_ref'
name|'in'
name|'pifs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VLAN.create'"
op|','
nl|'\n'
name|'pif_ref'
op|','
nl|'\n'
name|'str'
op|'('
name|'vlan_num'
op|')'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Check VLAN tag is appropriate'
nl|'\n'
indent|'        '
name|'network_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'network.get_record'"
op|','
name|'network_ref'
op|')'
newline|'\n'
comment|'# Retrieve PIFs from network'
nl|'\n'
name|'for'
name|'pif_ref'
name|'in'
name|'network_rec'
op|'['
string|"'PIFs'"
op|']'
op|':'
newline|'\n'
comment|'# Retrieve VLAN from PIF'
nl|'\n'
indent|'            '
name|'pif_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'PIF.get_record'"
op|','
name|'pif_ref'
op|')'
newline|'\n'
name|'pif_vlan'
op|'='
name|'int'
op|'('
name|'pif_rec'
op|'['
string|"'VLAN'"
op|']'
op|')'
newline|'\n'
comment|'# Raise an exception if VLAN != vlan_num'
nl|'\n'
name|'if'
name|'pif_vlan'
op|'!='
name|'vlan_num'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"PIF %(pif_rec[\'uuid\'])s for network "'
nl|'\n'
string|'"%(bridge)s has VLAN id %(pif_vlan)d. "'
nl|'\n'
string|'"Expected %(vlan_num)d"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
