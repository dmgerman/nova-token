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
name|'distutils'
op|'.'
name|'version'
name|'as'
name|'dist_version'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_engine'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'migrate'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'util'
name|'as'
name|'migrate_util'
newline|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
nl|'\n'
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
op|'@'
name|'migrate_util'
op|'.'
name|'decorator'
newline|'\n'
DECL|function|patched_with_engine
name|'def'
name|'patched_with_engine'
op|'('
name|'f'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'url'
op|'='
name|'a'
op|'['
number|'0'
op|']'
newline|'\n'
name|'engine'
op|'='
name|'migrate_util'
op|'.'
name|'construct_engine'
op|'('
name|'url'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'kw'
op|'['
string|"'engine'"
op|']'
op|'='
name|'engine'
newline|'\n'
name|'return'
name|'f'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'engine'
op|','
name|'migrate_util'
op|'.'
name|'Engine'
op|')'
name|'and'
name|'engine'
name|'is'
name|'not'
name|'url'
op|':'
newline|'\n'
indent|'            '
name|'migrate_util'
op|'.'
name|'log'
op|'.'
name|'debug'
op|'('
string|"'Disposing SQLAlchemy engine %s'"
op|','
name|'engine'
op|')'
newline|'\n'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(jkoelker) When migrate 0.7.3 is released and nova depends'
nl|'\n'
comment|'#                on that version or higher, this can be removed'
nl|'\n'
DECL|variable|MIN_PKG_VERSION
dedent|''
dedent|''
dedent|''
name|'MIN_PKG_VERSION'
op|'='
name|'dist_version'
op|'.'
name|'StrictVersion'
op|'('
string|"'0.7.3'"
op|')'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'hasattr'
op|'('
name|'migrate'
op|','
string|"'__version__'"
op|')'
name|'or'
nl|'\n'
name|'dist_version'
op|'.'
name|'StrictVersion'
op|'('
name|'migrate'
op|'.'
name|'__version__'
op|')'
op|'<'
name|'MIN_PKG_VERSION'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'migrate_util'
op|'.'
name|'with_engine'
op|'='
name|'patched_with_engine'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(jkoelker) Delay importing migrate until we are patched'
nl|'\n'
dedent|''
name|'from'
name|'migrate'
name|'import'
name|'exceptions'
name|'as'
name|'versioning_exceptions'
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
name|'from'
name|'migrate'
op|'.'
name|'versioning'
op|'.'
name|'repository'
name|'import'
name|'Repository'
newline|'\n'
nl|'\n'
DECL|variable|_REPOSITORY
name|'_REPOSITORY'
op|'='
name|'None'
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
name|'if'
name|'version'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'int'
op|'('
name|'version'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"version should be an integer"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'current_version'
op|'='
name|'db_version'
op|'('
op|')'
newline|'\n'
name|'repository'
op|'='
name|'_find_migrate_repo'
op|'('
op|')'
newline|'\n'
name|'if'
name|'version'
name|'is'
name|'None'
name|'or'
name|'version'
op|'>'
name|'current_version'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'upgrade'
op|'('
name|'get_engine'
op|'('
op|')'
op|','
name|'repository'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'versioning_api'
op|'.'
name|'downgrade'
op|'('
name|'get_engine'
op|'('
op|')'
op|','
name|'repository'
op|','
nl|'\n'
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|db_version
dedent|''
dedent|''
name|'def'
name|'db_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'repository'
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
name|'get_engine'
op|'('
op|')'
op|','
name|'repository'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'versioning_exceptions'
op|'.'
name|'DatabaseNotControlledError'
op|':'
newline|'\n'
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
name|'get_engine'
op|'('
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
name|'tables'
op|'='
name|'meta'
op|'.'
name|'tables'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'tables'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'db_version_control'
op|'('
name|'migration'
op|'.'
name|'INIT_VERSION'
op|')'
newline|'\n'
name|'return'
name|'versioning_api'
op|'.'
name|'db_version'
op|'('
name|'get_engine'
op|'('
op|')'
op|','
name|'repository'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# Some pre-Essex DB's may not be version controlled."
nl|'\n'
comment|'# Require them to upgrade using Essex first.'
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Upgrade DB using Essex release first."'
op|')'
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
name|'repository'
op|'='
name|'_find_migrate_repo'
op|'('
op|')'
newline|'\n'
name|'versioning_api'
op|'.'
name|'version_control'
op|'('
name|'get_engine'
op|'('
op|')'
op|','
name|'repository'
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
name|'global'
name|'_REPOSITORY'
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
name|'if'
name|'_REPOSITORY'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_REPOSITORY'
op|'='
name|'Repository'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_REPOSITORY'
newline|'\n'
dedent|''
endmarker|''
end_unit
