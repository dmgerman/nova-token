begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
string|'"""Handles database requests from other nova services."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
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
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
nl|'\n'
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
comment|'# Instead of having a huge list of arguments to instance_update(), we just'
nl|'\n'
comment|'# accept a dict of fields to update and use this whitelist to validate it.'
nl|'\n'
DECL|variable|allowed_updates
name|'allowed_updates'
op|'='
op|'['
string|"'task_state'"
op|','
string|"'vm_state'"
op|','
string|"'expected_task_state'"
op|','
nl|'\n'
string|"'power_state'"
op|','
string|"'access_ip_v4'"
op|','
string|"'access_ip_v6'"
op|','
nl|'\n'
string|"'launched_at'"
op|','
string|"'terminated_at'"
op|','
string|"'host'"
op|','
string|"'node'"
op|','
nl|'\n'
string|"'memory_mb'"
op|','
string|"'vcpus'"
op|','
string|"'root_gb'"
op|','
string|"'ephemeral_gb'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|','
string|"'root_device_name'"
op|','
string|"'launched_on'"
op|','
nl|'\n'
string|"'progress'"
op|','
string|"'vm_mode'"
op|','
string|"'default_ephemeral_device'"
op|','
nl|'\n'
string|"'default_swap_device'"
op|','
string|"'root_device_name'"
op|','
nl|'\n'
string|"'system_metadata'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'# Fields that we want to convert back into a datetime object.'
nl|'\n'
DECL|variable|datetime_fields
name|'datetime_fields'
op|'='
op|'['
string|"'launched_at'"
op|','
string|"'terminated_at'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorManager
name|'class'
name|'ConductorManager'
op|'('
name|'manager'
op|'.'
name|'SchedulerDependentManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mission: TBD."""'
newline|'\n'
nl|'\n'
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.40'"
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'ConductorManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'conductor'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'='
name|'compute_api'
op|'.'
name|'SecurityGroupAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|ping
dedent|''
name|'def'
name|'ping'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
op|'{'
string|"'service'"
op|':'
string|"'conductor'"
op|','
string|"'arg'"
op|':'
name|'arg'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'KeyError'
op|','
name|'ValueError'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidUUID'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'UnexpectedTaskStateError'
op|')'
newline|'\n'
DECL|member|instance_update
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'updates'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'not'
name|'in'
name|'allowed_updates'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Instance update attempted for "'
nl|'\n'
string|'"\'%(key)s\' on %(instance_uuid)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'KeyError'
op|'('
string|'"unexpected update keyword \'%s\'"'
op|'%'
name|'key'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'key'
name|'in'
name|'datetime_fields'
name|'and'
name|'isinstance'
op|'('
name|'value'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'old_ref'
op|','
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'instance_ref'
op|','
name|'service'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|')'
newline|'\n'
DECL|member|instance_get
name|'def'
name|'instance_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|')'
newline|'\n'
DECL|member|instance_get_by_uuid
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all
dedent|''
name|'def'
name|'instance_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_host
dedent|''
name|'def'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'node'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_host_and_node'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'MigrationNotFound'
op|')'
newline|'\n'
DECL|member|migration_get
name|'def'
name|'migration_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'migration_get'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'migration_id'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_get_unconfirmed_by_dest_compute
dedent|''
name|'def'
name|'migration_get_unconfirmed_by_dest_compute'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'confirm_window'
op|','
nl|'\n'
name|'dest_compute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migrations'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'migration_get_unconfirmed_by_dest_compute'
op|'('
nl|'\n'
name|'context'
op|','
name|'confirm_window'
op|','
name|'dest_compute'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migrations'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_get_in_progress_by_host_and_node
dedent|''
name|'def'
name|'migration_get_in_progress_by_host_and_node'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migrations'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'migration_get_in_progress_by_host_and_node'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migrations'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_create
dedent|''
name|'def'
name|'migration_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'.'
name|'update'
op|'('
op|'{'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'source_compute'"
op|':'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'source_node'"
op|':'
name|'instance'
op|'['
string|"'node'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'migration_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'migration_create'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'MigrationNotFound'
op|')'
newline|'\n'
DECL|member|migration_update
name|'def'
name|'migration_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'migration_update'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'migration'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
name|'status'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'migration_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'AggregateHostExists'
op|')'
newline|'\n'
DECL|member|aggregate_host_add
name|'def'
name|'aggregate_host_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_host_add'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'host_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'AggregateHostNotFound'
op|')'
newline|'\n'
DECL|member|aggregate_host_delete
name|'def'
name|'aggregate_host_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'AggregateNotFound'
op|')'
newline|'\n'
DECL|member|aggregate_get
name|'def'
name|'aggregate_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_get'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'aggregate_id'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get_by_host
dedent|''
name|'def'
name|'aggregate_get_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregates'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_get_by_host'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'host'
op|','
name|'key'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'aggregates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_add
dedent|''
name|'def'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'new_metadata'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_metadata_add'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'metadata'
op|','
name|'set_delete'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'new_metadata'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'AggregateMetadataNotFound'
op|')'
newline|'\n'
DECL|member|aggregate_metadata_delete
name|'def'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'aggregate_metadata_delete'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'aggregate'
op|'['
string|"'id'"
op|']'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bw_usage_update
dedent|''
name|'def'
name|'bw_usage_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'bw_in'
op|'='
name|'None'
op|','
name|'bw_out'
op|'='
name|'None'
op|','
nl|'\n'
name|'last_ctr_in'
op|'='
name|'None'
op|','
name|'last_ctr_out'
op|'='
name|'None'
op|','
nl|'\n'
name|'last_refreshed'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'['
name|'bw_in'
op|','
name|'bw_out'
op|','
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|']'
op|'.'
name|'count'
op|'('
name|'None'
op|')'
op|'!='
number|'4'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'bw_usage_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'bw_in'
op|','
name|'bw_out'
op|','
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|','
nl|'\n'
name|'last_refreshed'
op|')'
newline|'\n'
dedent|''
name|'usage'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'bw_usage_get'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'start_period'
op|','
name|'mac'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'usage'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
nl|'\n'
DECL|member|security_group_get_by_instance
dedent|''
name|'def'
name|'security_group_get_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_rule_get_by_security_group
dedent|''
name|'def'
name|'security_group_rule_get_by_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'secgroup'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'secgroup'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'rule'
op|')'
newline|'\n'
nl|'\n'
DECL|member|provider_fw_rule_get_all
dedent|''
name|'def'
name|'provider_fw_rule_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
DECL|member|agent_build_get_by_triple
dedent|''
name|'def'
name|'agent_build_get_by_triple'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'agent_build_get_by_triple'
op|'('
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
nl|'\n'
name|'architecture'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_update_or_create
dedent|''
name|'def'
name|'block_device_mapping_update_or_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|','
nl|'\n'
name|'create'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'create'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'create'
name|'is'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_update'
op|'('
name|'context'
op|','
name|'values'
op|'['
string|"'id'"
op|']'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_get_all_by_instance
dedent|''
dedent|''
name|'def'
name|'block_device_mapping_get_all_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdms'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'bdms'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy
dedent|''
name|'def'
name|'block_device_mapping_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'bdms'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance'
op|'='
name|'None'
op|','
name|'volume_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdms'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'bdm'
name|'in'
name|'bdms'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_destroy'
op|'('
name|'context'
op|','
name|'bdm'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'instance'
name|'is'
name|'not'
name|'None'
name|'and'
name|'volume_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_destroy_by_instance_and_volume'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'instance'
name|'is'
name|'not'
name|'None'
name|'and'
name|'device_name'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'block_device_mapping_destroy_by_instance_and_device'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'device_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# NOTE(danms): This shouldn't happen"
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"Invalid block_device_mapping_destroy"'
nl|'\n'
string|'" invocation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_filters
dedent|''
dedent|''
name|'def'
name|'instance_get_all_by_filters'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|','
name|'sort_key'
op|','
nl|'\n'
name|'sort_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|','
name|'sort_dir'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_hung_in_rebooting
dedent|''
name|'def'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'context'
op|','
name|'timeout'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_active_by_window
dedent|''
name|'def'
name|'instance_get_active_by_window'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_active_by_window'
op|'('
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
nl|'\n'
name|'project_id'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_active_by_window_joined
dedent|''
name|'def'
name|'instance_get_active_by_window_joined'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_active_by_window_joined'
op|'('
nl|'\n'
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'project_id'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_info_cache_delete
dedent|''
name|'def'
name|'instance_info_cache_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_info_cache_delete'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_info_cache_update
dedent|''
name|'def'
name|'instance_info_cache_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_info_cache_update'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_type_get
dedent|''
name|'def'
name|'instance_type_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_type_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'context'
op|','
name|'instance_type_id'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_fault_create
dedent|''
name|'def'
name|'instance_fault_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_fault_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|vol_get_usage_by_time
dedent|''
name|'def'
name|'vol_get_usage_by_time'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'start_time'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'vol_get_usage_by_time'
op|'('
name|'context'
op|','
name|'start_time'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|vol_usage_update
dedent|''
name|'def'
name|'vol_usage_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vol_id'
op|','
name|'rd_req'
op|','
name|'rd_bytes'
op|','
name|'wr_req'
op|','
nl|'\n'
name|'wr_bytes'
op|','
name|'instance'
op|','
name|'last_refreshed'
op|'='
name|'None'
op|','
nl|'\n'
name|'update_totals'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'vol_usage_update'
op|'('
name|'context'
op|','
name|'vol_id'
op|','
name|'rd_req'
op|','
name|'rd_bytes'
op|','
name|'wr_req'
op|','
nl|'\n'
name|'wr_bytes'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'last_refreshed'
op|','
nl|'\n'
name|'update_totals'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'HostBinaryNotFound'
op|')'
newline|'\n'
DECL|member|service_get_all_by
name|'def'
name|'service_get_all_by'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'binary'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'any'
op|'('
op|'('
name|'topic'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'all'
op|'('
op|'('
name|'topic'
op|','
name|'host'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'topic'
op|'=='
string|"'compute'"
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
comment|'# FIXME(comstud) Potentially remove this on bump to v2.0'
nl|'\n'
name|'result'
op|'='
op|'['
name|'result'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_by_host_and_topic'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
name|'topic'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'all'
op|'('
op|'('
name|'host'
op|','
name|'binary'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'topic'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|action_event_start
dedent|''
name|'def'
name|'action_event_start'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'evt'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'action_event_start'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'evt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|action_event_finish
dedent|''
name|'def'
name|'action_event_finish'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'evt'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'action_event_finish'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'evt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_create
dedent|''
name|'def'
name|'service_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'svc'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'svc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'ServiceNotFound'
op|')'
newline|'\n'
DECL|member|service_destroy
name|'def'
name|'service_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_create
dedent|''
name|'def'
name|'compute_node_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'compute_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_update
dedent|''
name|'def'
name|'compute_node_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'values'
op|','
name|'prune_stats'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'compute_node_update'
op|'('
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|','
name|'values'
op|','
nl|'\n'
name|'prune_stats'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rpc_common'
op|'.'
name|'client_exceptions'
op|'('
name|'exception'
op|'.'
name|'ServiceNotFound'
op|')'
newline|'\n'
DECL|member|service_update
name|'def'
name|'service_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'service'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'svc'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'service'
op|'['
string|"'id'"
op|']'
op|','
name|'values'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'svc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_get
dedent|''
name|'def'
name|'task_log_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
name|'state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'task_log_get'
op|'('
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'state'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_begin_task
dedent|''
name|'def'
name|'task_log_begin_task'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'task_items'
op|'='
name|'None'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'task_log_begin_task'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'task_name'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
name|'task_items'
op|','
nl|'\n'
name|'message'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_end_task
dedent|''
name|'def'
name|'task_log_end_task'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'errors'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'task_log_end_task'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'task_name'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
name|'errors'
op|','
name|'message'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|notify_usage_exists
dedent|''
name|'def'
name|'notify_usage_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'current_period'
op|'='
name|'False'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|'='
name|'True'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'None'
op|','
name|'extra_usage_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute_utils'
op|'.'
name|'notify_usage_exists'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'current_period'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|','
nl|'\n'
name|'system_metadata'
op|','
name|'extra_usage_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_groups_trigger_handler
dedent|''
name|'def'
name|'security_groups_trigger_handler'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'event'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'trigger_handler'
op|'('
name|'event'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_groups_trigger_members_refresh
dedent|''
name|'def'
name|'security_groups_trigger_members_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'trigger_members_refresh'
op|'('
name|'context'
op|','
name|'group_ids'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
