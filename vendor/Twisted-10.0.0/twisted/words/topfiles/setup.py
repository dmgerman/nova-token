begin_unit
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'dist'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'SystemExit'
op|'('
string|'"twisted.python.dist module not found.  Make sure you "'
nl|'\n'
string|'"have installed the Twisted core package before "'
nl|'\n'
string|'"attempting to install any other Twisted projects."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'sys'
op|'.'
name|'version_info'
op|'['
op|':'
number|'2'
op|']'
op|'>='
op|'('
number|'2'
op|','
number|'4'
op|')'
op|':'
newline|'\n'
DECL|variable|extraMeta
indent|'        '
name|'extraMeta'
op|'='
name|'dict'
op|'('
nl|'\n'
DECL|variable|classifiers
name|'classifiers'
op|'='
op|'['
nl|'\n'
string|'"Development Status :: 4 - Beta"'
op|','
nl|'\n'
string|'"Environment :: No Input/Output (Daemon)"'
op|','
nl|'\n'
string|'"Intended Audience :: Developers"'
op|','
nl|'\n'
string|'"License :: OSI Approved :: MIT License"'
op|','
nl|'\n'
string|'"Programming Language :: Python"'
op|','
nl|'\n'
string|'"Topic :: Communications :: Chat"'
op|','
nl|'\n'
string|'"Topic :: Communications :: Chat :: AOL Instant Messenger"'
op|','
nl|'\n'
string|'"Topic :: Communications :: Chat :: ICQ"'
op|','
nl|'\n'
string|'"Topic :: Communications :: Chat :: Internet Relay Chat"'
op|','
nl|'\n'
string|'"Topic :: Internet"'
op|','
nl|'\n'
string|'"Topic :: Software Development :: Libraries :: Python Modules"'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|extraMeta
indent|'        '
name|'extraMeta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'dist'
op|'.'
name|'setup'
op|'('
nl|'\n'
DECL|variable|twisted_subproject
name|'twisted_subproject'
op|'='
string|'"words"'
op|','
nl|'\n'
DECL|variable|scripts
name|'scripts'
op|'='
name|'dist'
op|'.'
name|'getScripts'
op|'('
string|'"words"'
op|')'
op|','
nl|'\n'
comment|'# metadata'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Twisted Words"'
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|'"Twisted Words contains Instant Messaging implementations."'
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|'"Twisted Matrix Laboratories"'
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|'"twisted-python@twistedmatrix.com"'
op|','
nl|'\n'
DECL|variable|maintainer
name|'maintainer'
op|'='
string|'"Jp Calderone"'
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|'"http://twistedmatrix.com/trac/wiki/TwistedWords"'
op|','
nl|'\n'
DECL|variable|license
name|'license'
op|'='
string|'"MIT"'
op|','
nl|'\n'
name|'long_description'
op|'='
string|'"""\\\nTwisted Words contains implementations of many Instant Messaging\nprotocols, including IRC, Jabber, MSN, OSCAR (AIM & ICQ), TOC (AOL),\nand some functionality for creating bots, inter-protocol gateways, and\na client application for many of the protocols.\n\nIn support of Jabber, Twisted Words also contains X-ish, a library for\nprocessing XML with Twisted and Python, with support for a Pythonic DOM and\nan XPath-like toolkit.\n"""'
op|','
nl|'\n'
op|'**'
name|'extraMeta'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
