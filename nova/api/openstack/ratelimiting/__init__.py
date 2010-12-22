begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""Rate limiting of arbitrary actions."""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
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
name|'faults'
newline|'\n'
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
string|'"""Rate limit incoming requests according to the OpenStack rate limits."""'
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
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a rate limiting middleware that wraps the given application.\n\n        By default, rate counters are stored in memory.  If service_host is\n        specified, the middleware instead relies on the ratelimiting.WSGIApp\n        at the given host+port to keep rate counters.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'service_host'
op|':'
newline|'\n'
comment|'#TODO(gundlach): These limits were based on limitations of Cloud'
nl|'\n'
comment|'#Servers.  We should revisit them in Nova.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'limiter'
op|'='
name|'Limiter'
op|'('
name|'limits'
op|'='
op|'{'
nl|'\n'
string|"'DELETE'"
op|':'
op|'('
number|'100'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'PUT'"
op|':'
op|'('
number|'10'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'POST'"
op|':'
op|'('
number|'10'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'POST servers'"
op|':'
op|'('
number|'50'
op|','
name|'PER_DAY'
op|')'
op|','
nl|'\n'
string|"'GET changes-since'"
op|':'
op|'('
number|'3'
op|','
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'limiter'
op|'='
name|'WSGIAppProxy'
op|'('
name|'service_host'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'RateLimitingMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
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
string|'"""Rate limit the request.\n\n        If the request should be rate limited, return a 413 status with a\n        Retry-After header giving the time when the request would succeed.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'limited_request'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
nl|'\n'
DECL|member|limited_request
dedent|''
name|'def'
name|'limited_request'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rate limit the request.\n\n        If the request should be rate limited, return a 413 status with a\n        Retry-After header giving the time when the request would succeed.\n        """'
newline|'\n'
name|'action_name'
op|'='
name|'self'
op|'.'
name|'get_action_name'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'action_name'
op|':'
newline|'\n'
comment|'# Not rate limited'
nl|'\n'
indent|'            '
name|'return'
name|'application'
newline|'\n'
dedent|''
name|'delay'
op|'='
name|'self'
op|'.'
name|'get_delay'
op|'('
name|'action_name'
op|','
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
comment|'# TODO(gundlach): Get the retry-after format correct.'
nl|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
nl|'\n'
name|'explanation'
op|'='
op|'('
string|"'Too many requests.'"
op|')'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'delay'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'application'
newline|'\n'
nl|'\n'
DECL|member|get_delay
dedent|''
name|'def'
name|'get_delay'
op|'('
name|'self'
op|','
name|'action_name'
op|','
name|'username'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the delay for the given action and username, or None if\n        the action would not be rate limited.\n        """'
newline|'\n'
name|'if'
name|'action_name'
op|'=='
string|"'POST servers'"
op|':'
newline|'\n'
comment|'# "POST servers" is a POST, so it counts against "POST" too.'
nl|'\n'
comment|'# Attempt the "POST" first, lest we are rate limited by "POST" but'
nl|'\n'
comment|'# use up a precious "POST servers" call.'
nl|'\n'
indent|'            '
name|'delay'
op|'='
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'perform'
op|'('
string|'"POST"'
op|','
name|'username'
op|'='
name|'username'
op|')'
newline|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'delay'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'perform'
op|'('
name|'action_name'
op|','
name|'username'
op|'='
name|'username'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_action_name
dedent|''
name|'def'
name|'get_action_name'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the action name for this request."""'
newline|'\n'
name|'if'
name|'req'
op|'.'
name|'method'
op|'=='
string|"'GET'"
name|'and'
string|"'changes-since'"
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'GET changes-since'"
newline|'\n'
dedent|''
name|'if'
name|'req'
op|'.'
name|'method'
op|'=='
string|"'POST'"
name|'and'
name|'req'
op|'.'
name|'path_info'
op|'.'
name|'startswith'
op|'('
string|"'/servers'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'POST servers'"
newline|'\n'
dedent|''
name|'if'
name|'req'
op|'.'
name|'method'
name|'in'
op|'['
string|"'PUT'"
op|','
string|"'POST'"
op|','
string|"'DELETE'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'req'
op|'.'
name|'method'
newline|'\n'
dedent|''
name|'return'
name|'None'
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
nl|'\n'
indent|'    '
string|'"""Class providing rate limiting of arbitrary actions."""'
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
string|'"""Create a rate limiter.\n\n        limits: a dict mapping from action name to a tuple.  The tuple contains\n        the number of times the action may be performed, and the time period\n        (in seconds) during which the number must not be exceeded for this\n        action.  Example: dict(reboot=(10, ratelimiting.PER_MINUTE)) would\n        allow 10 \'reboot\' actions per minute.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'limits'
op|'='
name|'limits'
newline|'\n'
name|'self'
op|'.'
name|'_levels'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|perform
dedent|''
name|'def'
name|'perform'
op|'('
name|'self'
op|','
name|'action_name'
op|','
name|'username'
op|'='
string|"'nobody'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attempt to perform an action by the given username.\n\n        action_name: the string name of the action to perform.  This must\n        be a key in the limits dict passed to the ctor.\n\n        username: an optional string name of the user performing the action.\n        Each user has her own set of rate limiting counters.  Defaults to\n        \'nobody\' (so that if you never specify a username when calling\n        perform(), a single set of counters will be used.)\n\n        Return None if the action may proceed.  If the action may not proceed\n        because it has been rate limited, return the float number of seconds\n        until the action would succeed.\n        """'
newline|'\n'
comment|'# Think of rate limiting as a bucket leaking water at 1cc/second.  The'
nl|'\n'
comment|'# bucket can hold as many ccs as there are seconds in the rate'
nl|'\n'
comment|'# limiting period (e.g. 3600 for per-hour ratelimits), and if you can'
nl|'\n'
comment|'# perform N actions in that time, each action fills the bucket by'
nl|'\n'
comment|'# 1/Nth of its volume.  You may only perform an action if the bucket'
nl|'\n'
comment|'# would not overflow.'
nl|'\n'
name|'now'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'username'
op|','
name|'action_name'
op|')'
newline|'\n'
name|'last_time_performed'
op|','
name|'water_level'
op|'='
name|'self'
op|'.'
name|'_levels'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'('
name|'now'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
comment|'# The bucket leaks 1cc/second.'
nl|'\n'
name|'water_level'
op|'-='
op|'('
name|'now'
op|'-'
name|'last_time_performed'
op|')'
newline|'\n'
name|'if'
name|'water_level'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'water_level'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'num_allowed_per_period'
op|','
name|'period_in_secs'
op|'='
name|'self'
op|'.'
name|'limits'
op|'['
name|'action_name'
op|']'
newline|'\n'
comment|"# Fill the bucket by 1/Nth its capacity, and hope it doesn't overflow."
nl|'\n'
name|'capacity'
op|'='
name|'period_in_secs'
newline|'\n'
name|'new_level'
op|'='
name|'water_level'
op|'+'
op|'('
name|'capacity'
op|'*'
number|'1.0'
op|'/'
name|'num_allowed_per_period'
op|')'
newline|'\n'
name|'if'
name|'new_level'
op|'>'
name|'capacity'
op|':'
newline|'\n'
comment|'# Delay this many seconds.'
nl|'\n'
indent|'            '
name|'return'
name|'new_level'
op|'-'
name|'capacity'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_levels'
op|'['
name|'key'
op|']'
op|'='
op|'('
name|'now'
op|','
name|'new_level'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# If one instance of this WSGIApps is unable to handle your load, put a'
nl|'\n'
comment|'# sharding app in front that shards by username to one of many backends.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|WSGIApp
dedent|''
dedent|''
name|'class'
name|'WSGIApp'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Application that tracks rate limits in memory.  Send requests to it of\n    this form:\n\n    POST /limiter/<username>/<urlencoded action>\n\n    and receive a 200 OK, or a 403 Forbidden with an X-Wait-Seconds header\n    containing the number of seconds to wait before the action would succeed.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'limiter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the WSGI application using the given Limiter instance."""'
newline|'\n'
name|'self'
op|'.'
name|'limiter'
op|'='
name|'limiter'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
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
name|'parts'
op|'='
name|'req'
op|'.'
name|'path_info'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
comment|'# format: /limiter/<username>/<urlencoded action>'
nl|'\n'
name|'if'
name|'req'
op|'.'
name|'method'
op|'!='
string|"'POST'"
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
dedent|''
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'!='
number|'4'
name|'or'
name|'parts'
op|'['
number|'1'
op|']'
op|'!='
string|"'limiter'"
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
op|')'
newline|'\n'
dedent|''
name|'username'
op|'='
name|'parts'
op|'['
number|'2'
op|']'
newline|'\n'
name|'action_name'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'parts'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'perform'
op|'('
name|'action_name'
op|','
name|'username'
op|')'
newline|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'X-Wait-Seconds'"
op|':'
string|'"%.2f"'
op|'%'
name|'delay'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# 200 OK'
nl|'\n'
indent|'            '
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WSGIAppProxy
dedent|''
dedent|''
dedent|''
name|'class'
name|'WSGIAppProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Limiter lookalike that proxies to a ratelimiting.WSGIApp."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'service_host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a proxy pointing to a ratelimiting.WSGIApp at the given\n        host."""'
newline|'\n'
name|'self'
op|'.'
name|'service_host'
op|'='
name|'service_host'
newline|'\n'
nl|'\n'
DECL|member|perform
dedent|''
name|'def'
name|'perform'
op|'('
name|'self'
op|','
name|'action'
op|','
name|'username'
op|'='
string|"'nobody'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'self'
op|'.'
name|'service_host'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/limiter/%s/%s'"
op|'%'
op|'('
name|'username'
op|','
name|'action'
op|')'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'conn'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'.'
name|'status'
op|'=='
number|'200'
op|':'
newline|'\n'
comment|'# No delay'
nl|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'float'
op|'('
name|'resp'
op|'.'
name|'getheader'
op|'('
string|"'X-Wait-Seconds'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
