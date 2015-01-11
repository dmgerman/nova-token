begin_unit
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
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
name|'as'
name|'oslodbutils'
newline|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Integer'
op|','
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Table'
op|','
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'NoSuchTableError'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'sql'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'types'
name|'import'
name|'UserDefinedType'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SA_VERSION
name|'SA_VERSION'
op|'='
name|'tuple'
op|'('
name|'map'
op|'('
name|'int'
op|','
name|'sqlalchemy'
op|'.'
name|'__version__'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CustomType
name|'class'
name|'CustomType'
op|'('
name|'UserDefinedType'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Dummy column type for testing unsupported types."""'
newline|'\n'
DECL|member|get_col_spec
name|'def'
name|'get_col_spec'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"CustomType"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestMigrationUtilsSQLite
dedent|''
dedent|''
name|'class'
name|'TestMigrationUtilsSQLite'
op|'('
name|'test_base'
op|'.'
name|'DbTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for testing utils that are used in db migrations."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestMigrationUtilsSQLite'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_from_select
dedent|''
name|'def'
name|'test_delete_from_select'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|'"__test_deletefromselect_table__"'
newline|'\n'
name|'uuidstrs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'unused'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'uuidstrs'
op|'.'
name|'append'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'test_table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
nl|'\n'
name|'nullable'
op|'='
name|'False'
op|','
name|'autoincrement'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'uuid'"
op|','
name|'String'
op|'('
number|'36'
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
name|'test_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
comment|'# Add 10 rows to table'
nl|'\n'
name|'for'
name|'uuidstr'
name|'in'
name|'uuidstrs'
op|':'
newline|'\n'
indent|'            '
name|'ins_stmt'
op|'='
name|'test_table'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'values'
op|'('
name|'uuid'
op|'='
name|'uuidstr'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'execute'
op|'('
name|'ins_stmt'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete 4 rows in one chunk'
nl|'\n'
dedent|''
name|'column'
op|'='
name|'test_table'
op|'.'
name|'c'
op|'.'
name|'id'
newline|'\n'
name|'query_delete'
op|'='
name|'sql'
op|'.'
name|'select'
op|'('
op|'['
name|'column'
op|']'
op|','
nl|'\n'
name|'test_table'
op|'.'
name|'c'
op|'.'
name|'id'
op|'<'
number|'5'
op|')'
op|'.'
name|'order_by'
op|'('
name|'column'
op|')'
newline|'\n'
name|'delete_statement'
op|'='
name|'utils'
op|'.'
name|'DeleteFromSelect'
op|'('
name|'test_table'
op|','
nl|'\n'
name|'query_delete'
op|','
name|'column'
op|')'
newline|'\n'
name|'result_delete'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
name|'delete_statement'
op|')'
newline|'\n'
comment|'# Verify we delete 4 rows'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result_delete'
op|'.'
name|'rowcount'
op|','
number|'4'
op|')'
newline|'\n'
nl|'\n'
name|'query_all'
op|'='
name|'sql'
op|'.'
name|'select'
op|'('
op|'['
name|'test_table'
op|']'
op|')'
op|'.'
name|'where'
op|'('
name|'test_table'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|'.'
name|'in_'
op|'('
name|'uuidstrs'
op|')'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
name|'query_all'
op|')'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
comment|'# Verify we still have 6 rows in table'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rows'
op|')'
op|','
number|'6'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_shadow_table
dedent|''
name|'def'
name|'test_check_shadow_table'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_check_shadow_table'"
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'c'"
op|','
name|'String'
op|'('
number|'256'
op|')'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# check missing shadow table'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NoSuchTableError'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'check_shadow_table'
op|','
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
name|'shadow_table'
op|'='
name|'Table'
op|'('
name|'db'
op|'.'
name|'_SHADOW_TABLE_PREFIX'
op|'+'
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|')'
newline|'\n'
name|'shadow_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# check missing column'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'check_shadow_table'
op|','
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# check when all is ok'
nl|'\n'
name|'c'
op|'='
name|'Column'
op|'('
string|"'c'"
op|','
name|'String'
op|'('
number|'256'
op|')'
op|')'
newline|'\n'
name|'shadow_table'
op|'.'
name|'create_column'
op|'('
name|'c'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'check_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# check extra column'
nl|'\n'
name|'d'
op|'='
name|'Column'
op|'('
string|"'d'"
op|','
name|'Integer'
op|')'
newline|'\n'
name|'shadow_table'
op|'.'
name|'create_column'
op|'('
name|'d'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'check_shadow_table'
op|','
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_shadow_table_different_types
dedent|''
name|'def'
name|'test_check_shadow_table_different_types'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_check_shadow_table_different_types'"
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'shadow_table'
op|'='
name|'Table'
op|'('
name|'db'
op|'.'
name|'_SHADOW_TABLE_PREFIX'
op|'+'
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'String'
op|'('
number|'256'
op|')'
op|')'
op|')'
newline|'\n'
name|'shadow_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'check_shadow_table'
op|','
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test_base'
op|'.'
name|'backend_specific'
op|'('
string|"'sqlite'"
op|')'
newline|'\n'
DECL|member|test_check_shadow_table_with_unsupported_sqlite_type
name|'def'
name|'test_check_shadow_table_with_unsupported_sqlite_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_check_shadow_table_with_unsupported_sqlite_type'"
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'c'"
op|','
name|'CustomType'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'shadow_table'
op|'='
name|'Table'
op|'('
name|'db'
op|'.'
name|'_SHADOW_TABLE_PREFIX'
op|'+'
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'c'"
op|','
name|'CustomType'
op|')'
op|')'
newline|'\n'
name|'shadow_table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'check_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_shadow_table_by_table_instance
dedent|''
name|'def'
name|'test_create_shadow_table_by_table_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_create_shadow_table_by_table_instance'"
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'b'"
op|','
name|'String'
op|'('
number|'256'
op|')'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table'
op|'='
name|'table'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'check_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_shadow_table_by_name
dedent|''
name|'def'
name|'test_create_shadow_table_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_create_shadow_table_by_name'"
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'b'"
op|','
name|'String'
op|'('
number|'256'
op|')'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|'='
name|'table_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'check_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test_base'
op|'.'
name|'backend_specific'
op|'('
string|"'sqlite'"
op|')'
newline|'\n'
DECL|member|test_create_shadow_table_not_supported_type
name|'def'
name|'test_create_shadow_table_not_supported_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_create_shadow_table_not_supported_type'"
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'CustomType'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# reflection of custom types has been fixed upstream'
nl|'\n'
name|'if'
name|'SA_VERSION'
op|'<'
op|'('
number|'0'
op|','
number|'9'
op|','
number|'0'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'oslodbutils'
op|'.'
name|'ColumnError'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|','
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|'='
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'utils'
op|'.'
name|'create_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
nl|'\n'
name|'table_name'
op|'='
name|'table_name'
op|','
nl|'\n'
name|'a'
op|'='
name|'Column'
op|'('
string|"'a'"
op|','
name|'CustomType'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'utils'
op|'.'
name|'check_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_shadow_both_table_and_table_name_are_none
dedent|''
name|'def'
name|'test_create_shadow_both_table_and_table_name_are_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|','
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_shadow_both_table_and_table_name_are_specified
dedent|''
name|'def'
name|'test_create_shadow_both_table_and_table_name_are_specified'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
op|'('
string|"'test_create_shadow_both_table_and_table_name_are_'"
nl|'\n'
string|"'specified'"
op|')'
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|','
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|','
name|'table'
op|'='
name|'table'
op|','
name|'table_name'
op|'='
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_duplicate_shadow_table
dedent|''
name|'def'
name|'test_create_duplicate_shadow_table'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table_name'
op|'='
string|"'test_create_duplicate_shadow_table'"
newline|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'self'
op|'.'
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'a'"
op|','
name|'Integer'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|'='
name|'table_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ShadowTableExists'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'create_shadow_table'
op|','
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|'='
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestMigrationUtilsPostgreSQL'
op|'('
name|'TestMigrationUtilsSQLite'
op|','
nl|'\n'
DECL|class|TestMigrationUtilsPostgreSQL
name|'test_base'
op|'.'
name|'PostgreSQLOpportunisticTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestMigrationUtilsMySQL'
op|'('
name|'TestMigrationUtilsSQLite'
op|','
nl|'\n'
DECL|class|TestMigrationUtilsMySQL
name|'test_base'
op|'.'
name|'MySQLOpportunisticTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
