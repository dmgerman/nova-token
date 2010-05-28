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
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
nl|'\n'
DECL|class|One
name|'class'
name|'One'
op|'('
name|'pb'
op|'.'
name|'Root'
op|')'
op|':'
newline|'\n'
DECL|member|remote_takeTwo
indent|'    '
name|'def'
name|'remote_takeTwo'
op|'('
name|'self'
op|','
name|'two'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"received a Two called"'
op|','
name|'two'
newline|'\n'
name|'print'
string|'"telling it to print(12)"'
newline|'\n'
name|'two'
op|'.'
name|'callRemote'
op|'('
string|'"print"'
op|','
number|'12'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
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
