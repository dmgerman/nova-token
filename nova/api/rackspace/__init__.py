begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nWSGI middleware for Rackspace API controllers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'routes'
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
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'ratelimiting'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'sharedipgroups'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'nova_api_auth'"
op|','
nl|'\n'
string|"'nova.api.rackspace.auth.BasicApiAuthManager'"
op|','
nl|'\n'
string|"'The auth mechanism to use for the Rackspace API implemenation'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI entry point for all Rackspace API requests."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'AuthMiddleware'
op|'('
name|'RateLimitingMiddleware'
op|'('
name|'APIRouter'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|class|AuthMiddleware
dedent|''
dedent|''
name|'class'
name|'AuthMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Authorize the rackspace API request or return an HTTP Forbidden."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auth_driver'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'FLAGS'
op|'.'
name|'nova_api_auth'
op|')'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'AuthMiddleware'
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
name|'if'
name|'not'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'has_key'
op|'('
string|'"X-Auth-Token"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'auth_driver'
op|'.'
name|'authenticate'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'user'
op|'='
name|'self'
op|'.'
name|'auth_driver'
op|'.'
name|'authorize_token'
op|'('
name|'req'
op|'.'
name|'headers'
op|'['
string|'"X-Auth-Token"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
dedent|''
name|'context'
op|'='
op|'{'
string|"'user'"
op|':'
name|'user'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
DECL|class|RateLimitingMiddleware
dedent|''
dedent|''
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
name|'if'
name|'not'
name|'service_host'
op|':'
newline|'\n'
comment|'#TODO(gundlach): These limits were based on limitations of Cloud '
nl|'\n'
comment|'#Servers.  We should revisit them in Nova.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'limiter'
op|'='
name|'ratelimiting'
op|'.'
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
name|'ratelimiting'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'PUT'"
op|':'
op|'('
number|'10'
op|','
name|'ratelimiting'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'POST'"
op|':'
op|'('
number|'10'
op|','
name|'ratelimiting'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
string|"'POST servers'"
op|':'
op|'('
number|'50'
op|','
name|'ratelimiting'
op|'.'
name|'PER_DAY'
op|')'
op|','
nl|'\n'
string|"'GET changes-since'"
op|':'
op|'('
number|'3'
op|','
name|'ratelimiting'
op|'.'
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
name|'ratelimiting'
op|'.'
name|'WSGIAppProxy'
op|'('
name|'service_host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"""Rate limit the request.\n        \n        If the request should be rate limited, return a 413 status with a \n        Retry-After header giving the time when the request would succeed.\n        """'
newline|'\n'
name|'username'
op|'='
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Auth-User'"
op|']'
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
comment|'# not rate limited'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
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
name|'username'
op|')'
newline|'\n'
name|'if'
name|'delay'
op|':'
newline|'\n'
comment|'# TODO(gundlach): Get the retry-after format correct.'
nl|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
name|'headers'
op|'='
op|'{'
nl|'\n'
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
dedent|''
name|'return'
name|'self'
op|'.'
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
DECL|class|APIRouter
dedent|''
dedent|''
name|'class'
name|'APIRouter'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Routes requests on the Rackspace API to the appropriate controller\n    and method.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"server"'
op|','
string|'"servers"'
op|','
name|'controller'
op|'='
name|'servers'
op|'.'
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"image"'
op|','
string|'"images"'
op|','
name|'controller'
op|'='
name|'images'
op|'.'
name|'Controller'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"flavor"'
op|','
string|'"flavors"'
op|','
name|'controller'
op|'='
name|'flavors'
op|'.'
name|'Controller'
op|'('
op|')'
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"sharedipgroup"'
op|','
string|'"sharedipgroups"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'sharedipgroups'
op|'.'
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'APIRouter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
