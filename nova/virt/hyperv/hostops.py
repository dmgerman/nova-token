begin_unit
comment|'# Copyright 2012 Cloudbase Solutions Srl'
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
string|'"""\nManagement class for host operations.\n"""'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'platform'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'os_win'
name|'import'
name|'constants'
name|'as'
name|'os_win_const'
newline|'\n'
name|'from'
name|'os_win'
name|'import'
name|'utilsfactory'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'compute'
name|'import'
name|'arch'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'hv_type'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_mode'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
name|'pathutils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostOps
name|'class'
name|'HostOps'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_hostutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_hostutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'pathutils'
op|'.'
name|'PathUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_cpu_info
dedent|''
name|'def'
name|'_get_cpu_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the CPU information.\n        :returns: A dictionary containing the main properties\n        of the central processor in the hypervisor.\n        """'
newline|'\n'
name|'cpu_info'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'processors'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_cpus_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'w32_arch_dict'
op|'='
name|'constants'
op|'.'
name|'WMI_WIN32_PROCESSOR_ARCHITECTURE'
newline|'\n'
name|'cpu_info'
op|'['
string|"'arch'"
op|']'
op|'='
name|'w32_arch_dict'
op|'.'
name|'get'
op|'('
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'Architecture'"
op|']'
op|','
nl|'\n'
string|"'Unknown'"
op|')'
newline|'\n'
name|'cpu_info'
op|'['
string|"'model'"
op|']'
op|'='
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'Name'"
op|']'
newline|'\n'
name|'cpu_info'
op|'['
string|"'vendor'"
op|']'
op|'='
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'Manufacturer'"
op|']'
newline|'\n'
nl|'\n'
name|'topology'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'topology'
op|'['
string|"'sockets'"
op|']'
op|'='
name|'len'
op|'('
name|'processors'
op|')'
newline|'\n'
name|'topology'
op|'['
string|"'cores'"
op|']'
op|'='
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'NumberOfCores'"
op|']'
newline|'\n'
name|'topology'
op|'['
string|"'threads'"
op|']'
op|'='
op|'('
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'NumberOfLogicalProcessors'"
op|']'
op|'//'
nl|'\n'
name|'processors'
op|'['
number|'0'
op|']'
op|'['
string|"'NumberOfCores'"
op|']'
op|')'
newline|'\n'
name|'cpu_info'
op|'['
string|"'topology'"
op|']'
op|'='
name|'topology'
newline|'\n'
nl|'\n'
name|'features'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
name|'for'
name|'fkey'
op|','
name|'fname'
name|'in'
name|'os_win_const'
op|'.'
name|'PROCESSOR_FEATURE'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'is_cpu_feature_present'
op|'('
name|'fkey'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'features'
op|'.'
name|'append'
op|'('
name|'fname'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'cpu_info'
op|'['
string|"'features'"
op|']'
op|'='
name|'features'
newline|'\n'
nl|'\n'
name|'return'
name|'cpu_info'
newline|'\n'
nl|'\n'
DECL|member|_get_memory_info
dedent|''
name|'def'
name|'_get_memory_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'total_mem_kb'
op|','
name|'free_mem_kb'
op|')'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_memory_info'
op|'('
op|')'
newline|'\n'
name|'total_mem_mb'
op|'='
name|'total_mem_kb'
op|'//'
number|'1024'
newline|'\n'
name|'free_mem_mb'
op|'='
name|'free_mem_kb'
op|'//'
number|'1024'
newline|'\n'
name|'return'
op|'('
name|'total_mem_mb'
op|','
name|'free_mem_mb'
op|','
name|'total_mem_mb'
op|'-'
name|'free_mem_mb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_local_hdd_info_gb
dedent|''
name|'def'
name|'_get_local_hdd_info_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'drive'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'splitdrive'
op|'('
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instances_dir'
op|'('
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
op|'('
name|'size'
op|','
name|'free_space'
op|')'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_volume_info'
op|'('
name|'drive'
op|')'
newline|'\n'
nl|'\n'
name|'total_gb'
op|'='
name|'size'
op|'//'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'free_gb'
op|'='
name|'free_space'
op|'//'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'used_gb'
op|'='
name|'total_gb'
op|'-'
name|'free_gb'
newline|'\n'
name|'return'
op|'('
name|'total_gb'
op|','
name|'free_gb'
op|','
name|'used_gb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_hypervisor_version
dedent|''
name|'def'
name|'_get_hypervisor_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get hypervisor version.\n        :returns: hypervisor version (ex. 6003)\n        """'
newline|'\n'
nl|'\n'
comment|'# NOTE(claudiub): The hypervisor_version will be stored in the database'
nl|'\n'
comment|'# as an Integer and it will be used by the scheduler, if required by'
nl|'\n'
comment|"# the image property 'hypervisor_version_requires'."
nl|'\n'
comment|'# The hypervisor_version will then be converted back to a version'
nl|'\n'
comment|'# by splitting the int in groups of 3 digits.'
nl|'\n'
comment|"# E.g.: hypervisor_version 6003 is converted to '6.3'."
nl|'\n'
name|'version'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_windows_version'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'version'
op|'='
name|'int'
op|'('
name|'version'
op|'['
number|'0'
op|']'
op|')'
op|'*'
number|'1000'
op|'+'
name|'int'
op|'('
name|'version'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Windows version: %s '"
op|','
name|'version'
op|')'
newline|'\n'
name|'return'
name|'version'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve resource info.\n\n        This method is called when nova-compute launches, and\n        as part of a periodic task.\n\n        :returns: dictionary describing resources\n\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'get_available_resource called'"
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'total_mem_mb'
op|','
nl|'\n'
name|'free_mem_mb'
op|','
nl|'\n'
name|'used_mem_mb'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_memory_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'total_hdd_gb'
op|','
nl|'\n'
name|'free_hdd_gb'
op|','
nl|'\n'
name|'used_hdd_gb'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_local_hdd_info_gb'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'cpu_info'
op|'='
name|'self'
op|'.'
name|'_get_cpu_info'
op|'('
op|')'
newline|'\n'
name|'cpu_topology'
op|'='
name|'cpu_info'
op|'['
string|"'topology'"
op|']'
newline|'\n'
name|'vcpus'
op|'='
op|'('
name|'cpu_topology'
op|'['
string|"'sockets'"
op|']'
op|'*'
nl|'\n'
name|'cpu_topology'
op|'['
string|"'cores'"
op|']'
op|'*'
nl|'\n'
name|'cpu_topology'
op|'['
string|"'threads'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'dic'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'total_mem_mb'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'used_mem_mb'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'total_hdd_gb'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'used_hdd_gb'
op|','
nl|'\n'
string|"'hypervisor_type'"
op|':'
string|'"hyperv"'
op|','
nl|'\n'
string|"'hypervisor_version'"
op|':'
name|'self'
op|'.'
name|'_get_hypervisor_version'
op|'('
op|')'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'platform'
op|'.'
name|'node'
op|'('
op|')'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'cpu_info'"
op|':'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'cpu_info'
op|')'
op|','
nl|'\n'
string|"'supported_instances'"
op|':'
nl|'\n'
op|'['
op|'('
name|'arch'
op|'.'
name|'I686'
op|','
name|'hv_type'
op|'.'
name|'HYPERV'
op|','
name|'vm_mode'
op|'.'
name|'HVM'
op|')'
op|','
nl|'\n'
op|'('
name|'arch'
op|'.'
name|'X86_64'
op|','
name|'hv_type'
op|'.'
name|'HYPERV'
op|','
name|'vm_mode'
op|'.'
name|'HVM'
op|')'
op|']'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'dic'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
name|'def'
name|'host_power_action'
op|'('
name|'self'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots, shuts down or powers up the host."""'
newline|'\n'
name|'if'
name|'action'
name|'in'
op|'['
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_SHUTDOWN'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_REBOOT'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'host_power_action'
op|'('
name|'action'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'action'
op|'=='
name|'constants'
op|'.'
name|'HOST_POWER_ACTION_STARTUP'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Host PowerOn is not supported by the Hyper-V driver"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_ip_addr
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_host_ip_addr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_ip'
op|'='
name|'CONF'
op|'.'
name|'my_ip'
newline|'\n'
name|'if'
name|'not'
name|'host_ip'
op|':'
newline|'\n'
comment|'# Return the first available address'
nl|'\n'
indent|'            '
name|'host_ip'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_local_ips'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Host IP address is: %s"'
op|','
name|'host_ip'
op|')'
newline|'\n'
name|'return'
name|'host_ip'
newline|'\n'
nl|'\n'
DECL|member|get_host_uptime
dedent|''
name|'def'
name|'get_host_uptime'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the host uptime."""'
newline|'\n'
nl|'\n'
name|'tick_count64'
op|'='
name|'self'
op|'.'
name|'_hostutils'
op|'.'
name|'get_host_tick_count64'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# format the string to match libvirt driver uptime'
nl|'\n'
comment|'# Libvirt uptime returns a combination of the following'
nl|'\n'
comment|'# - current host time'
nl|'\n'
comment|'# - time since host is up'
nl|'\n'
comment|'# - number of logged in users'
nl|'\n'
comment|'# - cpu load'
nl|'\n'
comment|'# Since the Windows function GetTickCount64 returns only'
nl|'\n'
comment|'# the time since the host is up, returning 0s for cpu load'
nl|'\n'
comment|'# and number of logged in users.'
nl|'\n'
comment|'# This is done to ensure the format of the returned'
nl|'\n'
comment|'# value is same as in libvirt'
nl|'\n'
name|'return'
string|'"%s up %s,  0 users,  load average: 0, 0, 0"'
op|'%'
op|'('
nl|'\n'
name|'str'
op|'('
name|'time'
op|'.'
name|'strftime'
op|'('
string|'"%H:%M:%S"'
op|')'
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'milliseconds'
op|'='
name|'int'
op|'('
name|'tick_count64'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
