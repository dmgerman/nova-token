begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nHandles all requests relating to volumes.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'rpc'
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
name|'import'
name|'nova'
op|'.'
name|'policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
DECL|variable|volume_host_opt
name|'volume_host_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'snapshot_same_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Create volume from snapshot at the host where snapshot resides'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opt'
op|'('
name|'volume_host_opt'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'storage_availability_zone'"
op|','
string|"'nova.volume.manager'"
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
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_check_policy
name|'def'
name|'wrap_check_policy'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check policy corresponding to the wrapped methods prior to execution\n\n    This decorator requires the first 3 args of the wrapped function\n    to be (self, context, volume)\n    """'
newline|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'func'
op|')'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'target_obj'
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
name|'check_policy'
op|'('
name|'context'
op|','
name|'func'
op|'.'
name|'__name__'
op|','
name|'target_obj'
op|')'
newline|'\n'
name|'return'
name|'func'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'target_obj'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_policy
dedent|''
name|'def'
name|'check_policy'
op|'('
name|'context'
op|','
name|'action'
op|','
name|'target_obj'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'target'
op|'='
op|'{'
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'target'
op|'.'
name|'update'
op|'('
name|'target_obj'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
name|'_action'
op|'='
string|"'volume:%s'"
op|'%'
name|'action'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'context'
op|','
name|'_action'
op|','
name|'target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the volume manager."""'
newline|'\n'
nl|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'size'
op|','
name|'name'
op|','
name|'description'
op|','
name|'snapshot'
op|'='
name|'None'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'None'
op|','
name|'metadata'
op|'='
name|'None'
op|','
name|'availability_zone'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_policy'
op|'('
name|'context'
op|','
string|"'create'"
op|')'
newline|'\n'
name|'if'
name|'snapshot'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'snapshot'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"available"'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"status must be available"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidSnapshot'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'size'
op|':'
newline|'\n'
indent|'                '
name|'size'
op|'='
name|'snapshot'
op|'['
string|"'volume_size'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'snapshot_id'
op|'='
name|'snapshot'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'snapshot_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'size'
op|','
name|'int'
op|')'
name|'or'
name|'size'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Volume size must be an integer and greater than 0'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'reservations'
op|'='
name|'QUOTAS'
op|'.'
name|'reserve'
op|'('
name|'context'
op|','
name|'volumes'
op|'='
number|'1'
op|','
name|'gigabytes'
op|'='
name|'size'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'OverQuota'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'overs'
op|'='
name|'e'
op|'.'
name|'kwargs'
op|'['
string|"'overs'"
op|']'
newline|'\n'
name|'usages'
op|'='
name|'e'
op|'.'
name|'kwargs'
op|'['
string|"'usages'"
op|']'
newline|'\n'
name|'quotas'
op|'='
name|'e'
op|'.'
name|'kwargs'
op|'['
string|"'quotas'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_consumed
name|'def'
name|'_consumed'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'('
name|'usages'
op|'['
name|'name'
op|']'
op|'['
string|"'reserved'"
op|']'
op|'+'
name|'usages'
op|'['
name|'name'
op|']'
op|'['
string|"'in_use'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'pid'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'if'
string|"'gigabytes'"
name|'in'
name|'overs'
op|':'
newline|'\n'
indent|'                '
name|'consumed'
op|'='
name|'_consumed'
op|'('
string|"'gigabytes'"
op|')'
newline|'\n'
name|'quota'
op|'='
name|'quotas'
op|'['
string|"'gigabytes'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Quota exceeded for %(pid)s, tried to create "'
nl|'\n'
string|'"%(size)sG volume (%(consumed)dG of %(quota)dG "'
nl|'\n'
string|'"already consumed)"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'VolumeSizeTooLarge'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'volumes'"
name|'in'
name|'overs'
op|':'
newline|'\n'
indent|'                '
name|'consumed'
op|'='
name|'_consumed'
op|'('
string|"'volumes'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Quota exceeded for %(pid)s, tried to create "'
nl|'\n'
string|'"volume (%(consumed)d volumes already consumed)"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'VolumeLimitExceeded'
op|'('
name|'allowed'
op|'='
name|'quotas'
op|'['
string|"'volumes'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'availability_zone'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'availability_zone'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'volume_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'volume_type_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'volume_type_id'
op|'='
name|'volume_type'
op|'.'
name|'get'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'options'
op|'='
op|'{'
nl|'\n'
string|"'size'"
op|':'
name|'size'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'snapshot_id'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'status'"
op|':'
string|'"creating"'
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|'"detached"'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'volume_type_id'"
op|':'
name|'volume_type_id'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'metadata'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|','
name|'options'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_cast_create_volume'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'snapshot_id'
op|','
name|'reservations'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|_cast_create_volume
dedent|''
name|'def'
name|'_cast_create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'snapshot_id'
op|','
name|'reservations'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# NOTE(Rongze Zhu): It is a simple solution for bug 1008866'
nl|'\n'
comment|'# If snapshot_id is set, make the call create volume directly to'
nl|'\n'
comment|'# the volume host where the snapshot resides instead of passing it'
nl|'\n'
comment|'# through the scheduer. So snapshot can be copy to new volume.'
nl|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'snapshot_id'
name|'and'
name|'FLAGS'
op|'.'
name|'snapshot_same_host'
op|':'
newline|'\n'
indent|'            '
name|'snapshot_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'src_volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_ref'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
nl|'\n'
name|'src_volume_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume_id'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'snapshot_id'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'scheduler_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"topic"'
op|':'
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
nl|'\n'
string|'"volume_id"'
op|':'
name|'volume_id'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'snapshot_id'
op|','
nl|'\n'
string|'"reservations"'
op|':'
name|'reservations'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'volume'
op|'['
string|"'host'"
op|']'
op|':'
newline|'\n'
comment|'# NOTE(vish): scheduling failed, so delete it'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
name|'not'
name|'in'
op|'['
string|'"available"'
op|','
string|'"error"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Volume status must be available or error"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'snapshots'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get_all_for_volume'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'snapshots'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Volume still has %d dependent snapshots"'
op|')'
op|'%'
name|'len'
op|'('
name|'snapshots'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
op|'{'
string|"'status'"
op|':'
string|"'deleting'"
op|','
nl|'\n'
string|"'terminated_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"delete_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'dict'
op|'('
name|'rv'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
name|'check_policy'
op|'('
name|'context'
op|','
string|"'get'"
op|','
name|'volume'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'search_opts'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_policy'
op|'('
name|'context'
op|','
string|"'get_all'"
op|')'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'volumes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'volumes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_all_by_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'search_opts'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Searching by: %s"'
op|')'
op|'%'
name|'str'
op|'('
name|'search_opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_check_metadata_match
name|'def'
name|'_check_metadata_match'
op|'('
name|'volume'
op|','
name|'searchdict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'volume_metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'volume_metadata'
op|'['
name|'i'
op|'['
string|"'key'"
op|']'
op|']'
op|'='
name|'i'
op|'['
string|"'value'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'searchdict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
op|'('
name|'k'
name|'not'
name|'in'
name|'volume_metadata'
op|'.'
name|'keys'
op|'('
op|')'
name|'or'
nl|'\n'
name|'volume_metadata'
op|'['
name|'k'
op|']'
op|'!='
name|'v'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|'# search_option to filter_name mapping.'
nl|'\n'
dedent|''
name|'filter_mapping'
op|'='
op|'{'
string|"'metadata'"
op|':'
name|'_check_metadata_match'
op|'}'
newline|'\n'
nl|'\n'
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
comment|'# go over all filters in the list'
nl|'\n'
indent|'                '
name|'for'
name|'opt'
op|','
name|'values'
name|'in'
name|'search_opts'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'filter_func'
op|'='
name|'filter_mapping'
op|'['
name|'opt'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|'# no such filter - ignore it, go to next filter'
nl|'\n'
indent|'                        '
name|'continue'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'filter_func'
op|'('
name|'volume'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'result'
op|'.'
name|'append'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'volumes'
op|'='
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'volumes'
newline|'\n'
nl|'\n'
DECL|member|get_snapshot
dedent|''
name|'def'
name|'get_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_policy'
op|'('
name|'context'
op|','
string|"'get_snapshot'"
op|')'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'rv'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_snapshots
dedent|''
name|'def'
name|'get_all_snapshots'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_policy'
op|'('
name|'context'
op|','
string|"'get_all_snapshots'"
op|')'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get_all_by_project'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|check_attach
name|'def'
name|'check_attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"status must be available"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|'"attached"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already attached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|check_detach
name|'def'
name|'check_detach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"already detached"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|reserve_volume
name|'def'
name|'reserve_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|'"status"'
op|':'
string|'"attaching"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|unreserve_volume
name|'def'
name|'unreserve_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|'"attaching"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|'"status"'
op|':'
string|'"available"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'instance_uuid'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'queue'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"attach_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"instance_uuid"'
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|'"mountpoint"'
op|':'
name|'mountpoint'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|detach
name|'def'
name|'detach'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'queue'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"detach_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|initialize_connection
name|'def'
name|'initialize_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'queue'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"initialize_connection"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"connector"'
op|':'
name|'connector'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|terminate_connection
name|'def'
name|'terminate_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'unreserve_volume'
op|'('
name|'context'
op|','
name|'volume'
op|')'
newline|'\n'
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'queue'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"terminate_connection"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"connector"'
op|':'
name|'connector'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_snapshot
dedent|''
name|'def'
name|'_create_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'name'
op|','
name|'description'
op|','
nl|'\n'
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_policy'
op|'('
name|'context'
op|','
string|"'create_snapshot'"
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
op|'('
name|'not'
name|'force'
op|')'
name|'and'
op|'('
name|'volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"available"'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"must be available"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'options'
op|'='
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'status'"
op|':'
string|'"creating"'
op|','
nl|'\n'
string|"'progress'"
op|':'
string|"'0%'"
op|','
nl|'\n'
string|"'volume_size'"
op|':'
name|'volume'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'description'
op|'}'
newline|'\n'
nl|'\n'
name|'snapshot'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_create'
op|'('
name|'context'
op|','
name|'options'
op|')'
newline|'\n'
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_snapshot"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'snapshot'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'snapshot'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
name|'context'
op|','
name|'volume'
op|','
name|'name'
op|','
name|'description'
op|','
nl|'\n'
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot_force
dedent|''
name|'def'
name|'create_snapshot_force'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
name|'context'
op|','
name|'volume'
op|','
name|'name'
op|','
name|'description'
op|','
nl|'\n'
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|delete_snapshot
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'snapshot'
op|'['
string|"'status'"
op|']'
name|'not'
name|'in'
op|'['
string|'"available"'
op|','
string|'"error"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Volume Snapshot status must be available or error"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
name|'snapshot'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'deleting'"
op|'}'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
op|')'
newline|'\n'
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"delete_snapshot"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"snapshot_id"'
op|':'
name|'snapshot'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|get_volume_metadata
name|'def'
name|'get_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get all metadata associated with a volume."""'
newline|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_metadata_get'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'rv'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|delete_volume_metadata
name|'def'
name|'delete_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the given metadata item from a volume."""'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_metadata_delete'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wrap_check_policy'
newline|'\n'
DECL|member|update_volume_metadata
name|'def'
name|'update_volume_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'metadata'
op|','
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates or creates volume metadata.\n\n        If delete is True, metadata items that are not specified in the\n        `metadata` argument will be deleted.\n\n        """'
newline|'\n'
name|'if'
name|'delete'
op|':'
newline|'\n'
indent|'            '
name|'_metadata'
op|'='
name|'metadata'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'_metadata'
op|'='
name|'self'
op|'.'
name|'get_volume_metadata'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'_metadata'
op|'.'
name|'update'
op|'('
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_metadata_update'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
name|'_metadata'
op|','
name|'True'
op|')'
newline|'\n'
name|'return'
name|'_metadata'
newline|'\n'
nl|'\n'
DECL|member|get_volume_metadata_value
dedent|''
name|'def'
name|'get_volume_metadata_value'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get value of particular metadata key."""'
newline|'\n'
name|'metadata'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
newline|'\n'
name|'if'
name|'metadata'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'i'
name|'in'
name|'volume'
op|'['
string|"'volume_metadata'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'i'
op|'['
string|"'key'"
op|']'
op|'=='
name|'key'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'i'
op|'['
string|"'value'"
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
