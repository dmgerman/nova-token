begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Grid Dynamics'
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
name|'import'
name|'abc'
newline|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'excutils'
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
name|'disk'
name|'import'
name|'api'
name|'as'
name|'disk'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
newline|'\n'
nl|'\n'
DECL|variable|__imagebackend_opts
name|'__imagebackend_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'libvirt_images_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'default'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'VM Images format. Acceptable values are: raw, qcow2, lvm,'"
nl|'\n'
string|"' default. If default is specified,'"
nl|'\n'
string|"' then use_cow_images flag is used instead of this one.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'libvirt_images_volume_group'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'LVM Volume Group that is used for VM images, when you'"
nl|'\n'
string|"' specify libvirt_images_type=lvm.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'libvirt_sparse_logical_volumes'"
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
string|"'Create sparse logical volumes (with virtualsize)'"
nl|'\n'
string|"' if this flag is set to True.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'__imagebackend_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Image
name|'class'
name|'Image'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|__metaclass__
indent|'    '
name|'__metaclass__'
op|'='
name|'abc'
op|'.'
name|'ABCMeta'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'source_type'
op|','
name|'driver_format'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Image initialization.\n\n        :source_type: block or file\n        :driver_format: raw or qcow2\n        :is_block_dev:\n        """'
newline|'\n'
name|'self'
op|'.'
name|'source_type'
op|'='
name|'source_type'
newline|'\n'
name|'self'
op|'.'
name|'driver_format'
op|'='
name|'driver_format'
newline|'\n'
name|'self'
op|'.'
name|'is_block_dev'
op|'='
name|'is_block_dev'
newline|'\n'
nl|'\n'
comment|'# NOTE(mikal): We need a lock directory which is shared along with'
nl|'\n'
comment|'# instance files, to cover the scenario where multiple compute nodes'
nl|'\n'
comment|'# are trying to create a base file at the same time'
nl|'\n'
name|'self'
op|'.'
name|'lock_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
string|"'locks'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|create_image
name|'def'
name|'create_image'
op|'('
name|'self'
op|','
name|'prepare_template'
op|','
name|'base'
op|','
name|'size'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create image from template.\n\n        Contains specific behavior for each image type.\n\n        :prepare_template: function, that creates template.\n        Should accept `target` argument.\n        :base: Template name\n        :size: Size of created image in bytes\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|libvirt_info
dedent|''
name|'def'
name|'libvirt_info'
op|'('
name|'self'
op|','
name|'disk_bus'
op|','
name|'disk_dev'
op|','
name|'device_type'
op|','
name|'cache_mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get `LibvirtConfigGuestDisk` filled for this image.\n\n        :disk_dev: Disk bus device name\n        :disk_bus: Disk bus type\n        :device_type: Device type for this image.\n        :cache_mode: Caching mode for this image\n        """'
newline|'\n'
name|'info'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'info'
op|'.'
name|'source_type'
op|'='
name|'self'
op|'.'
name|'source_type'
newline|'\n'
name|'info'
op|'.'
name|'source_device'
op|'='
name|'device_type'
newline|'\n'
name|'info'
op|'.'
name|'target_bus'
op|'='
name|'disk_bus'
newline|'\n'
name|'info'
op|'.'
name|'target_dev'
op|'='
name|'disk_dev'
newline|'\n'
name|'info'
op|'.'
name|'driver_cache'
op|'='
name|'cache_mode'
newline|'\n'
name|'info'
op|'.'
name|'driver_format'
op|'='
name|'self'
op|'.'
name|'driver_format'
newline|'\n'
name|'driver_name'
op|'='
name|'libvirt_utils'
op|'.'
name|'pick_disk_driver_name'
op|'('
name|'self'
op|'.'
name|'is_block_dev'
op|')'
newline|'\n'
name|'info'
op|'.'
name|'driver_name'
op|'='
name|'driver_name'
newline|'\n'
name|'info'
op|'.'
name|'source_path'
op|'='
name|'self'
op|'.'
name|'path'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
DECL|member|cache
dedent|''
name|'def'
name|'cache'
op|'('
name|'self'
op|','
name|'fn'
op|','
name|'fname'
op|','
name|'size'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates image from template.\n\n        Ensures that template and image not already exists.\n        Ensures that base directory exists.\n        Synchronizes on template fetching.\n\n        :fn: function, that creates template.\n        Should accept `target` argument.\n        :fname: Template name\n        :size: Size of created image in bytes (optional)\n        """'
newline|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'fname'
op|','
name|'external'
op|'='
name|'True'
op|','
name|'lock_path'
op|'='
name|'self'
op|'.'
name|'lock_path'
op|')'
newline|'\n'
DECL|function|call_if_not_exists
name|'def'
name|'call_if_not_exists'
op|'('
name|'target'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'fn'
op|'('
name|'target'
op|'='
name|'target'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
string|"'_base'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'ensure_tree'
op|'('
name|'base_dir'
op|')'
newline|'\n'
dedent|''
name|'base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'fname'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'create_image'
op|'('
name|'call_if_not_exists'
op|','
name|'base'
op|','
name|'size'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Raw
dedent|''
dedent|''
dedent|''
name|'class'
name|'Raw'
op|'('
name|'Image'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Raw'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|'"file"'
op|','
string|'"raw"'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_image
dedent|''
name|'def'
name|'create_image'
op|'('
name|'self'
op|','
name|'prepare_template'
op|','
name|'base'
op|','
name|'size'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'base'
op|','
name|'external'
op|'='
name|'True'
op|','
name|'lock_path'
op|'='
name|'self'
op|'.'
name|'lock_path'
op|')'
newline|'\n'
DECL|function|copy_raw_image
name|'def'
name|'copy_raw_image'
op|'('
name|'base'
op|','
name|'target'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'libvirt_utils'
op|'.'
name|'copy_image'
op|'('
name|'base'
op|','
name|'target'
op|')'
newline|'\n'
name|'if'
name|'size'
op|':'
newline|'\n'
indent|'                '
name|'disk'
op|'.'
name|'extend'
op|'('
name|'target'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'generating'
op|'='
string|"'image_id'"
name|'not'
name|'in'
name|'kwargs'
newline|'\n'
name|'if'
name|'generating'
op|':'
newline|'\n'
comment|'#Generating image in place'
nl|'\n'
indent|'            '
name|'prepare_template'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'path'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'prepare_template'
op|'('
name|'target'
op|'='
name|'base'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'copy_raw_image'
op|'('
name|'base'
op|','
name|'self'
op|'.'
name|'path'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Qcow2
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Qcow2'
op|'('
name|'Image'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Qcow2'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|'"file"'
op|','
string|'"qcow2"'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_image
dedent|''
name|'def'
name|'create_image'
op|'('
name|'self'
op|','
name|'prepare_template'
op|','
name|'base'
op|','
name|'size'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'base'
op|','
name|'external'
op|'='
name|'True'
op|','
name|'lock_path'
op|'='
name|'self'
op|'.'
name|'lock_path'
op|')'
newline|'\n'
DECL|function|copy_qcow2_image
name|'def'
name|'copy_qcow2_image'
op|'('
name|'base'
op|','
name|'target'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'qcow2_base'
op|'='
name|'base'
newline|'\n'
name|'if'
name|'size'
op|':'
newline|'\n'
indent|'                '
name|'size_gb'
op|'='
name|'size'
op|'/'
op|'('
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'qcow2_base'
op|'+='
string|"'_%d'"
op|'%'
name|'size_gb'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'qcow2_base'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'with'
name|'utils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'qcow2_base'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'libvirt_utils'
op|'.'
name|'copy_image'
op|'('
name|'base'
op|','
name|'qcow2_base'
op|')'
newline|'\n'
name|'disk'
op|'.'
name|'extend'
op|'('
name|'qcow2_base'
op|','
name|'size'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'libvirt_utils'
op|'.'
name|'create_cow_image'
op|'('
name|'qcow2_base'
op|','
name|'target'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'prepare_template'
op|'('
name|'target'
op|'='
name|'base'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'copy_qcow2_image'
op|'('
name|'base'
op|','
name|'self'
op|'.'
name|'path'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Lvm
dedent|''
dedent|''
dedent|''
name|'class'
name|'Lvm'
op|'('
name|'Image'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|escape
name|'def'
name|'escape'
op|'('
name|'fname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fname'
op|'.'
name|'replace'
op|'('
string|"'_'"
op|','
string|"'__'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Lvm'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|'"block"'
op|','
string|'"raw"'
op|','
name|'is_block_dev'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'libvirt_images_volume_group'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'You should specify'"
nl|'\n'
string|"' libvirt_images_volume_group'"
nl|'\n'
string|"' flag to use LVM images.'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'vg'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_images_volume_group'
newline|'\n'
name|'self'
op|'.'
name|'lv'
op|'='
string|"'%s_%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'escape'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'escape'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'/dev'"
op|','
name|'self'
op|'.'
name|'vg'
op|','
name|'self'
op|'.'
name|'lv'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sparse'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_sparse_logical_volumes'
newline|'\n'
nl|'\n'
DECL|member|create_image
dedent|''
name|'def'
name|'create_image'
op|'('
name|'self'
op|','
name|'prepare_template'
op|','
name|'base'
op|','
name|'size'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'base'
op|','
name|'external'
op|'='
name|'True'
op|','
name|'lock_path'
op|'='
name|'self'
op|'.'
name|'lock_path'
op|')'
newline|'\n'
DECL|function|create_lvm_image
name|'def'
name|'create_lvm_image'
op|'('
name|'base'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_size'
op|'='
name|'disk'
op|'.'
name|'get_disk_size'
op|'('
name|'base'
op|')'
newline|'\n'
name|'resize'
op|'='
name|'size'
op|'>'
name|'base_size'
newline|'\n'
name|'size'
op|'='
name|'size'
name|'if'
name|'resize'
name|'else'
name|'base_size'
newline|'\n'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'vg'
op|','
name|'self'
op|'.'
name|'lv'
op|','
nl|'\n'
name|'size'
op|','
name|'sparse'
op|'='
name|'self'
op|'.'
name|'sparse'
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'dd'"
op|','
string|"'if=%s'"
op|'%'
name|'base'
op|','
string|"'of=%s'"
op|'%'
name|'self'
op|'.'
name|'path'
op|','
string|"'bs=4M'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'resize'
op|':'
newline|'\n'
indent|'                '
name|'disk'
op|'.'
name|'resize2fs'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'generated'
op|'='
string|"'ephemeral_size'"
name|'in'
name|'kwargs'
newline|'\n'
nl|'\n'
comment|'#Generate images with specified size right on volume'
nl|'\n'
name|'if'
name|'generated'
name|'and'
name|'size'
op|':'
newline|'\n'
indent|'            '
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'vg'
op|','
name|'self'
op|'.'
name|'lv'
op|','
nl|'\n'
name|'size'
op|','
name|'sparse'
op|'='
name|'self'
op|'.'
name|'sparse'
op|')'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'remove_volume_on_error'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'prepare_template'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'path'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'prepare_template'
op|'('
name|'target'
op|'='
name|'base'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'remove_volume_on_error'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'create_lvm_image'
op|'('
name|'base'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|member|remove_volume_on_error
name|'def'
name|'remove_volume_on_error'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
newline|'\n'
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
name|'libvirt_utils'
op|'.'
name|'remove_logical_volumes'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Backend
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Backend'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'use_cow'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'BACKEND'
op|'='
op|'{'
nl|'\n'
string|"'raw'"
op|':'
name|'Raw'
op|','
nl|'\n'
string|"'qcow2'"
op|':'
name|'Qcow2'
op|','
nl|'\n'
string|"'lvm'"
op|':'
name|'Lvm'
op|','
nl|'\n'
string|"'default'"
op|':'
name|'Qcow2'
name|'if'
name|'use_cow'
name|'else'
name|'Raw'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|image
dedent|''
name|'def'
name|'image'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|','
nl|'\n'
name|'image_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs image for selected backend\n\n        :instance: Instance name.\n        :name: Image name.\n        :image_type: Image type.\n        Optional, is FLAGS.libvirt_images_type by default.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'image_type'
op|':'
newline|'\n'
indent|'            '
name|'image_type'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_images_type'
newline|'\n'
dedent|''
name|'image'
op|'='
name|'self'
op|'.'
name|'BACKEND'
op|'.'
name|'get'
op|'('
name|'image_type'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'Unknown image_type=%s'"
op|')'
op|'%'
name|'image_type'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'image'
op|'('
name|'instance'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
