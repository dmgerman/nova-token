begin_unit
name|'import'
name|'cloudservers'
newline|'\n'
nl|'\n'
DECL|class|IdFake
name|'class'
name|'IdFake'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'id'
op|'='
name|'id'
newline|'\n'
nl|'\n'
comment|'# to get your access key:'
nl|'\n'
comment|'# from nova.auth import users'
nl|'\n'
comment|'# users.UserManger.instance().get_users()[0].access'
nl|'\n'
DECL|variable|rscloud
dedent|''
dedent|''
name|'rscloud'
op|'='
name|'cloudservers'
op|'.'
name|'CloudServers'
op|'('
nl|'\n'
string|"'admin'"
op|','
nl|'\n'
string|"'6cca875e-5ab3-4c60-9852-abf5c5c60cc6'"
nl|'\n'
op|')'
newline|'\n'
name|'rscloud'
op|'.'
name|'client'
op|'.'
name|'AUTH_URL'
op|'='
string|"'http://localhost:8773/v1.0'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|rv
name|'rv'
op|'='
name|'rscloud'
op|'.'
name|'servers'
op|'.'
name|'list'
op|'('
op|')'
newline|'\n'
name|'print'
string|'"SERVERS: %s"'
op|'%'
name|'rv'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'rv'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
DECL|variable|server
indent|'    '
name|'server'
op|'='
name|'rscloud'
op|'.'
name|'servers'
op|'.'
name|'create'
op|'('
nl|'\n'
string|'"test-server"'
op|','
nl|'\n'
name|'IdFake'
op|'('
string|'"ami-tiny"'
op|')'
op|','
nl|'\n'
name|'IdFake'
op|'('
string|'"m1.tiny"'
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'print'
string|'"LAUNCH: %s"'
op|'%'
name|'server'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|server
indent|'    '
name|'server'
op|'='
name|'rv'
op|'['
number|'0'
op|']'
newline|'\n'
name|'print'
string|'"Server to kill: %s"'
op|'%'
name|'server'
newline|'\n'
nl|'\n'
dedent|''
name|'raw_input'
op|'('
string|'"press enter key to kill the server"'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
