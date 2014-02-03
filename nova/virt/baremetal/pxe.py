begin_unit
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""\nClass for PXE bare-metal nodes.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'jinja2'
newline|'\n'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
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
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'loopingcall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
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
name|'base'
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
op|'.'
name|'baremetal'
name|'import'
name|'utils'
name|'as'
name|'bm_utils'
newline|'\n'
nl|'\n'
DECL|variable|pxe_opts
name|'pxe_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'deploy_kernel'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default kernel image ID used in deployment phase'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'deploy_ramdisk'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default ramdisk image ID used in deployment phase'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'net_config_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir/nova/virt/baremetal/'"
nl|'\n'
string|"'net-dhcp.ubuntu.template'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for injected network config'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pxe_append_params'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'nofb nomodeset vga=normal'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Additional append parameters for baremetal PXE boot'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pxe_config_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir/nova/virt/baremetal/pxe_config.template'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for PXE configuration'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_file_injection'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If True, enable file injection for network info, '"
nl|'\n'
string|"'files and admin password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'pxe_deploy_timeout'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Timeout for PXE deployments. Default: 0 (unlimited)'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'pxe_network_config'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If set, pass the network configuration details to the '"
nl|'\n'
string|"'initramfs via cmdline.'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pxe_bootfile_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'This gets passed to Neutron as the bootfile dhcp '"
nl|'\n'
string|"'parameter when the dhcp_options_enabled is set.'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'pxelinux.0'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'pxe_opts'
op|','
name|'baremetal_group'
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
DECL|function|build_pxe_network_config
name|'def'
name|'build_pxe_network_config'
op|'('
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'interfaces'
op|'='
name|'bm_utils'
op|'.'
name|'map_network_interfaces'
op|'('
name|'network_info'
op|','
name|'CONF'
op|'.'
name|'use_ipv6'
op|')'
newline|'\n'
name|'template'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'        '
name|'template'
op|'='
string|'"ip=%(address)s::%(gateway)s:%(netmask)s::%(name)s:off"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'template'
op|'='
op|'('
string|'"ip=[%(address_v6)s]::[%(gateway_v6)s]:"'
nl|'\n'
string|'"[%(netmask_v6)s]::%(name)s:off"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'net_config'
op|'='
op|'['
name|'template'
op|'%'
name|'iface'
name|'for'
name|'iface'
name|'in'
name|'interfaces'
op|']'
newline|'\n'
name|'return'
string|"' '"
op|'.'
name|'join'
op|'('
name|'net_config'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_pxe_config
dedent|''
name|'def'
name|'build_pxe_config'
op|'('
name|'deployment_id'
op|','
name|'deployment_key'
op|','
name|'deployment_iscsi_iqn'
op|','
nl|'\n'
name|'deployment_aki_path'
op|','
name|'deployment_ari_path'
op|','
nl|'\n'
name|'aki_path'
op|','
name|'ari_path'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build the PXE config file for a node\n\n    This method builds the PXE boot configuration file for a node,\n    given all the required parameters.\n\n    The resulting file has both a "deploy" and "boot" label, which correspond\n    to the two phases of booting. This may be extended later.\n\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Building PXE config for deployment %s."'
op|')'
op|'%'
name|'deployment_id'
op|')'
newline|'\n'
nl|'\n'
name|'network_config'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'network_info'
name|'and'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_network_config'
op|':'
newline|'\n'
indent|'        '
name|'network_config'
op|'='
name|'build_pxe_network_config'
op|'('
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'pxe_options'
op|'='
op|'{'
nl|'\n'
string|"'deployment_id'"
op|':'
name|'deployment_id'
op|','
nl|'\n'
string|"'deployment_key'"
op|':'
name|'deployment_key'
op|','
nl|'\n'
string|"'deployment_iscsi_iqn'"
op|':'
name|'deployment_iscsi_iqn'
op|','
nl|'\n'
string|"'deployment_aki_path'"
op|':'
name|'deployment_aki_path'
op|','
nl|'\n'
string|"'deployment_ari_path'"
op|':'
name|'deployment_ari_path'
op|','
nl|'\n'
string|"'aki_path'"
op|':'
name|'aki_path'
op|','
nl|'\n'
string|"'ari_path'"
op|':'
name|'ari_path'
op|','
nl|'\n'
string|"'pxe_append_params'"
op|':'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_append_params'
op|','
nl|'\n'
string|"'pxe_network_config'"
op|':'
name|'network_config'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'tmpl_path'
op|','
name|'tmpl_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_config_template'
op|')'
newline|'\n'
name|'env'
op|'='
name|'jinja2'
op|'.'
name|'Environment'
op|'('
name|'loader'
op|'='
name|'jinja2'
op|'.'
name|'FileSystemLoader'
op|'('
name|'tmpl_path'
op|')'
op|')'
newline|'\n'
name|'template'
op|'='
name|'env'
op|'.'
name|'get_template'
op|'('
name|'tmpl_file'
op|')'
newline|'\n'
name|'return'
name|'template'
op|'.'
name|'render'
op|'('
op|'{'
string|"'pxe_options'"
op|':'
name|'pxe_options'
op|','
nl|'\n'
string|"'ROOT'"
op|':'
string|"'${ROOT}'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_network_config
dedent|''
name|'def'
name|'build_network_config'
op|'('
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'interfaces'
op|'='
name|'bm_utils'
op|'.'
name|'map_network_interfaces'
op|'('
name|'network_info'
op|','
name|'CONF'
op|'.'
name|'use_ipv6'
op|')'
newline|'\n'
name|'tmpl_path'
op|','
name|'tmpl_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'net_config_template'
op|')'
newline|'\n'
name|'env'
op|'='
name|'jinja2'
op|'.'
name|'Environment'
op|'('
name|'loader'
op|'='
name|'jinja2'
op|'.'
name|'FileSystemLoader'
op|'('
name|'tmpl_path'
op|')'
op|')'
newline|'\n'
name|'template'
op|'='
name|'env'
op|'.'
name|'get_template'
op|'('
name|'tmpl_file'
op|')'
newline|'\n'
name|'return'
name|'template'
op|'.'
name|'render'
op|'('
op|'{'
string|"'interfaces'"
op|':'
name|'interfaces'
op|','
nl|'\n'
string|"'use_ipv6'"
op|':'
name|'CONF'
op|'.'
name|'use_ipv6'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_deploy_aki_id
dedent|''
name|'def'
name|'get_deploy_aki_id'
op|'('
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'flavor'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'baremetal:deploy_kernel_id'"
op|','
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'deploy_kernel'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_deploy_ari_id
dedent|''
name|'def'
name|'get_deploy_ari_id'
op|'('
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'flavor'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'baremetal:deploy_ramdisk_id'"
op|','
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'deploy_ramdisk'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_dir_path
dedent|''
name|'def'
name|'get_image_dir_path'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate the dir for an instances disk."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_file_path
dedent|''
name|'def'
name|'get_image_file_path'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate the full path for an instances disk."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
string|"'disk'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pxe_config_file_path
dedent|''
name|'def'
name|'get_pxe_config_file_path'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate the path for an instances PXE config file."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'config'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_partition_sizes
dedent|''
name|'def'
name|'get_partition_sizes'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'root_mb'
op|'='
name|'flavor'
op|'['
string|"'root_gb'"
op|']'
op|'*'
number|'1024'
newline|'\n'
name|'swap_mb'
op|'='
name|'flavor'
op|'['
string|"'swap'"
op|']'
newline|'\n'
name|'ephemeral_mb'
op|'='
name|'flavor'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
comment|'# NOTE(deva): For simpler code paths on the deployment side,'
nl|'\n'
comment|'#             we always create a swap partition. If the flavor'
nl|'\n'
comment|'#             does not specify any swap, we default to 1MB'
nl|'\n'
name|'if'
name|'swap_mb'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'swap_mb'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pxe_mac_path
dedent|''
name|'def'
name|'get_pxe_mac_path'
op|'('
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a MAC address into a PXE config file name."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
nl|'\n'
string|"'pxelinux.cfg'"
op|','
nl|'\n'
string|'"01-"'
op|'+'
name|'mac'
op|'.'
name|'replace'
op|'('
string|'":"'
op|','
string|'"-"'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_tftp_image_info
dedent|''
name|'def'
name|'get_tftp_image_info'
op|'('
name|'instance'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate the paths for tftp files for this instance\n\n    Raises NovaException if\n    - instance does not contain kernel_id or ramdisk_id\n    - deploy_kernel_id or deploy_ramdisk_id can not be read from\n      flavor[\'extra_specs\'] and defaults are not set\n\n    """'
newline|'\n'
name|'image_info'
op|'='
op|'{'
nl|'\n'
string|"'kernel'"
op|':'
op|'['
name|'None'
op|','
name|'None'
op|']'
op|','
nl|'\n'
string|"'ramdisk'"
op|':'
op|'['
name|'None'
op|','
name|'None'
op|']'
op|','
nl|'\n'
string|"'deploy_kernel'"
op|':'
op|'['
name|'None'
op|','
name|'None'
op|']'
op|','
nl|'\n'
string|"'deploy_ramdisk'"
op|':'
op|'['
name|'None'
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'image_info'
op|'['
string|"'kernel'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
string|"'kernel_id'"
op|']'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'ramdisk'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
string|"'ramdisk_id'"
op|']'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'deploy_kernel'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'get_deploy_aki_id'
op|'('
name|'flavor'
op|')'
newline|'\n'
name|'image_info'
op|'['
string|"'deploy_ramdisk'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'get_deploy_ari_id'
op|'('
name|'flavor'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'missing_labels'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'label'
name|'in'
name|'image_info'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'uuid'
op|','
name|'path'
op|')'
op|'='
name|'image_info'
op|'['
name|'label'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'uuid'
op|':'
newline|'\n'
indent|'            '
name|'missing_labels'
op|'.'
name|'append'
op|'('
name|'label'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image_info'
op|'['
name|'label'
op|']'
op|'['
number|'1'
op|']'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'label'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'missing_labels'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"Can not activate PXE bootloader. The following boot parameters "'
nl|'\n'
string|'"were not passed to baremetal driver: %s"'
op|')'
op|'%'
name|'missing_labels'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'image_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PXE
dedent|''
name|'class'
name|'PXE'
op|'('
name|'base'
op|'.'
name|'NodeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""PXE bare metal driver."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PXE'
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
DECL|member|_collect_mac_addresses
dedent|''
name|'def'
name|'_collect_mac_addresses'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'macs'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'nic'
name|'in'
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
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'nic'
op|'['
string|"'address'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'macs'
op|'.'
name|'add'
op|'('
name|'nic'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'sorted'
op|'('
name|'macs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cache_tftp_images
dedent|''
name|'def'
name|'_cache_tftp_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch the necessary kernels and ramdisks for the instance."""'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Fetching kernel and ramdisk for instance %s"'
op|')'
op|'%'
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'label'
name|'in'
name|'image_info'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'uuid'
op|','
name|'path'
op|')'
op|'='
name|'image_info'
op|'['
name|'label'
op|']'
newline|'\n'
name|'bm_utils'
op|'.'
name|'cache_image'
op|'('
nl|'\n'
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'target'
op|'='
name|'path'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'uuid'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cache_image
dedent|''
dedent|''
name|'def'
name|'_cache_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch the instance\'s image from Glance\n\n        This method pulls the relevant AMI and associated kernel and ramdisk,\n        and the deploy kernel and ramdisk from Glance, and writes them\n        to the appropriate places on local disk.\n\n        Both sets of kernel and ramdisk are needed for PXE booting, so these\n        are stored under CONF.baremetal.tftp_root.\n\n        At present, the AMI is cached and certain files are injected.\n        Debian/ubuntu-specific assumptions are made regarding the injected\n        files. In a future revision, this functionality will be replaced by a\n        more scalable and os-agnostic approach: the deployment ramdisk will\n        fetch from Glance directly, and write its own last-mile configuration.\n\n        """'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'get_image_dir_path'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
name|'image_path'
op|'='
name|'get_image_file_path'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Fetching image %(ami)s for instance %(name)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'ami'"
op|':'
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|','
string|"'name'"
op|':'
name|'instance'
op|'['
string|"'name'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'cache_image'
op|'('
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'target'
op|'='
name|'image_path'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|','
name|'image_path'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_inject_into_image
dedent|''
name|'def'
name|'_inject_into_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
name|'admin_password'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Inject last-mile configuration into instances image\n\n        Much of this method is a hack around DHCP and cloud-init\n        not working together with baremetal provisioning yet.\n\n        """'
newline|'\n'
comment|"# NOTE(deva): We assume that if we're not using a kernel,"
nl|'\n'
comment|'#             then the target partition is the first partition'
nl|'\n'
name|'partition'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|'['
string|"'kernel_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'partition'
op|'='
string|'"1"'
newline|'\n'
nl|'\n'
dedent|''
name|'ssh_key'
op|'='
name|'None'
newline|'\n'
name|'if'
string|"'key_data'"
name|'in'
name|'instance'
name|'and'
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'ssh_key'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'injected_files'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'injected_files'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(deva): copy so we dont modify the original'
nl|'\n'
indent|'            '
name|'injected_files'
op|'='
name|'list'
op|'('
name|'injected_files'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'net_config'
op|'='
name|'build_network_config'
op|'('
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'injected_files'
op|'.'
name|'append'
op|'('
op|'('
string|"'/etc/hostname'"
op|','
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Injecting files into image for instance %(name)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'instance'
op|'['
string|"'name'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'bm_utils'
op|'.'
name|'inject_into_image'
op|'('
nl|'\n'
name|'image'
op|'='
name|'get_image_file_path'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
name|'key'
op|'='
name|'ssh_key'
op|','
nl|'\n'
name|'net'
op|'='
name|'net_config'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'utils'
op|'.'
name|'instance_meta'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'partition'
op|'='
name|'partition'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cache_images
dedent|''
name|'def'
name|'cache_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Prepare all the images for this instance."""'
newline|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'flavor_get'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
name|'tftp_image_info'
op|'='
name|'get_tftp_image_info'
op|'('
name|'instance'
op|','
name|'flavor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cache_tftp_images'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'tftp_image_info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_cache_image'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'use_file_injection'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_inject_into_image'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'admin_password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy_images
dedent|''
dedent|''
name|'def'
name|'destroy_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete instance\'s image file."""'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'get_image_file_path'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'rmtree_without_raise'
op|'('
name|'get_image_dir_path'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dhcp_options_for_instance
dedent|''
name|'def'
name|'dhcp_options_for_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'{'
string|"'opt_name'"
op|':'
string|"'bootfile-name'"
op|','
nl|'\n'
string|"'opt_value'"
op|':'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_bootfile_name'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'opt_name'"
op|':'
string|"'server-ip-address'"
op|','
nl|'\n'
string|"'opt_value'"
op|':'
name|'CONF'
op|'.'
name|'my_ip'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'opt_name'"
op|':'
string|"'tftp-server'"
op|','
nl|'\n'
string|"'opt_value'"
op|':'
name|'CONF'
op|'.'
name|'my_ip'
op|'}'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|activate_bootloader
dedent|''
name|'def'
name|'activate_bootloader'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Configure PXE boot loader for an instance\n\n        Kernel and ramdisk images are downloaded by cache_tftp_images,\n        and stored in /tftpboot/{uuid}/\n\n        This method writes the instances config file, and then creates\n        symlinks for each MAC address in the instance.\n\n        By default, the complete layout looks like this:\n\n        /tftpboot/\n            ./{uuid}/\n                 kernel\n                 ramdisk\n                 deploy_kernel\n                 deploy_ramdisk\n                 config\n            ./pxelinux.cfg/\n                 {mac} -> ../{uuid}/config\n        """'
newline|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'flavor_get'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
name|'image_info'
op|'='
name|'get_tftp_image_info'
op|'('
name|'instance'
op|','
name|'flavor'
op|')'
newline|'\n'
op|'('
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|')'
op|'='
name|'get_partition_sizes'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'pxe_config_file_path'
op|'='
name|'get_pxe_config_file_path'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'image_file_path'
op|'='
name|'get_image_file_path'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'deployment_key'
op|'='
name|'bm_utils'
op|'.'
name|'random_alnum'
op|'('
number|'32'
op|')'
newline|'\n'
name|'deployment_iscsi_iqn'
op|'='
string|'"iqn-%s"'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
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
nl|'\n'
op|'{'
string|"'deploy_key'"
op|':'
name|'deployment_key'
op|','
nl|'\n'
string|"'image_path'"
op|':'
name|'image_file_path'
op|','
nl|'\n'
string|"'pxe_config_path'"
op|':'
name|'pxe_config_file_path'
op|','
nl|'\n'
string|"'root_mb'"
op|':'
name|'root_mb'
op|','
nl|'\n'
string|"'swap_mb'"
op|':'
name|'swap_mb'
op|','
nl|'\n'
string|"'ephemeral_mb'"
op|':'
name|'ephemeral_mb'
op|'}'
op|')'
newline|'\n'
name|'pxe_config'
op|'='
name|'build_pxe_config'
op|'('
nl|'\n'
name|'node'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'deployment_key'
op|','
nl|'\n'
name|'deployment_iscsi_iqn'
op|','
nl|'\n'
name|'image_info'
op|'['
string|"'deploy_kernel'"
op|']'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'image_info'
op|'['
string|"'deploy_ramdisk'"
op|']'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'image_info'
op|'['
string|"'kernel'"
op|']'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'image_info'
op|'['
string|"'ramdisk'"
op|']'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'write_to_file'
op|'('
name|'pxe_config_file_path'
op|','
name|'pxe_config'
op|')'
newline|'\n'
nl|'\n'
name|'macs'
op|'='
name|'self'
op|'.'
name|'_collect_mac_addresses'
op|'('
name|'context'
op|','
name|'node'
op|')'
newline|'\n'
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'            '
name|'mac_path'
op|'='
name|'get_pxe_mac_path'
op|'('
name|'mac'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'mac_path'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'create_link_without_raise'
op|'('
name|'pxe_config_file_path'
op|','
name|'mac_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deactivate_bootloader
dedent|''
dedent|''
name|'def'
name|'deactivate_bootloader'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete PXE bootloader images and config."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
op|'{'
string|"'deploy_key'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'image_path'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pxe_config_path'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'root_mb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'swap_mb'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NodeNotFound'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): the flavor extra_specs do not need to be'
nl|'\n'
comment|'# present/correct at deactivate time, so pass something empty'
nl|'\n'
comment|'# to avoid an extra lookup'
nl|'\n'
dedent|''
name|'flavor'
op|'='
name|'dict'
op|'('
name|'extra_specs'
op|'='
op|'{'
nl|'\n'
string|"'baremetal:deploy_ramdisk_id'"
op|':'
string|"'ignore'"
op|','
nl|'\n'
string|"'baremetal:deploy_kernel_id'"
op|':'
string|"'ignore'"
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image_info'
op|'='
name|'get_tftp_image_info'
op|'('
name|'instance'
op|','
name|'flavor'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NovaException'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'label'
name|'in'
name|'image_info'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'uuid'
op|','
name|'path'
op|')'
op|'='
name|'image_info'
op|'['
name|'label'
op|']'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'get_pxe_config_file_path'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'macs'
op|'='
name|'self'
op|'.'
name|'_collect_mac_addresses'
op|'('
name|'context'
op|','
name|'node'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'db_exc'
op|'.'
name|'DBError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'                '
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'get_pxe_mac_path'
op|'('
name|'mac'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bm_utils'
op|'.'
name|'rmtree_without_raise'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|activate_node
dedent|''
name|'def'
name|'activate_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait for PXE deployment to complete."""'
newline|'\n'
nl|'\n'
name|'locals'
op|'='
op|'{'
string|"'error'"
op|':'
string|"''"
op|','
string|"'started'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_wait_for_deploy
name|'def'
name|'_wait_for_deploy'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Called at an interval until the deployment completes."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'row'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'!='
name|'row'
op|'.'
name|'get'
op|'('
string|"'instance_uuid'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'locals'
op|'['
string|"'error'"
op|']'
op|'='
name|'_'
op|'('
string|'"Node associated with another instance"'
nl|'\n'
string|'" while waiting for deploy of %s"'
op|')'
newline|'\n'
name|'raise'
name|'loopingcall'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'status'
op|'='
name|'row'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|')'
newline|'\n'
name|'if'
op|'('
name|'status'
op|'=='
name|'baremetal_states'
op|'.'
name|'DEPLOYING'
nl|'\n'
name|'and'
name|'locals'
op|'['
string|"'started'"
op|']'
op|'=='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"PXE deploy started for instance %s"'
op|')'
nl|'\n'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'locals'
op|'['
string|"'started'"
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'status'
name|'in'
op|'('
name|'baremetal_states'
op|'.'
name|'DEPLOYDONE'
op|','
nl|'\n'
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"PXE deploy completed for instance %s"'
op|')'
nl|'\n'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'raise'
name|'loopingcall'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'status'
op|'=='
name|'baremetal_states'
op|'.'
name|'DEPLOYFAIL'
op|':'
newline|'\n'
indent|'                    '
name|'locals'
op|'['
string|"'error'"
op|']'
op|'='
name|'_'
op|'('
string|'"PXE deploy failed for instance %s"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NodeNotFound'
op|':'
newline|'\n'
indent|'                '
name|'locals'
op|'['
string|"'error'"
op|']'
op|'='
name|'_'
op|'('
string|'"Baremetal node deleted while waiting "'
nl|'\n'
string|'"for deployment of instance %s"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_deploy_timeout'
name|'and'
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'>'
name|'expiration'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'locals'
op|'['
string|"'error'"
op|']'
op|'='
name|'_'
op|'('
string|'"Timeout reached while waiting for "'
nl|'\n'
string|'"PXE deploy of instance %s"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'locals'
op|'['
string|"'error'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'loopingcall'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'expiration'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'+'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
nl|'\n'
name|'seconds'
op|'='
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'pxe_deploy_timeout'
op|')'
newline|'\n'
name|'timer'
op|'='
name|'loopingcall'
op|'.'
name|'FixedIntervalLoopingCall'
op|'('
name|'_wait_for_deploy'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'1'
op|')'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'locals'
op|'['
string|"'error'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
nl|'\n'
name|'locals'
op|'['
string|"'error'"
op|']'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deactivate_node
dedent|''
dedent|''
name|'def'
name|'deactivate_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
