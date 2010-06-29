begin_unit
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allow
name|'def'
name|'allow'
op|'('
op|'*'
name|'roles'
op|')'
op|':'
newline|'\n'
DECL|function|wrap
indent|'    '
name|'def'
name|'wrap'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped_f
indent|'        '
name|'def'
name|'wrapped_f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_superuser'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'role'
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'__matches_role'
op|'('
name|'context'
op|','
name|'role'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped_f'
newline|'\n'
dedent|''
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
DECL|function|deny
dedent|''
name|'def'
name|'deny'
op|'('
op|'*'
name|'roles'
op|')'
op|':'
newline|'\n'
DECL|function|wrap
indent|'    '
name|'def'
name|'wrap'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped_f
indent|'        '
name|'def'
name|'wrapped_f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_superuser'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'role'
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'__matches_role'
op|'('
name|'context'
op|','
name|'role'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped_f'
newline|'\n'
dedent|''
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
DECL|function|__matches_role
dedent|''
name|'def'
name|'__matches_role'
op|'('
name|'context'
op|','
name|'role'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'role'
op|'=='
string|"'all'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'role'
op|'=='
string|"'none'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'context'
op|'.'
name|'project'
op|'.'
name|'has_role'
op|'('
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
name|'role'
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
