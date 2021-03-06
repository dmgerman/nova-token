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
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'os_win'
name|'import'
name|'exceptions'
name|'as'
name|'os_win_exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
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
name|'hyperv'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'snapshotops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotOpsTestCase
name|'class'
name|'SnapshotOpsTestCase'
op|'('
name|'test_base'
op|'.'
name|'HyperVBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V SnapshotOps class."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'SnapshotOpsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
string|"'fake_context'"
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'='
name|'snapshotops'
op|'.'
name|'SnapshotOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vmutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vhdutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.glance.get_remote_image_service'"
op|')'
newline|'\n'
DECL|member|test_save_glance_image
name|'def'
name|'test_save_glance_image'
op|'('
name|'self'
op|','
name|'mock_get_remote_image_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_metadata'
op|'='
op|'{'
string|'"is_public"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|'"vhd"'
op|','
nl|'\n'
string|'"container_format"'
op|':'
string|'"bare"'
op|','
nl|'\n'
string|'"properties"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'glance_image_service'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_get_remote_image_service'
op|'.'
name|'return_value'
op|'='
op|'('
name|'glance_image_service'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_save_glance_image'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|','
nl|'\n'
name|'image_vhd_path'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'mock_get_remote_image_service'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'open'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'PATH'
op|','
string|"'rb'"
op|')'
newline|'\n'
name|'glance_image_service'
op|'.'
name|'update'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|','
name|'image_metadata'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'open'
op|'('
op|')'
op|'.'
name|'__enter__'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.hyperv.snapshotops.SnapshotOps._save_glance_image'"
op|')'
newline|'\n'
DECL|member|_test_snapshot
name|'def'
name|'_test_snapshot'
op|'('
name|'self'
op|','
name|'mock_save_glance_image'
op|','
name|'base_disk_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mock_update'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'fake_src_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'fake'"
op|','
string|"'path'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_root_vhd_path'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'fake_src_path'
op|')'
newline|'\n'
name|'fake_exp_dir'
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
string|"'fake'"
op|','
string|"'exp'"
op|')'
op|','
string|"'dir'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'get_export_dir'
op|'.'
name|'return_value'
op|'='
name|'fake_exp_dir'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_parent_path'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'base_disk_path'
op|')'
newline|'\n'
name|'fake_snapshot_path'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vmutils'
op|'.'
name|'take_vm_snapshot'
op|'.'
name|'return_value'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'snapshot'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'mock_instance'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|','
nl|'\n'
name|'update_task_state'
op|'='
name|'mock_update'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vmutils'
op|'.'
name|'take_vm_snapshot'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock_instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'mock_lookup_path'
op|'='
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_root_vhd_path'
newline|'\n'
name|'mock_lookup_path'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock_instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'mock_get_vhd_path'
op|'='
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_parent_path'
newline|'\n'
name|'mock_get_vhd_path'
op|'.'
name|'assert_called_once_with'
op|'('
name|'fake_src_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'get_export_dir'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock_instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'fake_src_path'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fake_exp_dir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'fake_src_path'
op|')'
op|')'
op|')'
op|']'
newline|'\n'
name|'dest_vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fake_exp_dir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'fake_src_path'
op|')'
op|')'
newline|'\n'
name|'if'
name|'base_disk_path'
op|':'
newline|'\n'
indent|'            '
name|'basename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'base_disk_path'
op|')'
newline|'\n'
name|'base_dest_disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fake_exp_dir'
op|','
name|'basename'
op|')'
newline|'\n'
name|'expected'
op|'.'
name|'append'
op|'('
name|'mock'
op|'.'
name|'call'
op|'('
name|'base_disk_path'
op|','
name|'base_dest_disk_path'
op|')'
op|')'
newline|'\n'
name|'mock_reconnect'
op|'='
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vhdutils'
op|'.'
name|'reconnect_parent_vhd'
newline|'\n'
name|'mock_reconnect'
op|'.'
name|'assert_called_once_with'
op|'('
name|'dest_vhd_path'
op|','
nl|'\n'
name|'base_dest_disk_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vhdutils'
op|'.'
name|'merge_vhd'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'dest_vhd_path'
op|')'
newline|'\n'
name|'mock_save_glance_image'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|','
name|'base_dest_disk_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mock_save_glance_image'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'IMAGE_ID'
op|','
name|'dest_vhd_path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'copyfile'
op|'.'
name|'has_calls'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'expected_update'
op|'='
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_UPLOADING'
op|','
nl|'\n'
name|'expected_state'
op|'='
name|'task_states'
op|'.'
name|'IMAGE_PENDING_UPLOAD'
op|')'
op|']'
newline|'\n'
name|'mock_update'
op|'.'
name|'has_calls'
op|'('
name|'expected_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_vmutils'
op|'.'
name|'remove_vm_snapshot'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'fake_snapshot_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'_pathutils'
op|'.'
name|'rmtree'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'fake_exp_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot
dedent|''
name|'def'
name|'test_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'fake'"
op|','
string|"'disk'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_snapshot'
op|'('
name|'base_disk_path'
op|'='
name|'base_disk_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_no_base_disk
dedent|''
name|'def'
name|'test_snapshot_no_base_disk'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_snapshot'
op|'('
name|'base_disk_path'
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
op|'.'
name|'object'
op|'('
name|'snapshotops'
op|'.'
name|'SnapshotOps'
op|','
string|"'_snapshot'"
op|')'
newline|'\n'
DECL|member|test_snapshot_instance_not_found
name|'def'
name|'test_snapshot_instance_not_found'
op|'('
name|'self'
op|','
name|'mock_snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'mock_snapshot'
op|'.'
name|'side_effect'
op|'='
name|'os_win_exc'
op|'.'
name|'HyperVVMNotFoundException'
op|'('
nl|'\n'
name|'vm_name'
op|'='
name|'mock_instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'snapshot'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'mock_instance'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'image_id'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'update_task_state'
op|')'
newline|'\n'
nl|'\n'
name|'mock_snapshot'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'mock_instance'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'image_id'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'update_task_state'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
