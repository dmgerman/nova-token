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
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
comment|'# Separator used between cell name and item'
nl|'\n'
DECL|variable|_CELL_ITEM_SEP
name|'_CELL_ITEM_SEP'
op|'='
string|"'@'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instances_to_sync
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
DECL|function|_add_cell_to_service
dedent|''
dedent|''
name|'def'
name|'_add_cell_to_service'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'service'
op|'['
string|"'id'"
op|']'
op|'='
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'service'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'service'
op|'['
string|"'host'"
op|']'
op|'='
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_cell_to_compute_node
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
name|'compute_node'
op|'['
string|"'id'"
op|']'
op|'='
name|'cell_with_item'
op|'('
name|'cell_name'
op|','
name|'compute_node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# Might have a 'service' backref.  But if is_primitive() was used"
nl|'\n'
comment|'# on this and it recursed too deep, \'service\' may be "?".'
nl|'\n'
name|'service'
op|'='
name|'compute_node'
op|'.'
name|'get'
op|'('
string|"'service'"
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'service'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_add_cell_to_service'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_cell_to_service
dedent|''
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
name|'_add_cell_to_service'
op|'('
name|'service'
op|','
name|'cell_name'
op|')'
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
