begin_unit
comment|'# Copyright 2014 Rackspace Hosting'
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Table'
op|','
name|'Index'
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
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Change instances (project_id) index to cover (project_id, deleted)."""'
newline|'\n'
nl|'\n'
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
comment|"# Indexes can't be changed, we need to create the new one and delete"
nl|'\n'
comment|'# the old one'
nl|'\n'
nl|'\n'
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
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'index'
name|'in'
name|'instances'
op|'.'
name|'indexes'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'['
name|'c'
op|'.'
name|'name'
name|'for'
name|'c'
name|'in'
name|'index'
op|'.'
name|'columns'
op|']'
op|'=='
op|'['
string|"'project_id'"
op|','
string|"'deleted'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Skipped adding instances_project_id_deleted_idx '"
nl|'\n'
string|"'because an equivalent index already exists.'"
op|')'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'index'
op|'='
name|'Index'
op|'('
string|"'instances_project_id_deleted_idx'"
op|','
nl|'\n'
name|'instances'
op|'.'
name|'c'
op|'.'
name|'project_id'
op|','
name|'instances'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
newline|'\n'
name|'index'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'index'
name|'in'
name|'instances'
op|'.'
name|'indexes'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'['
name|'c'
op|'.'
name|'name'
name|'for'
name|'c'
name|'in'
name|'index'
op|'.'
name|'columns'
op|']'
op|'=='
op|'['
string|"'project_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'index'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
