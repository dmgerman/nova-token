begin_unit
comment|'# Copyright 2013 Intel Corporation.'
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
string|'"""\nCPU monitor based on compute driver to retrieve CPU information\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'monitors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'monitors'
name|'import'
name|'cpu_monitor'
name|'as'
name|'monitor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.driver'"
op|')'
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
DECL|class|ComputeDriverCPUMonitor
name|'class'
name|'ComputeDriverCPUMonitor'
op|'('
name|'monitor'
op|'.'
name|'_CPUMonitorBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""CPU monitor based on compute driver\n\n    The class inherits from the base class for resource monitors,\n    and implements the essential methods to get metric names and their real\n    values for CPU utilization.\n\n    The compute manager could load the monitors to retrieve the metrics\n    of the devices on compute nodes and know their resource information\n    periodically.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'parent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ComputeDriverCPUMonitor'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'parent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'source'
op|'='
name|'CONF'
op|'.'
name|'compute_driver'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'self'
op|'.'
name|'compute_manager'
op|'.'
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'_cpu_stats'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_frequency
name|'def'
name|'_get_cpu_frequency'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.frequency"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_user_time
name|'def'
name|'_get_cpu_user_time'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.user.time"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_kernel_time
name|'def'
name|'_get_cpu_kernel_time'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.kernel.time"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_idle_time
name|'def'
name|'_get_cpu_idle_time'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.idle.time"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_iowait_time
name|'def'
name|'_get_cpu_iowait_time'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.iowait.time"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_user_percent
name|'def'
name|'_get_cpu_user_percent'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.user.percent"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_kernel_percent
name|'def'
name|'_get_cpu_kernel_percent'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.kernel.percent"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_idle_percent
name|'def'
name|'_get_cpu_idle_percent'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.idle.percent"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_iowait_percent
name|'def'
name|'_get_cpu_iowait_percent'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.iowait.percent"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'monitors'
op|'.'
name|'ResourceMonitorBase'
op|'.'
name|'add_timestamp'
newline|'\n'
DECL|member|_get_cpu_percent
name|'def'
name|'_get_cpu_percent'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"cpu.percent"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update_data
dedent|''
name|'def'
name|'_update_data'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# Don't allow to call this function so frequently (<= 1 sec)"
nl|'\n'
indent|'        '
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"timestamp"'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'delta'
op|'='
name|'now'
op|'-'
name|'self'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"timestamp"'
op|')'
newline|'\n'
name|'if'
name|'delta'
op|'.'
name|'seconds'
op|'<='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"timestamp"'
op|']'
op|'='
name|'now'
newline|'\n'
nl|'\n'
comment|"# Extract node's CPU statistics."
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'stats'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_host_cpu_stats'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.user.time"'
op|']'
op|'='
name|'stats'
op|'['
string|'"user"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.kernel.time"'
op|']'
op|'='
name|'stats'
op|'['
string|'"kernel"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.idle.time"'
op|']'
op|'='
name|'stats'
op|'['
string|'"idle"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.iowait.time"'
op|']'
op|'='
name|'stats'
op|'['
string|'"iowait"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.frequency"'
op|']'
op|'='
name|'stats'
op|'['
string|'"frequency"'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'NotImplementedError'
op|','
name|'TypeError'
op|','
name|'KeyError'
op|')'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Not all properties needed are implemented "'
nl|'\n'
string|'"in the compute driver: %s"'
op|')'
op|','
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ResourceMonitorError'
op|'('
nl|'\n'
name|'monitor'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
comment|'# The compute driver API returns the absolute values for CPU times.'
nl|'\n'
comment|'# We compute the utilization percentages for each specific CPU time'
nl|'\n'
comment|'# after calculating the delta between the current reading and the'
nl|'\n'
comment|'# previous reading.'
nl|'\n'
dedent|''
name|'stats'
op|'['
string|'"total"'
op|']'
op|'='
op|'('
name|'stats'
op|'['
string|'"user"'
op|']'
op|'+'
name|'stats'
op|'['
string|'"kernel"'
op|']'
nl|'\n'
op|'+'
name|'stats'
op|'['
string|'"idle"'
op|']'
op|'+'
name|'stats'
op|'['
string|'"iowait"'
op|']'
op|')'
newline|'\n'
name|'cputime'
op|'='
name|'float'
op|'('
name|'stats'
op|'['
string|'"total"'
op|']'
op|'-'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"total"'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'perc'
op|'='
op|'('
name|'stats'
op|'['
string|'"user"'
op|']'
op|'-'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"user"'
op|','
number|'0'
op|')'
op|')'
op|'/'
name|'cputime'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.user.percent"'
op|']'
op|'='
name|'perc'
newline|'\n'
nl|'\n'
name|'perc'
op|'='
op|'('
name|'stats'
op|'['
string|'"kernel"'
op|']'
op|'-'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"kernel"'
op|','
number|'0'
op|')'
op|')'
op|'/'
name|'cputime'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.kernel.percent"'
op|']'
op|'='
name|'perc'
newline|'\n'
nl|'\n'
name|'perc'
op|'='
op|'('
name|'stats'
op|'['
string|'"idle"'
op|']'
op|'-'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"idle"'
op|','
number|'0'
op|')'
op|')'
op|'/'
name|'cputime'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.idle.percent"'
op|']'
op|'='
name|'perc'
newline|'\n'
nl|'\n'
name|'perc'
op|'='
op|'('
name|'stats'
op|'['
string|'"iowait"'
op|']'
op|'-'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"iowait"'
op|','
number|'0'
op|')'
op|')'
op|'/'
name|'cputime'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.iowait.percent"'
op|']'
op|'='
name|'perc'
newline|'\n'
nl|'\n'
comment|'# Compute the current system-wide CPU utilization as a percentage.'
nl|'\n'
name|'used'
op|'='
name|'stats'
op|'['
string|'"user"'
op|']'
op|'+'
name|'stats'
op|'['
string|'"kernel"'
op|']'
op|'+'
name|'stats'
op|'['
string|'"iowait"'
op|']'
newline|'\n'
name|'prev_used'
op|'='
op|'('
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"user"'
op|','
number|'0'
op|')'
nl|'\n'
op|'+'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"kernel"'
op|','
number|'0'
op|')'
nl|'\n'
op|'+'
name|'self'
op|'.'
name|'_cpu_stats'
op|'.'
name|'get'
op|'('
string|'"iowait"'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'perc'
op|'='
op|'('
name|'used'
op|'-'
name|'prev_used'
op|')'
op|'/'
name|'cputime'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'['
string|'"cpu.percent"'
op|']'
op|'='
name|'perc'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_cpu_stats'
op|'='
name|'stats'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
