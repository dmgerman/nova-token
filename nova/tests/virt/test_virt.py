begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata'
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
name|'io'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
name|'disk_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'mount'
name|'import'
name|'api'
name|'as'
name|'mount'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
name|'PROC_MOUNTS_CONTENTS'
op|'='
string|'"""rootfs / rootfs rw 0 0\nsysfs /sys sysfs rw,nosuid,nodev,noexec,relatime 0 0\nproc /proc proc rw,nosuid,nodev,noexec,relatime 0 0\nudev /dev devtmpfs rw,relatime,size=1013160k,nr_inodes=253290,mode=755 0 0\ndevpts /dev/pts devpts rw,nosuid,noexec,relatime,gid=5,mode=620 0 0\ntmpfs /run tmpfs rw,nosuid,relatime,size=408904k,mode=755 0 0"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestVirtDriver
name|'class'
name|'TestVirtDriver'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_block_device
indent|'    '
name|'def'
name|'test_block_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'swap'
op|'='
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'ephemerals'
op|'='
op|'['
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
op|'['
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sde'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|']'
newline|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda'"
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'swap'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
name|'ephemerals'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
name|'block_device_mapping'
op|'}'
newline|'\n'
nl|'\n'
name|'empty_block_device_info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'block_device_info'
op|')'
op|','
string|"'/dev/sda'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'empty_block_device_info'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
op|','
name|'swap'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
nl|'\n'
name|'empty_block_device_info'
op|')'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
nl|'\n'
name|'empty_block_device_info'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
op|'{'
string|"'swap'"
op|':'
name|'None'
op|'}'
op|')'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
op|'{'
string|"'swap'"
op|':'
name|'None'
op|'}'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
nl|'\n'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'None'
op|')'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'None'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'block_device_info'
op|')'
op|','
nl|'\n'
name|'ephemerals'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'empty_block_device_info'
op|')'
op|','
nl|'\n'
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_is_usable
dedent|''
name|'def'
name|'test_swap_is_usable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
name|'None'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'0'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeMount
dedent|''
dedent|''
name|'class'
name|'FakeMount'
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
name|'image'
op|','
name|'mount_dir'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image'
op|'='
name|'image'
newline|'\n'
name|'self'
op|'.'
name|'partition'
op|'='
name|'partition'
newline|'\n'
name|'self'
op|'.'
name|'mount_dir'
op|'='
name|'mount_dir'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'self'
op|'.'
name|'mapped'
op|'='
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
DECL|member|do_mount
dedent|''
name|'def'
name|'do_mount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'linked'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'mounted'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
string|"'/dev/fake'"
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|do_umount
dedent|''
name|'def'
name|'do_umount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'linked'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|do_teardown
dedent|''
name|'def'
name|'do_teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'linked'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDiskImage
dedent|''
dedent|''
name|'class'
name|'TestDiskImage'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestDiskImage'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|mock_proc_mounts
dedent|''
name|'def'
name|'mock_proc_mounts'
op|'('
name|'self'
op|','
name|'mock_open'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'io'
op|'.'
name|'StringIO'
op|'('
name|'unicode'
op|'('
name|'PROC_MOUNTS_CONTENTS'
op|')'
op|')'
newline|'\n'
name|'mock_open'
op|'.'
name|'return_value'
op|'='
name|'response'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'__builtin__.open'"
op|')'
newline|'\n'
DECL|member|test_mount
name|'def'
name|'test_mount'
op|'('
name|'self'
op|','
name|'mock_open'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_proc_mounts'
op|'('
name|'mock_open'
op|')'
newline|'\n'
name|'image'
op|'='
string|"'/tmp/fake-image'"
newline|'\n'
name|'mountdir'
op|'='
string|"'/mnt/fake_rootfs'"
newline|'\n'
name|'fakemount'
op|'='
name|'FakeMount'
op|'('
name|'image'
op|','
name|'mountdir'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_for_format
name|'def'
name|'fake_instance_for_format'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'imgfmt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fakemount'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mount'
op|'.'
name|'Mount'
op|','
string|"'instance_for_format'"
op|','
nl|'\n'
name|'staticmethod'
op|'('
name|'fake_instance_for_format'
op|')'
op|')'
newline|'\n'
name|'diskimage'
op|'='
name|'disk_api'
op|'.'
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'mount_dir'
op|'='
name|'mountdir'
op|')'
newline|'\n'
name|'dev'
op|'='
name|'diskimage'
op|'.'
name|'mount'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'diskimage'
op|'.'
name|'_mounter'
op|','
name|'fakemount'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'/dev/fake'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'__builtin__.open'"
op|')'
newline|'\n'
DECL|member|test_umount
name|'def'
name|'test_umount'
op|'('
name|'self'
op|','
name|'mock_open'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_proc_mounts'
op|'('
name|'mock_open'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
string|"'/tmp/fake-image'"
newline|'\n'
name|'mountdir'
op|'='
string|"'/mnt/fake_rootfs'"
newline|'\n'
name|'fakemount'
op|'='
name|'FakeMount'
op|'('
name|'image'
op|','
name|'mountdir'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_for_format
name|'def'
name|'fake_instance_for_format'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'imgfmt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fakemount'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mount'
op|'.'
name|'Mount'
op|','
string|"'instance_for_format'"
op|','
nl|'\n'
name|'staticmethod'
op|'('
name|'fake_instance_for_format'
op|')'
op|')'
newline|'\n'
name|'diskimage'
op|'='
name|'disk_api'
op|'.'
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'mount_dir'
op|'='
name|'mountdir'
op|')'
newline|'\n'
name|'dev'
op|'='
name|'diskimage'
op|'.'
name|'mount'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'diskimage'
op|'.'
name|'_mounter'
op|','
name|'fakemount'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'/dev/fake'"
op|')'
newline|'\n'
name|'diskimage'
op|'.'
name|'umount'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'diskimage'
op|'.'
name|'_mounter'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'__builtin__.open'"
op|')'
newline|'\n'
DECL|member|test_teardown
name|'def'
name|'test_teardown'
op|'('
name|'self'
op|','
name|'mock_open'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mock_proc_mounts'
op|'('
name|'mock_open'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
string|"'/tmp/fake-image'"
newline|'\n'
name|'mountdir'
op|'='
string|"'/mnt/fake_rootfs'"
newline|'\n'
name|'fakemount'
op|'='
name|'FakeMount'
op|'('
name|'image'
op|','
name|'mountdir'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_for_format
name|'def'
name|'fake_instance_for_format'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'imgfmt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fakemount'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mount'
op|'.'
name|'Mount'
op|','
string|"'instance_for_format'"
op|','
nl|'\n'
name|'staticmethod'
op|'('
name|'fake_instance_for_format'
op|')'
op|')'
newline|'\n'
name|'diskimage'
op|'='
name|'disk_api'
op|'.'
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'mount_dir'
op|'='
name|'mountdir'
op|')'
newline|'\n'
name|'dev'
op|'='
name|'diskimage'
op|'.'
name|'mount'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'diskimage'
op|'.'
name|'_mounter'
op|','
name|'fakemount'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dev'
op|','
string|"'/dev/fake'"
op|')'
newline|'\n'
name|'diskimage'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'diskimage'
op|'.'
name|'_mounter'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestVirtDisk
dedent|''
dedent|''
name|'class'
name|'TestVirtDisk'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestVirtDisk'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lxc_setup_container
dedent|''
name|'def'
name|'test_lxc_setup_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
string|"'/tmp/fake-image'"
newline|'\n'
name|'container_dir'
op|'='
string|"'/mnt/fake_rootfs/'"
newline|'\n'
nl|'\n'
DECL|function|proc_mounts
name|'def'
name|'proc_mounts'
op|'('
name|'self'
op|','
name|'mount_point'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_for_format
dedent|''
name|'def'
name|'fake_instance_for_format'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'imgfmt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FakeMount'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'_'
op|':'
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'disk_api'
op|'.'
name|'_DiskImage'
op|','
string|"'_device_for_path'"
op|','
name|'proc_mounts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'mount'
op|'.'
name|'Mount'
op|','
string|"'instance_for_format'"
op|','
nl|'\n'
name|'staticmethod'
op|'('
name|'fake_instance_for_format'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'disk_api'
op|'.'
name|'setup_container'
op|'('
name|'image'
op|','
name|'container_dir'
op|')'
op|','
nl|'\n'
string|"'/dev/fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lxc_teardown_container
dedent|''
name|'def'
name|'test_lxc_teardown_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|proc_mounts
indent|'        '
name|'def'
name|'proc_mounts'
op|'('
name|'self'
op|','
name|'mount_point'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mount_points'
op|'='
op|'{'
nl|'\n'
string|"'/mnt/loop/nopart'"
op|':'
string|"'/dev/loop0'"
op|','
nl|'\n'
string|"'/mnt/loop/part'"
op|':'
string|"'/dev/mapper/loop0p1'"
op|','
nl|'\n'
string|"'/mnt/nbd/nopart'"
op|':'
string|"'/dev/nbd15'"
op|','
nl|'\n'
string|"'/mnt/nbd/part'"
op|':'
string|"'/dev/mapper/nbd15p1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'mount_points'
op|'['
name|'mount_point'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'_'
op|':'
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'disk_api'
op|'.'
name|'_DiskImage'
op|','
string|"'_device_for_path'"
op|','
name|'proc_mounts'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/loop/nopart'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'umount'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|'('
string|"'losetup'"
op|','
string|"'--detach'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/loop/part'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'umount'"
op|','
string|"'/dev/mapper/loop0p1'"
op|')'
op|','
nl|'\n'
op|'('
string|"'kpartx'"
op|','
string|"'-d'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|'('
string|"'losetup'"
op|','
string|"'--detach'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/nbd/nopart'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'umount'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|'('
string|"'qemu-nbd'"
op|','
string|"'-d'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/nbd/part'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'umount'"
op|','
string|"'/dev/mapper/nbd15p1'"
op|')'
op|','
nl|'\n'
op|'('
string|"'kpartx'"
op|','
string|"'-d'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|'('
string|"'qemu-nbd'"
op|','
string|"'-d'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'executes'
op|','
name|'expected_commands'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lxc_teardown_container_with_namespace_cleaned
dedent|''
name|'def'
name|'test_lxc_teardown_container_with_namespace_cleaned'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|proc_mounts
indent|'        '
name|'def'
name|'proc_mounts'
op|'('
name|'self'
op|','
name|'mount_point'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'_'
op|':'
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'disk_api'
op|'.'
name|'_DiskImage'
op|','
string|"'_device_for_path'"
op|','
name|'proc_mounts'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/loop/nopart'"
op|','
string|"'/dev/loop0'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'losetup'"
op|','
string|"'--detach'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/loop/part'"
op|','
string|"'/dev/loop0'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'losetup'"
op|','
string|"'--detach'"
op|','
string|"'/dev/loop0'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/nbd/nopart'"
op|','
string|"'/dev/nbd15'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'qemu-nbd'"
op|','
string|"'-d'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'disk_api'
op|'.'
name|'teardown_container'
op|'('
string|"'/mnt/nbd/part'"
op|','
string|"'/dev/nbd15'"
op|')'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
nl|'\n'
op|'('
string|"'qemu-nbd'"
op|','
string|"'-d'"
op|','
string|"'/dev/nbd15'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'executes'
op|','
name|'expected_commands'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
