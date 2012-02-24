begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack, LLC'
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
string|'"""\nTests for database migrations. This test case reads the configuration\nfile test_migrations.conf for database connection settings\nto use in the tests. For each connection found in the config file,\nthe test case runs a series of test cases to ensure that migrations work\nproperly both upgrading and downgrading, and that no data loss occurs\nif possible.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'ConfigParser'
newline|'\n'
name|'import'
name|'commands'
newline|'\n'
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
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
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
name|'from'
name|'sqlalchemy'
name|'import'
name|'create_engine'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'migrate_repo'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
string|"'nova.tests.test_migrations'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|MIGRATE_PKG_VER
name|'MIGRATE_PKG_VER'
op|'='
name|'dist_version'
op|'.'
name|'StrictVersion'
op|'('
name|'migrate'
op|'.'
name|'__version__'
op|')'
newline|'\n'
DECL|variable|USE_MIGRATE_PATCH
name|'USE_MIGRATE_PATCH'
op|'='
name|'MIGRATE_PKG_VER'
op|'<'
name|'dist_version'
op|'.'
name|'StrictVersion'
op|'('
string|"'0.7.3'"
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
dedent|''
dedent|''
dedent|''
name|'if'
name|'USE_MIGRATE_PATCH'
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
op|'.'
name|'versioning'
name|'import'
name|'api'
name|'as'
name|'migration_api'
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
nl|'\n'
DECL|class|TestMigrations
name|'class'
name|'TestMigrations'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test sqlalchemy-migrate migrations"""'
newline|'\n'
nl|'\n'
DECL|variable|TEST_DATABASES
name|'TEST_DATABASES'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|DEFAULT_CONFIG_FILE
name|'DEFAULT_CONFIG_FILE'
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
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|"'test_migrations.conf'"
op|')'
newline|'\n'
comment|'# Test machines can set the NOVA_TEST_MIGRATIONS_CONF variable'
nl|'\n'
comment|'# to override the location of the config file for migration testing'
nl|'\n'
DECL|variable|CONFIG_FILE_PATH
name|'CONFIG_FILE_PATH'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'NOVA_TEST_MIGRATIONS_CONF'"
op|','
nl|'\n'
name|'DEFAULT_CONFIG_FILE'
op|')'
newline|'\n'
DECL|variable|MIGRATE_FILE
name|'MIGRATE_FILE'
op|'='
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'migrate_repo'
op|'.'
name|'__file__'
newline|'\n'
DECL|variable|REPOSITORY
name|'REPOSITORY'
op|'='
name|'Repository'
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
name|'MIGRATE_FILE'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestMigrations'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestMigrations'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Load test databases from the config file. Only do this'
nl|'\n'
comment|'# once. No need to re-run this on each test...'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'config_path is %s'"
op|'%'
name|'TestMigrations'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'TestMigrations'
op|'.'
name|'TEST_DATABASES'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'TestMigrations'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cp'
op|'='
name|'ConfigParser'
op|'.'
name|'RawConfigParser'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'cp'
op|'.'
name|'read'
op|'('
name|'TestMigrations'
op|'.'
name|'CONFIG_FILE_PATH'
op|')'
newline|'\n'
name|'defaults'
op|'='
name|'cp'
op|'.'
name|'defaults'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'defaults'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'TestMigrations'
op|'.'
name|'TEST_DATABASES'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'snake_walk'
op|'='
name|'cp'
op|'.'
name|'getboolean'
op|'('
string|"'walk_style'"
op|','
string|"'snake_walk'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ConfigParser'
op|'.'
name|'ParsingError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Failed to read test_migrations.conf config "'
nl|'\n'
string|'"file. Got error: %s"'
op|'%'
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Failed to find test_migrations.conf config "'
nl|'\n'
string|'"file."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'engines'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'TestMigrations'
op|'.'
name|'TEST_DATABASES'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'engines'
op|'['
name|'key'
op|']'
op|'='
name|'create_engine'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|'# We start each test case with a completely blank slate.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_reset_databases'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TestMigrations'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# We destroy the test data store between each test case,'
nl|'\n'
comment|'# and recreate it, which ensures that we have no side-effects'
nl|'\n'
comment|'# from the tests'
nl|'\n'
name|'self'
op|'.'
name|'_reset_databases'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_databases
dedent|''
name|'def'
name|'_reset_databases'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|execute_cmd
indent|'        '
name|'def'
name|'execute_cmd'
op|'('
name|'cmd'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'status'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'engine'
name|'in'
name|'self'
op|'.'
name|'engines'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'conn_string'
op|'='
name|'TestMigrations'
op|'.'
name|'TEST_DATABASES'
op|'['
name|'key'
op|']'
newline|'\n'
name|'conn_pieces'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'conn_string'
op|')'
newline|'\n'
name|'if'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'sqlite'"
op|')'
op|':'
newline|'\n'
comment|'# We can just delete the SQLite database, which is'
nl|'\n'
comment|'# the easiest and cleanest solution'
nl|'\n'
indent|'                '
name|'db_path'
op|'='
name|'conn_pieces'
op|'.'
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'db_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'db_path'
op|')'
newline|'\n'
comment|'# No need to recreate the SQLite DB. SQLite will'
nl|'\n'
comment|"# create it for us if it's not there..."
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'mysql'"
op|')'
op|':'
newline|'\n'
comment|'# We can execute the MySQL client to destroy and re-create'
nl|'\n'
comment|'# the MYSQL database, which is easier and less error-prone'
nl|'\n'
comment|'# than using SQLAlchemy to do this via MetaData...trust me.'
nl|'\n'
indent|'                '
name|'database'
op|'='
name|'conn_pieces'
op|'.'
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'loc_pieces'
op|'='
name|'conn_pieces'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"'@'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'loc_pieces'
op|'['
number|'1'
op|']'
newline|'\n'
name|'auth_pieces'
op|'='
name|'loc_pieces'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'user'
op|'='
name|'auth_pieces'
op|'['
number|'0'
op|']'
newline|'\n'
name|'password'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'auth_pieces'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'auth_pieces'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'password'
op|'='
string|'"-p%s"'
op|'%'
name|'auth_pieces'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'sql'
op|'='
op|'('
string|'"drop database if exists %(database)s; "'
nl|'\n'
string|'"create database %(database)s;"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"mysql -u%(user)s %(password)s -h%(host)s "'
nl|'\n'
string|'"-e\\"%(sql)s\\""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'conn_string'
op|'.'
name|'startswith'
op|'('
string|"'postgresql'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'database'
op|'='
name|'conn_pieces'
op|'.'
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'loc_pieces'
op|'='
name|'conn_pieces'
op|'.'
name|'netloc'
op|'.'
name|'split'
op|'('
string|"'@'"
op|')'
newline|'\n'
name|'host'
op|'='
name|'loc_pieces'
op|'['
number|'1'
op|']'
newline|'\n'
name|'auth_pieces'
op|'='
name|'loc_pieces'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'user'
op|'='
name|'auth_pieces'
op|'['
number|'0'
op|']'
newline|'\n'
name|'password'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'auth_pieces'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'auth_pieces'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'password'
op|'='
name|'auth_pieces'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'cmd'
op|'='
op|'('
string|'"touch ~/.pgpass;"'
nl|'\n'
string|'"chmod 0600 ~/.pgpass;"'
nl|'\n'
string|'"sed -i -e"'
nl|'\n'
string|'"\'1{s/^.*$/\\*:\\*:\\*:%(user)s:%(password)s/};"'
nl|'\n'
string|'"1!d\' ~/.pgpass"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'sql'
op|'='
op|'('
string|'"UPDATE pg_catalog.pg_database SET datallowconn=false "'
nl|'\n'
string|'"WHERE datname=\'%(database)s\';"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"psql -U%(user)s -h%(host)s -c\\"%(sql)s\\""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'sql'
op|'='
op|'('
string|'"SELECT pg_catalog.pg_terminate_backend(procpid) "'
nl|'\n'
string|'"FROM pg_catalog.pg_stat_activity "'
nl|'\n'
string|'"WHERE datname=\'%(database)s\';"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"psql -U%(user)s -h%(host)s -c\\"%(sql)s\\""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'sql'
op|'='
op|'('
string|'"drop database if exists %(database)s;"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"psql -U%(user)s -h%(host)s -c\\"%(sql)s\\""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'sql'
op|'='
op|'('
string|'"create database %(database)s;"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|'"psql -U%(user)s -h%(host)s -c\\"%(sql)s\\""'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'execute_cmd'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_walk_versions
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_walk_versions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Walks all version scripts for each tested database, ensuring\n        that there are no errors in the version scripts for each engine\n        """'
newline|'\n'
name|'for'
name|'key'
op|','
name|'engine'
name|'in'
name|'self'
op|'.'
name|'engines'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_walk_versions'
op|'('
name|'engine'
op|','
name|'self'
op|'.'
name|'snake_walk'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_walk_versions
dedent|''
dedent|''
name|'def'
name|'_walk_versions'
op|'('
name|'self'
op|','
name|'engine'
op|'='
name|'None'
op|','
name|'snake_walk'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# Determine latest version script from the repo, then'
nl|'\n'
comment|'# upgrade from 1 through to the latest, with no data'
nl|'\n'
comment|'# in the databases. This just checks that the schema itself'
nl|'\n'
comment|'# upgrades successfully.'
nl|'\n'
nl|'\n'
comment|'# Place the database under version control'
nl|'\n'
indent|'        '
name|'migration_api'
op|'.'
name|'version_control'
op|'('
name|'engine'
op|','
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'latest version is %s'"
op|'%'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|'.'
name|'latest'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'version'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|'.'
name|'latest'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
comment|'# upgrade -> downgrade -> upgrade'
nl|'\n'
indent|'            '
name|'migration_api'
op|'.'
name|'upgrade'
op|'('
name|'engine'
op|','
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
name|'if'
name|'snake_walk'
op|':'
newline|'\n'
indent|'                '
name|'migration_api'
op|'.'
name|'downgrade'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
nl|'\n'
name|'version'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|'-'
number|'1'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
name|'migration_api'
op|'.'
name|'upgrade'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
nl|'\n'
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now walk it back down to 0 from the latest, testing'
nl|'\n'
comment|'# the downgrade paths.'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'version'
name|'in'
name|'reversed'
op|'('
nl|'\n'
name|'xrange'
op|'('
number|'0'
op|','
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|'.'
name|'latest'
op|')'
op|')'
op|':'
newline|'\n'
comment|'# downgrade -> upgrade -> downgrade'
nl|'\n'
indent|'            '
name|'migration_api'
op|'.'
name|'downgrade'
op|'('
name|'engine'
op|','
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
name|'if'
name|'snake_walk'
op|':'
newline|'\n'
indent|'                '
name|'migration_api'
op|'.'
name|'upgrade'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
nl|'\n'
name|'version'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|'+'
number|'1'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
name|'migration_api'
op|'.'
name|'downgrade'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|','
nl|'\n'
name|'version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'version'
op|','
nl|'\n'
name|'migration_api'
op|'.'
name|'db_version'
op|'('
name|'engine'
op|','
nl|'\n'
name|'TestMigrations'
op|'.'
name|'REPOSITORY'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
