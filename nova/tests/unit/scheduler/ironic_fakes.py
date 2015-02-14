begin_unit
comment|'# Copyright 2014 OpenStack Foundation'
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
string|'"""\nFake nodes for Ironic host manager tests.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
nl|'\n'
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
number|'10'
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
name|'vcpus_used'
op|'='
number|'0'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host1'"
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|"'node1uuid'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'1'
op|','
name|'hypervisor_type'
op|'='
string|"'ironic'"
op|','
nl|'\n'
DECL|variable|stats
name|'stats'
op|'='
name|'dict'
op|'('
name|'ironic_driver'
op|'='
nl|'\n'
string|'"nova.virt.ironic.driver.IronicDriver"'
op|','
nl|'\n'
DECL|variable|cpu_arch
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|','
nl|'\n'
DECL|variable|supported_hv_specs
name|'supported_hv_specs'
op|'='
op|'['
name|'objects'
op|'.'
name|'HVSpec'
op|'.'
name|'from_list'
op|'('
nl|'\n'
op|'['
string|'"i386"'
op|','
string|'"baremetal"'
op|','
string|'"baremetal"'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'10'
op|','
name|'free_ram_mb'
op|'='
number|'1024'
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
number|'20'
op|','
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host2'"
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|"'node2uuid'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'1'
op|','
name|'hypervisor_type'
op|'='
string|"'ironic'"
op|','
nl|'\n'
DECL|variable|stats
name|'stats'
op|'='
name|'dict'
op|'('
name|'ironic_driver'
op|'='
nl|'\n'
string|'"nova.virt.ironic.driver.IronicDriver"'
op|','
nl|'\n'
DECL|variable|cpu_arch
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|','
nl|'\n'
DECL|variable|supported_hv_specs
name|'supported_hv_specs'
op|'='
op|'['
name|'objects'
op|'.'
name|'HVSpec'
op|'.'
name|'from_list'
op|'('
nl|'\n'
op|'['
string|'"i386"'
op|','
string|'"baremetal"'
op|','
string|'"baremetal"'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'20'
op|','
name|'free_ram_mb'
op|'='
number|'2048'
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
number|'30'
op|','
name|'memory_mb'
op|'='
number|'3072'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host3'"
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|"'node3uuid'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'1'
op|','
name|'hypervisor_type'
op|'='
string|"'ironic'"
op|','
nl|'\n'
DECL|variable|stats
name|'stats'
op|'='
name|'dict'
op|'('
name|'ironic_driver'
op|'='
nl|'\n'
string|'"nova.virt.ironic.driver.IronicDriver"'
op|','
nl|'\n'
DECL|variable|cpu_arch
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|','
nl|'\n'
DECL|variable|supported_hv_specs
name|'supported_hv_specs'
op|'='
op|'['
name|'objects'
op|'.'
name|'HVSpec'
op|'.'
name|'from_list'
op|'('
nl|'\n'
op|'['
string|'"i386"'
op|','
string|'"baremetal"'
op|','
string|'"baremetal"'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'30'
op|','
name|'free_ram_mb'
op|'='
number|'3072'
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
number|'40'
op|','
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
nl|'\n'
name|'vcpus_used'
op|'='
number|'0'
op|','
name|'local_gb_used'
op|'='
number|'0'
op|','
name|'memory_mb_used'
op|'='
number|'0'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'None'
op|','
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'host4'"
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|"'node4uuid'"
op|','
name|'host_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'1'
op|','
name|'hypervisor_type'
op|'='
string|"'ironic'"
op|','
nl|'\n'
DECL|variable|stats
name|'stats'
op|'='
name|'dict'
op|'('
name|'ironic_driver'
op|'='
nl|'\n'
string|'"nova.virt.ironic.driver.IronicDriver"'
op|','
nl|'\n'
DECL|variable|cpu_arch
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|','
nl|'\n'
DECL|variable|supported_hv_specs
name|'supported_hv_specs'
op|'='
op|'['
name|'objects'
op|'.'
name|'HVSpec'
op|'.'
name|'from_list'
op|'('
nl|'\n'
op|'['
string|'"i386"'
op|','
string|'"baremetal"'
op|','
string|'"baremetal"'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'40'
op|','
name|'free_ram_mb'
op|'='
number|'4096'
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
number|'50'
op|','
name|'memory_mb'
op|'='
number|'5120'
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
name|'cpu_info'
op|'='
string|"'baremetal cpu'"
op|','
nl|'\n'
DECL|variable|stats
name|'stats'
op|'='
name|'dict'
op|'('
name|'ironic_driver'
op|'='
nl|'\n'
string|'"nova.virt.ironic.driver.IronicDriver"'
op|','
nl|'\n'
DECL|variable|cpu_arch
name|'cpu_arch'
op|'='
string|"'i386'"
op|')'
op|','
nl|'\n'
DECL|variable|supported_hv_specs
name|'supported_hv_specs'
op|'='
op|'['
name|'objects'
op|'.'
name|'HVSpec'
op|'.'
name|'from_list'
op|'('
nl|'\n'
op|'['
string|'"i386"'
op|','
string|'"baremetal"'
op|','
string|'"baremetal"'
op|']'
op|')'
op|']'
op|','
nl|'\n'
name|'free_disk_gb'
op|'='
number|'50'
op|','
name|'free_ram_mb'
op|'='
number|'5120'
op|','
nl|'\n'
DECL|variable|hypervisor_hostname
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
dedent|''
endmarker|''
end_unit
