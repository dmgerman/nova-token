begin_unit
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nA poll() based implementation of the twisted main loop.\n\nTo install the event loop (and you should do this before any connections,\nlisteners or connectors are added)::\n\n    from twisted.internet import pollreactor\n    pollreactor.install()\n"""'
newline|'\n'
nl|'\n'
comment|'# System imports'
nl|'\n'
name|'import'
name|'errno'
op|','
name|'sys'
newline|'\n'
name|'from'
name|'select'
name|'import'
name|'error'
name|'as'
name|'SelectError'
op|','
name|'poll'
newline|'\n'
name|'from'
name|'select'
name|'import'
name|'POLLIN'
op|','
name|'POLLOUT'
op|','
name|'POLLHUP'
op|','
name|'POLLERR'
op|','
name|'POLLNVAL'
newline|'\n'
nl|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
comment|'# Twisted imports'
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
name|'main'
op|','
name|'posixbase'
op|','
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'interfaces'
name|'import'
name|'IReactorFDSet'
newline|'\n'
nl|'\n'
DECL|variable|POLL_DISCONNECTED
name|'POLL_DISCONNECTED'
op|'='
op|'('
name|'POLLHUP'
op|'|'
name|'POLLERR'
op|'|'
name|'POLLNVAL'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PollReactor
name|'class'
name|'PollReactor'
op|'('
name|'posixbase'
op|'.'
name|'PosixReactorBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A reactor that uses poll(2).\n\n    @ivar _poller: A L{poll} which will be used to check for I/O\n        readiness.\n\n    @ivar _selectables: A dictionary mapping integer file descriptors to\n        instances of L{FileDescriptor} which have been registered with the\n        reactor.  All L{FileDescriptors} which are currently receiving read or\n        write readiness notifications will be present as values in this\n        dictionary.\n\n    @ivar _reads: A dictionary mapping integer file descriptors to arbitrary\n        values (this is essentially a set).  Keys in this dictionary will be\n        registered with C{_poller} for read readiness notifications which will\n        be dispatched to the corresponding L{FileDescriptor} instances in\n        C{_selectables}.\n\n    @ivar _writes: A dictionary mapping integer file descriptors to arbitrary\n        values (this is essentially a set).  Keys in this dictionary will be\n        registered with C{_poller} for write readiness notifications which will\n        be dispatched to the corresponding L{FileDescriptor} instances in\n        C{_selectables}.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IReactorFDSet'
op|')'
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
string|'"""\n        Initialize polling object, file descriptor tracking dictionaries, and\n        the base class.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_poller'
op|'='
name|'poll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_selectables'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_reads'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_writes'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'posixbase'
op|'.'
name|'PosixReactorBase'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_updateRegistration
dedent|''
name|'def'
name|'_updateRegistration'
op|'('
name|'self'
op|','
name|'fd'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Register/unregister an fd with the poller."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_poller'
op|'.'
name|'unregister'
op|'('
name|'fd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'mask'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_reads'
op|':'
newline|'\n'
indent|'            '
name|'mask'
op|'='
name|'mask'
op|'|'
name|'POLLIN'
newline|'\n'
dedent|''
name|'if'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_writes'
op|':'
newline|'\n'
indent|'            '
name|'mask'
op|'='
name|'mask'
op|'|'
name|'POLLOUT'
newline|'\n'
dedent|''
name|'if'
name|'mask'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_poller'
op|'.'
name|'register'
op|'('
name|'fd'
op|','
name|'mask'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_selectables'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_dictRemove
dedent|''
dedent|''
dedent|''
name|'def'
name|'_dictRemove'
op|'('
name|'self'
op|','
name|'selectable'
op|','
name|'mdict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# the easy way'
nl|'\n'
indent|'            '
name|'fd'
op|'='
name|'selectable'
op|'.'
name|'fileno'
op|'('
op|')'
newline|'\n'
comment|'# make sure the fd is actually real.  In some situations we can get'
nl|'\n'
comment|'# -1 here.'
nl|'\n'
name|'mdict'
op|'['
name|'fd'
op|']'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
comment|'# the hard way: necessary because fileno() may disappear at any'
nl|'\n'
comment|"# moment, thanks to python's underlying sockets impl"
nl|'\n'
indent|'            '
name|'for'
name|'fd'
op|','
name|'fdes'
name|'in'
name|'self'
op|'.'
name|'_selectables'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'selectable'
name|'is'
name|'fdes'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# Hmm, maybe not the right course of action?  This method can't"
nl|'\n'
comment|'# fail, because it happens inside error detection...'
nl|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'fd'
name|'in'
name|'mdict'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'mdict'
op|'['
name|'fd'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_updateRegistration'
op|'('
name|'fd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|addReader
dedent|''
dedent|''
name|'def'
name|'addReader'
op|'('
name|'self'
op|','
name|'reader'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a FileDescriptor for notification of data available to read.\n        """'
newline|'\n'
name|'fd'
op|'='
name|'reader'
op|'.'
name|'fileno'
op|'('
op|')'
newline|'\n'
name|'if'
name|'fd'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_reads'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
op|'='
name|'reader'
newline|'\n'
name|'self'
op|'.'
name|'_reads'
op|'['
name|'fd'
op|']'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'_updateRegistration'
op|'('
name|'fd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|addWriter
dedent|''
dedent|''
name|'def'
name|'addWriter'
op|'('
name|'self'
op|','
name|'writer'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a FileDescriptor for notification of data available to write.\n        """'
newline|'\n'
name|'fd'
op|'='
name|'writer'
op|'.'
name|'fileno'
op|'('
op|')'
newline|'\n'
name|'if'
name|'fd'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_writes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
op|'='
name|'writer'
newline|'\n'
name|'self'
op|'.'
name|'_writes'
op|'['
name|'fd'
op|']'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'_updateRegistration'
op|'('
name|'fd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|removeReader
dedent|''
dedent|''
name|'def'
name|'removeReader'
op|'('
name|'self'
op|','
name|'reader'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a Selectable for notification of data available to read.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_dictRemove'
op|'('
name|'reader'
op|','
name|'self'
op|'.'
name|'_reads'
op|')'
newline|'\n'
nl|'\n'
DECL|member|removeWriter
dedent|''
name|'def'
name|'removeWriter'
op|'('
name|'self'
op|','
name|'writer'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a Selectable for notification of data available to write.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_dictRemove'
op|'('
name|'writer'
op|','
name|'self'
op|'.'
name|'_writes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|removeAll
dedent|''
name|'def'
name|'removeAll'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove all selectables, and return a list of them.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_removeAll'
op|'('
nl|'\n'
op|'['
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
name|'for'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_reads'
op|']'
op|','
nl|'\n'
op|'['
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
name|'for'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_writes'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|doPoll
dedent|''
name|'def'
name|'doPoll'
op|'('
name|'self'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll the poller for new events."""'
newline|'\n'
name|'if'
name|'timeout'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'timeout'
op|'='
name|'int'
op|'('
name|'timeout'
op|'*'
number|'1000'
op|')'
comment|'# convert seconds to milliseconds'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'l'
op|'='
name|'self'
op|'.'
name|'_poller'
op|'.'
name|'poll'
op|'('
name|'timeout'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'SelectError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'['
number|'0'
op|']'
op|'=='
name|'errno'
op|'.'
name|'EINTR'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'_drdw'
op|'='
name|'self'
op|'.'
name|'_doReadOrWrite'
newline|'\n'
name|'for'
name|'fd'
op|','
name|'event'
name|'in'
name|'l'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'selectable'
op|'='
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
comment|"# Handles the infrequent case where one selectable's"
nl|'\n'
comment|'# handler disconnects another.'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'log'
op|'.'
name|'callWithLogger'
op|'('
name|'selectable'
op|','
name|'_drdw'
op|','
name|'selectable'
op|','
name|'fd'
op|','
name|'event'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|doIteration
dedent|''
dedent|''
name|'doIteration'
op|'='
name|'doPoll'
newline|'\n'
nl|'\n'
DECL|member|_doReadOrWrite
name|'def'
name|'_doReadOrWrite'
op|'('
name|'self'
op|','
name|'selectable'
op|','
name|'fd'
op|','
name|'event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'why'
op|'='
name|'None'
newline|'\n'
name|'inRead'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'event'
op|'&'
name|'POLL_DISCONNECTED'
name|'and'
name|'not'
op|'('
name|'event'
op|'&'
name|'POLLIN'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'why'
op|'='
name|'main'
op|'.'
name|'CONNECTION_LOST'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'event'
op|'&'
name|'POLLIN'
op|':'
newline|'\n'
indent|'                    '
name|'why'
op|'='
name|'selectable'
op|'.'
name|'doRead'
op|'('
op|')'
newline|'\n'
name|'inRead'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'why'
name|'and'
name|'event'
op|'&'
name|'POLLOUT'
op|':'
newline|'\n'
indent|'                    '
name|'why'
op|'='
name|'selectable'
op|'.'
name|'doWrite'
op|'('
op|')'
newline|'\n'
name|'inRead'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'selectable'
op|'.'
name|'fileno'
op|'('
op|')'
op|'=='
name|'fd'
op|':'
newline|'\n'
indent|'                    '
name|'why'
op|'='
name|'error'
op|'.'
name|'ConnectionFdescWentAway'
op|'('
string|"'Filedescriptor went away'"
op|')'
newline|'\n'
name|'inRead'
op|'='
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'log'
op|'.'
name|'deferr'
op|'('
op|')'
newline|'\n'
name|'why'
op|'='
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'why'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_disconnectSelectable'
op|'('
name|'selectable'
op|','
name|'why'
op|','
name|'inRead'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getReaders
dedent|''
dedent|''
name|'def'
name|'getReaders'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
name|'for'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_reads'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getWriters
dedent|''
name|'def'
name|'getWriters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_selectables'
op|'['
name|'fd'
op|']'
name|'for'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_writes'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|install
dedent|''
dedent|''
name|'def'
name|'install'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Install the poll() reactor."""'
newline|'\n'
name|'p'
op|'='
name|'PollReactor'
op|'('
op|')'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'main'
name|'import'
name|'installReactor'
newline|'\n'
name|'installReactor'
op|'('
name|'p'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|__all__
dedent|''
name|'__all__'
op|'='
op|'['
string|'"PollReactor"'
op|','
string|'"install"'
op|']'
newline|'\n'
endmarker|''
end_unit
