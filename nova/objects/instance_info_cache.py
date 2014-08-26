begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'opts'
name|'as'
name|'cells_opts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'rpcapi'
name|'as'
name|'cells_rpcapi'
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
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
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
DECL|class|InstanceInfoCache
name|'class'
name|'InstanceInfoCache'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Converted network_info to store the model.'
nl|'\n'
comment|'# Version 1.2: Added new() and update_cells kwarg to save().'
nl|'\n'
comment|'# Version 1.3: Added delete()'
nl|'\n'
comment|'# Version 1.4: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.5: Actually set the deleted, created_at, updated_at, and'
nl|'\n'
comment|'#              deleted_at attributes'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.5'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'network_info'"
op|':'
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'NetworkModel'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'info_cache'
op|','
name|'db_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'info_cache'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'info_cache'
op|'['
name|'field'
op|']'
op|'='
name|'db_obj'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'info_cache'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'info_cache'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'return'
name|'info_cache'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|new
name|'def'
name|'new'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an InfoCache object that can be used to create the DB\n        entry for the first time.\n\n        When save()ing this object, the info_cache_update() DB call\n        will properly handle creating it if it doesn\'t exist already.\n        """'
newline|'\n'
name|'info_cache'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'info_cache'
op|'.'
name|'instance_uuid'
op|'='
name|'instance_uuid'
newline|'\n'
name|'info_cache'
op|'.'
name|'network_info'
op|'='
name|'None'
newline|'\n'
name|'info_cache'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
comment|'# Leave the fields dirty'
nl|'\n'
name|'return'
name|'info_cache'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_obj'
op|'='
name|'db'
op|'.'
name|'instance_info_cache_get'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_obj'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInfoCacheNotFound'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_info_cache_cells_update
name|'def'
name|'_info_cache_cells_update'
op|'('
name|'ctxt'
op|','
name|'info_cache'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cell_type'
op|'='
name|'cells_opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
newline|'\n'
name|'if'
name|'cell_type'
op|'!='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'cells_api'
op|'='
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cells_api'
op|'.'
name|'instance_info_cache_update_at_top'
op|'('
name|'ctxt'
op|','
name|'info_cache'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to notify cells of instance info "'
nl|'\n'
string|'"cache update"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'update_cells'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'network_info'"
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'nw_info_json'
op|'='
name|'self'
op|'.'
name|'fields'
op|'['
string|"'network_info'"
op|']'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'self'
op|','
string|"'network_info'"
op|','
name|'self'
op|'.'
name|'network_info'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'db'
op|'.'
name|'instance_info_cache_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
name|'nw_info_json'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'update_cells'
name|'and'
name|'rv'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_info_cache_cells_update'
op|'('
name|'context'
op|','
name|'rv'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'instance_info_cache_delete'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|refresh
name|'def'
name|'refresh'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'get_by_instance_uuid'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'current'
op|'.'
name|'_context'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'field'
op|')'
name|'and'
name|'self'
op|'['
name|'field'
op|']'
op|'!='
name|'current'
op|'['
name|'field'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'['
name|'field'
op|']'
op|'='
name|'current'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
