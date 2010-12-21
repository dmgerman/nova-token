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
string|'"""\nWSGI middleware for OpenStack API controllers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'traceback'
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
name|'context'
newline|'\n'
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
name|'import'
name|'backup_schedules'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'ratelimiting'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'sharedipgroups'
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
string|"'nova.api.openstack.auth.BasicApiAuthManager'"
op|','
nl|'\n'
string|"'The auth mechanism to use for the OpenStack API implemenation'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'allow_admin_api'"
op|','
nl|'\n'
name|'False'
op|','
nl|'\n'
string|"'When True, this API service will accept admin operations.'"
op|')'
newline|'\n'
nl|'\n'
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
string|'"""WSGI entry point for all OpenStack API requests."""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Caught error: %s"'
op|'%'
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthMiddleware
dedent|''
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
string|'"""Authorize the openstack API request or return an HTTP Forbidden."""'
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
string|"'X-Auth-Token'"
name|'not'
name|'in'
name|'req'
op|'.'
name|'headers'
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
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|','
name|'user'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
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
comment|'#TODO(gundlach): These limits were based on limitations of Cloud'
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
string|"'Too many requests.'"
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
string|'"""\n    Routes requests on the OpenStack API to the appropriate controller\n    and method.\n    """'
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
op|','
nl|'\n'
name|'collection'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|','
nl|'\n'
name|'member'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'resource'
op|'('
string|'"backup_schedule"'
op|','
string|'"backup_schedules"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'backup_schedules'
op|'.'
name|'Controller'
op|'('
op|')'
op|','
nl|'\n'
name|'parent_resource'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'server'"
op|','
nl|'\n'
name|'collection_name'
op|'='
string|"'servers'"
op|')'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Including admin operations in API."'
op|')'
newline|'\n'
comment|'# TODO: Place routes for admin operations here.'
nl|'\n'
nl|'\n'
dedent|''
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
nl|'\n'
nl|'\n'
DECL|class|Versions
dedent|''
dedent|''
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
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
string|'"""Respond to a request for all OpenStack API versions."""'
newline|'\n'
name|'response'
op|'='
op|'{'
nl|'\n'
string|'"versions"'
op|':'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
string|'"CURRENT"'
op|','
name|'id'
op|'='
string|'"v1.0"'
op|')'
op|']'
op|'}'
newline|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"application/xml"'
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
name|'dict'
op|'('
name|'version'
op|'='
op|'['
string|'"status"'
op|','
string|'"id"'
op|']'
op|')'
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Serializer'
op|'('
name|'req'
op|'.'
name|'environ'
op|','
name|'metadata'
op|')'
op|'.'
name|'to_content_type'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited
dedent|''
dedent|''
name|'def'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a slice of items according to requested offset and limit.\n\n    items - a sliceable\n    req - wobob.Request possibly containing offset and limit GET variables.\n          offset is where to start in the list, and limit is the maximum number\n          of items to return.\n\n    If limit is not specified, 0, or > 1000, defaults to 1000.\n    """'
newline|'\n'
name|'offset'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'offset'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'limit'
op|':'
newline|'\n'
indent|'        '
name|'limit'
op|'='
number|'1000'
newline|'\n'
dedent|''
name|'limit'
op|'='
name|'min'
op|'('
number|'1000'
op|','
name|'limit'
op|')'
newline|'\n'
name|'range_end'
op|'='
name|'offset'
op|'+'
name|'limit'
newline|'\n'
name|'return'
name|'items'
op|'['
name|'offset'
op|':'
name|'range_end'
op|']'
newline|'\n'
nl|'\n'
DECL|function|auth_factory
dedent|''
name|'def'
name|'auth_factory'
op|'('
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
DECL|function|auth
indent|'    '
name|'def'
name|'auth'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'AuthMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'auth'
newline|'\n'
nl|'\n'
DECL|function|ratelimit_factory
dedent|''
name|'def'
name|'ratelimit_factory'
op|'('
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
DECL|function|rl
indent|'    '
name|'def'
name|'rl'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'RateLimitingMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rl'
newline|'\n'
nl|'\n'
DECL|function|router_factory
dedent|''
name|'def'
name|'router_factory'
op|'('
name|'global_cof'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|versions_factory
dedent|''
name|'def'
name|'versions_factory'
op|'('
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'Versions'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
