begin_unit
comment|'#! /usr/bin/python'
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
DECL|class|Client
name|'class'
name|'Client'
op|':'
newline|'\n'
DECL|member|connect
indent|'    '
name|'def'
name|'connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deferred'
op|'='
name|'pb'
op|'.'
name|'getObjectAt'
op|'('
string|'"localhost"'
op|','
number|'8800'
op|','
number|'30'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'got_obj'
op|','
name|'self'
op|'.'
name|'err_obj'
op|')'
newline|'\n'
comment|'# when the Deferred fires (i.e. when the connection is established and'
nl|'\n'
comment|"# we receive a reference to the remote object), the 'got_obj' callback"
nl|'\n'
comment|'# will be run'
nl|'\n'
nl|'\n'
DECL|member|got_obj
dedent|''
name|'def'
name|'got_obj'
op|'('
name|'self'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"got object:"'
op|','
name|'obj'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'='
name|'obj'
newline|'\n'
name|'print'
string|'"asking it to add"'
newline|'\n'
name|'def2'
op|'='
name|'self'
op|'.'
name|'server'
op|'.'
name|'callRemote'
op|'('
string|'"add"'
op|','
number|'1'
op|','
number|'2'
op|')'
newline|'\n'
name|'def2'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'add_done'
op|','
name|'self'
op|'.'
name|'err'
op|')'
newline|'\n'
comment|'# this Deferred fires when the method call is complete'
nl|'\n'
nl|'\n'
DECL|member|err_obj
dedent|''
name|'def'
name|'err_obj'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"error getting object"'
op|','
name|'reason'
newline|'\n'
name|'self'
op|'.'
name|'quit'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_done
dedent|''
name|'def'
name|'add_done'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"addition complete, result is"'
op|','
name|'result'
newline|'\n'
name|'print'
string|'"now trying subtract"'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'server'
op|'.'
name|'callRemote'
op|'('
string|'"subtract"'
op|','
number|'5'
op|','
number|'12'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'sub_done'
op|','
name|'self'
op|'.'
name|'err'
op|')'
newline|'\n'
nl|'\n'
DECL|member|err
dedent|''
name|'def'
name|'err'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"Error running remote method"'
op|','
name|'reason'
newline|'\n'
name|'self'
op|'.'
name|'quit'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|sub_done
dedent|''
name|'def'
name|'sub_done'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"subtraction result is"'
op|','
name|'result'
newline|'\n'
name|'self'
op|'.'
name|'quit'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|quit
dedent|''
name|'def'
name|'quit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"shutting down"'
newline|'\n'
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|c
dedent|''
dedent|''
name|'c'
op|'='
name|'Client'
op|'('
op|')'
newline|'\n'
name|'c'
op|'.'
name|'connect'
op|'('
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
