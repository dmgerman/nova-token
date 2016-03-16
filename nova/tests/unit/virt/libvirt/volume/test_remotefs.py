begin_unit
comment|'# Copyright 2014 Cloudbase Solutions Srl'
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
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'remotefs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteFSTestCase
name|'class'
name|'RemoteFSTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remote filesystem operations test case."""'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
DECL|member|_test_mount_share
name|'def'
name|'_test_mount_share'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'already_mounted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'already_mounted'
op|':'
newline|'\n'
indent|'            '
name|'err_msg'
op|'='
string|"'Device or resource busy'"
newline|'\n'
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
op|'['
nl|'\n'
name|'None'
op|','
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
name|'err_msg'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'remotefs'
op|'.'
name|'mount_share'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_type'
op|','
nl|'\n'
name|'options'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_options'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_type'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_options'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mount_new_share
dedent|''
name|'def'
name|'test_mount_new_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_mount_share'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mount_already_mounted_share
dedent|''
name|'def'
name|'test_mount_already_mounted_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_mount_share'
op|'('
name|'already_mounted'
op|'='
name|'True'
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
string|"'execute'"
op|')'
newline|'\n'
DECL|member|test_unmount_share
name|'def'
name|'test_unmount_share'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'unmount_share'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'umount'"
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'attempts'
op|'='
number|'3'
op|','
nl|'\n'
name|'delay_on_retry'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'tempfile.mkdtemp'"
op|','
name|'return_value'
op|'='
string|"'/tmp/Mercury'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_remove_remote_file_rsync
name|'def'
name|'test_remove_remote_file_rsync'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_mkdtemp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'remove_file'
op|'('
string|"'host'"
op|','
string|"'dest'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'rsync_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
nl|'\n'
string|"'--delete'"
op|','
string|"'--include'"
op|','
nl|'\n'
string|"'dest'"
op|','
string|"'--exclude'"
op|','
string|"'*'"
op|','
nl|'\n'
string|"'/tmp/Mercury/'"
op|','
string|"'host:'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'0'
op|']'
op|','
name|'rsync_call_args'
op|')'
newline|'\n'
name|'rm_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rm'"
op|','
string|"'-rf'"
op|','
string|"'/tmp/Mercury'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'1'
op|']'
op|','
name|'rm_call_args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'mock_execute'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_mkdtemp'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.ssh_execute'"
op|')'
newline|'\n'
DECL|member|test_remove_remote_file_ssh
name|'def'
name|'test_remove_remote_file_ssh'
op|'('
name|'self'
op|','
name|'mock_ssh_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'SshDriver'
op|'('
op|')'
op|'.'
name|'remove_file'
op|'('
string|"'host'"
op|','
string|"'dest'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_ssh_execute'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
string|"'host'"
op|','
string|"'rm'"
op|','
string|"'dest'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
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
string|"'tempfile.mkdtemp'"
op|','
name|'return_value'
op|'='
string|"'/tmp/Venus'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_remove_remote_dir_rsync
name|'def'
name|'test_remove_remote_dir_rsync'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_mkdtemp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'remove_dir'
op|'('
string|"'host'"
op|','
string|"'dest'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'rsync_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
nl|'\n'
string|"'--delete-excluded'"
op|','
string|"'/tmp/Venus/'"
op|','
nl|'\n'
string|"'host:dest'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'0'
op|']'
op|','
name|'rsync_call_args'
op|')'
newline|'\n'
name|'rsync_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
nl|'\n'
string|"'--delete'"
op|','
string|"'--include'"
op|','
nl|'\n'
string|"'dest'"
op|','
string|"'--exclude'"
op|','
string|"'*'"
op|','
nl|'\n'
string|"'/tmp/Venus/'"
op|','
string|"'host:'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'1'
op|']'
op|','
name|'rsync_call_args'
op|')'
newline|'\n'
name|'rm_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rm'"
op|','
string|"'-rf'"
op|','
string|"'/tmp/Venus'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'2'
op|']'
op|','
name|'rm_call_args'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_mkdtemp'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.ssh_execute'"
op|')'
newline|'\n'
DECL|member|test_remove_remote_dir_ssh
name|'def'
name|'test_remove_remote_dir_ssh'
op|'('
name|'self'
op|','
name|'mock_ssh_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'SshDriver'
op|'('
op|')'
op|'.'
name|'remove_dir'
op|'('
string|"'host'"
op|','
string|"'dest'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_ssh_execute'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
string|"'host'"
op|','
string|"'rm'"
op|','
string|"'-rf'"
op|','
string|"'dest'"
op|','
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
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
string|"'tempfile.mkdtemp'"
op|','
name|'return_value'
op|'='
string|"'/tmp/Mars'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_create_remote_file_rsync
name|'def'
name|'test_create_remote_file_rsync'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_mkdtemp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'create_file'
op|'('
string|"'host'"
op|','
string|"'dest_dir'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mkdir_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
string|"'/tmp/Mars/'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'0'
op|']'
op|','
name|'mkdir_call_args'
op|')'
newline|'\n'
name|'touch_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'touch'"
op|','
string|"'/tmp/Mars/dest_dir'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'1'
op|']'
op|','
name|'touch_call_args'
op|')'
newline|'\n'
name|'rsync_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
string|"'--relative'"
op|','
nl|'\n'
string|"'--no-implied-dirs'"
op|','
nl|'\n'
string|"'/tmp/Mars/./dest_dir'"
op|','
string|"'host:/'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'2'
op|']'
op|','
name|'rsync_call_args'
op|')'
newline|'\n'
name|'rm_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rm'"
op|','
string|"'-rf'"
op|','
string|"'/tmp/Mars'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'3'
op|']'
op|','
name|'rm_call_args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'mock_execute'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_mkdtemp'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.ssh_execute'"
op|')'
newline|'\n'
DECL|member|test_create_remote_file_ssh
name|'def'
name|'test_create_remote_file_ssh'
op|'('
name|'self'
op|','
name|'mock_ssh_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'SshDriver'
op|'('
op|')'
op|'.'
name|'create_file'
op|'('
string|"'host'"
op|','
string|"'dest_dir'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_ssh_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'host'"
op|','
string|"'touch'"
op|','
nl|'\n'
string|"'dest_dir'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
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
string|"'tempfile.mkdtemp'"
op|','
name|'return_value'
op|'='
string|"'/tmp/Jupiter'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_create_remote_dir_rsync
name|'def'
name|'test_create_remote_dir_rsync'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_mkdtemp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'create_dir'
op|'('
string|"'host'"
op|','
string|"'dest_dir'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mkdir_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
string|"'/tmp/Jupiter/dest_dir'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'0'
op|']'
op|','
name|'mkdir_call_args'
op|')'
newline|'\n'
name|'rsync_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
string|"'--relative'"
op|','
nl|'\n'
string|"'--no-implied-dirs'"
op|','
nl|'\n'
string|"'/tmp/Jupiter/./dest_dir'"
op|','
string|"'host:/'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'1'
op|']'
op|','
name|'rsync_call_args'
op|')'
newline|'\n'
name|'rm_call_args'
op|'='
name|'mock'
op|'.'
name|'call'
op|'('
string|"'rm'"
op|','
string|"'-rf'"
op|','
string|"'/tmp/Jupiter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_execute'
op|'.'
name|'mock_calls'
op|'['
number|'2'
op|']'
op|','
name|'rm_call_args'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_mkdtemp'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.ssh_execute'"
op|')'
newline|'\n'
DECL|member|test_create_remote_dir_ssh
name|'def'
name|'test_create_remote_dir_ssh'
op|'('
name|'self'
op|','
name|'mock_ssh_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'SshDriver'
op|'('
op|')'
op|'.'
name|'create_dir'
op|'('
string|"'host'"
op|','
string|"'dest_dir'"
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_ssh_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'host'"
op|','
string|"'mkdir'"
op|','
nl|'\n'
string|"'-p'"
op|','
string|"'dest_dir'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
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
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_remote_copy_file_rsync
name|'def'
name|'test_remote_copy_file_rsync'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'copy_file'
op|'('
string|"'1.2.3.4:/home/star_wars'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'compression'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
nl|'\n'
string|"'1.2.3.4:/home/star_wars'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
nl|'\n'
string|"'--compress'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
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
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_remote_copy_file_rsync_without_compression
name|'def'
name|'test_remote_copy_file_rsync_without_compression'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'RsyncDriver'
op|'('
op|')'
op|'.'
name|'copy_file'
op|'('
string|"'1.2.3.4:/home/star_wars'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'compression'
op|'='
name|'False'
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
nl|'\n'
string|"'1.2.3.4:/home/star_wars'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
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
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_remote_copy_file_ssh
name|'def'
name|'test_remote_copy_file_ssh'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'SshDriver'
op|'('
op|')'
op|'.'
name|'copy_file'
op|'('
string|"'1.2.3.4:/home/SpaceOdyssey'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
name|'None'
op|','
name|'None'
op|','
name|'True'
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'scp'"
op|','
nl|'\n'
string|"'1.2.3.4:/home/SpaceOdyssey'"
op|','
nl|'\n'
string|"'/home/favourite'"
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
