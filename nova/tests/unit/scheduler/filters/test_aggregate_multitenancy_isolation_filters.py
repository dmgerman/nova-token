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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'aggregate_multitenancy_isolation'
name|'as'
name|'ami'
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
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_metadata_get_by_host'"
op|')'
newline|'\n'
DECL|class|TestAggregateMultitenancyIsolationFilter
name|'class'
name|'TestAggregateMultitenancyIsolationFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'TestAggregateMultitenancyIsolationFilter'
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
name|'filt_cls'
op|'='
name|'ami'
op|'.'
name|'AggregateMultiTenancyIsolation'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_multi_tenancy_isolation_with_meta_passes
dedent|''
name|'def'
name|'test_aggregate_multi_tenancy_isolation_with_meta_passes'
op|'('
name|'self'
op|','
nl|'\n'
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'filter_tenant_id'"
op|':'
name|'set'
op|'('
op|'['
string|"'my_tenantid'"
op|']'
op|')'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'project_id'
op|'='
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_multi_tenancy_isolation_with_meta_passes_comma
dedent|''
name|'def'
name|'test_aggregate_multi_tenancy_isolation_with_meta_passes_comma'
op|'('
name|'self'
op|','
nl|'\n'
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'filter_tenant_id'"
op|':'
nl|'\n'
name|'set'
op|'('
op|'['
string|"'my_tenantid'"
op|','
string|"'mytenantid2'"
op|']'
op|')'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'project_id'
op|'='
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_multi_tenancy_isolation_fails
dedent|''
name|'def'
name|'test_aggregate_multi_tenancy_isolation_fails'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'filter_tenant_id'"
op|':'
name|'set'
op|'('
op|'['
string|"'other_tenantid'"
op|']'
op|')'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'project_id'
op|'='
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_multi_tenancy_isolation_fails_comma
dedent|''
name|'def'
name|'test_aggregate_multi_tenancy_isolation_fails_comma'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'filter_tenant_id'"
op|':'
nl|'\n'
name|'set'
op|'('
op|'['
string|"'other_tenantid'"
op|','
string|"'other_tenantid2'"
op|']'
op|')'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'project_id'
op|'='
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_multi_tenancy_isolation_no_meta_passes
dedent|''
name|'def'
name|'test_aggregate_multi_tenancy_isolation_no_meta_passes'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'project_id'
op|'='
string|"'my_tenantid'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'compute'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
