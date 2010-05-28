begin_unit
comment|'# -*- test-case-name: twisted.test.test_monkey -*-'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2007 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|MonkeyPatcher
name|'class'
name|'MonkeyPatcher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Cover up attributes with new objects. Neat for monkey-patching things for\n    unit-testing purposes.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'patches'
op|')'
op|':'
newline|'\n'
comment|'# List of patches to apply in (obj, name, value).'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_patchesToApply'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# List of the original values for things that have been patched.'
nl|'\n'
comment|'# (obj, name, value) format.'
nl|'\n'
name|'self'
op|'.'
name|'_originals'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'patch'
name|'in'
name|'patches'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'addPatch'
op|'('
op|'*'
name|'patch'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|addPatch
dedent|''
dedent|''
name|'def'
name|'addPatch'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add a patch so that the attribute C{name} on C{obj} will be assigned to\n        C{value} when C{patch} is called or during C{runWithPatches}.\n\n        You can restore the original values with a call to restore().\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_patchesToApply'
op|'.'
name|'append'
op|'('
op|'('
name|'obj'
op|','
name|'name'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_alreadyPatched
dedent|''
name|'def'
name|'_alreadyPatched'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Has the C{name} attribute of C{obj} already been patched by this\n        patcher?\n        """'
newline|'\n'
name|'for'
name|'o'
op|','
name|'n'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_originals'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'o'
op|','
name|'n'
op|')'
op|'=='
op|'('
name|'obj'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|patch
dedent|''
name|'def'
name|'patch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Apply all of the patches that have been specified with L{addPatch}.\n        Reverse this operation using L{restore}.\n        """'
newline|'\n'
name|'for'
name|'obj'
op|','
name|'name'
op|','
name|'value'
name|'in'
name|'self'
op|'.'
name|'_patchesToApply'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_alreadyPatched'
op|'('
name|'obj'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_originals'
op|'.'
name|'append'
op|'('
op|'('
name|'obj'
op|','
name|'name'
op|','
name|'getattr'
op|'('
name|'obj'
op|','
name|'name'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'setattr'
op|'('
name|'obj'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|restore
dedent|''
dedent|''
name|'def'
name|'restore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Restore all original values to any patched objects.\n        """'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'_originals'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|','
name|'name'
op|','
name|'value'
op|'='
name|'self'
op|'.'
name|'_originals'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'obj'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|runWithPatches
dedent|''
dedent|''
name|'def'
name|'runWithPatches'
op|'('
name|'self'
op|','
name|'f'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Apply each patch already specified. Then run the function f with the\n        given args and kwargs. Restore everything when done.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'patch'
op|'('
op|')'
newline|'\n'
name|'try'
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
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'restore'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
