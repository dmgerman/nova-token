begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nAIM echo bot.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'protocols'
name|'import'
name|'toc'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
op|','
name|'protocol'
newline|'\n'
name|'import'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'im'
op|'.'
name|'tocsupport'
name|'as'
name|'ts'
newline|'\n'
nl|'\n'
comment|'# account info'
nl|'\n'
DECL|variable|screenname
name|'screenname'
op|'='
string|"'username'"
newline|'\n'
DECL|variable|password
name|'password'
op|'='
string|"'password'"
newline|'\n'
nl|'\n'
DECL|class|aimBot
name|'class'
name|'aimBot'
op|'('
name|'toc'
op|'.'
name|'TOCClient'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AOL Instant Messenger echo bot"""'
newline|'\n'
nl|'\n'
DECL|member|gotConfig
name|'def'
name|'gotConfig'
op|'('
name|'self'
op|','
name|'mode'
op|','
name|'buddylist'
op|','
name|'permit'
op|','
name|'deny'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""called when the server sends us config info"""'
newline|'\n'
name|'global'
name|'screename'
newline|'\n'
nl|'\n'
comment|'# add someone to our deny list?'
nl|'\n'
name|'self'
op|'.'
name|'add_deny'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# add ourself to our buddy list'
nl|'\n'
name|'self'
op|'.'
name|'add_buddy'
op|'('
op|'['
name|'screenname'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# finish up the signon procedure'
nl|'\n'
name|'self'
op|'.'
name|'signon'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|updateBuddy
dedent|''
name|'def'
name|'updateBuddy'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'online'
op|','
name|'evilness'
op|','
name|'signontime'
op|','
name|'idletime'
op|','
name|'userclass'
op|','
name|'away'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""called when a buddy changes state"""'
newline|'\n'
name|'print'
string|'"status changed for"'
op|','
name|'username'
newline|'\n'
nl|'\n'
DECL|member|hearWarning
dedent|''
name|'def'
name|'hearWarning'
op|'('
name|'self'
op|','
name|'warnlvl'
op|','
name|'screenname'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""called when someone warns us"""'
newline|'\n'
name|'print'
name|'screenname'
op|','
string|'"warned us"'
newline|'\n'
nl|'\n'
DECL|member|hearError
dedent|''
name|'def'
name|'hearError'
op|'('
name|'self'
op|','
name|'errcode'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""called when server sends error"""'
newline|'\n'
name|'print'
string|'"recieved error:"'
op|','
name|'errcode'
newline|'\n'
nl|'\n'
DECL|member|hearMessage
dedent|''
name|'def'
name|'hearMessage'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'message'
op|','
name|'autoreply'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""called when a message is recieved"""'
newline|'\n'
nl|'\n'
comment|"# remove the incoming message' html"
nl|'\n'
name|'msg'
op|'='
name|'ts'
op|'.'
name|'dehtml'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'print'
string|'"got message:"'
op|','
name|'msg'
newline|'\n'
nl|'\n'
comment|'# construct the reply, and turn it into html'
nl|'\n'
name|'reply'
op|'='
name|'ts'
op|'.'
name|'html'
op|'('
string|'"echo: %s"'
op|'%'
name|'msg'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'say'
op|'('
name|'username'
op|','
name|'reply'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|cc
dedent|''
dedent|''
name|'cc'
op|'='
name|'protocol'
op|'.'
name|'ClientCreator'
op|'('
name|'reactor'
op|','
name|'aimBot'
op|','
name|'screenname'
op|','
name|'password'
op|')'
newline|'\n'
name|'cc'
op|'.'
name|'connectTCP'
op|'('
string|'"toc.oscar.aol.com"'
op|','
number|'9898'
op|')'
newline|'\n'
nl|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
