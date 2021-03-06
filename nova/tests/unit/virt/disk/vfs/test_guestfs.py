begin_unit
comment|'#    Copyright (C) 2012 Red Hat, Inc.'
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
name|'fixtures'
newline|'\n'
name|'import'
name|'mock'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
name|'import'
name|'fakeguestfs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
name|'import'
name|'guestfs'
name|'as'
name|'vfsimpl'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'image'
name|'import'
name|'model'
name|'as'
name|'imgmodel'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtDiskVFSGuestFSTest
name|'class'
name|'VirtDiskVFSGuestFSTest'
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
name|'VirtDiskVFSGuestFSTest'
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
name|'useFixture'
op|'('
nl|'\n'
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.virt.disk.vfs.guestfs.guestfs'"
op|','
nl|'\n'
name|'fakeguestfs'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'qcowfile'
op|'='
name|'imgmodel'
op|'.'
name|'LocalFileImage'
op|'('
string|'"/dummy.qcow2"'
op|','
nl|'\n'
name|'imgmodel'
op|'.'
name|'FORMAT_QCOW2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rawfile'
op|'='
name|'imgmodel'
op|'.'
name|'LocalFileImage'
op|'('
string|'"/dummy.img"'
op|','
nl|'\n'
name|'imgmodel'
op|'.'
name|'FORMAT_RAW'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lvmfile'
op|'='
name|'imgmodel'
op|'.'
name|'LocalBlockImage'
op|'('
string|'"/dev/volgroup/myvol"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rbdfile'
op|'='
name|'imgmodel'
op|'.'
name|'RBDImage'
op|'('
string|'"myvol"'
op|','
string|'"mypool"'
op|','
nl|'\n'
string|'"cthulu"'
op|','
nl|'\n'
string|'"arrrrrgh"'
op|','
nl|'\n'
op|'['
string|'"server1:123"'
op|','
string|'"server2:123"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_appliance_setup_inspect
dedent|''
name|'def'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'drives'
op|','
name|'forcetcg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'forcetcg'
op|':'
newline|'\n'
indent|'            '
name|'vfsimpl'
op|'.'
name|'force_tcg'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vfsimpl'
op|'.'
name|'force_tcg'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
nl|'\n'
name|'image'
op|','
nl|'\n'
name|'partition'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'forcetcg'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"force_tcg"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
name|'vfsimpl'
op|'.'
name|'force_tcg'
op|'('
name|'False'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'drives'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'drives'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/guestvgf-lv_root"'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/vda1"'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/guestvgf-lv_home"'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'2'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/boot"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'1'
op|']'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/home"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'2'
op|']'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'handle'
op|'='
name|'vfs'
op|'.'
name|'handle'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handle'
op|'.'
name|'closed'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_auto
dedent|''
name|'def'
name|'test_appliance_setup_inspect_auto'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drives'
op|'='
op|'['
op|'('
string|'"/dummy.qcow2"'
op|','
op|'{'
string|'"format"'
op|':'
string|'"qcow2"'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
name|'drives'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_tcg
dedent|''
name|'def'
name|'test_appliance_setup_inspect_tcg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drives'
op|'='
op|'['
op|'('
string|'"/dummy.qcow2"'
op|','
op|'{'
string|'"format"'
op|':'
string|'"qcow2"'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
name|'drives'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_raw
dedent|''
name|'def'
name|'test_appliance_setup_inspect_raw'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drives'
op|'='
op|'['
op|'('
string|'"/dummy.img"'
op|','
op|'{'
string|'"format"'
op|':'
string|'"raw"'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|'.'
name|'rawfile'
op|','
name|'drives'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_lvm
dedent|''
name|'def'
name|'test_appliance_setup_inspect_lvm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drives'
op|'='
op|'['
op|'('
string|'"/dev/volgroup/myvol"'
op|','
op|'{'
string|'"format"'
op|':'
string|'"raw"'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|'.'
name|'lvmfile'
op|','
name|'drives'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_rbd
dedent|''
name|'def'
name|'test_appliance_setup_inspect_rbd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drives'
op|'='
op|'['
op|'('
string|'"mypool/myvol"'
op|','
op|'{'
string|'"format"'
op|':'
string|'"raw"'
op|','
nl|'\n'
string|'"protocol"'
op|':'
string|'"rbd"'
op|','
nl|'\n'
string|'"username"'
op|':'
string|'"cthulu"'
op|','
nl|'\n'
string|'"secret"'
op|':'
string|'"arrrrrgh"'
op|','
nl|'\n'
string|'"server"'
op|':'
op|'['
string|'"server1:123"'
op|','
nl|'\n'
string|'"server2:123"'
op|']'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_test_appliance_setup_inspect'
op|'('
name|'self'
op|'.'
name|'rbdfile'
op|','
name|'drives'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_no_root_raises
dedent|''
name|'def'
name|'test_appliance_setup_inspect_no_root_raises'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
nl|'\n'
name|'partition'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
comment|'# call setup to init the handle so we can stub it'
nl|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_inspect_os
name|'def'
name|'fake_inspect_os'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
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
name|'vfs'
op|'.'
name|'handle'
op|','
string|"'inspect_os'"
op|','
name|'fake_inspect_os'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
name|'vfs'
op|'.'
name|'setup_os_inspect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_inspect_multi_boots_raises
dedent|''
name|'def'
name|'test_appliance_setup_inspect_multi_boots_raises'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
nl|'\n'
name|'partition'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
comment|'# call setup to init the handle so we can stub it'
nl|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_inspect_os
name|'def'
name|'fake_inspect_os'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
string|"'fake1'"
op|','
string|"'fake2'"
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
name|'vfs'
op|'.'
name|'handle'
op|','
string|"'inspect_os'"
op|','
name|'fake_inspect_os'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
name|'vfs'
op|'.'
name|'setup_os_inspect'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_static_nopart
dedent|''
name|'def'
name|'test_appliance_setup_static_nopart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
nl|'\n'
name|'partition'
op|'='
name|'None'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sda"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'handle'
op|'='
name|'vfs'
op|'.'
name|'handle'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handle'
op|'.'
name|'closed'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_appliance_setup_static_part
dedent|''
name|'def'
name|'test_appliance_setup_static_part'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|','
nl|'\n'
name|'partition'
op|'='
number|'2'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'backend_settings'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sda2"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'mounts'
op|'['
number|'0'
op|']'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'handle'
op|'='
name|'vfs'
op|'.'
name|'handle'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handle'
op|'.'
name|'running'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handle'
op|'.'
name|'closed'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'handle'
op|'.'
name|'mounts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_makepath
dedent|''
name|'def'
name|'test_makepath'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"/some/dir"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"/other/dir"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"/some/dir"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"/other/dir"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/dir"'
op|']'
op|'['
string|'"isdir"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/other/dir"'
op|']'
op|'['
string|'"isdir"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_append_file
dedent|''
name|'def'
name|'test_append_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'append_file'
op|'('
string|'"/some/file"'
op|','
string|'" Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"/some/file"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Hello World Goodbye"'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"content"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_replace_file
dedent|''
name|'def'
name|'test_replace_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'replace_file'
op|'('
string|'"/some/file"'
op|','
string|'"Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"/some/file"'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Goodbye"'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"content"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_file
dedent|''
name|'def'
name|'test_read_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Hello World"'
op|','
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_has_file
dedent|''
name|'def'
name|'test_has_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'has_file'
op|'('
string|'"/some/file"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'has_file'
op|'('
string|'"/other/file"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_permissions
dedent|''
name|'def'
name|'test_set_permissions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0o700'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"mode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_permissions'
op|'('
string|'"/some/file"'
op|','
number|'0o7777'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0o7777'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"mode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_ownership
dedent|''
name|'def'
name|'test_set_ownership'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'100'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'100'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
string|'"fred"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'105'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'100'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
name|'None'
op|','
string|'"users"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'105'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'500'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
string|'"joe"'
op|','
string|'"admins"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'110'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'600'
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_close_on_error
dedent|''
name|'def'
name|'test_close_on_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'kwargs'
op|'['
string|"'close_on_exit'"
op|']'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fakeguestfs'
op|'.'
name|'GuestFS'
op|','
string|"'SUPPORT_CLOSE_ON_EXIT'"
op|','
name|'False'
op|')'
newline|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'close_on_exit'"
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_python_return_dict
dedent|''
name|'def'
name|'test_python_return_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'kwargs'
op|'['
string|"'python_return_dict'"
op|']'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fakeguestfs'
op|'.'
name|'GuestFS'
op|','
string|"'SUPPORT_RETURN_DICT'"
op|','
name|'False'
op|')'
newline|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'python_return_dict'"
op|','
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_debug_disable
dedent|''
name|'def'
name|'test_setup_debug_disable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'trace_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'verbose_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'event_callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_debug_enabled
dedent|''
name|'def'
name|'test_setup_debug_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'debug'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'guestfs'"
op|')'
newline|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'trace_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'verbose_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'event_callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_format_fs
dedent|''
name|'def'
name|'test_get_format_fs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'rawfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ext3'"
op|','
name|'vfs'
op|'.'
name|'get_image_fs'
op|'('
op|')'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|','
string|"'setup_os'"
op|')'
newline|'\n'
DECL|member|test_setup_mount
name|'def'
name|'test_setup_mount'
op|'('
name|'self'
op|','
name|'setup_os'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'setup_os'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|','
string|"'setup_os'"
op|')'
newline|'\n'
DECL|member|test_setup_mount_false
name|'def'
name|'test_setup_mount_false'
op|'('
name|'self'
op|','
name|'setup_os'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
name|'mount'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'setup_os'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.access'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.uname'"
op|','
name|'return_value'
op|'='
op|'('
string|"'Linux'"
op|','
string|"''"
op|','
string|"'kernel_name'"
op|')'
op|')'
newline|'\n'
DECL|member|test_appliance_setup_inspect_capabilties_fail_with_ubuntu
name|'def'
name|'test_appliance_setup_inspect_capabilties_fail_with_ubuntu'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_uname'
op|','
nl|'\n'
name|'mock_access'
op|')'
op|':'
newline|'\n'
comment|'# In ubuntu os will default host kernel as 600 permission'
nl|'\n'
indent|'        '
name|'m'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'m'
op|'.'
name|'launch'
op|'.'
name|'side_effect'
op|'='
name|'Exception'
newline|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSGuestFS'
op|'('
name|'self'
op|'.'
name|'qcowfile'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'eventlet.tpool.Proxy'"
op|','
name|'return_value'
op|'='
name|'m'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'LibguestfsCannotReadKernel'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'inspect_capabilities'
op|')'
newline|'\n'
name|'m'
op|'.'
name|'add_drive'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'/dev/null'"
op|')'
newline|'\n'
name|'m'
op|'.'
name|'launch'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_access'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'/boot/vmlinuz-kernel_name'"
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'mock_uname'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
