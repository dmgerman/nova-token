begin_unit
comment|'# Copyright (c) 2015 Quobyte Inc.'
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
string|'"""Unit tests for the Quobyte volume driver module."""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
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
name|'fileutils'
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
name|'quobyte'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuobyteTestCase
name|'class'
name|'QuobyteTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'fileutils'
op|','
string|'"ensure_tree"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|')'
newline|'\n'
DECL|member|test_quobyte_mount_volume
name|'def'
name|'test_quobyte_mount_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_ensure_tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'mount_volume'
op|'('
name|'quobyte_volume'
op|','
name|'export_mnt_base'
op|')'
newline|'\n'
nl|'\n'
name|'mock_ensure_tree'
op|'.'
name|'assert_called_once_with'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'mount.quobyte'"
op|','
nl|'\n'
name|'quobyte_volume'
op|','
nl|'\n'
name|'export_mnt_base'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'4'
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_has_calls'
op|'('
name|'expected_commands'
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
name|'fileutils'
op|','
string|'"ensure_tree"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|')'
newline|'\n'
DECL|member|test_quobyte_mount_volume_with_config
name|'def'
name|'test_quobyte_mount_volume_with_config'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_execute'
op|','
nl|'\n'
name|'mock_ensure_tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
name|'config_file_dummy'
op|'='
string|'"/etc/quobyte/dummy.conf"'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'mount_volume'
op|'('
name|'quobyte_volume'
op|','
nl|'\n'
name|'export_mnt_base'
op|','
nl|'\n'
name|'config_file_dummy'
op|')'
newline|'\n'
nl|'\n'
name|'mock_ensure_tree'
op|'.'
name|'assert_called_once_with'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'mount.quobyte'"
op|','
nl|'\n'
name|'quobyte_volume'
op|','
nl|'\n'
name|'export_mnt_base'
op|','
nl|'\n'
string|"'-c'"
op|','
nl|'\n'
name|'config_file_dummy'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'4'
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_has_calls'
op|'('
name|'expected_commands'
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
name|'fileutils'
op|','
string|'"ensure_tree"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'processutils'
op|'.'
nl|'\n'
name|'ProcessExecutionError'
op|')'
op|')'
newline|'\n'
DECL|member|test_quobyte_mount_volume_fails
name|'def'
name|'test_quobyte_mount_volume_fails'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_ensure_tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|','
nl|'\n'
name|'quobyte'
op|'.'
name|'mount_volume'
op|','
nl|'\n'
name|'quobyte_volume'
op|','
nl|'\n'
name|'export_mnt_base'
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
name|'utils'
op|','
string|'"execute"'
op|')'
newline|'\n'
DECL|member|test_quobyte_umount_volume
name|'def'
name|'test_quobyte_umount_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'umount_volume'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'umount.quobyte'"
op|','
nl|'\n'
name|'export_mnt_base'
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
name|'quobyte'
op|'.'
name|'LOG'
op|','
string|'"error"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|')'
newline|'\n'
DECL|member|test_quobyte_umount_volume_warns
name|'def'
name|'test_quobyte_umount_volume_warns'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_execute'
op|','
nl|'\n'
name|'mock_debug'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|exec_side_effect
name|'def'
name|'exec_side_effect'
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
name|'exerror'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
op|')'
newline|'\n'
name|'exerror'
op|'.'
name|'message'
op|'='
string|'"Device or resource busy"'
newline|'\n'
name|'raise'
name|'exerror'
newline|'\n'
dedent|''
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
name|'exec_side_effect'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'umount_volume'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'mock_debug'
op|'.'
nl|'\n'
name|'assert_called_once_with'
op|'('
string|'"The Quobyte volume at %s is still in use."'
op|','
nl|'\n'
name|'export_mnt_base'
op|')'
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
name|'quobyte'
op|'.'
name|'LOG'
op|','
string|'"exception"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|')'
op|')'
newline|'\n'
DECL|member|test_quobyte_umount_volume_fails
name|'def'
name|'test_quobyte_umount_volume_fails'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_execute'
op|','
nl|'\n'
name|'mock_exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'umount_volume'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'mock_exception'
op|'.'
nl|'\n'
name|'assert_called_once_with'
op|'('
string|'"Couldn\'t unmount "'
nl|'\n'
string|'"the Quobyte Volume at %s"'
op|','
nl|'\n'
name|'export_mnt_base'
op|')'
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
name|'os'
op|','
string|'"access"'
op|','
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|')'
newline|'\n'
DECL|member|test_quobyte_is_valid_volume
name|'def'
name|'test_quobyte_is_valid_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_access'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'quobyte'
op|'.'
name|'validate_volume'
op|'('
name|'export_mnt_base'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'getfattr'"
op|','
nl|'\n'
string|"'-n'"
op|','
nl|'\n'
string|"'quobyte.info'"
op|','
nl|'\n'
name|'export_mnt_base'
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
name|'utils'
op|','
string|'"execute"'
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'processutils'
op|'.'
nl|'\n'
name|'ProcessExecutionError'
op|')'
op|')'
newline|'\n'
DECL|member|test_quobyte_is_valid_volume_vol_not_valid_volume
name|'def'
name|'test_quobyte_is_valid_volume_vol_not_valid_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'quobyte'
op|'.'
name|'validate_volume'
op|','
nl|'\n'
name|'export_mnt_base'
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
name|'os'
op|','
string|'"access"'
op|','
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|'"execute"'
op|','
nl|'\n'
name|'side_effect'
op|'='
op|'('
name|'processutils'
op|'.'
nl|'\n'
name|'ProcessExecutionError'
op|')'
op|')'
newline|'\n'
DECL|member|test_quobyte_is_valid_volume_vol_no_valid_access
name|'def'
name|'test_quobyte_is_valid_volume_vol_no_valid_access'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_execute'
op|','
nl|'\n'
name|'mock_access'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'quobyte_volume'
op|'='
string|"'192.168.1.1/volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'quobyte_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'quobyte'
op|'.'
name|'validate_volume'
op|','
nl|'\n'
name|'export_mnt_base'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
