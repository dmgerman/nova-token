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
name|'sqlalchemy'
name|'import'
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Text'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|BASE_TABLE_NAME
name|'BASE_TABLE_NAME'
op|'='
string|"'instance_extra'"
newline|'\n'
DECL|variable|NEW_COLUMN_NAME
name|'NEW_COLUMN_NAME'
op|'='
string|"'flavor'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
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
nl|'\n'
name|'for'
name|'prefix'
name|'in'
op|'('
string|"''"
op|','
string|"'shadow_'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'Table'
op|'('
name|'prefix'
op|'+'
name|'BASE_TABLE_NAME'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'new_column'
op|'='
name|'Column'
op|'('
name|'NEW_COLUMN_NAME'
op|','
name|'Text'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'table'
op|'.'
name|'c'
op|','
name|'NEW_COLUMN_NAME'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'.'
name|'create_column'
op|'('
name|'new_column'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
