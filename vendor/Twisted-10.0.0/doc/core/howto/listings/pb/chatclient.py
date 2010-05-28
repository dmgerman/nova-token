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
name|'from'
name|'twisted'
op|'.'
name|'cred'
name|'import'
name|'credentials'
newline|'\n'
nl|'\n'
DECL|class|Client
name|'class'
name|'Client'
op|'('
name|'pb'
op|'.'
name|'Referenceable'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|remote_print
indent|'    '
name|'def'
name|'remote_print'
op|'('
name|'self'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'message'
newline|'\n'
nl|'\n'
DECL|member|connect
dedent|''
name|'def'
name|'connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'factory'
op|'='
name|'pb'
op|'.'
name|'PBClientFactory'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'connectTCP'
op|'('
string|'"localhost"'
op|','
number|'8800'
op|','
name|'factory'
op|')'
newline|'\n'
name|'def1'
op|'='
name|'factory'
op|'.'
name|'login'
op|'('
name|'credentials'
op|'.'
name|'UsernamePassword'
op|'('
string|'"alice"'
op|','
string|'"1234"'
op|')'
op|','
nl|'\n'
name|'client'
op|'='
name|'self'
op|')'
newline|'\n'
name|'def1'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'connected'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|connected
dedent|''
name|'def'
name|'connected'
op|'('
name|'self'
op|','
name|'perspective'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"connected, joining group #lookingForFourth"'
newline|'\n'
comment|'# this perspective is a reference to our User object'
nl|'\n'
name|'d'
op|'='
name|'perspective'
op|'.'
name|'callRemote'
op|'('
string|'"joinGroup"'
op|','
string|'"#lookingForFourth"'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'gotGroup'
op|')'
newline|'\n'
nl|'\n'
DECL|member|gotGroup
dedent|''
name|'def'
name|'gotGroup'
op|'('
name|'self'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"joined group, now sending a message to all members"'
newline|'\n'
comment|"# 'group' is a reference to the Group object (through a ViewPoint)"
nl|'\n'
name|'d'
op|'='
name|'group'
op|'.'
name|'callRemote'
op|'('
string|'"send"'
op|','
string|'"You can call me Al."'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'shutdown'
op|')'
newline|'\n'
nl|'\n'
DECL|member|shutdown
dedent|''
name|'def'
name|'shutdown'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'Client'
op|'('
op|')'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
nl|'\n'
endmarker|''
end_unit
