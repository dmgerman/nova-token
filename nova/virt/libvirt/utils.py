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
name|'errno'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
name|'jsonutils'
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
nl|'\n'
DECL|variable|util_opts
name|'util_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'image_info_filename_pattern'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$instances_path/$base_dir_name/%(image)s.info'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allows image information files to be stored in '"
nl|'\n'
string|"'non-standard locations'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'base_dir_name'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
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
name|'util_opts'
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
string|'"""Get iscsi initiator name for this machine"""'
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
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create COW image\n\n    Creates a COW image with the given backing file\n\n    :param backing_file: Existing image on which to base the COW image\n    :param path: Desired location of the COW image\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
string|"'qcow2'"
op|','
string|"'-o'"
op|','
nl|'\n'
string|"'backing_file=%s'"
op|'%'
name|'backing_file'
op|','
name|'path'
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
string|"'lv_path'"
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
string|'"""Remove one or more logical volume."""'
newline|'\n'
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
name|'FLAGS'
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
name|'FLAGS'
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
op|'['
string|"'virtual size'"
op|']'
newline|'\n'
name|'size'
op|'='
name|'size'
op|'.'
name|'split'
op|'('
string|"'('"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
op|')'
op|'['
number|'0'
op|']'
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
name|'get'
op|'('
string|"'backing file'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'backing_file'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'actual path: '"
name|'in'
name|'backing_file'
op|':'
newline|'\n'
indent|'            '
name|'backing_file'
op|'='
name|'backing_file'
op|'.'
name|'split'
op|'('
string|"'actual path: '"
op|')'
op|'['
number|'1'
op|']'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
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
DECL|function|mkfs
dedent|''
dedent|''
dedent|''
name|'def'
name|'mkfs'
op|'('
name|'fs'
op|','
name|'path'
op|','
name|'label'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Format a file or block device\n\n    :param fs: Filesystem type (examples include \'swap\', \'ext3\', \'ext4\'\n               \'btrfs\', etc.)\n    :param path: Path to file or block device to format\n    :param label: Volume label to use\n    """'
newline|'\n'
name|'if'
name|'fs'
op|'=='
string|"'swap'"
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|"'mkswap'"
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
string|"'mkfs'"
op|','
string|"'-t'"
op|','
name|'fs'
op|']'
newline|'\n'
comment|'#add -F to force no interactive excute on non-block device.'
nl|'\n'
name|'if'
name|'fs'
name|'in'
op|'['
string|"'ext3'"
op|','
string|"'ext4'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'-F'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'label'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'-n'"
op|','
name|'label'
op|']'
op|')'
newline|'\n'
dedent|''
name|'args'
op|'.'
name|'append'
op|'('
name|'path'
op|')'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
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
dedent|''
name|'qemu_img_cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
nl|'\n'
string|"'convert'"
op|','
nl|'\n'
string|"'-f'"
op|','
nl|'\n'
name|'source_fmt'
op|','
nl|'\n'
string|"'-O'"
op|','
nl|'\n'
name|'dest_fmt'
op|','
nl|'\n'
string|"'-s'"
op|','
nl|'\n'
name|'snapshot_name'
op|','
nl|'\n'
name|'disk_path'
op|','
nl|'\n'
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
string|'"""Grab image"""'
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
DECL|function|get_info_filename
dedent|''
name|'def'
name|'get_info_filename'
op|'('
name|'base_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Construct a filename for storing addtional information about a base\n    image.\n\n    Returns a filename.\n    """'
newline|'\n'
nl|'\n'
name|'base_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'base_path'
op|')'
newline|'\n'
name|'return'
op|'('
name|'FLAGS'
op|'.'
name|'image_info_filename_pattern'
nl|'\n'
op|'%'
op|'{'
string|"'image'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid_info_file
dedent|''
name|'def'
name|'is_valid_info_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test if a given path matches the pattern for info files."""'
newline|'\n'
nl|'\n'
name|'digest_size'
op|'='
name|'hashlib'
op|'.'
name|'sha1'
op|'('
op|')'
op|'.'
name|'digestsize'
op|'*'
number|'2'
newline|'\n'
name|'regexp'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'image_info_filename_pattern'
nl|'\n'
op|'%'
op|'{'
string|"'image'"
op|':'
op|'('
string|"'([0-9a-f]{%(digest_size)d}|'"
nl|'\n'
string|"'[0-9a-f]{%(digest_size)d}_sm|'"
nl|'\n'
string|"'[0-9a-f]{%(digest_size)d}_[0-9]+)'"
nl|'\n'
op|'%'
op|'{'
string|"'digest_size'"
op|':'
name|'digest_size'
op|'}'
op|')'
op|'}'
op|')'
newline|'\n'
name|'m'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
name|'regexp'
op|','
name|'path'
op|')'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|read_stored_info
dedent|''
name|'def'
name|'read_stored_info'
op|'('
name|'base_path'
op|','
name|'field'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read information about an image.\n\n    Returns an empty dictionary if there is no info, just the field value if\n    a field is requested, or the entire dictionary otherwise.\n    """'
newline|'\n'
nl|'\n'
name|'info_file'
op|'='
name|'get_info_filename'
op|'('
name|'base_path'
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
name|'info_file'
op|')'
op|':'
newline|'\n'
comment|'# Special case to handle essex checksums being converted'
nl|'\n'
indent|'        '
name|'old_filename'
op|'='
name|'base_path'
op|'+'
string|"'.sha1'"
newline|'\n'
name|'if'
name|'field'
op|'=='
string|"'sha1'"
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'old_filename'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'hash_file'
op|'='
name|'open'
op|'('
name|'old_filename'
op|')'
newline|'\n'
name|'hash_value'
op|'='
name|'hash_file'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'hash_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'write_stored_info'
op|'('
name|'base_path'
op|','
name|'field'
op|'='
name|'field'
op|','
name|'value'
op|'='
name|'hash_value'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'old_filename'
op|')'
newline|'\n'
name|'d'
op|'='
op|'{'
name|'field'
op|':'
name|'hash_value'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Reading image info file: %s'"
op|')'
op|','
name|'info_file'
op|')'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'info_file'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'serialized'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'rstrip'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Read: %s'"
op|')'
op|','
name|'serialized'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'serialized'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'ValueError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Error reading image info file %(filename)s: '"
nl|'\n'
string|"'%(error)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'filename'"
op|':'
name|'info_file'
op|','
nl|'\n'
string|"'error'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'field'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'d'
op|'.'
name|'get'
op|'('
name|'field'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_stored_info
dedent|''
name|'def'
name|'write_stored_info'
op|'('
name|'target'
op|','
name|'field'
op|'='
name|'None'
op|','
name|'value'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Write information about an image."""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'field'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'info_file'
op|'='
name|'get_info_filename'
op|'('
name|'target'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'ensure_tree'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'info_file'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'read_stored_info'
op|'('
name|'info_file'
op|')'
newline|'\n'
name|'d'
op|'['
name|'field'
op|']'
op|'='
name|'value'
newline|'\n'
name|'serialized'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'d'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Writing image info file: %s'"
op|')'
op|','
name|'info_file'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Wrote: %s'"
op|')'
op|','
name|'serialized'
op|')'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'info_file'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'serialized'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
