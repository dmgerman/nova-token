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
string|'"""Handles database requests from other nova services"""'
newline|'\n'
nl|'\n'
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
string|"'host'"
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
string|'"""Mission: TBD"""'
newline|'\n'
nl|'\n'
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.1'"
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
nl|'\n'
DECL|member|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'updates'
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
DECL|member|migration_update
dedent|''
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
dedent|''
dedent|''
endmarker|''
end_unit
