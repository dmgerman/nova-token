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
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
DECL|class|Error
name|'class'
name|'Error'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
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
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'Uncaught exception'"
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
nl|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
