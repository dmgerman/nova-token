begin_unit
comment|'# Copyright 2012 SINA Corporation'
nl|'\n'
comment|'# Copyright 2014 Cisco Systems, Inc.'
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
comment|'#'
nl|'\n'
nl|'\n'
string|'"""Extracts OpenStack config option info from module(s)."""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'print_function'
newline|'\n'
nl|'\n'
name|'import'
name|'argparse'
newline|'\n'
name|'import'
name|'imp'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'textwrap'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'stevedore'
op|'.'
name|'named'
newline|'\n'
nl|'\n'
DECL|variable|STROPT
name|'STROPT'
op|'='
string|'"StrOpt"'
newline|'\n'
DECL|variable|BOOLOPT
name|'BOOLOPT'
op|'='
string|'"BoolOpt"'
newline|'\n'
DECL|variable|INTOPT
name|'INTOPT'
op|'='
string|'"IntOpt"'
newline|'\n'
DECL|variable|FLOATOPT
name|'FLOATOPT'
op|'='
string|'"FloatOpt"'
newline|'\n'
DECL|variable|LISTOPT
name|'LISTOPT'
op|'='
string|'"ListOpt"'
newline|'\n'
DECL|variable|DICTOPT
name|'DICTOPT'
op|'='
string|'"DictOpt"'
newline|'\n'
DECL|variable|MULTISTROPT
name|'MULTISTROPT'
op|'='
string|'"MultiStrOpt"'
newline|'\n'
nl|'\n'
DECL|variable|OPT_TYPES
name|'OPT_TYPES'
op|'='
op|'{'
nl|'\n'
name|'STROPT'
op|':'
string|"'string value'"
op|','
nl|'\n'
name|'BOOLOPT'
op|':'
string|"'boolean value'"
op|','
nl|'\n'
name|'INTOPT'
op|':'
string|"'integer value'"
op|','
nl|'\n'
name|'FLOATOPT'
op|':'
string|"'floating point value'"
op|','
nl|'\n'
name|'LISTOPT'
op|':'
string|"'list value'"
op|','
nl|'\n'
name|'DICTOPT'
op|':'
string|"'dict value'"
op|','
nl|'\n'
name|'MULTISTROPT'
op|':'
string|"'multi valued'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|OPTION_REGEX
name|'OPTION_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"(%s)"'
op|'%'
string|'"|"'
op|'.'
name|'join'
op|'('
op|'['
name|'STROPT'
op|','
name|'BOOLOPT'
op|','
name|'INTOPT'
op|','
nl|'\n'
name|'FLOATOPT'
op|','
name|'LISTOPT'
op|','
name|'DICTOPT'
op|','
nl|'\n'
name|'MULTISTROPT'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|PY_EXT
name|'PY_EXT'
op|'='
string|'".py"'
newline|'\n'
DECL|variable|BASEDIR
name|'BASEDIR'
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
string|'"../../../../"'
op|')'
op|')'
newline|'\n'
DECL|variable|WORDWRAP_WIDTH
name|'WORDWRAP_WIDTH'
op|'='
number|'60'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|raise_extension_exception
name|'def'
name|'raise_extension_exception'
op|'('
name|'extmanager'
op|','
name|'ep'
op|','
name|'err'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate
dedent|''
name|'def'
name|'generate'
op|'('
name|'argv'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'parser'
op|'='
name|'argparse'
op|'.'
name|'ArgumentParser'
op|'('
nl|'\n'
name|'description'
op|'='
string|"'generate sample configuration file'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-m'"
op|','
name|'dest'
op|'='
string|"'modules'"
op|','
name|'action'
op|'='
string|"'append'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'-l'"
op|','
name|'dest'
op|'='
string|"'libraries'"
op|','
name|'action'
op|'='
string|"'append'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'srcfiles'"
op|','
name|'nargs'
op|'='
string|"'*'"
op|')'
newline|'\n'
name|'parsed_args'
op|'='
name|'parser'
op|'.'
name|'parse_args'
op|'('
name|'argv'
op|')'
newline|'\n'
nl|'\n'
name|'mods_by_pkg'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'filepath'
name|'in'
name|'parsed_args'
op|'.'
name|'srcfiles'
op|':'
newline|'\n'
indent|'        '
name|'pkg_name'
op|'='
name|'filepath'
op|'.'
name|'split'
op|'('
name|'os'
op|'.'
name|'sep'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'mod_str'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
string|"'.'"
op|'.'
name|'join'
op|'('
name|'filepath'
op|'.'
name|'split'
op|'('
name|'os'
op|'.'
name|'sep'
op|')'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'filepath'
op|')'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'mods_by_pkg'
op|'.'
name|'setdefault'
op|'('
name|'pkg_name'
op|','
name|'list'
op|'('
op|')'
op|')'
op|'.'
name|'append'
op|'('
name|'mod_str'
op|')'
newline|'\n'
comment|'# NOTE(lzyeval): place top level modules before packages'
nl|'\n'
dedent|''
name|'pkg_names'
op|'='
name|'sorted'
op|'('
name|'pkg'
name|'for'
name|'pkg'
name|'in'
name|'mods_by_pkg'
name|'if'
name|'pkg'
op|'.'
name|'endswith'
op|'('
name|'PY_EXT'
op|')'
op|')'
newline|'\n'
name|'ext_names'
op|'='
name|'sorted'
op|'('
name|'pkg'
name|'for'
name|'pkg'
name|'in'
name|'mods_by_pkg'
name|'if'
name|'pkg'
name|'not'
name|'in'
name|'pkg_names'
op|')'
newline|'\n'
name|'pkg_names'
op|'.'
name|'extend'
op|'('
name|'ext_names'
op|')'
newline|'\n'
nl|'\n'
comment|'# opts_by_group is a mapping of group name to an options list'
nl|'\n'
comment|'# The options list is a list of (module, options) tuples'
nl|'\n'
name|'opts_by_group'
op|'='
op|'{'
string|"'DEFAULT'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'parsed_args'
op|'.'
name|'modules'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'module_name'
name|'in'
name|'parsed_args'
op|'.'
name|'modules'
op|':'
newline|'\n'
indent|'            '
name|'module'
op|'='
name|'_import_module'
op|'('
name|'module_name'
op|')'
newline|'\n'
name|'if'
name|'module'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'group'
op|','
name|'opts'
name|'in'
name|'_list_opts'
op|'('
name|'module'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'opts_by_group'
op|'.'
name|'setdefault'
op|'('
name|'group'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'append'
op|'('
op|'('
name|'module_name'
op|','
nl|'\n'
name|'opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Look for entry points defined in libraries (or applications) for'
nl|'\n'
comment|'# option discovery, and include their return values in the output.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Each entry point should be a function returning an iterable'
nl|'\n'
comment|'# of pairs with the group name (or None for the default group)'
nl|'\n'
comment|'# and the list of Opt instances for that group.'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'parsed_args'
op|'.'
name|'libraries'
op|':'
newline|'\n'
indent|'        '
name|'loader'
op|'='
name|'stevedore'
op|'.'
name|'named'
op|'.'
name|'NamedExtensionManager'
op|'('
nl|'\n'
string|"'oslo_config.opts'"
op|','
nl|'\n'
name|'names'
op|'='
name|'list'
op|'('
name|'set'
op|'('
name|'parsed_args'
op|'.'
name|'libraries'
op|')'
op|')'
op|','
nl|'\n'
name|'invoke_on_load'
op|'='
name|'False'
op|','
nl|'\n'
name|'on_load_failure_callback'
op|'='
name|'raise_extension_exception'
nl|'\n'
op|')'
newline|'\n'
name|'for'
name|'ext'
name|'in'
name|'loader'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'group'
op|','
name|'opts'
name|'in'
name|'ext'
op|'.'
name|'plugin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'opt_list'
op|'='
name|'opts_by_group'
op|'.'
name|'setdefault'
op|'('
name|'group'
name|'or'
string|"'DEFAULT'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'opt_list'
op|'.'
name|'append'
op|'('
op|'('
name|'ext'
op|'.'
name|'name'
op|','
name|'opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'pkg_name'
name|'in'
name|'pkg_names'
op|':'
newline|'\n'
indent|'        '
name|'mods'
op|'='
name|'mods_by_pkg'
op|'.'
name|'get'
op|'('
name|'pkg_name'
op|')'
newline|'\n'
name|'mods'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'mod_str'
name|'in'
name|'mods'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'mod_str'
op|'.'
name|'endswith'
op|'('
string|"'.__init__'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'mod_str'
op|'='
name|'mod_str'
op|'['
op|':'
name|'mod_str'
op|'.'
name|'rfind'
op|'('
string|'"."'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'mod_obj'
op|'='
name|'_import_module'
op|'('
name|'mod_str'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'mod_obj'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'RuntimeError'
op|'('
string|'"Unable to import module %s"'
op|'%'
name|'mod_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'group'
op|','
name|'opts'
name|'in'
name|'_list_opts'
op|'('
name|'mod_obj'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'opts_by_group'
op|'.'
name|'setdefault'
op|'('
name|'group'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'append'
op|'('
op|'('
name|'mod_str'
op|','
name|'opts'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'print_group_opts'
op|'('
string|"'DEFAULT'"
op|','
name|'opts_by_group'
op|'.'
name|'pop'
op|'('
string|"'DEFAULT'"
op|','
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'group'
name|'in'
name|'sorted'
op|'('
name|'opts_by_group'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print_group_opts'
op|'('
name|'group'
op|','
name|'opts_by_group'
op|'['
name|'group'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_import_module
dedent|''
dedent|''
name|'def'
name|'_import_module'
op|'('
name|'mod_str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'mod_str'
op|'.'
name|'startswith'
op|'('
string|"'bin.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'imp'
op|'.'
name|'load_source'
op|'('
name|'mod_str'
op|'['
number|'4'
op|':'
op|']'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'bin'"
op|','
name|'mod_str'
op|'['
number|'4'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'sys'
op|'.'
name|'modules'
op|'['
name|'mod_str'
op|'['
number|'4'
op|':'
op|']'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'mod_str'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'"Error importing module %s: %s\\n"'
op|'%'
op|'('
name|'mod_str'
op|','
name|'str'
op|'('
name|'e'
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_in_group
dedent|''
dedent|''
name|'def'
name|'_is_in_group'
op|'('
name|'opt'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"Check if opt is in group."'
newline|'\n'
name|'for'
name|'value'
name|'in'
name|'group'
op|'.'
name|'_opts'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(llu): Temporary workaround for bug #1262148, wait until'
nl|'\n'
comment|"# newly released oslo.config support '==' operator."
nl|'\n'
indent|'        '
name|'if'
name|'not'
op|'('
name|'value'
op|'['
string|"'opt'"
op|']'
op|'!='
name|'opt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_guess_groups
dedent|''
name|'def'
name|'_guess_groups'
op|'('
name|'opt'
op|','
name|'mod_obj'
op|')'
op|':'
newline|'\n'
comment|'# is it in the DEFAULT group?'
nl|'\n'
indent|'    '
name|'if'
name|'_is_in_group'
op|'('
name|'opt'
op|','
name|'cfg'
op|'.'
name|'CONF'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'DEFAULT'"
newline|'\n'
nl|'\n'
comment|'# what other groups is it in?'
nl|'\n'
dedent|''
name|'for'
name|'value'
name|'in'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'GroupAttr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'_is_in_group'
op|'('
name|'opt'
op|','
name|'value'
op|'.'
name|'_group'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'value'
op|'.'
name|'_group'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
string|'"Unable to find group for option %s, "'
nl|'\n'
string|'"maybe it\'s defined twice in the same group?"'
nl|'\n'
op|'%'
name|'opt'
op|'.'
name|'name'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_list_opts
dedent|''
name|'def'
name|'_list_opts'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
DECL|function|is_opt
indent|'    '
name|'def'
name|'is_opt'
op|'('
name|'o'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'isinstance'
op|'('
name|'o'
op|','
name|'cfg'
op|'.'
name|'Opt'
op|')'
name|'and'
nl|'\n'
name|'not'
name|'isinstance'
op|'('
name|'o'
op|','
name|'cfg'
op|'.'
name|'SubCommandOpt'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'opts'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
name|'for'
name|'attr_str'
name|'in'
name|'dir'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attr_obj'
op|'='
name|'getattr'
op|'('
name|'obj'
op|','
name|'attr_str'
op|')'
newline|'\n'
name|'if'
name|'is_opt'
op|'('
name|'attr_obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'opts'
op|'.'
name|'append'
op|'('
name|'attr_obj'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'isinstance'
op|'('
name|'attr_obj'
op|','
name|'list'
op|')'
name|'and'
nl|'\n'
name|'all'
op|'('
name|'map'
op|'('
name|'lambda'
name|'x'
op|':'
name|'is_opt'
op|'('
name|'x'
op|')'
op|','
name|'attr_obj'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'opts'
op|'.'
name|'extend'
op|'('
name|'attr_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'opt'
name|'in'
name|'opts'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'.'
name|'setdefault'
op|'('
name|'_guess_groups'
op|'('
name|'opt'
op|','
name|'obj'
op|')'
op|','
op|'['
op|']'
op|')'
op|'.'
name|'append'
op|'('
name|'opt'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|print_group_opts
dedent|''
name|'def'
name|'print_group_opts'
op|'('
name|'group'
op|','
name|'opts_by_module'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
op|'('
string|'"[%s]"'
op|'%'
name|'group'
op|')'
newline|'\n'
name|'print'
op|'('
string|"''"
op|')'
newline|'\n'
name|'for'
name|'mod'
op|','
name|'opts'
name|'in'
name|'opts_by_module'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|"'#'"
op|')'
newline|'\n'
name|'print'
op|'('
string|"'# Options defined in %s'"
op|'%'
name|'mod'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#'"
op|')'
newline|'\n'
name|'print'
op|'('
string|"''"
op|')'
newline|'\n'
name|'for'
name|'opt'
name|'in'
name|'opts'
op|':'
newline|'\n'
indent|'            '
name|'_print_opt'
op|'('
name|'opt'
op|')'
newline|'\n'
dedent|''
name|'print'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
dedent|''
dedent|''
name|'def'
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'8.8.8.8'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_sanitize_default
dedent|''
dedent|''
name|'def'
name|'_sanitize_default'
op|'('
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set up a reasonably sensible default for pybasedir, my_ip and host."""'
newline|'\n'
name|'if'
name|'value'
op|'.'
name|'startswith'
op|'('
name|'sys'
op|'.'
name|'prefix'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(jd) Don't use os.path.join, because it is likely to think the"
nl|'\n'
comment|'# second part is an absolute pathname and therefore drop the first'
nl|'\n'
comment|'# part.'
nl|'\n'
indent|'        '
name|'value'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
string|'"/usr/"'
op|'+'
name|'value'
op|'['
name|'len'
op|'('
name|'sys'
op|'.'
name|'prefix'
op|')'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'.'
name|'startswith'
op|'('
name|'BASEDIR'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
op|'.'
name|'replace'
op|'('
name|'BASEDIR'
op|','
string|"'/usr/lib/python/site-packages'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'BASEDIR'
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
op|'.'
name|'replace'
op|'('
name|'BASEDIR'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'=='
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'10.0.0.1'"
newline|'\n'
dedent|''
name|'elif'
name|'value'
name|'in'
op|'('
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
name|'socket'
op|'.'
name|'getfqdn'
op|'('
op|')'
op|')'
name|'and'
string|"'host'"
name|'in'
name|'name'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'nova'"
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'.'
name|'strip'
op|'('
op|')'
op|'!='
name|'value'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'\'"%s"\''
op|'%'
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_print_opt
dedent|''
name|'def'
name|'_print_opt'
op|'('
name|'opt'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'opt_name'
op|','
name|'opt_default'
op|','
name|'opt_help'
op|'='
name|'opt'
op|'.'
name|'dest'
op|','
name|'opt'
op|'.'
name|'default'
op|','
name|'opt'
op|'.'
name|'help'
newline|'\n'
name|'if'
name|'not'
name|'opt_help'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'\'WARNING: "%s" is missing help string.\\n\''
op|'%'
name|'opt_name'
op|')'
newline|'\n'
name|'opt_help'
op|'='
string|'""'
newline|'\n'
dedent|''
name|'opt_type'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'opt_type'
op|'='
name|'OPTION_REGEX'
op|'.'
name|'search'
op|'('
name|'str'
op|'('
name|'type'
op|'('
name|'opt'
op|')'
op|')'
op|')'
op|'.'
name|'group'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'AttributeError'
op|')'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'"%s\\n"'
op|'%'
name|'str'
op|'('
name|'err'
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
dedent|''
name|'opt_help'
op|'='
string|"u'%s (%s)'"
op|'%'
op|'('
name|'opt_help'
op|','
nl|'\n'
name|'OPT_TYPES'
op|'['
name|'opt_type'
op|']'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#'"
op|','
string|'"\\n# "'
op|'.'
name|'join'
op|'('
name|'textwrap'
op|'.'
name|'wrap'
op|'('
name|'opt_help'
op|','
name|'WORDWRAP_WIDTH'
op|')'
op|')'
op|')'
newline|'\n'
name|'if'
name|'opt'
op|'.'
name|'deprecated_opts'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'deprecated_opt'
name|'in'
name|'opt'
op|'.'
name|'deprecated_opts'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'deprecated_opt'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'deprecated_group'
op|'='
op|'('
name|'deprecated_opt'
op|'.'
name|'group'
name|'if'
nl|'\n'
name|'deprecated_opt'
op|'.'
name|'group'
name|'else'
string|'"DEFAULT"'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'# Deprecated group/name - [%s]/%s'"
op|'%'
nl|'\n'
op|'('
name|'deprecated_group'
op|','
nl|'\n'
name|'deprecated_opt'
op|'.'
name|'name'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'opt_default'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
string|"'#%s=<None>'"
op|'%'
name|'opt_name'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'STROPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
name|'_sanitize_default'
op|'('
name|'opt_name'
op|','
nl|'\n'
name|'opt_default'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'BOOLOPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'bool'
op|')'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
name|'str'
op|'('
name|'opt_default'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'INTOPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'int'
op|')'
name|'and'
nl|'\n'
name|'not'
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'bool'
op|')'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
name|'opt_default'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'FLOATOPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'float'
op|')'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
name|'opt_default'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'LISTOPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'list'
op|')'
op|')'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
string|"','"
op|'.'
name|'join'
op|'('
name|'opt_default'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'DICTOPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'dict'
op|')'
op|')'
newline|'\n'
name|'opt_default_strlist'
op|'='
op|'['
name|'str'
op|'('
name|'key'
op|')'
op|'+'
string|"':'"
op|'+'
name|'str'
op|'('
name|'value'
op|')'
nl|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'opt_default'
op|'.'
name|'items'
op|'('
op|')'
op|']'
newline|'\n'
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
string|"','"
op|'.'
name|'join'
op|'('
name|'opt_default_strlist'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'opt_type'
op|'=='
name|'MULTISTROPT'
op|':'
newline|'\n'
indent|'            '
name|'assert'
op|'('
name|'isinstance'
op|'('
name|'opt_default'
op|','
name|'list'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'opt_default'
op|':'
newline|'\n'
indent|'                '
name|'opt_default'
op|'='
op|'['
string|"''"
op|']'
newline|'\n'
dedent|''
name|'for'
name|'default'
name|'in'
name|'opt_default'
op|':'
newline|'\n'
indent|'                '
name|'print'
op|'('
string|"'#%s=%s'"
op|'%'
op|'('
name|'opt_name'
op|','
name|'default'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'print'
op|'('
string|"''"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'\'Error in option "%s"\\n\''
op|'%'
name|'opt_name'
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
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'generate'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
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
