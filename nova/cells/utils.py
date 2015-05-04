begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nCells Utility Methods\n"""'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
nl|'\n'
nl|'\n'
comment|"# Separator used between cell names for the 'full cell name' and routing"
nl|'\n'
comment|'# path'
nl|'\n'
DECL|variable|PATH_CELL_SEP
name|'PATH_CELL_SEP'
op|'='
string|"'!'"
newline|'\n'
comment|"# Flag prepended to a cell name to indicate data shouldn't be synced during"
nl|'\n'
comment|'# an instance save.  There are no illegal chars in a cell name so using the'
nl|'\n'
comment|'# meaningful PATH_CELL_SEP in an invalid way will need to suffice.'
nl|'\n'
DECL|variable|BLOCK_SYNC_FLAG
name|'BLOCK_SYNC_FLAG'
op|'='
string|"'!!'"
newline|'\n'
comment|'# Separator used between cell name and item'
nl|'\n'
DECL|variable|_CELL_ITEM_SEP
name|'_CELL_ITEM_SEP'
op|'='
string|"'@'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProxyObjectSerializer
name|'class'
name|'ProxyObjectSerializer'
op|'('
name|'obj_base'
op|'.'
name|'NovaObjectSerializer'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ProxyObjectSerializer'
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
name|'serializer'
op|'='
name|'super'
op|'('
name|'ProxyObjectSerializer'
op|','
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_process_object
dedent|''
name|'def'
name|'_process_object'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objprim'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_CellProxy'
op|'.'
name|'obj_from_primitive'
op|'('
name|'self'
op|'.'
name|'serializer'
op|','
name|'objprim'
op|','
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_CellProxy
dedent|''
dedent|''
name|'class'
name|'_CellProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'cell_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_obj'
op|'='
name|'obj'
newline|'\n'
name|'self'
op|'.'
name|'_cell_path'
op|'='
name|'cell_path'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|id
name|'def'
name|'id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cell_with_item'
op|'('
name|'self'
op|'.'
name|'_cell_path'
op|','
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|host
name|'def'
name|'host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cell_with_item'
op|'('
name|'self'
op|'.'
name|'_cell_path'
op|','
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
op|'=='
string|"'id'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'=='
string|"'host'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'host'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_obj'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_to_primitive
dedent|''
name|'def'
name|'obj_to_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_p'
op|'='
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'obj_p'
op|'['
string|"'cell_proxy.class_name'"
op|']'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'obj_p'
op|'['
string|"'cell_proxy.cell_path'"
op|']'
op|'='
name|'self'
op|'.'
name|'_cell_path'
newline|'\n'
name|'return'
name|'obj_p'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_primitive
name|'def'
name|'obj_from_primitive'
op|'('
name|'cls'
op|','
name|'serializer'
op|','
name|'primitive'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj_primitive'
op|'='
name|'primitive'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'cell_path'
op|'='
name|'obj_primitive'
op|'.'
name|'pop'
op|'('
string|"'cell_proxy.cell_path'"
op|','
name|'None'
op|')'
newline|'\n'
name|'klass_name'
op|'='
name|'obj_primitive'
op|'.'
name|'pop'
op|'('
string|"'cell_proxy.class_name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'obj'
op|'='
name|'serializer'
op|'.'
name|'_process_object'
op|'('
name|'context'
op|','
name|'obj_primitive'
op|')'
newline|'\n'
name|'if'
name|'klass_name'
name|'is'
name|'not'
name|'None'
name|'and'
name|'cell_path'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'klass'
op|'='
name|'getattr'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
name|'klass_name'
op|')'
newline|'\n'
name|'return'
name|'klass'
op|'('
name|'obj'
op|','
name|'cell_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
comment|'# dict-ish syntax sugar'
nl|'\n'
DECL|member|_iteritems
dedent|''
dedent|''
name|'def'
name|'_iteritems'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""For backwards-compatibility with dict-based objects.\n\n        NOTE(sbauza): May be removed in the future.\n        """'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'obj_fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'name'
op|')'
name|'or'
nl|'\n'
name|'name'
name|'in'
name|'self'
op|'.'
name|'_obj'
op|'.'
name|'obj_extra_fields'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'name'
op|'=='
string|"'id'"
op|':'
newline|'\n'
indent|'                    '
name|'yield'
name|'name'
op|','
name|'self'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'host'"
op|':'
newline|'\n'
indent|'                    '
name|'yield'
name|'name'
op|','
name|'self'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'yield'
name|'name'
op|','
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_obj'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'_iteritems'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'iteritems'
op|'='
name|'_iteritems'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_obj'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeNodeProxy
dedent|''
dedent|''
name|'class'
name|'ComputeNodeProxy'
op|'('
name|'_CellProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceProxy
dedent|''
name|'class'
name|'ServiceProxy'
op|'('
name|'_CellProxy'
op|')'
op|':'
newline|'\n'
DECL|member|__getattr__
indent|'    '
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
op|'=='
string|"'compute_node'"
op|':'
newline|'\n'
comment|'# NOTE(sbauza): As the Service object is still having a nested'
nl|'\n'
comment|"# ComputeNode object that consumers of this Proxy don't use, we can"
nl|'\n'
comment|"# safely remove it from what's returned"
nl|'\n'
indent|'            '
name|'raise'
name|'AttributeError'
newline|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_obj'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instances_to_sync
dedent|''
dedent|''
name|'def'
name|'get_instances_to_sync'
op|'('
name|'context'
op|','
name|'updated_since'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'True'
op|','
name|'shuffle'
op|'='
name|'False'
op|','
name|'uuids_only'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a generator that will return a list of active and\n    deleted instances to sync with parent cells.  The list may\n    optionally be shuffled for periodic updates so that multiple\n    cells services aren\'t self-healing the same instances in nearly\n    lockstep.\n    """'
newline|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'updated_since'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'changes-since'"
op|']'
op|'='
name|'updated_since'
newline|'\n'
dedent|''
name|'if'
name|'project_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'deleted'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'['
string|"'deleted'"
op|']'
op|'='
name|'False'
newline|'\n'
comment|'# Active instances first.'
nl|'\n'
dedent|''
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|','
string|"'deleted'"
op|','
string|"'asc'"
op|')'
newline|'\n'
name|'if'
name|'shuffle'
op|':'
newline|'\n'
indent|'        '
name|'random'
op|'.'
name|'shuffle'
op|'('
name|'instances'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuids_only'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cell_with_item
dedent|''
dedent|''
dedent|''
name|'def'
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Turn cell_name and item into <cell_name>@<item>."""'
newline|'\n'
name|'if'
name|'cell_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'item'
newline|'\n'
dedent|''
name|'return'
name|'cell_name'
op|'+'
name|'_CELL_ITEM_SEP'
op|'+'
name|'str'
op|'('
name|'item'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|split_cell_and_item
dedent|''
name|'def'
name|'split_cell_and_item'
op|'('
name|'cell_and_item'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Split a combined cell@item and return them."""'
newline|'\n'
name|'result'
op|'='
name|'cell_and_item'
op|'.'
name|'rsplit'
op|'('
name|'_CELL_ITEM_SEP'
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'result'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'None'
op|','
name|'cell_and_item'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_cell_to_compute_node
dedent|''
dedent|''
name|'def'
name|'add_cell_to_compute_node'
op|'('
name|'compute_node'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fix compute_node attributes that should be unique.  Allows\n    API cell to query the \'id\' by cell@id.\n    """'
newline|'\n'
comment|'# NOTE(sbauza): As compute_node is a ComputeNode object, we need to wrap it'
nl|'\n'
comment|'# for adding the cell_path information'
nl|'\n'
name|'compute_proxy'
op|'='
name|'ComputeNodeProxy'
op|'('
name|'compute_node'
op|','
name|'cell_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
name|'compute_proxy'
op|'.'
name|'service'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ServiceNotFound'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'service'
op|','
name|'objects'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute_proxy'
op|'.'
name|'service'
op|'='
name|'ServiceProxy'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'compute_proxy'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_cell_to_service
dedent|''
name|'def'
name|'add_cell_to_service'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fix service attributes that should be unique.  Allows\n    API cell to query the \'id\' or \'host\' by cell@id/host.\n    """'
newline|'\n'
comment|'# NOTE(sbauza): As service is a Service object, we need to wrap it'
nl|'\n'
comment|'# for adding the cell_path information'
nl|'\n'
name|'service_proxy'
op|'='
name|'ServiceProxy'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
newline|'\n'
name|'return'
name|'service_proxy'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_cell_to_task_log
dedent|''
name|'def'
name|'add_cell_to_task_log'
op|'('
name|'task_log'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fix task_log attributes that should be unique.  In particular,\n    the \'id\' and \'host\' fields should be prepended with cell name.\n    """'
newline|'\n'
name|'task_log'
op|'['
string|"'id'"
op|']'
op|'='
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'task_log'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'task_log'
op|'['
string|"'host'"
op|']'
op|'='
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'task_log'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
