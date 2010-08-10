begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
comment|'#    under the License.'
nl|'\n'
nl|'\n'
string|'"""\nUtility methods for working with WSGI servers\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'wsgi'
newline|'\n'
name|'eventlet'
op|'.'
name|'patcher'
op|'.'
name|'monkey_patch'
op|'('
name|'all'
op|'='
name|'False'
op|','
name|'socket'
op|'='
name|'True'
op|')'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'routes'
op|'.'
name|'middleware'
newline|'\n'
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"routes.middleware"'
op|')'
op|'.'
name|'addHandler'
op|'('
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|run_server
name|'def'
name|'run_server'
op|'('
name|'application'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run a WSGI server with the given application."""'
newline|'\n'
name|'sock'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
op|'('
string|"'0.0.0.0'"
op|','
name|'port'
op|')'
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'server'
op|'('
name|'sock'
op|','
name|'application'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(gundlach): I think we should toss this class, now that it has no purpose.'
nl|'\n'
DECL|class|Application
dedent|''
name|'class'
name|'Application'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base WSGI application wrapper. Subclasses need to implement __call__."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'r"""Subclasses will probably want to implement __call__ like this:\n\n        @webob.dec.wsgify\n        def __call__(self, req):\n          # Any of the following objects work as responses:\n\n          # Option 1: simple string\n          res = \'message\\n\'\n\n          # Option 2: a nicely formatted HTTP exception page\n          res = exc.HTTPForbidden(detail=\'Nice try\')\n\n          # Option 3: a webob Response object (in case you need to play with\n          # headers, or you want to be treated like an iterable, or or or)\n          res = Response();\n          res.app_iter = open(\'somefile\')\n\n          # Option 4: any wsgi app to be run next\n          res = self.application\n\n          # Option 5: you can get a Response object for a wsgi app, too, to\n          # play with headers etc\n          res = req.get_response(self.application)\n\n          # You can then just return your response...\n          return res\n          # ... or set req.response and return None.\n          req.response = res\n\n        See the end of http://pythonpaste.org/webob/modules/dec.html\n        for more info.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|'"You must implement __call__"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Middleware
dedent|''
dedent|''
name|'class'
name|'Middleware'
op|'('
name|'Application'
op|')'
op|':'
comment|'# pylint: disable-msg=W0223'
newline|'\n'
indent|'    '
string|'"""Base WSGI middleware wrapper. These classes require an\n    application to be initialized that will be called next."""'
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
comment|'# pylint: disable-msg=W0231'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Debug
dedent|''
dedent|''
name|'class'
name|'Debug'
op|'('
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper class that can be insertd into any WSGI application chain\n    to get information about the request and response."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'environ'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'key'
op|','
string|'"="'
op|','
name|'value'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
name|'wrapper'
op|'='
name|'debug_start_response'
op|'('
name|'start_response'
op|')'
newline|'\n'
name|'return'
name|'debug_print_body'
op|'('
name|'self'
op|'.'
name|'application'
op|'('
name|'environ'
op|','
name|'wrapper'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|debug_start_response
dedent|''
dedent|''
name|'def'
name|'debug_start_response'
op|'('
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrap the start_response to capture when called."""'
newline|'\n'
nl|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'status'
op|','
name|'headers'
op|','
name|'exc_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Print out all headers when start_response is called."""'
newline|'\n'
name|'print'
name|'status'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'key'
op|','
string|'"="'
op|','
name|'value'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
name|'start_response'
op|'('
name|'status'
op|','
name|'headers'
op|','
name|'exc_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|debug_print_body
dedent|''
name|'def'
name|'debug_print_body'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Print the body of the response as it is sent back."""'
newline|'\n'
nl|'\n'
DECL|class|Wrapper
name|'class'
name|'Wrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Iterate through all the body parts and print before returning."""'
newline|'\n'
nl|'\n'
DECL|member|__iter__
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'part'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'part'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'part'
newline|'\n'
dedent|''
name|'print'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'Wrapper'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ParsedRoutes
dedent|''
name|'class'
name|'ParsedRoutes'
op|'('
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Processed parsed routes from routes.middleware.RoutesMiddleware\n    and call either the controller if found or the default application\n    otherwise."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'environ'
op|'['
string|"'routes.route'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'application'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
dedent|''
name|'app'
op|'='
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'app'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
nl|'\n'
DECL|class|MichaelRouter
dedent|''
dedent|''
name|'class'
name|'MichaelRouter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    My attempt at a routing class.  Just override __init__ to call\n    super, then set up routes in self.map.\n    """'
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
name|'self'
op|'.'
name|'map'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_router'
op|'='
name|'routes'
op|'.'
name|'middleware'
op|'.'
name|'RoutesMiddleware'
op|'('
name|'self'
op|'.'
name|'_proceed'
op|','
name|'self'
op|'.'
name|'map'
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
string|'"""\n        Route the incoming request to a controller based on self.map.\n        If no match, return a 404.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_router'
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
DECL|member|_proceed
name|'def'
name|'_proceed'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called by self._router after matching the incoming request to a route\n        and putting the information into req.environ.\n        """'
newline|'\n'
name|'if'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'routes.route'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'match'
op|'='
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'match'
op|'.'
name|'get'
op|'('
string|"'_is_wsgi'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'wsgiapp'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'wsgiapp'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# TODO(gundlach): doubt this is the right way -- and it really'
nl|'\n'
comment|'# feels like this code should exist somewhere already on the'
nl|'\n'
comment|'# internet'
nl|'\n'
indent|'            '
name|'controller'
op|','
name|'action'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
op|','
name|'match'
op|'['
string|"'action'"
op|']'
newline|'\n'
name|'delete'
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'delete'
name|'match'
op|'['
string|"'action'"
op|']'
newline|'\n'
name|'return'
name|'_as_response'
op|'('
name|'getattr'
op|'('
name|'controller'
op|','
name|'action'
op|')'
op|'('
op|'**'
name|'match'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'controller'
op|'='
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_dispatch'
op|'('
name|'controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_as_response
dedent|''
name|'def'
name|'_as_response'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When routing to a non-wsgi controller+action, its result will\n        be passed here before returning up the WSGI chain to be converted\n        into a webob.Response\n\n\n\n\n\nclass ApiVersionRouter(MichaelRouter):\n    \n    def __init__(self):\n        super(ApiVersionRouter, self).__init__(self)\n\n        self.map.connect(None, "/v1.0/{path_info:.*}", controller=RsApiRouter())\n        self.map.connect(None, "/ec2/{path_info:.*}", controller=Ec2ApiRouter())\n\nclass RsApiRouter(MichaelRouter):\n    def __init__(self):\n        super(RsApiRouter, self).__init__(self)\n\n        self.map.resource("server", "servers", controller=CloudServersServerApi())\n        self.map.resource("image", "images", controller=CloudServersImageApi())\n        self.map.resource("flavor", "flavors", controller=CloudServersFlavorApi())\n        self.map.resource("sharedipgroup", "sharedipgroups",\n                          controller=CloudServersSharedIpGroupApi())\n\nclass Ec2ApiRouter(object):\n    def __getattr__(self, key):\n        return lambda *x: {\'dummy response\': \'i am a dummy response\'}\nCloudServersServerApi = CloudServersImageApi = CloudServersFlavorApi = \\\n        CloudServersSharedIpGroupApi = Ec2ApiRouter\n\nclass Router(Middleware): # pylint: disable-msg=R0921\n    """'
name|'Wrapper'
name|'to'
name|'help'
name|'setup'
name|'routes'
op|'.'
name|'middleware'
op|'.'
name|'RoutesMiddleware'
op|'.'
string|'"""\n\n    def __init__(self, application):\n        self.map = routes.Mapper()\n        self._build_map()\n        application = ParsedRoutes(application)\n        application = routes.middleware.RoutesMiddleware(application, self.map)\n        super(Router, self).__init__(application)\n\n    def __call__(self, environ, start_response):\n        return self.application(environ, start_response)\n\n    def _build_map(self):\n        """'
name|'Method'
name|'to'
name|'create'
name|'new'
name|'connections'
name|'for'
name|'the'
name|'routing'
name|'map'
op|'.'
string|'"""\n        raise NotImplementedError("You must implement _build_map")\n\n    def _connect(self, *args, **kwargs):\n        """'
name|'Wrapper'
name|'for'
name|'the'
name|'map'
op|'.'
name|'connect'
name|'method'
op|'.'
string|'"""\n        self.map.connect(*args, **kwargs)\n\n\ndef route_args(application):\n    """'
name|'Decorator'
name|'to'
name|'make'
name|'grabbing'
name|'routing'
name|'args'
name|'more'
name|'convenient'
op|'.'
string|'"""\n\n    def wrapper(self, req):\n        """'
name|'Call'
name|'application'
name|'with'
name|'req'
name|'and'
name|'parsed'
name|'routing'
name|'args'
name|'from'
op|'.'
end_unit
