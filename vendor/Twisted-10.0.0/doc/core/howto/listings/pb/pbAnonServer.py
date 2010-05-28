begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2007-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nImplement the realm for and run on port 8800 a PB service which allows both\nanonymous and username/password based access.\n\nSuccessful username/password-based login requests given an instance of\nMyPerspective with a name which matches the username with which they\nauthenticated.  Success anonymous login requests are given an instance of\nMyPerspective with the name "Anonymous".\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'sys'
name|'import'
name|'stdout'
newline|'\n'
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
name|'python'
op|'.'
name|'log'
name|'import'
name|'startLogging'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'checkers'
name|'import'
name|'ANONYMOUS'
op|','
name|'AllowAnonymousAccess'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'checkers'
name|'import'
name|'InMemoryUsernamePasswordDatabaseDontUse'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'portal'
name|'import'
name|'IRealm'
op|','
name|'Portal'
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
name|'spread'
op|'.'
name|'pb'
name|'import'
name|'Avatar'
op|','
name|'IPerspective'
op|','
name|'PBServerFactory'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MyPerspective
name|'class'
name|'MyPerspective'
op|'('
name|'Avatar'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Trivial avatar exposing a single remote method for demonstrative\n    purposes.  All successful login attempts in this example will result in\n    an avatar which is an instance of this class.\n\n    @type name: C{str}\n    @ivar name: The username which was used during login or C{"Anonymous"}\n    if the login was anonymous (a real service might want to avoid the\n    collision this introduces between anonoymous users and authenticated\n    users named "Anonymous").\n    """'
newline|'\n'
DECL|member|__init__
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
nl|'\n'
nl|'\n'
DECL|member|perspective_foo
dedent|''
name|'def'
name|'perspective_foo'
op|'('
name|'self'
op|','
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Print a simple message which gives the argument this method was\n        called with and this avatar\'s name.\n        """'
newline|'\n'
name|'print'
string|'"I am %s.  perspective_foo(%s) called on %s."'
op|'%'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'name'
op|','
name|'arg'
op|','
name|'self'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|MyRealm
dedent|''
dedent|''
name|'class'
name|'MyRealm'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Trivial realm which supports anonymous and named users by creating\n    avatars which are instances of MyPerspective for either.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IRealm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|requestAvatar
name|'def'
name|'requestAvatar'
op|'('
name|'self'
op|','
name|'avatarId'
op|','
name|'mind'
op|','
op|'*'
name|'interfaces'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'IPerspective'
name|'not'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
string|'"MyRealm only handles IPerspective"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'avatarId'
name|'is'
name|'ANONYMOUS'
op|':'
newline|'\n'
indent|'            '
name|'avatarId'
op|'='
string|'"Anonymous"'
newline|'\n'
dedent|''
name|'return'
name|'IPerspective'
op|','
name|'MyPerspective'
op|'('
name|'avatarId'
op|')'
op|','
name|'lambda'
op|':'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Create a PB server using MyRealm and run it on port 8800.\n    """'
newline|'\n'
name|'startLogging'
op|'('
name|'stdout'
op|')'
newline|'\n'
nl|'\n'
name|'p'
op|'='
name|'Portal'
op|'('
name|'MyRealm'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Here the username/password checker is registered.'
nl|'\n'
name|'c1'
op|'='
name|'InMemoryUsernamePasswordDatabaseDontUse'
op|'('
name|'user1'
op|'='
string|'"pass1"'
op|','
name|'user2'
op|'='
string|'"pass2"'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'registerChecker'
op|'('
name|'c1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Here the anonymous checker is registered.'
nl|'\n'
name|'c2'
op|'='
name|'AllowAnonymousAccess'
op|'('
op|')'
newline|'\n'
name|'p'
op|'.'
name|'registerChecker'
op|'('
name|'c2'
op|')'
newline|'\n'
nl|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8800'
op|','
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
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
