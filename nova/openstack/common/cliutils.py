begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'inspect'
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
nl|'\n'
DECL|member|__init__
indent|'    '
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
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'self'
op|'.'
name|'missing'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"An argument is missing"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|'"%(num)d arguments are missing"'
op|'%'
nl|'\n'
name|'dict'
op|'('
name|'num'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'missing'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_args
dedent|''
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
string|'"""Check that the supplied args are sufficient for calling a function.\n\n    >>> validate_args(lambda a: None)\n    Traceback (most recent call last):\n        ...\n    MissingArgs: An argument is missing\n    >>> validate_args(lambda a, b, c, d: None, 0, c=1)\n    Traceback (most recent call last):\n        ...\n    MissingArgs: 2 arguments are missing\n\n    :param fn: the function to check\n    :param arg: the positional arguments supplied\n    :param kwargs: the keyword arguments supplied\n    """'
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
string|"'im_self'"
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
dedent|''
dedent|''
endmarker|''
end_unit
