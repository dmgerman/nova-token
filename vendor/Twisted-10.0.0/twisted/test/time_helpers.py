begin_unit
comment|'# Copyright (c) 2001-2010 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nHelper class to writing deterministic time-based unit tests.\n\nDo not use this module.  It is a lie.  See L{twisted.internet.task.Clock}\ninstead.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'warnings'
newline|'\n'
name|'warnings'
op|'.'
name|'warn'
op|'('
nl|'\n'
string|'"twisted.test.time_helpers is deprecated since Twisted 10.0.  "'
nl|'\n'
string|'"See twisted.internet.task.Clock instead."'
op|','
nl|'\n'
name|'category'
op|'='
name|'DeprecationWarning'
op|','
name|'stacklevel'
op|'='
number|'2'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Clock
name|'class'
name|'Clock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A utility for monkey-patches various parts of Twisted to use a\n    simulated timing mechanism. DO NOT use this class. Use\n    L{twisted.internet.task.Clock}.\n    """'
newline|'\n'
DECL|variable|rightNow
name|'rightNow'
op|'='
number|'0.0'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the current simulated time.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'rightNow'
newline|'\n'
nl|'\n'
DECL|member|install
dedent|''
name|'def'
name|'install'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Monkeypatch L{twisted.internet.reactor.seconds} to use\n        L{__call__} as a time source\n        """'
newline|'\n'
comment|'# Violation is fun.'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'self'
op|'.'
name|'reactor_original'
op|'='
name|'reactor'
op|'.'
name|'seconds'
newline|'\n'
name|'reactor'
op|'.'
name|'seconds'
op|'='
name|'self'
newline|'\n'
nl|'\n'
DECL|member|uninstall
dedent|''
name|'def'
name|'uninstall'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove the monkeypatching of L{twisted.internet.reactor.seconds}.\n        """'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'seconds'
op|'='
name|'self'
op|'.'
name|'reactor_original'
newline|'\n'
nl|'\n'
DECL|member|adjust
dedent|''
name|'def'
name|'adjust'
op|'('
name|'self'
op|','
name|'amount'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Adjust the current simulated time upward by the given C{amount}.\n\n        Note that this does not cause any scheduled calls to be run.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'rightNow'
op|'+='
name|'amount'
newline|'\n'
nl|'\n'
DECL|member|pump
dedent|''
name|'def'
name|'pump'
op|'('
name|'self'
op|','
name|'reactor'
op|','
name|'timings'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Iterate the given C{reactor} with increments of time specified\n        by C{timings}.\n\n        For each timing, the simulated time will be L{adjust}ed and\n        the reactor will be iterated twice.\n        """'
newline|'\n'
name|'timings'
op|'='
name|'list'
op|'('
name|'timings'
op|')'
newline|'\n'
name|'timings'
op|'.'
name|'reverse'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'adjust'
op|'('
name|'timings'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
name|'while'
name|'timings'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'adjust'
op|'('
name|'timings'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'iterate'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'iterate'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
