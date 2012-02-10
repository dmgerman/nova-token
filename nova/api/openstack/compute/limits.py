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
string|'"""\nModule dedicated functions/classes dealing with rate limiting requests.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'math'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'limits'
name|'as'
name|'limits_views'
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
name|'from'
name|'nova'
name|'import'
name|'wsgi'
name|'as'
name|'base_wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Convenience constants for the limits dictionary passed to Limiter().'
nl|'\n'
DECL|variable|PER_SECOND
name|'PER_SECOND'
op|'='
number|'1'
newline|'\n'
DECL|variable|PER_MINUTE
name|'PER_MINUTE'
op|'='
number|'60'
newline|'\n'
DECL|variable|PER_HOUR
name|'PER_HOUR'
op|'='
number|'60'
op|'*'
number|'60'
newline|'\n'
DECL|variable|PER_DAY
name|'PER_DAY'
op|'='
number|'60'
op|'*'
number|'60'
op|'*'
number|'24'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|limits_nsmap
name|'limits_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsTemplate
name|'class'
name|'LimitsTemplate'
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
string|"'limits'"
op|','
name|'selector'
op|'='
string|"'limits'"
op|')'
newline|'\n'
nl|'\n'
name|'rates'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'rates'"
op|')'
newline|'\n'
name|'rate'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'rates'
op|','
string|"'rate'"
op|','
name|'selector'
op|'='
string|"'rate'"
op|')'
newline|'\n'
name|'rate'
op|'.'
name|'set'
op|'('
string|"'uri'"
op|','
string|"'uri'"
op|')'
newline|'\n'
name|'rate'
op|'.'
name|'set'
op|'('
string|"'regex'"
op|','
string|"'regex'"
op|')'
newline|'\n'
name|'limit'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'rate'
op|','
string|"'limit'"
op|','
name|'selector'
op|'='
string|"'limit'"
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'value'"
op|','
string|"'value'"
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'verb'"
op|','
string|"'verb'"
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'remaining'"
op|','
string|"'remaining'"
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'unit'"
op|','
string|"'unit'"
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'next-available'"
op|','
string|"'next-available'"
op|')'
newline|'\n'
nl|'\n'
name|'absolute'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'absolute'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'absolute'"
op|')'
newline|'\n'
name|'limit'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'absolute'
op|','
string|"'limit'"
op|','
nl|'\n'
name|'selector'
op|'='
name|'xmlutil'
op|'.'
name|'get_items'
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'name'"
op|','
number|'0'
op|')'
newline|'\n'
name|'limit'
op|'.'
name|'set'
op|'('
string|"'value'"
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'limits_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsController
dedent|''
dedent|''
name|'class'
name|'LimitsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Controller for accessing limits in the OpenStack API.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'LimitsTemplate'
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
string|'"""\n        Return all global and rate limit information.\n        """'
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
name|'abs_limits'
op|'='
name|'quota'
op|'.'
name|'get_project_quotas'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'rate_limits'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|'"nova.limits"'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'builder'
op|'.'
name|'build'
op|'('
name|'rate_limits'
op|','
name|'abs_limits'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_view_builder
dedent|''
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'limits_views'
op|'.'
name|'ViewBuilder'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'LimitsController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Limit
dedent|''
name|'class'
name|'Limit'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Stores information about a limit for HTTP requests.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|UNITS
name|'UNITS'
op|'='
op|'{'
nl|'\n'
number|'1'
op|':'
string|'"SECOND"'
op|','
nl|'\n'
number|'60'
op|':'
string|'"MINUTE"'
op|','
nl|'\n'
number|'60'
op|'*'
number|'60'
op|':'
string|'"HOUR"'
op|','
nl|'\n'
number|'60'
op|'*'
number|'60'
op|'*'
number|'24'
op|':'
string|'"DAY"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|UNIT_MAP
name|'UNIT_MAP'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'v'
op|','
name|'k'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'UNITS'
op|'.'
name|'items'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'uri'
op|','
name|'regex'
op|','
name|'value'
op|','
name|'unit'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize a new `Limit`.\n\n        @param verb: HTTP verb (POST, PUT, etc.)\n        @param uri: Human-readable URI\n        @param regex: Regular expression format for this limit\n        @param value: Integer number of requests which can be made\n        @param unit: Unit of measure for the value parameter\n        """'
newline|'\n'
name|'self'
op|'.'
name|'verb'
op|'='
name|'verb'
newline|'\n'
name|'self'
op|'.'
name|'uri'
op|'='
name|'uri'
newline|'\n'
name|'self'
op|'.'
name|'regex'
op|'='
name|'regex'
newline|'\n'
name|'self'
op|'.'
name|'value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unit'
op|'='
name|'unit'
newline|'\n'
name|'self'
op|'.'
name|'unit_string'
op|'='
name|'self'
op|'.'
name|'display_unit'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remaining'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'value'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
string|'"Limit value must be > 0"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'last_request'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'next_request'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'water_level'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'capacity'
op|'='
name|'self'
op|'.'
name|'unit'
newline|'\n'
name|'self'
op|'.'
name|'request_value'
op|'='
name|'float'
op|'('
name|'self'
op|'.'
name|'capacity'
op|')'
op|'/'
name|'float'
op|'('
name|'self'
op|'.'
name|'value'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'error_message'
op|'='
name|'_'
op|'('
string|'"Only %(value)s %(verb)s request(s) can be "'
nl|'\n'
string|'"made to %(uri)s every %(unit_string)s."'
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Represents a call to this limit from a relevant request.\n\n        @param verb: string http verb (POST, GET, etc.)\n        @param url: string URL\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'verb'
op|'!='
name|'verb'
name|'or'
name|'not'
name|'re'
op|'.'
name|'match'
op|'('
name|'self'
op|'.'
name|'regex'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'self'
op|'.'
name|'_get_time'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'last_request'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'last_request'
op|'='
name|'now'
newline|'\n'
nl|'\n'
dedent|''
name|'leak_value'
op|'='
name|'now'
op|'-'
name|'self'
op|'.'
name|'last_request'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'water_level'
op|'-='
name|'leak_value'
newline|'\n'
name|'self'
op|'.'
name|'water_level'
op|'='
name|'max'
op|'('
name|'self'
op|'.'
name|'water_level'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'water_level'
op|'+='
name|'self'
op|'.'
name|'request_value'
newline|'\n'
nl|'\n'
name|'difference'
op|'='
name|'self'
op|'.'
name|'water_level'
op|'-'
name|'self'
op|'.'
name|'capacity'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'last_request'
op|'='
name|'now'
newline|'\n'
nl|'\n'
name|'if'
name|'difference'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'water_level'
op|'-='
name|'self'
op|'.'
name|'request_value'
newline|'\n'
name|'self'
op|'.'
name|'next_request'
op|'='
name|'now'
op|'+'
name|'difference'
newline|'\n'
name|'return'
name|'difference'
newline|'\n'
nl|'\n'
dedent|''
name|'cap'
op|'='
name|'self'
op|'.'
name|'capacity'
newline|'\n'
name|'water'
op|'='
name|'self'
op|'.'
name|'water_level'
newline|'\n'
name|'val'
op|'='
name|'self'
op|'.'
name|'value'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'remaining'
op|'='
name|'math'
op|'.'
name|'floor'
op|'('
op|'('
op|'('
name|'cap'
op|'-'
name|'water'
op|')'
op|'/'
name|'cap'
op|')'
op|'*'
name|'val'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'next_request'
op|'='
name|'now'
newline|'\n'
nl|'\n'
DECL|member|_get_time
dedent|''
name|'def'
name|'_get_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve the current time. Broken out for testability."""'
newline|'\n'
name|'return'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|display_unit
dedent|''
name|'def'
name|'display_unit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Display the string name of the unit."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'UNITS'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'unit'
op|','
string|'"UNKNOWN"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|display
dedent|''
name|'def'
name|'display'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a useful representation of this class."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"verb"'
op|':'
name|'self'
op|'.'
name|'verb'
op|','
nl|'\n'
string|'"URI"'
op|':'
name|'self'
op|'.'
name|'uri'
op|','
nl|'\n'
string|'"regex"'
op|':'
name|'self'
op|'.'
name|'regex'
op|','
nl|'\n'
string|'"value"'
op|':'
name|'self'
op|'.'
name|'value'
op|','
nl|'\n'
string|'"remaining"'
op|':'
name|'int'
op|'('
name|'self'
op|'.'
name|'remaining'
op|')'
op|','
nl|'\n'
string|'"unit"'
op|':'
name|'self'
op|'.'
name|'display_unit'
op|'('
op|')'
op|','
nl|'\n'
string|'"resetTime"'
op|':'
name|'int'
op|'('
name|'self'
op|'.'
name|'next_request'
name|'or'
name|'self'
op|'.'
name|'_get_time'
op|'('
op|')'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# "Limit" format is a dictionary with the HTTP verb, human-readable URI,'
nl|'\n'
comment|'# a regular-expression to match, value and unit of measure (PER_DAY, etc.)'
nl|'\n'
nl|'\n'
DECL|variable|DEFAULT_LIMITS
dedent|''
dedent|''
name|'DEFAULT_LIMITS'
op|'='
op|'['
nl|'\n'
name|'Limit'
op|'('
string|'"POST"'
op|','
string|'"*"'
op|','
string|'".*"'
op|','
number|'10'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"POST"'
op|','
string|'"*/servers"'
op|','
string|'"^/servers"'
op|','
number|'50'
op|','
name|'PER_DAY'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"PUT"'
op|','
string|'"*"'
op|','
string|'".*"'
op|','
number|'10'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"GET"'
op|','
string|'"*changes-since*"'
op|','
string|'".*changes-since.*"'
op|','
number|'3'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"DELETE"'
op|','
string|'"*"'
op|','
string|'".*"'
op|','
number|'100'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RateLimitingMiddleware
name|'class'
name|'RateLimitingMiddleware'
op|'('
name|'base_wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Rate-limits requests passing through this middleware. All limit information\n    is stored in memory for this implementation.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'limits'
op|'='
name|'None'
op|','
name|'limiter'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize new `RateLimitingMiddleware`, which wraps the given WSGI\n        application and sets up the given limits.\n\n        @param application: WSGI application to wrap\n        @param limits: String describing limits\n        @param limiter: String identifying class for representing limits\n\n        Other parameters are passed to the constructor for the limiter.\n        """'
newline|'\n'
name|'base_wsgi'
op|'.'
name|'Middleware'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
newline|'\n'
nl|'\n'
comment|'# Select the limiter class'
nl|'\n'
name|'if'
name|'limiter'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'limiter'
op|'='
name|'Limiter'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'limiter'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'limiter'
op|')'
newline|'\n'
nl|'\n'
comment|'# Parse the limits, if any are provided'
nl|'\n'
dedent|''
name|'if'
name|'limits'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'limits'
op|'='
name|'limiter'
op|'.'
name|'parse_limits'
op|'('
name|'limits'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_limiter'
op|'='
name|'limiter'
op|'('
name|'limits'
name|'or'
name|'DEFAULT_LIMITS'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"""\n        Represents a single call through this middleware. We should record the\n        request if we have a limit relevant to it. If no limit is relevant to\n        the request, ignore it.\n\n        If the request should be rate limited, return a fault telling the user\n        they are over the limit and need to retry later.\n        """'
newline|'\n'
name|'verb'
op|'='
name|'req'
op|'.'
name|'method'
newline|'\n'
name|'url'
op|'='
name|'req'
op|'.'
name|'url'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|'"nova.context"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'username'
op|'='
name|'context'
op|'.'
name|'user_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'username'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'delay'
op|','
name|'error'
op|'='
name|'self'
op|'.'
name|'_limiter'
op|'.'
name|'check_for_delay'
op|'('
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"This request was rate-limited."'
op|')'
newline|'\n'
name|'retry'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'delay'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'OverLimitFault'
op|'('
name|'msg'
op|','
name|'error'
op|','
name|'retry'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.limits"'
op|']'
op|'='
name|'self'
op|'.'
name|'_limiter'
op|'.'
name|'get_limits'
op|'('
name|'username'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Limiter
dedent|''
dedent|''
name|'class'
name|'Limiter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Rate-limit checking class which handles limits in memory.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'limits'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize the new `Limiter`.\n\n        @param limits: List of `Limit` objects\n        """'
newline|'\n'
name|'self'
op|'.'
name|'limits'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'limits'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'levels'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'lambda'
op|':'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'limits'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Pick up any per-user limit information'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'kwargs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'user:'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'username'
op|'='
name|'key'
op|'['
number|'5'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'levels'
op|'['
name|'username'
op|']'
op|'='
name|'self'
op|'.'
name|'parse_limits'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_limits
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_limits'
op|'('
name|'self'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the limits for a given user.\n        """'
newline|'\n'
name|'return'
op|'['
name|'limit'
op|'.'
name|'display'
op|'('
op|')'
name|'for'
name|'limit'
name|'in'
name|'self'
op|'.'
name|'levels'
op|'['
name|'username'
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|check_for_delay
dedent|''
name|'def'
name|'check_for_delay'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check the given verb/user/user triplet for limit.\n\n        @return: Tuple of delay (in seconds) and error message (or None, None)\n        """'
newline|'\n'
name|'delays'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'limit'
name|'in'
name|'self'
op|'.'
name|'levels'
op|'['
name|'username'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'delay'
op|'='
name|'limit'
op|'('
name|'verb'
op|','
name|'url'
op|')'
newline|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
indent|'                '
name|'delays'
op|'.'
name|'append'
op|'('
op|'('
name|'delay'
op|','
name|'limit'
op|'.'
name|'error_message'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'delays'
op|':'
newline|'\n'
indent|'            '
name|'delays'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'delays'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
comment|'# Note: This method gets called before the class is instantiated,'
nl|'\n'
comment|'# so this must be either a static method or a class method.  It is'
nl|'\n'
comment|'# used to develop a list of limits to feed to the constructor.  We'
nl|'\n'
comment|'# put this in the class so that subclasses can override the'
nl|'\n'
comment|'# default limit parsing.'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|parse_limits
name|'def'
name|'parse_limits'
op|'('
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Convert a string into a list of Limit instances.  This\n        implementation expects a semicolon-separated sequence of\n        parenthesized groups, where each group contains a\n        comma-separated sequence consisting of HTTP method,\n        user-readable URI, a URI reg-exp, an integer number of\n        requests which can be made, and a unit of measure.  Valid\n        values for the latter are "SECOND", "MINUTE", "HOUR", and\n        "DAY".\n\n        @return: List of Limit instances.\n        """'
newline|'\n'
nl|'\n'
comment|'# Handle empty limit strings'
nl|'\n'
name|'limits'
op|'='
name|'limits'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'limits'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Split up the limits by semicolon'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'group'
name|'in'
name|'limits'
op|'.'
name|'split'
op|'('
string|"';'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
name|'group'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'group'
op|'['
op|':'
number|'1'
op|']'
op|'!='
string|"'('"
name|'or'
name|'group'
op|'['
op|'-'
number|'1'
op|':'
op|']'
op|'!='
string|"')'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
string|'"Limit rules must be surrounded by "'
nl|'\n'
string|'"parentheses"'
op|')'
newline|'\n'
dedent|''
name|'group'
op|'='
name|'group'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
comment|'# Extract the Limit arguments'
nl|'\n'
name|'args'
op|'='
op|'['
name|'a'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'a'
name|'in'
name|'group'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'!='
number|'5'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
string|'"Limit rules must contain the following "'
nl|'\n'
string|'"arguments: verb, uri, regex, value, unit"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Pull out the arguments'
nl|'\n'
dedent|''
name|'verb'
op|','
name|'uri'
op|','
name|'regex'
op|','
name|'value'
op|','
name|'unit'
op|'='
name|'args'
newline|'\n'
nl|'\n'
comment|'# Upper-case the verb'
nl|'\n'
name|'verb'
op|'='
name|'verb'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Convert value--raises ValueError if it's not integer"
nl|'\n'
name|'value'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|'# Convert unit'
nl|'\n'
name|'unit'
op|'='
name|'unit'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'if'
name|'unit'
name|'not'
name|'in'
name|'Limit'
op|'.'
name|'UNIT_MAP'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
string|'"Invalid units specified"'
op|')'
newline|'\n'
dedent|''
name|'unit'
op|'='
name|'Limit'
op|'.'
name|'UNIT_MAP'
op|'['
name|'unit'
op|']'
newline|'\n'
nl|'\n'
comment|'# Build a limit'
nl|'\n'
name|'result'
op|'.'
name|'append'
op|'('
name|'Limit'
op|'('
name|'verb'
op|','
name|'uri'
op|','
name|'regex'
op|','
name|'value'
op|','
name|'unit'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WsgiLimiter
dedent|''
dedent|''
name|'class'
name|'WsgiLimiter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Rate-limit checking from a WSGI application. Uses an in-memory `Limiter`.\n\n    To use:\n        POST /<username> with JSON data such as:\n        {\n            "verb" : GET,\n            "path" : "/servers"\n        }\n\n    and receive a 204 No Content, or a 403 Forbidden with an X-Wait-Seconds\n    header containing the number of seconds to wait before the action would\n    succeed.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'limits'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize the new `WsgiLimiter`.\n\n        @param limits: List of `Limit` objects\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_limiter'
op|'='
name|'Limiter'
op|'('
name|'limits'
name|'or'
name|'DEFAULT_LIMITS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Handles a call to this application. Returns 204 if the request is\n        acceptable to the limiter, else a 403 is returned with a relevant\n        header indicating when the request *will* succeed.\n        """'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'method'
op|'!='
string|'"POST"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPMethodNotAllowed'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
name|'dict'
op|'('
name|'json'
op|'.'
name|'loads'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'username'
op|'='
name|'request'
op|'.'
name|'path_info_pop'
op|'('
op|')'
newline|'\n'
name|'verb'
op|'='
name|'info'
op|'.'
name|'get'
op|'('
string|'"verb"'
op|')'
newline|'\n'
name|'path'
op|'='
name|'info'
op|'.'
name|'get'
op|'('
string|'"path"'
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|','
name|'error'
op|'='
name|'self'
op|'.'
name|'_limiter'
op|'.'
name|'check_for_delay'
op|'('
name|'verb'
op|','
name|'path'
op|','
name|'username'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'='
op|'{'
string|'"X-Wait-Seconds"'
op|':'
string|'"%.2f"'
op|'%'
name|'delay'
op|'}'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'headers'
op|'='
name|'headers'
op|','
name|'explanation'
op|'='
name|'error'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNoContent'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WsgiLimiterProxy
dedent|''
dedent|''
dedent|''
name|'class'
name|'WsgiLimiterProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Rate-limit requests based on answers from a remote source.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'limiter_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize the new `WsgiLimiterProxy`.\n\n        @param limiter_address: IP/port combination of where to request limit\n        """'
newline|'\n'
name|'self'
op|'.'
name|'limiter_address'
op|'='
name|'limiter_address'
newline|'\n'
nl|'\n'
DECL|member|check_for_delay
dedent|''
name|'def'
name|'check_for_delay'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'path'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|'"verb"'
op|':'
name|'verb'
op|','
string|'"path"'
op|':'
name|'path'
op|'}'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|'"Content-Type"'
op|':'
string|'"application/json"'
op|'}'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'self'
op|'.'
name|'limiter_address'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'username'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'.'
name|'request'
op|'('
string|'"POST"'
op|','
string|'"/%s"'
op|'%'
op|'('
name|'username'
op|')'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'.'
name|'request'
op|'('
string|'"POST"'
op|','
string|'"/"'
op|','
name|'body'
op|','
name|'headers'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'resp'
op|'='
name|'conn'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
number|'200'
op|'>='
name|'resp'
op|'.'
name|'status'
op|'<'
number|'300'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'resp'
op|'.'
name|'getheader'
op|'('
string|'"X-Wait-Seconds"'
op|')'
op|','
name|'resp'
op|'.'
name|'read'
op|'('
op|')'
name|'or'
name|'None'
newline|'\n'
nl|'\n'
comment|'# Note: This method gets called before the class is instantiated,'
nl|'\n'
comment|'# so this must be either a static method or a class method.  It is'
nl|'\n'
comment|'# used to develop a list of limits to feed to the constructor.'
nl|'\n'
comment|'# This implementation returns an empty list, since all limit'
nl|'\n'
comment|'# decisions are made by a remote server.'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|parse_limits
name|'def'
name|'parse_limits'
op|'('
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ignore a limits string--simply doesn\'t apply for the limit\n        proxy.\n\n        @return: Empty list.\n        """'
newline|'\n'
nl|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
