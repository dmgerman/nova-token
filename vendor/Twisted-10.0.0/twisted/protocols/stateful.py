begin_unit
comment|'# -*- test-case-name: twisted.test.test_stateful -*-'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'cStringIO'
name|'import'
name|'StringIO'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'StringIO'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
DECL|class|StatefulProtocol
dedent|''
name|'class'
name|'StatefulProtocol'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Protocol that stores state for you.\n\n    state is a pair (function, num_bytes). When num_bytes bytes of data arrives\n    from the network, function is called. It is expected to return the next\n    state or None to keep same state. Initial state is returned by\n    getInitialState (override it).\n    """'
newline|'\n'
DECL|variable|_sful_data
name|'_sful_data'
op|'='
name|'None'
op|','
name|'None'
op|','
number|'0'
newline|'\n'
nl|'\n'
DECL|member|makeConnection
name|'def'
name|'makeConnection'
op|'('
name|'self'
op|','
name|'transport'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'protocol'
op|'.'
name|'Protocol'
op|'.'
name|'makeConnection'
op|'('
name|'self'
op|','
name|'transport'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_sful_data'
op|'='
name|'self'
op|'.'
name|'getInitialState'
op|'('
op|')'
op|','
name|'StringIO'
op|'('
op|')'
op|','
number|'0'
newline|'\n'
nl|'\n'
DECL|member|getInitialState
dedent|''
name|'def'
name|'getInitialState'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'state'
op|','
name|'buffer'
op|','
name|'offset'
op|'='
name|'self'
op|'.'
name|'_sful_data'
newline|'\n'
name|'buffer'
op|'.'
name|'seek'
op|'('
number|'0'
op|','
number|'2'
op|')'
newline|'\n'
name|'buffer'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'blen'
op|'='
name|'buffer'
op|'.'
name|'tell'
op|'('
op|')'
comment|'# how many bytes total is in the buffer'
newline|'\n'
name|'buffer'
op|'.'
name|'seek'
op|'('
name|'offset'
op|')'
newline|'\n'
name|'while'
name|'blen'
op|'-'
name|'offset'
op|'>='
name|'state'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
name|'buffer'
op|'.'
name|'read'
op|'('
name|'state'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'offset'
op|'+='
name|'state'
op|'['
number|'1'
op|']'
newline|'\n'
name|'next'
op|'='
name|'state'
op|'['
number|'0'
op|']'
op|'('
name|'d'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'disconnecting'
op|':'
comment|'# XXX: argh stupid hack borrowed right from LineReceiver'
newline|'\n'
indent|'                '
name|'return'
comment|"# dataReceived won't be called again, so who cares about consistent state"
newline|'\n'
dedent|''
name|'if'
name|'next'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'next'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'offset'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'b'
op|'='
name|'buffer'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'buffer'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'buffer'
op|'.'
name|'truncate'
op|'('
op|')'
newline|'\n'
name|'buffer'
op|'.'
name|'write'
op|'('
name|'b'
op|')'
newline|'\n'
name|'offset'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_sful_data'
op|'='
name|'state'
op|','
name|'buffer'
op|','
name|'offset'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
