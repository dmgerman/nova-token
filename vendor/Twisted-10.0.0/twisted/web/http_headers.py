begin_unit
comment|'# -*- test-case-name: twisted.web.test.test_http_headers'
nl|'\n'
comment|'# Copyright (c) 2008-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nAn API for storing HTTP header names and values.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'UserDict'
name|'import'
name|'DictMixin'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dashCapitalize
name|'def'
name|'_dashCapitalize'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return a string which is capitalized using \'-\' as a word separator.\n\n    @param name: The name of the header to capitalize.\n    @type name: str\n\n    @return: The given header capitalized using \'-\' as a word separator.\n    @rtype: str\n    """'
newline|'\n'
name|'return'
string|"'-'"
op|'.'
name|'join'
op|'('
op|'['
name|'word'
op|'.'
name|'capitalize'
op|'('
op|')'
name|'for'
name|'word'
name|'in'
name|'name'
op|'.'
name|'split'
op|'('
string|"'-'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|_DictHeaders
dedent|''
name|'class'
name|'_DictHeaders'
op|'('
name|'DictMixin'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A C{dict}-like wrapper around L{Headers} to provide backwards compatibility\n    for L{Request.received_headers} and L{Request.headers} which used to be\n    plain C{dict} instances.\n\n    @type _headers: L{Headers}\n    @ivar _headers: The real header storage object.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'headers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_headers'
op|'='
name|'headers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the last value for header of C{key}.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'hasHeader'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'getRawHeaders'
op|'('
name|'key'
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'raise'
name|'KeyError'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Set the given header.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'setRawHeaders'
op|'('
name|'key'
op|','
op|'['
name|'value'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Delete the given header.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'hasHeader'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'removeHeader'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'KeyError'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|keys
dedent|''
dedent|''
name|'def'
name|'keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a list of all header names.\n        """'
newline|'\n'
name|'return'
op|'['
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'getAllRawHeaders'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|copy
dedent|''
name|'def'
name|'copy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a C{dict} mapping each header name to the last corresponding\n        header value.\n        """'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'self'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Python 2.3 DictMixin.setdefault is defined so as not to have a default'
nl|'\n'
comment|'# for the value parameter.  This is necessary to make this setdefault look'
nl|'\n'
comment|'# like dict.setdefault on Python 2.3. -exarkun'
nl|'\n'
DECL|member|setdefault
dedent|''
name|'def'
name|'setdefault'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Retrieve the last value for the given header name.  If there are no\n        values present for that header, set the value to C{value} and return\n        that instead.  Note that C{None} is the default for C{value} for\n        backwards compatibility, but header values may only be of type C{str}.\n        """'
newline|'\n'
name|'return'
name|'DictMixin'
op|'.'
name|'setdefault'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# The remaining methods are only for efficiency.  The same behavior'
nl|'\n'
comment|'# should remain even if they are removed.  For details, see'
nl|'\n'
comment|'# <http://docs.python.org/lib/module-UserDict.html>.'
nl|'\n'
comment|'# -exarkun'
nl|'\n'
DECL|member|__contains__
dedent|''
name|'def'
name|'__contains__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return C{True} if the named header is present, C{False} otherwise.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'getRawHeaders'
op|'('
name|'name'
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return an iterator of the lowercase name of each header present.\n        """'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'getAllRawHeaders'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|iteritems
dedent|''
dedent|''
name|'def'
name|'iteritems'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return an iterable of two-tuples of each lower-case header name and the\n        last value for that header.\n        """'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'getAllRawHeaders'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
op|','
name|'v'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|Headers
dedent|''
dedent|''
dedent|''
name|'class'
name|'Headers'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This class stores the HTTP headers as both a parsed representation\n    and the raw string representation. It converts between the two on\n    demand.\n\n    @cvar _caseMappings: A C{dict} that maps lowercase header names\n        to their canonicalized representation.\n\n    @ivar _rawHeaders: A C{dict} mapping header names as C{str} to C{lists} of\n        header values as C{str}.\n    """'
newline|'\n'
DECL|variable|_caseMappings
name|'_caseMappings'
op|'='
op|'{'
string|"'www-authenticate'"
op|':'
string|"'WWW-Authenticate'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'rawHeaders'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_rawHeaders'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'rawHeaders'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'name'
op|','
name|'values'
name|'in'
name|'rawHeaders'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'setRawHeaders'
op|'('
name|'name'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a string fully describing the headers set on this object.\n        """'
newline|'\n'
name|'return'
string|"'%s(%r)'"
op|'%'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'self'
op|'.'
name|'_rawHeaders'
op|','
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|__cmp__
dedent|''
name|'def'
name|'__cmp__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Define L{Headers} instances as being equal to each other if they have\n        the same raw headers.\n        """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'other'
op|','
name|'Headers'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cmp'
op|'('
name|'self'
op|'.'
name|'_rawHeaders'
op|','
name|'other'
op|'.'
name|'_rawHeaders'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'NotImplemented'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|hasHeader
dedent|''
name|'def'
name|'hasHeader'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check for the existence of a given header.\n\n        @type name: C{str}\n        @param name: The name of the HTTP header to check for.\n\n        @rtype: C{bool}\n        @return: C{True} if the header exists, otherwise C{False}.\n        """'
newline|'\n'
name|'return'
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
name|'self'
op|'.'
name|'_rawHeaders'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|removeHeader
dedent|''
name|'def'
name|'removeHeader'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove the named header from this header object.\n\n        @type name: C{str}\n        @param name: The name of the HTTP header to remove.\n\n        @return: C{None}\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_rawHeaders'
op|'.'
name|'pop'
op|'('
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setRawHeaders
dedent|''
name|'def'
name|'setRawHeaders'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets the raw representation of the given header.\n\n        @type name: C{str}\n        @param name: The name of the HTTP header to set the values for.\n\n        @type values: C{list}\n        @param values: A list of strings each one being a header value of\n            the given name.\n\n        @return: C{None}\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_rawHeaders'
op|'['
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
op|']'
op|'='
name|'values'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|addRawHeader
dedent|''
name|'def'
name|'addRawHeader'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add a new raw value for the given header.\n\n        @type name: C{str}\n        @param name: The name of the header for which to set the value.\n\n        @type value: C{str}\n        @param value: The value to set for the named header.\n        """'
newline|'\n'
name|'values'
op|'='
name|'self'
op|'.'
name|'getRawHeaders'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'values'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setRawHeaders'
op|'('
name|'name'
op|','
op|'['
name|'value'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'.'
name|'append'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getRawHeaders
dedent|''
dedent|''
name|'def'
name|'getRawHeaders'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns a list of headers matching the given name as the raw string\n        given.\n\n        @type name: C{str}\n        @param name: The name of the HTTP header to get the values of.\n\n        @param default: The value to return if no header with the given C{name}\n            exists.\n\n        @rtype: C{list}\n        @return: A C{list} of values for the given header.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_rawHeaders'
op|'.'
name|'get'
op|'('
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getAllRawHeaders
dedent|''
name|'def'
name|'getAllRawHeaders'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return an iterator of key, value pairs of all headers contained in this\n        object, as strings.  The keys are capitalized in canonical\n        capitalization.\n        """'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_rawHeaders'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'_canonicalNameCaps'
op|'('
name|'k'
op|')'
op|','
name|'v'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_canonicalNameCaps
dedent|''
dedent|''
name|'def'
name|'_canonicalNameCaps'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the canonical name for the given header.\n\n        @type name: C{str}\n        @param name: The all-lowercase header name to capitalize in its\n            canonical form.\n\n        @rtype: C{str}\n        @return: The canonical name of the header.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_caseMappings'
op|'.'
name|'get'
op|'('
name|'name'
op|','
name|'_dashCapitalize'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|__all__
dedent|''
dedent|''
name|'__all__'
op|'='
op|'['
string|"'Headers'"
op|']'
newline|'\n'
endmarker|''
end_unit
