begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_keys
name|'def'
name|'_translate_keys'
op|'('
name|'user'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
name|'name'
op|'='
name|'user'
op|'.'
name|'name'
op|','
nl|'\n'
name|'access'
op|'='
name|'user'
op|'.'
name|'access'
op|','
nl|'\n'
name|'secret'
op|'='
name|'user'
op|'.'
name|'secret'
op|','
nl|'\n'
name|'admin'
op|'='
name|'user'
op|'.'
name|'admin'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
indent|'    '
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"user"'
op|':'
op|'['
string|'"id"'
op|','
string|'"name"'
op|','
string|'"access"'
op|','
string|'"secret"'
op|','
string|'"admin"'
op|']'
op|'}'
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_admin
dedent|''
name|'def'
name|'_check_admin'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""We cannot depend on the db layer to check for admin access\n           for the auth manager, so we do it here"""'
newline|'\n'
name|'if'
name|'not'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'_'
op|'('
string|'"Not admin user"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all users in brief"""'
newline|'\n'
name|'users'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_users'
op|'('
op|')'
newline|'\n'
name|'users'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'users'
op|','
name|'req'
op|')'
newline|'\n'
name|'users'
op|'='
op|'['
name|'_translate_keys'
op|'('
name|'user'
op|')'
name|'for'
name|'user'
name|'in'
name|'users'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'users'
op|'='
name|'users'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all users in detail"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given user id"""'
newline|'\n'
nl|'\n'
comment|'#NOTE(justinsb): The drivers are a little inconsistent in how they'
nl|'\n'
comment|'#  deal with "NotFound" - some throw, some return None.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'user'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'user'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'id'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
name|'is_admin'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'admin'"
op|')'
name|'in'
op|'('
string|"'T'"
op|','
string|"'True'"
op|','
name|'True'
op|')'
newline|'\n'
name|'name'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'access'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'access'"
op|')'
newline|'\n'
name|'secret'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'secret'"
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
name|'name'
op|','
name|'access'
op|','
name|'secret'
op|','
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'user'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_admin'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
name|'is_admin'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'admin'"
op|')'
newline|'\n'
name|'if'
name|'is_admin'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'is_admin'
op|'='
name|'is_admin'
name|'in'
op|'('
string|"'T'"
op|','
string|"'True'"
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
name|'access'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'access'"
op|')'
newline|'\n'
name|'secret'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'.'
name|'get'
op|'('
string|"'secret'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'modify_user'
op|'('
name|'id'
op|','
name|'access'
op|','
name|'secret'
op|','
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'user'
op|'='
name|'_translate_keys'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
name|'id'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
