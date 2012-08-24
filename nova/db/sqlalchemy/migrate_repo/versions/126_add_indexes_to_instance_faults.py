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
comment|'# Based on instance_fault_get_by_instance_uuids'
nl|'\n'
comment|'# from: nova/db/sqlalchemy/api.py'
nl|'\n'
name|'t'
op|'='
name|'Table'
op|'('
string|"'instance_faults'"
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
string|"'instance_faults_instance_uuid_deleted_created_at_idx'"
op|','
nl|'\n'
name|'t'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'created_at'
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
string|"'instance_faults'"
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
string|"'instance_faults_instance_uuid_deleted_created_at_idx'"
op|','
nl|'\n'
name|'t'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|','
name|'t'
op|'.'
name|'c'
op|'.'
name|'created_at'
op|')'
newline|'\n'
name|'i'
op|'.'
name|'drop'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
