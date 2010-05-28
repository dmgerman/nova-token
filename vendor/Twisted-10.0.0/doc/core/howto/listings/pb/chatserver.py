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
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
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
DECL|class|ChatServer
name|'class'
name|'ChatServer'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'groups'
op|'='
op|'{'
op|'}'
comment|'# indexed by name'
newline|'\n'
nl|'\n'
DECL|member|joinGroup
dedent|''
name|'def'
name|'joinGroup'
op|'('
name|'self'
op|','
name|'groupname'
op|','
name|'user'
op|','
name|'allowMattress'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'groups'
op|'.'
name|'has_key'
op|'('
name|'groupname'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'groups'
op|'['
name|'groupname'
op|']'
op|'='
name|'Group'
op|'('
name|'groupname'
op|','
name|'allowMattress'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'groups'
op|'['
name|'groupname'
op|']'
op|'.'
name|'addUser'
op|'('
name|'user'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'groups'
op|'['
name|'groupname'
op|']'
newline|'\n'
nl|'\n'
DECL|class|ChatRealm
dedent|''
dedent|''
name|'class'
name|'ChatRealm'
op|':'
newline|'\n'
indent|'    '
name|'implements'
op|'('
name|'portal'
op|'.'
name|'IRealm'
op|')'
newline|'\n'
DECL|member|requestAvatar
name|'def'
name|'requestAvatar'
op|'('
name|'self'
op|','
name|'avatarID'
op|','
name|'mind'
op|','
op|'*'
name|'interfaces'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'pb'
op|'.'
name|'IPerspective'
name|'in'
name|'interfaces'
newline|'\n'
name|'avatar'
op|'='
name|'User'
op|'('
name|'avatarID'
op|')'
newline|'\n'
name|'avatar'
op|'.'
name|'server'
op|'='
name|'self'
op|'.'
name|'server'
newline|'\n'
name|'avatar'
op|'.'
name|'attached'
op|'('
name|'mind'
op|')'
newline|'\n'
name|'return'
name|'pb'
op|'.'
name|'IPerspective'
op|','
name|'avatar'
op|','
name|'lambda'
name|'a'
op|'='
name|'avatar'
op|':'
name|'a'
op|'.'
name|'detached'
op|'('
name|'mind'
op|')'
newline|'\n'
nl|'\n'
DECL|class|User
dedent|''
dedent|''
name|'class'
name|'User'
op|'('
name|'pb'
op|'.'
name|'Avatar'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
DECL|member|attached
dedent|''
name|'def'
name|'attached'
op|'('
name|'self'
op|','
name|'mind'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'remote'
op|'='
name|'mind'
newline|'\n'
DECL|member|detached
dedent|''
name|'def'
name|'detached'
op|'('
name|'self'
op|','
name|'mind'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'remote'
op|'='
name|'None'
newline|'\n'
DECL|member|perspective_joinGroup
dedent|''
name|'def'
name|'perspective_joinGroup'
op|'('
name|'self'
op|','
name|'groupname'
op|','
name|'allowMattress'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'server'
op|'.'
name|'joinGroup'
op|'('
name|'groupname'
op|','
name|'self'
op|','
name|'allowMattress'
op|')'
newline|'\n'
DECL|member|send
dedent|''
name|'def'
name|'send'
op|'('
name|'self'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'remote'
op|'.'
name|'callRemote'
op|'('
string|'"print"'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Group
dedent|''
dedent|''
name|'class'
name|'Group'
op|'('
name|'pb'
op|'.'
name|'Viewable'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'groupname'
op|','
name|'allowMattress'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'groupname'
newline|'\n'
name|'self'
op|'.'
name|'allowMattress'
op|'='
name|'allowMattress'
newline|'\n'
name|'self'
op|'.'
name|'users'
op|'='
op|'['
op|']'
newline|'\n'
DECL|member|addUser
dedent|''
name|'def'
name|'addUser'
op|'('
name|'self'
op|','
name|'user'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'users'
op|'.'
name|'append'
op|'('
name|'user'
op|')'
newline|'\n'
DECL|member|view_send
dedent|''
name|'def'
name|'view_send'
op|'('
name|'self'
op|','
name|'from_user'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'allowMattress'
name|'and'
name|'message'
op|'.'
name|'find'
op|'('
string|'"mattress"'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|','
string|'"Don\'t say that word"'
newline|'\n'
dedent|''
name|'for'
name|'user'
name|'in'
name|'self'
op|'.'
name|'users'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'.'
name|'send'
op|'('
string|'"<%s> says: %s"'
op|'%'
op|'('
name|'from_user'
op|'.'
name|'name'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|realm
dedent|''
dedent|''
dedent|''
name|'realm'
op|'='
name|'ChatRealm'
op|'('
op|')'
newline|'\n'
name|'realm'
op|'.'
name|'server'
op|'='
name|'ChatServer'
op|'('
op|')'
newline|'\n'
DECL|variable|checker
name|'checker'
op|'='
name|'checkers'
op|'.'
name|'InMemoryUsernamePasswordDatabaseDontUse'
op|'('
op|')'
newline|'\n'
name|'checker'
op|'.'
name|'addUser'
op|'('
string|'"alice"'
op|','
string|'"1234"'
op|')'
newline|'\n'
name|'checker'
op|'.'
name|'addUser'
op|'('
string|'"bob"'
op|','
string|'"secret"'
op|')'
newline|'\n'
name|'checker'
op|'.'
name|'addUser'
op|'('
string|'"carol"'
op|','
string|'"fido"'
op|')'
newline|'\n'
DECL|variable|p
name|'p'
op|'='
name|'portal'
op|'.'
name|'Portal'
op|'('
name|'realm'
op|','
op|'['
name|'checker'
op|']'
op|')'
newline|'\n'
nl|'\n'
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
name|'p'
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
