begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""Utilities and helper functions that won\'t produce circular imports."""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|getcallargs
name|'def'
name|'getcallargs'
op|'('
name|'function'
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
string|'"""This is a simplified inspect.getcallargs (2.7+).\n\n    It should be replaced when python >= 2.7 is standard.\n    """'
newline|'\n'
name|'keyed_args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'argnames'
op|','
name|'varargs'
op|','
name|'keywords'
op|','
name|'defaults'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'function'
op|')'
newline|'\n'
nl|'\n'
name|'keyed_args'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(alaski) the implicit 'self' or 'cls' argument shows up in"
nl|'\n'
comment|"# argnames but not in args or kwargs.  Uses 'in' rather than '==' because"
nl|'\n'
comment|"# some tests use 'self2'."
nl|'\n'
name|'if'
string|"'self'"
name|'in'
name|'argnames'
op|'['
number|'0'
op|']'
name|'or'
string|"'cls'"
op|'=='
name|'argnames'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
comment|'# The function may not actually be a method or have im_self.'
nl|'\n'
comment|"# Typically seen when it's stubbed with mox."
nl|'\n'
indent|'        '
name|'if'
name|'inspect'
op|'.'
name|'ismethod'
op|'('
name|'function'
op|')'
name|'and'
name|'hasattr'
op|'('
name|'function'
op|','
string|"'im_self'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'keyed_args'
op|'['
name|'argnames'
op|'['
number|'0'
op|']'
op|']'
op|'='
name|'function'
op|'.'
name|'im_self'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'keyed_args'
op|'['
name|'argnames'
op|'['
number|'0'
op|']'
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'remaining_argnames'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'x'
op|':'
name|'x'
name|'not'
name|'in'
name|'keyed_args'
op|','
name|'argnames'
op|')'
newline|'\n'
name|'keyed_args'
op|'.'
name|'update'
op|'('
name|'dict'
op|'('
name|'zip'
op|'('
name|'remaining_argnames'
op|','
name|'args'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'defaults'
op|':'
newline|'\n'
indent|'        '
name|'num_defaults'
op|'='
name|'len'
op|'('
name|'defaults'
op|')'
newline|'\n'
name|'for'
name|'argname'
op|','
name|'value'
name|'in'
name|'zip'
op|'('
name|'argnames'
op|'['
op|'-'
name|'num_defaults'
op|':'
op|']'
op|','
name|'defaults'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'argname'
name|'not'
name|'in'
name|'keyed_args'
op|':'
newline|'\n'
indent|'                '
name|'keyed_args'
op|'['
name|'argname'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'keyed_args'
newline|'\n'
dedent|''
endmarker|''
end_unit
