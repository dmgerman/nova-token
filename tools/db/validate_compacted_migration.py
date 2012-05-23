begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
string|'"""\nUtility for ensuring DB schemas don\'t change when compacting migrations.\n\nEach release cycle the plan is to compact all of the migrations from that\nrelease into a single file. This is a manual and, unfortunately, error-prone\nprocess. To ensure that the schema doesn\'t change, this tool can be used to\ndiff the compacted DB schema to the original, uncompacted form.\n\nNotes:\n\nThis utility assumes you start off in the branch containing the compacted\nmigration.\n\nRun like:\n\n    ./tools/db/validate_compacted_migration.py mysql 82 master\n"""'
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
comment|'### Dump'
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
name|'compacted_version'
op|','
name|'dump_filename'
op|','
nl|'\n'
name|'latest'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'migrate'
op|'('
name|'db_driver'
op|','
name|'db_name'
op|','
name|'compacted_version'
op|','
name|'latest'
op|'='
name|'latest'
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
comment|'### Diff'
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
op|'%'
name|'locals'
op|'('
op|')'
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
comment|'### Database'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|MySQL
dedent|''
name|'class'
name|'MySQL'
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
op|'%'
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|url
dedent|''
name|'def'
name|'url'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'mysql://root@localhost/%s'"
op|'%'
name|'name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Postgres
dedent|''
dedent|''
name|'class'
name|'Postgres'
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
op|'%'
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|url
dedent|''
name|'def'
name|'url'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'postgres://localhost/%s'"
op|'%'
name|'name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_db_driver_class
dedent|''
dedent|''
name|'def'
name|'_get_db_driver_class'
op|'('
name|'db_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'db_type'
op|'=='
string|'"mysql"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'MySQL'
newline|'\n'
dedent|''
name|'elif'
name|'db_type'
op|'=='
string|'"postgres"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'Postgres'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"database %s not supported"'
op|'%'
name|'db_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'### Migrate'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|migrate
dedent|''
dedent|''
name|'def'
name|'migrate'
op|'('
name|'db_driver'
op|','
name|'db_name'
op|','
name|'compacted_version'
op|','
name|'latest'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): sqlalchemy-migrate currently cannot handle the skipping of'
nl|'\n'
comment|'# migration numbers'
nl|'\n'
indent|'    '
name|'_migrate_cmd'
op|'('
nl|'\n'
name|'db_driver'
op|','
name|'db_name'
op|','
string|"'version_control'"
op|','
name|'str'
op|'('
name|'compacted_version'
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
name|'not'
name|'latest'
op|':'
newline|'\n'
indent|'        '
name|'upgrade_cmd'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'compacted_version'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_migrate_cmd'
op|'('
name|'db_driver'
op|','
name|'db_name'
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
name|'db_driver'
op|','
name|'db_name'
op|','
op|'*'
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'db_driver'
op|'.'
name|'url'
op|'('
name|'db_name'
op|')'
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
comment|'### Git'
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
comment|'### Command'
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
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"ERROR: %s"'
op|'%'
name|'msg'
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
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"ERROR: %s"'
op|'%'
name|'msg'
newline|'\n'
nl|'\n'
dedent|''
name|'prog'
op|'='
string|'"validate_compacted_migration.py"'
newline|'\n'
name|'args'
op|'='
op|'['
string|'"<mysql|postgres>"'
op|','
string|'"<compacted-version>"'
op|','
nl|'\n'
string|'"<uncompacted-branch-name>"'
op|']'
newline|'\n'
nl|'\n'
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
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
name|'db_type'
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
string|'"must specify DB type"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'compacted_version'
op|'='
name|'int'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'2'
op|']'
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
string|"'must specify compacted migration version'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'('
string|"'compacted version must be a number'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'uncompacted_branch_name'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'3'
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
string|"'must specify uncompacted branch name'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db_type'
op|','
name|'compacted_version'
op|','
name|'uncompacted_branch_name'
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
name|'COMPACTED_DB'
op|'='
string|"'compacted'"
newline|'\n'
name|'UNCOMPACTED_DB'
op|'='
string|"'uncompacted'"
newline|'\n'
nl|'\n'
name|'COMPACTED_FILENAME'
op|'='
name|'COMPACTED_DB'
op|'+'
string|'".dump"'
newline|'\n'
name|'UNCOMPACTED_FILENAME'
op|'='
name|'UNCOMPACTED_DB'
op|'+'
string|'".dump"'
newline|'\n'
nl|'\n'
name|'db_type'
op|','
name|'compacted_version'
op|','
name|'uncompacted_branch_name'
op|'='
name|'parse_options'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Since we're going to be switching branches, ensure user doesn't have any"
nl|'\n'
comment|'# uncommited changes'
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
string|'"You have uncommited changes. Please commit them before running "'
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
name|'db_type'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Dump Compacted'
nl|'\n'
name|'dump_db'
op|'('
name|'db_driver'
op|','
name|'COMPACTED_DB'
op|','
name|'compacted_version'
op|','
name|'COMPACTED_FILENAME'
op|')'
newline|'\n'
nl|'\n'
comment|'# Dump Uncompacted'
nl|'\n'
name|'original_branch_name'
op|'='
name|'git_current_branch_name'
op|'('
op|')'
newline|'\n'
name|'git_checkout'
op|'('
name|'uncompacted_branch_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'dump_db'
op|'('
name|'db_driver'
op|','
name|'UNCOMPACTED_DB'
op|','
name|'compacted_version'
op|','
nl|'\n'
name|'UNCOMPACTED_FILENAME'
op|','
name|'latest'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'git_checkout'
op|'('
name|'original_branch_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'diff_files'
op|'('
name|'UNCOMPACTED_FILENAME'
op|','
name|'COMPACTED_FILENAME'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
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
