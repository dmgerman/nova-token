begin_unit
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
name|'import'
name|'fixtures'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'test_volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'scality'
newline|'\n'
nl|'\n'
nl|'\n'
name|'class'
name|'LibvirtScalityVolumeDriverTestCase'
op|'('
nl|'\n'
DECL|class|LibvirtScalityVolumeDriverTestCase
name|'test_volume'
op|'.'
name|'LibvirtVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_scality_driver
indent|'    '
name|'def'
name|'test_libvirt_scality_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'TEST_MOUNT'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tempdir'
op|','
string|"'fake_mount'"
op|')'
newline|'\n'
name|'TEST_CONFIG'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tempdir'
op|','
string|"'fake_config'"
op|')'
newline|'\n'
name|'TEST_VOLDIR'
op|'='
string|"'volumes'"
newline|'\n'
name|'TEST_VOLNAME'
op|'='
string|"'volume_name'"
newline|'\n'
name|'TEST_CONN_INFO'
op|'='
op|'{'
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'sofs_path'"
op|':'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TEST_VOLDIR'
op|','
name|'TEST_VOLNAME'
op|')'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'TEST_VOLPATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TEST_MOUNT'
op|','
nl|'\n'
name|'TEST_VOLDIR'
op|','
nl|'\n'
name|'TEST_VOLNAME'
op|')'
newline|'\n'
name|'open'
op|'('
name|'TEST_CONFIG'
op|','
string|'"w+"'
op|')'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TEST_MOUNT'
op|','
string|"'sys'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_access_wrapper
name|'def'
name|'_access_wrapper'
op|'('
name|'path'
op|','
name|'flags'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|'=='
string|"'/sbin/mount.sofs'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'os'
op|'.'
name|'access'
op|'('
name|'path'
op|','
name|'flags'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|','
string|"'access'"
op|','
name|'_access_wrapper'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scality_sofs_config'
op|'='
name|'TEST_CONFIG'
op|','
nl|'\n'
name|'scality_sofs_mount_point'
op|'='
name|'TEST_MOUNT'
op|','
nl|'\n'
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
name|'driver'
op|'='
name|'scality'
op|'.'
name|'LibvirtScalityVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'connect_volume'
op|'('
name|'TEST_CONN_INFO'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
nl|'\n'
name|'device_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'TEST_MOUNT'
op|','
nl|'\n'
name|'TEST_CONN_INFO'
op|'['
string|"'data'"
op|']'
op|'['
string|"'sofs_path'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device_path'
op|','
nl|'\n'
name|'TEST_CONN_INFO'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'driver'
op|'.'
name|'get_config'
op|'('
name|'TEST_CONN_INFO'
op|','
name|'self'
op|'.'
name|'disk_info'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assertFileTypeEquals'
op|'('
name|'tree'
op|','
name|'TEST_VOLPATH'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
