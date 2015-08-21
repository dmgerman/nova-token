begin_unit
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
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|NON_QUOTA_KEYS
name|'NON_QUOTA_KEYS'
op|'='
op|'['
string|"'tenant_id'"
op|','
string|"'id'"
op|','
string|"'force'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Quotas that are only enabled by specific extensions'
nl|'\n'
DECL|variable|EXTENDED_QUOTAS
name|'EXTENDED_QUOTAS'
op|'='
op|'{'
string|"'server_groups'"
op|':'
string|"'os-server-group-quotas'"
op|','
nl|'\n'
string|"'server_group_members'"
op|':'
string|"'os-server-group-quotas'"
op|'}'
newline|'\n'
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
DECL|class|QuotaSetsController
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
DECL|variable|supported_quotas
indent|'    '
name|'supported_quotas'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'self'
op|'.'
name|'supported_quotas'
op|'='
name|'QUOTAS'
op|'.'
name|'resources'
newline|'\n'
name|'for'
name|'resource'
op|','
name|'extension'
name|'in'
name|'EXTENDED_QUOTAS'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
name|'extension'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'supported_quotas'
op|'.'
name|'remove'
op|'('
name|'resource'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_quota_set
dedent|''
dedent|''
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
name|'if'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'resource'
name|'in'
name|'self'
op|'.'
name|'supported_quotas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'resource'
name|'in'
name|'quota_set'
op|':'
newline|'\n'
indent|'                '
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
name|'resource'
op|','
name|'limit'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: -1 is a flag value for unlimited, maximum value is limited'
nl|'\n'
comment|"# by SQL standard integer type `INT` which is `0x7FFFFFFF`, it's a"
nl|'\n'
comment|'# general value for SQL, using a hardcoded value here is not a'
nl|'\n'
comment|'# `nice` way, but it seems like the only way for now:'
nl|'\n'
comment|'# http://dev.mysql.com/doc/refman/5.0/en/integer-types.html'
nl|'\n'
comment|'# http://www.postgresql.org/docs/9.1/static/datatype-numeric.html'
nl|'\n'
indent|'        '
name|'if'
name|'limit'
op|'<'
op|'-'
number|'1'
name|'or'
name|'limit'
op|'>'
name|'db'
op|'.'
name|'MAX_INT'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s "'
nl|'\n'
string|'"must be in the range of -1 and %(max)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'max'"
op|':'
name|'db'
op|'.'
name|'MAX_INT'
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
DECL|function|conv_inf
dedent|''
name|'def'
name|'conv_inf'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'float'
op|'('
string|'"inf"'
op|')'
name|'if'
name|'value'
op|'=='
op|'-'
number|'1'
name|'else'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'conv_inf'
op|'('
name|'limit'
op|')'
op|'<'
name|'conv_inf'
op|'('
name|'minimum'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s must "'
nl|'\n'
string|'"be greater than or equal to already used and "'
nl|'\n'
string|'"reserved %(minimum)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'minimum'"
op|':'
name|'minimum'
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
dedent|''
name|'if'
name|'conv_inf'
op|'('
name|'limit'
op|')'
op|'>'
name|'conv_inf'
op|'('
name|'maximum'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Quota limit %(limit)s for %(resource)s must be "'
nl|'\n'
string|'"less than or equal to %(maximum)s."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'maximum'"
op|':'
name|'maximum'
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
op|'{'
name|'k'
op|':'
name|'v'
op|'['
string|"'limit'"
op|']'
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
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
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
name|'None'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-user-quotas'"
op|')'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
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
name|'Forbidden'
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
DECL|member|update
dedent|''
dedent|''
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
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
indent|'            '
name|'nova'
op|'.'
name|'context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AdminRequired'
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
nl|'\n'
comment|'# By default, we can force update the quota if the extended'
nl|'\n'
comment|'# is not loaded'
nl|'\n'
name|'force_update'
op|'='
name|'True'
newline|'\n'
name|'extended_loaded'
op|'='
name|'False'
newline|'\n'
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
comment|'# force optional has been enabled, the default value of'
nl|'\n'
comment|'# force_update need to be changed to False'
nl|'\n'
indent|'            '
name|'extended_loaded'
op|'='
name|'True'
newline|'\n'
name|'force_update'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'user_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-user-quotas'"
op|')'
op|':'
newline|'\n'
comment|'# Update user quotas only if the extended is loaded'
nl|'\n'
indent|'            '
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
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks.'
nl|'\n'
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
name|'Forbidden'
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
comment|'# NOTE(dims): Pass #1 - In this loop for quota_set.items(), we figure'
nl|'\n'
comment|'# out if we have bad keys or if we need to forcibly set quotas or'
nl|'\n'
comment|'# if some of the values for the quotas can be converted to integers.'
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
op|'('
name|'key'
name|'not'
name|'in'
name|'self'
op|'.'
name|'supported_quotas'
nl|'\n'
name|'and'
name|'key'
name|'not'
name|'in'
name|'NON_QUOTA_KEYS'
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
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'=='
string|"'force'"
name|'and'
name|'extended_loaded'
op|':'
newline|'\n'
comment|'# only check the force optional when the extended has'
nl|'\n'
comment|'# been loaded'
nl|'\n'
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
name|'not'
name|'in'
name|'NON_QUOTA_KEYS'
name|'and'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'utils'
op|'.'
name|'validate_integer'
op|'('
name|'value'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'bad_keys'
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
comment|'# NOTE(dims): Pass #2 - In this loop for quota_set.items(), based on'
nl|'\n'
comment|'# force_update flag we validate the quota limit. A loop just for'
nl|'\n'
comment|'# the validation of min/max values ensure that we can bail out if'
nl|'\n'
comment|'# any of the items in the set is bad.'
nl|'\n'
dedent|''
name|'valid_quotas'
op|'='
op|'{'
op|'}'
newline|'\n'
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
name|'in'
name|'NON_QUOTA_KEYS'
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
name|'not'
name|'force_update'
op|':'
newline|'\n'
indent|'                '
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
name|'key'
op|','
name|'value'
op|','
name|'minimum'
op|','
name|'maximum'
op|')'
newline|'\n'
dedent|''
name|'valid_quotas'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
comment|'# NOTE(dims): Pass #3 - At this point we know that all the keys and'
nl|'\n'
comment|'# values are valid and we can iterate and update them all in one'
nl|'\n'
comment|'# shot without having to worry about rolling back etc as we have done'
nl|'\n'
comment|'# the validation up front in the 2 loops above.'
nl|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'valid_quotas'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'objects'
op|'.'
name|'Quotas'
op|'.'
name|'create_limit'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'key'
op|','
name|'value'
op|','
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
name|'objects'
op|'.'
name|'Quotas'
op|'.'
name|'update_limit'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'key'
op|','
name|'value'
op|','
name|'user_id'
op|'='
name|'user_id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'values'
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
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_format_quota_set'
op|'('
name|'None'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|defaults
dedent|''
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
name|'values'
op|'='
name|'QUOTAS'
op|'.'
name|'get_defaults'
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
name|'values'
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
name|'if'
name|'user_id'
name|'and'
name|'not'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-user-quotas'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
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
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0'
nl|'\n'
comment|'# because this version has to be stable even if it means that'
nl|'\n'
comment|'# only admins can call this method while the policy could be'
nl|'\n'
comment|'# changed.'
nl|'\n'
name|'nova'
op|'.'
name|'context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'user_id'
op|':'
newline|'\n'
indent|'                    '
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
indent|'                    '
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
name|'Forbidden'
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
string|'"2011-08-08T00:00:00Z"'
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