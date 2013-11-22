begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'urlparse'
newline|'\n'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-quota-sets"'
newline|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|authorize_update
name|'authorize_update'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:update'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_show
name|'authorize_show'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:show'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_delete
name|'authorize_delete'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:delete'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_detail
name|'authorize_detail'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:detail'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaTemplate
name|'class'
name|'QuotaTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'quota_set'"
op|','
name|'selector'
op|'='
string|"'quota_set'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'QUOTAS'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
name|'resource'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'text'
op|'='
name|'resource'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaDetailTemplate
dedent|''
dedent|''
name|'class'
name|'QuotaDetailTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'quota_set'"
op|','
name|'selector'
op|'='
string|"'quota_set'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'QUOTAS'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
name|'resource'
op|','
nl|'\n'
name|'selector'
op|'='
name|'resource'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'in_use'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'reserved'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'limit'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSetsController
dedent|''
dedent|''
name|'class'
name|'QuotaSetsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_format_quota_set
indent|'    '
name|'def'
name|'_format_quota_set'
op|'('
name|'self'
op|','
name|'project_id'
op|','
name|'quota_set'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert the quota object to a result dict."""'
newline|'\n'
name|'quota_set'
op|'.'
name|'update'
op|'('
name|'id'
op|'='
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'quota_set'
op|'='
name|'quota_set'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_quota_limit
dedent|''
name|'def'
name|'_validate_quota_limit'
op|'('
name|'self'
op|','
name|'limit'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: -1 is a flag value for unlimited'
nl|'\n'
indent|'        '
name|'if'
name|'limit'
op|'<'
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota limit must be -1 or greater."'
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
dedent|''
name|'if'
op|'('
op|'('
name|'limit'
op|'<'
name|'minimum'
op|')'
name|'and'
nl|'\n'
op|'('
name|'maximum'
op|'!='
op|'-'
number|'1'
name|'or'
op|'('
name|'maximum'
op|'=='
op|'-'
number|'1'
name|'and'
name|'limit'
op|'!='
op|'-'
number|'1'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota limit must greater than %s."'
op|')'
op|'%'
name|'minimum'
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
dedent|''
name|'if'
name|'maximum'
op|'!='
op|'-'
number|'1'
name|'and'
name|'limit'
op|'>'
name|'maximum'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota limit must less than %s."'
op|')'
op|'%'
name|'maximum'
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
DECL|member|_get_quotas
dedent|''
dedent|''
name|'def'
name|'_get_quotas'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|'='
name|'None'
op|','
name|'usages'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_user_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'usages'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'usages'
op|'='
name|'usages'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'usages'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'values'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|'['
string|"'limit'"
op|']'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'values'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'403'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'QuotaTemplate'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_show'
op|'('
name|'context'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nova'
op|'.'
name|'context'
op|'.'
name|'authorize_project_context'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|'='
name|'user_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'403'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'QuotaDetailTemplate'
op|')'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_detail'
op|'('
name|'context'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nova'
op|'.'
name|'context'
op|'.'
name|'authorize_project_context'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'QuotaTemplate'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_update'
op|'('
name|'context'
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'id'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'bad_keys'
op|'='
op|'['
op|']'
newline|'\n'
name|'force_update'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'quota_set'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"quota_set not specified"'
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
dedent|''
name|'quota_set'
op|'='
name|'body'
op|'['
string|"'quota_set'"
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'quota_set'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'not'
name|'in'
name|'QUOTAS'
name|'and'
name|'key'
op|'!='
string|"'force'"
op|':'
newline|'\n'
indent|'                '
name|'bad_keys'
op|'.'
name|'append'
op|'('
name|'key'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'=='
string|"'force'"
op|':'
newline|'\n'
indent|'                '
name|'force_update'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'key'
op|'!='
string|"'force'"
name|'and'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota value for key \'%(key)s\' should be an "'
nl|'\n'
string|'"integer.  It is actually type \'%(vtype)s\'."'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'msg'
op|'%'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
string|"'vtype'"
op|':'
name|'type'
op|'('
name|'value'
op|')'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'msg'
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
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'bad_keys'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Bad key(s) %s in quota_set"'
op|')'
op|'%'
string|'","'
op|'.'
name|'join'
op|'('
name|'bad_keys'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'settable_quotas'
op|'='
name|'QUOTAS'
op|'.'
name|'get_settable_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'quotas'
op|'='
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Force update quotas: %s"'
op|')'
op|','
name|'force_update'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'force'"
name|'or'
op|'('
name|'not'
name|'value'
name|'and'
name|'value'
op|'!='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
comment|'# validate whether already used and reserved exceeds the new'
nl|'\n'
comment|'# quota, this check will be ignored if admin want to force'
nl|'\n'
comment|'# update'
nl|'\n'
dedent|''
name|'value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
name|'if'
name|'force_update'
name|'is'
name|'not'
name|'True'
name|'and'
name|'value'
op|'>='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'quota_value'
op|'='
name|'quotas'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'quota_value'
name|'and'
name|'quota_value'
op|'['
string|"'limit'"
op|']'
op|'>='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'quota_used'
op|'='
op|'('
name|'quota_value'
op|'['
string|"'in_use'"
op|']'
op|'+'
nl|'\n'
name|'quota_value'
op|'['
string|"'reserved'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Quota %(key)s used: %(quota_used)s, "'
nl|'\n'
string|'"value: %(value)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
string|"'quota_used'"
op|':'
name|'quota_used'
op|','
nl|'\n'
string|"'value'"
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'quota_used'
op|'>'
name|'value'
op|':'
newline|'\n'
indent|'                        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota value %(value)s for %(key)s are "'
nl|'\n'
string|'"less than already used and reserved "'
nl|'\n'
string|'"%(quota_used)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'value'"
op|':'
name|'value'
op|','
string|"'key'"
op|':'
name|'key'
op|','
nl|'\n'
string|"'quota_used'"
op|':'
name|'quota_used'
op|'}'
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
dedent|''
dedent|''
name|'minimum'
op|'='
name|'settable_quotas'
op|'['
name|'key'
op|']'
op|'['
string|"'minimum'"
op|']'
newline|'\n'
name|'maximum'
op|'='
name|'settable_quotas'
op|'['
name|'key'
op|']'
op|'['
string|"'maximum'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_validate_quota_limit'
op|'('
name|'value'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'key'
op|','
name|'value'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'QuotaExists'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'quota_update'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'key'
op|','
name|'value'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AdminRequired'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|')'
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
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'QuotaTemplate'
op|')'
newline|'\n'
DECL|member|defaults
name|'def'
name|'defaults'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_show'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'id'
op|','
name|'QUOTAS'
op|'.'
name|'get_defaults'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'403'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
op|')'
newline|'\n'
DECL|member|delete
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize_delete'
op|'('
name|'context'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'QUERY_STRING'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'user_id'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'user_id'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nova'
op|'.'
name|'context'
op|'.'
name|'authorize_project_context'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'user_id'
op|':'
newline|'\n'
indent|'                '
name|'QUOTAS'
op|'.'
name|'destroy_all_by_project_and_user'
op|'('
name|'context'
op|','
nl|'\n'
name|'id'
op|','
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'QUOTAS'
op|'.'
name|'destroy_all_by_project'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSets
dedent|''
dedent|''
dedent|''
name|'class'
name|'QuotaSets'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quotas management support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Quotas"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/os-quotas-sets/api/v3"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'QuotaSetsController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'defaults'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
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
