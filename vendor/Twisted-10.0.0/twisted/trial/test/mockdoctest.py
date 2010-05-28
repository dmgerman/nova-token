begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'# this module is a trivial class with doctests and a __test__ attribute'
nl|'\n'
comment|"# to test trial's doctest support with python2.4"
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|Counter
name|'class'
name|'Counter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""a simple counter object for testing trial\'s doctest support\n\n         >>> c = Counter()\n         >>> c.value()\n         0\n         >>> c += 3\n         >>> c.value()\n         3\n         >>> c.incr()\n         >>> c.value() == 4\n         True\n         >>> c == 4\n         True\n         >>> c != 9\n         True\n\n    """'
newline|'\n'
DECL|variable|_count
name|'_count'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'initialValue'
op|'='
number|'0'
op|','
name|'maxval'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_count'
op|'='
name|'initialValue'
newline|'\n'
name|'self'
op|'.'
name|'maxval'
op|'='
name|'maxval'
newline|'\n'
nl|'\n'
DECL|member|__iadd__
dedent|''
name|'def'
name|'__iadd__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""add other to my value and return self\n\n             >>> c = Counter(100)\n             >>> c += 333\n             >>> c == 433\n             True\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'maxval'
name|'is'
name|'not'
name|'None'
name|'and'
op|'('
op|'('
name|'self'
op|'.'
name|'_count'
op|'+'
name|'other'
op|')'
op|'>'
name|'self'
op|'.'
name|'maxval'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|','
string|'"sorry, counter got too big"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_count'
op|'+='
name|'other'
newline|'\n'
dedent|''
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""equality operator, compare other to my value()\n           \n           >>> c = Counter()\n           >>> c == 0\n           True\n           >>> c += 10\n           >>> c.incr()\n           >>> c == 10   # fail this test on purpose\n           True\n\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_count'
op|'=='
name|'other'
newline|'\n'
nl|'\n'
DECL|member|__ne__
dedent|''
name|'def'
name|'__ne__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""inequality operator\n\n             >>> c = Counter()\n             >>> c != 10\n             True\n        """'
newline|'\n'
name|'return'
name|'not'
name|'self'
op|'.'
name|'__eq__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
DECL|member|incr
dedent|''
name|'def'
name|'incr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""increment my value by 1\n\n             >>> from twisted.trial.test.mockdoctest import Counter\n             >>> c = Counter(10, 11)\n             >>> c.incr()\n             >>> c.value() == 11\n             True\n             >>> c.incr()\n             Traceback (most recent call last):\n               File "<stdin>", line 1, in ?\n               File "twisted/trial/test/mockdoctest.py", line 51, in incr\n                 self.__iadd__(1)\n               File "twisted/trial/test/mockdoctest.py", line 39, in __iadd__\n                 raise ValueError, "sorry, counter got too big"\n             ValueError: sorry, counter got too big\n        """'
newline|'\n'
name|'self'
op|'.'
name|'__iadd__'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|value
dedent|''
name|'def'
name|'value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return this counter\'s value\n\n             >>> c = Counter(555)\n             >>> c.value() == 555\n             True\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_count'
newline|'\n'
nl|'\n'
DECL|member|unexpectedException
dedent|''
name|'def'
name|'unexpectedException'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""i will raise an unexpected exception...\n        ... *CAUSE THAT\'S THE KINDA GUY I AM*\n            \n              >>> 1/0\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
