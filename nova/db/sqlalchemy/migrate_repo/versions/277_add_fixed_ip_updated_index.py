begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
DECL|variable|INDEX_COLUMNS
name|'INDEX_COLUMNS'
op|'='
op|'['
string|"'deleted'"
op|','
string|"'allocated'"
op|','
string|"'updated_at'"
op|']'
newline|'\n'
DECL|variable|INDEX_NAME
name|'INDEX_NAME'
op|'='
string|"'fixed_ips_%s_idx'"
op|'%'
op|'('
string|"'_'"
op|'.'
name|'join'
op|'('
name|'INDEX_COLUMNS'
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_table_index
name|'def'
name|'_get_table_index'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'for'
name|'idx'
name|'in'
name|'table'
op|'.'
name|'indexes'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'idx'
op|'.'
name|'columns'
op|'.'
name|'keys'
op|'('
op|')'
op|'=='
name|'INDEX_COLUMNS'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'idx'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'meta'
op|','
name|'table'
op|','
name|'idx'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
dedent|''
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|','
name|'table'
op|','
name|'index'
op|'='
name|'_get_table_index'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'if'
name|'index'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Skipped adding %s because an equivalent index'"
nl|'\n'
string|"' already exists.'"
op|')'
op|','
name|'INDEX_NAME'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'columns'
op|'='
op|'['
name|'getattr'
op|'('
name|'table'
op|'.'
name|'c'
op|','
name|'col_name'
op|')'
name|'for'
name|'col_name'
name|'in'
name|'INDEX_COLUMNS'
op|']'
newline|'\n'
name|'index'
op|'='
name|'Index'
op|'('
name|'INDEX_NAME'
op|','
op|'*'
name|'columns'
op|')'
newline|'\n'
name|'index'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
