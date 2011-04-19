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
name|'datetime'
newline|'\n'
nl|'\n'
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
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
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
string|"'nova.volume'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'quota'
op|'.'
name|'allowed_volumes'
op|'('
name|'context'
op|','
number|'1'
op|','
name|'size'
op|')'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'pid'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Quota exceeeded for %(pid)s, tried to create"'
nl|'\n'
string|'" %(size)sG volume"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'quota'
op|'.'
name|'QuotaError'
op|'('
name|'_'
op|'('
string|'"Volume quota exceeded. You cannot "'
nl|'\n'
string|'"create a volume of size %sG"'
op|')'
op|'%'
name|'size'
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
string|"'availability_zone'"
op|':'
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
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
name|'volume'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
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
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
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
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Volume status must be available"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
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
name|'self'
op|'.'
name|'db'
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
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'fields'
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
name|'volume_id'
op|','
name|'fields'
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
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'volume_get_all'
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
name|'volume_get_all_by_project'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
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
DECL|member|check_attach
dedent|''
name|'def'
name|'check_attach'
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
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
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
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Volume status must be available"'
op|')'
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
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Volume is already attached"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_detach
dedent|''
dedent|''
name|'def'
name|'check_detach'
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
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
comment|'# TODO(vish): abstract status checking?'
nl|'\n'
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
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Volume is already detached"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_compute
dedent|''
dedent|''
name|'def'
name|'remove_from_compute'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove volume from specified compute host."""'
newline|'\n'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"remove_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|"'volume_id'"
op|':'
name|'volume_id'
op|'}'
op|'}'
op|')'
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
name|'volume_id'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
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
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Volume status must be available"'
op|')'
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
name|'volume_id'
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
string|'"create_snapshot"'
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
DECL|member|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
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
name|'snapshot'
op|'='
name|'self'
op|'.'
name|'get_snapshot'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'if'
name|'snapshot'
op|'['
string|"'status'"
op|']'
op|'!='
string|'"available"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Snapshot status must be available"'
op|')'
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
name|'snapshot_id'
op|','
op|'{'
string|"'status'"
op|':'
string|"'deleting'"
op|'}'
op|')'
newline|'\n'
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
string|'"delete_snapshot"'
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
string|'"snapshot_id"'
op|':'
name|'snapshot_id'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
