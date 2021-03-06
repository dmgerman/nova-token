begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
string|'"""\nUtility for diff\'ing two versions of the DB schema.\n\nEach release cycle the plan is to compact all of the migrations from that\nrelease into a single file. This is a manual and, unfortunately, error-prone\nprocess. To ensure that the schema doesn\'t change, this tool can be used to\ndiff the compacted DB schema to the original, uncompacted form.\n\nThe database is specified by providing a SQLAlchemy connection URL WITHOUT the\ndatabase-name portion (that will be filled in automatically with a temporary\ndatabase name).\n\nThe schema versions are specified by providing a git ref (a branch name or\ncommit hash) and a SQLAlchemy-Migrate version number:\n\nRun like:\n\n    MYSQL:\n\n    ./tools/db/schema_diff.py mysql+pymysql://root@localhost \\\n                              master:latest my_branch:82\n\n    POSTGRESQL:\n\n    ./tools/db/schema_diff.py postgresql://localhost \\\n                              master:latest my_branch:82\n\n    DB2:\n    ./tools/db/schema_diff.py ibm_db_sa://localhost \\\n                              master:latest my_branch:82\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'print_function'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Dump'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|dump_db
name|'def'
name|'dump_db'
op|'('
name|'db_driver'
op|','
name|'db_name'
op|','
name|'db_url'
op|','
name|'migration_version'
op|','
name|'dump_filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'db_url'
op|'.'
name|'endswith'
op|'('
string|"'/'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_url'
op|'+='
string|"'/'"
newline|'\n'
nl|'\n'
dedent|''
name|'db_url'
op|'+='
name|'db_name'
newline|'\n'
nl|'\n'
name|'db_driver'
op|'.'
name|'create'
op|'('
name|'db_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'_migrate'
op|'('
name|'db_url'
op|','
name|'migration_version'
op|')'
newline|'\n'
name|'db_driver'
op|'.'
name|'dump'
op|'('
name|'db_name'
op|','
name|'dump_filename'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'db_driver'
op|'.'
name|'drop'
op|'('
name|'db_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Diff'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|diff_files
dedent|''
dedent|''
name|'def'
name|'diff_files'
op|'('
name|'filename1'
op|','
name|'filename2'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pipeline'
op|'='
op|'['
string|"'diff -U 3 %(filename1)s %(filename2)s'"
nl|'\n'
op|'%'
op|'{'
string|"'filename1'"
op|':'
name|'filename1'
op|','
string|"'filename2'"
op|':'
name|'filename2'
op|'}'
op|']'
newline|'\n'
nl|'\n'
comment|'# Use colordiff if available'
nl|'\n'
name|'if'
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|"'which'"
op|','
string|"'colordiff'"
op|']'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'pipeline'
op|'.'
name|'append'
op|'('
string|"'colordiff'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'pipeline'
op|'.'
name|'append'
op|'('
string|"'less -R'"
op|')'
newline|'\n'
nl|'\n'
name|'cmd'
op|'='
string|"' | '"
op|'.'
name|'join'
op|'('
name|'pipeline'
op|')'
newline|'\n'
name|'subprocess'
op|'.'
name|'check_call'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Database'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|Mysql
dedent|''
name|'class'
name|'Mysql'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|create
indent|'    '
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
op|'['
string|"'mysqladmin'"
op|','
string|"'-u'"
op|','
string|"'root'"
op|','
string|"'create'"
op|','
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|drop
dedent|''
name|'def'
name|'drop'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
op|'['
string|"'mysqladmin'"
op|','
string|"'-f'"
op|','
string|"'-u'"
op|','
string|"'root'"
op|','
string|"'drop'"
op|','
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dump
dedent|''
name|'def'
name|'dump'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'dump_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
nl|'\n'
string|"'mysqldump -u root %(name)s > %(dump_filename)s'"
nl|'\n'
op|'%'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'dump_filename'"
op|':'
name|'dump_filename'
op|'}'
op|','
nl|'\n'
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Postgresql
dedent|''
dedent|''
name|'class'
name|'Postgresql'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|create
indent|'    '
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
op|'['
string|"'createdb'"
op|','
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|drop
dedent|''
name|'def'
name|'drop'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
op|'['
string|"'dropdb'"
op|','
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dump
dedent|''
name|'def'
name|'dump'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'dump_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
nl|'\n'
string|"'pg_dump %(name)s > %(dump_filename)s'"
nl|'\n'
op|'%'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'dump_filename'"
op|':'
name|'dump_filename'
op|'}'
op|','
nl|'\n'
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Ibm_db_sa
dedent|''
dedent|''
name|'class'
name|'Ibm_db_sa'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|db2cmd
name|'def'
name|'db2cmd'
op|'('
name|'cls'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wraps a command to be run under the DB2 instance user."""'
newline|'\n'
name|'subprocess'
op|'.'
name|'check_call'
op|'('
string|'\'su - $(db2ilist) -c "%s"\''
op|'%'
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db2cmd'
op|'('
string|"'db2 \\'create database %s\\''"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|drop
dedent|''
name|'def'
name|'drop'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db2cmd'
op|'('
string|"'db2 \\'drop database %s\\''"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dump
dedent|''
name|'def'
name|'dump'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'dump_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db2cmd'
op|'('
string|"'db2look -d %(name)s -e -o %(dump_filename)s'"
op|'%'
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'dump_filename'"
op|':'
name|'dump_filename'
op|'}'
op|')'
newline|'\n'
comment|"# The output file gets dumped to the db2 instance user's home directory"
nl|'\n'
comment|'# so we have to copy it back to our current working directory.'
nl|'\n'
name|'subprocess'
op|'.'
name|'check_call'
op|'('
string|"'cp /home/$(db2ilist)/%s ./'"
op|'%'
name|'dump_filename'
op|','
nl|'\n'
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_db_driver_class
dedent|''
dedent|''
name|'def'
name|'_get_db_driver_class'
op|'('
name|'db_url'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'globals'
op|'('
op|')'
op|'['
name|'db_url'
op|'.'
name|'split'
op|'('
string|"'://'"
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'capitalize'
op|'('
op|')'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"database %s not supported"'
op|')'
op|'%'
name|'db_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Migrate'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|variable|MIGRATE_REPO
dedent|''
dedent|''
name|'MIGRATE_REPO'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
op|','
string|'"nova/db/sqlalchemy/migrate_repo"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_migrate
name|'def'
name|'_migrate'
op|'('
name|'db_url'
op|','
name|'migration_version'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'earliest_version'
op|'='
name|'_migrate_get_earliest_version'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): sqlalchemy-migrate currently cannot handle the skipping of'
nl|'\n'
comment|'# migration numbers.'
nl|'\n'
name|'_migrate_cmd'
op|'('
nl|'\n'
name|'db_url'
op|','
string|"'version_control'"
op|','
name|'str'
op|'('
name|'earliest_version'
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'upgrade_cmd'
op|'='
op|'['
string|"'upgrade'"
op|']'
newline|'\n'
name|'if'
name|'migration_version'
op|'!='
string|"'latest'"
op|':'
newline|'\n'
indent|'        '
name|'upgrade_cmd'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'migration_version'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_migrate_cmd'
op|'('
name|'db_url'
op|','
op|'*'
name|'upgrade_cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_migrate_cmd
dedent|''
name|'def'
name|'_migrate_cmd'
op|'('
name|'db_url'
op|','
op|'*'
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'manage_py'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'MIGRATE_REPO'
op|','
string|"'manage.py'"
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'['
string|"'python'"
op|','
name|'manage_py'
op|']'
newline|'\n'
name|'args'
op|'+='
name|'cmd'
newline|'\n'
name|'args'
op|'+='
op|'['
string|"'--repository=%s'"
op|'%'
name|'MIGRATE_REPO'
op|','
nl|'\n'
string|"'--url=%s'"
op|'%'
name|'db_url'
op|']'
newline|'\n'
nl|'\n'
name|'subprocess'
op|'.'
name|'check_call'
op|'('
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_migrate_get_earliest_version
dedent|''
name|'def'
name|'_migrate_get_earliest_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'versions_glob'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'MIGRATE_REPO'
op|','
string|"'versions'"
op|','
string|"'???_*.py'"
op|')'
newline|'\n'
nl|'\n'
name|'versions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'path'
name|'in'
name|'glob'
op|'.'
name|'iglob'
op|'('
name|'versions_glob'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'path'
op|')'
newline|'\n'
name|'prefix'
op|'='
name|'filename'
op|'.'
name|'split'
op|'('
string|"'_'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'int'
op|'('
name|'prefix'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'versions'
op|'.'
name|'append'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'versions'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'versions'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Git'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|git_current_branch_name
dedent|''
name|'def'
name|'git_current_branch_name'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ref_name'
op|'='
name|'git_symbolic_ref'
op|'('
string|"'HEAD'"
op|','
name|'quiet'
op|'='
name|'True'
op|')'
newline|'\n'
name|'current_branch_name'
op|'='
name|'ref_name'
op|'.'
name|'replace'
op|'('
string|"'refs/heads/'"
op|','
string|"''"
op|')'
newline|'\n'
name|'return'
name|'current_branch_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|git_symbolic_ref
dedent|''
name|'def'
name|'git_symbolic_ref'
op|'('
name|'ref'
op|','
name|'quiet'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'args'
op|'='
op|'['
string|"'git'"
op|','
string|"'symbolic-ref'"
op|','
name|'ref'
op|']'
newline|'\n'
name|'if'
name|'quiet'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'.'
name|'append'
op|'('
string|"'-q'"
op|')'
newline|'\n'
dedent|''
name|'proc'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'args'
op|','
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|')'
newline|'\n'
name|'stdout'
op|','
name|'stderr'
op|'='
name|'proc'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
name|'return'
name|'stdout'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|git_checkout
dedent|''
name|'def'
name|'git_checkout'
op|'('
name|'branch_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'subprocess'
op|'.'
name|'check_call'
op|'('
op|'['
string|"'git'"
op|','
string|"'checkout'"
op|','
name|'branch_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|git_has_uncommited_changes
dedent|''
name|'def'
name|'git_has_uncommited_changes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|"'git'"
op|','
string|"'diff'"
op|','
string|"'--quiet'"
op|','
string|"'--exit-code'"
op|']'
op|')'
op|'=='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Command'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|die
dedent|''
name|'def'
name|'die'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
op|'('
string|'"ERROR: %s"'
op|'%'
name|'msg'
op|','
name|'file'
op|'='
name|'sys'
op|'.'
name|'stderr'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|usage
dedent|''
name|'def'
name|'usage'
op|'('
name|'msg'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'msg'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|'"ERROR: %s"'
op|'%'
name|'msg'
op|','
name|'file'
op|'='
name|'sys'
op|'.'
name|'stderr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'prog'
op|'='
string|'"schema_diff.py"'
newline|'\n'
name|'args'
op|'='
op|'['
string|'"<db-url>"'
op|','
string|'"<orig-branch:orig-version>"'
op|','
nl|'\n'
string|'"<new-branch:new-version>"'
op|']'
newline|'\n'
nl|'\n'
name|'print'
op|'('
string|'"usage: %s %s"'
op|'%'
op|'('
name|'prog'
op|','
string|"' '"
op|'.'
name|'join'
op|'('
name|'args'
op|')'
op|')'
op|','
name|'file'
op|'='
name|'sys'
op|'.'
name|'stderr'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_options
dedent|''
name|'def'
name|'parse_options'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'db_url'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'('
string|'"must specify DB connection url"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'orig_branch'
op|','
name|'orig_version'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'2'
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'('
string|"'original branch and version required (e.g. master:82)'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'new_branch'
op|','
name|'new_version'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'3'
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'('
string|"'new branch and version required (e.g. master:82)'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db_url'
op|','
name|'orig_branch'
op|','
name|'orig_version'
op|','
name|'new_branch'
op|','
name|'new_version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
string|'"%Y%m%d_%H%M%S"'
op|')'
newline|'\n'
nl|'\n'
name|'ORIG_DB'
op|'='
string|"'orig_db_%s'"
op|'%'
name|'timestamp'
newline|'\n'
name|'NEW_DB'
op|'='
string|"'new_db_%s'"
op|'%'
name|'timestamp'
newline|'\n'
nl|'\n'
name|'ORIG_DUMP'
op|'='
name|'ORIG_DB'
op|'+'
string|'".dump"'
newline|'\n'
name|'NEW_DUMP'
op|'='
name|'NEW_DB'
op|'+'
string|'".dump"'
newline|'\n'
nl|'\n'
name|'options'
op|'='
name|'parse_options'
op|'('
op|')'
newline|'\n'
name|'db_url'
op|','
name|'orig_branch'
op|','
name|'orig_version'
op|','
name|'new_branch'
op|','
name|'new_version'
op|'='
name|'options'
newline|'\n'
nl|'\n'
comment|"# Since we're going to be switching branches, ensure user doesn't have any"
nl|'\n'
comment|'# uncommitted changes'
nl|'\n'
name|'if'
name|'git_has_uncommited_changes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'die'
op|'('
string|'"You have uncommitted changes. Please commit them before running "'
nl|'\n'
string|'"this command."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db_driver'
op|'='
name|'_get_db_driver_class'
op|'('
name|'db_url'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'users_branch'
op|'='
name|'git_current_branch_name'
op|'('
op|')'
newline|'\n'
name|'git_checkout'
op|'('
name|'orig_branch'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Dump Original Schema'
nl|'\n'
indent|'        '
name|'dump_db'
op|'('
name|'db_driver'
op|','
name|'ORIG_DB'
op|','
name|'db_url'
op|','
name|'orig_version'
op|','
name|'ORIG_DUMP'
op|')'
newline|'\n'
nl|'\n'
comment|'# Dump New Schema'
nl|'\n'
name|'git_checkout'
op|'('
name|'new_branch'
op|')'
newline|'\n'
name|'dump_db'
op|'('
name|'db_driver'
op|','
name|'NEW_DB'
op|','
name|'db_url'
op|','
name|'new_version'
op|','
name|'NEW_DUMP'
op|')'
newline|'\n'
nl|'\n'
name|'diff_files'
op|'('
name|'ORIG_DUMP'
op|','
name|'NEW_DUMP'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'git_checkout'
op|'('
name|'users_branch'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ORIG_DUMP'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'ORIG_DUMP'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'NEW_DUMP'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'NEW_DUMP'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
