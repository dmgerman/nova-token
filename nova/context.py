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
string|'"""RequestContext: context for requests that persist through all of nova."""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestContext
name|'class'
name|'RequestContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Security context and request information.\n\n    Represents the user taking a given action within the system.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|','
name|'is_admin'
op|'='
name|'None'
op|','
name|'read_deleted'
op|'='
name|'False'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'None'
op|','
name|'timestamp'
op|'='
name|'None'
op|','
name|'request_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'auth_token'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'user'
op|','
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_user'
op|'='
name|'user'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
name|'user'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_user'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
name|'user'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'project'
op|','
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_project'
op|'='
name|'project'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_project'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
name|'project'
newline|'\n'
dedent|''
name|'if'
name|'is_admin'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'user_id'
name|'and'
name|'self'
op|'.'
name|'user'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'is_admin'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_admin'
op|'='
name|'is_admin'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'read_deleted'
op|'='
name|'read_deleted'
newline|'\n'
name|'self'
op|'.'
name|'remote_address'
op|'='
name|'remote_address'
newline|'\n'
name|'if'
name|'not'
name|'timestamp'
op|':'
newline|'\n'
indent|'            '
name|'timestamp'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'timestamp'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'timestamp'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'timestamp'
op|'='
name|'utils'
op|'.'
name|'parse_isotime'
op|'('
name|'timestamp'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'timestamp'
op|'='
name|'timestamp'
newline|'\n'
name|'if'
name|'not'
name|'request_id'
op|':'
newline|'\n'
indent|'            '
name|'chars'
op|'='
string|"'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-'"
newline|'\n'
name|'request_id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
name|'chars'
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'20'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'request_id'
op|'='
name|'request_id'
newline|'\n'
name|'self'
op|'.'
name|'auth_token'
op|'='
name|'auth_token'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|user
name|'def'
name|'user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Delay import of manager, so that we can import this'
nl|'\n'
comment|'#             file from manager.'
nl|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_user'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_user'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_user'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|project
name|'def'
name|'project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Delay import of manager, so that we can import this'
nl|'\n'
comment|'#             file from manager.'
nl|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_project'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'auth_manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_project'
op|'='
name|'auth_manager'
op|'.'
name|'get_project'
op|'('
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_project'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'user'"
op|':'
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'is_admin'"
op|':'
name|'self'
op|'.'
name|'is_admin'
op|','
nl|'\n'
string|"'read_deleted'"
op|':'
name|'self'
op|'.'
name|'read_deleted'
op|','
nl|'\n'
string|"'remote_address'"
op|':'
name|'self'
op|'.'
name|'remote_address'
op|','
nl|'\n'
string|"'timestamp'"
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
name|'self'
op|'.'
name|'timestamp'
op|')'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'self'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'auth_token'"
op|':'
name|'self'
op|'.'
name|'auth_token'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|elevated
dedent|''
name|'def'
name|'elevated'
op|'('
name|'self'
op|','
name|'read_deleted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a version of this context with admin flag set."""'
newline|'\n'
name|'return'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'True'
op|','
nl|'\n'
name|'read_deleted'
op|','
nl|'\n'
name|'self'
op|'.'
name|'remote_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'timestamp'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'auth_token'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_admin_context
dedent|''
dedent|''
name|'def'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'RequestContext'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'True'
op|','
name|'read_deleted'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
