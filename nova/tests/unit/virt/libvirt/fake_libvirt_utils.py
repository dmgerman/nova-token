begin_unit
comment|'#    Copyright (c) 2011 OpenStack Foundation'
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
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
nl|'\n'
DECL|variable|files
name|'files'
op|'='
op|'{'
string|"'console.log'"
op|':'
name|'True'
op|'}'
newline|'\n'
DECL|variable|disk_sizes
name|'disk_sizes'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|disk_backing_files
name|'disk_backing_files'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|disk_type
name|'disk_type'
op|'='
string|'"qcow2"'
newline|'\n'
nl|'\n'
DECL|variable|RESIZE_SNAPSHOT_NAME
name|'RESIZE_SNAPSHOT_NAME'
op|'='
name|'libvirt_utils'
op|'.'
name|'RESIZE_SNAPSHOT_NAME'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
name|'def'
name|'create_image'
op|'('
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_cow_image
dedent|''
name|'def'
name|'create_cow_image'
op|'('
name|'backing_file'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_size
dedent|''
name|'def'
name|'get_disk_size'
op|'('
name|'path'
op|','
name|'format'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_backing_file
dedent|''
name|'def'
name|'get_disk_backing_file'
op|'('
name|'path'
op|','
name|'format'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'disk_backing_files'
op|'.'
name|'get'
op|'('
name|'path'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_type_from_path
dedent|''
name|'def'
name|'get_disk_type_from_path'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'disk_type'
name|'in'
op|'('
string|"'raw'"
op|','
string|"'qcow2'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'disk_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|copy_image
dedent|''
name|'def'
name|'copy_image'
op|'('
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|resize2fs
dedent|''
name|'def'
name|'resize2fs'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_lvm_image
dedent|''
name|'def'
name|'create_lvm_image'
op|'('
name|'vg'
op|','
name|'lv'
op|','
name|'size'
op|','
name|'sparse'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_group_free_space
dedent|''
name|'def'
name|'volume_group_free_space'
op|'('
name|'vg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_logical_volumes
dedent|''
name|'def'
name|'remove_logical_volumes'
op|'('
op|'*'
name|'paths'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
name|'def'
name|'write_to_file'
op|'('
name|'path'
op|','
name|'contents'
op|','
name|'umask'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown
dedent|''
name|'def'
name|'chown'
op|'('
name|'path'
op|','
name|'owner'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_snapshot
dedent|''
name|'def'
name|'extract_snapshot'
op|'('
name|'disk_path'
op|','
name|'source_fmt'
op|','
name|'out_path'
op|','
name|'dest_fmt'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'files'
op|'['
name|'out_path'
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|File
dedent|''
name|'class'
name|'File'
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
name|'path'
op|','
name|'mode'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fp'
op|'='
name|'StringIO'
op|'('
name|'files'
op|'['
name|'path'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fp'
op|'='
name|'StringIO'
op|'('
name|'files'
op|'['
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'path'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'fp'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
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
name|'self'
op|'.'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_open
dedent|''
dedent|''
name|'def'
name|'file_open'
op|'('
name|'path'
op|','
name|'mode'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'File'
op|'('
name|'path'
op|','
name|'mode'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_disk
dedent|''
name|'def'
name|'find_disk'
op|'('
name|'virt_dom'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'disk_type'
op|'=='
string|"'lvm'"
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"/dev/nova-vg/lv"'
op|','
string|'"raw"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'disk_type'
name|'in'
op|'['
string|"'raw'"
op|','
string|"'qcow2'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"filename"'
op|','
name|'disk_type'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"unknown_type_disk"'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_file
dedent|''
dedent|''
name|'def'
name|'load_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'r'"
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fp'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|logical_volume_info
dedent|''
dedent|''
name|'def'
name|'logical_volume_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fs_info
dedent|''
name|'def'
name|'get_fs_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'total'"
op|':'
number|'128'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|','
nl|'\n'
string|"'used'"
op|':'
number|'44'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|','
nl|'\n'
string|"'free'"
op|':'
number|'84'
op|'*'
op|'('
number|'1024'
op|'**'
number|'3'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image
dedent|''
name|'def'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'image_id'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_raw_image
dedent|''
name|'def'
name|'fetch_raw_image'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'image_id'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_path
dedent|''
name|'def'
name|'get_instance_path'
op|'('
name|'instance'
op|','
name|'forceold'
op|'='
name|'False'
op|','
name|'relative'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'libvirt_utils'
op|'.'
name|'get_instance_path'
op|'('
name|'instance'
op|','
name|'forceold'
op|'='
name|'forceold'
op|','
nl|'\n'
name|'relative'
op|'='
name|'relative'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_path_at_destination
dedent|''
name|'def'
name|'get_instance_path_at_destination'
op|'('
name|'instance'
op|','
name|'migrate_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'libvirt_utils'
op|'.'
name|'get_instance_path_at_destination'
op|'('
name|'instance'
op|','
nl|'\n'
name|'migrate_data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pick_disk_driver_name
dedent|''
name|'def'
name|'pick_disk_driver_name'
op|'('
name|'hypervisor_version'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"qemu"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid_hostname
dedent|''
name|'def'
name|'is_valid_hostname'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown_for_id_maps
dedent|''
name|'def'
name|'chown_for_id_maps'
op|'('
name|'path'
op|','
name|'id_maps'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_arch
dedent|''
name|'def'
name|'get_arch'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'libvirt_utils'
op|'.'
name|'get_arch'
op|'('
name|'image_meta'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
