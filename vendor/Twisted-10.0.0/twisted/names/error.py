begin_unit
comment|'# -*- test-case-name: twisted.names.test -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nException class definitions for Twisted Names.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'defer'
name|'import'
name|'TimeoutError'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DomainError
name|'class'
name|'DomainError'
op|'('
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a lookup failed because there were no records matching the given\n    C{name, class, type} triple.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthoritativeDomainError
dedent|''
name|'class'
name|'AuthoritativeDomainError'
op|'('
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a lookup failed for a name for which this server is authoritative\n    because there were no records matching the given C{name, class, type}\n    triple.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSQueryTimeoutError
dedent|''
name|'class'
name|'DNSQueryTimeoutError'
op|'('
name|'TimeoutError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a lookup failed due to a timeout.\n\n    @ivar id: The id of the message which timed out.\n    """'
newline|'\n'
DECL|member|__init__
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
name|'TimeoutError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSFormatError
dedent|''
dedent|''
name|'class'
name|'DNSFormatError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with a result of L{twisted.names.dns.EFORMAT}.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSServerError
dedent|''
name|'class'
name|'DNSServerError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with a result of L{twisted.names.dns.ESERVER}.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSNameError
dedent|''
name|'class'
name|'DNSNameError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with a result of L{twisted.names.dns.ENAME}.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSNotImplementedError
dedent|''
name|'class'
name|'DNSNotImplementedError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with a result of L{twisted.names.dns.ENOTIMP}.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSQueryRefusedError
dedent|''
name|'class'
name|'DNSQueryRefusedError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with a result of L{twisted.names.dns.EREFUSED}.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSUnknownError
dedent|''
name|'class'
name|'DNSUnknownError'
op|'('
name|'DomainError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed with an unknown result.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResolverError
dedent|''
name|'class'
name|'ResolverError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Indicates a query failed because of a decision made by the local\n    resolver object.\n    """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|__all__
dedent|''
name|'__all__'
op|'='
op|'['
nl|'\n'
string|"'DomainError'"
op|','
string|"'AuthoritativeDomainError'"
op|','
string|"'DNSQueryTimeoutError'"
op|','
nl|'\n'
nl|'\n'
string|"'DNSFormatError'"
op|','
string|"'DNSServerError'"
op|','
string|"'DNSNameError'"
op|','
nl|'\n'
string|"'DNSNotImplementedError'"
op|','
string|"'DNSQueryRefusedError'"
op|','
nl|'\n'
string|"'DNSUnknownError'"
op|','
string|"'ResolverError'"
op|']'
newline|'\n'
endmarker|''
end_unit
