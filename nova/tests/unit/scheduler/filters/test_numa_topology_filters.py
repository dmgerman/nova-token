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
name|'uuid'
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
name|'numa_topology_filter'
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
DECL|class|TestNUMATopologyFilter
name|'class'
name|'TestNUMATopologyFilter'
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
name|'TestNUMATopologyFilter'
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
name|'numa_topology_filter'
op|'.'
name|'NUMATopologyFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_numa_topology_filter_pass
dedent|''
name|'def'
name|'test_numa_topology_filter_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'16.0'
op|','
nl|'\n'
string|"'ram_allocation_ratio'"
op|':'
number|'1.5'
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
DECL|member|test_numa_topology_filter_numa_instance_no_numa_host_fail
dedent|''
name|'def'
name|'test_numa_topology_filter_numa_instance_no_numa_host_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
op|'{'
string|"'pci_stats'"
op|':'
name|'None'
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
DECL|member|test_numa_topology_filter_numa_host_no_numa_instance_pass
dedent|''
name|'def'
name|'test_numa_topology_filter_numa_host_no_numa_instance_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
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
DECL|member|test_numa_topology_filter_fail_fit
dedent|''
name|'def'
name|'test_numa_topology_filter_fail_fit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'2'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'16.0'
op|','
nl|'\n'
string|"'ram_allocation_ratio'"
op|':'
number|'1.5'
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
DECL|member|test_numa_topology_filter_fail_memory
dedent|''
name|'def'
name|'test_numa_topology_filter_fail_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
nl|'\n'
name|'memory'
op|'='
number|'1024'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'16.0'
op|','
nl|'\n'
string|"'ram_allocation_ratio'"
op|':'
number|'1'
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
DECL|member|test_numa_topology_filter_fail_cpu
dedent|''
name|'def'
name|'test_numa_topology_filter_fail_cpu'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|','
number|'4'
op|','
number|'5'
op|']'
op|')'
op|','
nl|'\n'
name|'memory'
op|'='
number|'512'
op|')'
op|']'
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ram_allocation_ratio'"
op|':'
number|'1.5'
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
DECL|member|test_numa_topology_filter_pass_set_limit
dedent|''
name|'def'
name|'test_numa_topology_filter_pass_set_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_topology'
op|'='
name|'objects'
op|'.'
name|'InstanceNUMATopology'
op|'('
nl|'\n'
name|'cells'
op|'='
op|'['
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceNUMACell'
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
number|'3'
op|']'
op|')'
op|','
name|'memory'
op|'='
number|'512'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'numa_topology'
op|'='
name|'instance_topology'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
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
string|"'node1'"
op|','
nl|'\n'
op|'{'
string|"'numa_topology'"
op|':'
name|'fakes'
op|'.'
name|'NUMA_TOPOLOGY'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'cpu_allocation_ratio'"
op|':'
number|'21'
op|','
nl|'\n'
string|"'ram_allocation_ratio'"
op|':'
number|'1.3'
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
name|'limits'
op|'='
name|'host'
op|'.'
name|'limits'
op|'['
string|"'numa_topology'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limits'
op|'.'
name|'cpu_allocation_ratio'
op|','
number|'21'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limits'
op|'.'
name|'ram_allocation_ratio'
op|','
number|'1.3'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
