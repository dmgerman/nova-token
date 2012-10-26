begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012, Cloudscaling'
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
string|'"""nova HACKING file compliance testing\n\nbuilt on top of pep8.py\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'fnmatch'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'tokenize'
newline|'\n'
name|'import'
name|'warnings'
newline|'\n'
nl|'\n'
name|'import'
name|'pep8'
newline|'\n'
nl|'\n'
comment|"# Don't need this for testing"
nl|'\n'
name|'logging'
op|'.'
name|'disable'
op|'('
string|"'LOG'"
op|')'
newline|'\n'
nl|'\n'
comment|'#N1xx comments'
nl|'\n'
comment|'#N2xx except'
nl|'\n'
comment|'#N3xx imports'
nl|'\n'
comment|'#N4xx docstrings'
nl|'\n'
comment|'#N5xx dictionaries/lists'
nl|'\n'
comment|'#N6xx calling methods'
nl|'\n'
comment|'#N7xx localization'
nl|'\n'
comment|'#N8xx git commit messages'
nl|'\n'
nl|'\n'
DECL|variable|IMPORT_EXCEPTIONS
name|'IMPORT_EXCEPTIONS'
op|'='
op|'['
string|"'sqlalchemy'"
op|','
string|"'migrate'"
op|','
string|"'nova.db.sqlalchemy.session'"
op|']'
newline|'\n'
DECL|variable|DOCSTRING_TRIPLE
name|'DOCSTRING_TRIPLE'
op|'='
op|'['
string|'\'"""\''
op|','
string|'"\'\'\'"'
op|']'
newline|'\n'
DECL|variable|VERBOSE_MISSING_IMPORT
name|'VERBOSE_MISSING_IMPORT'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'HACKING_VERBOSE_MISSING_IMPORT'"
op|','
string|"'False'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Monkey patch broken excluded filter in pep8'
nl|'\n'
DECL|function|filename_match
name|'def'
name|'filename_match'
op|'('
name|'filename'
op|','
name|'patterns'
op|','
name|'default'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Check if patterns contains a pattern that matches filename.\n    If patterns is unspecified, this always returns True.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'patterns'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'default'
newline|'\n'
dedent|''
name|'return'
name|'any'
op|'('
name|'fnmatch'
op|'.'
name|'fnmatch'
op|'('
name|'filename'
op|','
name|'pattern'
op|')'
name|'for'
name|'pattern'
name|'in'
name|'patterns'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|excluded
dedent|''
name|'def'
name|'excluded'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Check if options.exclude contains a pattern that matches filename.\n    """'
newline|'\n'
name|'basename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'filename'
op|')'
newline|'\n'
name|'return'
name|'any'
op|'('
op|'('
name|'filename_match'
op|'('
name|'filename'
op|','
name|'pep8'
op|'.'
name|'options'
op|'.'
name|'exclude'
op|','
nl|'\n'
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'filename_match'
op|'('
name|'basename'
op|','
name|'pep8'
op|'.'
name|'options'
op|'.'
name|'exclude'
op|','
nl|'\n'
name|'default'
op|'='
name|'False'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|input_dir
dedent|''
name|'def'
name|'input_dir'
op|'('
name|'dirname'
op|','
name|'runner'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Check all Python source files in this directory and all subdirectories.\n    """'
newline|'\n'
name|'dirname'
op|'='
name|'dirname'
op|'.'
name|'rstrip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'if'
name|'excluded'
op|'('
name|'dirname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'runner'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'runner'
op|'='
name|'pep8'
op|'.'
name|'input_file'
newline|'\n'
dedent|''
name|'for'
name|'root'
op|','
name|'dirs'
op|','
name|'files'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'dirname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'pep8'
op|'.'
name|'options'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
string|"'directory '"
op|'+'
name|'root'
op|')'
newline|'\n'
dedent|''
name|'pep8'
op|'.'
name|'options'
op|'.'
name|'counters'
op|'['
string|"'directories'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'dirs'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'subdir'
name|'in'
name|'dirs'
op|'['
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'excluded'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'subdir'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'dirs'
op|'.'
name|'remove'
op|'('
name|'subdir'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'files'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'filename'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pep8'
op|'.'
name|'filename_match'
op|'('
name|'filename'
op|')'
name|'and'
name|'not'
name|'excluded'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pep8'
op|'.'
name|'options'
op|'.'
name|'counters'
op|'['
string|"'files'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'runner'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'filename'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_import_exception
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'is_import_exception'
op|'('
name|'mod'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
name|'mod'
name|'in'
name|'IMPORT_EXCEPTIONS'
name|'or'
nl|'\n'
name|'any'
op|'('
name|'mod'
op|'.'
name|'startswith'
op|'('
name|'m'
op|'+'
string|"'.'"
op|')'
name|'for'
name|'m'
name|'in'
name|'IMPORT_EXCEPTIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_normalize
dedent|''
name|'def'
name|'import_normalize'
op|'('
name|'line'
op|')'
op|':'
newline|'\n'
comment|'# convert "from x import y" to "import x.y"'
nl|'\n'
comment|'# handle "from x import y as z" to "import x.y as z"'
nl|'\n'
indent|'    '
name|'split_line'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
op|'('
string|'"import"'
name|'in'
name|'line'
name|'and'
name|'line'
op|'.'
name|'startswith'
op|'('
string|'"from "'
op|')'
name|'and'
string|'","'
name|'not'
name|'in'
name|'line'
name|'and'
nl|'\n'
name|'split_line'
op|'['
number|'2'
op|']'
op|'=='
string|'"import"'
name|'and'
name|'split_line'
op|'['
number|'3'
op|']'
op|'!='
string|'"*"'
name|'and'
nl|'\n'
name|'split_line'
op|'['
number|'1'
op|']'
op|'!='
string|'"__future__"'
name|'and'
nl|'\n'
op|'('
name|'len'
op|'('
name|'split_line'
op|')'
op|'=='
number|'4'
name|'or'
nl|'\n'
op|'('
name|'len'
op|'('
name|'split_line'
op|')'
op|'=='
number|'6'
name|'and'
name|'split_line'
op|'['
number|'4'
op|']'
op|'=='
string|'"as"'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"import %s.%s"'
op|'%'
op|'('
name|'split_line'
op|'['
number|'1'
op|']'
op|','
name|'split_line'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'line'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_todo_format
dedent|''
dedent|''
name|'def'
name|'nova_todo_format'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for \'TODO()\'.\n\n    nova HACKING guide recommendation for TODO:\n    Include your name with TODOs as in "#TODO(termie)"\n    N101\n    """'
newline|'\n'
name|'pos'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'TODO'"
op|')'
newline|'\n'
name|'pos1'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'TODO('"
op|')'
newline|'\n'
name|'pos2'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'#'"
op|')'
comment|"# make sure it's a comment"
newline|'\n'
name|'if'
op|'('
name|'pos'
op|'!='
name|'pos1'
name|'and'
name|'pos2'
op|'>='
number|'0'
name|'and'
name|'pos2'
op|'<'
name|'pos'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'pos'
op|','
string|'"NOVA N101: Use TODO(NAME)"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_except_format
dedent|''
dedent|''
name|'def'
name|'nova_except_format'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for \'except:\'.\n\n    nova HACKING guide recommends not using except:\n    Do not write "except:", use "except Exception:" at the very least\n    N201\n    """'
newline|'\n'
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"except:"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
number|'6'
op|','
string|'"NOVA N201: no \'except:\' at least use \'except Exception:\'"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_except_format_assert
dedent|''
dedent|''
name|'def'
name|'nova_except_format_assert'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for \'assertRaises(Exception\'.\n\n    nova HACKING guide recommends not using assertRaises(Exception...):\n    Do not use overly broad Exception type\n    N202\n    """'
newline|'\n'
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"self.assertRaises(Exception"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
number|'1'
op|','
string|'"NOVA N202: assertRaises Exception too broad"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_one_import_per_line
dedent|''
dedent|''
name|'def'
name|'nova_one_import_per_line'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for import format.\n\n    nova HACKING guide recommends one import per line:\n    Do not import more than one module per line\n\n    Examples:\n    BAD: from nova.rpc.common import RemoteError, LOG\n    N301\n    """'
newline|'\n'
name|'pos'
op|'='
name|'logical_line'
op|'.'
name|'find'
op|'('
string|"','"
op|')'
newline|'\n'
name|'parts'
op|'='
name|'logical_line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
op|'('
name|'pos'
op|'>'
op|'-'
number|'1'
name|'and'
op|'('
name|'parts'
op|'['
number|'0'
op|']'
op|'=='
string|'"import"'
name|'or'
nl|'\n'
name|'parts'
op|'['
number|'0'
op|']'
op|'=='
string|'"from"'
name|'and'
name|'parts'
op|'['
number|'2'
op|']'
op|'=='
string|'"import"'
op|')'
name|'and'
nl|'\n'
name|'not'
name|'is_import_exception'
op|'('
name|'parts'
op|'['
number|'1'
op|']'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'pos'
op|','
string|'"NOVA N301: one import per line"'
newline|'\n'
nl|'\n'
DECL|variable|_missingImport
dedent|''
dedent|''
name|'_missingImport'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_import_module_only
name|'def'
name|'nova_import_module_only'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for import module only.\n\n    nova HACKING guide recommends importing only modules:\n    Do not import objects, only modules\n    N302 import only modules\n    N303 Invalid Import\n    N304 Relative Import\n    """'
newline|'\n'
DECL|function|importModuleCheck
name|'def'
name|'importModuleCheck'
op|'('
name|'mod'
op|','
name|'parent'
op|'='
name|'None'
op|','
name|'added'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        If can\'t find module on first try, recursively check for relative\n        imports\n        """'
newline|'\n'
name|'current_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'pep8'
op|'.'
name|'current_file'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'warnings'
op|'.'
name|'catch_warnings'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'warnings'
op|'.'
name|'simplefilter'
op|'('
string|"'ignore'"
op|','
name|'DeprecationWarning'
op|')'
newline|'\n'
name|'valid'
op|'='
name|'True'
newline|'\n'
name|'if'
name|'parent'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'is_import_exception'
op|'('
name|'parent'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'return'
newline|'\n'
dedent|''
name|'parent_mod'
op|'='
name|'__import__'
op|'('
name|'parent'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
op|'['
name|'mod'
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'valid'
op|'='
name|'inspect'
op|'.'
name|'ismodule'
op|'('
name|'getattr'
op|'('
name|'parent_mod'
op|','
name|'mod'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'__import__'
op|'('
name|'mod'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
op|'['
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'valid'
op|'='
name|'inspect'
op|'.'
name|'ismodule'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'mod'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'valid'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'added'
op|':'
newline|'\n'
indent|'                        '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'added'
op|'='
name|'False'
newline|'\n'
name|'return'
name|'logical_line'
op|'.'
name|'find'
op|'('
name|'mod'
op|')'
op|','
op|'('
string|'"NOVA N304: No "'
nl|'\n'
string|'"relative  imports. \'%s\' is a relative import"'
nl|'\n'
op|'%'
name|'logical_line'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'logical_line'
op|'.'
name|'find'
op|'('
name|'mod'
op|')'
op|','
op|'('
string|'"NOVA N302: import only "'
nl|'\n'
string|'"modules. \'%s\' does not import a module"'
nl|'\n'
op|'%'
name|'logical_line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
op|'('
name|'ImportError'
op|','
name|'NameError'
op|')'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'added'
op|':'
newline|'\n'
indent|'                '
name|'added'
op|'='
name|'True'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'append'
op|'('
name|'current_path'
op|')'
newline|'\n'
name|'return'
name|'importModuleCheck'
op|'('
name|'mod'
op|','
name|'parent'
op|','
name|'added'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
name|'logical_line'
op|'.'
name|'split'
op|'('
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'name'
name|'not'
name|'in'
name|'_missingImport'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'VERBOSE_MISSING_IMPORT'
op|'!='
string|"'False'"
op|':'
newline|'\n'
indent|'                        '
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
op|'('
string|'"ERROR: import \'%s\' in %s "'
nl|'\n'
string|'"failed: %s"'
op|'%'
nl|'\n'
op|'('
name|'name'
op|','
name|'pep8'
op|'.'
name|'current_file'
op|','
name|'exc'
op|')'
op|')'
newline|'\n'
dedent|''
name|'_missingImport'
op|'.'
name|'add'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'added'
op|'='
name|'False'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|'# Invalid import'
nl|'\n'
indent|'            '
name|'return'
name|'logical_line'
op|'.'
name|'find'
op|'('
name|'mod'
op|')'
op|','
op|'('
string|'"NOVA N303: Invalid import, "'
nl|'\n'
string|'"AttributeError raised"'
op|')'
newline|'\n'
nl|'\n'
comment|'# convert "from x import y" to " import x.y"'
nl|'\n'
comment|'# convert "from x import y as z" to " import x.y"'
nl|'\n'
dedent|''
dedent|''
name|'import_normalize'
op|'('
name|'logical_line'
op|')'
newline|'\n'
name|'split_line'
op|'='
name|'logical_line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"import "'
op|')'
name|'and'
string|'","'
name|'not'
name|'in'
name|'logical_line'
name|'and'
nl|'\n'
op|'('
name|'len'
op|'('
name|'split_line'
op|')'
op|'=='
number|'2'
name|'or'
nl|'\n'
op|'('
name|'len'
op|'('
name|'split_line'
op|')'
op|'=='
number|'4'
name|'and'
name|'split_line'
op|'['
number|'2'
op|']'
op|'=='
string|'"as"'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mod'
op|'='
name|'split_line'
op|'['
number|'1'
op|']'
newline|'\n'
name|'rval'
op|'='
name|'importModuleCheck'
op|'('
name|'mod'
op|')'
newline|'\n'
name|'if'
name|'rval'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'rval'
newline|'\n'
nl|'\n'
comment|'# TODO(jogo) handle "from x import *"'
nl|'\n'
nl|'\n'
comment|'#TODO(jogo): import template: N305'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_import_alphabetical
dedent|''
dedent|''
dedent|''
name|'def'
name|'nova_import_alphabetical'
op|'('
name|'physical_line'
op|','
name|'line_number'
op|','
name|'lines'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for imports in alphabetical order.\n\n    nova HACKING guide recommendation for imports:\n    imports in human alphabetical order\n    N306\n    """'
newline|'\n'
comment|'# handle import x'
nl|'\n'
comment|"# use .lower since capitalization shouldn't dictate order"
nl|'\n'
name|'split_line'
op|'='
name|'import_normalize'
op|'('
name|'physical_line'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'split_previous'
op|'='
name|'import_normalize'
op|'('
name|'lines'
op|'['
name|'line_number'
op|'-'
number|'2'
op|']'
nl|'\n'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
comment|'# with or without "as y"'
nl|'\n'
name|'length'
op|'='
op|'['
number|'2'
op|','
number|'4'
op|']'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'split_line'
op|')'
name|'in'
name|'length'
name|'and'
name|'len'
op|'('
name|'split_previous'
op|')'
name|'in'
name|'length'
name|'and'
nl|'\n'
name|'split_line'
op|'['
number|'0'
op|']'
op|'=='
string|'"import"'
name|'and'
name|'split_previous'
op|'['
number|'0'
op|']'
op|'=='
string|'"import"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'split_line'
op|'['
number|'1'
op|']'
op|'<'
name|'split_previous'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
number|'0'
op|','
string|'"NOVA N306: imports not in alphabetical order (%s, %s)"'
nl|'\n'
op|'%'
op|'('
name|'split_previous'
op|'['
number|'1'
op|']'
op|','
name|'split_line'
op|'['
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_docstring_start_space
dedent|''
dedent|''
dedent|''
name|'def'
name|'nova_docstring_start_space'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for docstring not start with space.\n\n    nova HACKING guide recommendation for docstring:\n    Docstring should not start with space\n    N401\n    """'
newline|'\n'
name|'pos'
op|'='
name|'max'
op|'('
op|'['
name|'physical_line'
op|'.'
name|'find'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'DOCSTRING_TRIPLE'
op|']'
op|')'
comment|'# start'
newline|'\n'
name|'if'
op|'('
name|'pos'
op|'!='
op|'-'
number|'1'
name|'and'
name|'len'
op|'('
name|'physical_line'
op|')'
op|'>'
name|'pos'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'physical_line'
op|'['
name|'pos'
op|'+'
number|'3'
op|']'
op|'=='
string|"' '"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'pos'
op|','
string|'"NOVA N401: one line docstring should not start with"'
nl|'\n'
string|'" a space"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_docstring_one_line
dedent|''
dedent|''
dedent|''
name|'def'
name|'nova_docstring_one_line'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check one line docstring end.\n\n    nova HACKING guide recommendation for one line docstring:\n    A one line docstring looks like this and ends in a period.\n    N402\n    """'
newline|'\n'
name|'pos'
op|'='
name|'max'
op|'('
op|'['
name|'physical_line'
op|'.'
name|'find'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'DOCSTRING_TRIPLE'
op|']'
op|')'
comment|'# start'
newline|'\n'
name|'end'
op|'='
name|'max'
op|'('
op|'['
name|'physical_line'
op|'['
op|'-'
number|'4'
op|':'
op|'-'
number|'1'
op|']'
op|'=='
name|'i'
name|'for'
name|'i'
name|'in'
name|'DOCSTRING_TRIPLE'
op|']'
op|')'
comment|'# end'
newline|'\n'
name|'if'
op|'('
name|'pos'
op|'!='
op|'-'
number|'1'
name|'and'
name|'end'
name|'and'
name|'len'
op|'('
name|'physical_line'
op|')'
op|'>'
name|'pos'
op|'+'
number|'4'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'physical_line'
op|'['
op|'-'
number|'5'
op|']'
op|'!='
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'pos'
op|','
string|'"NOVA N402: one line docstring needs a period"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_docstring_multiline_end
dedent|''
dedent|''
dedent|''
name|'def'
name|'nova_docstring_multiline_end'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check multi line docstring end.\n\n    nova HACKING guide recommendation for docstring:\n    Docstring should end on a new line\n    N403\n    """'
newline|'\n'
name|'pos'
op|'='
name|'max'
op|'('
op|'['
name|'physical_line'
op|'.'
name|'find'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'DOCSTRING_TRIPLE'
op|']'
op|')'
comment|'# start'
newline|'\n'
name|'if'
op|'('
name|'pos'
op|'!='
op|'-'
number|'1'
name|'and'
name|'len'
op|'('
name|'physical_line'
op|')'
op|'=='
name|'pos'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'physical_line'
newline|'\n'
name|'if'
op|'('
name|'physical_line'
op|'['
name|'pos'
op|'+'
number|'3'
op|']'
op|'=='
string|"' '"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'pos'
op|','
string|'"NOVA N403: multi line docstring end on new line"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FORMAT_RE
dedent|''
dedent|''
dedent|''
name|'FORMAT_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"%(?:"'
nl|'\n'
string|'"%|"'
comment|'# Ignore plain percents'
nl|'\n'
string|'"(\\(\\w+\\))?"'
comment|'# mapping key'
nl|'\n'
string|'"([#0 +-]?"'
comment|'# flag'
nl|'\n'
string|'"(?:\\d+|\\*)?"'
comment|'# width'
nl|'\n'
string|'"(?:\\.\\d+)?"'
comment|'# precision'
nl|'\n'
string|'"[hlL]?"'
comment|'# length mod'
nl|'\n'
string|'"\\w))"'
op|')'
comment|'# type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalizationError
name|'class'
name|'LocalizationError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_i18n
dedent|''
name|'def'
name|'check_i18n'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generator that checks token stream for localization errors.\n\n    Expects tokens to be ``send``ed one by one.\n    Raises LocalizationError if some error is found.\n    """'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'token_type'
op|','
name|'text'
op|','
name|'_'
op|','
name|'_'
op|','
name|'line'
op|'='
name|'yield'
newline|'\n'
dedent|''
name|'except'
name|'GeneratorExit'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'token_type'
op|'=='
name|'tokenize'
op|'.'
name|'NAME'
name|'and'
name|'text'
op|'=='
string|'"_"'
name|'and'
nl|'\n'
name|'not'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'def _(msg):'"
op|')'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'token_type'
op|','
name|'text'
op|','
name|'start'
op|','
name|'_'
op|','
name|'_'
op|'='
name|'yield'
newline|'\n'
name|'if'
name|'token_type'
op|'!='
name|'tokenize'
op|'.'
name|'NL'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'token_type'
op|'!='
name|'tokenize'
op|'.'
name|'OP'
name|'or'
name|'text'
op|'!='
string|'"("'
op|':'
newline|'\n'
indent|'                '
name|'continue'
comment|'# not a localization call'
newline|'\n'
nl|'\n'
dedent|''
name|'format_string'
op|'='
string|"''"
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'token_type'
op|','
name|'text'
op|','
name|'start'
op|','
name|'_'
op|','
name|'_'
op|'='
name|'yield'
newline|'\n'
name|'if'
name|'token_type'
op|'=='
name|'tokenize'
op|'.'
name|'STRING'
op|':'
newline|'\n'
indent|'                    '
name|'format_string'
op|'+='
name|'eval'
op|'('
name|'text'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'token_type'
op|'=='
name|'tokenize'
op|'.'
name|'NL'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'format_string'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N701: Empty localization string"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'token_type'
op|'!='
name|'tokenize'
op|'.'
name|'OP'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N701: Invalid localization call"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'text'
op|'!='
string|'")"'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'text'
op|'=='
string|'"%"'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N702: Formatting operation should be outside"'
nl|'\n'
string|'" of localization method call"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'text'
op|'=='
string|'"+"'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N702: Use bare string concatenation instead"'
nl|'\n'
string|'" of +"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N702: Argument to _ must be just a string"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'format_specs'
op|'='
name|'FORMAT_RE'
op|'.'
name|'findall'
op|'('
name|'format_string'
op|')'
newline|'\n'
name|'positional_specs'
op|'='
op|'['
op|'('
name|'key'
op|','
name|'spec'
op|')'
name|'for'
name|'key'
op|','
name|'spec'
name|'in'
name|'format_specs'
nl|'\n'
name|'if'
name|'not'
name|'key'
name|'and'
name|'spec'
op|']'
newline|'\n'
comment|'# not spec means %%, key means %(smth)s'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'positional_specs'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'LocalizationError'
op|'('
name|'start'
op|','
nl|'\n'
string|'"NOVA N703: Multiple positional placeholders"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_localization_strings
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'nova_localization_strings'
op|'('
name|'logical_line'
op|','
name|'tokens'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check localization in line.\n\n    N701: bad localization call\n    N702: complex expression instead of string as argument to _()\n    N703: multiple positional placeholders\n    """'
newline|'\n'
nl|'\n'
name|'gen'
op|'='
name|'check_i18n'
op|'('
op|')'
newline|'\n'
name|'next'
op|'('
name|'gen'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'map'
op|'('
name|'gen'
op|'.'
name|'send'
op|','
name|'tokens'
op|')'
newline|'\n'
name|'gen'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'LocalizationError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'e'
op|'.'
name|'args'
newline|'\n'
nl|'\n'
comment|'#TODO(jogo) Dict and list objects'
nl|'\n'
nl|'\n'
DECL|variable|current_file
dedent|''
dedent|''
name|'current_file'
op|'='
string|'""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|readlines
name|'def'
name|'readlines'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Record the current file being tested."""'
newline|'\n'
name|'pep8'
op|'.'
name|'current_file'
op|'='
name|'filename'
newline|'\n'
name|'return'
name|'open'
op|'('
name|'filename'
op|')'
op|'.'
name|'readlines'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_nova
dedent|''
name|'def'
name|'add_nova'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Monkey patch in nova guidelines.\n\n    Look for functions that start with nova_  and have arguments\n    and add them to pep8 module\n    Assumes you know how to write pep8.py checks\n    """'
newline|'\n'
name|'for'
name|'name'
op|','
name|'function'
name|'in'
name|'globals'
op|'('
op|')'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'inspect'
op|'.'
name|'isfunction'
op|'('
name|'function'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'args'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'function'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'args'
name|'and'
name|'name'
op|'.'
name|'startswith'
op|'('
string|'"nova"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'exec'
op|'('
string|'"pep8.%s = %s"'
op|'%'
op|'('
name|'name'
op|','
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|once_git_check_commit_title
dedent|''
dedent|''
dedent|''
name|'def'
name|'once_git_check_commit_title'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check git commit messages.\n\n    nova HACKING recommends not referencing a bug or blueprint in first line,\n    it should provide an accurate description of the change\n    N801\n    N802 Title limited to 50 chars\n    """'
newline|'\n'
comment|'#Get title of most recent commit'
nl|'\n'
nl|'\n'
name|'subp'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
op|'['
string|"'git'"
op|','
string|"'log'"
op|','
string|"'--no-merges'"
op|','
string|"'--pretty=%s'"
op|','
string|"'-1'"
op|']'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|')'
newline|'\n'
name|'title'
op|'='
name|'subp'
op|'.'
name|'communicate'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'subp'
op|'.'
name|'returncode'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"git log failed with code %s"'
op|'%'
name|'subp'
op|'.'
name|'returncode'
op|')'
newline|'\n'
nl|'\n'
comment|'#From https://github.com/openstack/openstack-ci-puppet'
nl|'\n'
comment|'#       /blob/master/modules/gerrit/manifests/init.pp#L74'
nl|'\n'
comment|'#Changeid|bug|blueprint'
nl|'\n'
dedent|''
name|'git_keywords'
op|'='
op|'('
string|"r'(I[0-9a-f]{8,40})|'"
nl|'\n'
string|"'([Bb]ug|[Ll][Pp])[\\s\\#:]*(\\d+)|'"
nl|'\n'
string|"'([Bb]lue[Pp]rint|[Bb][Pp])[\\s\\#:]*([A-Za-z0-9\\\\-]+)'"
op|')'
newline|'\n'
name|'GIT_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
name|'git_keywords'
op|')'
newline|'\n'
nl|'\n'
name|'error'
op|'='
name|'False'
newline|'\n'
comment|'#NOTE(jogo) if match regex but over 3 words, acceptable title'
nl|'\n'
name|'if'
name|'GIT_REGEX'
op|'.'
name|'search'
op|'('
name|'title'
op|')'
name|'is'
name|'not'
name|'None'
name|'and'
name|'len'
op|'('
name|'title'
op|'.'
name|'split'
op|'('
op|')'
op|')'
op|'<='
number|'3'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|'"N801: git commit title (\'%s\') should provide an accurate "'
nl|'\n'
string|'"description of the change, not just a reference to a bug "'
nl|'\n'
string|'"or blueprint"'
op|'%'
name|'title'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'error'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'title'
op|'.'
name|'decode'
op|'('
string|"'utf-8'"
op|')'
op|')'
op|'>'
number|'72'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|'"N802: git commit title (\'%s\') should be under 50 chars"'
nl|'\n'
op|'%'
name|'title'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'error'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'error'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
comment|'#include nova path'
nl|'\n'
indent|'    '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'append'
op|'('
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
op|')'
newline|'\n'
comment|'#Run once tests (not per line)'
nl|'\n'
DECL|variable|once_error
name|'once_error'
op|'='
name|'once_git_check_commit_title'
op|'('
op|')'
newline|'\n'
comment|'#NOVA error codes start with an N'
nl|'\n'
name|'pep8'
op|'.'
name|'ERRORCODE_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'[EWN]\\d{3}'"
op|')'
newline|'\n'
name|'add_nova'
op|'('
op|')'
newline|'\n'
name|'pep8'
op|'.'
name|'current_file'
op|'='
name|'current_file'
newline|'\n'
name|'pep8'
op|'.'
name|'readlines'
op|'='
name|'readlines'
newline|'\n'
name|'pep8'
op|'.'
name|'excluded'
op|'='
name|'excluded'
newline|'\n'
name|'pep8'
op|'.'
name|'input_dir'
op|'='
name|'input_dir'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pep8'
op|'.'
name|'_main'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
name|'once_error'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'_missingImport'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
op|'('
string|'"%i imports missing in this test environment"'
nl|'\n'
op|'%'
name|'len'
op|'('
name|'_missingImport'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
