begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'import'
name|'imp'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
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
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'extensions'"
op|')'
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
nl|'\n'
nl|'\n'
DECL|class|ExtensionActionController
name|'class'
name|'ExtensionActionController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'action_name'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
name|'self'
op|'.'
name|'action_name'
op|'='
name|'action_name'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'input_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'action_name'
name|'in'
name|'input_dict'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'handler'
op|'('
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
newline|'\n'
comment|'# no action handler found (bump to downstream application)'
nl|'\n'
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'application'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionMiddleware
dedent|''
dedent|''
name|'class'
name|'ExtensionMiddleware'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Extensions middleware that intercepts configured routes for extensions.\n    """'
newline|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|factory
name|'def'
name|'factory'
op|'('
name|'cls'
op|','
name|'global_config'
op|','
op|'**'
name|'local_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" paste factory """'
newline|'\n'
DECL|function|_factory
name|'def'
name|'_factory'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'('
name|'app'
op|','
op|'**'
name|'local_config'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_factory'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'ext_mgr'
op|'='
name|'None'
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
nl|'\n'
name|'if'
name|'ext_mgr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ext_mgr'
op|'='
name|'ExtensionManager'
op|'('
name|'FLAGS'
op|'.'
name|'osapi_extensions_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# create custom mapper connections for extended actions'
nl|'\n'
dedent|''
name|'for'
name|'action'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_actions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'controller'
op|'='
name|'ExtensionActionController'
op|'('
name|'application'
op|','
name|'action'
op|'.'
name|'name'
op|','
nl|'\n'
name|'action'
op|'.'
name|'handler'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/%s/{id}/action.:(format)"'
op|'%'
name|'action'
op|'.'
name|'collection'
op|','
nl|'\n'
name|'action'
op|'='
string|"'action'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
op|'['
string|"'POST'"
op|']'
op|')'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/%s/{id}/action"'
op|'%'
name|'action'
op|'.'
name|'collection'
op|','
nl|'\n'
name|'action'
op|'='
string|"'action'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
op|'['
string|"'POST'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'mapper'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'ExtensionMiddleware'
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
string|'"""\n        Route the incoming request with router.\n        """'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'extended.app'"
op|']'
op|'='
name|'self'
op|'.'
name|'application'
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
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
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
string|'"""\n        Called by self._router after matching the incoming request to a route\n        and putting the information into req.environ.  Either returns the\n        routed WSGI app\'s response or defers to the extended application.\n        """'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'extended.app'"
op|']'
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
DECL|class|ExtensionManager
dedent|''
dedent|''
name|'class'
name|'ExtensionManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Initializing extension manager.'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_load_extensions'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        returns a list of ExtensionResource objects\n        """'
newline|'\n'
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'.'
name|'append'
op|'('
name|'ext'
op|'.'
name|'get_resources'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ext'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'actions'
op|'.'
name|'extend'
op|'('
name|'ext'
op|'.'
name|'get_actions'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
DECL|member|_load_extensions
dedent|''
name|'def'
name|'_load_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Load extensions from the configured path. The extension name is\n        constructed from the camel cased module_name + \'Extension\'. If your\n        extension module was named widgets.py the extension class within that\n        module should be \'WidgetsExtension\'.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'f'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Loading extension file: %s'"
op|')'
op|','
name|'f'
op|')'
newline|'\n'
name|'mod_name'
op|','
name|'file_ext'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'splitext'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'f'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
name|'ext_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'path'
op|','
name|'f'
op|')'
newline|'\n'
name|'if'
name|'file_ext'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'.py'"
op|':'
newline|'\n'
indent|'                '
name|'mod'
op|'='
name|'imp'
op|'.'
name|'load_source'
op|'('
name|'mod_name'
op|','
name|'ext_path'
op|')'
newline|'\n'
name|'ext_name'
op|'='
name|'mod_name'
op|'['
number|'0'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
name|'mod_name'
op|'['
number|'1'
op|':'
op|']'
op|'+'
string|"'Extension'"
newline|'\n'
name|'self'
op|'.'
name|'extensions'
op|'.'
name|'append'
op|'('
name|'getattr'
op|'('
name|'mod'
op|','
name|'ext_name'
op|')'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionAction
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtensionAction'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'member'
op|','
name|'collection'
op|','
name|'name'
op|','
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'member'
op|'='
name|'member'
newline|'\n'
name|'self'
op|'.'
name|'collection'
op|'='
name|'collection'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'='
name|'handler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionResource
dedent|''
dedent|''
name|'class'
name|'ExtensionResource'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Example ExtensionResource object. All ExtensionResource objects should\n    adhere to this interface.\n    """'
newline|'\n'
nl|'\n'
DECL|member|add_routes
name|'def'
name|'add_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
