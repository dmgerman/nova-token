begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""Telnet-based shell."""'
newline|'\n'
nl|'\n'
comment|'# twisted imports'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'telnet'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
op|','
name|'failure'
newline|'\n'
nl|'\n'
comment|'# system imports'
nl|'\n'
name|'import'
name|'string'
op|','
name|'copy'
op|','
name|'sys'
newline|'\n'
name|'from'
name|'cStringIO'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Shell
name|'class'
name|'Shell'
op|'('
name|'telnet'
op|'.'
name|'Telnet'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Python command-line shell."""'
newline|'\n'
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
name|'telnet'
op|'.'
name|'Telnet'
op|'.'
name|'connectionMade'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lineBuffer'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|loggedIn
dedent|''
name|'def'
name|'loggedIn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|'">>> "'
op|')'
newline|'\n'
nl|'\n'
DECL|member|checkUserAndPass
dedent|''
name|'def'
name|'checkUserAndPass'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
op|'('
name|'self'
op|'.'
name|'factory'
op|'.'
name|'username'
op|'=='
name|'username'
op|')'
name|'and'
op|'('
name|'password'
op|'=='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'password'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Write some data to the transport.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|telnet_Command
dedent|''
name|'def'
name|'telnet_Command'
op|'('
name|'self'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'lineBuffer'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'cmd'
op|':'
newline|'\n'
indent|'                '
name|'cmd'
op|'='
name|'string'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'lineBuffer'
op|','
string|"'\\n'"
op|')'
op|'+'
string|"'\\n\\n\\n'"
newline|'\n'
name|'self'
op|'.'
name|'doCommand'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lineBuffer'
op|'='
op|'['
op|']'
newline|'\n'
name|'return'
string|'"Command"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'lineBuffer'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|'"... "'
op|')'
newline|'\n'
name|'return'
string|'"Command"'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'doCommand'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
string|'"Command"'
newline|'\n'
nl|'\n'
DECL|member|doCommand
dedent|''
dedent|''
name|'def'
name|'doCommand'
op|'('
name|'self'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# TODO -- refactor this, Reality.author.Author, and the manhole shell'
nl|'\n'
comment|'#to use common functionality (perhaps a twisted.python.code module?)'
nl|'\n'
indent|'        '
name|'fn'
op|'='
string|"'$telnet$'"
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
name|'sys'
op|'.'
name|'stdout'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'self'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'code'
op|'='
name|'compile'
op|'('
name|'cmd'
op|','
name|'fn'
op|','
string|"'eval'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'eval'
op|'('
name|'code'
op|','
name|'self'
op|'.'
name|'factory'
op|'.'
name|'namespace'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'code'
op|'='
name|'compile'
op|'('
name|'cmd'
op|','
name|'fn'
op|','
string|"'exec'"
op|')'
newline|'\n'
name|'exec'
name|'code'
name|'in'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'namespace'
newline|'\n'
dedent|''
name|'except'
name|'SyntaxError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'self'
op|'.'
name|'lineBuffer'
name|'and'
name|'str'
op|'('
name|'e'
op|')'
op|'['
op|':'
number|'14'
op|']'
op|'=='
string|'"unexpected EOF"'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'lineBuffer'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|'"... "'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'failure'
op|'.'
name|'Failure'
op|'('
op|')'
op|'.'
name|'printTraceback'
op|'('
name|'file'
op|'='
name|'self'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'deferr'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
string|"'\\r\\n>>> '"
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                    '
name|'io'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'failure'
op|'.'
name|'Failure'
op|'('
op|')'
op|'.'
name|'printTraceback'
op|'('
name|'file'
op|'='
name|'self'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'deferr'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
string|"'\\r\\n>>> '"
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'out'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'factory'
op|'.'
name|'namespace'
op|'['
string|"'_'"
op|']'
op|'='
name|'result'
newline|'\n'
name|'if'
name|'result'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'repr'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|"'\\r\\n'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|'">>> "'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShellFactory
dedent|''
dedent|''
name|'class'
name|'ShellFactory'
op|'('
name|'protocol'
op|'.'
name|'Factory'
op|')'
op|':'
newline|'\n'
DECL|variable|username
indent|'    '
name|'username'
op|'='
string|'"admin"'
newline|'\n'
DECL|variable|password
name|'password'
op|'='
string|'"admin"'
newline|'\n'
DECL|variable|protocol
name|'protocol'
op|'='
name|'Shell'
newline|'\n'
DECL|variable|service
name|'service'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'namespace'
op|'='
op|'{'
nl|'\n'
string|"'factory'"
op|':'
name|'self'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'_'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|setService
dedent|''
name|'def'
name|'setService'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'namespace'
op|'['
string|"'service'"
op|']'
op|'='
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
newline|'\n'
nl|'\n'
DECL|member|__getstate__
dedent|''
name|'def'
name|'__getstate__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This returns the persistent state of this shell factory.\n        """'
newline|'\n'
name|'dict'
op|'='
name|'self'
op|'.'
name|'__dict__'
newline|'\n'
name|'ns'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'dict'
op|'['
string|"'namespace'"
op|']'
op|')'
newline|'\n'
name|'dict'
op|'['
string|"'namespace'"
op|']'
op|'='
name|'ns'
newline|'\n'
name|'if'
name|'ns'
op|'.'
name|'has_key'
op|'('
string|"'__builtins__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'ns'
op|'['
string|"'__builtins__'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'dict'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
