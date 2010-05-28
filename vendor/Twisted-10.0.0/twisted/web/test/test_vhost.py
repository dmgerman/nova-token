begin_unit
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.web.vhost}.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'defer'
name|'import'
name|'gatherResults'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
op|'.'
name|'unittest'
name|'import'
name|'TestCase'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'http'
name|'import'
name|'NOT_FOUND'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'static'
name|'import'
name|'Data'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'vhost'
name|'import'
name|'NameVirtualHost'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'test'
op|'.'
name|'test_web'
name|'import'
name|'DummyRequest'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'test'
op|'.'
name|'_util'
name|'import'
name|'_render'
newline|'\n'
nl|'\n'
DECL|class|NameVirtualHostTests
name|'class'
name|'NameVirtualHostTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{NameVirtualHost}.\n    """'
newline|'\n'
DECL|member|test_renderWithoutHost
name|'def'
name|'test_renderWithoutHost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{NameVirtualHost.render} returns the result of rendering the\n        instance\'s C{default} if it is not C{None} and there is no I{Host}\n        header in the request.\n        """'
newline|'\n'
name|'virtualHostResource'
op|'='
name|'NameVirtualHost'
op|'('
op|')'
newline|'\n'
name|'virtualHostResource'
op|'.'
name|'default'
op|'='
name|'Data'
op|'('
string|'"correct result"'
op|','
string|'""'
op|')'
newline|'\n'
name|'request'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'virtualHostResource'
op|'.'
name|'render'
op|'('
name|'request'
op|')'
op|','
string|'"correct result"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_renderWithoutHostNoDefault
dedent|''
name|'def'
name|'test_renderWithoutHostNoDefault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{NameVirtualHost.render} returns a response with a status of I{NOT\n        FOUND} if the instance\'s C{default} is C{None} and there is no I{Host}\n        header in the request.\n        """'
newline|'\n'
name|'virtualHostResource'
op|'='
name|'NameVirtualHost'
op|'('
op|')'
newline|'\n'
name|'request'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'d'
op|'='
name|'_render'
op|'('
name|'virtualHostResource'
op|','
name|'request'
op|')'
newline|'\n'
DECL|function|cbRendered
name|'def'
name|'cbRendered'
op|'('
name|'ignored'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'request'
op|'.'
name|'responseCode'
op|','
name|'NOT_FOUND'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'cbRendered'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_renderWithHost
dedent|''
name|'def'
name|'test_renderWithHost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{NameVirtualHost.render} returns the result of rendering the resource\n        which is the value in the instance\'s C{host} dictionary corresponding\n        to the key indicated by the value of the I{Host} header in the request.\n        """'
newline|'\n'
name|'virtualHostResource'
op|'='
name|'NameVirtualHost'
op|'('
op|')'
newline|'\n'
name|'virtualHostResource'
op|'.'
name|'addHost'
op|'('
string|"'example.org'"
op|','
name|'Data'
op|'('
string|'"winner"'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'host'"
op|']'
op|'='
string|"'example.org'"
newline|'\n'
name|'d'
op|'='
name|'_render'
op|'('
name|'virtualHostResource'
op|','
name|'request'
op|')'
newline|'\n'
DECL|function|cbRendered
name|'def'
name|'cbRendered'
op|'('
name|'ignored'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'request'
op|'.'
name|'written'
op|')'
op|','
string|'"winner"'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'cbRendered'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
comment|'# The port portion of the Host header should not be considered.'
nl|'\n'
name|'requestWithPort'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'requestWithPort'
op|'.'
name|'headers'
op|'['
string|"'host'"
op|']'
op|'='
string|"'example.org:8000'"
newline|'\n'
name|'dWithPort'
op|'='
name|'_render'
op|'('
name|'virtualHostResource'
op|','
name|'requestWithPort'
op|')'
newline|'\n'
DECL|function|cbRendered
name|'def'
name|'cbRendered'
op|'('
name|'ignored'
op|','
name|'requestWithPort'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'requestWithPort'
op|'.'
name|'written'
op|')'
op|','
string|'"winner"'
op|')'
newline|'\n'
dedent|''
name|'dWithPort'
op|'.'
name|'addCallback'
op|'('
name|'cbRendered'
op|','
name|'requestWithPort'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'gatherResults'
op|'('
op|'['
name|'d'
op|','
name|'dWithPort'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_renderWithUnknownHost
dedent|''
name|'def'
name|'test_renderWithUnknownHost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{NameVirtualHost.render} returns the result of rendering the\n        instance\'s C{default} if it is not C{None} and there is no host\n        matching the value of the I{Host} header in the request.\n        """'
newline|'\n'
name|'virtualHostResource'
op|'='
name|'NameVirtualHost'
op|'('
op|')'
newline|'\n'
name|'virtualHostResource'
op|'.'
name|'default'
op|'='
name|'Data'
op|'('
string|'"correct data"'
op|','
string|'""'
op|')'
newline|'\n'
name|'request'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'host'"
op|']'
op|'='
string|"'example.com'"
newline|'\n'
name|'d'
op|'='
name|'_render'
op|'('
name|'virtualHostResource'
op|','
name|'request'
op|')'
newline|'\n'
DECL|function|cbRendered
name|'def'
name|'cbRendered'
op|'('
name|'ignored'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'request'
op|'.'
name|'written'
op|')'
op|','
string|'"correct data"'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'cbRendered'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_renderWithUnknownHostNoDefault
dedent|''
name|'def'
name|'test_renderWithUnknownHostNoDefault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{NameVirtualHost.render} returns a response with a status of I{NOT\n        FOUND} if the instance\'s C{default} is C{None} and there is no host\n        matching the value of the I{Host} header in the request.\n        """'
newline|'\n'
name|'virtualHostResource'
op|'='
name|'NameVirtualHost'
op|'('
op|')'
newline|'\n'
name|'request'
op|'='
name|'DummyRequest'
op|'('
op|'['
string|"''"
op|']'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'host'"
op|']'
op|'='
string|"'example.com'"
newline|'\n'
name|'d'
op|'='
name|'_render'
op|'('
name|'virtualHostResource'
op|','
name|'request'
op|')'
newline|'\n'
DECL|function|cbRendered
name|'def'
name|'cbRendered'
op|'('
name|'ignored'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'request'
op|'.'
name|'responseCode'
op|','
name|'NOT_FOUND'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'cbRendered'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
