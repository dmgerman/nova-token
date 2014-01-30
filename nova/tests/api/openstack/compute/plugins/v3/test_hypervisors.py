begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'hypervisors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_HYPERS
name|'TEST_HYPERS'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|service_id
name|'service_id'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|service
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|'"compute1"'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|'"nova-compute"'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|'"compute_topic"'
op|','
nl|'\n'
DECL|variable|report_count
name|'report_count'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|availability_zone
name|'availability_zone'
op|'='
string|'"nova"'
op|')'
op|','
nl|'\n'
DECL|variable|vcpus
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
DECL|variable|memory_mb
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|local_gb
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
DECL|variable|vcpus_used
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|memory_mb_used
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|local_gb_used
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
DECL|variable|hypervisor_type
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|hypervisor_hostname
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
DECL|variable|free_ram_mb
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|free_disk_gb
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
DECL|variable|current_workload
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|running_vms
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|cpu_info
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
DECL|variable|disk_available_least
name|'disk_available_least'
op|'='
number|'100'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|service_id
name|'service_id'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|service
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|'"compute2"'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|'"nova-compute"'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|'"compute_topic"'
op|','
nl|'\n'
DECL|variable|report_count
name|'report_count'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|availability_zone
name|'availability_zone'
op|'='
string|'"nova"'
op|')'
op|','
nl|'\n'
DECL|variable|vcpus
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
DECL|variable|memory_mb
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|local_gb
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
DECL|variable|vcpus_used
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|memory_mb_used
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|local_gb_used
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
DECL|variable|hypervisor_type
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|hypervisor_hostname
name|'hypervisor_hostname'
op|'='
string|'"hyper2"'
op|','
nl|'\n'
DECL|variable|free_ram_mb
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
DECL|variable|free_disk_gb
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
DECL|variable|current_workload
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|running_vms
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|cpu_info
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
DECL|variable|disk_available_least
name|'disk_available_least'
op|'='
number|'100'
op|')'
op|']'
newline|'\n'
DECL|variable|TEST_SERVERS
name|'TEST_SERVERS'
op|'='
op|'['
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst1"'
op|','
name|'uuid'
op|'='
string|'"uuid1"'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst2"'
op|','
name|'uuid'
op|'='
string|'"uuid2"'
op|','
name|'host'
op|'='
string|'"compute2"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst3"'
op|','
name|'uuid'
op|'='
string|'"uuid3"'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst4"'
op|','
name|'uuid'
op|'='
string|'"uuid4"'
op|','
name|'host'
op|'='
string|'"compute2"'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'db_api'
op|'.'
name|'require_admin_context'
newline|'\n'
DECL|function|fake_compute_node_get_all
name|'def'
name|'fake_compute_node_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'TEST_HYPERS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_node_search_by_hypervisor
dedent|''
name|'def'
name|'fake_compute_node_search_by_hypervisor'
op|'('
name|'context'
op|','
name|'hypervisor_re'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'TEST_HYPERS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_node_get
dedent|''
name|'def'
name|'fake_compute_node_get'
op|'('
name|'context'
op|','
name|'compute_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'hyper'
name|'in'
name|'TEST_HYPERS'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hyper'
op|'['
string|"'id'"
op|']'
op|'=='
name|'compute_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'hyper'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
name|'host'
op|'='
name|'compute_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_node_statistics
dedent|''
name|'def'
name|'fake_compute_node_statistics'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'count'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'0'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'0'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'0'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'0'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'0'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'0'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'hyper'
name|'in'
name|'TEST_HYPERS'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'count'"
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'key'
op|']'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'key'
op|']'
op|'+='
name|'hyper'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get_all_by_host
dedent|''
name|'def'
name|'fake_instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'results'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'inst'
name|'in'
name|'TEST_SERVERS'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'inst'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'results'
op|'.'
name|'append'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'results'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorsTest
dedent|''
name|'class'
name|'HypervisorsTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'HypervisorsTest'
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
name|'controller'
op|'='
name|'hypervisors'
op|'.'
name|'HypervisorsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|','
name|'fake_compute_node_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_search_by_hypervisor'"
op|','
nl|'\n'
name|'fake_compute_node_search_by_hypervisor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_get'"
op|','
nl|'\n'
name|'fake_compute_node_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_statistics'"
op|','
nl|'\n'
name|'fake_compute_node_statistics'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_host'"
op|','
nl|'\n'
name|'fake_instance_get_all_by_host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_view_hypervisor_nodetail_noservers
dedent|''
name|'def'
name|'test_view_hypervisor_nodetail_noservers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
name|'TEST_HYPERS'
op|'['
number|'0'
op|']'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_view_hypervisor_detail_noservers
dedent|''
name|'def'
name|'test_view_hypervisor_detail_noservers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
name|'TEST_HYPERS'
op|'['
number|'0'
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'100'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'compute1'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_view_hypervisor_servers
dedent|''
name|'def'
name|'test_view_hypervisor_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
name|'TEST_HYPERS'
op|'['
number|'0'
op|']'
op|','
name|'False'
op|','
nl|'\n'
name|'TEST_SERVERS'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'servers'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst1"'
op|','
name|'id'
op|'='
string|'"uuid1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst2"'
op|','
name|'id'
op|'='
string|'"uuid2"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst3"'
op|','
name|'id'
op|'='
string|'"uuid3"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst4"'
op|','
name|'id'
op|'='
string|'"uuid4"'
op|')'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'hypervisor_hostname'
op|'='
string|'"hyper2"'
op|')'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_non_admin
dedent|''
name|'def'
name|'test_index_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/detail'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'100'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'host'
op|'='
string|'"compute2"'
op|')'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper2"'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'100'
op|')'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_non_admin
dedent|''
name|'def'
name|'test_detail_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/detail'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_noid
dedent|''
name|'def'
name|'test_show_noid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/3'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_non_integer_id
dedent|''
name|'def'
name|'test_show_non_integer_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/abc'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'abc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_withid
dedent|''
name|'def'
name|'test_show_withid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'250'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'125'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'5'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'125'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'2'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'2'
op|','
nl|'\n'
name|'cpu_info'
op|'='
string|"'cpu_info'"
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'100'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_non_admin
dedent|''
name|'def'
name|'test_show_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uptime_noid
dedent|''
name|'def'
name|'test_uptime_noid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/3'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uptime_notimplemented
dedent|''
name|'def'
name|'test_uptime_notimplemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_host_uptime
indent|'        '
name|'def'
name|'fake_get_host_uptime'
op|'('
name|'context'
op|','
name|'hyp'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
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
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|"'get_host_uptime'"
op|','
nl|'\n'
name|'fake_get_host_uptime'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'uptime'
op|','
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uptime_implemented
dedent|''
name|'def'
name|'test_uptime_implemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_host_uptime
indent|'        '
name|'def'
name|'fake_get_host_uptime'
op|'('
name|'context'
op|','
name|'hyp'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"fake uptime"'
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
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|"'get_host_uptime'"
op|','
nl|'\n'
name|'fake_get_host_uptime'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'uptime'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'uptime'
op|'='
string|'"fake uptime"'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uptime_non_integer_id
dedent|''
name|'def'
name|'test_uptime_non_integer_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/abc/uptime'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'uptime'
op|','
name|'req'
op|','
string|"'abc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uptime_non_admin
dedent|''
name|'def'
name|'test_uptime_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1/uptime'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'uptime'
op|','
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_search
dedent|''
name|'def'
name|'test_search'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/search?query=hyper'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'search'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'hypervisor_hostname'
op|'='
string|'"hyper2"'
op|')'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_search_non_exist
dedent|''
name|'def'
name|'test_search_non_exist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_compute_node_search_by_hypervisor_return_empty
indent|'        '
name|'def'
name|'fake_compute_node_search_by_hypervisor_return_empty'
op|'('
name|'context'
op|','
nl|'\n'
name|'hypervisor_re'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_search_by_hypervisor'"
op|','
nl|'\n'
name|'fake_compute_node_search_by_hypervisor_return_empty'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/search?query=a'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'search'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_search_without_query
dedent|''
name|'def'
name|'test_search_without_query'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/search'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'search'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers
dedent|''
name|'def'
name|'test_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1/servers'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servers'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor'
op|'='
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'servers'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst1"'
op|','
name|'id'
op|'='
string|'"uuid1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|'"inst3"'
op|','
name|'id'
op|'='
string|'"uuid3"'
op|')'
op|']'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_non_id
dedent|''
name|'def'
name|'test_servers_non_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/3/servers'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servers'
op|','
name|'req'
op|','
string|"'3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_non_admin
dedent|''
name|'def'
name|'test_servers_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1/servers'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servers'
op|','
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_return_empty
dedent|''
name|'def'
name|'test_servers_return_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_instance_get_all_by_host_return_empty
indent|'        '
name|'def'
name|'fake_instance_get_all_by_host_return_empty'
op|'('
name|'context'
op|','
name|'hypervisor_re'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_all_by_host'"
op|','
nl|'\n'
name|'fake_instance_get_all_by_host_return_empty'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1/servers'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servers'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor'
op|'='
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|','
nl|'\n'
name|'servers'
op|'='
op|'['
op|']'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_with_non_integer_hypervisor_id
dedent|''
name|'def'
name|'test_servers_with_non_integer_hypervisor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/abc/servers'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servers'
op|','
name|'req'
op|','
string|"'abc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_statistics
dedent|''
name|'def'
name|'test_statistics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/statistics'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'statistics'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor_statistics'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'count'
op|'='
number|'2'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'8'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'20'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'500'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb_used'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'local_gb_used'
op|'='
number|'250'
op|','
nl|'\n'
name|'free_ram_mb'
op|'='
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'250'
op|','
nl|'\n'
name|'current_workload'
op|'='
number|'4'
op|','
nl|'\n'
name|'running_vms'
op|'='
number|'4'
op|','
nl|'\n'
name|'disk_available_least'
op|'='
number|'200'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_statistics_non_admin
dedent|''
name|'def'
name|'test_statistics_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/statistics'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'statistics'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorsSerializersTest
dedent|''
dedent|''
name|'class'
name|'HypervisorsSerializersTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|compare_to_exemplar
indent|'    '
name|'def'
name|'compare_to_exemplar'
op|'('
name|'self'
op|','
name|'exemplar'
op|','
name|'hyper'
op|')'
op|':'
newline|'\n'
comment|'# Check attributes'
nl|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
op|'('
string|"'service'"
op|','
string|"'servers'"
op|')'
op|':'
newline|'\n'
comment|'# These turn into child elements and get tested'
nl|'\n'
comment|'# separately below...'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|','
name|'hyper'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check child elements'
nl|'\n'
dedent|''
name|'required_children'
op|'='
name|'set'
op|'('
op|'['
name|'child'
name|'for'
name|'child'
name|'in'
op|'('
string|"'service'"
op|','
string|"'servers'"
op|')'
nl|'\n'
name|'if'
name|'child'
name|'in'
name|'exemplar'
op|']'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'hyper'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'child'
op|'.'
name|'tag'
op|','
name|'required_children'
op|')'
newline|'\n'
name|'required_children'
op|'.'
name|'remove'
op|'('
name|'child'
op|'.'
name|'tag'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check the node...'
nl|'\n'
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'service'"
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'['
string|"'service'"
op|']'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|','
name|'child'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'servers'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'child'
op|')'
op|','
name|'len'
op|'('
name|'exemplar'
op|'['
string|"'servers'"
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'grandchild'
name|'in'
name|'enumerate'
op|'('
name|'child'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'server'"
op|','
name|'grandchild'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'['
string|"'servers'"
op|']'
op|'['
name|'idx'
op|']'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'value'
op|')'
op|','
name|'grandchild'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Are they all accounted for?'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'required_children'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
