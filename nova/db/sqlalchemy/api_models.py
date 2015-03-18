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
nl|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'declarative'
name|'import'
name|'declarative_base'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'ForeignKey'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'schema'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Text'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_NovaAPIBase
name|'class'
name|'_NovaAPIBase'
op|'('
name|'models'
op|'.'
name|'ModelBase'
op|','
name|'models'
op|'.'
name|'TimestampMixin'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|API_BASE
dedent|''
name|'API_BASE'
op|'='
name|'declarative_base'
op|'('
name|'cls'
op|'='
name|'_NovaAPIBase'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellMapping
name|'class'
name|'CellMapping'
op|'('
name|'API_BASE'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Contains information on communicating with a cell"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'cell_mappings'"
newline|'\n'
DECL|variable|__table_args__
name|'__table_args__'
op|'='
op|'('
name|'Index'
op|'('
string|"'uuid_idx'"
op|','
string|"'uuid'"
op|')'
op|','
nl|'\n'
name|'schema'
op|'.'
name|'UniqueConstraint'
op|'('
string|"'uuid'"
op|','
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'uniq_cell_mappings0uuid'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|uuid
name|'uuid'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'36'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|transport_url
name|'transport_url'
op|'='
name|'Column'
op|'('
name|'Text'
op|'('
op|')'
op|')'
newline|'\n'
DECL|variable|database_connection
name|'database_connection'
op|'='
name|'Column'
op|'('
name|'Text'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMapping
dedent|''
name|'class'
name|'InstanceMapping'
op|'('
name|'API_BASE'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Contains the mapping of an instance to which cell it is in"""'
newline|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'instance_mappings'"
newline|'\n'
DECL|variable|__table_args__
name|'__table_args__'
op|'='
op|'('
name|'Index'
op|'('
string|"'project_id_idx'"
op|','
string|"'project_id'"
op|')'
op|','
nl|'\n'
name|'Index'
op|'('
string|"'instance_uuid_idx'"
op|','
string|"'instance_uuid'"
op|')'
op|','
nl|'\n'
name|'schema'
op|'.'
name|'UniqueConstraint'
op|'('
string|"'instance_uuid'"
op|','
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'uniq_instance_mappings0instance_uuid'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'36'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|cell_id
name|'cell_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'cell_mappings.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit