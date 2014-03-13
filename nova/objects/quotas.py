begin_unit
comment|'#    Copyright 2013 Rackspace Hosting.'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ids_from_instance
name|'def'
name|'ids_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
op|'('
name|'context'
op|'.'
name|'is_admin'
name|'and'
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|'!='
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
dedent|''
name|'if'
name|'context'
op|'.'
name|'user_id'
op|'!='
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'user_id'
op|'='
name|'instance'
op|'['
string|"'user_id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'user_id'
op|'='
name|'context'
op|'.'
name|'user_id'
newline|'\n'
dedent|''
name|'return'
name|'project_id'
op|','
name|'user_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Quotas
dedent|''
name|'class'
name|'Quotas'
op|'('
name|'base'
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
string|"'reservations'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'Quotas'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
comment|'# Set up defaults.'
nl|'\n'
name|'self'
op|'.'
name|'reservations'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_reservations
name|'def'
name|'from_reservations'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'reservations'
op|','
name|'instance'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Transitional for compatibility."""'
newline|'\n'
name|'if'
name|'instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'project_id'
op|'='
name|'None'
newline|'\n'
name|'user_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'project_id'
op|','
name|'user_id'
op|'='
name|'ids_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'quotas'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'quotas'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'quotas'
op|'.'
name|'reservations'
op|'='
name|'reservations'
newline|'\n'
name|'quotas'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'quotas'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'quotas'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'quotas'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|reserve
name|'def'
name|'reserve'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'expire'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'user_id'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'deltas'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reservations'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'reserve'
op|'('
name|'context'
op|','
name|'expire'
op|'='
name|'expire'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
op|'**'
name|'deltas'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reservations'
op|'='
name|'reservations'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|commit
name|'def'
name|'commit'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'reservations'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'context'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'self'
op|'.'
name|'_context'
newline|'\n'
dedent|''
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'commit'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'reservations'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reservations'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|rollback
name|'def'
name|'rollback'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rollback quotas."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'reservations'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'context'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'self'
op|'.'
name|'_context'
newline|'\n'
dedent|''
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'rollback'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'reservations'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reservations'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotasNoOp
dedent|''
dedent|''
name|'class'
name|'QuotasNoOp'
op|'('
name|'Quotas'
op|')'
op|':'
newline|'\n'
DECL|member|reserve
indent|'    '
name|'def'
name|'reserve'
op|'('
name|'context'
op|','
name|'expire'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'user_id'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'deltas'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|commit
dedent|''
name|'def'
name|'commit'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|rollback
dedent|''
name|'def'
name|'rollback'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
