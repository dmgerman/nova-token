begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2013 Wenhao Xu <xuwenhao2008@gmail.com>.'
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
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'String'
op|','
name|'Table'
op|','
name|'DateTime'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'dialects'
name|'import'
name|'postgresql'
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
string|'"""Convert period_beginning and period_ending to DateTime."""'
newline|'\n'
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
name|'dialect'
op|'='
name|'migrate_engine'
op|'.'
name|'url'
op|'.'
name|'get_dialect'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'dialect'
name|'is'
name|'postgresql'
op|'.'
name|'dialect'
op|':'
newline|'\n'
comment|'# We need to handle postresql specially.'
nl|'\n'
comment|"# Can't use migrate's alter() because it does not support"
nl|'\n'
comment|'# explicit casting'
nl|'\n'
indent|'        '
name|'for'
name|'column'
name|'in'
op|'('
string|"'period_beginning'"
op|','
string|"'period_ending'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE task_log "'
nl|'\n'
string|'"ALTER COLUMN %s TYPE TIMESTAMP WITHOUT TIME ZONE "'
nl|'\n'
string|'"USING %s::TIMESTAMP WITHOUT TIME ZONE"'
nl|'\n'
op|'%'
op|'('
name|'column'
op|','
name|'column'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'task_log'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'period_beginning'
op|'.'
name|'alter'
op|'('
name|'DateTime'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'period_ending'
op|'.'
name|'alter'
op|'('
name|'DateTime'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert columns back to String(255)."""'
newline|'\n'
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
comment|"# don't need to handle postgresql here."
nl|'\n'
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'task_log'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'period_beginning'
op|'.'
name|'alter'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'period_ending'
op|'.'
name|'alter'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
