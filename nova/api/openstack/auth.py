begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
name|'as'
name|'base_wsgi'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_forwarded_for'"
op|','
string|"'nova.api.auth'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoAuthMiddlewareBase
name|'class'
name|'NoAuthMiddlewareBase'
op|'('
name|'base_wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a fake token if one isn\'t specified."""'
newline|'\n'
nl|'\n'
DECL|member|base_call
name|'def'
name|'base_call'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'project_id_in_path'
op|','
name|'always_admin'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'X-Auth-Token'"
name|'not'
name|'in'
name|'req'
op|'.'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'user_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Auth-User'"
op|','
string|"'admin'"
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Auth-Project-Id'"
op|','
string|"'admin'"
op|')'
newline|'\n'
name|'if'
name|'project_id_in_path'
op|':'
newline|'\n'
indent|'                '
name|'os_url'
op|'='
string|"'/'"
op|'.'
name|'join'
op|'('
op|'['
name|'req'
op|'.'
name|'url'
op|'.'
name|'rstrip'
op|'('
string|"'/'"
op|')'
op|','
name|'project_id'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'os_url'
op|'='
name|'req'
op|'.'
name|'url'
op|'.'
name|'rstrip'
op|'('
string|"'/'"
op|')'
newline|'\n'
dedent|''
name|'res'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): This is expecting and returning Auth(1.1), whereas'
nl|'\n'
comment|'#             keystone uses 2.0 auth.  We should probably allow'
nl|'\n'
comment|'#             2.0 auth here as well.'
nl|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Server-Management-Url'"
op|']'
op|'='
name|'os_url'
newline|'\n'
name|'res'
op|'.'
name|'content_type'
op|'='
string|"'text/plain'"
newline|'\n'
name|'res'
op|'.'
name|'status'
op|'='
string|"'204'"
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
dedent|''
name|'token'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-Token'"
op|']'
newline|'\n'
name|'user_id'
op|','
name|'_sep'
op|','
name|'project_id'
op|'='
name|'token'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'project_id'
name|'or'
name|'user_id'
newline|'\n'
name|'remote_address'
op|'='
name|'getattr'
op|'('
name|'req'
op|','
string|"'remote_address'"
op|','
string|"'127.0.0.1'"
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'is_admin'
op|'='
name|'always_admin'
name|'or'
op|'('
name|'user_id'
op|'=='
string|"'admin'"
op|')'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'is_admin'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'ctx'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoAuthMiddleware
dedent|''
dedent|''
name|'class'
name|'NoAuthMiddleware'
op|'('
name|'NoAuthMiddlewareBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a fake token if one isn\'t specified.\n\n    noauth2 provides admin privs if \'admin\' is provided as the user id.\n\n    """'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'base_call'
op|'('
name|'req'
op|','
name|'True'
op|','
name|'always_admin'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoAuthMiddlewareV2_18
dedent|''
dedent|''
name|'class'
name|'NoAuthMiddlewareV2_18'
op|'('
name|'NoAuthMiddlewareBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a fake token if one isn\'t specified.\n\n    This provides a version of the middleware which does not add\n    project_id into server management urls.\n\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'base_call'
op|'('
name|'req'
op|','
name|'False'
op|','
name|'always_admin'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
