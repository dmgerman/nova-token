begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""\nManage hosts in the current zone.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'UserDict'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
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
name|'import'
name|'exception'
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
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'weights'
newline|'\n'
nl|'\n'
DECL|variable|host_manager_opts
name|'host_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'scheduler_available_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.scheduler.filters.all_filters'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Filter classes available to the scheduler which may '"
nl|'\n'
string|"'be specified more than once.  An entry of '"
nl|'\n'
string|'\'"nova.scheduler.filters.standard_filters" \''
nl|'\n'
string|"'maps to all filters included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_default_filters'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'RetryFilter'"
op|','
nl|'\n'
string|"'AvailabilityZoneFilter'"
op|','
nl|'\n'
string|"'RamFilter'"
op|','
nl|'\n'
string|"'ComputeFilter'"
op|','
nl|'\n'
string|"'ComputeCapabilitiesFilter'"
op|','
nl|'\n'
string|"'ImagePropertiesFilter'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which filter class names to use for filtering hosts '"
nl|'\n'
string|"'when not specified in the request.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_weight_classes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.scheduler.weights.all_weighers'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which weight class names to use for weighing hosts'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'host_manager_opts'
op|')'
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
DECL|class|ReadOnlyDict
name|'class'
name|'ReadOnlyDict'
op|'('
name|'UserDict'
op|'.'
name|'IterableUserDict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A read-only dict."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'source'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'update'
op|'('
name|'source'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|pop
dedent|''
name|'def'
name|'pop'
op|'('
name|'self'
op|','
name|'key'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|popitem
dedent|''
name|'def'
name|'popitem'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'source'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'source'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'source'
op|','
name|'UserDict'
op|'.'
name|'UserDict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
name|'source'
op|'.'
name|'data'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'source'
op|','
name|'type'
op|'('
op|'{'
op|'}'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'='
name|'source'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'TypeError'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostState
dedent|''
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
string|'"""Mutable and immutable information tracked for a host.\n    This is an attempt to remove the ad-hoc data structures\n    previously used and lock down access.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'node'
op|','
name|'capabilities'
op|'='
name|'None'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'nodename'
op|'='
name|'node'
newline|'\n'
name|'self'
op|'.'
name|'update_capabilities'
op|'('
name|'capabilities'
op|','
name|'service'
op|')'
newline|'\n'
nl|'\n'
comment|'# Mutable available resources.'
nl|'\n'
comment|'# These will change as resources are virtually "consumed".'
nl|'\n'
name|'self'
op|'.'
name|'total_usable_disk_gb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'disk_mb_used'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_total'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'='
number|'0'
newline|'\n'
comment|"# Valid vm types on this host: 'pv', 'hvm' or 'all'"
nl|'\n'
name|'if'
string|"'allowed_vm_type'"
name|'in'
name|'self'
op|'.'
name|'capabilities'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'allowed_vm_type'
op|'='
name|'self'
op|'.'
name|'capabilities'
op|'['
string|"'allowed_vm_type'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'allowed_vm_type'
op|'='
string|"'all'"
newline|'\n'
nl|'\n'
comment|'# Additional host information from the compute node stats:'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'vm_states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'task_states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'num_instances'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'num_instances_by_project'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'num_instances_by_os_type'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'num_io_ops'
op|'='
number|'0'
newline|'\n'
nl|'\n'
comment|'# Resource oversubscription values for the compute host:'
nl|'\n'
name|'self'
op|'.'
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'updated'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|update_capabilities
dedent|''
name|'def'
name|'update_capabilities'
op|'('
name|'self'
op|','
name|'capabilities'
op|'='
name|'None'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# Read-only capability dicts'
nl|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'capabilities'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'capabilities'
op|'='
name|'ReadOnlyDict'
op|'('
name|'capabilities'
op|')'
newline|'\n'
name|'if'
name|'service'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'service'
op|'='
name|'ReadOnlyDict'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_from_compute_node
dedent|''
name|'def'
name|'update_from_compute_node'
op|'('
name|'self'
op|','
name|'compute'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update information about a host from its compute_node info."""'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'updated'
name|'and'
name|'compute'
op|'['
string|"'updated_at'"
op|']'
nl|'\n'
name|'and'
name|'self'
op|'.'
name|'updated'
op|'>'
name|'compute'
op|'['
string|"'updated_at'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'all_ram_mb'
op|'='
name|'compute'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Assume virtual size is all consumed by instances if use qcow2 disk.'
nl|'\n'
name|'least'
op|'='
name|'compute'
op|'.'
name|'get'
op|'('
string|"'disk_available_least'"
op|')'
newline|'\n'
name|'free_disk_mb'
op|'='
name|'least'
name|'if'
name|'least'
name|'is'
name|'not'
name|'None'
name|'else'
name|'compute'
op|'['
string|"'free_disk_gb'"
op|']'
newline|'\n'
name|'free_disk_mb'
op|'*='
number|'1024'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'disk_mb_used'
op|'='
name|'compute'
op|'['
string|"'local_gb_used'"
op|']'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
comment|'#NOTE(jogo) free_ram_mb can be negative'
nl|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'='
name|'compute'
op|'['
string|"'free_ram_mb'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'total_usable_ram_mb'
op|'='
name|'all_ram_mb'
newline|'\n'
name|'self'
op|'.'
name|'total_usable_disk_gb'
op|'='
name|'compute'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'='
name|'free_disk_mb'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_total'
op|'='
name|'compute'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'='
name|'compute'
op|'['
string|"'vcpus_used'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'updated'
op|'='
name|'compute'
op|'['
string|"'updated_at'"
op|']'
newline|'\n'
nl|'\n'
name|'stats'
op|'='
name|'compute'
op|'.'
name|'get'
op|'('
string|"'stats'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'statmap'
op|'='
name|'self'
op|'.'
name|'_statmap'
op|'('
name|'stats'
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances on host'
nl|'\n'
name|'self'
op|'.'
name|'num_instances'
op|'='
name|'int'
op|'('
name|'statmap'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances by project_id'
nl|'\n'
name|'project_id_keys'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'statmap'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
nl|'\n'
name|'k'
op|'.'
name|'startswith'
op|'('
string|'"num_proj_"'
op|')'
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'project_id_keys'
op|':'
newline|'\n'
indent|'            '
name|'project_id'
op|'='
name|'key'
op|'['
number|'9'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'num_instances_by_project'
op|'['
name|'project_id'
op|']'
op|'='
name|'int'
op|'('
name|'statmap'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances in certain vm_states'
nl|'\n'
dedent|''
name|'vm_state_keys'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'statmap'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|'"num_vm_"'
op|')'
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'vm_state_keys'
op|':'
newline|'\n'
indent|'            '
name|'vm_state'
op|'='
name|'key'
op|'['
number|'7'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'vm_states'
op|'['
name|'vm_state'
op|']'
op|'='
name|'int'
op|'('
name|'statmap'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances in certain task_states'
nl|'\n'
dedent|''
name|'task_state_keys'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'statmap'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
nl|'\n'
name|'k'
op|'.'
name|'startswith'
op|'('
string|'"num_task_"'
op|')'
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'task_state_keys'
op|':'
newline|'\n'
indent|'            '
name|'task_state'
op|'='
name|'key'
op|'['
number|'9'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'task_states'
op|'['
name|'task_state'
op|']'
op|'='
name|'int'
op|'('
name|'statmap'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances by host_type'
nl|'\n'
dedent|''
name|'os_keys'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'statmap'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|'"num_os_type_"'
op|')'
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'os_keys'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'='
name|'key'
op|'['
number|'12'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'num_instances_by_os_type'
op|'['
name|'os'
op|']'
op|'='
name|'int'
op|'('
name|'statmap'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'num_io_ops'
op|'='
name|'int'
op|'('
name|'statmap'
op|'.'
name|'get'
op|'('
string|"'io_workload'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|consume_from_instance
dedent|''
name|'def'
name|'consume_from_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Incrementally update host state from an instance."""'
newline|'\n'
name|'disk_mb'
op|'='
op|'('
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
op|'*'
number|'1024'
newline|'\n'
name|'ram_mb'
op|'='
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'vcpus'
op|'='
name|'instance'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'free_ram_mb'
op|'-='
name|'ram_mb'
newline|'\n'
name|'self'
op|'.'
name|'free_disk_mb'
op|'-='
name|'disk_mb'
newline|'\n'
name|'self'
op|'.'
name|'vcpus_used'
op|'+='
name|'vcpus'
newline|'\n'
name|'self'
op|'.'
name|'updated'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Track number of instances on host'
nl|'\n'
name|'self'
op|'.'
name|'num_instances'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Track number of instances by project_id'
nl|'\n'
name|'project_id'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|')'
newline|'\n'
name|'if'
name|'project_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'num_instances_by_project'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'num_instances_by_project'
op|'['
name|'project_id'
op|']'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'num_instances_by_project'
op|'['
name|'project_id'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Track number of instances in certain vm_states'
nl|'\n'
name|'vm_state'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
name|'if'
name|'vm_state'
name|'not'
name|'in'
name|'self'
op|'.'
name|'vm_states'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'vm_states'
op|'['
name|'vm_state'
op|']'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'vm_states'
op|'['
name|'vm_state'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Track number of instances in certain task_states'
nl|'\n'
name|'task_state'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|')'
newline|'\n'
name|'if'
name|'task_state'
name|'not'
name|'in'
name|'self'
op|'.'
name|'task_states'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'task_states'
op|'['
name|'task_state'
op|']'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'task_states'
op|'['
name|'task_state'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Track number of instances by host_type'
nl|'\n'
name|'os_type'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'os_type'"
op|')'
newline|'\n'
name|'if'
name|'os_type'
name|'not'
name|'in'
name|'self'
op|'.'
name|'num_instances_by_os_type'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'num_instances_by_os_type'
op|'['
name|'os_type'
op|']'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'num_instances_by_os_type'
op|'['
name|'os_type'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'vm_state'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'vm_state'"
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|')'
newline|'\n'
name|'task_state'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'task_state'"
op|')'
newline|'\n'
name|'if'
name|'vm_state'
op|'=='
name|'vm_states'
op|'.'
name|'BUILDING'
name|'or'
name|'task_state'
name|'in'
op|'['
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|','
name|'task_states'
op|'.'
name|'REBUILDING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_PREP'
op|','
name|'task_states'
op|'.'
name|'IMAGE_SNAPSHOT'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'IMAGE_BACKUP'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'num_io_ops'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_statmap
dedent|''
dedent|''
name|'def'
name|'_statmap'
op|'('
name|'self'
op|','
name|'stats'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
op|'('
name|'st'
op|'['
string|"'key'"
op|']'
op|','
name|'st'
op|'['
string|"'value'"
op|']'
op|')'
name|'for'
name|'st'
name|'in'
name|'stats'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
string|'"(%s, %s) ram:%s disk:%s io_ops:%s instances:%s vm_type:%s"'
op|'%'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'nodename'
op|','
name|'self'
op|'.'
name|'free_ram_mb'
op|','
name|'self'
op|'.'
name|'free_disk_mb'
op|','
nl|'\n'
name|'self'
op|'.'
name|'num_io_ops'
op|','
name|'self'
op|'.'
name|'num_instances'
op|','
name|'self'
op|'.'
name|'allowed_vm_type'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostManager
dedent|''
dedent|''
name|'class'
name|'HostManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base HostManager class."""'
newline|'\n'
nl|'\n'
comment|'# Can be overridden in a subclass'
nl|'\n'
DECL|variable|host_state_cls
name|'host_state_cls'
op|'='
name|'HostState'
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
comment|'# { (host, hypervisor_hostname) : { <service> : { cap k : v }}}'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'host_state_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'HostFilterHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'scheduler_available_filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weight_handler'
op|'='
name|'weights'
op|'.'
name|'HostWeightHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weight_classes'
op|'='
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'scheduler_weight_classes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_choose_host_filters
dedent|''
name|'def'
name|'_choose_host_filters'
op|'('
name|'self'
op|','
name|'filter_cls_names'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Since the caller may specify which filters to use we need\n        to have an authoritative list of what is permissible. This\n        function checks the filter names against a predefined set\n        of acceptable filters.\n        """'
newline|'\n'
name|'if'
name|'filter_cls_names'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'filter_cls_names'
op|'='
name|'CONF'
op|'.'
name|'scheduler_default_filters'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'filter_cls_names'
op|','
op|'('
name|'list'
op|','
name|'tuple'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'filter_cls_names'
op|'='
op|'['
name|'filter_cls_names'
op|']'
newline|'\n'
dedent|''
name|'good_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'bad_filters'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'filter_name'
name|'in'
name|'filter_cls_names'
op|':'
newline|'\n'
indent|'            '
name|'found_class'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'cls'
name|'in'
name|'self'
op|'.'
name|'filter_classes'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'cls'
op|'.'
name|'__name__'
op|'=='
name|'filter_name'
op|':'
newline|'\n'
indent|'                    '
name|'good_filters'
op|'.'
name|'append'
op|'('
name|'cls'
op|')'
newline|'\n'
name|'found_class'
op|'='
name|'True'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'found_class'
op|':'
newline|'\n'
indent|'                '
name|'bad_filters'
op|'.'
name|'append'
op|'('
name|'filter_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'bad_filters'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
name|'bad_filters'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'SchedulerHostFilterNotFound'
op|'('
name|'filter_name'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'good_filters'
newline|'\n'
nl|'\n'
DECL|member|get_filtered_hosts
dedent|''
name|'def'
name|'get_filtered_hosts'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'filter_class_names'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Filter hosts and return only ones passing all filters."""'
newline|'\n'
nl|'\n'
DECL|function|_strip_ignore_hosts
name|'def'
name|'_strip_ignore_hosts'
op|'('
name|'host_map'
op|','
name|'hosts_to_ignore'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ignored_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'host'
name|'in'
name|'hosts_to_ignore'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'host'
name|'in'
name|'host_map'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'host_map'
op|'['
name|'host'
op|']'
newline|'\n'
name|'ignored_hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'ignored_hosts_str'
op|'='
string|"', '"
op|'.'
name|'join'
op|'('
name|'ignored_hosts'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Host filter ignoring hosts: %(ignored_hosts_str)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_match_forced_hosts
dedent|''
name|'def'
name|'_match_forced_hosts'
op|'('
name|'host_map'
op|','
name|'hosts_to_force'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'host'
name|'in'
name|'host_map'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'host'
name|'not'
name|'in'
name|'hosts_to_force'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'host_map'
op|'['
name|'host'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'host_map'
op|':'
newline|'\n'
indent|'                '
name|'forced_hosts_str'
op|'='
string|"', '"
op|'.'
name|'join'
op|'('
name|'hosts_to_force'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"No hosts matched due to not matching \'force_hosts\'"'
nl|'\n'
string|'"value of \'%(forced_hosts_str)s\'"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'forced_hosts_str'
op|'='
string|"', '"
op|'.'
name|'join'
op|'('
name|'host_map'
op|'.'
name|'iterkeys'
op|'('
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Host filter forcing available hosts to '"
nl|'\n'
string|"'%(forced_hosts_str)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'_choose_host_filters'
op|'('
name|'filter_class_names'
op|')'
newline|'\n'
name|'ignore_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'ignore_hosts'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'force_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_hosts'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'ignore_hosts'
name|'or'
name|'force_hosts'
op|':'
newline|'\n'
indent|'            '
name|'name_to_cls_map'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'x'
op|'.'
name|'host'
op|','
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'hosts'
op|']'
op|')'
newline|'\n'
name|'if'
name|'ignore_hosts'
op|':'
newline|'\n'
indent|'                '
name|'_strip_ignore_hosts'
op|'('
name|'name_to_cls_map'
op|','
name|'ignore_hosts'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'name_to_cls_map'
op|':'
newline|'\n'
indent|'                    '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'force_hosts'
op|':'
newline|'\n'
indent|'                '
name|'_match_forced_hosts'
op|'('
name|'name_to_cls_map'
op|','
name|'force_hosts'
op|')'
newline|'\n'
comment|'# NOTE(vish): Skip filters on forced hosts.'
nl|'\n'
name|'if'
name|'name_to_cls_map'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'name_to_cls_map'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'hosts'
op|'='
name|'name_to_cls_map'
op|'.'
name|'itervalues'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'filter_classes'
op|','
nl|'\n'
name|'hosts'
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_weighed_hosts
dedent|''
name|'def'
name|'get_weighed_hosts'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Weigh the hosts."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_weighed_objects'
op|'('
name|'self'
op|'.'
name|'weight_classes'
op|','
nl|'\n'
name|'hosts'
op|','
name|'weight_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the per-service capabilities based on this notification."""'
newline|'\n'
nl|'\n'
name|'if'
name|'service_name'
op|'!='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Ignoring %(service_name)s service update '"
nl|'\n'
string|"'from %(host)s'"
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'state_key'
op|'='
op|'('
name|'host'
op|','
name|'capabilities'
op|'.'
name|'get'
op|'('
string|"'hypervisor_hostname'"
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received %(service_name)s service update from "'
nl|'\n'
string|'"%(state_key)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|"# Copy the capabilities, so we don't modify the original dict"
nl|'\n'
name|'capab_copy'
op|'='
name|'dict'
op|'('
name|'capabilities'
op|')'
newline|'\n'
name|'capab_copy'
op|'['
string|'"timestamp"'
op|']'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
comment|'# Reported time'
newline|'\n'
name|'self'
op|'.'
name|'service_states'
op|'['
name|'state_key'
op|']'
op|'='
name|'capab_copy'
newline|'\n'
nl|'\n'
DECL|member|get_all_host_states
dedent|''
name|'def'
name|'get_all_host_states'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of HostStates that represents all the hosts\n        the HostManager knows about. Also, each of the consumable resources\n        in HostState are pre-populated and adjusted based on data in the db.\n        """'
newline|'\n'
nl|'\n'
comment|'# Get resource usage across the available compute nodes:'
nl|'\n'
name|'compute_nodes'
op|'='
name|'db'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'seen_nodes'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'compute'
name|'in'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'compute'
op|'['
string|"'service'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'service'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"No service for compute ID %s"'
op|')'
op|'%'
name|'compute'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'node'
op|'='
name|'compute'
op|'.'
name|'get'
op|'('
string|"'hypervisor_hostname'"
op|')'
newline|'\n'
name|'state_key'
op|'='
op|'('
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'capabilities'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'.'
name|'get'
op|'('
name|'state_key'
op|','
name|'None'
op|')'
newline|'\n'
name|'host_state'
op|'='
name|'self'
op|'.'
name|'host_state_map'
op|'.'
name|'get'
op|'('
name|'state_key'
op|')'
newline|'\n'
name|'if'
name|'host_state'
op|':'
newline|'\n'
indent|'                '
name|'host_state'
op|'.'
name|'update_capabilities'
op|'('
name|'capabilities'
op|','
nl|'\n'
name|'dict'
op|'('
name|'service'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'host_state'
op|'='
name|'self'
op|'.'
name|'host_state_cls'
op|'('
name|'host'
op|','
name|'node'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'service'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_state_map'
op|'['
name|'state_key'
op|']'
op|'='
name|'host_state'
newline|'\n'
dedent|''
name|'host_state'
op|'.'
name|'update_from_compute_node'
op|'('
name|'compute'
op|')'
newline|'\n'
name|'seen_nodes'
op|'.'
name|'add'
op|'('
name|'state_key'
op|')'
newline|'\n'
nl|'\n'
comment|'# remove compute nodes from host_state_map if they are not active'
nl|'\n'
dedent|''
name|'dead_nodes'
op|'='
name|'set'
op|'('
name|'self'
op|'.'
name|'host_state_map'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'-'
name|'seen_nodes'
newline|'\n'
name|'for'
name|'state_key'
name|'in'
name|'dead_nodes'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|','
name|'node'
op|'='
name|'state_key'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Removing dead compute node %(host)s:%(node)s "'
nl|'\n'
string|'"from scheduler"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'host_state_map'
op|'['
name|'state_key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'host_state_map'
op|'.'
name|'itervalues'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
