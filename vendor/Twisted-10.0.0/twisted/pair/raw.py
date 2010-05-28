begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
string|'"""Interface definitions for working with raw packets"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'Interface'
newline|'\n'
nl|'\n'
DECL|class|IRawDatagramProtocol
name|'class'
name|'IRawDatagramProtocol'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An interface for protocols such as UDP, ICMP and TCP."""'
newline|'\n'
nl|'\n'
DECL|member|addProto
name|'def'
name|'addProto'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add a protocol on top of this one.\n        """'
newline|'\n'
nl|'\n'
DECL|member|datagramReceived
dedent|''
name|'def'
name|'datagramReceived'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        An IP datagram has been received. Parse and process it.\n        """'
newline|'\n'
nl|'\n'
DECL|class|IRawPacketProtocol
dedent|''
dedent|''
name|'class'
name|'IRawPacketProtocol'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An interface for low-level protocols such as IP and ARP."""'
newline|'\n'
nl|'\n'
DECL|member|addProto
name|'def'
name|'addProto'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add a protocol on top of this one.\n        """'
newline|'\n'
nl|'\n'
DECL|member|datagramReceived
dedent|''
name|'def'
name|'datagramReceived'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        An IP datagram has been received. Parse and process it.\n        """'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
