begin_unit
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
op|','
name|'MetaData'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|','
nl|'\n'
name|'autoload_with'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'types'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'instances'
op|'.'
name|'select'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'types'
op|'['
name|'instance'
op|'.'
name|'id'
op|']'
op|'='
name|'int'
op|'('
name|'instance'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'types'
op|'['
name|'instance'
op|'.'
name|'id'
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'integer_column'
op|'='
name|'Column'
op|'('
string|"'instance_type_id_int'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
name|'string_column'
op|'='
name|'instances'
op|'.'
name|'c'
op|'.'
name|'instance_type_id'
newline|'\n'
nl|'\n'
name|'integer_column'
op|'.'
name|'create'
op|'('
name|'instances'
op|')'
newline|'\n'
name|'for'
name|'instance_id'
op|','
name|'instance_type_id'
name|'in'
name|'types'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'update'
op|'='
name|'instances'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'instance_id'
op|')'
op|'.'
name|'values'
op|'('
name|'instance_type_id_int'
op|'='
name|'instance_type_id'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'update'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'string_column'
op|'.'
name|'alter'
op|'('
name|'name'
op|'='
string|"'instance_type_id_str'"
op|')'
newline|'\n'
name|'integer_column'
op|'.'
name|'alter'
op|'('
name|'name'
op|'='
string|"'instance_type_id'"
op|')'
newline|'\n'
name|'string_column'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|','
nl|'\n'
name|'autoload_with'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'integer_column'
op|'='
name|'instances'
op|'.'
name|'c'
op|'.'
name|'instance_type_id'
newline|'\n'
name|'string_column'
op|'='
name|'Column'
op|'('
string|"'instance_type_id_str'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'types'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'instances'
op|'.'
name|'select'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance'
op|'.'
name|'instance_type_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'types'
op|'['
name|'instance'
op|'.'
name|'id'
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'types'
op|'['
name|'instance'
op|'.'
name|'id'
op|']'
op|'='
name|'str'
op|'('
name|'instance'
op|'.'
name|'instance_type_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'string_column'
op|'.'
name|'create'
op|'('
name|'instances'
op|')'
newline|'\n'
name|'for'
name|'instance_id'
op|','
name|'instance_type_id'
name|'in'
name|'types'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'update'
op|'='
name|'instances'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'instance_id'
op|')'
op|'.'
name|'values'
op|'('
name|'instance_type_id_str'
op|'='
name|'instance_type_id'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'update'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'integer_column'
op|'.'
name|'alter'
op|'('
name|'name'
op|'='
string|"'instance_type_id_int'"
op|')'
newline|'\n'
name|'string_column'
op|'.'
name|'alter'
op|'('
name|'name'
op|'='
string|"'instance_type_id'"
op|')'
newline|'\n'
name|'integer_column'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
