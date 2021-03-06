begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
nl|'\n'
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
op|'.'
name|'objects'
name|'import'
name|'instance_fault'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'uuidsentinel'
name|'as'
name|'uuids'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_faults
name|'fake_faults'
op|'='
op|'{'
nl|'\n'
string|"'fake-uuid'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'faults_instance'
op|','
string|"'code'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'msg1'"
op|','
string|"'details'"
op|':'
string|"'details'"
op|','
string|"'host'"
op|':'
string|"'host'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'faults_instance'
op|','
string|"'code'"
op|':'
number|'456'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'msg2'"
op|','
string|"'details'"
op|':'
string|"'details'"
op|','
string|"'host'"
op|':'
string|"'host'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceFault
name|'class'
name|'_TestInstanceFault'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_latest_for_instance
indent|'    '
name|'def'
name|'test_get_latest_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_fault_get_by_instance_uuids'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_faults'
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
name|'fault'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|'.'
name|'get_latest_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'key'
op|']'
op|','
name|'fault'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_latest_for_instance_with_none
dedent|''
dedent|''
name|'def'
name|'test_get_latest_for_instance_with_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_fault_get_by_instance_uuids'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
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
name|'fault'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|'.'
name|'get_latest_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_instance
dedent|''
name|'def'
name|'test_get_by_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_fault_get_by_instance_uuids'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_faults'
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
name|'faults'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFaultList'
op|'.'
name|'get_by_instance_uuids'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'db_fault'
name|'in'
name|'enumerate'
op|'('
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'db_fault'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|'['
name|'index'
op|']'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'faults'
op|'['
name|'index'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_instance_with_none
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_get_by_instance_with_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'instance_fault_get_by_instance_uuids'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_fault_get_by_instance_uuids'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
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
name|'faults'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFaultList'
op|'.'
name|'get_by_instance_uuids'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake-uuid'"
op|']'
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
name|'faults'
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
string|"'nova.cells.rpcapi.CellsAPI.instance_fault_create_at_top'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_fault_create'"
op|')'
newline|'\n'
DECL|member|_test_create
name|'def'
name|'_test_create'
op|'('
name|'self'
op|','
name|'update_cells'
op|','
name|'mock_create'
op|','
name|'cells_fault_create'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_create'
op|'.'
name|'return_value'
op|'='
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'fault'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'fault'
op|'.'
name|'instance_uuid'
op|'='
name|'uuids'
op|'.'
name|'faults_instance'
newline|'\n'
name|'fault'
op|'.'
name|'code'
op|'='
number|'456'
newline|'\n'
name|'fault'
op|'.'
name|'message'
op|'='
string|"'foo'"
newline|'\n'
name|'fault'
op|'.'
name|'details'
op|'='
string|"'you screwed up'"
newline|'\n'
name|'fault'
op|'.'
name|'host'
op|'='
string|"'myhost'"
newline|'\n'
name|'fault'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'fault'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'mock_create'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'faults_instance'
op|','
nl|'\n'
string|"'code'"
op|':'
number|'456'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'details'"
op|':'
string|"'you screwed up'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'myhost'"
op|'}'
op|')'
newline|'\n'
name|'if'
name|'update_cells'
op|':'
newline|'\n'
indent|'            '
name|'cells_fault_create'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'fake_faults'
op|'['
string|"'fake-uuid'"
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cells_fault_create'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_no_cells
dedent|''
dedent|''
name|'def'
name|'test_create_no_cells'
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
name|'enable'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_api_cell
dedent|''
name|'def'
name|'test_create_api_cell'
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
name|'cell_type'
op|'='
string|"'api'"
op|','
name|'enable'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_compute_cell
dedent|''
name|'def'
name|'test_create_compute_cell'
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
name|'cell_type'
op|'='
string|"'compute'"
op|','
name|'enable'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_already_created
dedent|''
name|'def'
name|'test_create_already_created'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fault'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'fault'
op|'.'
name|'id'
op|'='
number|'1'
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
name|'fault'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceFault'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceFault
name|'_TestInstanceFault'
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
name|'TestInstanceFaultRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestInstanceFaultRemote
name|'_TestInstanceFault'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
