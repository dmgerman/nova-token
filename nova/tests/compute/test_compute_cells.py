begin_unit
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|variable|ORIG_COMPUTE_API
name|'ORIG_COMPUTE_API'
op|'='
name|'None'
newline|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enable'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
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
name|'inst'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'network_api'
op|','
string|"'deallocate_for_instance'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
name|'None'
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
name|'inst'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'network_api'
op|','
string|"'deallocate_for_instance'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
name|'None'
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
DECL|member|test_get_migrations
dedent|''
name|'def'
name|'test_get_migrations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'cell_name'"
op|':'
string|"'ChildCell'"
op|','
string|"'status'"
op|':'
string|"'confirmed'"
op|'}'
newline|'\n'
name|'migrations'
op|'='
op|'{'
string|"'migrations'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1234'
op|'}'
op|']'
op|'}'
newline|'\n'
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
string|"'get_migrations'"
op|')'
newline|'\n'
name|'cells_rpcapi'
op|'.'
name|'get_migrations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'migrations'
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
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_migrations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'migrations'
op|','
name|'response'
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
