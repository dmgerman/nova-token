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
name|'type_filter'
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
DECL|class|TestTypeFilter
name|'class'
name|'TestTypeFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_type_filter
indent|'    '
name|'def'
name|'test_type_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'type_filter'
op|'.'
name|'TypeAffinityFilter'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'fake_host'"
op|','
string|"'fake_node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'target_id'
op|'='
number|'1'
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
name|'MagicMock'
op|'('
op|')'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'id'
op|'='
name|'target_id'
op|')'
op|')'
newline|'\n'
comment|'# True since no instances on host'
nl|'\n'
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
comment|'# Add an instance with the same instance_type_id'
nl|'\n'
name|'inst1'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'uuid'
op|'='
string|"'aa'"
op|','
name|'instance_type_id'
op|'='
name|'target_id'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'instances'
op|'='
op|'{'
name|'inst1'
op|'.'
name|'uuid'
op|':'
name|'inst1'
op|'}'
newline|'\n'
comment|'# True since only same instance_type_id on host'
nl|'\n'
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
comment|'# Add an instance with a different instance_type_id'
nl|'\n'
name|'diff_type'
op|'='
name|'target_id'
op|'+'
number|'1'
newline|'\n'
name|'inst2'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'uuid'
op|'='
string|"'bb'"
op|','
name|'instance_type_id'
op|'='
name|'diff_type'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'instances'
op|'.'
name|'update'
op|'('
op|'{'
name|'inst2'
op|'.'
name|'uuid'
op|':'
name|'inst2'
op|'}'
op|')'
newline|'\n'
comment|'# False since host now has an instance of a different type'
nl|'\n'
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
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_type_filter_no_metadata
name|'def'
name|'test_aggregate_type_filter_no_metadata'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'type_filter'
op|'.'
name|'AggregateTypeAffinityFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake1'"
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'fake_host'"
op|','
string|"'fake_node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# tests when no instance_type is defined for aggregate'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
comment|'# True as no instance_type set for aggregate'
nl|'\n'
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
name|'agg_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
string|"'instance_type'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_type_filter_single_instance_type
name|'def'
name|'test_aggregate_type_filter_single_instance_type'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'type_filter'
op|'.'
name|'AggregateTypeAffinityFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake1'"
op|')'
op|')'
newline|'\n'
name|'spec_obj2'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake2'"
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'fake_host'"
op|','
string|"'fake_node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# tests when a single instance_type is defined for an aggregate'
nl|'\n'
comment|'# using legacy single value syntax'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'fake1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# True as instance_type is allowed for aggregate'
nl|'\n'
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
comment|'# False as instance_type is not allowed for aggregate'
nl|'\n'
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
name|'spec_obj2'
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
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_type_filter_multi_aggregate
name|'def'
name|'test_aggregate_type_filter_multi_aggregate'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'type_filter'
op|'.'
name|'AggregateTypeAffinityFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake1'"
op|')'
op|')'
newline|'\n'
name|'spec_obj2'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake2'"
op|')'
op|')'
newline|'\n'
name|'spec_obj3'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake3'"
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'fake_host'"
op|','
string|"'fake_node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# tests when a single instance_type is defined for multiple aggregates'
nl|'\n'
comment|'# using legacy single value syntax'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'fake1'"
op|','
string|"'fake2'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# True as instance_type is allowed for first aggregate'
nl|'\n'
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
comment|'# True as instance_type is allowed for second aggregate'
nl|'\n'
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
name|'spec_obj2'
op|')'
op|')'
newline|'\n'
comment|'# False as instance_type is not allowed for aggregates'
nl|'\n'
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
name|'spec_obj3'
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
string|"'nova.scheduler.filters.utils.aggregate_values_from_key'"
op|')'
newline|'\n'
DECL|member|test_aggregate_type_filter_multi_instance_type
name|'def'
name|'test_aggregate_type_filter_multi_instance_type'
op|'('
name|'self'
op|','
name|'agg_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'type_filter'
op|'.'
name|'AggregateTypeAffinityFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake1'"
op|')'
op|')'
newline|'\n'
name|'spec_obj2'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake2'"
op|')'
op|')'
newline|'\n'
name|'spec_obj3'
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
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'name'
op|'='
string|"'fake3'"
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'fake_host'"
op|','
string|"'fake_node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# tests when multiple instance_types are defined for aggregate'
nl|'\n'
name|'agg_mock'
op|'.'
name|'return_value'
op|'='
name|'set'
op|'('
op|'['
string|"'fake1,fake2'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# True as instance_type is allowed for aggregate'
nl|'\n'
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
comment|'# True as instance_type is allowed for aggregate'
nl|'\n'
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
name|'spec_obj2'
op|')'
op|')'
newline|'\n'
comment|'# False as instance_type is not allowed for aggregate'
nl|'\n'
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
name|'spec_obj3'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
