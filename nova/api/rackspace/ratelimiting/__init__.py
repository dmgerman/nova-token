begin_unit
string|'"""Rate limiting of arbitrary actions."""'
newline|'\n'
nl|'\n'
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
DECL|class|Limiter
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
nl|'\n'
comment|'# If one instance of this WSGIApps is unable to handle your load, put a'
nl|'\n'
comment|'# sharding app in front that shards by username to one of many backends.'
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
name|'delay'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
comment|'# 200 OK'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
