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
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'designer'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
newline|'\n'
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
comment|'# quantum_ovs_bridge is used, if Quantum provides Nova'
nl|'\n'
comment|"# the 'vif_type' portbinding field"
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
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use virtio for bridge interfaces with KVM/QEMU'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBaseVIFDriver
name|'class'
name|'LibvirtBaseVIFDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|get_vif_devname
indent|'    '
name|'def'
name|'get_vif_devname'
op|'('
name|'self'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'vif_devname'"
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'mapping'
op|'['
string|"'vif_devname'"
op|']'
newline|'\n'
dedent|''
name|'return'
op|'('
string|'"nic"'
op|'+'
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
op|'['
op|':'
name|'network_model'
op|'.'
name|'NIC_NAME_LEN'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'model'
op|'='
name|'None'
newline|'\n'
name|'driver'
op|'='
name|'None'
newline|'\n'
name|'if'
op|'('
name|'CONF'
op|'.'
name|'libvirt_type'
name|'in'
op|'('
string|"'kvm'"
op|','
string|"'qemu'"
op|')'
name|'and'
nl|'\n'
name|'CONF'
op|'.'
name|'libvirt_use_virtio_for_bridges'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
comment|'# Workaround libvirt bug, where it mistakenly'
nl|'\n'
comment|'# enables vhost mode, even for non-KVM guests'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_type'
op|'=='
string|'"qemu"'
op|':'
newline|'\n'
indent|'                '
name|'driver'
op|'='
string|'"qemu"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'designer'
op|'.'
name|'set_vif_guest_frontend_config'
op|'('
nl|'\n'
name|'conf'
op|','
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|','
name|'model'
op|','
name|'driver'
op|')'
newline|'\n'
nl|'\n'
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
name|'pass'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtGenericVIFDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtGenericVIFDriver'
op|'('
name|'LibvirtBaseVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generic VIF driver for libvirt networking."""'
newline|'\n'
nl|'\n'
DECL|member|get_bridge_name
name|'def'
name|'get_bridge_name'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_config_bridge
dedent|''
name|'def'
name|'get_config_bridge'
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
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtGenericVIFDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network'
op|','
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
name|'designer'
op|'.'
name|'set_vif_host_backend_bridge_config'
op|'('
nl|'\n'
name|'conf'
op|','
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
op|')'
op|')'
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
name|'name'
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
name|'primary_addr'
op|'='
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
newline|'\n'
name|'dhcp_server'
op|'='
name|'ra_server'
op|'='
name|'ipv4_cidr'
op|'='
name|'ipv6_cidr'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'if'
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'dhcp_server'
op|'='
name|'mapping'
op|'['
string|"'dhcp_server'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'ra_server'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'gateway_v6'"
op|')'
op|'+'
string|'"/128"'
newline|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'            '
name|'ipv4_cidr'
op|'='
name|'network'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'ipv6_cidr'
op|'='
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'designer'
op|'.'
name|'set_vif_host_backend_filter_config'
op|'('
nl|'\n'
name|'conf'
op|','
name|'name'
op|','
name|'primary_addr'
op|','
name|'dhcp_server'
op|','
nl|'\n'
name|'ra_server'
op|','
name|'ipv4_cidr'
op|','
name|'ipv6_cidr'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'vif_type'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'vif_type'"
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"vif_type=%(vif_type)s instance=%(instance)s "'
nl|'\n'
string|'"network=%(network)s mapping=%(mapping)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vif_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"vif_type parameter must be present "'
nl|'\n'
string|'"for this vif_driver implementation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vif_type'
op|'=='
name|'network_model'
op|'.'
name|'VIF_TYPE_BRIDGE'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'get_config_bridge'
op|'('
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unexpected vif_type=%s"'
op|')'
op|'%'
name|'vif_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug_bridge
dedent|''
dedent|''
name|'def'
name|'plug_bridge'
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
name|'super'
op|'('
name|'LibvirtGenericVIFDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'plug'
op|'('
name|'instance'
op|','
name|'vif'
op|')'
newline|'\n'
nl|'\n'
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
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
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
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
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
nl|'\n'
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
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
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
name|'iface'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
dedent|''
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
name|'vif_type'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'vif_type'"
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"vif_type=%(vif_type)s instance=%(instance)s "'
nl|'\n'
string|'"network=%(network)s mapping=%(mapping)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vif_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"vif_type parameter must be present "'
nl|'\n'
string|'"for this vif_driver implementation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vif_type'
op|'=='
name|'network_model'
op|'.'
name|'VIF_TYPE_BRIDGE'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'plug_bridge'
op|'('
name|'instance'
op|','
name|'vif'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unexpected vif_type=%s"'
op|')'
op|'%'
name|'vif_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug_bridge
dedent|''
dedent|''
name|'def'
name|'unplug_bridge'
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
name|'super'
op|'('
name|'LibvirtGenericVIFDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'unplug'
op|'('
name|'instance'
op|','
name|'vif'
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
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'vif_type'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'vif_type'"
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"vif_type=%(vif_type)s instance=%(instance)s "'
nl|'\n'
string|'"network=%(network)s mapping=%(mapping)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vif_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"vif_type parameter must be present "'
nl|'\n'
string|'"for this vif_driver implementation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vif_type'
op|'=='
name|'network_model'
op|'.'
name|'VIF_TYPE_BRIDGE'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unplug_bridge'
op|'('
name|'instance'
op|','
name|'vif'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unexpected vif_type=%s"'
op|')'
op|'%'
name|'vif_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBridgeDriver
dedent|''
dedent|''
dedent|''
name|'class'
name|'LibvirtBridgeDriver'
op|'('
name|'LibvirtGenericVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deprecated in favour of LibvirtGenericVIFDriver.\n       Retained in Grizzly for compatibility with Quantum\n       drivers which do not yet report \'vif_type\' port binding.\n       To be removed in Hxxxx."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'deprecated'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"LibvirtBridgeDriver is deprecated and "'
nl|'\n'
string|'"will be removed in the Hxxxx release. Please "'
nl|'\n'
string|'"update the \'libvirt_vif_driver\' config parameter "'
nl|'\n'
string|'"to use the LibvirtGenericVIFDriver class instead"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'return'
name|'self'
op|'.'
name|'get_config_bridge'
op|'('
name|'instance'
op|','
name|'network'
op|','
name|'mapping'
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
name|'self'
op|'.'
name|'plug_bridge'
op|'('
name|'instance'
op|','
name|'vif'
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
name|'self'
op|'.'
name|'unplug_bridge'
op|'('
name|'instance'
op|','
name|'vif'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtOpenVswitchDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtOpenVswitchDriver'
op|'('
name|'LibvirtBaseVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses libivrt type=\'ethernet\'\n\n    Used for libvirt versions that do not support\n    OVS virtual port XML (0.9.10 or earlier).\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_bridge_name
name|'def'
name|'get_bridge_name'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network'
op|'.'
name|'get'
op|'('
string|"'bridge'"
op|')'
name|'or'
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
newline|'\n'
nl|'\n'
DECL|member|get_ovs_interfaceid
dedent|''
name|'def'
name|'get_ovs_interfaceid'
op|'('
name|'self'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'ovs_interfaceid'"
op|')'
name|'or'
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtOpenVswitchDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network'
op|','
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
name|'designer'
op|'.'
name|'set_vif_host_backend_ethernet_config'
op|'('
name|'conf'
op|','
name|'dev'
op|')'
newline|'\n'
nl|'\n'
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
name|'network'
op|','
name|'mapping'
op|'='
name|'vif'
newline|'\n'
name|'iface_id'
op|'='
name|'self'
op|'.'
name|'get_ovs_interfaceid'
op|'('
name|'mapping'
op|')'
newline|'\n'
name|'dev'
op|'='
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'create_tap_dev'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'linux_net'
op|'.'
name|'create_ovs_vif_port'
op|'('
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
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
name|'linux_net'
op|'.'
name|'delete_ovs_vif_port'
op|'('
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
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
DECL|class|LibvirtHybridOVSBridgeDriver
dedent|''
dedent|''
dedent|''
name|'class'
name|'LibvirtHybridOVSBridgeDriver'
op|'('
name|'LibvirtBridgeDriver'
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
name|'network_model'
op|'.'
name|'NIC_NAME_LEN'
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
name|'network_model'
op|'.'
name|'NIC_NAME_LEN'
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
name|'network_model'
op|'.'
name|'NIC_NAME_LEN'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_bridge_name
dedent|''
name|'def'
name|'get_bridge_name'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network'
op|'.'
name|'get'
op|'('
string|"'bridge'"
op|')'
name|'or'
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
newline|'\n'
nl|'\n'
DECL|member|get_ovs_interfaceid
dedent|''
name|'def'
name|'get_ovs_interfaceid'
op|'('
name|'self'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'ovs_interfaceid'"
op|')'
name|'or'
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'br_name'
op|'='
name|'self'
op|'.'
name|'get_br_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'bridge'"
op|']'
op|'='
name|'br_name'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'LibvirtHybridOVSBridgeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network'
op|','
nl|'\n'
name|'mapping'
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
name|'self'
op|'.'
name|'get_ovs_interfaceid'
op|'('
name|'mapping'
op|')'
newline|'\n'
name|'br_name'
op|'='
name|'self'
op|'.'
name|'get_br_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
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
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
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
name|'linux_net'
op|'.'
name|'create_ovs_vif_port'
op|'('
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
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
DECL|member|unplug
dedent|''
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
name|'br_name'
op|'='
name|'self'
op|'.'
name|'get_br_name'
op|'('
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
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
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
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
name|'linux_net'
op|'.'
name|'delete_ovs_vif_port'
op|'('
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
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
name|'LibvirtBaseVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VIF driver for Open vSwitch that uses integrated libvirt\n       OVS virtual port XML (introduced in libvirt 0.9.11)."""'
newline|'\n'
nl|'\n'
DECL|member|get_bridge_name
name|'def'
name|'get_bridge_name'
op|'('
name|'self'
op|','
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'network'
op|'.'
name|'get'
op|'('
string|"'bridge'"
op|')'
name|'or'
name|'CONF'
op|'.'
name|'libvirt_ovs_bridge'
newline|'\n'
nl|'\n'
DECL|member|get_ovs_interfaceid
dedent|''
name|'def'
name|'get_ovs_interfaceid'
op|'('
name|'self'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'mapping'
op|'.'
name|'get'
op|'('
string|"'ovs_interfaceid'"
op|')'
name|'or'
name|'mapping'
op|'['
string|"'vif_uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
string|'"""Pass data required to create OVS virtual port element."""'
newline|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtOpenVswitchVirtualPortDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network'
op|','
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
name|'designer'
op|'.'
name|'set_vif_host_backend_ovs_config'
op|'('
nl|'\n'
name|'conf'
op|','
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_ovs_interfaceid'
op|'('
name|'mapping'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'pass'
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
string|'"""No action needed.  Libvirt takes care of cleanup."""'
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
name|'LibvirtBaseVIFDriver'
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
name|'network'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'def_bridge'
op|'='
op|'('
string|'"brq"'
op|'+'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
op|'['
op|':'
name|'network_model'
op|'.'
name|'NIC_NAME_LEN'
op|']'
newline|'\n'
name|'return'
name|'network'
op|'.'
name|'get'
op|'('
string|"'bridge'"
op|')'
name|'or'
name|'def_bridge'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
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
name|'linux_net'
op|'.'
name|'LinuxBridgeInterfaceDriver'
op|'.'
name|'ensure_bridge'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
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
name|'super'
op|'('
name|'QuantumLinuxBridgeVIFDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network'
op|','
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
nl|'\n'
name|'designer'
op|'.'
name|'set_vif_host_backend_bridge_config'
op|'('
nl|'\n'
name|'conf'
op|','
name|'self'
op|'.'
name|'get_bridge_name'
op|'('
name|'network'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_vif_devname'
op|'('
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'pass'
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
string|'"""No action needed.  Libvirt takes care of cleanup."""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
