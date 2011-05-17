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
comment|'#    under the License.import datetime'
nl|'\n'
nl|'\n'
string|'"""\nModule dedicated functions/classes dealing with rate limiting requests.\n"""'
newline|'\n'
nl|'\n'
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
name|'import'
name|'urllib'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'collections'
name|'import'
name|'defaultdict'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
op|'.'
name|'dec'
name|'import'
name|'wsgify'
newline|'\n'
nl|'\n'
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
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
name|'import'
name|'limits'
name|'as'
name|'limits_views'
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
comment|'#TODO remove when mark catches up'
nl|'\n'
DECL|variable|TEST_ABSOLUTE_LIMITS
name|'TEST_ABSOLUTE_LIMITS'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsController
name|'class'
name|'LimitsController'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Controller for accessing limits in the OpenStack API.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|'"application/xml"'
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"limit"'
op|':'
op|'['
string|'"verb"'
op|','
string|'"URI"'
op|','
string|'"uri"'
op|','
string|'"regex"'
op|','
string|'"value"'
op|','
string|'"unit"'
op|','
nl|'\n'
string|'"resetTime"'
op|','
string|'"next-available"'
op|','
string|'"remaining"'
op|','
string|'"name"'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"plurals"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
string|'"limit"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
comment|'# TODO(alex.meade) make this work'
nl|'\n'
comment|'#project_quota = quota.get_project_quota(...)'
nl|'\n'
comment|'#abs_limits = project_quota.limits'
nl|'\n'
comment|'#TODO remove when mark catches up'
nl|'\n'
name|'abs_limits'
op|'='
name|'TEST_ABSOLUTE_LIMITS'
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsControllerV10
dedent|''
dedent|''
name|'class'
name|'LimitsControllerV10'
op|'('
name|'LimitsController'
op|')'
op|':'
newline|'\n'
DECL|member|_get_view_builder
indent|'    '
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
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsControllerV11
dedent|''
dedent|''
name|'class'
name|'LimitsControllerV11'
op|'('
name|'LimitsController'
op|')'
op|':'
newline|'\n'
DECL|member|_get_view_builder
indent|'    '
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
name|'ViewBuilderV11'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Limit
dedent|''
dedent|''
name|'class'
name|'Limit'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Stores information about a limit for HTTP requets.\n    """'
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
string|'"made to %(uri)s every %(unit_string)s."'
op|'%'
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
name|'wsgi'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize new `RateLimitingMiddleware`, which wraps the given WSGI\n        application and sets up the given limits.\n\n        @param application: WSGI application to wrap\n        @param limits: List of dictionaries describing limits\n        """'
newline|'\n'
name|'wsgi'
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
name|'faults'
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
DECL|member|get_limits
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
dedent|''
dedent|''
endmarker|''
end_unit
