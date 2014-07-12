begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
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
op|'.'
name|'consoleauth'
name|'import'
name|'rpcapi'
name|'as'
name|'consoleauth_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-console-auth-tokens"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthTokensController
name|'class'
name|'ConsoleAuthTokensController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_consoleauth_rpcapi'
op|'='
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'ConsoleAuthTokensController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'401'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
DECL|member|show
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
string|'"""Checks a console auth token and returns the related connect info."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'token'
op|'='
name|'id'
newline|'\n'
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"token not provided"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'connect_info'
op|'='
name|'self'
op|'.'
name|'_consoleauth_rpcapi'
op|'.'
name|'check_token'
op|'('
name|'context'
op|','
name|'token'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'connect_info'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Token not found"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'console_type'
op|'='
name|'connect_info'
op|'.'
name|'get'
op|'('
string|"'console_type'"
op|')'
newline|'\n'
comment|'# This is currently required only for RDP consoles'
nl|'\n'
name|'if'
name|'console_type'
op|'!='
string|'"rdp-html5"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"The requested console type details are not "'
nl|'\n'
string|'"accessible"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'console'"
op|':'
nl|'\n'
name|'dict'
op|'('
op|'['
op|'('
name|'i'
op|','
name|'connect_info'
op|'['
name|'i'
op|']'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
op|'['
string|"'instance_uuid'"
op|','
string|"'host'"
op|','
string|"'port'"
op|','
nl|'\n'
string|"'internal_access_path'"
op|']'
nl|'\n'
name|'if'
name|'i'
name|'in'
name|'connect_info'
op|']'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthTokens
dedent|''
dedent|''
name|'class'
name|'ConsoleAuthTokens'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Console token authentication support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ConsoleAuthTokens"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'ConsoleAuthTokensController'
op|'('
op|')'
newline|'\n'
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-console-auth-tokens'"
op|','
nl|'\n'
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ext'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
