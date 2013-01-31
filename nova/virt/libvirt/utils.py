begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'#    Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'#    All Rights Reserved.'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'#    Copyright (c) 2011 Piston Cloud Computing, Inc'
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
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'images'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_opts
name|'libvirt_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'libvirt_snapshot_compression'"
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
string|"'Compress snapshot images when possible. This '"
nl|'\n'
string|"'currently applies exclusively to qcow2 images'"
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
name|'libvirt_opts'
op|')'
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
nl|'\n'
DECL|function|execute
name|'def'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_iscsi_initiator
dedent|''
name|'def'
name|'get_iscsi_initiator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get iscsi initiator name for this machine."""'
newline|'\n'
comment|'# NOTE(vish) openiscsi stores initiator name in a file that'
nl|'\n'
comment|'#            needs root permission to read.'
nl|'\n'
name|'contents'
op|'='
name|'utils'
op|'.'
name|'read_file_as_root'
op|'('
string|"'/etc/iscsi/initiatorname.iscsi'"
op|')'
newline|'\n'
name|'for'
name|'l'
name|'in'
name|'contents'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'l'
op|'.'
name|'startswith'
op|'('
string|"'InitiatorName='"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'l'
op|'['
name|'l'
op|'.'
name|'index'
op|'('
string|"'='"
op|')'
op|'+'
number|'1'
op|':'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
dedent|''
dedent|''
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
string|'"""Create a disk image\n\n    :param disk_format: Disk image format (as known by qemu-img)\n    :param path: Desired location of the disk image\n    :param size: Desired size of disk image. May be given as an int or\n                 a string. If given as an int, it will be interpreted\n                 as bytes. If it\'s a string, it should consist of a number\n                 with an optional suffix (\'K\' for Kibibytes,\n                 M for Mebibytes, \'G\' for Gibibytes, \'T\' for Tebibytes).\n                 If no suffix is given, it will be interpreted as bytes.\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
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
op|','
name|'size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create COW image\n\n    Creates a COW image with the given backing file\n\n    :param backing_file: Existing image on which to base the COW image\n    :param path: Desired location of the COW image\n    """'
newline|'\n'
name|'base_cmd'
op|'='
op|'['
string|"'qemu-img'"
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
string|"'qcow2'"
op|']'
newline|'\n'
name|'cow_opts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'backing_file'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'backing_file=%s'"
op|'%'
name|'backing_file'
op|']'
newline|'\n'
name|'base_details'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'backing_file'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'base_details'
op|'='
name|'None'
newline|'\n'
comment|"# This doesn't seem to get inherited so force it to..."
nl|'\n'
comment|'# http://paste.ubuntu.com/1213295/'
nl|'\n'
comment|'# TODO(harlowja) probably file a bug against qemu-img/qemu'
nl|'\n'
dedent|''
name|'if'
name|'base_details'
name|'and'
name|'base_details'
op|'.'
name|'cluster_size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'cluster_size=%s'"
op|'%'
name|'base_details'
op|'.'
name|'cluster_size'
op|']'
newline|'\n'
comment|"# For now don't inherit this due the following discussion..."
nl|'\n'
comment|'# See: http://www.gossamer-threads.com/lists/openstack/dev/10592'
nl|'\n'
comment|"# if 'preallocation' in base_details:"
nl|'\n'
comment|"#     cow_opts += ['preallocation=%s' % base_details['preallocation']]"
nl|'\n'
dedent|''
name|'if'
name|'base_details'
name|'and'
name|'base_details'
op|'.'
name|'encryption'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'encryption=%s'"
op|'%'
name|'base_details'
op|'.'
name|'encryption'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'size=%s'"
op|'%'
name|'size'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'cow_opts'
op|':'
newline|'\n'
comment|'# Format as a comma separated list'
nl|'\n'
indent|'        '
name|'csv_opts'
op|'='
string|'","'
op|'.'
name|'join'
op|'('
name|'cow_opts'
op|')'
newline|'\n'
name|'cow_opts'
op|'='
op|'['
string|"'-o'"
op|','
name|'csv_opts'
op|']'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'base_cmd'
op|'+'
name|'cow_opts'
op|'+'
op|'['
name|'path'
op|']'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|')'
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
string|'"""Create LVM image.\n\n    Creates a LVM image with given size.\n\n    :param vg: existing volume group which should hold this image\n    :param lv: name for this image (logical volume)\n    :size: size of image in bytes\n    :sparse: create sparse logical volume\n    """'
newline|'\n'
name|'free_space'
op|'='
name|'volume_group_free_space'
op|'('
name|'vg'
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_size
name|'def'
name|'check_size'
op|'('
name|'vg'
op|','
name|'lv'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'size'
op|'>'
name|'free_space'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'Insufficient Space on Volume Group %(vg)s.'"
nl|'\n'
string|"' Only %(free_space)db available,'"
nl|'\n'
string|"' but %(size)db required'"
nl|'\n'
string|"' by volume %(lv)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'sparse'
op|':'
newline|'\n'
indent|'        '
name|'preallocated_space'
op|'='
number|'64'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'check_size'
op|'('
name|'vg'
op|','
name|'lv'
op|','
name|'preallocated_space'
op|')'
newline|'\n'
name|'if'
name|'free_space'
op|'<'
name|'size'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Volume group %(vg)s will not be able'"
nl|'\n'
string|"' to hold sparse volume %(lv)s.'"
nl|'\n'
string|"' Virtual volume size is %(size)db,'"
nl|'\n'
string|"' but free space on volume group is'"
nl|'\n'
string|"' only %(free_space)db.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'='
op|'('
string|"'lvcreate'"
op|','
string|"'-L'"
op|','
string|"'%db'"
op|'%'
name|'preallocated_space'
op|','
nl|'\n'
string|"'--virtualsize'"
op|','
string|"'%db'"
op|'%'
name|'size'
op|','
string|"'-n'"
op|','
name|'lv'
op|','
name|'vg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'check_size'
op|'('
name|'vg'
op|','
name|'lv'
op|','
name|'size'
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'lvcreate'"
op|','
string|"'-L'"
op|','
string|"'%db'"
op|'%'
name|'size'
op|','
string|"'-n'"
op|','
name|'lv'
op|','
name|'vg'
op|')'
newline|'\n'
dedent|''
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|','
name|'attempts'
op|'='
number|'3'
op|')'
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
string|'"""Return available space on volume group in bytes.\n\n    :param vg: volume group name\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'vgs'"
op|','
string|"'--noheadings'"
op|','
string|"'--nosuffix'"
op|','
nl|'\n'
string|"'--units'"
op|','
string|"'b'"
op|','
string|"'-o'"
op|','
string|"'vg_free'"
op|','
name|'vg'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_group_total_space
dedent|''
name|'def'
name|'volume_group_total_space'
op|'('
name|'vg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return total space on volume group in bytes.\n\n    :param vg: volume group name\n    """'
newline|'\n'
nl|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'vgs'"
op|','
string|"'--noheadings'"
op|','
string|"'--nosuffix'"
op|','
nl|'\n'
string|"'--units'"
op|','
string|"'b'"
op|','
string|"'-o'"
op|','
string|"'vg_size'"
op|','
name|'vg'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_group_used_space
dedent|''
name|'def'
name|'volume_group_used_space'
op|'('
name|'vg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return available space on volume group in bytes.\n\n    :param vg: volume group name\n    """'
newline|'\n'
nl|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'vgs'"
op|','
string|"'--noheadings'"
op|','
string|"'--nosuffix'"
op|','
nl|'\n'
string|"'--separator'"
op|','
string|"'|'"
op|','
nl|'\n'
string|"'--units'"
op|','
string|"'b'"
op|','
string|"'-o'"
op|','
string|"'vg_size,vg_free'"
op|','
name|'vg'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"'|'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'info'
op|')'
op|'!='
number|'2'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"vg %s must be LVM volume group"'
op|')'
op|'%'
name|'vg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'int'
op|'('
name|'info'
op|'['
number|'0'
op|']'
op|')'
op|'-'
name|'int'
op|'('
name|'info'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_logical_volumes
dedent|''
name|'def'
name|'list_logical_volumes'
op|'('
name|'vg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""List logical volumes paths for given volume group.\n\n    :param vg: volume group name\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'lvs'"
op|','
string|"'--noheadings'"
op|','
string|"'-o'"
op|','
string|"'lv_name'"
op|','
name|'vg'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|logical_volume_info
dedent|''
name|'def'
name|'logical_volume_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get logical volume info.\n\n    :param path: logical volume path\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'lvs'"
op|','
string|"'-o'"
op|','
string|"'vg_all,lv_all'"
op|','
nl|'\n'
string|"'--separator'"
op|','
string|"'|'"
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'['
name|'line'
op|'.'
name|'split'
op|'('
string|"'|'"
op|')'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'info'
op|')'
op|'!='
number|'2'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"Path %s must be LVM logical volume"'
op|')'
op|'%'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'zip'
op|'('
op|'*'
name|'info'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|logical_volume_size
dedent|''
name|'def'
name|'logical_volume_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get logical volume size in bytes.\n\n    :param path: logical volume path\n    """'
newline|'\n'
comment|'# TODO(p-draigbrady) POssibly replace with the more general'
nl|'\n'
comment|'# use of blockdev --getsize64 in future'
nl|'\n'
name|'out'
op|','
name|'_err'
op|'='
name|'execute'
op|'('
string|"'lvs'"
op|','
string|"'-o'"
op|','
string|"'lv_size'"
op|','
string|"'--noheadings'"
op|','
string|"'--units'"
op|','
nl|'\n'
string|"'b'"
op|','
string|"'--nosuffix'"
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'int'
op|'('
name|'out'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clear_logical_volume
dedent|''
name|'def'
name|'clear_logical_volume'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Obfuscate the logical volume.\n\n    :param path: logical volume path\n    """'
newline|'\n'
comment|'# TODO(p-draigbrady): We currently overwrite with zeros'
nl|'\n'
comment|'# but we may want to make this configurable in future'
nl|'\n'
comment|'# for more or less security conscious setups.'
nl|'\n'
nl|'\n'
name|'vol_size'
op|'='
name|'logical_volume_size'
op|'('
name|'path'
op|')'
newline|'\n'
name|'bs'
op|'='
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'direct_flags'
op|'='
op|'('
string|"'oflag=direct'"
op|','
op|')'
newline|'\n'
name|'remaining_bytes'
op|'='
name|'vol_size'
newline|'\n'
nl|'\n'
comment|'# The loop caters for versions of dd that'
nl|'\n'
comment|"# don't support the iflag=count_bytes option."
nl|'\n'
name|'while'
name|'remaining_bytes'
op|':'
newline|'\n'
indent|'        '
name|'zero_blocks'
op|'='
name|'remaining_bytes'
op|'/'
name|'bs'
newline|'\n'
name|'seek_blocks'
op|'='
op|'('
name|'vol_size'
op|'-'
name|'remaining_bytes'
op|')'
op|'/'
name|'bs'
newline|'\n'
name|'zero_cmd'
op|'='
op|'('
string|"'dd'"
op|','
string|"'bs=%s'"
op|'%'
name|'bs'
op|','
nl|'\n'
string|"'if=/dev/zero'"
op|','
string|"'of=%s'"
op|'%'
name|'path'
op|','
nl|'\n'
string|"'seek=%s'"
op|'%'
name|'seek_blocks'
op|','
string|"'count=%s'"
op|'%'
name|'zero_blocks'
op|')'
newline|'\n'
name|'zero_cmd'
op|'+='
name|'direct_flags'
newline|'\n'
name|'if'
name|'zero_blocks'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'zero_cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'remaining_bytes'
op|'%='
name|'bs'
newline|'\n'
name|'bs'
op|'/='
number|'1024'
comment|'# Limit to 3 iterations'
newline|'\n'
name|'direct_flags'
op|'='
op|'('
op|')'
comment|'# Only use O_DIRECT with initial block size'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_logical_volumes
dedent|''
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
string|'"""Remove one or more logical volume."""'
newline|'\n'
nl|'\n'
name|'for'
name|'path'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'        '
name|'clear_logical_volume'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'paths'
op|':'
newline|'\n'
indent|'        '
name|'lvremove'
op|'='
op|'('
string|"'lvremove'"
op|','
string|"'-f'"
op|')'
op|'+'
name|'paths'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'lvremove'
op|','
name|'attempts'
op|'='
number|'3'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pick_disk_driver_name
dedent|''
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
string|'"""Pick the libvirt primary backend driver name\n\n    If the hypervisor supports multiple backend drivers, then the name\n    attribute selects the primary backend driver name, while the optional\n    type attribute provides the sub-type.  For example, xen supports a name\n    of "tap", "tap2", "phy", or "file", with a type of "aio" or "qcow2",\n    while qemu only supports a name of "qemu", but multiple types including\n    "raw", "bochs", "qcow2", and "qed".\n\n    :param is_block_dev:\n    :returns: driver_name or None\n    """'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_type'
op|'=='
string|'"xen"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'is_block_dev'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"phy"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"tap"'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'libvirt_type'
name|'in'
op|'('
string|"'kvm'"
op|','
string|"'qemu'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"qemu"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# UML doesn't want a driver_name set"
nl|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_size
dedent|''
dedent|''
name|'def'
name|'get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the (virtual) size of a disk image\n\n    :param path: Path to the disk image\n    :returns: Size (in bytes) of the given disk image as it would be seen\n              by a virtual machine.\n    """'
newline|'\n'
name|'size'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'virtual_size'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'size'
op|')'
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
name|'basename'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the backing file of a disk image\n\n    :param path: Path to the disk image\n    :returns: a path to the image\'s backing store\n    """'
newline|'\n'
name|'backing_file'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'backing_file'
newline|'\n'
name|'if'
name|'backing_file'
name|'and'
name|'basename'
op|':'
newline|'\n'
indent|'        '
name|'backing_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'backing_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'backing_file'
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
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Copy a disk image to an existing directory\n\n    :param src: Source image\n    :param dest: Destination path\n    :param host: Remote host\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
comment|'# We shell out to cp because that will intelligently copy'
nl|'\n'
comment|'# sparse files.  I.E. holes will not be written to DEST,'
nl|'\n'
comment|'# rather recreated efficiently.  In addition, since'
nl|'\n'
comment|'# coreutils 8.11, holes can be read efficiently too.'
nl|'\n'
indent|'        '
name|'execute'
op|'('
string|"'cp'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'dest'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'host'
op|','
name|'dest'
op|')'
newline|'\n'
comment|'# Try rsync first as that can compress and create sparse dest files.'
nl|'\n'
comment|"# Note however that rsync currently doesn't read sparse files"
nl|'\n'
comment|'# efficiently: https://bugzilla.samba.org/show_bug.cgi?id=8918'
nl|'\n'
comment|'# At least network traffic is mitigated with compression.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Do a relatively light weight test first, so that we'
nl|'\n'
comment|'# can fall back to scp, without having run out of space'
nl|'\n'
comment|'# on the destination for example.'
nl|'\n'
indent|'            '
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
string|"'--compress'"
op|','
string|"'--dry-run'"
op|','
name|'src'
op|','
name|'dest'
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
name|'execute'
op|'('
string|"'scp'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
string|"'--compress'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
dedent|''
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
string|'"""Write the given contents to a file\n\n    :param path: Destination file\n    :param contents: Desired contents of the file\n    :param umask: Umask to set when creating this file (will be reset)\n    """'
newline|'\n'
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'        '
name|'saved_umask'
op|'='
name|'os'
op|'.'
name|'umask'
op|'('
name|'umask'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
name|'contents'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'umask'
op|'('
name|'saved_umask'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown
dedent|''
dedent|''
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
string|'"""Change ownership of file or directory\n\n    :param path: File or directory whose ownership to change\n    :param owner: Desired new owner (given as uid or username)\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'chown'"
op|','
name|'owner'
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
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
string|'"""Create a snapshot in a disk image\n\n    :param disk_path: Path to disk image\n    :param snapshot_name: Name of snapshot in disk image\n    """'
newline|'\n'
name|'qemu_img_cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
nl|'\n'
string|"'snapshot'"
op|','
nl|'\n'
string|"'-c'"
op|','
nl|'\n'
name|'snapshot_name'
op|','
nl|'\n'
name|'disk_path'
op|')'
newline|'\n'
comment|'# NOTE(vish): libvirt changes ownership of images'
nl|'\n'
name|'execute'
op|'('
op|'*'
name|'qemu_img_cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
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
string|'"""Create a snapshot in a disk image\n\n    :param disk_path: Path to disk image\n    :param snapshot_name: Name of snapshot in disk image\n    """'
newline|'\n'
name|'qemu_img_cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
nl|'\n'
string|"'snapshot'"
op|','
nl|'\n'
string|"'-d'"
op|','
nl|'\n'
name|'snapshot_name'
op|','
nl|'\n'
name|'disk_path'
op|')'
newline|'\n'
comment|'# NOTE(vish): libvirt changes ownership of images'
nl|'\n'
name|'execute'
op|'('
op|'*'
name|'qemu_img_cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
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
string|'"""Extract a named snapshot from a disk image\n\n    :param disk_path: Path to disk image\n    :param snapshot_name: Name of snapshot in disk image\n    :param out_path: Desired path of extracted snapshot\n    """'
newline|'\n'
comment|'# NOTE(markmc): ISO is just raw to qemu-img'
nl|'\n'
name|'if'
name|'dest_fmt'
op|'=='
string|"'iso'"
op|':'
newline|'\n'
indent|'        '
name|'dest_fmt'
op|'='
string|"'raw'"
newline|'\n'
nl|'\n'
dedent|''
name|'qemu_img_cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
string|"'convert'"
op|','
string|"'-f'"
op|','
name|'source_fmt'
op|','
string|"'-O'"
op|','
name|'dest_fmt'
op|')'
newline|'\n'
nl|'\n'
comment|'# Conditionally enable compression of snapshots.'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_snapshot_compression'
name|'and'
name|'dest_fmt'
op|'=='
string|'"qcow2"'
op|':'
newline|'\n'
indent|'        '
name|'qemu_img_cmd'
op|'+='
op|'('
string|"'-c'"
op|','
op|')'
newline|'\n'
nl|'\n'
comment|'# When snapshot name is omitted we do a basic convert, which'
nl|'\n'
comment|'# is used by live snapshots.'
nl|'\n'
dedent|''
name|'if'
name|'snapshot_name'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'qemu_img_cmd'
op|'+='
op|'('
string|"'-s'"
op|','
name|'snapshot_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'qemu_img_cmd'
op|'+='
op|'('
name|'disk_path'
op|','
name|'out_path'
op|')'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'qemu_img_cmd'
op|')'
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
string|'"""Read contents of file\n\n    :param path: File to read\n    """'
newline|'\n'
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
indent|'        '
name|'return'
name|'fp'
op|'.'
name|'read'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Open file\n\n    see built-in file() documentation for more details\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'file'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
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
string|'"""Delete (unlink) file\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
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
string|'"""Find root device path for instance\n\n    May be file or device"""'
newline|'\n'
name|'xml_desc'
op|'='
name|'virt_dom'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml_desc'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_type'
op|'=='
string|"'lxc'"
op|':'
newline|'\n'
indent|'        '
name|'source'
op|'='
name|'domain'
op|'.'
name|'find'
op|'('
string|"'devices/filesystem/source'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'source'
op|'.'
name|'get'
op|'('
string|"'dir'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'disk_path'
op|'['
number|'0'
op|':'
name|'disk_path'
op|'.'
name|'rfind'
op|'('
string|"'rootfs'"
op|')'
op|']'
newline|'\n'
name|'disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'disk_path'
op|','
string|"'disk'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'source'
op|'='
name|'domain'
op|'.'
name|'find'
op|'('
string|"'devices/disk/source'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'source'
op|'.'
name|'get'
op|'('
string|"'file'"
op|')'
name|'or'
name|'source'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'disk_path'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"Can\'t retrieve root device path "'
nl|'\n'
string|'"from instance libvirt configuration"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'disk_path'
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
string|'"""Retrieve disk type (raw, qcow2, lvm) for given file."""'
newline|'\n'
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/dev'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'lvm'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'file_format'
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
string|'"""Get free/used/total space info for a filesystem\n\n    :param path: Any dirent on the filesystem\n    :returns: A dict containing:\n\n             :free: How much space is free (in bytes)\n             :used: How much space is used (in bytes)\n             :total: How big the filesystem is (in bytes)\n    """'
newline|'\n'
name|'hddinfo'
op|'='
name|'os'
op|'.'
name|'statvfs'
op|'('
name|'path'
op|')'
newline|'\n'
name|'total'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_blocks'
newline|'\n'
name|'free'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_bavail'
newline|'\n'
name|'used'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
op|'('
name|'hddinfo'
op|'.'
name|'f_blocks'
op|'-'
name|'hddinfo'
op|'.'
name|'f_bfree'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'total'"
op|':'
name|'total'
op|','
nl|'\n'
string|"'free'"
op|':'
name|'free'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'used'
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
string|'"""Grab image."""'
newline|'\n'
name|'images'
op|'.'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'target'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_path
dedent|''
name|'def'
name|'get_instance_path'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the correct path for instance storage.\n\n    This used to be calculated all over the place. This method centralizes\n    this into one location, which will make it easier to change the\n    algorithm used to name instance storage directories.\n\n    :param instance: the instance we want a path for\n\n    :returns: a path to store information about that instance\n    """'
newline|'\n'
comment|"# TODO(mikal): we should use UUID instead of name, as name isn't"
nl|'\n'
comment|'# nessesarily unique'
nl|'\n'
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
dedent|''
endmarker|''
end_unit
