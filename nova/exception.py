begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
string|'"""\nNova base exception handling, including decorator for re-raising\nNova-type exceptions. SHOULD include dedicated exception logging.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.exception'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
name|'class'
name|'ProcessExecutionError'
op|'('
name|'IOError'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'exit_code'
op|'='
name|'None'
op|','
name|'cmd'
op|'='
name|'None'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
name|'_'
op|'('
string|'"Unexpected error while running command."'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exit_code'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'exit_code'
op|'='
string|"'-'"
newline|'\n'
dedent|''
name|'message'
op|'='
name|'_'
op|'('
string|'"%s\\nCommand: %s\\nExit code: %s\\nStdout: %r\\nStderr: %r"'
op|')'
op|'%'
op|'('
name|'description'
op|','
name|'cmd'
op|','
name|'exit_code'
op|','
name|'stdout'
op|','
name|'stderr'
op|')'
newline|'\n'
name|'IOError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Error
dedent|''
dedent|''
name|'class'
name|'Error'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Error'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiError
dedent|''
dedent|''
name|'class'
name|'ApiError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
string|"'Unknown'"
op|','
name|'code'
op|'='
string|"'Unknown'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'message'
op|'='
name|'message'
newline|'\n'
name|'self'
op|'.'
name|'code'
op|'='
name|'code'
newline|'\n'
name|'super'
op|'('
name|'ApiError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|"'%s: %s'"
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotFound
dedent|''
dedent|''
name|'class'
name|'NotFound'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Duplicate
dedent|''
name|'class'
name|'Duplicate'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotAuthorized
dedent|''
name|'class'
name|'NotAuthorized'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotEmpty
dedent|''
name|'class'
name|'NotEmpty'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Invalid
dedent|''
name|'class'
name|'Invalid'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidInputException
dedent|''
name|'class'
name|'InvalidInputException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimeoutException
dedent|''
name|'class'
name|'TimeoutException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DBError
dedent|''
name|'class'
name|'DBError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps an implementation specific exception"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'inner_exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inner_exception'
op|'='
name|'inner_exception'
newline|'\n'
name|'super'
op|'('
name|'DBError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'str'
op|'('
name|'inner_exception'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_db_error
dedent|''
dedent|''
name|'def'
name|'wrap_db_error'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB exception wrapped'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'DBError'
op|'('
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_wrap'
newline|'\n'
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_exception
dedent|''
name|'def'
name|'wrap_exception'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
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
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'e'
op|','
name|'Error'
op|')'
op|':'
newline|'\n'
comment|'#exc_type, exc_value, exc_traceback = sys.exc_info()'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Uncaught exception'"
op|')'
op|')'
newline|'\n'
comment|'#logging.error(traceback.extract_stack(exc_traceback))'
nl|'\n'
name|'raise'
name|'Error'
op|'('
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
name|'return'
name|'_wrap'
newline|'\n'
dedent|''
endmarker|''
end_unit
