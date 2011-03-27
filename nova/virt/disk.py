begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nUtility methods to resize, repartition, and modify disk images.\n\nIncludes injection of SSH PGP keys into authorized_keys file.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.compute.disk'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'minimum_root_size'"
op|','
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'minimum size in bytes of root partition'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'block_size'"
op|','
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'256'
op|','
nl|'\n'
string|"'block_size to use for dd'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/interfaces.template'"
op|')'
op|','
nl|'\n'
string|"'Template file for injected network'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'timeout_nbd'"
op|','
number|'10'
op|','
nl|'\n'
string|"'time to wait for a NBD device coming up'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'max_nbd_devices'"
op|','
number|'16'
op|','
nl|'\n'
string|"'maximum number of possible nbd devices'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extend
name|'def'
name|'extend'
op|'('
name|'image'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Increase image to size"""'
newline|'\n'
name|'file_size'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getsize'
op|'('
name|'image'
op|')'
newline|'\n'
name|'if'
name|'file_size'
op|'>='
name|'size'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'truncate'"
op|','
string|"'-s'"
op|','
name|'size'
op|','
name|'image'
op|')'
newline|'\n'
comment|'# NOTE(vish): attempts to resize filesystem'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'e2fsck'"
op|','
string|"'-fp'"
op|','
name|'image'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'resize2fs'"
op|','
name|'image'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_data
dedent|''
name|'def'
name|'inject_data'
op|'('
name|'image'
op|','
name|'key'
op|'='
name|'None'
op|','
name|'net'
op|'='
name|'None'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'nbd'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects a ssh key and optionally net data into a disk image.\n\n    it will mount the image as a fully partitioned disk and attempt to inject\n    into the specified partition number.\n\n    If partition is not specified it mounts the image as a single partition.\n\n    """'
newline|'\n'
name|'device'
op|'='
name|'_link_device'
op|'('
name|'image'
op|','
name|'nbd'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'partition'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# create partition'
nl|'\n'
indent|'            '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'kpartx'"
op|','
string|"'-a'"
op|','
name|'device'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to load partition: %s'"
op|')'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'mapped_device'
op|'='
string|"'/dev/mapper/%sp%s'"
op|'%'
op|'('
name|'device'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|','
nl|'\n'
name|'partition'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mapped_device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
comment|"# We can only loopback mount raw images. If the device isn't there,"
nl|'\n'
comment|"# it's normally because it's a .vmdk or a .vdi etc"
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'mapped_device'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'Mapped device was not found (we can'"
nl|'\n'
string|"' only inject raw disk images): %s'"
op|'%'
nl|'\n'
name|'mapped_device'
op|')'
newline|'\n'
nl|'\n'
comment|"# Configure ext2fs so that it doesn't auto-check every N boots"
nl|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'tune2fs'"
op|','
nl|'\n'
string|"'-c'"
op|','
number|'0'
op|','
string|"'-i'"
op|','
number|'0'
op|','
name|'mapped_device'
op|')'
newline|'\n'
nl|'\n'
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# mount loopback to dir'
nl|'\n'
indent|'            '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'sudo'"
op|','
string|"'mount'"
op|','
name|'mapped_device'
op|','
name|'tmpdir'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
nl|'\n'
op|'%'
name|'err'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'inject_data_into_fs'
op|'('
name|'tmpdir'
op|','
name|'key'
op|','
name|'net'
op|','
name|'utils'
op|'.'
name|'execute'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# unmount device'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'umount'"
op|','
name|'mapped_device'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# remove temporary directory'
nl|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rmdir'"
op|','
name|'tmpdir'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'partition'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# remove partitions'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'kpartx'"
op|','
string|"'-d'"
op|','
name|'device'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'_unlink_device'
op|'('
name|'device'
op|','
name|'nbd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup_container
dedent|''
dedent|''
name|'def'
name|'setup_container'
op|'('
name|'image'
op|','
name|'container_dir'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Setup the LXC container\n\n    It will mount the loopback image to the container directory in order\n    to create the root filesystem for the container\n    """'
newline|'\n'
name|'nbd'
op|'='
string|'"False"'
newline|'\n'
name|'device'
op|'='
name|'_link_device'
op|'('
name|'image'
op|','
name|'nbd'
op|')'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'mount'"
op|','
name|'device'
op|','
name|'container_dir'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
nl|'\n'
op|'%'
name|'err'
op|')'
newline|'\n'
name|'_unlink_device'
op|'('
name|'device'
op|','
name|'nbd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy_container
dedent|''
dedent|''
name|'def'
name|'destroy_container'
op|'('
name|'target'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the container once it terminates\n\n    It will umount the container that is mounted, try to find the loopback\n    device associated with the container and delete it.\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'container_dir'
op|'='
string|"'%s/rootfs'"
op|'%'
name|'target'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'umount'"
op|','
name|'container_dir'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'losetup'"
op|','
string|"'-a'"
op|')'
newline|'\n'
name|'for'
name|'loop'
name|'in'
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'['
string|"'name'"
op|']'
name|'in'
name|'loop'
op|':'
newline|'\n'
indent|'                '
name|'device'
op|'='
name|'loop'
op|'.'
name|'split'
op|'('
name|'loop'
op|','
string|"':'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'losetup'"
op|','
string|"'--detach'"
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_link_device
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_link_device'
op|'('
name|'image'
op|','
name|'nbd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Link image to device using loopback or nbd"""'
newline|'\n'
name|'if'
name|'nbd'
op|':'
newline|'\n'
indent|'        '
name|'device'
op|'='
name|'_allocate_device'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'qemu-nbd'"
op|','
string|"'-c'"
op|','
name|'device'
op|','
name|'image'
op|')'
newline|'\n'
comment|'# NOTE(vish): this forks into another process, so give it a chance'
nl|'\n'
comment|'#             to set up before continuuing'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'timeout_nbd'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|'"/sys/block/%s/pid"'
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'device'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'device'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'nbd device %s did not show up'"
op|')'
op|'%'
name|'device'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'losetup'"
op|','
string|"'--find'"
op|','
string|"'--show'"
op|','
name|'image'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Could not attach image to loopback: %s'"
op|')'
nl|'\n'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unlink_device
dedent|''
dedent|''
name|'def'
name|'_unlink_device'
op|'('
name|'device'
op|','
name|'nbd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unlink image from device using loopback or nbd"""'
newline|'\n'
name|'if'
name|'nbd'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'qemu-nbd'"
op|','
string|"'-d'"
op|','
name|'device'
op|')'
newline|'\n'
name|'_free_device'
op|'('
name|'device'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'losetup'"
op|','
string|"'--detach'"
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_DEVICES
dedent|''
dedent|''
name|'_DEVICES'
op|'='
op|'['
string|"'/dev/nbd%s'"
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'max_nbd_devices'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_allocate_device
name|'def'
name|'_allocate_device'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): This assumes no other processes are allocating nbd devices.'
nl|'\n'
comment|'#             It may race cause a race condition if multiple'
nl|'\n'
comment|'#             workers are running on a given machine.'
nl|'\n'
indent|'    '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'_DEVICES'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'No free nbd devices'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'_DEVICES'
op|'.'
name|'pop'
op|'('
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
string|'"/sys/block/%s/pid"'
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'device'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'device'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_free_device
dedent|''
name|'def'
name|'_free_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_DEVICES'
op|'.'
name|'append'
op|'('
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_data_into_fs
dedent|''
name|'def'
name|'inject_data_into_fs'
op|'('
name|'fs'
op|','
name|'key'
op|','
name|'net'
op|','
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects data into a filesystem already mounted by the caller.\n    Virt connections can call this directly if they mount their fs\n    in a different way to inject_data\n    """'
newline|'\n'
name|'if'
name|'key'
op|':'
newline|'\n'
indent|'        '
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'net'
op|':'
newline|'\n'
indent|'        '
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_key_into_fs
dedent|''
dedent|''
name|'def'
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add the given public ssh key to root\'s authorized_keys.\n\n    key is an ssh key string.\n    fs is the path to the base of the filesystem into which to inject the key.\n    """'
newline|'\n'
name|'sshdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
string|"'root'"
op|','
string|"'.ssh'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'sshdir'
op|')'
comment|"# existing dir doesn't matter"
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'chown'"
op|','
string|"'root'"
op|','
name|'sshdir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'chmod'"
op|','
string|"'700'"
op|','
name|'sshdir'
op|')'
newline|'\n'
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'sshdir'
op|','
string|"'authorized_keys'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'tee'"
op|','
string|"'-a'"
op|','
name|'keyfile'
op|','
nl|'\n'
name|'process_input'
op|'='
string|"'\\n'"
op|'+'
name|'key'
op|'.'
name|'strip'
op|'('
op|')'
op|'+'
string|"'\\n'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_net_into_fs
dedent|''
name|'def'
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Inject /etc/network/interfaces into the filesystem rooted at fs.\n\n    net is the contents of /etc/network/interfaces.\n    """'
newline|'\n'
name|'netdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
string|"'etc'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'netdir'
op|')'
comment|"# existing dir doesn't matter"
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'chown'"
op|','
string|"'root:root'"
op|','
name|'netdir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'chmod'"
op|','
number|'755'
op|','
name|'netdir'
op|')'
newline|'\n'
name|'netfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'netdir'
op|','
string|"'interfaces'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo'"
op|','
string|"'tee'"
op|','
name|'netfile'
op|','
name|'process_input'
op|'='
name|'net'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
