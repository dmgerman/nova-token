begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nExample using stdio, Deferreds, LineReceiver and twisted.web.client.\n\nNote that the WebCheckerCommandProtocol protocol could easily be used in e.g.\na telnet server instead; see the comments for details.\n\nBased on an example by Abe Fettig.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'stdio'
op|','
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'basic'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
DECL|class|WebCheckerCommandProtocol
name|'class'
name|'WebCheckerCommandProtocol'
op|'('
name|'basic'
op|'.'
name|'LineReceiver'
op|')'
op|':'
newline|'\n'
DECL|variable|delimiter
indent|'    '
name|'delimiter'
op|'='
string|"'\\n'"
comment|'# unix terminal style newlines. remove this line'
newline|'\n'
comment|'# for use with Telnet'
nl|'\n'
nl|'\n'
DECL|member|connectionMade
name|'def'
name|'connectionMade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|'"Web checker console. Type \'help\' for help."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lineReceived
dedent|''
name|'def'
name|'lineReceived'
op|'('
name|'self'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
comment|'# Ignore blank lines'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'line'
op|':'
name|'return'
newline|'\n'
nl|'\n'
comment|'# Parse the command'
nl|'\n'
name|'commandParts'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'command'
op|'='
name|'commandParts'
op|'['
number|'0'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
name|'commandParts'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
comment|'# Dispatch the command to the appropriate method.  Note that all you'
nl|'\n'
comment|'# need to do to implement a new command is add another do_* method.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'do_'"
op|'+'
name|'command'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|"'Error: no such command.'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|"'Error: '"
op|'+'
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_help
dedent|''
dedent|''
dedent|''
name|'def'
name|'do_help'
op|'('
name|'self'
op|','
name|'command'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""help [command]: List commands, or show help on the given command"""'
newline|'\n'
name|'if'
name|'command'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sendLine'
op|'('
name|'getattr'
op|'('
name|'self'
op|','
string|"'do_'"
op|'+'
name|'command'
op|')'
op|'.'
name|'__doc__'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'commands'
op|'='
op|'['
name|'cmd'
op|'['
number|'3'
op|':'
op|']'
name|'for'
name|'cmd'
name|'in'
name|'dir'
op|'('
name|'self'
op|')'
name|'if'
name|'cmd'
op|'.'
name|'startswith'
op|'('
string|"'do_'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'sendLine'
op|'('
string|'"Valid commands: "'
op|'+'
string|'" "'
op|'.'
name|'join'
op|'('
name|'commands'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_quit
dedent|''
dedent|''
name|'def'
name|'do_quit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""quit: Quit this session"""'
newline|'\n'
name|'self'
op|'.'
name|'sendLine'
op|'('
string|"'Goodbye.'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_check
dedent|''
name|'def'
name|'do_check'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""check <url>: Attempt to download the given web page"""'
newline|'\n'
name|'client'
op|'.'
name|'getPage'
op|'('
name|'url'
op|')'
op|'.'
name|'addCallback'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'__checkSuccess'
op|')'
op|'.'
name|'addErrback'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'__checkFailure'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__checkSuccess
dedent|''
name|'def'
name|'__checkSuccess'
op|'('
name|'self'
op|','
name|'pageData'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|'"Success: got %i bytes."'
op|'%'
name|'len'
op|'('
name|'pageData'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__checkFailure
dedent|''
name|'def'
name|'__checkFailure'
op|'('
name|'self'
op|','
name|'failure'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|'"Failure: "'
op|'+'
name|'failure'
op|'.'
name|'getErrorMessage'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connectionLost
dedent|''
name|'def'
name|'connectionLost'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
comment|'# stop the reactor, only because this is meant to be run in Stdio.'
nl|'\n'
indent|'        '
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'stdio'
op|'.'
name|'StandardIO'
op|'('
name|'WebCheckerCommandProtocol'
op|'('
op|')'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
