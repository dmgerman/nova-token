begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2011 Midokura KK'
nl|'\n'
comment|'# Copyright (C) 2011 Nicira, Inc'
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
string|'"""VIF drivers for libvirt."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'vif'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
name|'as'
name|'vconfig'
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
DECL|variable|libvirt_vif_opts
name|'libvirt_vif_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'libvirt_ovs_bridge'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'br-int'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of Integration Bridge used by Open vSwitch'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'libvirt_use_virtio_for_bridges'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use virtio for bridge interfaces'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'libvirt_vif_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'libvirt_type'"
op|','
string|"'nova.virt.libvirt.driver'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LINUX_DEV_LEN
name|'LINUX_DEV_LEN'
op|'='
number|'14'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBridgeDriver
name|'class'
name|'LibvirtBridgeDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Linux bridge."""'
newline|'\n'
nl|'\n'
DECL|member|_get_configurations
name|'def'
name|'_get_configurations'
op|'('
name|'self'
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
string|'"""Get VIF configurations for bridge type."""'
newline|'\n'
nl|'\n'
name|'mac_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
nl|'\n'
dedent|''
name|'conf'
op|'.'
name|'filtername'
op|'='
string|'"nova-instance-"'
op|'+'
name|'instance'
op|'['
string|"'name'"
op|']'
op|'+'
string|'"-"'
op|'+'
name|'mac_id'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"IP"'
op|','
name|'mapping'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"DHCPSERVER"'
op|','
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"RASERVER"'
op|','
nl|'\n'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'gateway_v6'"
op|')'
op|'+'
string|'"/128"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|','
name|'mask'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_mask'
op|'('
name|'network'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJNET"'
op|','
name|'net'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJMASK"'
op|','
name|'mask'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'net_v6'
op|','
name|'prefixlen_v6'
op|'='
name|'netutils'
op|'.'
name|'get_net_and_prefixlen'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJNET6"'
op|','
name|'net_v6'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_filter_param'
op|'('
string|'"PROJMASK6"'
op|','
name|'prefixlen_v6'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that the bridge exists, and add VIF to it."""'
newline|'\n'
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'network'
op|'.'
name|'get'
op|'('
string|"'multi_host'"
op|')'
name|'and'
nl|'\n'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'should_create_bridge'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'should_create_vlan'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'iface'
op|'='
name|'CONF'
op|'.'
name|'vlan_interface'
name|'or'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ensuring vlan %(vlan)s and bridge %(bridge)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'vlan'"
op|':'
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_vlan_bridge'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'vlan'"
op|']'
op|','
nl|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'iface'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'iface'
op|'='
name|'CONF'
op|'.'
name|'flat_interface'
name|'or'
name|'network'
op|'['
string|"'bridge_interface'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Ensuring bridge %s"'
op|')'
op|','
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_bridge'
op|'('
nl|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
name|'iface'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_get_configurations'
op|'('
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No manual unplugging required."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtOpenVswitchDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtOpenVswitchDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses libivrt type=\'ethernet\'\n\n    Used for libvirt versions that do not support\n    OVS virtual port XML (0.9.10 or earlier).\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_dev_name
name|'def'
name|'get_dev_name'
op|'('
name|'self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"tap"'
op|'+'
name|'iface_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
newline|'\n'
nl|'\n'
DECL|member|create_ovs_vif_port
dedent|''
name|'def'
name|'create_ovs_vif_port'
op|'('
name|'self'
op|','
name|'dev'
op|','
name|'iface_id'
op|','
name|'mac'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ovs-vsctl'"
op|','
string|"'--'"
op|','
string|"'--may-exist'"
op|','
string|"'add-port'"
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
op|','
name|'dev'
op|','
nl|'\n'
string|"'--'"
op|','
string|"'set'"
op|','
string|"'Interface'"
op|','
name|'dev'
op|','
nl|'\n'
string|"'external-ids:iface-id=%s'"
op|'%'
name|'iface_id'
op|','
nl|'\n'
string|"'external-ids:iface-status=active'"
op|','
nl|'\n'
string|"'external-ids:attached-mac=%s'"
op|'%'
name|'mac'
op|','
nl|'\n'
string|"'external-ids:vm-uuid=%s'"
op|'%'
name|'instance_id'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_ovs_vif_port
dedent|''
name|'def'
name|'delete_ovs_vif_port'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ovs-vsctl'"
op|','
string|"'del-port'"
op|','
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
op|','
nl|'\n'
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'delete'"
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'linux_net'
op|'.'
name|'device_exists'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
comment|"# Older version of the command 'ip' from the iproute2 package"
nl|'\n'
comment|"# don't have support for the tuntap option (lp:882568).  If it"
nl|'\n'
comment|"# turns out we're on an old version we work around this by using"
nl|'\n'
comment|'# tunctl.'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|"# First, try with 'ip'"
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'tuntap'"
op|','
string|"'add'"
op|','
name|'dev'
op|','
string|"'mode'"
op|','
string|"'tap'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
comment|'# Second option: tunctl'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tunctl'"
op|','
string|"'-b'"
op|','
string|"'-t'"
op|','
name|'dev'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'dev'
op|','
string|"'up'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'create_ovs_vif_port'
op|'('
name|'dev'
op|','
name|'iface_id'
op|','
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"ethernet"'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'dev'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug the VIF by deleting the port from the bridge."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'self'
op|'.'
name|'delete_ovs_vif_port'
op|'('
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed while unplugging vif"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'class'
name|'LibvirtHybridOVSBridgeDriver'
op|'('
name|'LibvirtBridgeDriver'
op|','
nl|'\n'
DECL|class|LibvirtHybridOVSBridgeDriver
name|'LibvirtOpenVswitchDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver that uses OVS + Linux Bridge for iptables compatibility.\n\n    Enables the use of OVS-based Quantum plugins while at the same\n    time using iptables-based filtering, which requires that vifs be\n    plugged into a linux bridge, not OVS.  IPtables filtering is useful for\n    in particular for Nova security groups.\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_br_name
name|'def'
name|'get_br_name'
op|'('
name|'self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"qbr"'
op|'+'
name|'iface_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_veth_pair_names
dedent|''
name|'def'
name|'get_veth_pair_names'
op|'('
name|'self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
op|'('
string|'"qvb%s"'
op|'%'
name|'iface_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
op|','
nl|'\n'
op|'('
string|'"qvo%s"'
op|'%'
name|'iface_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Plug using hybrid strategy\n\n        Create a per-VIF linux bridge, then link that bridge to the OVS\n        integration bridge via a veth device, setting up the other end\n        of the veth device just like a normal OVS port.  Then boot the\n        VIF on the linux bridge using standard libvirt mechanisms\n        """'
newline|'\n'
nl|'\n'
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'br_name'
op|'='
name|'self'
op|'.'
name|'get_br_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
name|'v1_name'
op|','
name|'v2_name'
op|'='
name|'self'
op|'.'
name|'get_veth_pair_names'
op|'('
name|'iface_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'linux_net'
op|'.'
name|'device_exists'
op|'('
name|'br_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'brctl'"
op|','
string|"'addbr'"
op|','
name|'br_name'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'linux_net'
op|'.'
name|'device_exists'
op|'('
name|'v2_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'linux_net'
op|'.'
name|'_create_veth_pair'
op|'('
name|'v1_name'
op|','
name|'v2_name'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'br_name'
op|','
string|"'up'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'brctl'"
op|','
string|"'addif'"
op|','
name|'br_name'
op|','
name|'v1_name'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create_ovs_vif_port'
op|'('
name|'v2_name'
op|','
name|'iface_id'
op|','
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'['
string|"'bridge'"
op|']'
op|'='
name|'br_name'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_configurations'
op|'('
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""UnPlug using hybrid strategy\n\n        Unhook port from OVS, unhook port from bridge, delete\n        bridge, and delete both veth devices.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'br_name'
op|'='
name|'self'
op|'.'
name|'get_br_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
name|'v1_name'
op|','
name|'v2_name'
op|'='
name|'self'
op|'.'
name|'get_veth_pair_names'
op|'('
name|'iface_id'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'brctl'"
op|','
string|"'delif'"
op|','
name|'br_name'
op|','
name|'v1_name'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'link'"
op|','
string|"'set'"
op|','
name|'br_name'
op|','
string|"'down'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'brctl'"
op|','
string|"'delbr'"
op|','
name|'br_name'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'delete_ovs_vif_port'
op|'('
name|'v2_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed while unplugging vif"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtOpenVswitchVirtualPortDriver
dedent|''
dedent|''
dedent|''
name|'class'
name|'LibvirtOpenVswitchVirtualPortDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses integrated libvirt\n       OVS virtual port XML (introduced in libvirt 0.9.11)."""'
newline|'\n'
nl|'\n'
DECL|member|plug
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Pass data required to create OVS virtual port element"""'
newline|'\n'
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"openvswitch"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"interfaceid"'
op|','
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No action needed.  Libvirt takes care of cleanup"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumLinuxBridgeVIFDriver
dedent|''
dedent|''
name|'class'
name|'QuantumLinuxBridgeVIFDriver'
op|'('
name|'vif'
op|'.'
name|'VIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Linux Bridge when running Quantum."""'
newline|'\n'
nl|'\n'
DECL|member|get_bridge_name
name|'def'
name|'get_bridge_name'
op|'('
name|'self'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"brq"'
op|'+'
name|'network_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_dev_name
dedent|''
name|'def'
name|'get_dev_name'
op|'('
name|'self'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"tap"'
op|'+'
name|'iface_id'
op|')'
op|'['
op|':'
name|'LINUX_DEV_LEN'
op|']'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'iface_id'
op|'='
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_dev_name'
op|'('
name|'iface_id'
op|')'
newline|'\n'
nl|'\n'
name|'bridge'
op|'='
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_bridge'
op|'('
name|'bridge'
op|','
name|'None'
op|','
nl|'\n'
name|'filtering'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'dev'
newline|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'bridge'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No action needed.  Libvirt takes care of cleanup"""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
