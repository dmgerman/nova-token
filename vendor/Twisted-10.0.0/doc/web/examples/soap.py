begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'# '
nl|'\n'
string|'"""Example of publishing SOAP methods.\n\nSample usage::\n\n   >>> import SOAPpy\n   >>> p = SOAPpy.SOAPProxy(\'http://localhost:8080/\')\n   >>> p.add(a=1)\n   1\n   >>> p.add(a=1, b=3)\n   4\n   >>> p.echo([1, 2])\n   [1, 2]\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'soap'
op|','
name|'server'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
op|','
name|'defer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Example
name|'class'
name|'Example'
op|'('
name|'soap'
op|'.'
name|'SOAPPublisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publish two methods, \'add\' and \'echo\'."""'
newline|'\n'
nl|'\n'
DECL|member|soap_echo
name|'def'
name|'soap_echo'
op|'('
name|'self'
op|','
name|'x'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'x'
newline|'\n'
nl|'\n'
DECL|member|soap_add
dedent|''
name|'def'
name|'soap_add'
op|'('
name|'self'
op|','
name|'a'
op|'='
number|'0'
op|','
name|'b'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'a'
op|'+'
name|'b'
newline|'\n'
dedent|''
name|'soap_add'
op|'.'
name|'useKeywords'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|soap_deferred
name|'def'
name|'soap_deferred'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
number|'2'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8080'
op|','
name|'server'
op|'.'
name|'Site'
op|'('
name|'Example'
op|'('
op|')'
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
endmarker|''
end_unit
