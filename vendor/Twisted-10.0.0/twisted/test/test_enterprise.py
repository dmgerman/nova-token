begin_unit
comment|'# Copyright (c) 2001-2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nGeneral tests for twisted.enterprise.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'enterprise'
name|'import'
name|'util'
newline|'\n'
nl|'\n'
DECL|class|QuotingTestCase
name|'class'
name|'QuotingTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|testQuoting
indent|'    '
name|'def'
name|'testQuoting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'value'
op|','
name|'typ'
op|','
name|'expected'
name|'in'
op|'['
nl|'\n'
op|'('
number|'12'
op|','
string|'"integer"'
op|','
string|'"12"'
op|')'
op|','
nl|'\n'
op|'('
string|'"foo\'d"'
op|','
string|'"text"'
op|','
string|'"\'foo\'\'d\'"'
op|')'
op|','
nl|'\n'
op|'('
string|'"\\x00abc\\\\s\\xFF"'
op|','
string|'"bytea"'
op|','
string|'"\'\\\\\\\\000abc\\\\\\\\\\\\\\\\s\\\\377\'"'
op|')'
op|','
nl|'\n'
op|'('
number|'12'
op|','
string|'"text"'
op|','
string|'"\'12\'"'
op|')'
op|','
nl|'\n'
op|'('
string|'u"123\'456"'
op|','
string|'"text"'
op|','
string|'u"\'123\'\'456\'"'
op|')'
nl|'\n'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'callDeprecated'
op|'('
name|'util'
op|'.'
name|'_deprecatedVersion'
op|','
name|'util'
op|'.'
name|'quote'
op|','
name|'value'
op|','
nl|'\n'
name|'typ'
op|')'
op|','
nl|'\n'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_safeDeprecation
dedent|''
dedent|''
name|'def'
name|'test_safeDeprecation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{safe} is deprecated.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'callDeprecated'
op|'('
name|'util'
op|'.'
name|'_deprecatedVersion'
op|','
name|'util'
op|'.'
name|'safe'
op|','
string|'"foo"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_getKeyColumnDeprecation
dedent|''
name|'def'
name|'test_getKeyColumnDeprecation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{getKeyColumn} is deprecated.\n        """'
newline|'\n'
DECL|class|Row
name|'class'
name|'Row'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|rowKeyColumns
indent|'            '
name|'rowKeyColumns'
op|'='
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'callDeprecated'
op|'('
name|'util'
op|'.'
name|'_deprecatedVersion'
op|','
name|'util'
op|'.'
name|'getKeyColumn'
op|','
name|'Row'
op|','
string|'"foo"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
