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
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
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
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'compute_node'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'hv_spec'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_pci_device_pools'
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
DECL|variable|NOW
name|'NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
DECL|variable|fake_stats
name|'fake_stats'
op|'='
op|'{'
string|"'num_foo'"
op|':'
string|"'10'"
op|'}'
newline|'\n'
DECL|variable|fake_stats_db_format
name|'fake_stats_db_format'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'fake_stats'
op|')'
newline|'\n'
comment|'# host_ip is coerced from a string to an IPAddress'
nl|'\n'
comment|'# but needs to be converted to a string for the database format'
nl|'\n'
DECL|variable|fake_host_ip
name|'fake_host_ip'
op|'='
string|"'127.0.0.1'"
newline|'\n'
DECL|variable|fake_numa_topology
name|'fake_numa_topology'
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
op|')'
op|','
nl|'\n'
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
op|')'
op|']'
op|')'
newline|'\n'
DECL|variable|fake_numa_topology_db_format
name|'fake_numa_topology_db_format'
op|'='
name|'fake_numa_topology'
op|'.'
name|'_to_json'
op|'('
op|')'
newline|'\n'
DECL|variable|fake_hv_spec
name|'fake_hv_spec'
op|'='
name|'hv_spec'
op|'.'
name|'HVSpec'
op|'('
name|'arch'
op|'='
string|"'foo'"
op|','
name|'hv_type'
op|'='
string|"'bar'"
op|','
name|'vm_mode'
op|'='
string|"'foobar'"
op|')'
newline|'\n'
DECL|variable|fake_supported_hv_specs
name|'fake_supported_hv_specs'
op|'='
op|'['
name|'fake_hv_spec'
op|']'
newline|'\n'
comment|'# for backward compatibility, each supported instance object'
nl|'\n'
comment|'# is stored as a list in the database'
nl|'\n'
DECL|variable|fake_supported_hv_specs_db_format
name|'fake_supported_hv_specs_db_format'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
name|'fake_hv_spec'
op|'.'
name|'to_list'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
DECL|variable|fake_pci
name|'fake_pci'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'fake_pci_device_pools'
op|'.'
name|'fake_pool_list_primitive'
op|')'
newline|'\n'
DECL|variable|fake_compute_node
name|'fake_compute_node'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'service_id'"
op|':'
number|'456'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'4096'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'Hyper-Dan-VM-ware'"
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
number|'1001'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
string|"'vm.danplanet.com'"
op|','
nl|'\n'
string|"'free_ram_mb'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'free_disk_gb'"
op|':'
number|'256'
op|','
nl|'\n'
string|"'current_workload'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'running_vms'"
op|':'
number|'2013'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
string|"'Schmintel i786'"
op|','
nl|'\n'
string|"'disk_available_least'"
op|':'
number|'256'
op|','
nl|'\n'
string|"'metrics'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'stats'"
op|':'
name|'fake_stats_db_format'
op|','
nl|'\n'
string|"'host_ip'"
op|':'
name|'fake_host_ip'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fake_numa_topology_db_format'
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
name|'fake_supported_hv_specs_db_format'
op|','
nl|'\n'
string|"'pci_stats'"
op|':'
name|'fake_pci'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'# FIXME(sbauza) : For compatibility checking, to be removed once we are sure'
nl|'\n'
comment|'# that all computes are running latest DB version with host field in it.'
nl|'\n'
DECL|variable|fake_old_compute_node
name|'fake_old_compute_node'
op|'='
name|'fake_compute_node'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'del'
name|'fake_old_compute_node'
op|'['
string|"'host'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestComputeNodeObject
name|'class'
name|'_TestComputeNodeObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|supported_hv_specs_comparator
indent|'    '
name|'def'
name|'supported_hv_specs_comparator'
op|'('
name|'self'
op|','
name|'expected'
op|','
name|'obj_val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_val'
op|'='
op|'['
name|'inst'
op|'.'
name|'to_list'
op|'('
op|')'
name|'for'
name|'inst'
name|'in'
name|'obj_val'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'json_comparator'
op|'('
name|'expected'
op|','
name|'obj_val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pci_device_pools_comparator
dedent|''
name|'def'
name|'pci_device_pools_comparator'
op|'('
name|'self'
op|','
name|'expected'
op|','
name|'obj_val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_val'
op|'='
name|'obj_val'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'json_loads_comparator'
op|'('
name|'expected'
op|','
name|'obj_val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|json_loads_comparator
dedent|''
name|'def'
name|'json_loads_comparator'
op|'('
name|'self'
op|','
name|'expected'
op|','
name|'obj_val'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(edleafe): This is necessary because the dumps() version of the'
nl|'\n'
comment|"# PciDevicePoolList doesn't maintain ordering, so the output string"
nl|'\n'
comment|"# doesn't always match."
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'expected'
op|')'
op|','
name|'obj_val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|comparators
dedent|''
name|'def'
name|'comparators'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'stats'"
op|':'
name|'self'
op|'.'
name|'json_comparator'
op|','
nl|'\n'
string|"'host_ip'"
op|':'
name|'self'
op|'.'
name|'str_comparator'
op|','
nl|'\n'
string|"'supported_hv_specs'"
op|':'
name|'self'
op|'.'
name|'supported_hv_specs_comparator'
op|','
nl|'\n'
string|"'pci_device_pools'"
op|':'
name|'self'
op|'.'
name|'pci_device_pools_comparator'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|subs
dedent|''
name|'def'
name|'subs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'supported_hv_specs'"
op|':'
string|"'supported_instances'"
op|','
nl|'\n'
string|"'pci_device_pools'"
op|':'
string|"'pci_stats'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_id
dedent|''
name|'def'
name|'test_get_by_id'
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
string|"'compute_node_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_compute_node'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'Service'
op|','
string|"'get_by_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_get'"
op|')'
newline|'\n'
DECL|member|test_get_by_id_with_host_field_not_in_db
name|'def'
name|'test_get_by_id_with_host_field_not_in_db'
op|'('
name|'self'
op|','
name|'mock_cn_get'
op|','
nl|'\n'
name|'mock_obj_svc_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_compute_node_with_no_host'
op|'='
name|'fake_compute_node'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
name|'fake_compute_node_with_no_host'
op|'.'
name|'pop'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
nl|'\n'
name|'mock_cn_get'
op|'.'
name|'return_value'
op|'='
name|'fake_compute_node_with_no_host'
newline|'\n'
name|'mock_obj_svc_get'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
nl|'\n'
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_service_id
dedent|''
name|'def'
name|'test_get_by_service_id'
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
string|"'compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_nodes_get_by_service_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'456'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'fake_compute_node'
op|']'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_service_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_get_by_host_and_nodename'"
op|')'
newline|'\n'
DECL|member|test_get_by_host_and_nodename
name|'def'
name|'test_get_by_host_and_nodename'
op|'('
name|'self'
op|','
name|'cn_get_by_h_and_n'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_by_h_and_n'
op|'.'
name|'return_value'
op|'='
name|'fake_compute_node'
newline|'\n'
nl|'\n'
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_host_and_nodename'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake'"
op|','
string|"'vm.danplanet.com'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
string|"'nova.objects.Service.get_by_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_compute_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_get_by_host_and_nodename'"
op|')'
newline|'\n'
DECL|member|test_get_by_host_and_nodename_with_old_compute
name|'def'
name|'test_get_by_host_and_nodename_with_old_compute'
op|'('
name|'self'
op|','
name|'cn_get_by_h_and_n'
op|','
nl|'\n'
name|'svc_get_by_ch'
op|','
nl|'\n'
name|'cn_get_by_svc_id'
op|','
nl|'\n'
name|'svc_get_by_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_by_h_and_n'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
nl|'\n'
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'host'
op|'='
string|"'fake'"
newline|'\n'
name|'svc_get_by_ch'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
name|'cn_get_by_svc_id'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_old_compute_node'
op|']'
newline|'\n'
name|'svc_get_by_id'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
nl|'\n'
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_host_and_nodename'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake'"
op|','
string|"'vm.danplanet.com'"
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Result is still converted to new style Compute'
nl|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
string|"'nova.objects.Service.get_by_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_compute_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_get_by_host_and_nodename'"
op|')'
newline|'\n'
DECL|member|test_get_by_host_and_nodename_not_found
name|'def'
name|'test_get_by_host_and_nodename_not_found'
op|'('
name|'self'
op|','
name|'cn_get_by_h_and_n'
op|','
nl|'\n'
name|'svc_get_by_ch'
op|','
nl|'\n'
name|'cn_get_by_svc_id'
op|','
nl|'\n'
name|'svc_get_by_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_by_h_and_n'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
nl|'\n'
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'host'
op|'='
string|"'fake'"
newline|'\n'
name|'another_node'
op|'='
name|'fake_old_compute_node'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'another_node'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"'elsewhere'"
newline|'\n'
name|'svc_get_by_ch'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
name|'cn_get_by_svc_id'
op|'.'
name|'return_value'
op|'='
op|'['
name|'another_node'
op|']'
newline|'\n'
name|'svc_get_by_id'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|','
nl|'\n'
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_host_and_nodename'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake'"
op|','
string|"'vm.danplanet.com'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_compute_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_get_by_host_and_nodename'"
op|')'
newline|'\n'
DECL|member|test_get_by_host_and_nodename_good_and_bad
name|'def'
name|'test_get_by_host_and_nodename_good_and_bad'
op|'('
name|'self'
op|','
name|'cn_get_by_h_and_n'
op|','
nl|'\n'
name|'svc_get_by_ch'
op|','
nl|'\n'
name|'cn_get_by_svc_id'
op|','
nl|'\n'
name|'svc_get_by_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_by_h_and_n'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
nl|'\n'
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'host'
op|'='
string|"'fake'"
newline|'\n'
name|'bad_node'
op|'='
name|'fake_old_compute_node'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'bad_node'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"'elsewhere'"
newline|'\n'
name|'good_node'
op|'='
name|'fake_old_compute_node'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'svc_get_by_ch'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
name|'cn_get_by_svc_id'
op|'.'
name|'return_value'
op|'='
op|'['
name|'bad_node'
op|','
name|'good_node'
op|']'
newline|'\n'
name|'svc_get_by_id'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
nl|'\n'
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_host_and_nodename'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake'"
op|','
string|"'vm.danplanet.com'"
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Result is still converted to new style Compute'
nl|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'good_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
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
string|"'compute_node_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_create'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'service_id'"
op|':'
number|'456'
op|','
nl|'\n'
string|"'stats'"
op|':'
name|'fake_stats_db_format'
op|','
nl|'\n'
string|"'host_ip'"
op|':'
name|'fake_host_ip'
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
name|'fake_supported_hv_specs_db_format'
op|','
nl|'\n'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_compute_node'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'service_id'
op|'='
number|'456'
newline|'\n'
name|'compute'
op|'.'
name|'stats'
op|'='
name|'fake_stats'
newline|'\n'
comment|'# NOTE (pmurray): host_ip is coerced to an IPAddress'
nl|'\n'
name|'compute'
op|'.'
name|'host_ip'
op|'='
name|'fake_host_ip'
newline|'\n'
name|'compute'
op|'.'
name|'supported_hv_specs'
op|'='
name|'fake_supported_hv_specs'
newline|'\n'
name|'compute'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_recreate_fails
dedent|''
name|'def'
name|'test_recreate_fails'
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
string|"'compute_node_create'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'service_id'"
op|':'
number|'456'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_compute_node'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'service_id'
op|'='
number|'456'
newline|'\n'
name|'compute'
op|'.'
name|'create'
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
name|'compute'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|')'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_update'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'stats'"
op|':'
name|'fake_stats_db_format'
op|','
nl|'\n'
string|"'host_ip'"
op|':'
name|'fake_host_ip'
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
name|'fake_supported_hv_specs_db_format'
op|','
nl|'\n'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_compute_node'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'compute'
op|'.'
name|'vcpus_used'
op|'='
number|'3'
newline|'\n'
name|'compute'
op|'.'
name|'stats'
op|'='
name|'fake_stats'
newline|'\n'
comment|'# NOTE (pmurray): host_ip is coerced to an IPAddress'
nl|'\n'
name|'compute'
op|'.'
name|'host_ip'
op|'='
name|'fake_host_ip'
newline|'\n'
name|'compute'
op|'.'
name|'supported_hv_specs'
op|'='
name|'fake_supported_hv_specs'
newline|'\n'
name|'compute'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'compute'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'compute_node_create'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fake_compute_node'
op|')'
newline|'\n'
DECL|member|test_set_id_failure
name|'def'
name|'test_set_id_failure'
op|'('
name|'self'
op|','
name|'db_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ReadOnlyFieldError'
op|','
name|'setattr'
op|','
nl|'\n'
name|'compute'
op|','
string|"'id'"
op|','
number|'124'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
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
string|"'compute_node_delete'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'compute'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service
dedent|''
name|'def'
name|'test_service'
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
name|'service'
op|'.'
name|'Service'
op|','
string|"'get_by_id'"
op|')'
newline|'\n'
name|'service'
op|'.'
name|'Service'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'456'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'my-service'"
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
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'_context'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'compute'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'compute'
op|'.'
name|'service_id'
op|'='
number|'456'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'my-service'"
op|','
name|'compute'
op|'.'
name|'service'
op|')'
newline|'\n'
comment|"# Make sure it doesn't call Service.get_by_id() again"
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'my-service'"
op|','
name|'compute'
op|'.'
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all
dedent|''
name|'def'
name|'test_get_all'
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
string|"'compute_node_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
name|'fake_compute_node'
op|']'
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
name|'computes'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'computes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'computes'
op|'['
number|'0'
op|']'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_hypervisor
dedent|''
name|'def'
name|'test_get_by_hypervisor'
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
string|"'compute_node_search_by_hypervisor'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'compute_node_search_by_hypervisor'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'hyper'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
name|'fake_compute_node'
op|']'
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
name|'computes'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_by_hypervisor'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'hyper'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'computes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'computes'
op|'['
number|'0'
op|']'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
string|"'nova.db.compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_service
name|'def'
name|'test_get_by_service'
op|'('
name|'self'
op|','
name|'cn_get_by_svc_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_by_svc_id'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_compute_node'
op|']'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'computes'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_by_service'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'fake_service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'computes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'computes'
op|'['
number|'0'
op|']'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
string|"'nova.db.compute_node_get_all_by_host'"
op|')'
newline|'\n'
DECL|member|test_get_all_by_host
name|'def'
name|'test_get_all_by_host'
op|'('
name|'self'
op|','
name|'cn_get_all_by_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_all_by_host'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_compute_node'
op|']'
newline|'\n'
name|'computes'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_all_by_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'computes'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'computes'
op|'['
number|'0'
op|']'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
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
string|"'nova.objects.Service.get_by_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.compute_nodes_get_by_service_id'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Service.get_by_compute_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.compute_node_get_all_by_host'"
op|')'
newline|'\n'
DECL|member|test_get_all_by_host_with_old_compute
name|'def'
name|'test_get_all_by_host_with_old_compute'
op|'('
name|'self'
op|','
name|'cn_get_all_by_host'
op|','
nl|'\n'
name|'svc_get_by_ch'
op|','
nl|'\n'
name|'cn_get_by_svc_id'
op|','
nl|'\n'
name|'svc_get_by_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cn_get_all_by_host'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
nl|'\n'
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'fake_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'fake_service'
op|'.'
name|'host'
op|'='
string|"'fake'"
newline|'\n'
name|'svc_get_by_ch'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
name|'cn_get_by_svc_id'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_old_compute_node'
op|']'
newline|'\n'
name|'svc_get_by_id'
op|'.'
name|'return_value'
op|'='
name|'fake_service'
newline|'\n'
nl|'\n'
name|'computes'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNodeList'
op|'.'
name|'get_all_by_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'computes'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Result is still converted to new style Compute'
nl|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'computes'
op|'['
number|'0'
op|']'
op|','
name|'fake_compute_node'
op|','
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'subs'
op|'('
op|')'
op|','
nl|'\n'
name|'comparators'
op|'='
name|'self'
op|'.'
name|'comparators'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compat_numa_topology
dedent|''
name|'def'
name|'test_compat_numa_topology'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
op|')'
newline|'\n'
name|'primitive'
op|'='
name|'compute'
op|'.'
name|'obj_to_primitive'
op|'('
name|'target_version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'numa_topology'"
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compat_supported_hv_specs
dedent|''
name|'def'
name|'test_compat_supported_hv_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'supported_hv_specs'
op|'='
name|'fake_supported_hv_specs'
newline|'\n'
name|'primitive'
op|'='
name|'compute'
op|'.'
name|'obj_to_primitive'
op|'('
name|'target_version'
op|'='
string|"'1.5'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'supported_hv_specs'"
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compat_host
dedent|''
name|'def'
name|'test_compat_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
op|')'
newline|'\n'
name|'primitive'
op|'='
name|'compute'
op|'.'
name|'obj_to_primitive'
op|'('
name|'target_version'
op|'='
string|"'1.6'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'host'"
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_compat_pci_device_pools
dedent|''
name|'def'
name|'test_compat_pci_device_pools'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute'
op|'='
name|'compute_node'
op|'.'
name|'ComputeNode'
op|'('
op|')'
newline|'\n'
name|'compute'
op|'.'
name|'pci_device_pools'
op|'='
name|'fake_pci_device_pools'
op|'.'
name|'fake_pool_list'
newline|'\n'
name|'primitive'
op|'='
name|'compute'
op|'.'
name|'obj_to_primitive'
op|'('
name|'target_version'
op|'='
string|"'1.8'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'pci_device_pools'"
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestComputeNodeObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestComputeNodeObject
name|'_TestComputeNodeObject'
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
name|'TestRemoteComputeNodeObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteComputeNodeObject
name|'_TestComputeNodeObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
