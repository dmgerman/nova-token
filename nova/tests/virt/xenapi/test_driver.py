begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 Rackspace Hosting'
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
nl|'\n'
name|'import'
name|'math'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'unit'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'xenapi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIDriverTestCase
name|'class'
name|'XenAPIDriverTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for Driver operations."""'
newline|'\n'
nl|'\n'
DECL|member|host_stats
name|'def'
name|'host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'host_memory_total'"
op|':'
number|'3'
op|'*'
name|'unit'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'host_memory_free_computed'"
op|':'
number|'2'
op|'*'
name|'unit'
op|'.'
name|'Mi'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'4'
op|'*'
name|'unit'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'disk_used'"
op|':'
number|'5'
op|'*'
name|'unit'
op|'.'
name|'Gi'
op|','
nl|'\n'
string|"'host_hostname'"
op|':'
string|"'somename'"
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
string|"'x86_64'"
op|','
nl|'\n'
string|"'host_cpu_info'"
op|':'
op|'{'
string|"'cpu_count'"
op|':'
number|'50'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_available_resource
dedent|''
name|'def'
name|'test_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVMTests'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'='
name|'xenapi'
op|'.'
name|'XenAPIDriver'
op|'('
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|','
name|'False'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'_session'
op|'.'
name|'product_version'
op|'='
op|'('
number|'6'
op|','
number|'8'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|','
string|"'get_host_stats'"
op|','
name|'self'
op|'.'
name|'host_stats'
op|')'
newline|'\n'
nl|'\n'
name|'resources'
op|'='
name|'driver'
op|'.'
name|'get_available_resource'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'6008002'
op|','
name|'resources'
op|'['
string|"'hypervisor_version'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'resources'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'resources'
op|'['
string|"'memory_mb'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'resources'
op|'['
string|"'local_gb'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'resources'
op|'['
string|"'vcpus_used'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|'-'
number|'2'
op|','
name|'resources'
op|'['
string|"'memory_mb_used'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'5'
op|','
name|'resources'
op|'['
string|"'local_gb_used'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'xen'"
op|','
name|'resources'
op|'['
string|"'hypervisor_type'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'somename'"
op|','
name|'resources'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'50'
op|','
name|'resources'
op|'['
string|"'cpu_info'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_overhead
dedent|''
name|'def'
name|'test_overhead'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'stubs'
op|'.'
name|'FakeSessionForVMTests'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi'
op|'.'
name|'XenAPIDriver'
op|'('
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|','
name|'False'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
number|'30720'
op|'}'
newline|'\n'
nl|'\n'
comment|'# expected memory overhead per:'
nl|'\n'
comment|'# https://wiki.openstack.org/wiki/XenServer/Overhead'
nl|'\n'
name|'expected'
op|'='
name|'math'
op|'.'
name|'ceil'
op|'('
number|'251.832'
op|')'
newline|'\n'
name|'overhead'
op|'='
name|'driver'
op|'.'
name|'estimate_instance_overhead'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'overhead'
op|'['
string|"'memory_mb'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
