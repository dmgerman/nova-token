begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
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
nl|'\n'
nl|'\n'
DECL|class|FakeMount
name|'class'
name|'FakeMount'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|device
indent|'    '
name|'device'
op|'='
name|'None'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|instance_for_format
name|'def'
name|'instance_for_format'
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
indent|'        '
name|'return'
name|'FakeMount'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dev
dedent|''
name|'def'
name|'get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unget_dev
dedent|''
name|'def'
name|'unget_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APITestCase
dedent|''
dedent|''
name|'class'
name|'APITestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_can_resize_need_fs_type_specified
indent|'    '
name|'def'
name|'test_can_resize_need_fs_type_specified'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): Bug 1094373 saw a regression where we failed to'
nl|'\n'
comment|'# treat a failure to mount as a failure to be able to resize the'
nl|'\n'
comment|'# filesystem'
nl|'\n'
DECL|function|_fake_get_disk_size
indent|'        '
name|'def'
name|'_fake_get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'10'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.disk.api.get_disk_size'"
op|','
name|'_fake_get_disk_size'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_trycmd
name|'def'
name|'fake_trycmd'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
op|','
string|"'broken'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
name|'fake_trycmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_returns_true
name|'def'
name|'fake_returns_true'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|function|fake_returns_nothing
dedent|''
name|'def'
name|'fake_returns_nothing'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.disk.mount.nbd.NbdMount.get_dev'"
op|','
nl|'\n'
name|'fake_returns_true'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.disk.mount.nbd.NbdMount.map_dev'"
op|','
nl|'\n'
name|'fake_returns_true'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.disk.vfs.localfs.VFSLocalFS.get_image_fs'"
op|','
nl|'\n'
name|'fake_returns_nothing'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Force the use of localfs, which is what was used during the failure'
nl|'\n'
comment|'# reported in the bug'
nl|'\n'
DECL|function|fake_import_fails
name|'def'
name|'fake_import_fails'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Failed'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'oslo.utils.import_module'"
op|','
nl|'\n'
name|'fake_import_fails'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'imgfile'
op|'.'
name|'close'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'api'
op|'.'
name|'is_image_extendable'
op|'('
name|'imgfile'
op|','
name|'use_cow'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resize2fs_success
dedent|''
name|'def'
name|'test_resize2fs_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'e2fsck'"
op|','
nl|'\n'
string|"'-fp'"
op|','
nl|'\n'
name|'imgfile'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
nl|'\n'
name|'run_as_root'
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
nl|'\n'
name|'imgfile'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'resize2fs'
op|'('
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resize2fs_e2fsck_fails
dedent|''
name|'def'
name|'test_resize2fs_e2fsck_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'e2fsck'"
op|','
nl|'\n'
string|"'-fp'"
op|','
nl|'\n'
name|'imgfile'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'1'
op|','
number|'2'
op|']'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'False'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
string|'"fs error"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'resize2fs'
op|'('
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extend_qcow_success
dedent|''
name|'def'
name|'test_extend_qcow_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
name|'imgsize'
op|'='
number|'10'
newline|'\n'
name|'device'
op|'='
string|'"/dev/sdh"'
newline|'\n'
name|'use_cow'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'resize_fs_using_block_device'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mounter'
op|'='
name|'FakeMount'
op|'.'
name|'instance_for_format'
op|'('
nl|'\n'
name|'imgfile'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'qcow2'"
op|')'
newline|'\n'
name|'mounter'
op|'.'
name|'device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'can_resize_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'is_image_extendable'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'mounter'
op|','
string|"'get_dev'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'mounter'
op|','
string|"'unget_dev'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'resize2fs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'mount'
op|'.'
name|'Mount'
op|','
string|"'instance_for_format'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'api'
op|'.'
name|'can_resize_image'
op|'('
name|'imgfile'
op|','
name|'imgsize'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'resize'"
op|','
name|'imgfile'
op|','
name|'imgsize'
op|')'
newline|'\n'
name|'api'
op|'.'
name|'is_image_extendable'
op|'('
name|'imgfile'
op|','
name|'use_cow'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'mount'
op|'.'
name|'Mount'
op|'.'
name|'instance_for_format'
op|'('
nl|'\n'
name|'imgfile'
op|','
name|'None'
op|','
name|'None'
op|','
string|"'qcow2'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'mounter'
op|')'
newline|'\n'
name|'mounter'
op|'.'
name|'get_dev'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'api'
op|'.'
name|'resize2fs'
op|'('
name|'mounter'
op|'.'
name|'device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'mounter'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'extend'
op|'('
name|'imgfile'
op|','
name|'imgsize'
op|','
name|'use_cow'
op|'='
name|'use_cow'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extend_raw_success
dedent|''
name|'def'
name|'test_extend_raw_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
name|'imgsize'
op|'='
number|'10'
newline|'\n'
name|'use_cow'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'can_resize_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'is_image_extendable'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'api'
op|','
string|"'resize2fs'"
op|')'
newline|'\n'
nl|'\n'
name|'api'
op|'.'
name|'can_resize_image'
op|'('
name|'imgfile'
op|','
name|'imgsize'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'resize'"
op|','
name|'imgfile'
op|','
name|'imgsize'
op|')'
newline|'\n'
name|'api'
op|'.'
name|'is_image_extendable'
op|'('
name|'imgfile'
op|','
name|'use_cow'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'api'
op|'.'
name|'resize2fs'
op|'('
name|'imgfile'
op|','
name|'run_as_root'
op|'='
name|'False'
op|','
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'extend'
op|'('
name|'imgfile'
op|','
name|'imgsize'
op|','
name|'use_cow'
op|'='
name|'use_cow'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|HASH_EXT3
dedent|''
name|'HASH_EXT3'
op|'='
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'api'
op|'.'
name|'FS_FORMAT_EXT3'
op|')'
op|'['
op|':'
number|'7'
op|']'
newline|'\n'
DECL|variable|HASH_NTFS
name|'HASH_NTFS'
op|'='
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'api'
op|'.'
name|'FS_FORMAT_NTFS'
op|')'
op|'['
op|':'
number|'7'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_get_file_extension_for_os_type
name|'def'
name|'test_get_file_extension_for_os_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'HASH_EXT3'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'HASH_EXT3'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'linux'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'HASH_NTFS'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'windows'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_file_extension_for_os_type_with_overrides
dedent|''
name|'def'
name|'test_get_file_extension_for_os_type_with_overrides'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.disk.api._DEFAULT_MKFS_COMMAND'"
op|','
nl|'\n'
string|"'custom mkfs command'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a74d253"'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'linux'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a74d253"'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'windows'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a74d253"'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'osx'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'dict'
op|'('
name|'api'
op|'.'
name|'_MKFS_COMMAND'
op|','
nl|'\n'
op|'{'
string|"'osx'"
op|':'
string|"'custom mkfs command'"
op|'}'
op|','
name|'clear'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'HASH_EXT3'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'linux'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'HASH_NTFS'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'windows'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"a74d253"'
op|','
nl|'\n'
name|'api'
op|'.'
name|'get_file_extension_for_os_type'
op|'('
nl|'\n'
string|"'osx'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
