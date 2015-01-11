begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|path_opts
name|'path_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'pybasedir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
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
string|"'../'"
op|')'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the nova python module is installed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'bindir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'sys'
op|'.'
name|'prefix'
op|','
string|"'local'"
op|','
string|"'bin'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where nova binaries are installed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'state_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$pybasedir'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Top-level directory for maintaining nova\'s state"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'path_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|basedir_def
name|'def'
name|'basedir_def'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an uninterpolated path relative to $pybasedir."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'$pybasedir'"
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bindir_def
dedent|''
name|'def'
name|'bindir_def'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an uninterpolated path relative to $bindir."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'$bindir'"
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|state_path_def
dedent|''
name|'def'
name|'state_path_def'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an uninterpolated path relative to $state_path."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'$state_path'"
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|basedir_rel
dedent|''
name|'def'
name|'basedir_rel'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a path relative to $pybasedir."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'pybasedir'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bindir_rel
dedent|''
name|'def'
name|'bindir_rel'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a path relative to $bindir."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'bindir'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|state_path_rel
dedent|''
name|'def'
name|'state_path_rel'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a path relative to $state_path."""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'state_path'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
