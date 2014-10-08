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
name|'oslo'
op|'.'
name|'utils'
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
name|'hvtype'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_mode'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'ds_util'
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
nl|'\n'
DECL|function|_get_ds_capacity_and_freespace
name|'def'
name|'_get_ds_capacity_and_freespace'
op|'('
name|'session'
op|','
name|'cluster'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ds'
op|'='
name|'ds_util'
op|'.'
name|'get_datastore'
op|'('
name|'session'
op|','
name|'cluster'
op|')'
newline|'\n'
name|'return'
name|'ds'
op|'.'
name|'capacity'
op|','
name|'ds'
op|'.'
name|'freespace'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
op|','
number|'0'
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
name|'capacity'
op|','
name|'freespace'
op|'='
name|'_get_ds_capacity_and_freespace'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_cluster'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get cpu, memory stats from the cluster'
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
name|'capacity'
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
name|'freespace'
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
nl|'\n'
op|'('
name|'arch'
op|'.'
name|'I686'
op|','
name|'hvtype'
op|'.'
name|'VMWARE'
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
name|'hvtype'
op|'.'
name|'VMWARE'
op|','
name|'vm_mode'
op|'.'
name|'HVM'
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
