begin_unit
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'resource'
name|'import'
name|'Resource'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ReportResource
name|'class'
name|'ReportResource'
op|'('
name|'Resource'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|render_GET
indent|'    '
name|'def'
name|'render_GET'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'request'
op|'.'
name|'path'
newline|'\n'
name|'_'
op|','
name|'host'
op|','
name|'port'
op|'='
name|'request'
op|'.'
name|'getHost'
op|'('
op|')'
newline|'\n'
name|'url'
op|'='
name|'request'
op|'.'
name|'prePathURL'
op|'('
op|')'
newline|'\n'
name|'uri'
op|'='
name|'request'
op|'.'
name|'uri'
newline|'\n'
name|'secure'
op|'='
op|'('
name|'request'
op|'.'
name|'isSecure'
op|'('
op|')'
name|'and'
string|'"securely"'
op|')'
name|'or'
string|'"insecurely"'
newline|'\n'
name|'return'
op|'('
string|'"""\\\n<HTML>\n    <HEAD><TITLE>Welcome To Twisted Python Reporting</title></head>\n\n    <BODY><H1>Welcome To Twisted Python Reporting</H1>\n    <UL>\n    <LI>The path to me is %(path)s\n    <LI>The host I\'m on is %(host)s\n    <LI>The port I\'m on is %(port)s\n    <LI>I was accessed %(secure)s\n    <LI>A URL to me is %(url)s\n    <LI>My URI to me is %(uri)s\n    </UL>\n    </body>\n</html>"""'
op|'%'
name|'vars'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|resource
dedent|''
dedent|''
name|'resource'
op|'='
name|'ReportResource'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
