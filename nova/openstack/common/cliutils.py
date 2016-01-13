begin_unit
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
comment|'# W0603: Using the global statement'
nl|'\n'
comment|'# W0621: Redefining name %s from outer scope'
nl|'\n'
comment|'# pylint: disable=W0603,W0621'
nl|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'print_function'
newline|'\n'
nl|'\n'
name|'import'
name|'getpass'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'textwrap'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'encodeutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
name|'import'
name|'prettytable'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'six'
name|'import'
name|'moves'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'_i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MissingArgs
name|'class'
name|'MissingArgs'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Supplied arguments are not sufficient for calling a function."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'missing'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'missing'
op|'='
name|'missing'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing arguments: %s"'
op|')'
op|'%'
string|'", "'
op|'.'
name|'join'
op|'('
name|'missing'
op|')'
newline|'\n'
name|'super'
op|'('
name|'MissingArgs'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_args
dedent|''
dedent|''
name|'def'
name|'validate_args'
op|'('
name|'fn'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check that the supplied args are sufficient for calling a function.\n\n    >>> validate_args(lambda a: None)\n    Traceback (most recent call last):\n        ...\n    MissingArgs: Missing argument(s): a\n    >>> validate_args(lambda a, b, c, d: None, 0, c=1)\n    Traceback (most recent call last):\n        ...\n    MissingArgs: Missing argument(s): b, d\n\n    :param fn: the function to check\n    :param arg: the positional arguments supplied\n    :param kwargs: the keyword arguments supplied\n    """'
newline|'\n'
name|'argspec'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'fn'
op|')'
newline|'\n'
nl|'\n'
name|'num_defaults'
op|'='
name|'len'
op|'('
name|'argspec'
op|'.'
name|'defaults'
name|'or'
op|'['
op|']'
op|')'
newline|'\n'
name|'required_args'
op|'='
name|'argspec'
op|'.'
name|'args'
op|'['
op|':'
name|'len'
op|'('
name|'argspec'
op|'.'
name|'args'
op|')'
op|'-'
name|'num_defaults'
op|']'
newline|'\n'
nl|'\n'
DECL|function|isbound
name|'def'
name|'isbound'
op|'('
name|'method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'method'
op|','
string|"'__self__'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'isbound'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'required_args'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'missing'
op|'='
op|'['
name|'arg'
name|'for'
name|'arg'
name|'in'
name|'required_args'
name|'if'
name|'arg'
name|'not'
name|'in'
name|'kwargs'
op|']'
newline|'\n'
name|'missing'
op|'='
name|'missing'
op|'['
name|'len'
op|'('
name|'args'
op|')'
op|':'
op|']'
newline|'\n'
name|'if'
name|'missing'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'MissingArgs'
op|'('
name|'missing'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|arg
dedent|''
dedent|''
name|'def'
name|'arg'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator for CLI args.\n\n    Example:\n\n    >>> @arg("name", help="Name of the new entity")\n    ... def entity_create(args):\n    ...     pass\n    """'
newline|'\n'
DECL|function|_decorator
name|'def'
name|'_decorator'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'add_arg'
op|'('
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
DECL|function|env
dedent|''
name|'def'
name|'env'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the first environment variable set.\n\n    If all are empty, defaults to \'\' or keyword arg `default`.\n    """'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'arg'
op|')'
newline|'\n'
name|'if'
name|'value'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'default'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_arg
dedent|''
name|'def'
name|'add_arg'
op|'('
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bind CLI arguments to a shell.py `do_foo` function."""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'func'
op|','
string|"'arguments'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'.'
name|'arguments'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): avoid dups that can occur when the module is shared across'
nl|'\n'
comment|'# tests.'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'args'
op|','
name|'kwargs'
op|')'
name|'not'
name|'in'
name|'func'
op|'.'
name|'arguments'
op|':'
newline|'\n'
comment|'# Because of the semantics of decorator composition if we just append'
nl|'\n'
comment|'# to the options list positional options will appear to be backwards.'
nl|'\n'
indent|'        '
name|'func'
op|'.'
name|'arguments'
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
nl|'\n'
nl|'\n'
DECL|function|unauthenticated
dedent|''
dedent|''
name|'def'
name|'unauthenticated'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds \'unauthenticated\' attribute to decorated function.\n\n    Usage:\n\n    >>> @unauthenticated\n    ... def mymethod(f):\n    ...     pass\n    """'
newline|'\n'
name|'func'
op|'.'
name|'unauthenticated'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'func'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|isunauthenticated
dedent|''
name|'def'
name|'isunauthenticated'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks if the function does not require authentication.\n\n    Mark such functions with the `@unauthenticated` decorator.\n\n    :returns: bool\n    """'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'func'
op|','
string|"'unauthenticated'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|print_list
dedent|''
name|'def'
name|'print_list'
op|'('
name|'objs'
op|','
name|'fields'
op|','
name|'formatters'
op|'='
name|'None'
op|','
name|'sortby_index'
op|'='
number|'0'
op|','
nl|'\n'
name|'mixed_case_fields'
op|'='
name|'None'
op|','
name|'field_labels'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Print a list or objects as a table, one row per object.\n\n    :param objs: iterable of :class:`Resource`\n    :param fields: attributes that correspond to columns, in order\n    :param formatters: `dict` of callables for field formatting\n    :param sortby_index: index of the field for sorting table rows\n    :param mixed_case_fields: fields corresponding to object attributes that\n        have mixed case names (e.g., \'serverId\')\n    :param field_labels: Labels to use in the heading of the table, default to\n        fields.\n    """'
newline|'\n'
name|'formatters'
op|'='
name|'formatters'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'mixed_case_fields'
op|'='
name|'mixed_case_fields'
name|'or'
op|'['
op|']'
newline|'\n'
name|'field_labels'
op|'='
name|'field_labels'
name|'or'
name|'fields'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'field_labels'
op|')'
op|'!='
name|'len'
op|'('
name|'fields'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"Field labels list %(labels)s has different number "'
nl|'\n'
string|'"of elements than fields list %(fields)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'labels'"
op|':'
name|'field_labels'
op|','
string|"'fields'"
op|':'
name|'fields'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'sortby_index'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
string|"'sortby'"
op|':'
name|'field_labels'
op|'['
name|'sortby_index'
op|']'
op|'}'
newline|'\n'
dedent|''
name|'pt'
op|'='
name|'prettytable'
op|'.'
name|'PrettyTable'
op|'('
name|'field_labels'
op|')'
newline|'\n'
name|'pt'
op|'.'
name|'align'
op|'='
string|"'l'"
newline|'\n'
nl|'\n'
name|'for'
name|'o'
name|'in'
name|'objs'
op|':'
newline|'\n'
indent|'        '
name|'row'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'in'
name|'formatters'
op|':'
newline|'\n'
indent|'                '
name|'row'
op|'.'
name|'append'
op|'('
name|'formatters'
op|'['
name|'field'
op|']'
op|'('
name|'o'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'field'
name|'in'
name|'mixed_case_fields'
op|':'
newline|'\n'
indent|'                    '
name|'field_name'
op|'='
name|'field'
op|'.'
name|'replace'
op|'('
string|"' '"
op|','
string|"'_'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'field_name'
op|'='
name|'field'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
string|"' '"
op|','
string|"'_'"
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'getattr'
op|'('
name|'o'
op|','
name|'field_name'
op|','
string|"''"
op|')'
newline|'\n'
name|'row'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'pt'
op|'.'
name|'add_row'
op|'('
name|'row'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'six'
op|'.'
name|'PY2'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'pt'
op|'.'
name|'get_string'
op|'('
op|'**'
name|'kwargs'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'pt'
op|'.'
name|'get_string'
op|'('
op|'**'
name|'kwargs'
op|')'
op|')'
op|'.'
name|'decode'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|print_dict
dedent|''
dedent|''
name|'def'
name|'print_dict'
op|'('
name|'dct'
op|','
name|'dict_property'
op|'='
string|'"Property"'
op|','
name|'wrap'
op|'='
number|'0'
op|','
name|'dict_value'
op|'='
string|"'Value'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Print a `dict` as a table of two columns.\n\n    :param dct: `dict` to print\n    :param dict_property: name of the first column\n    :param wrap: wrapping for the second column\n    :param dict_value: header label for the value (second) column\n    """'
newline|'\n'
name|'pt'
op|'='
name|'prettytable'
op|'.'
name|'PrettyTable'
op|'('
op|'['
name|'dict_property'
op|','
name|'dict_value'
op|']'
op|')'
newline|'\n'
name|'pt'
op|'.'
name|'align'
op|'='
string|"'l'"
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'sorted'
op|'('
name|'dct'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
comment|'# convert dict to str to check length'
nl|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'v'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'wrap'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
name|'textwrap'
op|'.'
name|'fill'
op|'('
name|'six'
op|'.'
name|'text_type'
op|'('
name|'v'
op|')'
op|','
name|'wrap'
op|')'
newline|'\n'
comment|'# if value has a newline, add in multiple rows'
nl|'\n'
comment|'# e.g. fault with stacktrace'
nl|'\n'
dedent|''
name|'if'
name|'v'
name|'and'
name|'isinstance'
op|'('
name|'v'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
name|'and'
string|"r'\\n'"
name|'in'
name|'v'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'='
name|'v'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|"r'\\n'"
op|')'
newline|'\n'
name|'col1'
op|'='
name|'k'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'                '
name|'pt'
op|'.'
name|'add_row'
op|'('
op|'['
name|'col1'
op|','
name|'line'
op|']'
op|')'
newline|'\n'
name|'col1'
op|'='
string|"''"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'pt'
op|'.'
name|'add_row'
op|'('
op|'['
name|'k'
op|','
name|'v'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'six'
op|'.'
name|'PY2'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'pt'
op|'.'
name|'get_string'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'pt'
op|'.'
name|'get_string'
op|'('
op|')'
op|')'
op|'.'
name|'decode'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_password
dedent|''
dedent|''
name|'def'
name|'get_password'
op|'('
name|'max_password_prompts'
op|'='
number|'3'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read password from TTY."""'
newline|'\n'
name|'verify'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'env'
op|'('
string|'"OS_VERIFY_PASSWORD"'
op|')'
op|')'
newline|'\n'
name|'pw'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'sys'
op|'.'
name|'stdin'
op|','
string|'"isatty"'
op|')'
name|'and'
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'isatty'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Check for Ctrl-D'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'__'
name|'in'
name|'moves'
op|'.'
name|'range'
op|'('
name|'max_password_prompts'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pw1'
op|'='
name|'getpass'
op|'.'
name|'getpass'
op|'('
string|'"OS Password: "'
op|')'
newline|'\n'
name|'if'
name|'verify'
op|':'
newline|'\n'
indent|'                    '
name|'pw2'
op|'='
name|'getpass'
op|'.'
name|'getpass'
op|'('
string|'"Please verify: "'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'pw2'
op|'='
name|'pw1'
newline|'\n'
dedent|''
name|'if'
name|'pw1'
op|'=='
name|'pw2'
name|'and'
name|'pw1'
op|':'
newline|'\n'
indent|'                    '
name|'pw'
op|'='
name|'pw1'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'EOFError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'pw'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|service_type
dedent|''
name|'def'
name|'service_type'
op|'('
name|'stype'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds \'service_type\' attribute to decorated function.\n\n    Usage:\n\n    .. code-block:: python\n\n       @service_type(\'volume\')\n       def mymethod(f):\n       ...\n    """'
newline|'\n'
DECL|function|inner
name|'def'
name|'inner'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'.'
name|'service_type'
op|'='
name|'stype'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
dedent|''
name|'return'
name|'inner'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_service_type
dedent|''
name|'def'
name|'get_service_type'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves service type from function."""'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'f'
op|','
string|"'service_type'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pretty_choice_list
dedent|''
name|'def'
name|'pretty_choice_list'
op|'('
name|'l'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"', '"
op|'.'
name|'join'
op|'('
string|'"\'%s\'"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'l'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|exit
dedent|''
name|'def'
name|'exit'
op|'('
name|'msg'
op|'='
string|"''"
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
name|'msg'
op|','
name|'file'
op|'='
name|'sys'
op|'.'
name|'stderr'
op|')'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
