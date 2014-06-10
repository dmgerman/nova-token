begin_unit
comment|'#    Copyright 2013 Red Hat Inc.'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'rpcapi'
name|'as'
name|'cells_rpcapi'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'block_device'
name|'as'
name|'block_device_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestBlockDeviceMappingObject
name|'class'
name|'_TestBlockDeviceMappingObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|fake_bdm
indent|'    '
name|'def'
name|'fake_bdm'
op|'('
name|'self'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'instance'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'fake_bdm'
op|'='
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
name|'or'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'fake-snapshot-id-1'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'fake_bdm'
op|'['
string|"'instance'"
op|']'
op|'='
name|'instance'
newline|'\n'
dedent|''
name|'return'
name|'fake_bdm'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_bdm'
op|'='
name|'self'
op|'.'
name|'fake_bdm'
op|'('
op|')'
newline|'\n'
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
nl|'\n'
name|'db'
op|','
string|"'block_device_mapping_update'"
op|','
name|'return_value'
op|'='
name|'fake_bdm'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
nl|'\n'
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|','
string|"'bdm_update_or_create_at_top'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'bdm_update_mock'
op|','
name|'cells_update_mock'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bdm_object'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|')'
newline|'\n'
name|'bdm_object'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'bdm_object'
op|'.'
name|'volume_id'
op|'='
string|"'fake_volume_id'"
newline|'\n'
name|'bdm_object'
op|'.'
name|'save'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'bdm_update_mock'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
op|'{'
string|"'volume_id'"
op|':'
string|"'fake_volume_id'"
op|'}'
op|','
nl|'\n'
name|'legacy'
op|'='
name|'False'
op|')'
newline|'\n'
name|'cells_update_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fake_bdm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_instance_changed
dedent|''
dedent|''
name|'def'
name|'test_save_instance_changed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdm_object'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|')'
newline|'\n'
name|'bdm_object'
op|'.'
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'bdm_object'
op|'.'
name|'save'
op|','
name|'self'
op|'.'
name|'context'
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
name|'db'
op|','
string|"'block_device_mapping_get_by_volume_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_volume_id
name|'def'
name|'test_get_by_volume_id'
op|'('
name|'self'
op|','
name|'get_by_vol_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_vol_id'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_bdm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vol_bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'.'
name|'get_by_volume_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-volume-id'"
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'block_device_obj'
op|'.'
name|'BLOCK_DEVICE_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vol_bdm'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRemotes'
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
name|'db'
op|','
string|"'block_device_mapping_get_by_volume_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_volume_id_not_found
name|'def'
name|'test_get_by_volume_id_not_found'
op|'('
name|'self'
op|','
name|'get_by_vol_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_vol_id'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeBDMNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'.'
name|'get_by_volume_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-volume-id'"
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
name|'db'
op|','
string|"'block_device_mapping_get_by_volume_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_volume_instance_uuid_missmatch
name|'def'
name|'test_get_by_volume_instance_uuid_missmatch'
op|'('
name|'self'
op|','
name|'get_by_vol_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_bdm_vol'
op|'='
name|'self'
op|'.'
name|'fake_bdm'
op|'('
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'other-fake-instance'"
op|'}'
op|')'
newline|'\n'
name|'get_by_vol_id'
op|'.'
name|'return_value'
op|'='
name|'fake_bdm_vol'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolume'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'.'
name|'get_by_volume_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-volume-id'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake-instance'"
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
name|'db'
op|','
string|"'block_device_mapping_get_by_volume_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_volume_id_with_expected
name|'def'
name|'test_get_by_volume_id_with_expected'
op|'('
name|'self'
op|','
name|'get_by_vol_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_vol_id'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_bdm'
op|'('
nl|'\n'
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vol_bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'.'
name|'get_by_volume_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-volume-id'"
op|','
name|'expected_attrs'
op|'='
op|'['
string|"'instance'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'block_device_obj'
op|'.'
name|'BLOCK_DEVICE_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vol_bdm'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
dedent|''
name|'get_by_vol_id'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-volume-id'"
op|','
nl|'\n'
op|'['
string|"'instance'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_mocked
dedent|''
name|'def'
name|'test_create_mocked'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'volume_id'"
op|':'
string|"'fake-vol-id'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|'}'
newline|'\n'
name|'fake_bdm'
op|'='
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
name|'values'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'db'
op|','
string|"'block_device_mapping_create'"
op|','
name|'return_value'
op|'='
name|'fake_bdm'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|','
nl|'\n'
string|"'bdm_update_or_create_at_top'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'bdm_create_mock'
op|','
name|'cells_update_mock'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'bdm'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bdm_create_mock'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|','
name|'legacy'
op|'='
name|'False'
op|')'
newline|'\n'
name|'cells_update_mock'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'fake_bdm'
op|','
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'volume_id'"
op|':'
string|"'fake-vol-id'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|'}'
newline|'\n'
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|','
nl|'\n'
string|"'bdm_update_or_create_at_top'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bdm'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'v'
op|','
name|'getattr'
op|'('
name|'bdm'
op|','
name|'k'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_fails
dedent|''
dedent|''
name|'def'
name|'test_create_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'volume_id'"
op|':'
string|"'fake-vol-id'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|'}'
newline|'\n'
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'bdm'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'bdm'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_fails_instance
dedent|''
name|'def'
name|'test_create_fails_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'volume_id'"
op|':'
string|"'fake-vol-id'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'instance_obj'
op|'.'
name|'Instance'
op|'('
op|')'
op|'}'
newline|'\n'
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'bdm'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_mocked
dedent|''
name|'def'
name|'test_destroy_mocked'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'volume_id'"
op|':'
string|"'fake-vol-id'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
string|"'device_name'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
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
name|'db'
op|','
string|"'block_device_mapping_destroy'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|','
string|"'bdm_destroy_at_top'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'bdm_del'
op|','
name|'cells_destroy'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'bdm'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bdm_del'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'cells_destroy'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|'['
string|"'instance_uuid'"
op|']'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'values'
op|'['
string|"'device_name'"
op|']'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'values'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestBlockDeviceMappingObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestBlockDeviceMappingObject
name|'_TestBlockDeviceMappingObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteBlockDeviceMappingObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteBlockDeviceMappingObject
name|'_TestBlockDeviceMappingObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestBlockDeviceMappingListObject
dedent|''
name|'class'
name|'_TestBlockDeviceMappingListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|fake_bdm
indent|'    '
name|'def'
name|'fake_bdm'
op|'('
name|'self'
op|','
name|'bdm_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_bdm'
op|'='
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'bdm_id'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'fake-snapshot-id-1'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'fake_bdm'
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
name|'db'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid
name|'def'
name|'test_get_by_instance_uuid'
op|'('
name|'self'
op|','
name|'get_all_by_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fakes'
op|'='
op|'['
name|'self'
op|'.'
name|'fake_bdm'
op|'('
number|'123'
op|')'
op|','
name|'self'
op|'.'
name|'fake_bdm'
op|'('
number|'456'
op|')'
op|']'
newline|'\n'
name|'get_all_by_inst'
op|'.'
name|'return_value'
op|'='
name|'fakes'
newline|'\n'
name|'bdm_list'
op|'='
op|'('
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMappingList'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_instance_uuid'"
op|')'
op|')'
newline|'\n'
name|'for'
name|'faked'
op|','
name|'got'
name|'in'
name|'zip'
op|'('
name|'fakes'
op|','
name|'bdm_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'got'
op|','
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'faked'
op|'['
string|"'id'"
op|']'
op|','
name|'got'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid_no_result
name|'def'
name|'test_get_by_instance_uuid_no_result'
op|'('
name|'self'
op|','
name|'get_all_by_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_all_by_inst'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'bdm_list'
op|'='
op|'('
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMappingList'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_instance_uuid'"
op|')'
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
name|'bdm_list'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_root_volume_metadata
dedent|''
name|'def'
name|'test_root_volume_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_volume'
op|'='
op|'{'
nl|'\n'
string|"'volume_image_metadata'"
op|':'
op|'{'
string|"'vol_test_key'"
op|':'
string|"'vol_test_value'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|FakeVolumeApi
name|'class'
name|'FakeVolumeApi'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'            '
name|'def'
name|'get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'fake_volume'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'block_device_mapping'
op|'='
name|'block_device_obj'
op|'.'
name|'block_device_make_list'
op|'('
name|'None'
op|','
op|'['
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake_volume_id'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'volume_meta'
op|'='
name|'block_device_mapping'
op|'.'
name|'root_metadata'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|','
name|'FakeVolumeApi'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_volume'
op|'['
string|"'volume_image_metadata'"
op|']'
op|','
name|'volume_meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_root_image_metadata
dedent|''
name|'def'
name|'test_root_image_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_image'
op|'='
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'img_test_key'"
op|':'
string|"'img_test_value'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|FakeImageApi
name|'class'
name|'FakeImageApi'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|show
indent|'            '
name|'def'
name|'show'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'fake_image'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'block_device_mapping'
op|'='
name|'block_device_obj'
op|'.'
name|'block_device_make_list'
op|'('
name|'None'
op|','
op|'['
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'image'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|','
nl|'\n'
string|"'image_id'"
op|':'
string|'"fake-image"'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
name|'block_device_mapping'
op|'.'
name|'root_metadata'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'FakeImageApi'
op|'('
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_image'
op|'['
string|"'properties'"
op|']'
op|','
name|'image_meta'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestBlockDeviceMappingListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestBlockDeviceMappingListObject
name|'_TestBlockDeviceMappingListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteBlockDeviceMappingListObject'
op|'('
nl|'\n'
DECL|class|TestRemoteBlockDeviceMappingListObject
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
name|'_TestBlockDeviceMappingListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
