begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'api'
name|'as'
name|'versioning_api'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'exceptions'
name|'as'
name|'versioning_exceptions'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
comment|'# python-migration changed location of exceptions after 1.6.3'
nl|'\n'
comment|'# See LP Bug #717467'
nl|'\n'
indent|'        '
name|'from'
name|'migrate'
name|'import'
name|'exceptions'
name|'as'
name|'versioning_exceptions'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'exit'
op|'('
name|'_'
op|'('
string|'"python-migrate is not installed. Exiting."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
dedent|''
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_sync
name|'def'
name|'db_sync'
op|'('
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_version'
op|'('
op|')'
newline|'\n'
name|'repo_path'
op|'='
name|'_find_migrate_repo'
op|'('
op|')'
newline|'\n'
name|'return'
name|'versioning_api'
op|'.'
name|'upgrade'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'repo_path'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version
dedent|''
name|'def'
name|'db_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'repo_path'
op|'='
name|'_find_migrate_repo'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'db_version'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'repo_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'versioning_exceptions'
op|'.'
name|'DatabaseNotControlledError'
op|':'
newline|'\n'
comment|"# If we aren't version controlled we may already have the database"
nl|'\n'
comment|'# in the state from before we started version control, check for that'
nl|'\n'
comment|'# and set up version_control appropriately'
nl|'\n'
indent|'        '
name|'meta'
op|'='
name|'sqlalchemy'
op|'.'
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'engine'
op|'='
name|'sqlalchemy'
op|'.'
name|'create_engine'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'echo'
op|'='
name|'False'
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'reflect'
op|'('
name|'bind'
op|'='
name|'engine'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'table'
name|'in'
op|'('
string|"'auth_tokens'"
op|','
string|"'zones'"
op|','
string|"'export_devices'"
op|','
nl|'\n'
string|"'fixed_ips'"
op|','
string|"'floating_ips'"
op|','
string|"'instances'"
op|','
nl|'\n'
string|"'key_pairs'"
op|','
string|"'networks'"
op|','
string|"'projects'"
op|','
string|"'quotas'"
op|','
nl|'\n'
string|"'security_group_instance_association'"
op|','
nl|'\n'
string|"'security_group_rules'"
op|','
string|"'security_groups'"
op|','
nl|'\n'
string|"'services'"
op|','
string|"'migrations'"
op|','
nl|'\n'
string|"'users'"
op|','
string|"'user_project_association'"
op|','
nl|'\n'
string|"'user_project_role_association'"
op|','
nl|'\n'
string|"'user_role_association'"
op|','
nl|'\n'
string|"'volumes'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'assert'
name|'table'
name|'in'
name|'meta'
op|'.'
name|'tables'
newline|'\n'
dedent|''
name|'return'
name|'db_version_control'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AssertionError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'db_version_control'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version_control
dedent|''
dedent|''
dedent|''
name|'def'
name|'db_version_control'
op|'('
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'repo_path'
op|'='
name|'_find_migrate_repo'
op|'('
op|')'
newline|'\n'
name|'versioning_api'
op|'.'
name|'version_control'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
name|'repo_path'
op|','
name|'version'
op|')'
newline|'\n'
name|'return'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_migrate_repo
dedent|''
name|'def'
name|'_find_migrate_repo'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the path for the migrate repository."""'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|')'
op|','
nl|'\n'
string|"'migrate_repo'"
op|')'
newline|'\n'
name|'assert'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
newline|'\n'
name|'return'
name|'path'
newline|'\n'
dedent|''
endmarker|''
end_unit
