begin_unit
comment|'# Copyright (c) 2007 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.python.monkey}.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'monkey'
name|'import'
name|'MonkeyPatcher'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestObj
name|'class'
name|'TestObj'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'foo'
op|'='
string|"'foo value'"
newline|'\n'
name|'self'
op|'.'
name|'bar'
op|'='
string|"'bar value'"
newline|'\n'
name|'self'
op|'.'
name|'baz'
op|'='
string|"'baz value'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MonkeyPatcherTest
dedent|''
dedent|''
name|'class'
name|'MonkeyPatcherTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{MonkeyPatcher} monkey-patching class.\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'testObject'
op|'='
name|'TestObj'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'originalObject'
op|'='
name|'TestObj'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'='
name|'MonkeyPatcher'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_empty
dedent|''
name|'def'
name|'test_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        A monkey patcher without patches shouldn\'t change a thing.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# We can't assert that all state is unchanged, but at least we can"
nl|'\n'
comment|'# check our test object.'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'bar'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'bar'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'baz'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'baz'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_constructWithPatches
dedent|''
name|'def'
name|'test_constructWithPatches'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Constructing a L{MonkeyPatcher} with patches should add all of the\n        given patches to the patch list.\n        """'
newline|'\n'
name|'patcher'
op|'='
name|'MonkeyPatcher'
op|'('
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'haha'"
op|')'
op|','
nl|'\n'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'bar'"
op|','
string|"'hehe'"
op|')'
op|')'
newline|'\n'
name|'patcher'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'haha'"
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'hehe'"
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'bar'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'baz'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'baz'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_patchExisting
dedent|''
name|'def'
name|'test_patchExisting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Patching an attribute that exists sets it to the value defined in the\n        patch.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'haha'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
string|"'haha'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_patchNonExisting
dedent|''
name|'def'
name|'test_patchNonExisting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Patching a non-existing attribute fails with an C{AttributeError}.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'nowhere'"
op|','
nl|'\n'
string|"'blow up please'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'patch'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_patchAlreadyPatched
dedent|''
name|'def'
name|'test_patchAlreadyPatched'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Adding a patch for an object and attribute that already have a patch\n        overrides the existing patch.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'blah'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'BLAH'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
string|"'BLAH'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'restore'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_restoreTwiceIsANoOp
dedent|''
name|'def'
name|'test_restoreTwiceIsANoOp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Restoring an already-restored monkey patch is a no-op.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'blah'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'restore'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'restore'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_runWithPatchesDecoration
dedent|''
name|'def'
name|'test_runWithPatchesDecoration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        runWithPatches should run the given callable, passing in all arguments\n        and keyword arguments, and return the return value of the callable.\n        """'
newline|'\n'
name|'log'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'a'
op|','
name|'b'
op|','
name|'c'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'append'
op|'('
op|'('
name|'a'
op|','
name|'b'
op|','
name|'c'
op|')'
op|')'
newline|'\n'
name|'return'
string|"'foo'"
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'runWithPatches'
op|'('
name|'f'
op|','
number|'1'
op|','
number|'2'
op|','
name|'c'
op|'='
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'foo'"
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'('
number|'1'
op|','
number|'2'
op|','
number|'10'
op|')'
op|']'
op|','
name|'log'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_repeatedRunWithPatches
dedent|''
name|'def'
name|'test_repeatedRunWithPatches'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        We should be able to call the same function with runWithPatches more\n        than once. All patches should apply for each call.\n        """'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'bar'
op|','
nl|'\n'
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'baz'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'haha'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'runWithPatches'
op|'('
name|'f'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
op|'('
string|"'haha'"
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'bar'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'baz'
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'runWithPatches'
op|'('
name|'f'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
op|'('
string|"'haha'"
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'bar'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'baz'
op|')'
op|','
nl|'\n'
name|'result'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_runWithPatchesRestores
dedent|''
name|'def'
name|'test_runWithPatchesRestores'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        C{runWithPatches} should restore the original values after the function\n        has executed.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'haha'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'runWithPatches'
op|'('
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_runWithPatchesRestoresOnException
dedent|''
name|'def'
name|'test_runWithPatchesRestoresOnException'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Test runWithPatches restores the original values even when the function\n        raises an exception.\n        """'
newline|'\n'
DECL|function|_
name|'def'
name|'_'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
string|"'haha'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'bar'
op|','
string|"'blahblah'"
op|')'
newline|'\n'
name|'raise'
name|'RuntimeError'
op|','
string|'"Something went wrong!"'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'foo'"
op|','
string|"'haha'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'addPatch'
op|'('
name|'self'
op|'.'
name|'testObject'
op|','
string|"'bar'"
op|','
string|"'blahblah'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RuntimeError'
op|','
name|'self'
op|'.'
name|'monkeyPatcher'
op|'.'
name|'runWithPatches'
op|','
name|'_'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'foo'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'foo'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'testObject'
op|'.'
name|'bar'
op|','
name|'self'
op|'.'
name|'originalObject'
op|'.'
name|'bar'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
