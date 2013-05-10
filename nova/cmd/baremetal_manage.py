begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
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
comment|'# Interactive shell based on Django:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 2005, the Lawrence Journal-World'
nl|'\n'
comment|'# All rights reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Redistribution and use in source and binary forms, with or without'
nl|'\n'
comment|'# modification, are permitted provided that the following conditions are met:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     1. Redistributions of source code must retain the above copyright notice,'
nl|'\n'
comment|'#        this list of conditions and the following disclaimer.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     2. Redistributions in binary form must reproduce the above copyright'
nl|'\n'
comment|'#        notice, this list of conditions and the following disclaimer in the'
nl|'\n'
comment|'#        documentation and/or other materials provided with the distribution.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     3. Neither the name of Django nor the names of its contributors may be'
nl|'\n'
comment|'#        used to endorse or promote products derived from this software without'
nl|'\n'
comment|'#        specific prior written permission.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS'
nl|'\n'
comment|'# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT'
nl|'\n'
comment|'# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR'
nl|'\n'
comment|'# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT'
nl|'\n'
comment|'# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,'
nl|'\n'
comment|'# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT'
nl|'\n'
comment|'# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,'
nl|'\n'
comment|'# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY'
nl|'\n'
comment|'# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT'
nl|'\n'
comment|'# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE'
nl|'\n'
comment|'# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\n  CLI interface for nova bare-metal management.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cliutils'
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
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'migration'
name|'as'
name|'bmdb_migration'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Decorators for actions'
nl|'\n'
DECL|function|args
name|'def'
name|'args'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
DECL|function|_decorator
indent|'    '
name|'def'
name|'_decorator'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'.'
name|'__dict__'
op|'.'
name|'setdefault'
op|'('
string|"'args'"
op|','
op|'['
op|']'
op|')'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
op|'('
name|'args'
op|','
name|'kwargs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'func'
newline|'\n'
dedent|''
name|'return'
name|'_decorator'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalDbCommands
dedent|''
name|'class'
name|'BareMetalDbCommands'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for managing the bare-metal database."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'args'
op|'('
string|"'--version'"
op|','
name|'dest'
op|'='
string|"'version'"
op|','
name|'metavar'
op|'='
string|"'<version>'"
op|','
nl|'\n'
name|'help'
op|'='
string|"'Bare-metal Database version'"
op|')'
newline|'\n'
DECL|member|sync
name|'def'
name|'sync'
op|'('
name|'self'
op|','
name|'version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sync the database up to the most recent version."""'
newline|'\n'
name|'bmdb_migration'
op|'.'
name|'db_sync'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|version
dedent|''
name|'def'
name|'version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Print the current database version."""'
newline|'\n'
name|'v'
op|'='
name|'bmdb_migration'
op|'.'
name|'db_version'
op|'('
op|')'
newline|'\n'
name|'print'
op|'('
name|'v'
op|')'
newline|'\n'
comment|'# return for unittest'
nl|'\n'
name|'return'
name|'v'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CATEGORIES
dedent|''
dedent|''
name|'CATEGORIES'
op|'='
op|'{'
nl|'\n'
string|"'db'"
op|':'
name|'BareMetalDbCommands'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|methods_of
name|'def'
name|'methods_of'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all callable methods of an object that don\'t start with underscore\n    returns a list of tuples of the form (method_name, method)"""'
newline|'\n'
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'dir'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'callable'
op|'('
name|'getattr'
op|'('
name|'obj'
op|','
name|'i'
op|')'
op|')'
name|'and'
name|'not'
name|'i'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'append'
op|'('
op|'('
name|'i'
op|','
name|'getattr'
op|'('
name|'obj'
op|','
name|'i'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_command_parsers
dedent|''
name|'def'
name|'add_command_parsers'
op|'('
name|'subparsers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'parser'
op|'='
name|'subparsers'
op|'.'
name|'add_parser'
op|'('
string|"'bash-completion'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'query_category'"
op|','
name|'nargs'
op|'='
string|"'?'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'category'
name|'in'
name|'CATEGORIES'
op|':'
newline|'\n'
indent|'        '
name|'command_object'
op|'='
name|'CATEGORIES'
op|'['
name|'category'
op|']'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'parser'
op|'='
name|'subparsers'
op|'.'
name|'add_parser'
op|'('
name|'category'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'set_defaults'
op|'('
name|'command_object'
op|'='
name|'command_object'
op|')'
newline|'\n'
nl|'\n'
name|'category_subparsers'
op|'='
name|'parser'
op|'.'
name|'add_subparsers'
op|'('
name|'dest'
op|'='
string|"'action'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'action'
op|','
name|'action_fn'
op|')'
name|'in'
name|'methods_of'
op|'('
name|'command_object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parser'
op|'='
name|'category_subparsers'
op|'.'
name|'add_parser'
op|'('
name|'action'
op|')'
newline|'\n'
nl|'\n'
name|'action_kwargs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'args'
op|','
name|'kwargs'
name|'in'
name|'getattr'
op|'('
name|'action_fn'
op|','
string|"'args'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'action_kwargs'
op|'.'
name|'append'
op|'('
name|'kwargs'
op|'['
string|"'dest'"
op|']'
op|')'
newline|'\n'
name|'kwargs'
op|'['
string|"'dest'"
op|']'
op|'='
string|"'action_kwarg_'"
op|'+'
name|'kwargs'
op|'['
string|"'dest'"
op|']'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'parser'
op|'.'
name|'set_defaults'
op|'('
name|'action_fn'
op|'='
name|'action_fn'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'set_defaults'
op|'('
name|'action_kwargs'
op|'='
name|'action_kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'action_args'"
op|','
name|'nargs'
op|'='
string|"'*'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|category_opt
dedent|''
dedent|''
dedent|''
name|'category_opt'
op|'='
name|'cfg'
op|'.'
name|'SubCommandOpt'
op|'('
string|"'category'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Command categories'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Available categories'"
op|','
nl|'\n'
DECL|variable|handler
name|'handler'
op|'='
name|'add_command_parsers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse options and call the appropriate class/method."""'
newline|'\n'
name|'CONF'
op|'.'
name|'register_cli_opt'
op|'('
name|'category_opt'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cfg'
op|'.'
name|'ConfigFilesNotFoundError'
op|':'
newline|'\n'
indent|'        '
name|'cfgfile'
op|'='
name|'CONF'
op|'.'
name|'config_file'
op|'['
op|'-'
number|'1'
op|']'
name|'if'
name|'CONF'
op|'.'
name|'config_file'
name|'else'
name|'None'
newline|'\n'
name|'if'
name|'cfgfile'
name|'and'
name|'not'
name|'os'
op|'.'
name|'access'
op|'('
name|'cfgfile'
op|','
name|'os'
op|'.'
name|'R_OK'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'st'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'cfgfile'
op|')'
newline|'\n'
name|'print'
op|'('
name|'_'
op|'('
string|'"Could not read %s. Re-running with sudo"'
op|')'
op|'%'
name|'cfgfile'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'execvp'
op|'('
string|"'sudo'"
op|','
op|'['
string|"'sudo'"
op|','
string|"'-u'"
op|','
string|"'#%s'"
op|'%'
name|'st'
op|'.'
name|'st_uid'
op|']'
op|'+'
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'print'
op|'('
name|'_'
op|'('
string|"'sudo failed, continuing as if nothing happened'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'print'
op|'('
name|'_'
op|'('
string|"'Please re-run nova-manage as root.'"
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
number|'2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'name'
op|'=='
string|'"version"'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'version'
op|'.'
name|'version_string_with_package'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'name'
op|'=='
string|'"bash-completion"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'query_category'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
string|'" "'
op|'.'
name|'join'
op|'('
name|'CATEGORIES'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'query_category'
name|'in'
name|'CATEGORIES'
op|':'
newline|'\n'
indent|'            '
name|'fn'
op|'='
name|'CATEGORIES'
op|'['
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'query_category'
op|']'
newline|'\n'
name|'command_object'
op|'='
name|'fn'
op|'('
op|')'
newline|'\n'
name|'actions'
op|'='
name|'methods_of'
op|'('
name|'command_object'
op|')'
newline|'\n'
name|'print'
op|'('
string|'" "'
op|'.'
name|'join'
op|'('
op|'['
name|'k'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'actions'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fn'
op|'='
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'action_fn'
newline|'\n'
name|'fn_args'
op|'='
op|'['
name|'arg'
op|'.'
name|'decode'
op|'('
string|"'utf-8'"
op|')'
name|'for'
name|'arg'
name|'in'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'action_args'
op|']'
newline|'\n'
name|'fn_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'CONF'
op|'.'
name|'category'
op|'.'
name|'action_kwargs'
op|':'
newline|'\n'
indent|'        '
name|'v'
op|'='
name|'getattr'
op|'('
name|'CONF'
op|'.'
name|'category'
op|','
string|"'action_kwarg_'"
op|'+'
name|'k'
op|')'
newline|'\n'
name|'if'
name|'v'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'v'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
name|'v'
op|'.'
name|'decode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
dedent|''
name|'fn_kwargs'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
comment|'# call the action with the remaining arguments'
nl|'\n'
comment|'# check arguments'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'cliutils'
op|'.'
name|'validate_args'
op|'('
name|'fn'
op|','
op|'*'
name|'fn_args'
op|','
op|'**'
name|'fn_kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'cliutils'
op|'.'
name|'MissingArgs'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'fn'
op|'.'
name|'__doc__'
op|')'
newline|'\n'
name|'print'
op|'('
name|'e'
op|')'
newline|'\n'
name|'return'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'('
op|'*'
name|'fn_args'
op|','
op|'**'
name|'fn_kwargs'
op|')'
newline|'\n'
name|'return'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'_'
op|'('
string|'"Command failed, please check log for more info"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
