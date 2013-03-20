begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nTests For Compute w/ Cells\n"""'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'cells_api'
name|'as'
name|'compute_cells_api'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'compute'
name|'import'
name|'test_compute'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.test_compute_cells'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ORIG_COMPUTE_API
name|'ORIG_COMPUTE_API'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_call_to_cells
name|'def'
name|'stub_call_to_cells'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fn'
op|'='
name|'getattr'
op|'('
name|'ORIG_COMPUTE_API'
op|','
name|'method'
op|')'
newline|'\n'
name|'original_instance'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'original_instance'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'original_instance'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'original_instance'
newline|'\n'
comment|"# Restore this in 'child cell DB'"
nl|'\n'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Use NoopQuotaDriver in child cells.'
nl|'\n'
dedent|''
name|'saved_quotas'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
name|'quota'
op|'.'
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QuotaEngine'
op|'('
nl|'\n'
name|'quota_driver_class'
op|'='
name|'quota'
op|'.'
name|'NoopQuotaDriver'
op|'('
op|')'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fn'
op|'('
name|'context'
op|','
name|'instance'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'quota'
op|'.'
name|'QUOTAS'
op|'='
name|'saved_quotas'
newline|'\n'
name|'compute_api'
op|'.'
name|'QUOTAS'
op|'='
name|'saved_quotas'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_cast_to_cells
dedent|''
dedent|''
name|'def'
name|'stub_cast_to_cells'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fn'
op|'='
name|'getattr'
op|'('
name|'ORIG_COMPUTE_API'
op|','
name|'method'
op|')'
newline|'\n'
name|'original_instance'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'original_instance'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'original_instance'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'original_instance'
newline|'\n'
comment|"# Restore this in 'child cell DB'"
nl|'\n'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vm_state'
op|'='
name|'instance'
op|'['
string|"'vm_state'"
op|']'
op|','
nl|'\n'
name|'task_state'
op|'='
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Use NoopQuotaDriver in child cells.'
nl|'\n'
dedent|''
name|'saved_quotas'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
name|'quota'
op|'.'
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QuotaEngine'
op|'('
nl|'\n'
name|'quota_driver_class'
op|'='
name|'quota'
op|'.'
name|'NoopQuotaDriver'
op|'('
op|')'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'('
name|'context'
op|','
name|'instance'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'quota'
op|'.'
name|'QUOTAS'
op|'='
name|'saved_quotas'
newline|'\n'
name|'compute_api'
op|'.'
name|'QUOTAS'
op|'='
name|'saved_quotas'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|deploy_stubs
dedent|''
dedent|''
name|'def'
name|'deploy_stubs'
op|'('
name|'stubs'
op|','
name|'api'
op|','
name|'original_instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'call'
op|'='
name|'stub_call_to_cells'
newline|'\n'
name|'cast'
op|'='
name|'stub_cast_to_cells'
newline|'\n'
nl|'\n'
name|'if'
name|'original_instance'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'original_instance'
op|'='
name|'original_instance'
op|')'
newline|'\n'
name|'call'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'stub_call_to_cells'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'cast'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'stub_cast_to_cells'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'_call_to_cells'"
op|','
name|'call'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'_cast_to_cells'"
op|','
name|'cast'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_create_instance
dedent|''
name|'def'
name|'wrap_create_instance'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'func'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake
name|'def'
name|'fake'
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
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|','
string|"'_create_fake_instance'"
op|','
name|'fake'
op|')'
newline|'\n'
name|'original_instance'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'deploy_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
name|'original_instance'
op|'='
name|'original_instance'
op|')'
newline|'\n'
name|'return'
name|'func'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsComputeAPITestCase
dedent|''
name|'class'
name|'CellsComputeAPITestCase'
op|'('
name|'test_compute'
op|'.'
name|'ComputeAPITestCase'
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
name|'CellsComputeAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'global'
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'ORIG_COMPUTE_API'
op|'='
name|'self'
op|'.'
name|'compute_api'
newline|'\n'
nl|'\n'
DECL|function|_fake_cell_read_only
name|'def'
name|'_fake_cell_read_only'
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
name|'False'
newline|'\n'
nl|'\n'
DECL|function|_fake_validate_cell
dedent|''
name|'def'
name|'_fake_validate_cell'
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
newline|'\n'
nl|'\n'
DECL|function|_nop_update
dedent|''
name|'def'
name|'_nop_update'
op|'('
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute_cells_api'
op|'.'
name|'ComputeCellsAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'_cell_read_only'"
op|','
nl|'\n'
name|'_fake_cell_read_only'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'_validate_cell'"
op|','
nl|'\n'
name|'_fake_validate_cell'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(belliott) Don't update the instance state"
nl|'\n'
comment|'# for the tests at the API layer.  Let it happen after'
nl|'\n'
comment|'# the stub cast to cells so that expected_task_states'
nl|'\n'
comment|'# match.'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'update'"
op|','
name|'_nop_update'
op|')'
newline|'\n'
nl|'\n'
name|'deploy_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'compute_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_metadata
dedent|''
name|'def'
name|'test_instance_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test is incompatible with cells."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_live_migrate
dedent|''
name|'def'
name|'test_live_migrate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test is incompatible with cells."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_backdoor_port
dedent|''
name|'def'
name|'test_get_backdoor_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test is incompatible with cells."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_given_image_uuid
dedent|''
name|'def'
name|'test_snapshot_given_image_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test doesn\'t apply to API cell."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot
name|'def'
name|'test_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'test_snapshot'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot_image_metadata_inheritance
name|'def'
name|'test_snapshot_image_metadata_inheritance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'test_snapshot_image_metadata_inheritance'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot_minram_mindisk
name|'def'
name|'test_snapshot_minram_mindisk'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'test_snapshot_minram_mindisk'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot_minram_mindisk_VHD
name|'def'
name|'test_snapshot_minram_mindisk_VHD'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'test_snapshot_minram_mindisk_VHD'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot_minram_mindisk_img_missing_minram
name|'def'
name|'test_snapshot_minram_mindisk_img_missing_minram'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'test_snapshot_minram_mindisk_img_missing_minram'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_snapshot_minram_mindisk_no_image
name|'def'
name|'test_snapshot_minram_mindisk_no_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'test_snapshot_minram_mindisk_no_image'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_create_instance'
newline|'\n'
DECL|member|test_backup
name|'def'
name|'test_backup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'super'
op|'('
name|'CellsComputeAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'test_backup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_evacuate
dedent|''
name|'def'
name|'test_evacuate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test is incompatible with cells."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_instance_no_cell
dedent|''
name|'def'
name|'test_delete_instance_no_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells_rpcapi'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'cells_rpcapi'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'instance_delete_everywhere'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|"'_cast_to_cells'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'exc'
op|'='
name|'exception'
op|'.'
name|'InstanceUnknownCell'
op|'('
name|'instance_uuid'
op|'='
name|'inst'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'_cast_to_cells'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|','
nl|'\n'
string|"'delete'"
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'cells_rpcapi'
op|'.'
name|'instance_delete_everywhere'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'inst'
op|','
string|"'hard'"
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
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_delete_instance_no_cell
dedent|''
name|'def'
name|'test_soft_delete_instance_no_cell'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells_rpcapi'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'cells_rpcapi'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'cells_rpcapi'
op|','
nl|'\n'
string|"'instance_delete_everywhere'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|"'_cast_to_cells'"
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'exc'
op|'='
name|'exception'
op|'.'
name|'InstanceUnknownCell'
op|'('
name|'instance_uuid'
op|'='
name|'inst'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'_cast_to_cells'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|','
nl|'\n'
string|"'soft_delete'"
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'cells_rpcapi'
op|'.'
name|'instance_delete_everywhere'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'inst'
op|','
string|"'soft'"
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
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'soft_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsComputePolicyTestCase
dedent|''
dedent|''
name|'class'
name|'CellsComputePolicyTestCase'
op|'('
name|'test_compute'
op|'.'
name|'ComputePolicyTestCase'
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
name|'CellsComputePolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'global'
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'ORIG_COMPUTE_API'
op|'='
name|'self'
op|'.'
name|'compute_api'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute_cells_api'
op|'.'
name|'ComputeCellsAPI'
op|'('
op|')'
newline|'\n'
name|'deploy_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'compute_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'ORIG_COMPUTE_API'
newline|'\n'
name|'super'
op|'('
name|'CellsComputePolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
