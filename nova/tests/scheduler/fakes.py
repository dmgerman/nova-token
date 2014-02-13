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
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
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
op|'.'
name|'scheduler'
name|'import'
name|'filter_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|COMPUTE_NODES
name|'COMPUTE_NODES'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node2'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node3'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node4'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
comment|'# Broken entry'
nl|'\n'
name|'dict'
op|'('
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
name|'service'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|COMPUTE_NODES_METRICS
name|'COMPUTE_NODES_METRICS'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
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
number|'512'
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|metrics
name|'metrics'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host1'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host1'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|')'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node2'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|metrics
name|'metrics'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'1024'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host2'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'2.0'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host2'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|')'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
number|'3072'
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node3'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|metrics
name|'metrics'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'3072'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host3'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host3'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|')'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
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
number|'8192'
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
DECL|variable|service
name|'service'
op|'='
name|'dict'
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
name|'hypervisor_hostname'
op|'='
string|"'node4'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|hypervisor_version
name|'hypervisor_version'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|metrics
name|'metrics'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'['
op|'{'
string|"'name'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'8192'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host4'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'value'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source'"
op|':'
string|"'host4'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|INSTANCES
name|'INSTANCES'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host1'"
op|','
name|'node'
op|'='
string|"'node1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|','
name|'node'
op|'='
string|"'node2'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
op|','
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host2'"
op|','
name|'node'
op|'='
string|"'node2'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'1024'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
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
string|"'host3'"
op|','
name|'node'
op|'='
string|"'node3'"
op|')'
op|','
nl|'\n'
comment|'# Broken host'
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'1024'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
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
DECL|variable|host
name|'host'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
comment|'# No matching host'
nl|'\n'
name|'dict'
op|'('
name|'root_gb'
op|'='
number|'1024'
op|','
name|'ephemeral_gb'
op|'='
number|'0'
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
string|"'host5'"
op|','
name|'node'
op|'='
string|"'node5'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeFilterScheduler
name|'class'
name|'FakeFilterScheduler'
op|'('
name|'filter_scheduler'
op|'.'
name|'FilterScheduler'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeFilterScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'='
name|'host_manager'
op|'.'
name|'HostManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHostManager
dedent|''
dedent|''
name|'class'
name|'FakeHostManager'
op|'('
name|'host_manager'
op|'.'
name|'HostManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""host1: free_ram_mb=1024-512-512=0, free_disk_gb=1024-512-512=0\n       host2: free_ram_mb=2048-512=1536  free_disk_gb=2048-512=1536\n       host3: free_ram_mb=4096-1024=3072  free_disk_gb=4096-1024=3072\n       host4: free_ram_mb=8192  free_disk_gb=8192\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeHostManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
nl|'\n'
string|"'host1'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'1073741824'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'2147483648'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host3'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'3221225472'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host4'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'999999999'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHostState
dedent|''
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
nl|'\n'
nl|'\n'
DECL|class|FakeInstance
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeInstance'
op|'('
name|'object'
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
name|'context'
op|'='
name|'None'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance. Returns uuid."""'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
newline|'\n'
nl|'\n'
name|'i'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
name|'params'
op|'='
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'i'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_instance
dedent|''
name|'def'
name|'_create_fake_instance'
op|'('
name|'self'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance."""'
newline|'\n'
name|'if'
name|'not'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'vm_state'"
op|']'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
number|'2'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
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
DECL|class|FakeComputeAPI
dedent|''
dedent|''
name|'class'
name|'FakeComputeAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|create_db_entry_for_new_instance
indent|'    '
name|'def'
name|'create_db_entry_for_new_instance'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mox_host_manager_db_calls
dedent|''
dedent|''
name|'def'
name|'mox_host_manager_db_calls'
op|'('
name|'mock'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mock'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'COMPUTE_NODES'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
