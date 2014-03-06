begin_unit
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright (c) 2012 VMware, Inc.'
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
string|'"""\nManagement class for host-related functions (start, reboot, etc).\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
newline|'\n'
nl|'\n'
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
DECL|class|Host
name|'class'
name|'Host'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements host related operations."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
name|'def'
name|'host_power_action'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots or shuts down the host."""'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(action)s %(host)s"'
op|')'
op|','
op|'{'
string|"'action'"
op|':'
name|'action'
op|','
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'action'
op|'=='
string|'"reboot"'
op|':'
newline|'\n'
indent|'            '
name|'host_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"RebootHost_Task"'
op|','
name|'host_mor'
op|','
nl|'\n'
name|'force'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|'"shutdown"'
op|':'
newline|'\n'
indent|'            '
name|'host_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"ShutdownHost_Task"'
op|','
name|'host_mor'
op|','
nl|'\n'
name|'force'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|'"startup"'
op|':'
newline|'\n'
indent|'            '
name|'host_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"PowerUpHostFromStandBy_Task"'
op|','
name|'host_mor'
op|','
nl|'\n'
name|'timeoutSec'
op|'='
number|'60'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'host_task'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_maintenance_mode
dedent|''
name|'def'
name|'host_maintenance_mode'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start/Stop host maintenance window. On start, it triggers\n        guest VMs evacuation.\n        """'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Set maintenance mod on %(host)s to %(mode)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'mode'"
op|':'
name|'mode'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'mode'
op|':'
newline|'\n'
indent|'            '
name|'host_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"EnterMaintenanceMode_Task"'
op|','
nl|'\n'
name|'host_mor'
op|','
name|'timeout'
op|'='
number|'0'
op|','
nl|'\n'
name|'evacuatePoweredOffVms'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'host_task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|'"ExitMaintenanceMode_Task"'
op|','
nl|'\n'
name|'host_mor'
op|','
name|'timeout'
op|'='
number|'0'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_wait_for_task'
op|'('
name|'host_task'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_host_enabled
dedent|''
name|'def'
name|'set_host_enabled'
op|'('
name|'self'
op|','
name|'_host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the specified host\'s ability to accept new instances."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostState
dedent|''
dedent|''
name|'class'
name|'HostState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages information about the ESX host this compute\n    node is running on.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'host_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HostState'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host_name'
newline|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the current state of the host. If \'refresh\' is\n        True, run the update first.\n        """'
newline|'\n'
name|'if'
name|'refresh'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_stats'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_stats'
newline|'\n'
nl|'\n'
DECL|member|update_status
dedent|''
name|'def'
name|'update_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the current state of the host.\n        """'
newline|'\n'
name|'host_mor'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'summary'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
nl|'\n'
name|'host_mor'
op|','
nl|'\n'
string|'"HostSystem"'
op|','
nl|'\n'
string|'"summary"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'summary'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ds'
op|'='
name|'vm_util'
op|'.'
name|'get_datastore_ref_and_name'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|':'
newline|'\n'
indent|'            '
name|'ds'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'data'
op|'['
string|'"vcpus"'
op|']'
op|'='
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'numCpuThreads'
newline|'\n'
name|'data'
op|'['
string|'"cpu_info"'
op|']'
op|'='
op|'{'
string|'"vendor"'
op|':'
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'vendor'
op|','
nl|'\n'
string|'"model"'
op|':'
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'cpuModel'
op|','
nl|'\n'
string|'"topology"'
op|':'
op|'{'
string|'"cores"'
op|':'
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'numCpuCores'
op|','
nl|'\n'
string|'"sockets"'
op|':'
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'numCpuPkgs'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'numCpuThreads'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'data'
op|'['
string|'"disk_total"'
op|']'
op|'='
name|'ds'
op|'['
number|'2'
op|']'
op|'/'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'data'
op|'['
string|'"disk_available"'
op|']'
op|'='
name|'ds'
op|'['
number|'3'
op|']'
op|'/'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'data'
op|'['
string|'"disk_used"'
op|']'
op|'='
name|'data'
op|'['
string|'"disk_total"'
op|']'
op|'-'
name|'data'
op|'['
string|'"disk_available"'
op|']'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_total"'
op|']'
op|'='
name|'summary'
op|'.'
name|'hardware'
op|'.'
name|'memorySize'
op|'/'
name|'units'
op|'.'
name|'Mi'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_free"'
op|']'
op|'='
name|'data'
op|'['
string|'"host_memory_total"'
op|']'
op|'-'
name|'summary'
op|'.'
name|'quickStats'
op|'.'
name|'overallMemoryUsage'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_type"'
op|']'
op|'='
name|'summary'
op|'.'
name|'config'
op|'.'
name|'product'
op|'.'
name|'name'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_version"'
op|']'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_int'
op|'('
nl|'\n'
name|'str'
op|'('
name|'summary'
op|'.'
name|'config'
op|'.'
name|'product'
op|'.'
name|'version'
op|')'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_hostname"'
op|']'
op|'='
name|'self'
op|'.'
name|'_host_name'
newline|'\n'
name|'data'
op|'['
string|'"supported_instances"'
op|']'
op|'='
op|'['
op|'('
string|"'i686'"
op|','
string|"'vmware'"
op|','
string|"'hvm'"
op|')'
op|','
nl|'\n'
op|'('
string|"'x86_64'"
op|','
string|"'vmware'"
op|','
string|"'hvm'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
name|'data'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VCState
dedent|''
dedent|''
name|'class'
name|'VCState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages information about the VC host this compute\n    node is running on.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'host_name'
op|','
name|'cluster'
op|','
name|'datastore_regex'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VCState'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host_name'
newline|'\n'
name|'self'
op|'.'
name|'_cluster'
op|'='
name|'cluster'
newline|'\n'
name|'self'
op|'.'
name|'_datastore_regex'
op|'='
name|'datastore_regex'
newline|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the current state of the host. If \'refresh\' is\n        True, run the update first.\n        """'
newline|'\n'
name|'if'
name|'refresh'
name|'or'
name|'not'
name|'self'
op|'.'
name|'_stats'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'update_status'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_stats'
newline|'\n'
nl|'\n'
DECL|member|update_status
dedent|''
name|'def'
name|'update_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the current state of the cluster."""'
newline|'\n'
comment|'# Get cpu, memory stats, disk from the cluster'
nl|'\n'
name|'stats'
op|'='
name|'vm_util'
op|'.'
name|'get_stats_from_cluster'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'self'
op|'.'
name|'_cluster'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_datastore_regex'
op|')'
newline|'\n'
name|'about_info'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_about_info"'
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'data'
op|'['
string|'"vcpus"'
op|']'
op|'='
name|'stats'
op|'['
string|"'cpu'"
op|']'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'data'
op|'['
string|'"cpu_info"'
op|']'
op|'='
op|'{'
string|'"vendor"'
op|':'
name|'stats'
op|'['
string|"'cpu'"
op|']'
op|'['
string|"'vendor'"
op|']'
op|','
nl|'\n'
string|'"model"'
op|':'
name|'stats'
op|'['
string|"'cpu'"
op|']'
op|'['
string|"'model'"
op|']'
op|','
nl|'\n'
string|'"topology"'
op|':'
op|'{'
string|'"cores"'
op|':'
name|'stats'
op|'['
string|"'cpu'"
op|']'
op|'['
string|"'cores'"
op|']'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'stats'
op|'['
string|"'cpu'"
op|']'
op|'['
string|"'vcpus'"
op|']'
op|'}'
op|'}'
newline|'\n'
name|'data'
op|'['
string|'"disk_total"'
op|']'
op|'='
name|'stats'
op|'['
string|"'disk'"
op|']'
op|'['
string|"'total'"
op|']'
newline|'\n'
name|'data'
op|'['
string|'"disk_available"'
op|']'
op|'='
name|'stats'
op|'['
string|"'disk'"
op|']'
op|'['
string|"'free'"
op|']'
newline|'\n'
name|'data'
op|'['
string|'"disk_used"'
op|']'
op|'='
name|'data'
op|'['
string|'"disk_total"'
op|']'
op|'-'
name|'data'
op|'['
string|'"disk_available"'
op|']'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_total"'
op|']'
op|'='
name|'stats'
op|'['
string|"'mem'"
op|']'
op|'['
string|"'total'"
op|']'
newline|'\n'
name|'data'
op|'['
string|'"host_memory_free"'
op|']'
op|'='
name|'stats'
op|'['
string|"'mem'"
op|']'
op|'['
string|"'free'"
op|']'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_type"'
op|']'
op|'='
name|'about_info'
op|'.'
name|'name'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_version"'
op|']'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_int'
op|'('
nl|'\n'
name|'str'
op|'('
name|'about_info'
op|'.'
name|'version'
op|')'
op|')'
newline|'\n'
name|'data'
op|'['
string|'"hypervisor_hostname"'
op|']'
op|'='
name|'self'
op|'.'
name|'_host_name'
newline|'\n'
name|'data'
op|'['
string|'"supported_instances"'
op|']'
op|'='
op|'['
op|'('
string|"'i686'"
op|','
string|"'vmware'"
op|','
string|"'hvm'"
op|')'
op|','
nl|'\n'
op|'('
string|"'x86_64'"
op|','
string|"'vmware'"
op|','
string|"'hvm'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_stats'
op|'='
name|'data'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
