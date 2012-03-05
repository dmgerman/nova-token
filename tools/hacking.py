begin_unit
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
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'pep8'
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
comment|'#N6xx Calling methods'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_todo_format
name|'def'
name|'nova_todo_format'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    nova HACKING guide recommendation for TODO:\n    Include your name with TODOs as in "#TODO(termie)"\n    N101\n    """'
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
comment|'# make sure its a comment'
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
string|'"""\n    nova HACKING guide recommends not using except:\n    Do not write "except:", use "except Exception:" at the very least\n    N201\n    """'
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
name|'return'
number|'6'
op|','
string|'"NOVA N201: no \'except:\' at least use \'except Exception:\'"'
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
string|'"""\n    nova HACKING guide recommends not using assertRaises(Exception...):\n    Do not use overly broad Exception type\n    N202\n    """'
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
name|'return'
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
string|'"""\n    nova HACKING guide recommends one import per line:\n    Do not import more than one module per line\n\n    Examples:\n    BAD: from nova.rpc.common import RemoteError, LOG\n    BAD: from sqlalchemy import MetaData, Table\n    N301\n    """'
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
name|'if'
op|'('
name|'pos'
op|'>'
op|'-'
number|'1'
name|'and'
op|'('
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"import "'
op|')'
name|'or'
nl|'\n'
op|'('
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"from "'
op|')'
name|'and'
nl|'\n'
name|'logical_line'
op|'.'
name|'split'
op|'('
op|')'
op|'['
number|'2'
op|']'
op|'=='
string|'"import"'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'pos'
op|','
string|'"NOVA N301: one import per line"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|nova_import_module_only
dedent|''
dedent|''
name|'def'
name|'nova_import_module_only'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    nova HACKING guide recommends importing only modules:\n    Do not import objects, only modules\n    N302 import only modules\n    N303 Invalid Import\n    N304 Relative Import\n    """'
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
name|'valid'
op|'='
name|'True'
newline|'\n'
name|'if'
name|'parent'
op|':'
newline|'\n'
indent|'                '
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
indent|'                '
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
indent|'                '
name|'if'
name|'added'
op|':'
newline|'\n'
indent|'                    '
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
string|'"NOVA N304: No relative "'
nl|'\n'
string|'"imports. \'%s\' is a relative import"'
op|'%'
name|'logical_line'
op|')'
newline|'\n'
nl|'\n'
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
op|'%'
name|'logical_line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
op|'('
name|'ImportError'
op|','
name|'NameError'
op|')'
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
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
op|'('
string|'"ERROR: import \'%s\' failed, couldn\'t "'
nl|'\n'
string|'"find module"'
op|'%'
name|'logical_line'
op|')'
newline|'\n'
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
dedent|''
dedent|''
name|'split_line'
op|'='
name|'logical_line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# handle "import x"'
nl|'\n'
comment|'# handle "import x as y"'
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
name|'return'
name|'importModuleCheck'
op|'('
name|'mod'
op|')'
newline|'\n'
nl|'\n'
comment|'# handle "from x import y"'
nl|'\n'
comment|'# handle "from x import y as z"'
nl|'\n'
dedent|''
name|'elif'
op|'('
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"from "'
op|')'
name|'and'
string|'","'
name|'not'
name|'in'
name|'logical_line'
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
name|'mod'
op|'='
name|'split_line'
op|'['
number|'3'
op|']'
newline|'\n'
name|'return'
name|'importModuleCheck'
op|'('
name|'mod'
op|','
name|'split_line'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(jogo) handle "from x import *"'
nl|'\n'
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
string|'"""\n    record the current file being tested\n    """'
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
string|'"""\n    Look for functions that start with nova_  and have arguments\n    and add them to pep8 module\n    Assumes you know how to write pep8.py checks\n    """'
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
dedent|''
dedent|''
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
name|'_main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
