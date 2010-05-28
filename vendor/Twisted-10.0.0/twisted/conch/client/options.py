begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'conch'
op|'.'
name|'ssh'
op|'.'
name|'transport'
name|'import'
name|'SSHClientTransport'
op|','
name|'SSHCiphers'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'usage'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
DECL|class|ConchOptions
name|'class'
name|'ConchOptions'
op|'('
name|'usage'
op|'.'
name|'Options'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|optParameters
indent|'    '
name|'optParameters'
op|'='
op|'['
op|'['
string|"'user'"
op|','
string|"'l'"
op|','
name|'None'
op|','
string|"'Log in using this user name.'"
op|']'
op|','
nl|'\n'
op|'['
string|"'identity'"
op|','
string|"'i'"
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'['
string|"'ciphers'"
op|','
string|"'c'"
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'['
string|"'macs'"
op|','
string|"'m'"
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'['
string|"'port'"
op|','
string|"'p'"
op|','
name|'None'
op|','
string|"'Connect to this port.  Server must be on the same port.'"
op|']'
op|','
nl|'\n'
op|'['
string|"'option'"
op|','
string|"'o'"
op|','
name|'None'
op|','
string|"'Ignored OpenSSH options'"
op|']'
op|','
nl|'\n'
op|'['
string|"'host-key-algorithms'"
op|','
string|"''"
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'['
string|"'known-hosts'"
op|','
string|"''"
op|','
name|'None'
op|','
string|"'File to check for host keys'"
op|']'
op|','
nl|'\n'
op|'['
string|"'user-authentications'"
op|','
string|"''"
op|','
name|'None'
op|','
string|"'Types of user authentications to use.'"
op|']'
op|','
nl|'\n'
op|'['
string|"'logfile'"
op|','
string|"''"
op|','
name|'None'
op|','
string|"'File to log to, or - for stdout'"
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
op|'['
string|"'version'"
op|','
string|"'V'"
op|','
string|"'Display version number only.'"
op|']'
op|','
nl|'\n'
op|'['
string|"'compress'"
op|','
string|"'C'"
op|','
string|"'Enable compression.'"
op|']'
op|','
nl|'\n'
op|'['
string|"'log'"
op|','
string|"'v'"
op|','
string|"'Enable logging (defaults to stderr)'"
op|']'
op|','
nl|'\n'
op|'['
string|"'nox11'"
op|','
string|"'x'"
op|','
string|"'Disable X11 connection forwarding (default)'"
op|']'
op|','
nl|'\n'
op|'['
string|"'agent'"
op|','
string|"'A'"
op|','
string|"'Enable authentication agent forwarding'"
op|']'
op|','
nl|'\n'
op|'['
string|"'noagent'"
op|','
string|"'a'"
op|','
string|"'Disable authentication agent forwarding (default)'"
op|']'
op|','
nl|'\n'
op|'['
string|"'reconnect'"
op|','
string|"'r'"
op|','
string|"'Reconnect to the server if the connection is lost.'"
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|zsh_altArgDescr
name|'zsh_altArgDescr'
op|'='
op|'{'
string|'"connection-usage"'
op|':'
string|'"Connection types to use"'
op|'}'
newline|'\n'
comment|'#zsh_multiUse = ["foo", "bar"]'
nl|'\n'
DECL|variable|zsh_mutuallyExclusive
name|'zsh_mutuallyExclusive'
op|'='
op|'['
op|'('
string|'"agent"'
op|','
string|'"noagent"'
op|')'
op|']'
newline|'\n'
DECL|variable|zsh_actions
name|'zsh_actions'
op|'='
op|'{'
string|'"user"'
op|':'
string|'"_users"'
op|','
nl|'\n'
string|'"ciphers"'
op|':'
string|'"_values -s , \'ciphers to choose from\' %s"'
op|'%'
nl|'\n'
string|'" "'
op|'.'
name|'join'
op|'('
name|'SSHCiphers'
op|'.'
name|'cipherMap'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|'"macs"'
op|':'
string|'"_values -s , \'macs to choose from\' %s"'
op|'%'
nl|'\n'
string|'" "'
op|'.'
name|'join'
op|'('
name|'SSHCiphers'
op|'.'
name|'macMap'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|'"host-key-algorithms"'
op|':'
string|'"_values -s , \'host key algorithms to choose from\' %s"'
op|'%'
nl|'\n'
string|'" "'
op|'.'
name|'join'
op|'('
name|'SSHClientTransport'
op|'.'
name|'supportedPublicKeys'
op|')'
op|','
nl|'\n'
comment|'#"user-authentications":"_values -s , \'user authentication types to choose from\' %s" %'
nl|'\n'
comment|'#    " ".join(???),'
nl|'\n'
op|'}'
newline|'\n'
comment|'#zsh_actionDescr = {"logfile":"log file name", "random":"random seed"}'
nl|'\n'
comment|"# user, host, or user@host completion similar to zsh's ssh completion"
nl|'\n'
name|'zsh_extras'
op|'='
op|'['
string|'\'1:host | user@host:{_ssh;if compset -P "*@"; then _wanted hosts expl "remote host name" _ssh_hosts && ret=0 elif compset -S "@*"; then _wanted users expl "login name" _ssh_users -S "" && ret=0 else if (( $+opt_args[-l] )); then tmp=() else tmp=( "users:login name:_ssh_users -qS@" ) fi; _alternative "hosts:remote host name:_ssh_hosts" "$tmp[@]" && ret=0 fi}\''
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'.'
name|'Options'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'identitys'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'conns'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|opt_identity
dedent|''
name|'def'
name|'opt_identity'
op|'('
name|'self'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Identity for public-key authentication"""'
newline|'\n'
name|'self'
op|'.'
name|'identitys'
op|'.'
name|'append'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
DECL|member|opt_ciphers
dedent|''
name|'def'
name|'opt_ciphers'
op|'('
name|'self'
op|','
name|'ciphers'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Select encryption algorithms"'
newline|'\n'
name|'ciphers'
op|'='
name|'ciphers'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'for'
name|'cipher'
name|'in'
name|'ciphers'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'SSHCiphers'
op|'.'
name|'cipherMap'
op|'.'
name|'has_key'
op|'('
name|'cipher'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
string|'"Unknown cipher type \'%s\'"'
op|'%'
name|'cipher'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'['
string|"'ciphers'"
op|']'
op|'='
name|'ciphers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|opt_macs
dedent|''
name|'def'
name|'opt_macs'
op|'('
name|'self'
op|','
name|'macs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Specify MAC algorithms"'
newline|'\n'
name|'macs'
op|'='
name|'macs'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'SSHCiphers'
op|'.'
name|'macMap'
op|'.'
name|'has_key'
op|'('
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
string|'"Unknown mac type \'%s\'"'
op|'%'
name|'mac'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'['
string|"'macs'"
op|']'
op|'='
name|'macs'
newline|'\n'
nl|'\n'
DECL|member|opt_host_key_algorithms
dedent|''
name|'def'
name|'opt_host_key_algorithms'
op|'('
name|'self'
op|','
name|'hkas'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Select host key algorithms"'
newline|'\n'
name|'hkas'
op|'='
name|'hkas'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'for'
name|'hka'
name|'in'
name|'hkas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hka'
name|'not'
name|'in'
name|'SSHClientTransport'
op|'.'
name|'supportedPublicKeys'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
string|'"Unknown host key type \'%s\'"'
op|'%'
name|'hka'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'['
string|"'host-key-algorithms'"
op|']'
op|'='
name|'hkas'
newline|'\n'
nl|'\n'
DECL|member|opt_user_authentications
dedent|''
name|'def'
name|'opt_user_authentications'
op|'('
name|'self'
op|','
name|'uas'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Choose how to authenticate to the remote server"'
newline|'\n'
name|'self'
op|'['
string|"'user-authentications'"
op|']'
op|'='
name|'uas'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
nl|'\n'
comment|'#    def opt_compress(self):'
nl|'\n'
comment|'#        "Enable compression"'
nl|'\n'
comment|'#        self.enableCompression = 1'
nl|'\n'
comment|"#        SSHClientTransport.supportedCompressions[0:1] = ['zlib']"
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
