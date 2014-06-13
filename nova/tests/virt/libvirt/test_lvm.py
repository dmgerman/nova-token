begin_unit
comment|'# Copyright 2012 NTT Data. All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2012 Yahoo! Inc. All Rights Reserved.'
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
name|'contextlib'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
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
name|'processutils'
newline|'\n'
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
name|'libvirt'
name|'import'
name|'lvm'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LvmTestCase
name|'class'
name|'LvmTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_volume_size
indent|'    '
name|'def'
name|'test_get_volume_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
number|'123456789'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'blockdev'"
op|','
string|"'--getsize64'"
op|','
string|"'/dev/foo'"
op|')'
op|']'
newline|'\n'
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
name|'size'
op|'='
name|'lvm'
op|'.'
name|'get_volume_size'
op|'('
string|"'/dev/foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'size'
op|','
number|'123456789'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lvm_clear
dedent|''
name|'def'
name|'test_lvm_clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_lvm_size
indent|'        '
name|'def'
name|'fake_lvm_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'lvm_size'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
dedent|''
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
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
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
name|'lvm'
op|','
string|"'get_volume_size'"
op|','
name|'fake_lvm_size'
op|')'
newline|'\n'
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
comment|'# Test the correct dd commands are run for various sizes'
nl|'\n'
name|'lvm_size'
op|'='
number|'1'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v1'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'lvm_size'
op|'='
number|'1024'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1024'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v2'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'lvm_size'
op|'='
number|'1025'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1024'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v3'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v3'"
op|','
nl|'\n'
string|"'seek=1024'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'lvm_size'
op|'='
number|'1048576'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1048576'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v4'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'oflag=direct'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'lvm_size'
op|'='
number|'1048577'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1048576'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v5'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'oflag=direct'"
op|')'
op|']'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v5'"
op|','
nl|'\n'
string|"'seek=1048576'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v5'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'lvm_size'
op|'='
number|'1234567'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1048576'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v6'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'oflag=direct'"
op|')'
op|']'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1024'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v6'"
op|','
nl|'\n'
string|"'seek=1024'"
op|','
string|"'count=181'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'expected_commands'
op|'+='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v6'"
op|','
nl|'\n'
string|"'seek=1233920'"
op|','
string|"'count=647'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v6'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test volume_clear_size limits the size'
nl|'\n'
name|'lvm_size'
op|'='
number|'10485761'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear_size'"
op|','
string|"'1'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1048576'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v7'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'oflag=direct'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v7'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear_size'"
op|','
string|"'2'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'lvm_size'
op|'='
number|'1048576'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1048576'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/v9'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'oflag=direct'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/v9'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test volume_clear=shred'
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear'"
op|','
string|"'shred'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear_size'"
op|','
string|"'0'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'lvm_size'
op|'='
number|'1048576'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'shred'"
op|','
string|"'-n3'"
op|','
string|"'-s1048576'"
op|','
string|"'/dev/va'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/va'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear'"
op|','
string|"'shred'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear_size'"
op|','
string|"'1'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'lvm_size'
op|'='
number|'10485761'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'shred'"
op|','
string|"'-n3'"
op|','
string|"'-s1048576'"
op|','
string|"'/dev/vb'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/vb'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test volume_clear=none does nothing'
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear'"
op|','
string|"'none'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/vc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
comment|"# Test volume_clear=invalid falls back to the default 'zero'"
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'volume_clear'"
op|','
string|"'invalid'"
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'lvm_size'
op|'='
number|'1'
newline|'\n'
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'dd'"
op|','
string|"'bs=1'"
op|','
string|"'if=/dev/zero'"
op|','
string|"'of=/dev/vd'"
op|','
nl|'\n'
string|"'seek=0'"
op|','
string|"'count=1'"
op|','
string|"'conv=fdatasync'"
op|')'
op|']'
newline|'\n'
name|'lvm'
op|'.'
name|'clear_volume'
op|'('
string|"'/dev/vd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fail_remove_all_logical_volumes
dedent|''
name|'def'
name|'test_fail_remove_all_logical_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_execute
indent|'        '
name|'def'
name|'fake_execute'
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
name|'if'
string|"'vol2'"
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
string|"'Error'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'lvm'
op|','
string|"'clear_volume'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'libvirt_utils'
op|','
string|"'execute'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'fake_execute'
op|')'
op|')'
name|'as'
op|'('
name|'mock_clear'
op|','
name|'mock_execute'
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
name|'VolumesNotRemoved'
op|','
nl|'\n'
name|'lvm'
op|'.'
name|'remove_volumes'
op|','
nl|'\n'
op|'['
string|"'vol1'"
op|','
string|"'vol2'"
op|','
string|"'vol3'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'mock_execute'
op|'.'
name|'call_count'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
