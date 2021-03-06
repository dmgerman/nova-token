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
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
DECL|variable|fake_obj_numa
name|'fake_obj_numa'
op|'='
name|'objects'
op|'.'
name|'NUMATopology'
op|'('
nl|'\n'
DECL|variable|cells
name|'cells'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'2'
op|','
name|'memory_usage'
op|'='
number|'256'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
nl|'\n'
DECL|variable|siblings
name|'siblings'
op|'='
op|'['
op|']'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'1'
op|','
name|'memory_usage'
op|'='
number|'128'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
nl|'\n'
DECL|variable|siblings
name|'siblings'
op|'='
op|'['
op|']'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestNUMA
name|'class'
name|'_TestNUMA'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_convert_wipe
indent|'    '
name|'def'
name|'test_convert_wipe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d1'
op|'='
name|'fake_obj_numa'
op|'.'
name|'_to_dict'
op|'('
op|')'
newline|'\n'
name|'d2'
op|'='
name|'objects'
op|'.'
name|'NUMATopology'
op|'.'
name|'obj_from_primitive'
op|'('
name|'d1'
op|')'
op|'.'
name|'_to_dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'d1'
op|','
name|'d2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_legacy_limits
dedent|''
name|'def'
name|'test_from_legacy_limits'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'old_style'
op|'='
op|'{'
string|'"cells"'
op|':'
op|'['
nl|'\n'
op|'{'
string|'"mem"'
op|':'
op|'{'
nl|'\n'
string|'"total"'
op|':'
number|'1024'
op|','
nl|'\n'
string|'"limit"'
op|':'
number|'2048'
op|'}'
op|','
nl|'\n'
string|'"cpu_limit"'
op|':'
number|'96.0'
op|','
nl|'\n'
string|'"cpus"'
op|':'
string|'"0,1,2,3,4,5"'
op|','
nl|'\n'
string|'"id"'
op|':'
number|'0'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'limits'
op|'='
name|'objects'
op|'.'
name|'NUMATopologyLimits'
op|'.'
name|'obj_from_db_obj'
op|'('
name|'old_style'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'16.0'
op|','
name|'limits'
op|'.'
name|'cpu_allocation_ratio'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2.0'
op|','
name|'limits'
op|'.'
name|'ram_allocation_ratio'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_legacy_limits
dedent|''
name|'def'
name|'test_to_legacy_limits'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
name|'objects'
op|'.'
name|'NUMATopologyLimits'
op|'('
nl|'\n'
name|'cpu_allocation_ratio'
op|'='
number|'16'
op|','
nl|'\n'
name|'ram_allocation_ratio'
op|'='
number|'2'
op|')'
newline|'\n'
name|'host_topo'
op|'='
name|'objects'
op|'.'
name|'NUMATopology'
op|'('
name|'cells'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'1024'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'old_style'
op|'='
op|'{'
string|"'cells'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'mem'"
op|':'
op|'{'
string|"'total'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'limit'"
op|':'
number|'2048.0'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'cpus'"
op|':'
string|"'1,2'"
op|','
nl|'\n'
string|"'cpu_limit'"
op|':'
number|'32.0'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'old_style'
op|','
name|'limits'
op|'.'
name|'to_dict_legacy'
op|'('
name|'host_topo'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_free_cpus
dedent|''
name|'def'
name|'test_free_cpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'NUMATopology'
op|'('
name|'cells'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'2'
op|','
name|'memory_usage'
op|'='
number|'256'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'NUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'1'
op|','
name|'memory_usage'
op|'='
number|'128'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|')'
nl|'\n'
op|']'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'2'
op|']'
op|')'
op|','
name|'obj'
op|'.'
name|'cells'
op|'['
number|'0'
op|']'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'obj'
op|'.'
name|'cells'
op|'['
number|'1'
op|']'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pinning_logic
dedent|''
name|'def'
name|'test_pinning_logic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'numacell'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'2'
op|','
name|'memory_usage'
op|'='
number|'256'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'numacell'
op|'.'
name|'pin_cpus'
op|'('
name|'set'
op|'('
op|'['
number|'2'
op|','
number|'3'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'4'
op|']'
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningUnknown'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'pin_cpus'
op|','
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'55'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'pin_cpus'
op|','
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'4'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningUnknown'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus'
op|','
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'55'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus'
op|','
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'4'
op|']'
op|')'
op|')'
newline|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pinning_with_siblings
dedent|''
name|'def'
name|'test_pinning_with_siblings'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'numacell'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'2'
op|','
name|'memory_usage'
op|'='
number|'256'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|']'
op|')'
op|','
name|'set'
op|'('
op|'['
number|'2'
op|','
number|'4'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'numacell'
op|'.'
name|'pin_cpus_with_siblings'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus_with_siblings'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|']'
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus_with_siblings'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'3'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'pin_cpus_with_siblings'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'4'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|','
nl|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus_with_siblings'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'3'
op|']'
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
name|'numacell'
op|'.'
name|'unpin_cpus_with_siblings'
op|'('
name|'set'
op|'('
op|'['
number|'4'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
name|'numacell'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pages_topology_wipe
dedent|''
name|'def'
name|'test_pages_topology_wipe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pages_topology'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
nl|'\n'
name|'size_kb'
op|'='
number|'2048'
op|','
name|'total'
op|'='
number|'1024'
op|','
name|'used'
op|'='
number|'512'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2048'
op|','
name|'pages_topology'
op|'.'
name|'size_kb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1024'
op|','
name|'pages_topology'
op|'.'
name|'total'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'512'
op|','
name|'pages_topology'
op|'.'
name|'used'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'512'
op|','
name|'pages_topology'
op|'.'
name|'free'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1048576'
op|','
name|'pages_topology'
op|'.'
name|'free_kb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_fit_hugepages
dedent|''
name|'def'
name|'test_can_fit_hugepages'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
nl|'\n'
name|'id'
op|'='
number|'0'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'1024'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
op|']'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
nl|'\n'
name|'size_kb'
op|'='
number|'4'
op|','
name|'total'
op|'='
number|'1548736'
op|','
name|'used'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
nl|'\n'
name|'size_kb'
op|'='
number|'2048'
op|','
name|'total'
op|'='
number|'513'
op|','
name|'used'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
nl|'\n'
name|'size_kb'
op|'='
number|'1048576'
op|','
name|'total'
op|'='
number|'4'
op|','
name|'used'
op|'='
number|'1'
op|','
name|'reserved'
op|'='
number|'1'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'pagesize'
op|'='
number|'2048'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'20'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'21'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'19'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'pagesize'
op|'='
number|'1048576'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'20'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'20'
op|'*'
number|'2'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|'('
name|'pagesize'
op|','
number|'2'
op|'**'
number|'20'
op|'*'
number|'3'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'MemoryPageSizeNotSupported'
op|','
nl|'\n'
name|'cell'
op|'.'
name|'can_fit_hugepages'
op|','
number|'12345'
op|','
number|'2'
op|'**'
number|'20'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_behavior
dedent|''
name|'def'
name|'test_default_behavior'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_cell'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
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
name|'inst_cell'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_pages_equivalent
dedent|''
name|'def'
name|'test_numa_pages_equivalent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pt1'
op|','
name|'pt2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_pages_not_equivalent
dedent|''
name|'def'
name|'test_numa_pages_not_equivalent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'33'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pt1'
op|','
name|'pt2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_pages_not_equivalent_missing_a
dedent|''
name|'def'
name|'test_numa_pages_not_equivalent_missing_a'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pt1'
op|','
name|'pt2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_pages_not_equivalent_missing_b
dedent|''
name|'def'
name|'test_numa_pages_not_equivalent_missing_b'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'pt1'
op|','
name|'pt2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_equivalent
dedent|''
name|'def'
name|'test_numa_cell_equivalent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_not_equivalent
dedent|''
name|'def'
name|'test_numa_cell_not_equivalent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_not_equivalent_missing_a
dedent|''
name|'def'
name|'test_numa_cell_not_equivalent_missing_a'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_not_equivalent_missing_b
dedent|''
name|'def'
name|'test_numa_cell_not_equivalent_missing_b'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_equivalent_different_pages
dedent|''
name|'def'
name|'test_numa_cell_equivalent_different_pages'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
name|'pt1'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
name|'pt2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_cell_not_equivalent_different_pages
dedent|''
name|'def'
name|'test_numa_cell_not_equivalent_different_pages'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pt1'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'0'
op|')'
newline|'\n'
name|'pt2'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'32'
op|','
name|'used'
op|'='
number|'1'
op|')'
newline|'\n'
name|'cell1'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
name|'pt1'
op|']'
op|')'
newline|'\n'
name|'cell2'
op|'='
name|'objects'
op|'.'
name|'NUMACell'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'cpuset'
op|'='
name|'set'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'32'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
number|'10'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
number|'3'
op|','
number|'4'
op|']'
op|')'
op|','
nl|'\n'
name|'siblings'
op|'='
op|'['
name|'set'
op|'('
op|'['
number|'5'
op|','
number|'6'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
name|'pt2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'cell1'
op|','
name|'cell2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserved_property_not_set
dedent|''
name|'def'
name|'test_reserved_property_not_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'objects'
op|'.'
name|'NUMAPagesTopology'
op|'('
nl|'\n'
comment|'# To have reserved not set is similar than to have receive'
nl|'\n'
comment|'# a NUMAPageTopology version 1.0'
nl|'\n'
name|'size_kb'
op|'='
number|'1024'
op|','
name|'total'
op|'='
number|'64'
op|','
name|'used'
op|'='
number|'32'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'32'
op|','
name|'p'
op|'.'
name|'free'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestNUMA'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestNUMA
name|'_TestNUMA'
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
name|'TestNUMARemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestNUMARemote
name|'_TestNUMA'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
