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
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'six'
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
name|'from'
name|'webob'
name|'import'
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
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-simple-tenant-usage"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_strtime
name|'def'
name|'parse_strtime'
op|'('
name|'dstr'
op|','
name|'fmt'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'dstr'
op|','
name|'fmt'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'ValueError'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidStrTime'
op|'('
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsageController
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsageController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_hours_for
indent|'    '
name|'def'
name|'_hours_for'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'period_start'
op|','
name|'period_stop'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'launched_at'
op|'='
name|'instance'
op|'.'
name|'launched_at'
newline|'\n'
name|'terminated_at'
op|'='
name|'instance'
op|'.'
name|'terminated_at'
newline|'\n'
name|'if'
name|'terminated_at'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'terminated_at'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mriedem): Instance object DateTime fields are'
nl|'\n'
comment|'# timezone-aware so convert using isotime.'
nl|'\n'
indent|'                '
name|'terminated_at'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'terminated_at'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'launched_at'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'launched_at'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'launched_at'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'launched_at'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'terminated_at'
name|'and'
name|'terminated_at'
op|'<'
name|'period_start'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
comment|'# nothing if it started after the usage report ended'
nl|'\n'
dedent|''
name|'if'
name|'launched_at'
name|'and'
name|'launched_at'
op|'>'
name|'period_stop'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'if'
name|'launched_at'
op|':'
newline|'\n'
comment|"# if instance launched after period_started, don't charge for first"
nl|'\n'
indent|'            '
name|'start'
op|'='
name|'max'
op|'('
name|'launched_at'
op|','
name|'period_start'
op|')'
newline|'\n'
name|'if'
name|'terminated_at'
op|':'
newline|'\n'
comment|"# if instance stopped before period_stop, don't charge after"
nl|'\n'
indent|'                '
name|'stop'
op|'='
name|'min'
op|'('
name|'period_stop'
op|','
name|'terminated_at'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# instance is still running, so charge them up to current time'
nl|'\n'
indent|'                '
name|'stop'
op|'='
name|'period_stop'
newline|'\n'
dedent|''
name|'dt'
op|'='
name|'stop'
op|'-'
name|'start'
newline|'\n'
name|'seconds'
op|'='
op|'('
name|'dt'
op|'.'
name|'days'
op|'*'
number|'3600'
op|'*'
number|'24'
op|'+'
name|'dt'
op|'.'
name|'seconds'
op|'+'
nl|'\n'
name|'dt'
op|'.'
name|'microseconds'
op|'/'
number|'100000.0'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'seconds'
op|'/'
number|'3600.0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# instance hasn't launched, so no charge"
nl|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor
dedent|''
dedent|''
name|'def'
name|'_get_flavor'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'flavors_cache'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get flavor information from the instance object,\n        allowing a fallback to lookup by-id for deleted instances only.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance'
op|'.'
name|'get_flavor'
op|'('
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
name|'if'
name|'not'
name|'instance'
op|'.'
name|'deleted'
op|':'
newline|'\n'
comment|'# Only support the fallback mechanism for deleted instances'
nl|'\n'
comment|'# that would have been skipped by migration #153'
nl|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'flavor_type'
op|'='
name|'instance'
op|'.'
name|'instance_type_id'
newline|'\n'
name|'if'
name|'flavor_type'
name|'in'
name|'flavors_cache'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'flavors_cache'
op|'['
name|'flavor_type'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor_ref'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'flavor_type'
op|')'
newline|'\n'
name|'flavors_cache'
op|'['
name|'flavor_type'
op|']'
op|'='
name|'flavor_ref'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
op|':'
newline|'\n'
comment|"# can't bill if there is no flavor"
nl|'\n'
indent|'            '
name|'flavor_ref'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'flavor_ref'
newline|'\n'
nl|'\n'
DECL|member|_tenant_usages_for_period
dedent|''
name|'def'
name|'_tenant_usages_for_period'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
name|'tenant_id'
op|'='
name|'None'
op|','
name|'detailed'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'instances'
op|'='
name|'objects'
op|'.'
name|'InstanceList'
op|'.'
name|'get_active_by_window_joined'
op|'('
nl|'\n'
name|'context'
op|','
name|'period_start'
op|','
name|'period_stop'
op|','
name|'tenant_id'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
op|'['
string|"'flavor'"
op|']'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'flavors'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'info'
op|'['
string|"'hours'"
op|']'
op|'='
name|'self'
op|'.'
name|'_hours_for'
op|'('
name|'instance'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'_get_flavor'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'flavors'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'flavor'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'flavor'"
op|']'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'flavor'"
op|']'
op|'='
name|'flavor'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'.'
name|'uuid'
newline|'\n'
name|'info'
op|'['
string|"'name'"
op|']'
op|'='
name|'instance'
op|'.'
name|'display_name'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'instance'
op|'.'
name|'memory_mb'
newline|'\n'
name|'info'
op|'['
string|"'local_gb'"
op|']'
op|'='
name|'instance'
op|'.'
name|'root_gb'
op|'+'
name|'instance'
op|'.'
name|'ephemeral_gb'
newline|'\n'
name|'info'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'instance'
op|'.'
name|'vcpus'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'instance'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
comment|'# NOTE(mriedem): We need to normalize the start/end times back'
nl|'\n'
comment|"# to timezone-naive so the response doesn't change after the"
nl|'\n'
comment|'# conversion to objects.'
nl|'\n'
name|'info'
op|'['
string|"'started_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
name|'instance'
op|'.'
name|'launched_at'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|'='
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
name|'instance'
op|'.'
name|'terminated_at'
op|')'
name|'if'
nl|'\n'
name|'instance'
op|'.'
name|'terminated_at'
name|'else'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'state'"
op|']'
op|'='
string|"'terminated'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'info'
op|'['
string|"'state'"
op|']'
op|'='
name|'instance'
op|'.'
name|'vm_state'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'state'"
op|']'
op|'=='
string|"'terminated'"
op|':'
newline|'\n'
indent|'                '
name|'delta'
op|'='
name|'info'
op|'['
string|"'ended_at'"
op|']'
op|'-'
name|'info'
op|'['
string|"'started_at'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'delta'
op|'='
name|'now'
op|'-'
name|'info'
op|'['
string|"'started_at'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'info'
op|'['
string|"'uptime'"
op|']'
op|'='
name|'delta'
op|'.'
name|'days'
op|'*'
number|'24'
op|'*'
number|'3600'
op|'+'
name|'delta'
op|'.'
name|'seconds'
newline|'\n'
nl|'\n'
name|'if'
name|'info'
op|'['
string|"'tenant_id'"
op|']'
name|'not'
name|'in'
name|'rval'
op|':'
newline|'\n'
indent|'                '
name|'summary'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'summary'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'info'
op|'['
string|"'tenant_id'"
op|']'
newline|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'                    '
name|'summary'
op|'['
string|"'server_usages'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'summary'
op|'['
string|"'total_local_gb_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_vcpus_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_memory_mb_usage'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'total_hours'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'summary'
op|'['
string|"'start'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
name|'period_start'
op|')'
newline|'\n'
name|'summary'
op|'['
string|"'stop'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
name|'period_stop'
op|')'
newline|'\n'
name|'rval'
op|'['
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|']'
op|'='
name|'summary'
newline|'\n'
nl|'\n'
dedent|''
name|'summary'
op|'='
name|'rval'
op|'['
name|'info'
op|'['
string|"'tenant_id'"
op|']'
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_local_gb_usage'"
op|']'
op|'+='
name|'info'
op|'['
string|"'local_gb'"
op|']'
op|'*'
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_vcpus_usage'"
op|']'
op|'+='
name|'info'
op|'['
string|"'vcpus'"
op|']'
op|'*'
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'summary'
op|'['
string|"'total_memory_mb_usage'"
op|']'
op|'+='
op|'('
name|'info'
op|'['
string|"'memory_mb'"
op|']'
op|'*'
nl|'\n'
name|'info'
op|'['
string|"'hours'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'summary'
op|'['
string|"'total_hours'"
op|']'
op|'+='
name|'info'
op|'['
string|"'hours'"
op|']'
newline|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'                '
name|'summary'
op|'['
string|"'server_usages'"
op|']'
op|'.'
name|'append'
op|'('
name|'info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'rval'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse_datetime
dedent|''
name|'def'
name|'_parse_datetime'
op|'('
name|'self'
op|','
name|'dtstr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'dtstr'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'dtstr'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'dtstr'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'fmt'
name|'in'
op|'['
string|'"%Y-%m-%dT%H:%M:%S"'
op|','
nl|'\n'
string|'"%Y-%m-%dT%H:%M:%S.%f"'
op|','
nl|'\n'
string|'"%Y-%m-%d %H:%M:%S.%f"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'='
name|'parse_strtime'
op|'('
name|'dtstr'
op|','
name|'fmt'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidStrTime'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Datetime is in invalid format"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidStrTime'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mriedem): Instance object DateTime fields are timezone-aware'
nl|'\n'
comment|'# so we have to force UTC timezone for comparing this datetime against'
nl|'\n'
comment|'# instance object fields and still maintain backwards compatibility'
nl|'\n'
comment|'# in the API.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'value'
op|'.'
name|'utcoffset'
op|'('
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'value'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|_get_datetime_range
dedent|''
name|'def'
name|'_get_datetime_range'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'qs'
op|'='
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
newline|'\n'
name|'env'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'qs'
op|')'
newline|'\n'
comment|'# NOTE(lzyeval): env.get() always returns a list'
nl|'\n'
name|'period_start'
op|'='
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'start'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'period_stop'
op|'='
name|'self'
op|'.'
name|'_parse_datetime'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'end'"
op|','
op|'['
name|'None'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'period_start'
op|'<'
name|'period_stop'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid start time. The start time cannot occur after "'
nl|'\n'
string|'"the end time."'
op|')'
newline|'\n'
name|'raise'
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
name|'detailed'
op|'='
name|'env'
op|'.'
name|'get'
op|'('
string|"'detailed'"
op|','
op|'['
string|"'0'"
op|']'
op|')'
op|'['
number|'0'
op|']'
op|'=='
string|"'1'"
newline|'\n'
name|'return'
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'detailed'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""Retrieve tenant_usage for all tenants."""'
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
nl|'\n'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'list'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'detailed'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_datetime_range'
op|'('
nl|'\n'
name|'req'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidStrTime'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
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
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'period_stop'
op|'>'
name|'now'
op|':'
newline|'\n'
indent|'            '
name|'period_stop'
op|'='
name|'now'
newline|'\n'
dedent|''
name|'usages'
op|'='
name|'self'
op|'.'
name|'_tenant_usages_for_period'
op|'('
name|'context'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'detailed'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'tenant_usages'"
op|':'
name|'usages'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
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
string|'"""Retrieve tenant_usage for a specified tenant."""'
newline|'\n'
name|'tenant_id'
op|'='
name|'id'
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
nl|'\n'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'show'"
op|','
name|'target'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'tenant_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'period_start'
op|','
name|'period_stop'
op|','
name|'ignore'
op|')'
op|'='
name|'self'
op|'.'
name|'_get_datetime_range'
op|'('
nl|'\n'
name|'req'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidStrTime'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
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
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'isoformat'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'period_stop'
op|'>'
name|'now'
op|':'
newline|'\n'
indent|'            '
name|'period_stop'
op|'='
name|'now'
newline|'\n'
dedent|''
name|'usage'
op|'='
name|'self'
op|'.'
name|'_tenant_usages_for_period'
op|'('
name|'context'
op|','
nl|'\n'
name|'period_start'
op|','
nl|'\n'
name|'period_stop'
op|','
nl|'\n'
name|'tenant_id'
op|'='
name|'tenant_id'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'usage'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'usage'
op|'='
name|'list'
op|'('
name|'usage'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'usage'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'tenant_usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleTenantUsage
dedent|''
dedent|''
name|'class'
name|'SimpleTenantUsage'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simple tenant usage extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"SimpleTenantUsage"'
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
name|'SimpleTenantUsageController'
op|'('
op|')'
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
