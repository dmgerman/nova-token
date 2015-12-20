begin_unit
comment|'#    Copyright 2015 Red Hat, Inc.'
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
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
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
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register_if'
op|'('
name|'False'
op|')'
newline|'\n'
DECL|class|LiveMigrateData
name|'class'
name|'LiveMigrateData'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'is_volume_backed'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'migration'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Migration'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|to_legacy_dict
name|'def'
name|'to_legacy_dict'
op|'('
name|'self'
op|','
name|'pre_migration_result'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'legacy'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'is_volume_backed'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'is_volume_backed'"
op|']'
op|'='
name|'self'
op|'.'
name|'is_volume_backed'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'migration'"
op|']'
op|'='
name|'self'
op|'.'
name|'migration'
newline|'\n'
dedent|''
name|'if'
name|'pre_migration_result'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'legacy'
newline|'\n'
nl|'\n'
DECL|member|from_legacy_dict
dedent|''
name|'def'
name|'from_legacy_dict'
op|'('
name|'self'
op|','
name|'legacy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'is_volume_backed'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_volume_backed'
op|'='
name|'legacy'
op|'['
string|"'is_volume_backed'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'migration'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'migration'
op|'='
name|'legacy'
op|'['
string|"'migration'"
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit