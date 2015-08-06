begin_unit
comment|'# Copyright (C) 2013 Red Hat, Inc.'
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
string|'"""\nPolicy based configuration of libvirt objects\n\nThis module provides helper APIs for populating the config.py\nclasses based on common operational needs / policies\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'utils'
name|'as'
name|'pci_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_guest_frontend_config
name|'def'
name|'set_vif_guest_frontend_config'
op|'('
name|'conf'
op|','
name|'mac'
op|','
name|'model'
op|','
name|'driver'
op|','
name|'queues'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with guest frontend details.\n    """'
newline|'\n'
name|'conf'
op|'.'
name|'mac_addr'
op|'='
name|'mac'
newline|'\n'
name|'if'
name|'model'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'model'
op|'='
name|'model'
newline|'\n'
dedent|''
name|'if'
name|'driver'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'driver_name'
op|'='
name|'driver'
newline|'\n'
dedent|''
name|'if'
name|'queues'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'vhost_queues'
op|'='
name|'queues'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_bridge_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_bridge_config'
op|'('
name|'conf'
op|','
name|'brname'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for a software bridge.\n    """'
newline|'\n'
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
name|'brname'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_ethernet_config
dedent|''
name|'def'
name|'set_vif_host_backend_ethernet_config'
op|'('
name|'conf'
op|','
name|'tapname'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an externally configured\n    host device.\n\n    NB use of this configuration is discouraged by\n    libvirt project and will mark domains as \'tainted\'.\n    """'
newline|'\n'
nl|'\n'
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
name|'tapname'
newline|'\n'
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_ovs_config
dedent|''
name|'def'
name|'set_vif_host_backend_ovs_config'
op|'('
name|'conf'
op|','
name|'brname'
op|','
name|'interfaceid'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an OpenVSwitch bridge.\n    """'
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
name|'brname'
newline|'\n'
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
name|'interfaceid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'script'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_802qbg_config
dedent|''
name|'def'
name|'set_vif_host_backend_802qbg_config'
op|'('
name|'conf'
op|','
name|'devname'
op|','
name|'managerid'
op|','
nl|'\n'
name|'typeid'
op|','
name|'typeidversion'
op|','
nl|'\n'
name|'instanceid'
op|','
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an 802.1qbg device.\n    """'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"direct"'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'source_mode'
op|'='
string|'"vepa"'
newline|'\n'
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"802.1Qbg"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"managerid"'
op|','
name|'managerid'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"typeid"'
op|','
name|'typeid'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"typeidversion"'
op|','
name|'typeidversion'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"instanceid"'
op|','
name|'instanceid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_802qbh_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_802qbh_config'
op|'('
name|'conf'
op|','
name|'net_type'
op|','
name|'devname'
op|','
name|'profileid'
op|','
nl|'\n'
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an 802.1qbh device.\n    """'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
name|'net_type'
newline|'\n'
name|'if'
name|'net_type'
op|'=='
string|"'direct'"
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'source_mode'
op|'='
string|"'passthrough'"
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'pci_utils'
op|'.'
name|'get_ifname_by_pci_address'
op|'('
name|'devname'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
string|"'vhost'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'model'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'conf'
op|'.'
name|'vporttype'
op|'='
string|'"802.1Qbh"'
newline|'\n'
name|'conf'
op|'.'
name|'add_vport_param'
op|'('
string|'"profileid"'
op|','
name|'profileid'
op|')'
newline|'\n'
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_hw_veb
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_hw_veb'
op|'('
name|'conf'
op|','
name|'net_type'
op|','
name|'devname'
op|','
name|'vlan'
op|','
nl|'\n'
name|'tapname'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for an device that supports hardware\n    virtual ethernet bridge.\n    """'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
name|'net_type'
newline|'\n'
name|'if'
name|'net_type'
op|'=='
string|"'direct'"
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'source_mode'
op|'='
string|"'passthrough'"
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'pci_utils'
op|'.'
name|'get_ifname_by_pci_address'
op|'('
name|'devname'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
string|"'vhost'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'model'
op|'='
name|'None'
newline|'\n'
name|'conf'
op|'.'
name|'vlan'
op|'='
name|'vlan'
newline|'\n'
dedent|''
name|'if'
name|'tapname'
op|':'
newline|'\n'
indent|'        '
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'tapname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_ib_hostdev_config
dedent|''
dedent|''
name|'def'
name|'set_vif_host_backend_ib_hostdev_config'
op|'('
name|'conf'
op|','
name|'pci_slot'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with hostdev Interface.\n    """'
newline|'\n'
name|'conf'
op|'.'
name|'domain'
op|','
name|'conf'
op|'.'
name|'bus'
op|','
name|'conf'
op|'.'
name|'slot'
op|','
name|'conf'
op|'.'
name|'function'
op|'='
op|'('
nl|'\n'
name|'pci_utils'
op|'.'
name|'get_pci_address_fields'
op|'('
name|'pci_slot'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_direct_config
dedent|''
name|'def'
name|'set_vif_host_backend_direct_config'
op|'('
name|'conf'
op|','
name|'devname'
op|','
name|'mode'
op|'='
string|'"passthrough"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with direct Interface.\n    """'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"direct"'
newline|'\n'
name|'conf'
op|'.'
name|'source_mode'
op|'='
name|'mode'
newline|'\n'
name|'conf'
op|'.'
name|'source_dev'
op|'='
name|'devname'
newline|'\n'
name|'conf'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_host_backend_vhostuser_config
dedent|''
name|'def'
name|'set_vif_host_backend_vhostuser_config'
op|'('
name|'conf'
op|','
name|'mode'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Populate a LibvirtConfigGuestInterface instance\n    with host backend details for vhostuser socket.\n    """'
newline|'\n'
name|'conf'
op|'.'
name|'net_type'
op|'='
string|'"vhostuser"'
newline|'\n'
name|'conf'
op|'.'
name|'vhostuser_type'
op|'='
string|'"unix"'
newline|'\n'
name|'conf'
op|'.'
name|'vhostuser_mode'
op|'='
name|'mode'
newline|'\n'
name|'conf'
op|'.'
name|'vhostuser_path'
op|'='
name|'path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_vif_bandwidth_config
dedent|''
name|'def'
name|'set_vif_bandwidth_config'
op|'('
name|'conf'
op|','
name|'inst_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Config vif inbound/outbound bandwidth limit. parameters are\n    set in instance_type_extra_specs table, key is in  the format\n    quota:vif_inbound_average.\n    """'
newline|'\n'
nl|'\n'
name|'bandwidth_items'
op|'='
op|'['
string|"'vif_inbound_average'"
op|','
string|"'vif_inbound_peak'"
op|','
nl|'\n'
string|"'vif_inbound_burst'"
op|','
string|"'vif_outbound_average'"
op|','
string|"'vif_outbound_peak'"
op|','
nl|'\n'
string|"'vif_outbound_burst'"
op|']'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'inst_type'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|','
op|'{'
op|'}'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scope'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'scope'
op|')'
op|'>'
number|'1'
name|'and'
name|'scope'
op|'['
number|'0'
op|']'
op|'=='
string|"'quota'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'scope'
op|'['
number|'1'
op|']'
name|'in'
name|'bandwidth_items'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'conf'
op|','
name|'scope'
op|'['
number|'1'
op|']'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
