begin_unit
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nXMPP-specific SASL profile.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'protocols'
op|'.'
name|'jabber'
name|'import'
name|'sasl_mechanisms'
op|','
name|'xmlstream'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'xish'
name|'import'
name|'domish'
newline|'\n'
nl|'\n'
comment|'# The b64decode and b64encode functions from the base64 module are new in'
nl|'\n'
comment|'# Python 2.4. For Python 2.3 compatibility, the legacy interface is used while'
nl|'\n'
comment|'# working around MIMEisms.'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'base64'
name|'import'
name|'b64decode'
op|','
name|'b64encode'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'base64'
newline|'\n'
nl|'\n'
DECL|function|b64encode
name|'def'
name|'b64encode'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'""'
op|'.'
name|'join'
op|'('
name|'base64'
op|'.'
name|'encodestring'
op|'('
name|'s'
op|')'
op|'.'
name|'split'
op|'('
string|'"\\n"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|b64decode
dedent|''
name|'b64decode'
op|'='
name|'base64'
op|'.'
name|'decodestring'
newline|'\n'
nl|'\n'
DECL|variable|NS_XMPP_SASL
dedent|''
name|'NS_XMPP_SASL'
op|'='
string|"'urn:ietf:params:xml:ns:xmpp-sasl'"
newline|'\n'
nl|'\n'
DECL|function|get_mechanisms
name|'def'
name|'get_mechanisms'
op|'('
name|'xs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Parse the SASL feature to extract the available mechanism names.\n    """'
newline|'\n'
name|'mechanisms'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'element'
name|'in'
name|'xs'
op|'.'
name|'features'
op|'['
op|'('
name|'NS_XMPP_SASL'
op|','
string|"'mechanisms'"
op|')'
op|']'
op|'.'
name|'elements'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'element'
op|'.'
name|'name'
op|'=='
string|"'mechanism'"
op|':'
newline|'\n'
indent|'            '
name|'mechanisms'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'element'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mechanisms'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SASLError
dedent|''
name|'class'
name|'SASLError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    SASL base exception.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SASLNoAcceptableMechanism
dedent|''
name|'class'
name|'SASLNoAcceptableMechanism'
op|'('
name|'SASLError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The server did not present an acceptable SASL mechanism.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SASLAuthError
dedent|''
name|'class'
name|'SASLAuthError'
op|'('
name|'SASLError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    SASL Authentication failed.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'condition'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'condition'
op|'='
name|'condition'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"SASLAuthError with condition %r"'
op|'%'
name|'self'
op|'.'
name|'condition'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SASLIncorrectEncodingError
dedent|''
dedent|''
name|'class'
name|'SASLIncorrectEncodingError'
op|'('
name|'SASLError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    SASL base64 encoding was incorrect.\n\n    RFC 3920 specifies that any characters not in the base64 alphabet\n    and padding characters present elsewhere than at the end of the string\n    MUST be rejected. See also L{fromBase64}.\n\n    This exception is raised whenever the encoded string does not adhere\n    to these additional restrictions or when the decoding itself fails.\n\n    The recommended behaviour for so-called receiving entities (like servers in\n    client-to-server connections, see RFC 3920 for terminology) is to fail the\n    SASL negotiation with a C{\'incorrect-encoding\'} condition. For initiating\n    entities, one should assume the receiving entity to be either buggy or\n    malevolent. The stream should be terminated and reconnecting is not\n    advised.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|base64Pattern
dedent|''
name|'base64Pattern'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^[0-9A-Za-z+/]*[0-9A-Za-z+/=]{,2}$"'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fromBase64
name|'def'
name|'fromBase64'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Decode base64 encoded string.\n\n    This helper performs regular decoding of a base64 encoded string, but also\n    rejects any characters that are not in the base64 alphabet and padding\n    occurring elsewhere from the last or last two characters, as specified in\n    section 14.9 of RFC 3920. This safeguards against various attack vectors\n    among which the creation of a covert channel that "leaks" information.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'base64Pattern'
op|'.'
name|'match'
op|'('
name|'s'
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'SASLIncorrectEncodingError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'b64decode'
op|'('
name|'s'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'SASLIncorrectEncodingError'
op|'('
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|SASLInitiatingInitializer
dedent|''
dedent|''
name|'class'
name|'SASLInitiatingInitializer'
op|'('
name|'xmlstream'
op|'.'
name|'BaseFeatureInitiatingInitializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Stream initializer that performs SASL authentication.\n\n    The supported mechanisms by this initializer are C{DIGEST-MD5}, C{PLAIN}\n    and C{ANONYMOUS}. The C{ANONYMOUS} SASL mechanism is used when the JID, set\n    on the authenticator, does not have a localpart (username), requesting an\n    anonymous session where the username is generated by the server.\n    Otherwise, C{DIGEST-MD5} and C{PLAIN} are attempted, in that order.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|feature
name|'feature'
op|'='
op|'('
name|'NS_XMPP_SASL'
op|','
string|"'mechanisms'"
op|')'
newline|'\n'
DECL|variable|_deferred
name|'_deferred'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|setMechanism
name|'def'
name|'setMechanism'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Select and setup authentication mechanism.\n\n        Uses the authenticator\'s C{jid} and C{password} attribute for the\n        authentication credentials. If no supported SASL mechanisms are\n        advertized by the receiving party, a failing deferred is returned with\n        a L{SASLNoAcceptableMechanism} exception.\n        """'
newline|'\n'
nl|'\n'
name|'jid'
op|'='
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'authenticator'
op|'.'
name|'jid'
newline|'\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'authenticator'
op|'.'
name|'password'
newline|'\n'
nl|'\n'
name|'mechanisms'
op|'='
name|'get_mechanisms'
op|'('
name|'self'
op|'.'
name|'xmlstream'
op|')'
newline|'\n'
name|'if'
name|'jid'
op|'.'
name|'user'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'DIGEST-MD5'"
name|'in'
name|'mechanisms'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mechanism'
op|'='
name|'sasl_mechanisms'
op|'.'
name|'DigestMD5'
op|'('
string|"'xmpp'"
op|','
name|'jid'
op|'.'
name|'host'
op|','
name|'None'
op|','
nl|'\n'
name|'jid'
op|'.'
name|'user'
op|','
name|'password'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'PLAIN'"
name|'in'
name|'mechanisms'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mechanism'
op|'='
name|'sasl_mechanisms'
op|'.'
name|'Plain'
op|'('
name|'None'
op|','
name|'jid'
op|'.'
name|'user'
op|','
name|'password'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'SASLNoAcceptableMechanism'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'ANONYMOUS'"
name|'in'
name|'mechanisms'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mechanism'
op|'='
name|'sasl_mechanisms'
op|'.'
name|'Anonymous'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'SASLNoAcceptableMechanism'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|start
dedent|''
dedent|''
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Start SASL authentication exchange.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'setMechanism'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_deferred'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addObserver'
op|'('
string|"'/challenge'"
op|','
name|'self'
op|'.'
name|'onChallenge'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addOnetimeObserver'
op|'('
string|"'/success'"
op|','
name|'self'
op|'.'
name|'onSuccess'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addOnetimeObserver'
op|'('
string|"'/failure'"
op|','
name|'self'
op|'.'
name|'onFailure'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sendAuth'
op|'('
name|'self'
op|'.'
name|'mechanism'
op|'.'
name|'getInitialResponse'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_deferred'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|sendAuth
dedent|''
name|'def'
name|'sendAuth'
op|'('
name|'self'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initiate authentication protocol exchange.\n\n        If an initial client response is given in C{data}, it will be\n        sent along.\n\n        @param data: initial client response.\n        @type data: L{str} or L{None}.\n        """'
newline|'\n'
nl|'\n'
name|'auth'
op|'='
name|'domish'
op|'.'
name|'Element'
op|'('
op|'('
name|'NS_XMPP_SASL'
op|','
string|"'auth'"
op|')'
op|')'
newline|'\n'
name|'auth'
op|'['
string|"'mechanism'"
op|']'
op|'='
name|'self'
op|'.'
name|'mechanism'
op|'.'
name|'name'
newline|'\n'
name|'if'
name|'data'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'auth'
op|'.'
name|'addContent'
op|'('
name|'b64encode'
op|'('
name|'data'
op|')'
name|'or'
string|"'='"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'send'
op|'('
name|'auth'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|sendResponse
dedent|''
name|'def'
name|'sendResponse'
op|'('
name|'self'
op|','
name|'data'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send response to a challenge.\n\n        @param data: client response.\n        @type data: L{str}.\n        """'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'domish'
op|'.'
name|'Element'
op|'('
op|'('
name|'NS_XMPP_SASL'
op|','
string|"'response'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'response'
op|'.'
name|'addContent'
op|'('
name|'b64encode'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'send'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|onChallenge
dedent|''
name|'def'
name|'onChallenge'
op|'('
name|'self'
op|','
name|'element'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Parse challenge and send response from the mechanism.\n\n        @param element: the challenge protocol element.\n        @type element: L{domish.Element}.\n        """'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'challenge'
op|'='
name|'fromBase64'
op|'('
name|'str'
op|'('
name|'element'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'SASLIncorrectEncodingError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_deferred'
op|'.'
name|'errback'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sendResponse'
op|'('
name|'self'
op|'.'
name|'mechanism'
op|'.'
name|'getResponse'
op|'('
name|'challenge'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|onSuccess
dedent|''
dedent|''
name|'def'
name|'onSuccess'
op|'('
name|'self'
op|','
name|'success'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Clean up observers, reset the XML stream and send a new header.\n\n        @param success: the success protocol element. For now unused, but\n                        could hold additional data.\n        @type success: L{domish.Element}\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'removeObserver'
op|'('
string|"'/challenge'"
op|','
name|'self'
op|'.'
name|'onChallenge'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'removeObserver'
op|'('
string|"'/failure'"
op|','
name|'self'
op|'.'
name|'onFailure'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'sendHeader'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_deferred'
op|'.'
name|'callback'
op|'('
name|'xmlstream'
op|'.'
name|'Reset'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|onFailure
dedent|''
name|'def'
name|'onFailure'
op|'('
name|'self'
op|','
name|'failure'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Clean up observers, parse the failure and errback the deferred.\n\n        @param failure: the failure protocol element. Holds details on\n                        the error condition.\n        @type failure: L{domish.Element}\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'removeObserver'
op|'('
string|"'/challenge'"
op|','
name|'self'
op|'.'
name|'onChallenge'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'removeObserver'
op|'('
string|"'/success'"
op|','
name|'self'
op|'.'
name|'onSuccess'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'condition'
op|'='
name|'failure'
op|'.'
name|'firstChildElement'
op|'('
op|')'
op|'.'
name|'name'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'condition'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_deferred'
op|'.'
name|'errback'
op|'('
name|'SASLAuthError'
op|'('
name|'condition'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
