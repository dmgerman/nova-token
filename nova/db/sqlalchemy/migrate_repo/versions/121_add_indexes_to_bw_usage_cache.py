begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
name|'Index'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'exc'
name|'import'
name|'IntegrityError'
op|','
name|'OperationalError'
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
comment|'# Based on bw_usage_get_by_uuids'
nl|'\n'
comment|'# from: nova/db/sqlalchemy/api.py'
nl|'\n'
name|'t'
op|'='
name|'Table'
op|'('
string|"'bw_usage_cache'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'i'
op|'='
name|'Index'
op|'('
string|"'bw_usage_cache_uuid_start_period_idx'"
op|','
nl|'\n'
name|'t'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'start_period'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IntegrityError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'t'
op|'='
name|'Table'
op|'('
string|"'bw_usage_cache'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'i'
op|'='
name|'Index'
op|'('
string|"'bw_usage_cache_uuid_start_period_idx'"
op|','
nl|'\n'
name|'t'
op|'.'
name|'c'
op|'.'
name|'uuid'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'start_period'
op|')'
newline|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'url'
op|'.'
name|'get_dialect'
op|'('
op|')'
op|'.'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'sqlite'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'i'
op|'.'
name|'drop'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OperationalError'
op|':'
newline|'\n'
comment|'# Sqlite is very broken for any kind of table modification.'
nl|'\n'
comment|'# adding columns creates a new table, then copies the data,'
nl|'\n'
comment|'# and looses the indexes.'
nl|'\n'
comment|'# Thus later migrations that add columns will cause the'
nl|'\n'
comment|"# earlier migration's downgrade unittests to fail on"
nl|'\n'
comment|'# dropping indexes.'
nl|'\n'
comment|'# Honestly testing migrations on sqlite is not really a very'
nl|'\n'
comment|'# valid test (because of above facts), but that is for'
nl|'\n'
comment|'# another day. (mdragon)'
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'.'
name|'drop'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
