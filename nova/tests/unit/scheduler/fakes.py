begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nFakes For Scheduler tests.\n"""'
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
name|'import'
name|'host_manager'
newline|'\n'
nl|'\n'
DECL|variable|NUMA_TOPOLOGY
name|'NUMA_TOPOLOGY'
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
number|'0'
op|','
name|'memory_usage'
op|'='
number|'0'
op|','
name|'mempages'
op|'='
op|'['
op|']'
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
number|'0'
op|','
name|'memory_usage'
op|'='
number|'0'
op|','
name|'mempages'
op|'='
op|'['
op|']'
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
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|COMPUTE_NODES
name|'COMPUTE_NODES'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'1024'
op|','
name|'memory_mb'
op|'='
number|'1024'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
name|'None'
op|','
name|'free_ram_mb'
op|'='
number|'512'
op|','
name|'vcpus_used'
op|'='
number|'1'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'512'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'updated_at'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|','
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'0'
op|','
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|"'foo'"
op|','
name|'supported_hv_specs'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pci_device_pools'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
name|'None'
op|','
name|'stats'
op|'='
name|'None'
op|','
name|'metrics'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'id'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'2048'
op|','
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'1024'
op|','
name|'free_ram_mb'
op|'='
number|'1024'
op|','
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'1024'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'updated_at'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|','
name|'hypervisor_hostname'
op|'='
string|"'node2'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'0'
op|','
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|"'foo'"
op|','
name|'supported_hv_specs'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pci_device_pools'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
name|'None'
op|','
name|'stats'
op|'='
name|'None'
op|','
name|'metrics'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'id'
op|'='
number|'3'
op|','
name|'local_gb'
op|'='
number|'4096'
op|','
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'3333'
op|','
name|'free_ram_mb'
op|'='
number|'3072'
op|','
name|'vcpus_used'
op|'='
number|'1'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'3072'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'updated_at'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host3'"
op|','
name|'hypervisor_hostname'
op|'='
string|"'node3'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'0'
op|','
name|'numa_topology'
op|'='
name|'NUMA_TOPOLOGY'
op|'.'
name|'_to_json'
op|'('
op|')'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|"'foo'"
op|','
name|'supported_hv_specs'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pci_device_pools'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
name|'None'
op|','
name|'stats'
op|'='
name|'None'
op|','
name|'metrics'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'id'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'8192'
op|','
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'8192'
op|','
name|'free_ram_mb'
op|'='
number|'8192'
op|','
name|'vcpus_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'8888'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'updated_at'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host4'"
op|','
name|'hypervisor_hostname'
op|'='
string|"'node4'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'0'
op|','
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|"'foo'"
op|','
name|'supported_hv_specs'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'pci_device_pools'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
name|'None'
op|','
name|'stats'
op|'='
name|'None'
op|','
name|'metrics'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
comment|'# Broken entry'
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
nl|'\n'
name|'id'
op|'='
number|'5'
op|','
name|'local_gb'
op|'='
number|'1024'
op|','
name|'memory_mb'
op|'='
number|'1024'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake'"
op|','
name|'hypervisor_hostname'
op|'='
string|"'fake-hyp'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|SERVICES
name|'SERVICES'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host1'"
op|','
name|'disabled'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host2'"
op|','
name|'disabled'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host3'"
op|','
name|'disabled'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Service'
op|'('
name|'host'
op|'='
string|"'host4'"
op|','
name|'disabled'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_service_by_host
name|'def'
name|'get_service_by_host'
op|'('
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'services'
op|'='
op|'['
name|'service'
name|'for'
name|'service'
name|'in'
name|'SERVICES'
name|'if'
name|'service'
op|'.'
name|'host'
op|'=='
name|'host'
op|']'
newline|'\n'
name|'return'
name|'services'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHostState
dedent|''
name|'class'
name|'FakeHostState'
op|'('
name|'host_manager'
op|'.'
name|'HostState'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'node'
op|','
name|'attribute_dict'
op|','
name|'instances'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeHostState'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'if'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
name|'inst'
op|'.'
name|'uuid'
op|':'
name|'inst'
name|'for'
name|'inst'
name|'in'
name|'instances'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'for'
op|'('
name|'key'
op|','
name|'val'
op|')'
name|'in'
name|'attribute_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
