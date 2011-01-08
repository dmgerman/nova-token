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
name|'json'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
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
op|','
name|'time'
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
name|'import'
name|'webob'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WritableLogger
name|'class'
name|'WritableLogger'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A thin wrapper that responds to `write` and logs."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'logger'
op|','
name|'level'
op|'='
name|'logging'
op|'.'
name|'DEBUG'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logger'
op|'='
name|'logger'
newline|'\n'
name|'self'
op|'.'
name|'level'
op|'='
name|'level'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'logger'
op|'.'
name|'log'
op|'('
name|'self'
op|'.'
name|'level'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Server
dedent|''
dedent|''
name|'class'
name|'Server'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server class to manage multiple WSGI sockets and applications."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'threads'
op|'='
number|'1000'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'basicConfig'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'='
name|'eventlet'
op|'.'
name|'GreenPool'
op|'('
name|'threads'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'port'
op|','
name|'host'
op|'='
string|"'0.0.0.0'"
op|','
name|'backlog'
op|'='
number|'128'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run a WSGI server with the given application."""'
newline|'\n'
name|'logging'
op|'.'
name|'audit'
op|'('
string|'"Starting %s on %s:%s"'
op|','
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|','
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
name|'socket'
op|'='
name|'eventlet'
op|'.'
name|'listen'
op|'('
op|'('
name|'host'
op|','
name|'port'
op|')'
op|','
name|'backlog'
op|'='
name|'backlog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_run'
op|','
name|'application'
op|','
name|'socket'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wait until all servers have completed running."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'pool'
op|'.'
name|'waitall'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyboardInterrupt'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_run
dedent|''
dedent|''
name|'def'
name|'_run'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'socket'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start a WSGI server in a new green thread."""'
newline|'\n'
name|'logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'eventlet.wsgi.server'"
op|')'
newline|'\n'
name|'eventlet'
op|'.'
name|'wsgi'
op|'.'
name|'server'
op|'('
name|'socket'
op|','
name|'application'
op|','
name|'custom_pool'
op|'='
name|'self'
op|'.'
name|'pool'
op|','
nl|'\n'
name|'log'
op|'='
name|'WritableLogger'
op|'('
name|'logger'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Application
dedent|''
dedent|''
name|'class'
name|'Application'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
comment|'# TODO(gundlach): I think we should toss this class, now that it has no'
nl|'\n'
comment|'# purpose.'
nl|'\n'
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
newline|'\n'
indent|'    '
string|'"""\n    Base WSGI middleware wrapper. These classes require an application to be\n    initialized that will be called next.  By default the middleware will\n    simply call its wrapped app, or you can override __call__ to customize its\n    behavior.\n    """'
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
comment|'# pylint: disable-msg=W0221'
newline|'\n'
indent|'        '
string|'"""Override to implement middleware behavior."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
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
string|'"""Helper class that can be inserted into any WSGI application chain\n    to get information about the request and response."""'
newline|'\n'
nl|'\n'
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
name|'print'
op|'('
string|'"*"'
op|'*'
number|'40'
op|')'
op|'+'
string|'" REQUEST ENVIRON"'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'req'
op|'.'
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
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
nl|'\n'
name|'print'
op|'('
string|'"*"'
op|'*'
number|'40'
op|')'
op|'+'
string|'" RESPONSE HEADERS"'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'resp'
op|'.'
name|'headers'
op|'.'
name|'iteritems'
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
nl|'\n'
name|'resp'
op|'.'
name|'app_iter'
op|'='
name|'self'
op|'.'
name|'print_generator'
op|'('
name|'resp'
op|'.'
name|'app_iter'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|print_generator
name|'def'
name|'print_generator'
op|'('
name|'app_iter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Iterator that prints the contents of a wrapper string iterator\n        when iterated.\n        """'
newline|'\n'
name|'print'
op|'('
string|'"*"'
op|'*'
number|'40'
op|')'
op|'+'
string|'" BODY"'
newline|'\n'
name|'for'
name|'part'
name|'in'
name|'app_iter'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    WSGI middleware that maps incoming requests to WSGI apps.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a router for the given routes.Mapper.\n\n        Each route in `mapper` must specify a \'controller\', which is a\n        WSGI app to call.  You\'ll probably want to specify an \'action\' as\n        well and have your controller be a wsgi.Controller, who will route\n        the request to the action method.\n\n        Examples:\n          mapper = routes.Mapper()\n          sc = ServerController()\n\n          # Explicit mapping of one route to a controller+action\n          mapper.connect(None, "/svrlist", controller=sc, action="list")\n\n          # Actions are all implicitly defined\n          mapper.resource("server", "servers", controller=sc)\n\n          # Pointing to an arbitrary WSGI app.  You can specify the\n          # {path_info:.*} parameter so the target app can be handed just that\n          # section of the URL.\n          mapper.connect(None, "/v1.0/{path_info:.*}", controller=BlogApp())\n        """'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'='
name|'mapper'
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
name|'_dispatch'
op|','
nl|'\n'
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
name|'staticmethod'
newline|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|_dispatch
name|'def'
name|'_dispatch'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Called by self._router after matching the incoming request to a route\n        and putting the information into req.environ.  Either returns 404\n        or the routed WSGI app\'s response.\n        """'
newline|'\n'
name|'match'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'match'
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
name|'app'
op|'='
name|'match'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'return'
name|'app'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    WSGI app that reads routing information supplied by RoutesMiddleware\n    and calls the requested action method upon itself.  All action methods\n    must, in addition to their normal parameters, accept a \'req\' argument\n    which is the incoming webob.Request.  They raise a webob.exc exception,\n    or return a dict which will be serialized by requested content type.\n    """'
newline|'\n'
nl|'\n'
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
string|'"""\n        Call the method specified in req.environ by RoutesMiddleware.\n        """'
newline|'\n'
name|'arg_dict'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'action'
op|'='
name|'arg_dict'
op|'['
string|"'action'"
op|']'
newline|'\n'
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'action'
op|')'
newline|'\n'
name|'del'
name|'arg_dict'
op|'['
string|"'controller'"
op|']'
newline|'\n'
name|'del'
name|'arg_dict'
op|'['
string|"'action'"
op|']'
newline|'\n'
name|'arg_dict'
op|'['
string|"'req'"
op|']'
op|'='
name|'req'
newline|'\n'
name|'result'
op|'='
name|'method'
op|'('
op|'**'
name|'arg_dict'
op|')'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'result'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_serialize'
op|'('
name|'result'
op|','
name|'req'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_serialize
dedent|''
dedent|''
name|'def'
name|'_serialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Serialize the given dict to the response type requested in request.\n        Uses self._serialization_metadata if it exists, which is a dict mapping\n        MIME types to information needed to serialize to that type.\n        """'
newline|'\n'
name|'_metadata'
op|'='
name|'getattr'
op|'('
name|'type'
op|'('
name|'self'
op|')'
op|','
string|'"_serialization_metadata"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'Serializer'
op|'('
name|'request'
op|'.'
name|'environ'
op|','
name|'_metadata'
op|')'
newline|'\n'
name|'return'
name|'serializer'
op|'.'
name|'to_content_type'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_deserialize
dedent|''
name|'def'
name|'_deserialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deserialize the request body to the response type requested in request.\n        Uses self._serialization_metadata if it exists, which is a dict mapping\n        MIME types to information needed to serialize to that type.\n        """'
newline|'\n'
name|'_metadata'
op|'='
name|'getattr'
op|'('
name|'type'
op|'('
name|'self'
op|')'
op|','
string|'"_serialization_metadata"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'Serializer'
op|'('
name|'request'
op|'.'
name|'environ'
op|','
name|'_metadata'
op|')'
newline|'\n'
name|'return'
name|'serializer'
op|'.'
name|'deserialize'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Serializer
dedent|''
dedent|''
name|'class'
name|'Serializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Serializes and deserializes dictionaries to certain MIME types.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'metadata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a serializer based on the given WSGI environment.\n        \'metadata\' is an optional dict mapping MIME types to information\n        needed to serialize a dictionary to that type.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'metadata'
op|'='
name|'metadata'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"''"
op|','
name|'environ'
op|')'
newline|'\n'
name|'suffix'
op|'='
name|'req'
op|'.'
name|'path_info'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
name|'suffix'
op|'=='
string|"'json'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_to_json'
newline|'\n'
dedent|''
name|'elif'
name|'suffix'
op|'=='
string|"'xml'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_to_xml'
newline|'\n'
dedent|''
name|'elif'
string|"'application/json'"
name|'in'
name|'req'
op|'.'
name|'accept'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_to_json'
newline|'\n'
dedent|''
name|'elif'
string|"'application/xml'"
name|'in'
name|'req'
op|'.'
name|'accept'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_to_xml'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# This is the default'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_to_json'
newline|'\n'
nl|'\n'
DECL|member|to_content_type
dedent|''
dedent|''
name|'def'
name|'to_content_type'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Serialize a dictionary into a string.\n\n        The format of the string will be decided based on the Content Type\n        requested in self.environ: by Accept: header, or by URL suffix.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'handler'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize
dedent|''
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deserialize a string to a dictionary.\n\n        The string must be in the format of a supported MIME type.\n        """'
newline|'\n'
name|'datastring'
op|'='
name|'datastring'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'is_xml'
op|'='
op|'('
name|'datastring'
op|'['
number|'0'
op|']'
op|'=='
string|"'<'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'is_xml'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'datastring'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_from_xml'
op|'('
name|'datastring'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_from_xml
dedent|''
dedent|''
name|'def'
name|'_from_xml'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xmldata'
op|'='
name|'self'
op|'.'
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'application/xml'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'plurals'
op|'='
name|'set'
op|'('
name|'xmldata'
op|'.'
name|'get'
op|'('
string|"'plurals'"
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
name|'node'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
op|'{'
name|'node'
op|'.'
name|'nodeName'
op|':'
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'node'
op|','
name|'plurals'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_from_xml_node
dedent|''
name|'def'
name|'_from_xml_node'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'listnames'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Convert a minidom node to a simple Python type.\n\n        listnames is a collection of names of XML nodes whose subnodes should\n        be considered list items.\n        """'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'node'
op|'.'
name|'childNodes'
op|')'
op|'=='
number|'1'
name|'and'
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
op|'.'
name|'nodeType'
op|'=='
number|'3'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
op|'.'
name|'nodeValue'
newline|'\n'
dedent|''
name|'elif'
name|'node'
op|'.'
name|'nodeName'
name|'in'
name|'listnames'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'n'
op|','
name|'listnames'
op|')'
name|'for'
name|'n'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'node'
op|'.'
name|'attributes'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'attr'
op|']'
op|'='
name|'node'
op|'.'
name|'attributes'
op|'['
name|'attr'
op|']'
op|'.'
name|'nodeValue'
newline|'\n'
dedent|''
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'child'
op|'.'
name|'nodeType'
op|'!='
name|'node'
op|'.'
name|'TEXT_NODE'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'child'
op|'.'
name|'nodeName'
op|']'
op|'='
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'child'
op|','
nl|'\n'
name|'listnames'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_to_json
dedent|''
dedent|''
name|'def'
name|'_to_json'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_xml
dedent|''
name|'def'
name|'_to_xml'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
name|'self'
op|'.'
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'application/xml'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|'# We expect data to contain a single key which is the XML root.'
nl|'\n'
name|'root_key'
op|'='
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'metadata'
op|','
name|'root_key'
op|','
name|'data'
op|'['
name|'root_key'
op|']'
op|')'
newline|'\n'
name|'return'
name|'node'
op|'.'
name|'toprettyxml'
op|'('
name|'indent'
op|'='
string|"'    '"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_xml_node
dedent|''
name|'def'
name|'_to_xml_node'
op|'('
name|'self'
op|','
name|'doc'
op|','
name|'metadata'
op|','
name|'nodename'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recursive method to convert data members to XML nodes."""'
newline|'\n'
name|'result'
op|'='
name|'doc'
op|'.'
name|'createElement'
op|'('
name|'nodename'
op|')'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'data'
op|')'
name|'is'
name|'list'
op|':'
newline|'\n'
indent|'            '
name|'singular'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'plurals'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
name|'nodename'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'singular'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'nodename'
op|'.'
name|'endswith'
op|'('
string|"'s'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'singular'
op|'='
name|'nodename'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'singular'
op|'='
string|"'item'"
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'metadata'
op|','
name|'singular'
op|','
name|'item'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'type'
op|'('
name|'data'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'attrs'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'attributes'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
name|'nodename'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'data'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'k'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'.'
name|'setAttribute'
op|'('
name|'k'
op|','
name|'str'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'metadata'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Type is atom'
nl|'\n'
indent|'            '
name|'node'
op|'='
name|'doc'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
