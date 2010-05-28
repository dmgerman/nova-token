begin_unit
comment|'# -*- test-case-name: twisted.conch.test.test_channel -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
string|'"""\nThe parent class for all the SSH Channels.  Currently implemented channels\nare session. direct-tcp, and forwarded-tcp.\n\nMaintainer: Paul Swartz\n"""'
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
name|'internet'
name|'import'
name|'interfaces'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SSHChannel
name|'class'
name|'SSHChannel'
op|'('
name|'log'
op|'.'
name|'Logger'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A class that represents a multiplexed channel over an SSH connection.\n    The channel has a local window which is the maximum amount of data it will\n    receive, and a remote which is the maximum amount of data the remote side\n    will accept.  There is also a maximum packet size for any individual data\n    packet going each way.\n\n    @ivar name: the name of the channel.\n    @type name: C{str}\n    @ivar localWindowSize: the maximum size of the local window in bytes.\n    @type localWindowSize: C{int}\n    @ivar localWindowLeft: how many bytes are left in the local window.\n    @type localWindowLeft: C{int}\n    @ivar localMaxPacket: the maximum size of packet we will accept in bytes.\n    @type localMaxPacket: C{int}\n    @ivar remoteWindowLeft: how many bytes are left in the remote window.\n    @type remoteWindowLeft: C{int}\n    @ivar remoteMaxPacket: the maximum size of a packet the remote side will\n        accept in bytes.\n    @type remoteMaxPacket: C{int}\n    @ivar conn: the connection this channel is multiplexed through.\n    @type conn: L{SSHConnection}\n    @ivar data: any data to send to the other size when the channel is\n        requested.\n    @type data: C{str}\n    @ivar avatar: an avatar for the logged-in user (if a server channel)\n    @ivar localClosed: True if we aren\'t accepting more data.\n    @type localClosed: C{bool}\n    @ivar remoteClosed: True if the other size isn\'t accepting more data.\n    @type remoteClosed: C{bool}\n    """'
newline|'\n'
nl|'\n'
name|'implements'
op|'('
name|'interfaces'
op|'.'
name|'ITransport'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'None'
comment|'# only needed for client channels'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'localWindow'
op|'='
number|'0'
op|','
name|'localMaxPacket'
op|'='
number|'0'
op|','
nl|'\n'
name|'remoteWindow'
op|'='
number|'0'
op|','
name|'remoteMaxPacket'
op|'='
number|'0'
op|','
nl|'\n'
name|'conn'
op|'='
name|'None'
op|','
name|'data'
op|'='
name|'None'
op|','
name|'avatar'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'localWindowSize'
op|'='
name|'localWindow'
name|'or'
number|'131072'
newline|'\n'
name|'self'
op|'.'
name|'localWindowLeft'
op|'='
name|'self'
op|'.'
name|'localWindowSize'
newline|'\n'
name|'self'
op|'.'
name|'localMaxPacket'
op|'='
name|'localMaxPacket'
name|'or'
number|'32768'
newline|'\n'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'='
name|'remoteWindow'
newline|'\n'
name|'self'
op|'.'
name|'remoteMaxPacket'
op|'='
name|'remoteMaxPacket'
newline|'\n'
name|'self'
op|'.'
name|'areWriting'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'conn'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'data'
newline|'\n'
name|'self'
op|'.'
name|'avatar'
op|'='
name|'avatar'
newline|'\n'
name|'self'
op|'.'
name|'specificData'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'buf'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'extBuf'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'closing'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'localClosed'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'remoteClosed'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'None'
comment|'# gets set later by SSHConnection'
newline|'\n'
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
string|"'<SSHChannel %s (lw %i rw %i)>'"
op|'%'
op|'('
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'localWindowLeft'
op|','
name|'self'
op|'.'
name|'remoteWindowLeft'
op|')'
newline|'\n'
nl|'\n'
DECL|member|logPrefix
dedent|''
name|'def'
name|'logPrefix'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id'
op|'='
op|'('
name|'self'
op|'.'
name|'id'
name|'is'
name|'not'
name|'None'
name|'and'
name|'str'
op|'('
name|'self'
op|'.'
name|'id'
op|')'
op|')'
name|'or'
string|'"unknown"'
newline|'\n'
name|'return'
string|'"SSHChannel %s (%s) on %s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'logPrefix'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|channelOpen
dedent|''
name|'def'
name|'channelOpen'
op|'('
name|'self'
op|','
name|'specificData'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the channel is opened.  specificData is any data that the\n        other side sent us when opening the channel.\n\n        @type specificData: C{str}\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'channel open'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|openFailed
dedent|''
name|'def'
name|'openFailed'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the the open failed for some reason.\n        reason.desc is a string descrption, reason.code the the SSH error code.\n\n        @type reason: L{error.ConchError}\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'other side refused open\\nreason: %s'"
op|'%'
name|'reason'
op|')'
newline|'\n'
nl|'\n'
DECL|member|addWindowBytes
dedent|''
name|'def'
name|'addWindowBytes'
op|'('
name|'self'
op|','
name|'bytes'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when bytes are added to the remote window.  By default it clears\n        the data buffers.\n\n        @type bytes:    C{int}\n        """'
newline|'\n'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'='
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'+'
name|'bytes'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'areWriting'
name|'and'
name|'not'
name|'self'
op|'.'
name|'closing'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'areWriting'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'startWriting'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'buf'
op|':'
newline|'\n'
indent|'            '
name|'b'
op|'='
name|'self'
op|'.'
name|'buf'
newline|'\n'
name|'self'
op|'.'
name|'buf'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
name|'b'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'extBuf'
op|':'
newline|'\n'
indent|'            '
name|'b'
op|'='
name|'self'
op|'.'
name|'extBuf'
newline|'\n'
name|'self'
op|'.'
name|'extBuf'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
op|'('
name|'type'
op|','
name|'data'
op|')'
name|'in'
name|'b'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'writeExtended'
op|'('
name|'type'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|requestReceived
dedent|''
dedent|''
dedent|''
name|'def'
name|'requestReceived'
op|'('
name|'self'
op|','
name|'requestType'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when a request is sent to this channel.  By default it delegates\n        to self.request_<requestType>.\n        If this function returns true, the request succeeded, otherwise it\n        failed.\n\n        @type requestType:  C{str}\n        @type data:         C{str}\n        @rtype:             C{bool}\n        """'
newline|'\n'
name|'foo'
op|'='
name|'requestType'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'f'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'request_%s'"
op|'%'
name|'foo'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'log'
op|'.'
name|'msg'
op|'('
string|"'unhandled request for %s'"
op|'%'
name|'requestType'
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when we receive data.\n\n        @type data: C{str}\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'got data %s'"
op|'%'
name|'repr'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|extReceived
dedent|''
name|'def'
name|'extReceived'
op|'('
name|'self'
op|','
name|'dataType'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when we receive extended data (usually standard error).\n\n        @type dataType: C{int}\n        @type data:     C{str}\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'got extended data %s %s'"
op|'%'
op|'('
name|'dataType'
op|','
name|'repr'
op|'('
name|'data'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|eofReceived
dedent|''
name|'def'
name|'eofReceived'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the other side will send no more data.\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'remote eof'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|closeReceived
dedent|''
name|'def'
name|'closeReceived'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the other side has closed the channel.\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'remote close'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|closed
dedent|''
name|'def'
name|'closed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the channel is closed.  This means that both our side and\n        the remote side have closed the channel.\n        """'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'closed'"
op|')'
newline|'\n'
nl|'\n'
comment|'# transport stuff'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Write some data to the channel.  If there is not enough remote window\n        available, buffer until it is.  Otherwise, split the data into\n        packets of length remoteMaxPacket and send them.\n\n        @type data: C{str}\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'buf'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'buf'
op|'+='
name|'data'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'top'
op|'='
name|'len'
op|'('
name|'data'
op|')'
newline|'\n'
name|'if'
name|'top'
op|'>'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|','
name|'self'
op|'.'
name|'buf'
op|'='
op|'('
name|'data'
op|'['
op|':'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|']'
op|','
nl|'\n'
name|'data'
op|'['
name|'self'
op|'.'
name|'remoteWindowLeft'
op|':'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'areWriting'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'stopWriting'
op|'('
op|')'
newline|'\n'
name|'top'
op|'='
name|'self'
op|'.'
name|'remoteWindowLeft'
newline|'\n'
dedent|''
name|'rmp'
op|'='
name|'self'
op|'.'
name|'remoteMaxPacket'
newline|'\n'
name|'write'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'sendData'
newline|'\n'
name|'r'
op|'='
name|'range'
op|'('
number|'0'
op|','
name|'top'
op|','
name|'rmp'
op|')'
newline|'\n'
name|'for'
name|'offset'
name|'in'
name|'r'
op|':'
newline|'\n'
indent|'            '
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|'['
name|'offset'
op|':'
name|'offset'
op|'+'
name|'rmp'
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'-='
name|'top'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'closing'
name|'and'
name|'not'
name|'self'
op|'.'
name|'buf'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'loseConnection'
op|'('
op|')'
comment|'# try again'
newline|'\n'
nl|'\n'
DECL|member|writeExtended
dedent|''
dedent|''
name|'def'
name|'writeExtended'
op|'('
name|'self'
op|','
name|'dataType'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send extended data to this channel.  If there is not enough remote\n        window available, buffer until there is.  Otherwise, split the data\n        into packets of length remoteMaxPacket and send them.\n\n        @type dataType: C{int}\n        @type data:     C{str}\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'extBuf'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'extBuf'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'=='
name|'dataType'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'extBuf'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'+='
name|'data'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'extBuf'
op|'.'
name|'append'
op|'('
op|'['
name|'dataType'
op|','
name|'data'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'data'
op|')'
op|'>'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|','
name|'self'
op|'.'
name|'extBuf'
op|'='
op|'('
name|'data'
op|'['
op|':'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|']'
op|','
nl|'\n'
op|'['
op|'['
name|'dataType'
op|','
name|'data'
op|'['
name|'self'
op|'.'
name|'remoteWindowLeft'
op|':'
op|']'
op|']'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'areWriting'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'stopWriting'
op|'('
op|')'
newline|'\n'
dedent|''
name|'while'
name|'len'
op|'('
name|'data'
op|')'
op|'>'
name|'self'
op|'.'
name|'remoteMaxPacket'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'sendExtendedData'
op|'('
name|'self'
op|','
name|'dataType'
op|','
nl|'\n'
name|'data'
op|'['
op|':'
name|'self'
op|'.'
name|'remoteMaxPacket'
op|']'
op|')'
newline|'\n'
name|'data'
op|'='
name|'data'
op|'['
name|'self'
op|'.'
name|'remoteMaxPacket'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'-='
name|'self'
op|'.'
name|'remoteMaxPacket'
newline|'\n'
dedent|''
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'sendExtendedData'
op|'('
name|'self'
op|','
name|'dataType'
op|','
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remoteWindowLeft'
op|'-='
name|'len'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'closing'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'loseConnection'
op|'('
op|')'
comment|'# try again'
newline|'\n'
nl|'\n'
DECL|member|writeSequence
dedent|''
dedent|''
name|'def'
name|'writeSequence'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Part of the Transport interface.  Write a list of strings to the\n        channel.\n\n        @type data: C{list} of C{str}\n        """'
newline|'\n'
name|'self'
op|'.'
name|'write'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|loseConnection
dedent|''
name|'def'
name|'loseConnection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Close the channel if there is no buferred data.  Otherwise, note the\n        request and return.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'closing'
op|'='
number|'1'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'buf'
name|'and'
name|'not'
name|'self'
op|'.'
name|'extBuf'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'sendClose'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getPeer
dedent|''
dedent|''
name|'def'
name|'getPeer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a tuple describing the other side of the connection.\n\n        @rtype: C{tuple}\n        """'
newline|'\n'
name|'return'
op|'('
string|"'SSH'"
op|','
op|')'
op|'+'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'transport'
op|'.'
name|'getPeer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|getHost
dedent|''
name|'def'
name|'getHost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a tuple describing our side of the connection.\n\n        @rtype: C{tuple}\n        """'
newline|'\n'
name|'return'
op|'('
string|"'SSH'"
op|','
op|')'
op|'+'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'transport'
op|'.'
name|'getHost'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|stopWriting
dedent|''
name|'def'
name|'stopWriting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the remote buffer is full, as a hint to stop writing.\n        This can be ignored, but it can be helpful.\n        """'
newline|'\n'
nl|'\n'
DECL|member|startWriting
dedent|''
name|'def'
name|'startWriting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called when the remote buffer has more room, as a hint to continue\n        writing.\n        """'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
