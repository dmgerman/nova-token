begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""\nBase classes for our unit tests.\nAllows overriding of flags for use of fakes,\nand some black magic for inline callbacks.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'tornado'
name|'import'
name|'ioloop'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
name|'as'
name|'trial_unittest'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'fakerabbit'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'fake_tests'"
op|','
name|'True'
op|','
nl|'\n'
string|"'should we use everything for testing'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|skip_if_fake
name|'def'
name|'skip_if_fake'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_skipper
indent|'    '
name|'def'
name|'_skipper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'trial_unittest'
op|'.'
name|'SkipTest'
op|'('
string|"'Test cannot be run in fake mode'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'_skipper'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
name|'return'
name|'_skipper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TrialTestCase
dedent|''
name|'class'
name|'TrialTestCase'
op|'('
name|'trial_unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TrialTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# emulate some of the mox stuff, we can't use the metaclass"
nl|'\n'
comment|'# because it screws with our generators'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flag_overrides'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TrialTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'SmartUnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'            '
name|'fakerabbit'
op|'.'
name|'reset_all'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# attempt to wipe all keepers'
nl|'\n'
comment|'#keeper = datastore.Keeper()'
nl|'\n'
comment|'#keeper.clear_all()'
nl|'\n'
nl|'\n'
DECL|member|flags
dedent|''
dedent|''
name|'def'
name|'flags'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kw'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'flag_overrides'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|"'trying to override already overriden flag: %s'"
op|'%'
name|'k'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flag_overrides'
op|'['
name|'k'
op|']'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_flags
dedent|''
dedent|''
name|'def'
name|'reset_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'flag_overrides'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'BaseTestCase'
op|'('
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BaseTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# TODO(termie): we could possibly keep a more global registry of'
nl|'\n'
comment|'#               the injected listeners... this is fine for now though'
nl|'\n'
name|'self'
op|'.'
name|'injected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'ioloop'
op|'='
name|'ioloop'
op|'.'
name|'IOLoop'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_waiting'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_doneWaiting'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_timedOut'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'set_up'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_up
dedent|''
name|'def'
name|'set_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|tear_down
dedent|''
name|'def'
name|'tear_down'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BaseTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'injected'
op|':'
newline|'\n'
indent|'            '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'            '
name|'fakerabbit'
op|'.'
name|'reset_all'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'tear_down'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_waitForTest
dedent|''
name|'def'
name|'_waitForTest'
op|'('
name|'self'
op|','
name|'timeout'
op|'='
number|'60'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Push the ioloop along to wait for our test to complete. """'
newline|'\n'
name|'self'
op|'.'
name|'_waiting'
op|'='
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'add_timeout'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'timeout'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_timeout'
op|')'
newline|'\n'
DECL|function|_wait
name|'def'
name|'_wait'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_timedOut'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'test timed out'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_doneWaiting'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'return'
newline|'\n'
comment|'# we can use add_callback here but this uses less cpu when testing'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'add_timeout'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
number|'0.01'
op|','
name|'_wait'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'add_callback'
op|'('
name|'_wait'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_done
dedent|''
name|'def'
name|'_done'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_waiting'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'ioloop'
op|'.'
name|'remove_timeout'
op|'('
name|'self'
op|'.'
name|'_waiting'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_waiting'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_doneWaiting'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_maybeInlineCallbacks
dedent|''
name|'def'
name|'_maybeInlineCallbacks'
op|'('
name|'self'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" If we\'re doing async calls in our tests, wait on them.\n\n        This is probably the most complicated hunk of code we have so far.\n\n        First up, if the function is normal (not async) we just act normal\n        and return.\n\n        Async tests will use the "Inline Callbacks" pattern, which means\n        you yield Deferreds at every "waiting" step of your code instead\n        of making epic callback chains.\n\n        Example (callback chain, ugly):\n\n        d = self.node.terminate_instance(instance_id) # a Deferred instance\n        def _describe(_):\n            d_desc = self.node.describe_instances() # another Deferred instance\n            return d_desc\n        def _checkDescribe(rv):\n            self.assertEqual(rv, [])\n        d.addCallback(_describe)\n        d.addCallback(_checkDescribe)\n        d.addCallback(lambda x: self._done())\n        self._waitForTest()\n\n        Example (inline callbacks! yay!):\n\n        yield self.node.terminate_instance(instance_id)\n        rv = yield self.node.describe_instances()\n        self.assertEqual(rv, [])\n\n        If the test fits the Inline Callbacks pattern we will automatically\n        handle calling wait and done.\n        """'
newline|'\n'
comment|'# TODO(termie): this can be a wrapper function instead and'
nl|'\n'
comment|"#               and we can make a metaclass so that we don't"
nl|'\n'
comment|'#               have to copy all that "run" code below.'
nl|'\n'
name|'g'
op|'='
name|'f'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'g'
op|','
string|"'send'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'g'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'inlined'
op|'='
name|'defer'
op|'.'
name|'inlineCallbacks'
op|'('
name|'f'
op|')'
newline|'\n'
name|'d'
op|'='
name|'inlined'
op|'('
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|_catchExceptions
dedent|''
name|'def'
name|'_catchExceptions'
op|'('
name|'self'
op|','
name|'result'
op|','
name|'failure'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
op|'('
name|'failure'
op|'.'
name|'type'
op|','
name|'failure'
op|'.'
name|'value'
op|','
name|'failure'
op|'.'
name|'getTracebackObject'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'failure'
op|'.'
name|'value'
op|','
name|'self'
op|'.'
name|'failureException'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'addFailure'
op|'('
name|'self'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'failure'
op|'.'
name|'value'
op|','
name|'KeyboardInterrupt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'addError'
op|'('
name|'self'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_timeout
dedent|''
name|'def'
name|'_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_waiting'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_timedOut'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'result'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'result'
name|'is'
name|'None'
op|':'
name|'result'
op|'='
name|'self'
op|'.'
name|'defaultTestResult'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'.'
name|'startTest'
op|'('
name|'self'
op|')'
newline|'\n'
name|'testMethod'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'_testMethodName'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyboardInterrupt'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'addError'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'_exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'ok'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'self'
op|'.'
name|'_maybeInlineCallbacks'
op|'('
name|'testMethod'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'_catchExceptions'
op|'('
name|'result'
op|','
name|'x'
op|')'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addBoth'
op|'('
name|'lambda'
name|'x'
op|':'
name|'self'
op|'.'
name|'_done'
op|'('
op|')'
name|'and'
name|'x'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_waitForTest'
op|'('
op|')'
newline|'\n'
name|'ok'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'failureException'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'addFailure'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'_exc_info'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyboardInterrupt'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'addError'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'_exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyboardInterrupt'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'addError'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'_exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'ok'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'ok'
op|':'
name|'result'
op|'.'
name|'addSuccess'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'stopTest'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
