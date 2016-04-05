begin_unit
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
name|'sqlalchemy'
op|'.'
name|'orm'
name|'import'
name|'joinedload'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
nl|'\n'
nl|'\n'
op|'@'
name|'db_api'
op|'.'
name|'main_context_manager'
op|'.'
name|'writer'
newline|'\n'
DECL|function|_create_rp_in_db
name|'def'
name|'_create_rp_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_rp'
op|'='
name|'models'
op|'.'
name|'ResourceProvider'
op|'('
op|')'
newline|'\n'
name|'db_rp'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'session'
op|'.'
name|'add'
op|'('
name|'db_rp'
op|')'
newline|'\n'
name|'return'
name|'db_rp'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'db_api'
op|'.'
name|'main_context_manager'
op|'.'
name|'reader'
newline|'\n'
DECL|function|_get_rp_by_uuid_from_db
name|'def'
name|'_get_rp_by_uuid_from_db'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'ResourceProvider'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|ResourceProvider
name|'class'
name|'ResourceProvider'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'id'"
name|'in'
name|'self'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'uuid'"
name|'not'
name|'in'
name|'self'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'uuid is required'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'db_rp'
op|'='
name|'self'
op|'.'
name|'_create_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_rp'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_resource_provider'
op|'='
name|'cls'
op|'.'
name|'_get_by_uuid_from_db'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_resource_provider'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_create_in_db
name|'def'
name|'_create_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_create_rp_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'resource_provider'
op|','
name|'db_resource_provider'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'resource_provider'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'resource_provider'
op|','
name|'field'
op|','
name|'db_resource_provider'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'resource_provider'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'resource_provider'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'resource_provider'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_by_uuid_from_db
name|'def'
name|'_get_by_uuid_from_db'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_get_rp_by_uuid_from_db'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_HasAResourceProvider
dedent|''
dedent|''
name|'class'
name|'_HasAResourceProvider'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Code shared between Inventory and Allocation\n\n    Both contain a ResourceProvider.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_make_db
name|'def'
name|'_make_db'
op|'('
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'resource_provider'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'resource_provider'"
op|')'
newline|'\n'
name|'updates'
op|'['
string|"'resource_provider_id'"
op|']'
op|'='
name|'resource_provider'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'NotImplementedError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'resource_provider required'"
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'resource_class'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'resource_class'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'resource_class required'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'['
string|"'resource_class_id'"
op|']'
op|'='
name|'fields'
op|'.'
name|'ResourceClass'
op|'.'
name|'index'
op|'('
nl|'\n'
name|'resource_class'
op|')'
newline|'\n'
name|'return'
name|'updates'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'source'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'target'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'not'
name|'in'
op|'('
string|"'resource_provider'"
op|','
string|"'resource_class'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'target'
op|','
name|'field'
op|','
name|'source'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'resource_class'"
name|'not'
name|'in'
name|'target'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'.'
name|'resource_class'
op|'='
op|'('
nl|'\n'
name|'target'
op|'.'
name|'fields'
op|'['
string|"'resource_class'"
op|']'
op|'.'
name|'from_index'
op|'('
nl|'\n'
name|'source'
op|'['
string|"'resource_class_id'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
string|"'resource_provider'"
name|'not'
name|'in'
name|'target'
name|'and'
nl|'\n'
string|"'resource_provider'"
name|'in'
name|'source'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'.'
name|'resource_provider'
op|'='
name|'ResourceProvider'
op|'('
op|')'
newline|'\n'
name|'ResourceProvider'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'target'
op|'.'
name|'resource_provider'
op|','
nl|'\n'
name|'source'
op|'['
string|"'resource_provider'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'target'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'target'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'target'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'db_api'
op|'.'
name|'main_context_manager'
op|'.'
name|'writer'
newline|'\n'
DECL|function|_create_inventory_in_db
name|'def'
name|'_create_inventory_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_inventory'
op|'='
name|'models'
op|'.'
name|'Inventory'
op|'('
op|')'
newline|'\n'
name|'db_inventory'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'context'
op|'.'
name|'session'
op|'.'
name|'add'
op|'('
name|'db_inventory'
op|')'
newline|'\n'
name|'return'
name|'db_inventory'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'db_api'
op|'.'
name|'main_context_manager'
op|'.'
name|'writer'
newline|'\n'
DECL|function|_update_inventory_in_db
name|'def'
name|'_update_inventory_in_db'
op|'('
name|'context'
op|','
name|'id_'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
nl|'\n'
name|'models'
op|'.'
name|'Inventory'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'id_'
op|')'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|Inventory
name|'class'
name|'Inventory'
op|'('
name|'_HasAResourceProvider'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'resource_provider'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ResourceProvider'"
op|')'
op|','
nl|'\n'
string|"'resource_class'"
op|':'
name|'fields'
op|'.'
name|'ResourceClassField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'total'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'min_unit'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'max_unit'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'step_size'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'allocation_ratio'"
op|':'
name|'fields'
op|'.'
name|'FloatField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'id'"
name|'in'
name|'self'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'_make_db'
op|'('
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
op|')'
newline|'\n'
name|'db_inventory'
op|'='
name|'self'
op|'.'
name|'_create_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_inventory'
op|')'
newline|'\n'
nl|'\n'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'id'"
name|'not'
name|'in'
name|'self'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'save'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'not created'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_create_in_db
name|'def'
name|'_create_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_create_inventory_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_update_in_db
name|'def'
name|'_update_in_db'
op|'('
name|'context'
op|','
name|'id_'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_update_inventory_in_db'
op|'('
name|'context'
op|','
name|'id_'
op|','
name|'updates'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|InventoryList
name|'class'
name|'InventoryList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial Version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Inventory'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'db_api'
op|'.'
name|'main_context_manager'
op|'.'
name|'reader'
newline|'\n'
DECL|member|_get_all_by_resource_provider
name|'def'
name|'_get_all_by_resource_provider'
op|'('
name|'context'
op|','
name|'rp_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'Inventory'
op|')'
op|'.'
name|'options'
op|'('
name|'joinedload'
op|'('
string|"'resource_provider'"
op|')'
op|')'
op|'.'
name|'filter'
op|'('
name|'models'
op|'.'
name|'ResourceProvider'
op|'.'
name|'uuid'
op|'=='
name|'rp_uuid'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all_by_resource_provider_uuid
name|'def'
name|'get_all_by_resource_provider_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'rp_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inventory_list'
op|'='
name|'cls'
op|'.'
name|'_get_all_by_resource_provider'
op|'('
name|'context'
op|','
nl|'\n'
name|'rp_uuid'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Inventory'
op|','
nl|'\n'
name|'db_inventory_list'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
