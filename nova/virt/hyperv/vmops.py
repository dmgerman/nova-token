begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Cloud.com, Inc'
nl|'\n'
comment|'# Copyright 2012 Cloudbase Solutions Srl'
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
string|'"""\nManagement class for basic VM operations.\n"""'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'os'
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
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'base'
name|'as'
name|'instance_metadata'
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
name|'excutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
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
name|'configdrive'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'imagecache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeops'
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
DECL|variable|hyperv_opts
name|'hyperv_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'limit_cpu_features'"
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
string|"'Required for live migration among '"
nl|'\n'
string|"'hosts with different CPU features'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'config_drive_inject_password'"
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
string|"'Sets the admin password in the config drive image'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qemu_img_cmd'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"qemu-img.exe"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'qemu-img is used to convert between '"
nl|'\n'
string|"'different image types'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'config_drive_cdrom'"
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
string|"'Attaches the Config Drive image as a cdrom drive '"
nl|'\n'
string|"'instead of a disk drive'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enable_instance_metrics_collection'"
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
string|"'Enables metrics collections for an instance by using '"
nl|'\n'
string|"'Hyper-V\\'s metric APIs. Collected data can by retrieved '"
nl|'\n'
string|"'by other apps and services, e.g.: Ceilometer. '"
nl|'\n'
string|"'Requires Hyper-V / Windows Server 2012 and above'"
op|')'
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
name|'hyperv_opts'
op|','
string|"'hyperv'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_cow_images'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'network_api_class'"
op|','
string|"'nova.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_admin_permissions
name|'def'
name|'check_admin_permissions'
op|'('
name|'function'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'function'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Make sure the windows account has the required admin permissions.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_admin_permissions'
op|'('
op|')'
newline|'\n'
name|'return'
name|'function'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOps
dedent|''
name|'class'
name|'VMOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|_vif_driver_class_map
indent|'    '
name|'_vif_driver_class_map'
op|'='
op|'{'
nl|'\n'
string|"'nova.network.neutronv2.api.API'"
op|':'
nl|'\n'
string|"'nova.virt.hyperv.vif.HyperVNeutronVIFDriver'"
op|','
nl|'\n'
string|"'nova.network.api.API'"
op|':'
nl|'\n'
string|"'nova.virt.hyperv.vif.HyperVNovaNetworkVIFDriver'"
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vhdutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_pathutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'='
name|'imagecache'
op|'.'
name|'ImageCache'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vif_driver'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_load_vif_driver_class'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_vif_driver_class
dedent|''
name|'def'
name|'_load_vif_driver_class'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'class_name'
op|'='
name|'self'
op|'.'
name|'_vif_driver_class_map'
op|'['
name|'CONF'
op|'.'
name|'network_api_class'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_vif_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'class_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'TypeError'
op|'('
name|'_'
op|'('
string|'"VIF driver not found for "'
nl|'\n'
string|'"network_api_class: %s"'
op|')'
op|'%'
nl|'\n'
name|'CONF'
op|'.'
name|'network_api_class'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'list_instances'
op|'('
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
indent|'        '
string|'"""Get information about the VM."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"get_info called for instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'vm_exists'
op|'('
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_summary_info'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'state'
op|'='
name|'constants'
op|'.'
name|'HYPERV_POWER_STATE'
op|'['
name|'info'
op|'['
string|"'EnabledState'"
op|']'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'info'
op|'['
string|"'MemoryUsage'"
op|']'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'info'
op|'['
string|"'MemoryUsage'"
op|']'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'info'
op|'['
string|"'NumberOfProcessors'"
op|']'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
name|'info'
op|'['
string|"'UpTime'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_create_root_vhd
dedent|''
name|'def'
name|'_create_root_vhd'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_vhd_path'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'get_cached_image'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'root_vhd_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_vhd_path'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'use_cow_images'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Creating differencing VHD. Parent: "'
nl|'\n'
string|'"%(base_vhd_path)s, Target: %(root_vhd_path)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_path'"
op|':'
name|'base_vhd_path'
op|','
nl|'\n'
string|"'root_vhd_path'"
op|':'
name|'root_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'create_differencing_vhd'
op|'('
name|'root_vhd_path'
op|','
nl|'\n'
name|'base_vhd_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Copying VHD image %(base_vhd_path)s to target: "'
nl|'\n'
string|'"%(root_vhd_path)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_path'"
op|':'
name|'base_vhd_path'
op|','
nl|'\n'
string|"'root_vhd_path'"
op|':'
name|'root_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'('
name|'base_vhd_path'
op|','
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'base_vhd_info'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'('
name|'base_vhd_path'
op|')'
newline|'\n'
name|'base_vhd_size'
op|'='
name|'base_vhd_info'
op|'['
string|"'MaxInternalSize'"
op|']'
newline|'\n'
name|'root_vhd_size'
op|'='
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'*'
number|'1024'
op|'**'
number|'3'
newline|'\n'
nl|'\n'
name|'if'
name|'root_vhd_size'
op|'<'
name|'base_vhd_size'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'"Cannot resize a VHD to a "'
nl|'\n'
string|'"smaller size"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'root_vhd_size'
op|'>'
name|'base_vhd_size'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Resizing VHD %(root_vhd_path)s to new "'
nl|'\n'
string|'"size %(root_vhd_size)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'base_vhd_path'"
op|':'
name|'base_vhd_path'
op|','
nl|'\n'
string|"'root_vhd_path'"
op|':'
name|'root_vhd_path'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'resize_vhd'
op|'('
name|'root_vhd_path'
op|','
name|'root_vhd_size'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'('
name|'root_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'remove'
op|'('
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'root_vhd_path'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_admin_permissions'
newline|'\n'
DECL|member|spawn
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
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new VM and start it."""'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Spawning new instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'vm_exists'
op|'('
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceExists'
op|'('
name|'name'
op|'='
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
comment|"# Make sure we're starting with a clean slate."
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_delete_disk_files'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_vhd_path'
op|'='
name|'self'
op|'.'
name|'_create_root_vhd'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'create_instance'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'root_vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'configdrive'
op|'.'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_create_config_drive'
op|'('
name|'instance'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|"'Spawn instance failed'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|','
name|'root_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'create_vm'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'limit_cpu_features'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'root_vhd_path'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'attach_ide_drive'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'root_vhd_path'
op|','
nl|'\n'
number|'0'
op|','
nl|'\n'
number|'0'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'IDE_DISK'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'create_scsi_controller'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volumes'
op|'('
name|'block_device_info'
op|','
nl|'\n'
name|'instance_name'
op|','
nl|'\n'
name|'root_vhd_path'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating nic for instance: %s'"
op|')'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'create_nic'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'vif'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vif_driver'
op|'.'
name|'plug'
op|'('
name|'instance'
op|','
name|'vif'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'enable_instance_metrics_collection'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'enable_vm_metrics_collection'
op|'('
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_config_drive
dedent|''
dedent|''
name|'def'
name|'_create_config_drive'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'injected_files'
op|','
name|'admin_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'config_drive_format'
op|'!='
string|"'iso9660'"
op|':'
newline|'\n'
indent|'            '
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|'\'Invalid config_drive_format "%s"\''
op|')'
op|'%'
nl|'\n'
name|'CONF'
op|'.'
name|'config_drive_format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Using config drive for instance: %s'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'extra_md'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'admin_password'
name|'and'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'config_drive_inject_password'
op|':'
newline|'\n'
indent|'            '
name|'extra_md'
op|'['
string|"'admin_pass'"
op|']'
op|'='
name|'admin_password'
newline|'\n'
nl|'\n'
dedent|''
name|'inst_md'
op|'='
name|'instance_metadata'
op|'.'
name|'InstanceMetadata'
op|'('
name|'instance'
op|','
nl|'\n'
name|'content'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'extra_md'
op|'='
name|'extra_md'
op|')'
newline|'\n'
nl|'\n'
name|'instance_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'configdrive_path_iso'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instance_path'
op|','
string|"'configdrive.iso'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Creating config drive at %(path)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'configdrive_path_iso'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'configdrive'
op|'.'
name|'ConfigDriveBuilder'
op|'('
name|'instance_md'
op|'='
name|'inst_md'
op|')'
name|'as'
name|'cdb'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cdb'
op|'.'
name|'make_drive'
op|'('
name|'configdrive_path_iso'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Creating config drive failed with error: %s'"
op|')'
op|','
nl|'\n'
name|'e'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'config_drive_cdrom'
op|':'
newline|'\n'
indent|'            '
name|'drive_type'
op|'='
name|'constants'
op|'.'
name|'IDE_DISK'
newline|'\n'
name|'configdrive_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instance_path'
op|','
nl|'\n'
string|"'configdrive.vhd'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'qemu_img_cmd'
op|','
nl|'\n'
string|"'convert'"
op|','
nl|'\n'
string|"'-f'"
op|','
nl|'\n'
string|"'raw'"
op|','
nl|'\n'
string|"'-O'"
op|','
nl|'\n'
string|"'vpc'"
op|','
nl|'\n'
name|'configdrive_path_iso'
op|','
nl|'\n'
name|'configdrive_path'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'remove'
op|'('
name|'configdrive_path_iso'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'drive_type'
op|'='
name|'constants'
op|'.'
name|'IDE_DVD'
newline|'\n'
name|'configdrive_path'
op|'='
name|'configdrive_path_iso'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'attach_ide_drive'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'configdrive_path'
op|','
nl|'\n'
number|'1'
op|','
number|'0'
op|','
name|'drive_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_disconnect_volumes
dedent|''
name|'def'
name|'_disconnect_volumes'
op|'('
name|'self'
op|','
name|'volume_drives'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'volume_drive'
name|'in'
name|'volume_drives'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'disconnect_volume'
op|'('
name|'volume_drive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_disk_files
dedent|''
dedent|''
name|'def'
name|'_delete_disk_files'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'create_dir'
op|'='
name|'False'
op|','
nl|'\n'
name|'remove_dir'
op|'='
name|'True'
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
op|'='
name|'None'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Got request to destroy instance: %s"'
op|')'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'vm_exists'
op|'('
name|'instance_name'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'#Stop the VM first.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'storage'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_storage_paths'
op|'('
name|'instance_name'
op|')'
newline|'\n'
op|'('
name|'disk_files'
op|','
name|'volume_drives'
op|')'
op|'='
name|'storage'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'destroy_vm'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_disconnect_volumes'
op|'('
name|'volume_drives'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance not found: %s"'
op|')'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'destroy_disks'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_delete_disk_files'
op|'('
name|'instance_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|"'Failed to destroy instance: %s'"
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot the specified instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"reboot instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_REBOOT'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Pause instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_PAUSED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unpause paused VM instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Unpause instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Suspend the specified instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Suspend instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_SUSPENDED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resume the suspended VM instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Resume instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Power off instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_DISABLED'
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
string|'"""Power on the specified instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Power on instance"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_vm_state'
op|'('
name|'instance'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_vm_state
dedent|''
name|'def'
name|'_set_vm_state'
op|'('
name|'self'
op|','
name|'vm_name'
op|','
name|'req_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'set_vm_state'
op|'('
name|'vm_name'
op|','
name|'req_state'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Successfully changed state of VM %(vm_name)s"'
nl|'\n'
string|'" to: %(req_state)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'vm_name'"
op|':'
name|'vm_name'
op|','
string|"'req_state'"
op|':'
name|'req_state'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Failed to change vm state of %(vm_name)s"'
nl|'\n'
string|'" to %(req_state)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'vm_name'"
op|':'
name|'vm_name'
op|','
string|"'req_state'"
op|':'
name|'req_state'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
