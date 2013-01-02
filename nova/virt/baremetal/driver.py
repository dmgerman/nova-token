begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California / ISI'
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
string|'"""\nA driver for Bare-metal platform.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
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
name|'importutils'
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
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'firewall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'imagecache'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'inject_password'"
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
string|"'Whether baremetal compute injects password or not'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir/nova/virt/baremetal/interfaces.template'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for injected network'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vif_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.virt.baremetal.vif_driver.BareMetalVIFDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Baremetal VIF driver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.virt.baremetal.volume_driver.LibvirtVolumeDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Baremetal volume driver.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'instance_type_extra_specs'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'a list of additional capabilities corresponding to '"
nl|'\n'
string|"'instance_type_extra_specs for this compute '"
nl|'\n'
string|"'host to advertise. Valid entries are name=value, pairs '"
nl|'\n'
string|'\'For example, "key1:val1, key2:val2"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.virt.baremetal.pxe.PXE'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Baremetal driver back-end (pxe or tilera)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'power_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.virt.baremetal.ipmi.IPMI'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Baremetal power management method'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'tftp_root'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/tftpboot'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Baremetal compute node\\'s tftp root path'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|baremetal_group
name|'baremetal_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Baremetal Options'"
op|')'
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
name|'register_group'
op|'('
name|'baremetal_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|','
name|'baremetal_group'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_FIREWALL_DRIVER
name|'DEFAULT_FIREWALL_DRIVER'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
nl|'\n'
name|'firewall'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'firewall'
op|'.'
name|'NoopFirewallDriver'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_baremetal_nodes
name|'def'
name|'_get_baremetal_nodes'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'nodes'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'return'
name|'nodes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_baremetal_node_by_instance_uuid
dedent|''
name|'def'
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'ctx'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'if'
name|'node'
op|'['
string|"'service_host'"
op|']'
op|'!='
name|'CONF'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Request for baremetal node %s "'
nl|'\n'
string|'"sent to wrong service host"'
op|')'
op|'%'
name|'instance_uuid'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'node'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_update_state
dedent|''
name|'def'
name|'_update_state'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Update the node state in baremetal DB\n\n    If instance is not supplied, reset the instance_uuid field for this node.\n\n    """'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'task_state'"
op|':'
name|'state'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_power_manager
dedent|''
name|'def'
name|'get_power_manager'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cls'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'power_manager'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalDriver
dedent|''
name|'class'
name|'BareMetalDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""BareMetal hypervisor driver."""'
newline|'\n'
nl|'\n'
DECL|variable|capabilities
name|'capabilities'
op|'='
op|'{'
nl|'\n'
string|'"has_imagecache"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|','
name|'read_only'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BareMetalDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vif_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'vif_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'='
name|'firewall'
op|'.'
name|'load_driver'
op|'('
nl|'\n'
name|'default'
op|'='
name|'DEFAULT_FIREWALL_DRIVER'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'volume_driver'
op|','
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_cache_manager'
op|'='
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'extra_specs'
op|'['
string|'"baremetal_driver"'
op|']'
op|'='
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'driver'
newline|'\n'
name|'for'
name|'pair'
name|'in'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'instance_type_extra_specs'
op|':'
newline|'\n'
indent|'            '
name|'keyval'
op|'='
name|'pair'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'keyval'
op|'['
number|'0'
op|']'
op|'='
name|'keyval'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'keyval'
op|'['
number|'1'
op|']'
op|'='
name|'keyval'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'extra_specs'
op|'['
name|'keyval'
op|'['
number|'0'
op|']'
op|']'
op|'='
name|'keyval'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'not'
string|"'cpu_arch'"
name|'in'
name|'extra_specs'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'cpu_arch is not found in instance_type_extra_specs'"
op|')'
op|')'
newline|'\n'
name|'extra_specs'
op|'['
string|"'cpu_arch'"
op|']'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'extra_specs'
op|'='
name|'extra_specs'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'supported_instances'
op|'='
op|'['
nl|'\n'
op|'('
name|'extra_specs'
op|'['
string|"'cpu_arch'"
op|']'
op|','
string|"'baremetal'"
op|','
string|"'baremetal'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|get_hypervisor_type
dedent|''
name|'def'
name|'get_hypervisor_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'baremetal'"
newline|'\n'
nl|'\n'
DECL|member|get_hypervisor_version
dedent|''
name|'def'
name|'get_hypervisor_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(deva): define the version properly elsewhere'
nl|'\n'
indent|'        '
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'_get_baremetal_nodes'
op|'('
name|'ctx'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
op|'['
string|"'instance_uuid'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'inst'
op|'='
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctx'
op|','
nl|'\n'
name|'node'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'inst'
op|':'
newline|'\n'
indent|'                    '
name|'l'
op|'.'
name|'append'
op|'('
name|'inst'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'l'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'network_info'
op|'='
name|'None'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'node_id'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'node'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'node_id'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"Baremetal node id not supplied to driver"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(deva): this db method will raise an exception if the node is'
nl|'\n'
comment|'#             already in use. We call it here to ensure no one else'
nl|'\n'
comment|'#             allocates this node before we begin provisioning it.'
nl|'\n'
dedent|''
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_set_uuid_safe'
op|'('
name|'context'
op|','
name|'node_id'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'BUILDING'
op|'}'
op|')'
newline|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_plug_vifs'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'setup_basic_filtering'
op|'('
nl|'\n'
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'prepare_instance_filter'
op|'('
nl|'\n'
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'apply_instance_filter'
op|'('
nl|'\n'
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
name|'block_device_mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'                '
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'mountpoint'
op|'='
name|'vol'
op|'['
string|"'mount_device'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'attach_volume'
op|'('
nl|'\n'
name|'connection_info'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'image_info'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'cache_images'
op|'('
nl|'\n'
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'image_meta'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'network_info'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_bootloader'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'deactivate_bootloader'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'destroy_images'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
comment|'# TODO(deva): do network and volume cleanup here'
nl|'\n'
indent|'            '
name|'raise'
name|'e'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(deva): pm.activate_node should not raise exceptions.'
nl|'\n'
comment|'#             We check its success in "finally" block'
nl|'\n'
indent|'            '
name|'pm'
op|'.'
name|'activate_node'
op|'('
op|')'
newline|'\n'
name|'pm'
op|'.'
name|'start_console'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pm'
op|'.'
name|'state'
op|'!='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|':'
newline|'\n'
indent|'                '
name|'pm'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_update_state'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'pm'
op|'.'
name|'state'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Failed to update state record for "'
nl|'\n'
string|'"baremetal node %s"'
op|')'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
dedent|''
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'reboot_type'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'state'
op|'='
name|'pm'
op|'.'
name|'reboot_node'
op|'('
op|')'
newline|'\n'
name|'_update_state'
op|'('
name|'ctx'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
comment|'# TODO(deva): refactor so that dangling files can be cleaned'
nl|'\n'
comment|'#             up even after a failed boot or delete'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Delete called on non-existing instance %s"'
op|')'
nl|'\n'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'deactivate_node'
op|'('
name|'ctx'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'pm'
op|'.'
name|'stop_console'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'## power off the node'
nl|'\n'
name|'state'
op|'='
name|'pm'
op|'.'
name|'deactivate_node'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'## cleanup volumes'
nl|'\n'
comment|'# NOTE(vish): we disconnect from volumes regardless'
nl|'\n'
name|'block_device_mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'mountpoint'
op|'='
name|'vol'
op|'['
string|"'mount_device'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'detach_volume'
op|'('
name|'connection_info'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'deactivate_bootloader'
op|'('
name|'ctx'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'destroy_images'
op|'('
name|'ctx'
op|','
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# stop firewall'
nl|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'unfilter_instance'
op|'('
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_unplug_vifs'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
name|'_update_state'
op|'('
name|'ctx'
op|','
name|'node'
op|','
name|'None'
op|','
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_off
dedent|''
name|'def'
name|'power_off'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Power off the specified instance."""'
newline|'\n'
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'pm'
op|'.'
name|'deactivate_node'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_on
dedent|''
name|'def'
name|'power_on'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Power on the specified instance"""'
newline|'\n'
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'pm'
op|'.'
name|'activate_node'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volume_connector
dedent|''
name|'def'
name|'get_volume_connector'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_driver'
op|'.'
name|'get_volume_connector'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_driver'
op|'.'
name|'attach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|detach_volume
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_driver'
op|'.'
name|'detach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(deva): compute/manager.py expects to get NotFound exception'
nl|'\n'
comment|'#             so we convert from InstanceNotFound'
nl|'\n'
indent|'        '
name|'inst_uuid'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'inst_uuid'
op|')'
newline|'\n'
name|'pm'
op|'='
name|'get_power_manager'
op|'('
name|'node'
op|'='
name|'node'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'ps'
op|'='
name|'power_state'
op|'.'
name|'SHUTDOWN'
newline|'\n'
name|'if'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ps'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'state'"
op|':'
name|'ps'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'node'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'node'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'node'
op|'['
string|"'cpus'"
op|']'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'refresh_security_group_rules'
op|'('
name|'security_group_id'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'refresh_security_group_members'
op|'('
name|'security_group_id'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'refresh_provider_fw_rules'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_node_resource
dedent|''
name|'def'
name|'_node_resource'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vcpus_used'
op|'='
number|'0'
newline|'\n'
name|'memory_mb_used'
op|'='
number|'0'
newline|'\n'
name|'local_gb_used'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'vcpus'
op|'='
name|'node'
op|'['
string|"'cpus'"
op|']'
newline|'\n'
name|'memory_mb'
op|'='
name|'node'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'local_gb'
op|'='
name|'node'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'if'
name|'node'
op|'['
string|"'registration_status'"
op|']'
op|'!='
string|"'done'"
name|'or'
name|'node'
op|'['
string|"'instance_uuid'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'vcpus_used'
op|'='
name|'node'
op|'['
string|"'cpus'"
op|']'
newline|'\n'
name|'memory_mb_used'
op|'='
name|'node'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'local_gb_used'
op|'='
name|'node'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'dic'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'memory_mb'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'local_gb'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
name|'vcpus_used'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'memory_mb_used'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'local_gb_used'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
name|'self'
op|'.'
name|'get_hypervisor_type'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'self'
op|'.'
name|'get_hypervisor_version'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'str'
op|'('
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'baremetal cpu'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'dic'
newline|'\n'
nl|'\n'
DECL|member|refresh_instance_security_rules
dedent|''
name|'def'
name|'refresh_instance_security_rules'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'refresh_instance_security_rules'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|','
name|'nodename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'nodename'
op|')'
newline|'\n'
name|'dic'
op|'='
name|'self'
op|'.'
name|'_node_resource'
op|'('
name|'node'
op|')'
newline|'\n'
name|'return'
name|'dic'
newline|'\n'
nl|'\n'
DECL|member|ensure_filtering_rules_for_instance
dedent|''
name|'def'
name|'ensure_filtering_rules_for_instance'
op|'('
name|'self'
op|','
name|'instance_ref'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'setup_basic_filtering'
op|'('
name|'instance_ref'
op|','
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'prepare_instance_filter'
op|'('
name|'instance_ref'
op|','
nl|'\n'
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance_ref'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'firewall_driver'
op|'.'
name|'unfilter_instance'
op|'('
name|'instance_ref'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'caps'
op|'='
op|'['
op|']'
newline|'\n'
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'nodes'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_host'
op|'='
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'nodes'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'='
name|'self'
op|'.'
name|'_node_resource'
op|'('
name|'node'
op|')'
newline|'\n'
name|'nodename'
op|'='
name|'str'
op|'('
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'data'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'res'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'vcpus_used'"
op|']'
op|'='
name|'res'
op|'['
string|"'vcpus_used'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'cpu_info'"
op|']'
op|'='
name|'res'
op|'['
string|"'cpu_info'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'disk_total'"
op|']'
op|'='
name|'res'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'disk_used'"
op|']'
op|'='
name|'res'
op|'['
string|"'local_gb_used'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'disk_available'"
op|']'
op|'='
name|'res'
op|'['
string|"'local_gb'"
op|']'
op|'-'
name|'res'
op|'['
string|"'local_gb_used'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'host_memory_total'"
op|']'
op|'='
name|'res'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'host_memory_free'"
op|']'
op|'='
name|'res'
op|'['
string|"'memory_mb'"
op|']'
op|'-'
name|'res'
op|'['
string|"'memory_mb_used'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'hypervisor_type'"
op|']'
op|'='
name|'res'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'hypervisor_version'"
op|']'
op|'='
name|'res'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
name|'nodename'
newline|'\n'
name|'data'
op|'['
string|"'supported_instances'"
op|']'
op|'='
name|'self'
op|'.'
name|'supported_instances'
newline|'\n'
name|'data'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'host'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'host'
newline|'\n'
name|'data'
op|'['
string|"'node'"
op|']'
op|'='
name|'nodename'
newline|'\n'
comment|"# TODO(NTTdocomo): put node's extra specs here"
nl|'\n'
name|'caps'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'caps'
newline|'\n'
nl|'\n'
DECL|member|plug_vifs
dedent|''
name|'def'
name|'plug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Plugin VIFs into networks."""'
newline|'\n'
name|'self'
op|'.'
name|'_plug_vifs'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_plug_vifs
dedent|''
name|'def'
name|'_plug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
dedent|''
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'node'
op|':'
newline|'\n'
indent|'            '
name|'pifs'
op|'='
name|'db'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'pif'
name|'in'
name|'pifs'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'pif'
op|'['
string|"'vif_uuid'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'bm_interface_set_vif_uuid'
op|'('
name|'context'
op|','
name|'pif'
op|'['
string|"'id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
op|'('
name|'network'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'vif_driver'
op|'.'
name|'plug'
op|'('
name|'instance'
op|','
op|'('
name|'network'
op|','
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_unplug_vifs
dedent|''
dedent|''
name|'def'
name|'_unplug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
op|'('
name|'network'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'vif_driver'
op|'.'
name|'unplug'
op|'('
name|'instance'
op|','
op|'('
name|'network'
op|','
name|'mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|manage_image_cache
dedent|''
dedent|''
name|'def'
name|'manage_image_cache'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Manage the local cache of images."""'
newline|'\n'
name|'self'
op|'.'
name|'image_cache_manager'
op|'.'
name|'verify_base_images'
op|'('
name|'context'
op|','
name|'all_instances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'='
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_console_output'
op|'('
name|'node'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_available_nodes
dedent|''
name|'def'
name|'get_available_nodes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
op|'['
name|'str'
op|'('
name|'n'
op|'['
string|"'id'"
op|']'
op|')'
name|'for'
name|'n'
name|'in'
name|'_get_baremetal_nodes'
op|'('
name|'context'
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
