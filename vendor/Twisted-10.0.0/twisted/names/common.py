begin_unit
comment|'# -*- test-case-name: twisted.names.test -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nBase functionality useful to various parts of Twisted Names.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'names'
name|'import'
name|'dns'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'names'
op|'.'
name|'error'
name|'import'
name|'DNSFormatError'
op|','
name|'DNSServerError'
op|','
name|'DNSNameError'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'names'
op|'.'
name|'error'
name|'import'
name|'DNSNotImplementedError'
op|','
name|'DNSQueryRefusedError'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'names'
op|'.'
name|'error'
name|'import'
name|'DNSUnknownError'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
op|','
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
newline|'\n'
nl|'\n'
DECL|variable|EMPTY_RESULT
name|'EMPTY_RESULT'
op|'='
op|'('
op|')'
op|','
op|'('
op|')'
op|','
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|ResolverBase
name|'class'
name|'ResolverBase'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    L{ResolverBase} is a base class for L{IResolver} implementations which\n    deals with a lot of the boilerplate of implementing all of the lookup\n    methods.\n\n    @cvar _errormap: A C{dict} mapping DNS protocol failure response codes\n        to exception classes which will be used to represent those failures.\n    """'
newline|'\n'
DECL|variable|_errormap
name|'_errormap'
op|'='
op|'{'
nl|'\n'
name|'dns'
op|'.'
name|'EFORMAT'
op|':'
name|'DNSFormatError'
op|','
nl|'\n'
name|'dns'
op|'.'
name|'ESERVER'
op|':'
name|'DNSServerError'
op|','
nl|'\n'
name|'dns'
op|'.'
name|'ENAME'
op|':'
name|'DNSNameError'
op|','
nl|'\n'
name|'dns'
op|'.'
name|'ENOTIMP'
op|':'
name|'DNSNotImplementedError'
op|','
nl|'\n'
name|'dns'
op|'.'
name|'EREFUSED'
op|':'
name|'DNSQueryRefusedError'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|typeToMethod
name|'typeToMethod'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'typeToMethod'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'typeToMethod'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'typeToMethod'
op|'['
name|'k'
op|']'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|exceptionForCode
dedent|''
dedent|''
name|'def'
name|'exceptionForCode'
op|'('
name|'self'
op|','
name|'responseCode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Convert a response code (one of the possible values of\n        L{dns.Message.rCode} to an exception instance representing it.\n\n        @since: 10.0\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_errormap'
op|'.'
name|'get'
op|'('
name|'responseCode'
op|','
name|'DNSUnknownError'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|query
dedent|''
name|'def'
name|'query'
op|'('
name|'self'
op|','
name|'query'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'typeToMethod'
op|'['
name|'query'
op|'.'
name|'type'
op|']'
op|'('
name|'str'
op|'('
name|'query'
op|'.'
name|'name'
op|')'
op|','
name|'timeout'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'defer'
op|'.'
name|'fail'
op|'('
name|'failure'
op|'.'
name|'Failure'
op|'('
name|'NotImplementedError'
op|'('
name|'str'
op|'('
name|'self'
op|'.'
name|'__class__'
op|')'
op|'+'
string|'" "'
op|'+'
name|'str'
op|'('
name|'query'
op|'.'
name|'type'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_lookup
dedent|''
dedent|''
name|'def'
name|'_lookup'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'cls'
op|','
name|'type'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'defer'
op|'.'
name|'fail'
op|'('
name|'NotImplementedError'
op|'('
string|'"ResolverBase._lookup"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupAddress
dedent|''
name|'def'
name|'lookupAddress'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupAddress\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'A'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupIPV6Address
dedent|''
name|'def'
name|'lookupIPV6Address'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupIPV6Address\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'AAAA'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupAddress6
dedent|''
name|'def'
name|'lookupAddress6'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupAddress6\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'A6'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupMailExchange
dedent|''
name|'def'
name|'lookupMailExchange'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupMailExchange\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'MX'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupNameservers
dedent|''
name|'def'
name|'lookupNameservers'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupNameservers\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'NS'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupCanonicalName
dedent|''
name|'def'
name|'lookupCanonicalName'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupCanonicalName\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'CNAME'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupMailBox
dedent|''
name|'def'
name|'lookupMailBox'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupMailBox\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'MB'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupMailGroup
dedent|''
name|'def'
name|'lookupMailGroup'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupMailGroup\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'MG'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupMailRename
dedent|''
name|'def'
name|'lookupMailRename'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupMailRename\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'MR'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupPointer
dedent|''
name|'def'
name|'lookupPointer'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupPointer\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'PTR'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupAuthority
dedent|''
name|'def'
name|'lookupAuthority'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupAuthority\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'SOA'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupNull
dedent|''
name|'def'
name|'lookupNull'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupNull\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'NULL'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupWellKnownServices
dedent|''
name|'def'
name|'lookupWellKnownServices'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupWellKnownServices\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'WKS'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupService
dedent|''
name|'def'
name|'lookupService'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupService\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'SRV'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupHostInfo
dedent|''
name|'def'
name|'lookupHostInfo'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupHostInfo\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'HINFO'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupMailboxInfo
dedent|''
name|'def'
name|'lookupMailboxInfo'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupMailboxInfo\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'MINFO'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupText
dedent|''
name|'def'
name|'lookupText'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupText\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'TXT'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupResponsibility
dedent|''
name|'def'
name|'lookupResponsibility'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupResponsibility\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'RP'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupAFSDatabase
dedent|''
name|'def'
name|'lookupAFSDatabase'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupAFSDatabase\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'AFSDB'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookupZone
dedent|''
name|'def'
name|'lookupZone'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupZone\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'AXFR'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|lookupNamingAuthorityPointer
dedent|''
name|'def'
name|'lookupNamingAuthorityPointer'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupNamingAuthorityPointer\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'NAPTR'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|lookupAllRecords
dedent|''
name|'def'
name|'lookupAllRecords'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.lookupAllRecords\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'name'
op|','
name|'dns'
op|'.'
name|'IN'
op|','
name|'dns'
op|'.'
name|'ALL_RECORDS'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getHostByName
dedent|''
name|'def'
name|'getHostByName'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'timeout'
op|'='
name|'None'
op|','
name|'effort'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @see: twisted.names.client.getHostByName\n        """'
newline|'\n'
comment|'# XXX - respect timeout'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'lookupAllRecords'
op|'('
name|'name'
op|','
name|'timeout'
nl|'\n'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_cbRecords'
op|','
name|'name'
op|','
name|'effort'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cbRecords
dedent|''
name|'def'
name|'_cbRecords'
op|'('
name|'self'
op|','
op|'('
name|'ans'
op|','
name|'auth'
op|','
name|'add'
op|')'
op|','
name|'name'
op|','
name|'effort'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'extractRecord'
op|'('
name|'self'
op|','
name|'dns'
op|'.'
name|'Name'
op|'('
name|'name'
op|')'
op|','
name|'ans'
op|'+'
name|'auth'
op|'+'
name|'add'
op|','
name|'effort'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'error'
op|'.'
name|'DNSLookupError'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|function|extractRecord
dedent|''
dedent|''
name|'def'
name|'extractRecord'
op|'('
name|'resolver'
op|','
name|'name'
op|','
name|'answers'
op|','
name|'level'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'level'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'socket'
op|','
string|"'inet_ntop'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'r'
name|'in'
name|'answers'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'r'
op|'.'
name|'name'
op|'=='
name|'name'
name|'and'
name|'r'
op|'.'
name|'type'
op|'=='
name|'dns'
op|'.'
name|'A6'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'socket'
op|'.'
name|'inet_ntop'
op|'('
name|'socket'
op|'.'
name|'AF_INET6'
op|','
name|'r'
op|'.'
name|'payload'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'r'
name|'in'
name|'answers'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'r'
op|'.'
name|'name'
op|'=='
name|'name'
name|'and'
name|'r'
op|'.'
name|'type'
op|'=='
name|'dns'
op|'.'
name|'AAAA'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'socket'
op|'.'
name|'inet_ntop'
op|'('
name|'socket'
op|'.'
name|'AF_INET6'
op|','
name|'r'
op|'.'
name|'payload'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'r'
name|'in'
name|'answers'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'r'
op|'.'
name|'name'
op|'=='
name|'name'
name|'and'
name|'r'
op|'.'
name|'type'
op|'=='
name|'dns'
op|'.'
name|'A'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'socket'
op|'.'
name|'inet_ntop'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'r'
op|'.'
name|'payload'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'r'
name|'in'
name|'answers'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'r'
op|'.'
name|'name'
op|'=='
name|'name'
name|'and'
name|'r'
op|'.'
name|'type'
op|'=='
name|'dns'
op|'.'
name|'CNAME'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'extractRecord'
op|'('
name|'resolver'
op|','
name|'r'
op|'.'
name|'payload'
op|'.'
name|'name'
op|','
name|'answers'
op|','
name|'level'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'resolver'
op|'.'
name|'getHostByName'
op|'('
name|'str'
op|'('
name|'r'
op|'.'
name|'payload'
op|'.'
name|'name'
op|')'
op|','
name|'effort'
op|'='
name|'level'
op|'-'
number|'1'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
comment|"# No answers, but maybe there's a hint at who we should be asking about this"
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'r'
name|'in'
name|'answers'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'r'
op|'.'
name|'type'
op|'=='
name|'dns'
op|'.'
name|'NS'
op|':'
newline|'\n'
indent|'            '
name|'from'
name|'twisted'
op|'.'
name|'names'
name|'import'
name|'client'
newline|'\n'
name|'r'
op|'='
name|'client'
op|'.'
name|'Resolver'
op|'('
name|'servers'
op|'='
op|'['
op|'('
name|'str'
op|'('
name|'r'
op|'.'
name|'payload'
op|'.'
name|'name'
op|')'
op|','
name|'dns'
op|'.'
name|'PORT'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'r'
op|'.'
name|'lookupAddress'
op|'('
name|'str'
op|'('
name|'name'
op|')'
nl|'\n'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
op|'('
name|'ans'
op|','
name|'auth'
op|','
name|'add'
op|')'
op|':'
name|'extractRecord'
op|'('
name|'r'
op|','
name|'name'
op|','
name|'ans'
op|'+'
name|'auth'
op|'+'
name|'add'
op|','
name|'level'
op|'-'
number|'1'
op|')'
nl|'\n'
op|')'
op|'.'
name|'addBoth'
op|'('
name|'lambda'
name|'passthrough'
op|':'
op|'('
name|'r'
op|'.'
name|'protocol'
op|'.'
name|'transport'
op|'.'
name|'stopListening'
op|'('
op|')'
op|','
name|'passthrough'
op|')'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|typeToMethod
dedent|''
dedent|''
dedent|''
name|'typeToMethod'
op|'='
op|'{'
nl|'\n'
name|'dns'
op|'.'
name|'A'
op|':'
string|"'lookupAddress'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'AAAA'
op|':'
string|"'lookupIPV6Address'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'A6'
op|':'
string|"'lookupAddress6'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'NS'
op|':'
string|"'lookupNameservers'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'CNAME'
op|':'
string|"'lookupCanonicalName'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'SOA'
op|':'
string|"'lookupAuthority'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'MB'
op|':'
string|"'lookupMailBox'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'MG'
op|':'
string|"'lookupMailGroup'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'MR'
op|':'
string|"'lookupMailRename'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'NULL'
op|':'
string|"'lookupNull'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'WKS'
op|':'
string|"'lookupWellKnownServices'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'PTR'
op|':'
string|"'lookupPointer'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'HINFO'
op|':'
string|"'lookupHostInfo'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'MINFO'
op|':'
string|"'lookupMailboxInfo'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'MX'
op|':'
string|"'lookupMailExchange'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'TXT'
op|':'
string|"'lookupText'"
op|','
nl|'\n'
nl|'\n'
name|'dns'
op|'.'
name|'RP'
op|':'
string|"'lookupResponsibility'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'AFSDB'
op|':'
string|"'lookupAFSDatabase'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'SRV'
op|':'
string|"'lookupService'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'NAPTR'
op|':'
string|"'lookupNamingAuthorityPointer'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'AXFR'
op|':'
string|"'lookupZone'"
op|','
nl|'\n'
name|'dns'
op|'.'
name|'ALL_RECORDS'
op|':'
string|"'lookupAllRecords'"
op|','
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit
