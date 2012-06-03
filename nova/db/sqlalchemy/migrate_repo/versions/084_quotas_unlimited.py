begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc'
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
name|'sqlalchemy'
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
string|'"""Map quotas hard_limit from NULL to -1"""'
newline|'\n'
name|'_migrate_unlimited'
op|'('
name|'migrate_engine'
op|','
name|'None'
op|','
op|'-'
number|'1'
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
string|'"""Map quotas hard_limit from -1 to NULL"""'
newline|'\n'
name|'_migrate_unlimited'
op|'('
name|'migrate_engine'
op|','
op|'-'
number|'1'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_migrate_unlimited
dedent|''
name|'def'
name|'_migrate_unlimited'
op|'('
name|'migrate_engine'
op|','
name|'old_limit'
op|','
name|'new_limit'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
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
DECL|function|_migrate
name|'def'
name|'_migrate'
op|'('
name|'table_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'sqlalchemy'
op|'.'
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
name|'table'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'where'
op|'('
name|'table'
op|'.'
name|'c'
op|'.'
name|'hard_limit'
op|'=='
name|'old_limit'
op|')'
op|'.'
name|'values'
op|'('
name|'hard_limit'
op|'='
name|'new_limit'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_migrate'
op|'('
string|"'quotas'"
op|')'
newline|'\n'
name|'_migrate'
op|'('
string|"'quota_classes'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
