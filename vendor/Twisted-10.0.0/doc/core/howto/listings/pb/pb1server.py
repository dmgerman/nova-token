begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'spread'
name|'import'
name|'pb'
newline|'\n'
nl|'\n'
DECL|class|Two
name|'class'
name|'Two'
op|'('
name|'pb'
op|'.'
name|'Referenceable'
op|')'
op|':'
newline|'\n'
DECL|member|remote_three
indent|'    '
name|'def'
name|'remote_three'
op|'('
name|'self'
op|','
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"Two.three was given"'
op|','
name|'arg'
newline|'\n'
nl|'\n'
DECL|class|One
dedent|''
dedent|''
name|'class'
name|'One'
op|'('
name|'pb'
op|'.'
name|'Root'
op|')'
op|':'
newline|'\n'
DECL|member|remote_getTwo
indent|'    '
name|'def'
name|'remote_getTwo'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'two'
op|'='
name|'Two'
op|'('
op|')'
newline|'\n'
name|'print'
string|'"returning a Two called"'
op|','
name|'two'
newline|'\n'
name|'return'
name|'two'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8800'
op|','
name|'pb'
op|'.'
name|'PBServerFactory'
op|'('
name|'One'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
