begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'sqlalchemy'
name|'import'
name|'Boolean'
op|','
name|'Column'
op|','
name|'DateTime'
op|','
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
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
DECL|variable|resources
name|'resources'
op|'='
op|'['
nl|'\n'
string|"'instances'"
op|','
nl|'\n'
string|"'cores'"
op|','
nl|'\n'
string|"'volumes'"
op|','
nl|'\n'
string|"'gigabytes'"
op|','
nl|'\n'
string|"'floating_ips'"
op|','
nl|'\n'
string|"'metadata_items'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|old_style_quotas_table
name|'def'
name|'old_style_quotas_table'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'Table'
op|'('
name|'name'
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|','
nl|'\n'
name|'default'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|','
nl|'\n'
name|'onupdate'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
op|')'
op|','
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'project_id'"
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
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'instances'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'cores'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'volumes'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'gigabytes'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'floating_ips'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'metadata_items'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|new_style_quotas_table
dedent|''
name|'def'
name|'new_style_quotas_table'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'Table'
op|'('
name|'name'
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|','
nl|'\n'
name|'default'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|','
nl|'\n'
name|'onupdate'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
op|')'
op|','
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'project_id'"
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
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'resource'"
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
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'hard_limit'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|existing_quotas_table
dedent|''
name|'def'
name|'existing_quotas_table'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'Table'
op|'('
string|"'quotas'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|','
name|'autoload_with'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_assert_no_duplicate_project_ids
dedent|''
name|'def'
name|'_assert_no_duplicate_project_ids'
op|'('
name|'quotas'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'project_ids'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'message'
op|'='
op|'('
string|'\'There are multiple active quotas for project "%s" \''
nl|'\n'
string|"'(among others, possibly). '"
nl|'\n'
string|"'Please resolve all ambiguous quotas before '"
nl|'\n'
string|"'reattempting the migration.'"
op|')'
newline|'\n'
name|'for'
name|'quota'
name|'in'
name|'quotas'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'quota'
op|'.'
name|'project_id'
name|'not'
name|'in'
name|'project_ids'
op|','
name|'message'
op|'%'
name|'quota'
op|'.'
name|'project_id'
newline|'\n'
name|'project_ids'
op|'.'
name|'add'
op|'('
name|'quota'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_old_quotas_have_no_active_duplicates
dedent|''
dedent|''
name|'def'
name|'assert_old_quotas_have_no_active_duplicates'
op|'('
name|'migrate_engine'
op|','
name|'quotas'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that there are no duplicate non-deleted quota entries."""'
newline|'\n'
name|'select'
op|'='
name|'quotas'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'quotas'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|'=='
name|'False'
op|')'
newline|'\n'
name|'results'
op|'='
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'select'
op|')'
newline|'\n'
name|'_assert_no_duplicate_project_ids'
op|'('
name|'list'
op|'('
name|'results'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_new_quotas_have_no_active_duplicates
dedent|''
name|'def'
name|'assert_new_quotas_have_no_active_duplicates'
op|'('
name|'migrate_engine'
op|','
name|'quotas'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that there are no duplicate non-deleted quota entries."""'
newline|'\n'
name|'for'
name|'resource'
name|'in'
name|'resources'
op|':'
newline|'\n'
indent|'        '
name|'select'
op|'='
name|'quotas'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'quotas'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|'=='
name|'False'
op|')'
op|'.'
name|'where'
op|'('
name|'quotas'
op|'.'
name|'c'
op|'.'
name|'resource'
op|'=='
name|'resource'
op|')'
newline|'\n'
name|'results'
op|'='
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'select'
op|')'
newline|'\n'
name|'_assert_no_duplicate_project_ids'
op|'('
name|'list'
op|'('
name|'results'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_forward
dedent|''
dedent|''
name|'def'
name|'convert_forward'
op|'('
name|'migrate_engine'
op|','
name|'old_quotas'
op|','
name|'new_quotas'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'quotas'
op|'='
name|'list'
op|'('
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'old_quotas'
op|'.'
name|'select'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'quota'
name|'in'
name|'quotas'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'resource'
name|'in'
name|'resources'
op|':'
newline|'\n'
indent|'            '
name|'hard_limit'
op|'='
name|'getattr'
op|'('
name|'quota'
op|','
name|'resource'
op|')'
newline|'\n'
name|'if'
name|'hard_limit'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'insert'
op|'='
name|'new_quotas'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'values'
op|'('
nl|'\n'
name|'created_at'
op|'='
name|'quota'
op|'.'
name|'created_at'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'quota'
op|'.'
name|'updated_at'
op|','
nl|'\n'
name|'deleted_at'
op|'='
name|'quota'
op|'.'
name|'deleted_at'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'quota'
op|'.'
name|'deleted'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'quota'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'resource'
op|'='
name|'resource'
op|','
nl|'\n'
name|'hard_limit'
op|'='
name|'hard_limit'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'insert'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|earliest
dedent|''
dedent|''
dedent|''
name|'def'
name|'earliest'
op|'('
name|'date1'
op|','
name|'date2'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'date1'
name|'is'
name|'None'
name|'and'
name|'date2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'date1'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date2'
newline|'\n'
dedent|''
name|'if'
name|'date2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date1'
newline|'\n'
dedent|''
name|'if'
name|'date1'
op|'<'
name|'date2'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date1'
newline|'\n'
dedent|''
name|'return'
name|'date2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|latest
dedent|''
name|'def'
name|'latest'
op|'('
name|'date1'
op|','
name|'date2'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'date1'
name|'is'
name|'None'
name|'and'
name|'date2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'date1'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date2'
newline|'\n'
dedent|''
name|'if'
name|'date2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date1'
newline|'\n'
dedent|''
name|'if'
name|'date1'
op|'>'
name|'date2'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'date1'
newline|'\n'
dedent|''
name|'return'
name|'date2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_backward
dedent|''
name|'def'
name|'convert_backward'
op|'('
name|'migrate_engine'
op|','
name|'old_quotas'
op|','
name|'new_quotas'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'quotas'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'quota'
name|'in'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'new_quotas'
op|'.'
name|'select'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'quota'
op|'.'
name|'resource'
name|'not'
name|'in'
name|'resources'
nl|'\n'
name|'or'
name|'quota'
op|'.'
name|'hard_limit'
name|'is'
name|'None'
name|'or'
name|'quota'
op|'.'
name|'deleted'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'quota'
op|'.'
name|'project_id'
name|'in'
name|'quotas'
op|':'
newline|'\n'
indent|'            '
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'project_id'"
op|':'
name|'quota'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'quota'
op|'.'
name|'created_at'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'quota'
op|'.'
name|'updated_at'
op|','
nl|'\n'
name|'quota'
op|'.'
name|'resource'
op|':'
name|'quota'
op|'.'
name|'hard_limit'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'earliest'
op|'('
nl|'\n'
name|'quota'
op|'.'
name|'created_at'
op|','
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'latest'
op|'('
nl|'\n'
name|'quota'
op|'.'
name|'updated_at'
op|','
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'['
string|"'updated_at'"
op|']'
op|')'
newline|'\n'
name|'quotas'
op|'['
name|'quota'
op|'.'
name|'project_id'
op|']'
op|'['
name|'quota'
op|'.'
name|'resource'
op|']'
op|'='
name|'quota'
op|'.'
name|'hard_limit'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'quota'
name|'in'
name|'quotas'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'insert'
op|'='
name|'old_quotas'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'values'
op|'('
op|'**'
name|'quota'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'insert'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
dedent|''
dedent|''
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
comment|"# Upgrade operations go here. Don't create your own engine;"
nl|'\n'
comment|'# bind migrate_engine to your metadata'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'old_quotas'
op|'='
name|'existing_quotas_table'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'assert_old_quotas_have_no_active_duplicates'
op|'('
name|'migrate_engine'
op|','
name|'old_quotas'
op|')'
newline|'\n'
nl|'\n'
name|'new_quotas'
op|'='
name|'new_style_quotas_table'
op|'('
string|"'quotas_new'"
op|')'
newline|'\n'
name|'new_quotas'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'convert_forward'
op|'('
name|'migrate_engine'
op|','
name|'old_quotas'
op|','
name|'new_quotas'
op|')'
newline|'\n'
name|'old_quotas'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'new_quotas'
op|'.'
name|'rename'
op|'('
string|"'quotas'"
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
comment|'# Operations to reverse the above upgrade go here.'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'new_quotas'
op|'='
name|'existing_quotas_table'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'assert_new_quotas_have_no_active_duplicates'
op|'('
name|'migrate_engine'
op|','
name|'new_quotas'
op|')'
newline|'\n'
nl|'\n'
name|'old_quotas'
op|'='
name|'old_style_quotas_table'
op|'('
string|"'quotas_old'"
op|')'
newline|'\n'
name|'old_quotas'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'convert_backward'
op|'('
name|'migrate_engine'
op|','
name|'old_quotas'
op|','
name|'new_quotas'
op|')'
newline|'\n'
name|'new_quotas'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'old_quotas'
op|'.'
name|'rename'
op|'('
string|"'quotas'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
