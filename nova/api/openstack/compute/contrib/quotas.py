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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|authorize_update
name|'authorize_update'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'quotas:update'"
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
string|"'quotas:show'"
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
string|"'quotas:delete'"
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
DECL|class|QuotaSetsController
dedent|''
dedent|''
name|'class'
name|'QuotaSetsController'
op|'('
name|'object'
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
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
DECL|member|_format_quota_set
dedent|''
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
nl|'\n'
name|'result'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'str'
op|'('
name|'project_id'
op|')'
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
name|'result'
op|'['
name|'resource'
op|']'
op|'='
name|'quota_set'
op|'['
name|'resource'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'quota_set'
op|'='
name|'result'
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
name|'usages'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
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
nl|'\n'
name|'bad_keys'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'key'
name|'not'
name|'in'
name|'QUOTAS'
name|'and'
nl|'\n'
name|'key'
op|'!='
string|"'tenant_id'"
name|'and'
nl|'\n'
name|'key'
op|'!='
string|"'id'"
op|')'
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
nl|'\n'
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
name|'for'
name|'key'
name|'in'
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'int'
op|'('
name|'body'
op|'['
string|"'quota_set'"
op|']'
op|'['
name|'key'
op|']'
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
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Quota for %s should be integer."'
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
comment|'# NOTE(hzzhoushaoyu): Do not prevent valid value to be'
nl|'\n'
comment|'# updated. If raise BadRequest, some may be updated and'
nl|'\n'
comment|'# others may be not.'
nl|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_validate_quota_limit'
op|'('
name|'value'
op|')'
newline|'\n'
name|'try'
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
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProjectQuotaNotFound'
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
op|'{'
string|"'quota_set'"
op|':'
name|'self'
op|'.'
name|'_get_quotas'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
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
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-quotas'"
op|')'
op|':'
newline|'\n'
indent|'            '
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
name|'try'
op|':'
newline|'\n'
indent|'                '
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
name|'QUOTAS'
op|'.'
name|'destroy_all_by_project'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotAuthorized'
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Quotas
dedent|''
dedent|''
name|'class'
name|'Quotas'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
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
string|'"os-quota-sets"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/quotas-sets/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-08T00:00:00+00:00"'
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
string|"'os-quota-sets'"
op|','
nl|'\n'
name|'QuotaSetsController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'defaults'"
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
dedent|''
dedent|''
endmarker|''
end_unit
