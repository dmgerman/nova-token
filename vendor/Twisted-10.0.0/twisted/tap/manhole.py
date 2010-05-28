begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nI am the support module for making a manhole server with twistd.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'manhole'
name|'import'
name|'service'
newline|'\n'
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
name|'python'
name|'import'
name|'usage'
op|','
name|'util'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
name|'import'
name|'portal'
op|','
name|'checkers'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'strports'
newline|'\n'
name|'import'
name|'os'
op|','
name|'sys'
newline|'\n'
nl|'\n'
DECL|class|Options
name|'class'
name|'Options'
op|'('
name|'usage'
op|'.'
name|'Options'
op|')'
op|':'
newline|'\n'
DECL|variable|synopsis
indent|'    '
name|'synopsis'
op|'='
string|'"[options]"'
newline|'\n'
DECL|variable|optParameters
name|'optParameters'
op|'='
op|'['
nl|'\n'
op|'['
string|'"user"'
op|','
string|'"u"'
op|','
string|'"admin"'
op|','
string|'"Name of user to allow to log in"'
op|']'
op|','
nl|'\n'
op|'['
string|'"port"'
op|','
string|'"p"'
op|','
name|'str'
op|'('
name|'pb'
op|'.'
name|'portno'
op|')'
op|','
string|'"Port to listen on"'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|optFlags
name|'optFlags'
op|'='
op|'['
nl|'\n'
op|'['
string|'"tracebacks"'
op|','
string|'"T"'
op|','
string|'"Allow tracebacks to be sent over the network"'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|zsh_actions
name|'zsh_actions'
op|'='
op|'{'
string|'"user"'
op|':'
string|'"_users"'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|opt_password
name|'def'
name|'opt_password'
op|'('
name|'self'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Required.  \'-\' will prompt or read a password from stdin.\n        """'
newline|'\n'
comment|'# If standard input is a terminal, I prompt for a password and'
nl|'\n'
comment|'# confirm it.  Otherwise, I use the first line from standard'
nl|'\n'
comment|'# input, stripping off a trailing newline if there is one.'
nl|'\n'
name|'if'
name|'password'
name|'in'
op|'('
string|"''"
op|','
string|"'-'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'password'"
op|']'
op|'='
name|'util'
op|'.'
name|'getPassword'
op|'('
name|'confirm'
op|'='
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'password'"
op|']'
op|'='
name|'password'
newline|'\n'
DECL|variable|opt_w
dedent|''
dedent|''
name|'opt_w'
op|'='
name|'opt_password'
newline|'\n'
nl|'\n'
DECL|member|postOptions
name|'def'
name|'postOptions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'has_key'
op|'('
string|"'password'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'opt_password'
op|'('
string|"'-'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|makeService
dedent|''
dedent|''
dedent|''
name|'def'
name|'makeService'
op|'('
name|'config'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'port'
op|','
name|'user'
op|','
name|'password'
op|'='
name|'config'
op|'['
string|"'port'"
op|']'
op|','
name|'config'
op|'['
string|"'user'"
op|']'
op|','
name|'config'
op|'['
string|"'password'"
op|']'
newline|'\n'
name|'p'
op|'='
name|'portal'
op|'.'
name|'Portal'
op|'('
nl|'\n'
name|'service'
op|'.'
name|'Realm'
op|'('
name|'service'
op|'.'
name|'Service'
op|'('
name|'config'
op|'['
string|'"tracebacks"'
op|']'
op|','
name|'config'
op|'.'
name|'get'
op|'('
string|"'namespace'"
op|')'
op|')'
op|')'
op|','
nl|'\n'
op|'['
name|'checkers'
op|'.'
name|'InMemoryUsernamePasswordDatabaseDontUse'
op|'('
op|'**'
op|'{'
name|'user'
op|':'
name|'password'
op|'}'
op|')'
op|']'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'strports'
op|'.'
name|'service'
op|'('
name|'port'
op|','
name|'pb'
op|'.'
name|'PBServerFactory'
op|'('
name|'p'
op|','
name|'config'
op|'['
string|'"tracebacks"'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
