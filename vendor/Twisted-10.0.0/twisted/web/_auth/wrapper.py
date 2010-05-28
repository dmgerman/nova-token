begin_unit
comment|'# -*- test-case-name: twisted.web.test.test_httpauth -*-'
nl|'\n'
comment|'# Copyright (c) 2008-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nA guard implementation which supports HTTP header-based authentication\nschemes.\n\nIf no I{Authorization} header is supplied, an anonymous login will be\nattempted by using a L{Anonymous} credentials object.  If such a header is\nsupplied and does not contain allowed credentials, or if anonymous login is\ndenied, a 401 will be sent in the response along with I{WWW-Authenticate}\nheaders for each of the allowed authentication schemes.\n"""'
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
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'components'
name|'import'
name|'proxyForInterface'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'resource'
name|'import'
name|'IResource'
op|','
name|'ErrorPage'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'util'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
name|'import'
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'credentials'
name|'import'
name|'Anonymous'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnauthorizedResource
name|'class'
name|'UnauthorizedResource'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Simple IResource to escape Resource dispatch\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IResource'
op|')'
newline|'\n'
DECL|variable|isLeaf
name|'isLeaf'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'factories'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_credentialFactories'
op|'='
name|'factories'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|render
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send www-authenticate headers to the client\n        """'
newline|'\n'
DECL|function|generateWWWAuthenticate
name|'def'
name|'generateWWWAuthenticate'
op|'('
name|'scheme'
op|','
name|'challenge'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'challenge'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'l'
op|'.'
name|'append'
op|'('
string|'"%s=%s"'
op|'%'
op|'('
name|'k'
op|','
name|'quoteString'
op|'('
name|'v'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"%s %s"'
op|'%'
op|'('
name|'scheme'
op|','
string|'", "'
op|'.'
name|'join'
op|'('
name|'l'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|quoteString
dedent|''
name|'def'
name|'quoteString'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'\'"%s"\''
op|'%'
op|'('
name|'s'
op|'.'
name|'replace'
op|'('
string|"'\\\\'"
op|','
string|"'\\\\\\\\'"
op|')'
op|'.'
name|'replace'
op|'('
string|'\'"\''
op|','
string|'\'\\\\"\''
op|')'
op|','
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'.'
name|'setResponseCode'
op|'('
number|'401'
op|')'
newline|'\n'
name|'for'
name|'fact'
name|'in'
name|'self'
op|'.'
name|'_credentialFactories'
op|':'
newline|'\n'
indent|'            '
name|'challenge'
op|'='
name|'fact'
op|'.'
name|'getChallenge'
op|'('
name|'request'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'responseHeaders'
op|'.'
name|'addRawHeader'
op|'('
nl|'\n'
string|"'www-authenticate'"
op|','
nl|'\n'
name|'generateWWWAuthenticate'
op|'('
name|'fact'
op|'.'
name|'scheme'
op|','
name|'challenge'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'Unauthorized'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getChildWithDefault
dedent|''
name|'def'
name|'getChildWithDefault'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Disable resource dispatch\n        """'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|HTTPAuthSessionWrapper
dedent|''
dedent|''
name|'class'
name|'HTTPAuthSessionWrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Wrap a portal, enforcing supported header-based authentication schemes.\n\n    @ivar _portal: The L{Portal} which will be used to retrieve L{IResource}\n        avatars.\n\n    @ivar _credentialFactories: A list of L{ICredentialFactory} providers which\n        will be used to decode I{Authorization} headers into L{ICredentials}\n        providers.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IResource'
op|')'
newline|'\n'
DECL|variable|isLeaf
name|'isLeaf'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'portal'
op|','
name|'credentialFactories'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize a session wrapper\n\n        @type portal: C{Portal}\n        @param portal: The portal that will authenticate the remote client\n\n        @type credentialFactories: C{Iterable}\n        @param credentialFactories: The portal that will authenticate the\n            remote client based on one submitted C{ICredentialFactory}\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_portal'
op|'='
name|'portal'
newline|'\n'
name|'self'
op|'.'
name|'_credentialFactories'
op|'='
name|'credentialFactories'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_authorizedResource
dedent|''
name|'def'
name|'_authorizedResource'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get the L{IResource} which the given request is authorized to receive.\n        If the proper authorization headers are present, the resource will be\n        requested from the portal.  If not, an anonymous login attempt will be\n        made.\n        """'
newline|'\n'
name|'authheader'
op|'='
name|'request'
op|'.'
name|'getHeader'
op|'('
string|"'authorization'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'authheader'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'util'
op|'.'
name|'DeferredResource'
op|'('
name|'self'
op|'.'
name|'_login'
op|'('
name|'Anonymous'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'factory'
op|','
name|'respString'
op|'='
name|'self'
op|'.'
name|'_selectParseHeader'
op|'('
name|'authheader'
op|')'
newline|'\n'
name|'if'
name|'factory'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'UnauthorizedResource'
op|'('
name|'self'
op|'.'
name|'_credentialFactories'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'credentials'
op|'='
name|'factory'
op|'.'
name|'decode'
op|'('
name|'respString'
op|','
name|'request'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error'
op|'.'
name|'LoginFailed'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'UnauthorizedResource'
op|'('
name|'self'
op|'.'
name|'_credentialFactories'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'err'
op|'('
name|'None'
op|','
string|'"Unexpected failure from credentials factory"'
op|')'
newline|'\n'
name|'return'
name|'ErrorPage'
op|'('
number|'500'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'util'
op|'.'
name|'DeferredResource'
op|'('
name|'self'
op|'.'
name|'_login'
op|'('
name|'credentials'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|render
dedent|''
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Find the L{IResource} avatar suitable for the given request, if\n        possible, and render it.  Otherwise, perhaps render an error page\n        requiring authorization or describing an internal server failure.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_authorizedResource'
op|'('
name|'request'
op|')'
op|'.'
name|'render'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getChildWithDefault
dedent|''
name|'def'
name|'getChildWithDefault'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Inspect the Authorization HTTP header, and return a deferred which,\n        when fired after successful authentication, will return an authorized\n        C{Avatar}. On authentication failure, an C{UnauthorizedResource} will\n        be returned, essentially halting further dispatch on the wrapped\n        resource and all children\n        """'
newline|'\n'
comment|"# Don't consume any segments of the request - this class should be"
nl|'\n'
comment|'# transparent!'
nl|'\n'
name|'request'
op|'.'
name|'postpath'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'request'
op|'.'
name|'prepath'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_authorizedResource'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_login
dedent|''
name|'def'
name|'_login'
op|'('
name|'self'
op|','
name|'credentials'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get the L{IResource} avatar for the given credentials.\n\n        @return: A L{Deferred} which will be called back with an L{IResource}\n            avatar or which will errback if authentication fails.\n        """'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'_portal'
op|'.'
name|'login'
op|'('
name|'credentials'
op|','
name|'None'
op|','
name|'IResource'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'_loginSucceeded'
op|','
name|'self'
op|'.'
name|'_loginFailed'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_loginSucceeded
dedent|''
name|'def'
name|'_loginSucceeded'
op|'('
name|'self'
op|','
op|'('
name|'interface'
op|','
name|'avatar'
op|','
name|'logout'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Handle login success by wrapping the resulting L{IResource} avatar\n        so that the C{logout} callback will be invoked when rendering is\n        complete.\n        """'
newline|'\n'
DECL|class|ResourceWrapper
name|'class'
name|'ResourceWrapper'
op|'('
name|'proxyForInterface'
op|'('
name|'IResource'
op|','
string|"'resource'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""\n            Wrap an L{IResource} so that whenever it or a child of it\n            completes rendering, the cred logout hook will be invoked.\n\n            An assumption is made here that exactly one L{IResource} from\n            among C{avatar} and all of its children will be rendered.  If\n            more than one is rendered, C{logout} will be invoked multiple\n            times and probably earlier than desired.\n            """'
newline|'\n'
DECL|member|getChildWithDefault
name|'def'
name|'getChildWithDefault'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'                '
string|'"""\n                Pass through the lookup to the wrapped resource, wrapping\n                the result in L{ResourceWrapper} to ensure C{logout} is\n                called when rendering of the child is complete.\n                """'
newline|'\n'
name|'return'
name|'ResourceWrapper'
op|'('
name|'self'
op|'.'
name|'resource'
op|'.'
name|'getChildWithDefault'
op|'('
name|'name'
op|','
name|'request'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|render
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'                '
string|'"""\n                Hook into response generation so that when rendering has\n                finished completely, C{logout} is called.\n                """'
newline|'\n'
name|'request'
op|'.'
name|'notifyFinish'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'ign'
op|':'
name|'logout'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'ResourceWrapper'
op|','
name|'self'
op|')'
op|'.'
name|'render'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'ResourceWrapper'
op|'('
name|'avatar'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_loginFailed
dedent|''
name|'def'
name|'_loginFailed'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Handle login failure by presenting either another challenge (for\n        expected authentication/authorization-related failures) or a server\n        error page (for anything else).\n        """'
newline|'\n'
name|'if'
name|'result'
op|'.'
name|'check'
op|'('
name|'error'
op|'.'
name|'Unauthorized'
op|','
name|'error'
op|'.'
name|'LoginFailed'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'UnauthorizedResource'
op|'('
name|'self'
op|'.'
name|'_credentialFactories'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'err'
op|'('
nl|'\n'
name|'result'
op|','
nl|'\n'
string|'"HTTPAuthSessionWrapper.getChildWithDefault encountered "'
nl|'\n'
string|'"unexpected error"'
op|')'
newline|'\n'
name|'return'
name|'ErrorPage'
op|'('
number|'500'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_selectParseHeader
dedent|''
dedent|''
name|'def'
name|'_selectParseHeader'
op|'('
name|'self'
op|','
name|'header'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Choose an C{ICredentialFactory} from C{_credentialFactories}\n        suitable to use to decode the given I{Authenticate} header.\n\n        @return: A two-tuple of a factory and the remaining portion of the\n            header value to be decoded or a two-tuple of C{None} if no\n            factory can decode the header value.\n        """'
newline|'\n'
name|'elements'
op|'='
name|'header'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
newline|'\n'
name|'scheme'
op|'='
name|'elements'
op|'['
number|'0'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'for'
name|'fact'
name|'in'
name|'self'
op|'.'
name|'_credentialFactories'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fact'
op|'.'
name|'scheme'
op|'=='
name|'scheme'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'('
name|'fact'
op|','
string|"' '"
op|'.'
name|'join'
op|'('
name|'elements'
op|'['
number|'1'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
