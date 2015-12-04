begin_unit
comment|'# Copyright 2014 Cloudbase Solutions Srl'
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
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'hostops'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostOpsTestCase
name|'class'
name|'HostOpsTestCase'
op|'('
name|'test_base'
op|'.'
name|'HyperVBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V HostOps class."""'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_ARCHITECTURE
name|'FAKE_ARCHITECTURE'
op|'='
number|'0'
newline|'\n'
DECL|variable|FAKE_NAME
name|'FAKE_NAME'
op|'='
string|"'fake_name'"
newline|'\n'
DECL|variable|FAKE_MANUFACTURER
name|'FAKE_MANUFACTURER'
op|'='
string|"'FAKE_MANUFACTURER'"
newline|'\n'
DECL|variable|FAKE_NUM_CPUS
name|'FAKE_NUM_CPUS'
op|'='
number|'1'
newline|'\n'
DECL|variable|FAKE_INSTANCE_DIR
name|'FAKE_INSTANCE_DIR'
op|'='
string|'"C:/fake/dir"'
newline|'\n'
DECL|variable|FAKE_LOCAL_IP
name|'FAKE_LOCAL_IP'
op|'='
string|"'10.11.12.13'"
newline|'\n'
DECL|variable|FAKE_TICK_COUNT
name|'FAKE_TICK_COUNT'
op|'='
number|'1000000'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'HostOpsTestCase'
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
name|'_hostops'
op|'='
name|'hostops'
op|'.'
name|'HostOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_pathutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cpu_info
dedent|''
name|'def'
name|'test_get_cpu_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_processors'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'info'
op|'='
op|'{'
string|"'Architecture'"
op|':'
name|'self'
op|'.'
name|'FAKE_ARCHITECTURE'
op|','
nl|'\n'
string|"'Name'"
op|':'
name|'self'
op|'.'
name|'FAKE_NAME'
op|','
nl|'\n'
string|"'Manufacturer'"
op|':'
name|'self'
op|'.'
name|'FAKE_MANUFACTURER'
op|','
nl|'\n'
string|"'NumberOfCores'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|','
nl|'\n'
string|"'NumberOfLogicalProcessors'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|getitem
name|'def'
name|'getitem'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'info'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'mock_processors'
op|'.'
name|'__getitem__'
op|'.'
name|'side_effect'
op|'='
name|'getitem'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_cpus_info'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock_processors'
op|']'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_get_cpu_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_cpus_info'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'fkey'
op|')'
nl|'\n'
name|'for'
name|'fkey'
name|'in'
name|'constants'
op|'.'
name|'PROCESSOR_FEATURE'
op|'.'
name|'keys'
op|'('
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'is_cpu_feature_present'
op|'.'
name|'has_calls'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'expected_response'
op|'='
name|'self'
op|'.'
name|'_get_mock_cpu_info'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_response'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_mock_cpu_info
dedent|''
name|'def'
name|'_get_mock_cpu_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'vendor'"
op|':'
name|'self'
op|'.'
name|'FAKE_MANUFACTURER'
op|','
nl|'\n'
string|"'model'"
op|':'
name|'self'
op|'.'
name|'FAKE_NAME'
op|','
nl|'\n'
string|"'arch'"
op|':'
name|'constants'
op|'.'
name|'WMI_WIN32_PROCESSOR_ARCHITECTURE'
op|'['
nl|'\n'
name|'self'
op|'.'
name|'FAKE_ARCHITECTURE'
op|']'
op|','
nl|'\n'
string|"'features'"
op|':'
name|'constants'
op|'.'
name|'PROCESSOR_FEATURE'
op|'.'
name|'values'
op|'('
op|')'
op|','
nl|'\n'
string|"'topology'"
op|':'
op|'{'
string|"'cores'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|','
nl|'\n'
string|"'threads'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|','
nl|'\n'
string|"'sockets'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_get_memory_info
dedent|''
name|'def'
name|'test_get_memory_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_memory_info'
op|'.'
name|'return_value'
op|'='
op|'('
number|'2'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|','
nl|'\n'
number|'1'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_get_memory_info'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_memory_info'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
number|'2'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_local_hdd_info_gb
dedent|''
name|'def'
name|'test_get_local_hdd_info_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'.'
name|'return_value'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_volume_info'
op|'.'
name|'return_value'
op|'='
op|'('
number|'2'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
nl|'\n'
number|'1'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_get_local_hdd_info_gb'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instances_dir'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_volume_info'
op|'.'
name|'assert_called_once_with'
op|'('
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
number|'2'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hypervisor_version
dedent|''
name|'def'
name|'test_get_hypervisor_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_windows_version'
op|'.'
name|'return_value'
op|'='
string|"'6.3.9600'"
newline|'\n'
name|'response_lower'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_get_hypervisor_version'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_windows_version'
op|'.'
name|'return_value'
op|'='
string|"'10.1.0'"
newline|'\n'
name|'response_higher'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_get_hypervisor_version'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'6003'
op|','
name|'response_lower'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'10001'
op|','
name|'response_higher'
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
name|'hostops'
op|'.'
name|'HostOps'
op|','
string|"'_get_cpu_info'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'hostops'
op|'.'
name|'HostOps'
op|','
string|"'_get_memory_info'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'hostops'
op|'.'
name|'HostOps'
op|','
string|"'_get_hypervisor_version'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'hostops'
op|'.'
name|'HostOps'
op|','
string|"'_get_local_hdd_info_gb'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'platform.node'"
op|')'
newline|'\n'
DECL|member|test_get_available_resource
name|'def'
name|'test_get_available_resource'
op|'('
name|'self'
op|','
name|'mock_node'
op|','
nl|'\n'
name|'mock_get_local_hdd_info_gb'
op|','
nl|'\n'
name|'mock_get_hypervisor_version'
op|','
nl|'\n'
name|'mock_get_memory_info'
op|','
name|'mock_get_cpu_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_local_hdd_info_gb'
op|'.'
name|'return_value'
op|'='
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'LOCAL_GB'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'LOCAL_GB_FREE'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'LOCAL_GB_USED'
op|')'
newline|'\n'
name|'mock_get_memory_info'
op|'.'
name|'return_value'
op|'='
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'MEMORY_MB'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'MEMORY_MB_FREE'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'MEMORY_MB_USED'
op|')'
newline|'\n'
name|'mock_cpu_info'
op|'='
name|'self'
op|'.'
name|'_get_mock_cpu_info'
op|'('
op|')'
newline|'\n'
name|'mock_get_cpu_info'
op|'.'
name|'return_value'
op|'='
name|'mock_cpu_info'
newline|'\n'
name|'mock_get_hypervisor_version'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'VERSION'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_available_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_get_memory_info'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_get_cpu_info'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'mock_get_hypervisor_version'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'supported_instances'"
op|':'
op|'['
op|'('
string|'"i686"'
op|','
string|'"hyperv"'
op|','
string|'"hvm"'
op|')'
op|','
nl|'\n'
op|'('
string|'"x86_64"'
op|','
string|'"hyperv"'
op|','
string|'"hvm"'
op|')'
op|']'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'mock_node'
op|'('
op|')'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'mock_cpu_info'
op|')'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'VERSION'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'MEMORY_MB'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'MEMORY_MB_USED'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'LOCAL_GB'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'LOCAL_GB_USED'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'self'
op|'.'
name|'FAKE_NUM_CPUS'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|"'hyperv'"
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_host_power_action
dedent|''
name|'def'
name|'_test_host_power_action'
op|'('
name|'self'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'host_power_action'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'host_power_action'
op|'('
name|'action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'host_power_action'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_power_action_shutdown
dedent|''
name|'def'
name|'test_host_power_action_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_power_action'
op|'('
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_SHUTDOWN'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_power_action_reboot
dedent|''
name|'def'
name|'test_host_power_action_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_host_power_action'
op|'('
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_REBOOT'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_power_action_exception
dedent|''
name|'def'
name|'test_host_power_action_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'host_power_action'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_STARTUP'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_ip_addr
dedent|''
name|'def'
name|'test_get_host_ip_addr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'my_ip'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_local_ips'
op|'.'
name|'return_value'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'FAKE_LOCAL_IP'
op|']'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_ip_addr'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_local_ips'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'FAKE_LOCAL_IP'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'time.strftime'"
op|')'
newline|'\n'
DECL|member|test_get_host_uptime
name|'def'
name|'test_get_host_uptime'
op|'('
name|'self'
op|','
name|'mock_time'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'_hostutils'
op|'.'
name|'get_host_tick_count64'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'FAKE_TICK_COUNT'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_uptime'
op|'('
op|')'
newline|'\n'
name|'tdelta'
op|'='
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'milliseconds'
op|'='
name|'long'
op|'('
name|'self'
op|'.'
name|'FAKE_TICK_COUNT'
op|')'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"%s up %s,  0 users,  load average: 0, 0, 0"'
op|'%'
op|'('
nl|'\n'
name|'str'
op|'('
name|'mock_time'
op|'('
op|')'
op|')'
op|','
name|'str'
op|'('
name|'tdelta'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'response'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
