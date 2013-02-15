begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2011 OpenStack LLC'
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
name|'import'
name|'StringIO'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
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
nl|'\n'
DECL|function|get_iscsi_initiator
name|'def'
name|'get_iscsi_initiator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"fake.initiator.iqn"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_hbas
dedent|''
name|'def'
name|'get_fc_hbas'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|'{'
string|"'ClassDevice'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'ClassDevicePath'"
op|':'
string|"'/sys/devices/pci0000:00/0000:00:03.0'"
nl|'\n'
string|"'/0000:05:00.2/host1/fc_host/host1'"
op|','
nl|'\n'
string|"'dev_loss_tmo'"
op|':'
string|"'30'"
op|','
nl|'\n'
string|"'fabric_name'"
op|':'
string|"'0x1000000533f55566'"
op|','
nl|'\n'
string|"'issue_lip'"
op|':'
string|"'<store method only>'"
op|','
nl|'\n'
string|"'max_npiv_vports'"
op|':'
string|"'255'"
op|','
nl|'\n'
string|"'maxframe_size'"
op|':'
string|"'2048 bytes'"
op|','
nl|'\n'
string|"'node_name'"
op|':'
string|"'0x200010604b019419'"
op|','
nl|'\n'
string|"'npiv_vports_inuse'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'port_id'"
op|':'
string|"'0x680409'"
op|','
nl|'\n'
string|"'port_name'"
op|':'
string|"'0x100010604b019419'"
op|','
nl|'\n'
string|"'port_state'"
op|':'
string|"'Online'"
op|','
nl|'\n'
string|"'port_type'"
op|':'
string|"'NPort (fabric via point-to-point)'"
op|','
nl|'\n'
string|"'speed'"
op|':'
string|"'10 Gbit'"
op|','
nl|'\n'
string|"'supported_classes'"
op|':'
string|"'Class 3'"
op|','
nl|'\n'
string|"'supported_speeds'"
op|':'
string|"'10 Gbit'"
op|','
nl|'\n'
string|"'symbolic_name'"
op|':'
string|"'Emulex 554M FV4.0.493.0 DV8.3.27'"
op|','
nl|'\n'
string|"'tgtid_bind_type'"
op|':'
string|"'wwpn (World Wide Port Name)'"
op|','
nl|'\n'
string|"'uevent'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vport_create'"
op|':'
string|"'<store method only>'"
op|','
nl|'\n'
string|"'vport_delete'"
op|':'
string|"'<store method only>'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_hbas_info
dedent|''
name|'def'
name|'get_fc_hbas_info'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
name|'info'
op|'='
op|'['
op|'{'
string|"'port_name'"
op|':'
name|'hbas'
op|'['
number|'0'
op|']'
op|'['
string|"'port_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
op|','
nl|'\n'
string|"'node_name'"
op|':'
name|'hbas'
op|'['
number|'0'
op|']'
op|'['
string|"'node_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
op|','
nl|'\n'
string|"'host_device'"
op|':'
name|'hbas'
op|'['
number|'0'
op|']'
op|'['
string|"'ClassDevice'"
op|']'
op|','
nl|'\n'
string|"'device_path'"
op|':'
name|'hbas'
op|'['
number|'0'
op|']'
op|'['
string|"'ClassDevicePath'"
op|']'
op|'}'
op|']'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_wwpns
dedent|''
name|'def'
name|'get_fc_wwpns'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
name|'wwpns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'wwpn'
op|'='
name|'hba'
op|'['
string|"'port_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
name|'wwpns'
op|'.'
name|'append'
op|'('
name|'wwpn'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wwpns'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_wwnns
dedent|''
name|'def'
name|'get_fc_wwnns'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
name|'wwnns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'wwnn'
op|'='
name|'hba'
op|'['
string|"'node_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'wwnns'
op|'.'
name|'append'
op|'('
name|'wwnn'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wwnns'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
dedent|''
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
DECL|function|get_disk_backing_file
dedent|''
name|'def'
name|'get_disk_backing_file'
op|'('
name|'path'
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
DECL|function|get_disk_type
dedent|''
name|'def'
name|'get_disk_type'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
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
DECL|function|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'disk_path'
op|','
name|'snapshot_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
op|'('
name|'disk_path'
op|','
name|'snapshot_name'
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
name|'snapshot_name'
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
op|'.'
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
op|'.'
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
name|'return'
string|'"filename"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_file
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pick_disk_driver_name
dedent|''
name|'def'
name|'pick_disk_driver_name'
op|'('
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
dedent|''
endmarker|''
end_unit
