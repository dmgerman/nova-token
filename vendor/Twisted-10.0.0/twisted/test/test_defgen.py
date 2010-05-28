begin_unit
name|'from'
name|'__future__'
name|'import'
name|'generators'
op|','
name|'nested_scopes'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
op|','
name|'util'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'defer'
name|'import'
name|'waitForDeferred'
op|','
name|'deferredGenerator'
op|','
name|'Deferred'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
DECL|function|getThing
name|'def'
name|'getThing'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0'
op|','
name|'d'
op|'.'
name|'callback'
op|','
string|'"hi"'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|function|getOwie
dedent|''
name|'def'
name|'getOwie'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
name|'Deferred'
op|'('
op|')'
newline|'\n'
DECL|function|CRAP
name|'def'
name|'CRAP'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'.'
name|'errback'
op|'('
name|'ZeroDivisionError'
op|'('
string|"'OMG'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0'
op|','
name|'CRAP'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
comment|'# NOTE: most of the tests in DeferredGeneratorTests are duplicated'
nl|'\n'
comment|'# with slightly different syntax for the InlineCallbacksTests below.'
nl|'\n'
nl|'\n'
DECL|class|TerminalException
dedent|''
name|'class'
name|'TerminalException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|BaseDefgenTests
dedent|''
name|'class'
name|'BaseDefgenTests'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This class sets up a bunch of test cases which will test both\n    deferredGenerator and inlineCallbacks based generators. The subclasses\n    DeferredGeneratorTests and InlineCallbacksTests each provide the actual\n    generator implementations tested.\n    """'
newline|'\n'
nl|'\n'
DECL|member|testBasics
name|'def'
name|'testBasics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Test that a normal deferredGenerator works.  Tests yielding a\n        deferred which callbacks, as well as a deferred errbacks. Also\n        ensures returning a final value works.\n        """'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_genBasics'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'assertEqual'
op|','
string|"'WOOSH'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|testBuggy
dedent|''
name|'def'
name|'testBuggy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure that a buggy generator properly signals a Failure\n        condition on result deferred.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'assertFailure'
op|'('
name|'self'
op|'.'
name|'_genBuggy'
op|'('
op|')'
op|','
name|'ZeroDivisionError'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testNothing
dedent|''
name|'def'
name|'testNothing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that a generator which never yields results in None."""'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_genNothing'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'assertEqual'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testHandledTerminalFailure
dedent|''
name|'def'
name|'testHandledTerminalFailure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a Deferred Generator which yields a Deferred which fails and\n        handles the exception which results.  Assert that the Deferred\n        Generator does not errback its Deferred.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_genHandledTerminalFailure'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'assertEqual'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testHandledTerminalAsyncFailure
dedent|''
name|'def'
name|'testHandledTerminalAsyncFailure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Just like testHandledTerminalFailure, only with a Deferred which fires\n        asynchronously with an error.\n        """'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'deferredGeneratorResultDeferred'
op|'='
name|'self'
op|'.'
name|'_genHandledTerminalAsyncFailure'
op|'('
name|'d'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'errback'
op|'('
name|'TerminalException'
op|'('
string|'"Handled Terminal Failure"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'deferredGeneratorResultDeferred'
op|'.'
name|'addCallback'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testStackUsage
dedent|''
name|'def'
name|'testStackUsage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Make sure we don\'t blow the stack when yielding immediately\n        available deferreds.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_genStackUsage'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'assertEqual'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testStackUsage2
dedent|''
name|'def'
name|'testStackUsage2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Make sure we don\'t blow the stack when yielding immediately\n        available values.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_genStackUsage2'
op|'('
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'assertEqual'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeferredGeneratorTests
dedent|''
dedent|''
name|'class'
name|'DeferredGeneratorTests'
op|'('
name|'BaseDefgenTests'
op|','
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# First provide all the generator impls necessary for BaseDefgenTests'
nl|'\n'
DECL|member|_genBasics
indent|'    '
name|'def'
name|'_genBasics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'x'
op|'='
name|'waitForDeferred'
op|'('
name|'getThing'
op|'('
op|')'
op|')'
newline|'\n'
name|'yield'
name|'x'
newline|'\n'
name|'x'
op|'='
name|'x'
op|'.'
name|'getResult'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'x'
op|','
string|'"hi"'
op|')'
newline|'\n'
nl|'\n'
name|'ow'
op|'='
name|'waitForDeferred'
op|'('
name|'getOwie'
op|'('
op|')'
op|')'
newline|'\n'
name|'yield'
name|'ow'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ow'
op|'.'
name|'getResult'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ZeroDivisionError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'e'
op|')'
op|','
string|"'OMG'"
op|')'
newline|'\n'
dedent|''
name|'yield'
string|'"WOOSH"'
newline|'\n'
name|'return'
newline|'\n'
DECL|variable|_genBasics
dedent|''
name|'_genBasics'
op|'='
name|'deferredGenerator'
op|'('
name|'_genBasics'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_genBuggy
name|'def'
name|'_genBuggy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'waitForDeferred'
op|'('
name|'getThing'
op|'('
op|')'
op|')'
newline|'\n'
number|'1'
op|'/'
number|'0'
newline|'\n'
DECL|variable|_genBuggy
dedent|''
name|'_genBuggy'
op|'='
name|'deferredGenerator'
op|'('
name|'_genBuggy'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_genNothing
name|'def'
name|'_genNothing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
number|'0'
op|':'
name|'yield'
number|'1'
newline|'\n'
DECL|variable|_genNothing
dedent|''
name|'_genNothing'
op|'='
name|'deferredGenerator'
op|'('
name|'_genNothing'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_genHandledTerminalFailure
name|'def'
name|'_genHandledTerminalFailure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
name|'waitForDeferred'
op|'('
name|'defer'
op|'.'
name|'fail'
op|'('
name|'TerminalException'
op|'('
string|'"Handled Terminal Failure"'
op|')'
op|')'
op|')'
newline|'\n'
name|'yield'
name|'x'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'x'
op|'.'
name|'getResult'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TerminalException'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
DECL|variable|_genHandledTerminalFailure
dedent|''
dedent|''
name|'_genHandledTerminalFailure'
op|'='
name|'deferredGenerator'
op|'('
name|'_genHandledTerminalFailure'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_genHandledTerminalAsyncFailure
name|'def'
name|'_genHandledTerminalAsyncFailure'
op|'('
name|'self'
op|','
name|'d'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
name|'waitForDeferred'
op|'('
name|'d'
op|')'
newline|'\n'
name|'yield'
name|'x'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'x'
op|'.'
name|'getResult'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TerminalException'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
DECL|variable|_genHandledTerminalAsyncFailure
dedent|''
dedent|''
name|'_genHandledTerminalAsyncFailure'
op|'='
name|'deferredGenerator'
op|'('
name|'_genHandledTerminalAsyncFailure'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_genStackUsage
name|'def'
name|'_genStackUsage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'5000'
op|')'
op|':'
newline|'\n'
comment|'# Test with yielding a deferred'
nl|'\n'
indent|'            '
name|'x'
op|'='
name|'waitForDeferred'
op|'('
name|'defer'
op|'.'
name|'succeed'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'yield'
name|'x'
newline|'\n'
name|'x'
op|'='
name|'x'
op|'.'
name|'getResult'
op|'('
op|')'
newline|'\n'
dedent|''
name|'yield'
number|'0'
newline|'\n'
DECL|variable|_genStackUsage
dedent|''
name|'_genStackUsage'
op|'='
name|'deferredGenerator'
op|'('
name|'_genStackUsage'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_genStackUsage2
name|'def'
name|'_genStackUsage2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'5000'
op|')'
op|':'
newline|'\n'
comment|'# Test with yielding a random value'
nl|'\n'
indent|'            '
name|'yield'
number|'1'
newline|'\n'
dedent|''
name|'yield'
number|'0'
newline|'\n'
DECL|variable|_genStackUsage2
dedent|''
name|'_genStackUsage2'
op|'='
name|'deferredGenerator'
op|'('
name|'_genStackUsage2'
op|')'
newline|'\n'
nl|'\n'
comment|'# Tests unique to deferredGenerator'
nl|'\n'
nl|'\n'
DECL|member|testDeferredYielding
name|'def'
name|'testDeferredYielding'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure that yielding a Deferred directly is trapped as an\n        error.\n        """'
newline|'\n'
comment|'# See the comment _deferGenerator about d.callback(Deferred).'
nl|'\n'
DECL|function|_genDeferred
name|'def'
name|'_genDeferred'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'getThing'
op|'('
op|')'
newline|'\n'
dedent|''
name|'_genDeferred'
op|'='
name|'deferredGenerator'
op|'('
name|'_genDeferred'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'assertFailure'
op|'('
name|'_genDeferred'
op|'('
op|')'
op|','
name|'TypeError'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
comment|"## This has to be in a string so the new yield syntax doesn't cause a"
nl|'\n'
comment|'## syntax error in Python 2.4 and before.'
nl|'\n'
dedent|''
dedent|''
name|'inlineCallbacksTestsSource'
op|'='
string|'\'\'\'\nfrom twisted.internet.defer import inlineCallbacks, returnValue\n\nclass InlineCallbacksTests(BaseDefgenTests, unittest.TestCase):\n    # First provide all the generator impls necessary for BaseDefgenTests\n\n    def _genBasics(self):\n\n        x = yield getThing()\n\n        self.assertEquals(x, "hi")\n\n        try:\n            ow = yield getOwie()\n        except ZeroDivisionError, e:\n            self.assertEquals(str(e), \'OMG\')\n        returnValue("WOOSH")\n    _genBasics = inlineCallbacks(_genBasics)\n\n    def _genBuggy(self):\n        yield getThing()\n        1/0\n    _genBuggy = inlineCallbacks(_genBuggy)\n\n\n    def _genNothing(self):\n        if 0: yield 1\n    _genNothing = inlineCallbacks(_genNothing)\n\n\n    def _genHandledTerminalFailure(self):\n        try:\n            x = yield defer.fail(TerminalException("Handled Terminal Failure"))\n        except TerminalException:\n            pass\n    _genHandledTerminalFailure = inlineCallbacks(_genHandledTerminalFailure)\n\n\n    def _genHandledTerminalAsyncFailure(self, d):\n        try:\n            x = yield d\n        except TerminalException:\n            pass\n    _genHandledTerminalAsyncFailure = inlineCallbacks(\n        _genHandledTerminalAsyncFailure)\n\n\n    def _genStackUsage(self):\n        for x in range(5000):\n            # Test with yielding a deferred\n            x = yield defer.succeed(1)\n        returnValue(0)\n    _genStackUsage = inlineCallbacks(_genStackUsage)\n\n    def _genStackUsage2(self):\n        for x in range(5000):\n            # Test with yielding a random value\n            yield 1\n        returnValue(0)\n    _genStackUsage2 = inlineCallbacks(_genStackUsage2)\n\n    # Tests unique to inlineCallbacks\n\n    def testYieldNonDeferrred(self):\n        """\n        Ensure that yielding a non-deferred passes it back as the\n        result of the yield expression.\n        """\n        def _test():\n            x = yield 5\n            returnValue(5)\n        _test = inlineCallbacks(_test)\n\n        return _test().addCallback(self.assertEqual, 5)\n\n    def testReturnNoValue(self):\n        """Ensure a standard python return results in a None result."""\n        def _noReturn():\n            yield 5\n            return\n        _noReturn = inlineCallbacks(_noReturn)\n\n        return _noReturn().addCallback(self.assertEqual, None)\n\n    def testReturnValue(self):\n        """Ensure that returnValue works."""\n        def _return():\n            yield 5\n            returnValue(6)\n        _return = inlineCallbacks(_return)\n\n        return _return().addCallback(self.assertEqual, 6)\n\n\'\'\''
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'version_info'
op|'>'
op|'('
number|'2'
op|','
number|'5'
op|')'
op|':'
newline|'\n'
comment|'# Load tests'
nl|'\n'
indent|'    '
name|'exec'
name|'inlineCallbacksTestsSource'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Make a placeholder test case'
nl|'\n'
DECL|class|InlineCallbacksTests
indent|'    '
name|'class'
name|'InlineCallbacksTests'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|skip
indent|'        '
name|'skip'
op|'='
string|'"defer.defgen doesn\'t run on python < 2.5."'
newline|'\n'
DECL|member|test_everything
name|'def'
name|'test_everything'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
