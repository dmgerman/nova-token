begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 Boris Pavlovic (boris@pavlovic.me).'
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
name|'from'
name|'migrate'
op|'.'
name|'changeset'
name|'import'
name|'UniqueConstraint'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'engine'
name|'import'
name|'reflection'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'compiler'
name|'import'
name|'compiles'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Table'
op|','
name|'Column'
op|','
name|'Index'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'sql'
op|'.'
name|'expression'
name|'import'
name|'UpdateBase'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'types'
name|'import'
name|'NullType'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InsertFromSelect
name|'class'
name|'InsertFromSelect'
op|'('
name|'UpdateBase'
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
name|'table'
op|','
name|'select'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'table'
op|'='
name|'table'
newline|'\n'
name|'self'
op|'.'
name|'select'
op|'='
name|'select'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'compiles'
op|'('
name|'InsertFromSelect'
op|')'
newline|'\n'
DECL|function|visit_insert_from_select
name|'def'
name|'visit_insert_from_select'
op|'('
name|'element'
op|','
name|'compiler'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"INSERT INTO %s %s"'
op|'%'
op|'('
nl|'\n'
name|'compiler'
op|'.'
name|'process'
op|'('
name|'element'
op|'.'
name|'table'
op|','
name|'asfrom'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'compiler'
op|'.'
name|'process'
op|'('
name|'element'
op|'.'
name|'select'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_drop_unique_constraint_in_sqlite
dedent|''
name|'def'
name|'_drop_unique_constraint_in_sqlite'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'uc_name'
op|','
nl|'\n'
op|'**'
name|'col_name_col_instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'insp'
op|'='
name|'reflection'
op|'.'
name|'Inspector'
op|'.'
name|'from_engine'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'columns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'column'
name|'in'
name|'table'
op|'.'
name|'columns'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'column'
op|'.'
name|'type'
op|','
name|'NullType'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'new_column'
op|'='
name|'col_name_col_instance'
op|'.'
name|'get'
op|'('
name|'column'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Please specify column %s in col_name_col_instance "'
nl|'\n'
string|'"param. It is required because column has unsupported "'
nl|'\n'
string|'"type by sqlite)."'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|'%'
name|'column'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'new_column'
op|','
name|'Column'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"col_name_col_instance param has wrong type of "'
nl|'\n'
string|'"column instance for column %s It should be instance "'
nl|'\n'
string|'"of sqlalchemy.Column."'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|'%'
name|'column'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'columns'
op|'.'
name|'append'
op|'('
name|'new_column'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'columns'
op|'.'
name|'append'
op|'('
name|'column'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'constraints'
op|'='
op|'['
name|'constraint'
name|'for'
name|'constraint'
name|'in'
name|'table'
op|'.'
name|'constraints'
nl|'\n'
name|'if'
name|'not'
name|'constraint'
op|'.'
name|'name'
op|'=='
name|'uc_name'
op|']'
newline|'\n'
nl|'\n'
name|'new_table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|'+'
string|'"__tmp__"'
op|','
name|'meta'
op|','
op|'*'
op|'('
name|'columns'
op|'+'
name|'constraints'
op|')'
op|')'
newline|'\n'
name|'new_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'indexes'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'insp'
op|'.'
name|'get_indexes'
op|'('
name|'table_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'column_names'
op|'='
op|'['
name|'new_table'
op|'.'
name|'c'
op|'['
name|'c'
op|']'
name|'for'
name|'c'
name|'in'
name|'index'
op|'['
string|"'column_names'"
op|']'
op|']'
newline|'\n'
name|'indexes'
op|'.'
name|'append'
op|'('
name|'Index'
op|'('
name|'index'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
op|'*'
name|'column_names'
op|','
nl|'\n'
name|'unique'
op|'='
name|'index'
op|'['
string|'"unique"'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ins'
op|'='
name|'InsertFromSelect'
op|'('
name|'new_table'
op|','
name|'table'
op|'.'
name|'select'
op|'('
op|')'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'ins'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
op|'['
name|'index'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
name|'for'
name|'index'
name|'in'
name|'indexes'
op|']'
newline|'\n'
name|'new_table'
op|'.'
name|'rename'
op|'('
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drop_unique_constraint
dedent|''
name|'def'
name|'drop_unique_constraint'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'uc_name'
op|','
op|'*'
name|'columns'
op|','
nl|'\n'
op|'**'
name|'col_name_col_instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This method drops UC from table and works for mysql, postgresql and sqlite.\n    In mysql and postgresql we are able to use "alter table" constuction. In\n    sqlite is only one way to drop UC:\n        1) Create new table with same columns, indexes and constraints\n           (except one that we want to drop).\n        2) Copy data from old table to new.\n        3) Drop old table.\n        4) Rename new table to the name of old table.\n\n    :param migrate_engine: sqlalchemy engine\n    :oaram table_name:     name of table that contains uniq constarint.\n    :param uc_name:        name of uniq constraint that will be dropped.\n    :param columns:        columns that are in uniq constarint.\n    :param col_name_col_instance:   constains pair column_name=column_instance.\n                            column_instance is instance of Column. These params\n                            are required only for columns that have unsupported\n                            types by sqlite. For example BigInteger.\n    """'
newline|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
name|'in'
op|'['
string|'"mysql"'
op|','
string|'"postgresql"'
op|']'
op|':'
newline|'\n'
indent|'        '
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
name|'t'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'uc'
op|'='
name|'UniqueConstraint'
op|'('
op|'*'
name|'fields'
op|','
name|'table'
op|'='
name|'t'
op|','
name|'name'
op|'='
name|'uc_name'
op|')'
newline|'\n'
name|'uc'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'_drop_unique_constraint_in_sqlite'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|','
name|'uc_name'
op|','
nl|'\n'
op|'**'
name|'col_name_col_instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
