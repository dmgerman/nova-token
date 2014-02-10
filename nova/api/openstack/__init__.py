begin_unit
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
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'stevedore'
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
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'gettextutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
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
DECL|variable|api_opts
name|'api_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enabled'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether the V3 API is enabled or not'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'extensions_blacklist'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of v3 API extensions to never load. '"
nl|'\n'
string|"'Specify the extension aliases here.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'extensions_whitelist'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If the list is not empty then a v3 API extension '"
nl|'\n'
string|"'will only be loaded if it exists in this list. Specify '"
nl|'\n'
string|"'the extension aliases here.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
DECL|variable|api_opts_group
name|'api_opts_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'osapi_v3'"
op|','
name|'title'
op|'='
string|"'API v3 Options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_group'
op|'('
name|'api_opts_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'api_opts'
op|','
name|'api_opts_group'
op|')'
newline|'\n'
nl|'\n'
comment|'# List of v3 API extensions which are considered to form'
nl|'\n'
comment|'# the core API and so must be present'
nl|'\n'
comment|'# TODO(cyeoh): Expand this list as the core APIs are ported to V3'
nl|'\n'
DECL|variable|API_V3_CORE_EXTENSIONS
name|'API_V3_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'console-output'"
op|','
nl|'\n'
string|"'consoles'"
op|','
nl|'\n'
string|"'extensions'"
op|','
nl|'\n'
string|"'flavor-access'"
op|','
nl|'\n'
string|"'flavor-extra-specs'"
op|','
nl|'\n'
string|"'flavor-manage'"
op|','
nl|'\n'
string|"'flavors'"
op|','
nl|'\n'
string|"'ips'"
op|','
nl|'\n'
string|"'keypairs'"
op|','
nl|'\n'
string|"'server-metadata'"
op|','
nl|'\n'
string|"'servers'"
op|','
nl|'\n'
string|"'versions'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FaultWrapper
name|'class'
name|'FaultWrapper'
op|'('
name|'base_wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Calls down the middleware stack, making exceptions into faults."""'
newline|'\n'
nl|'\n'
DECL|variable|_status_to_type
name|'_status_to_type'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|status_to_type
name|'def'
name|'status_to_type'
op|'('
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'FaultWrapper'
op|'.'
name|'_status_to_type'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'clazz'
name|'in'
name|'utils'
op|'.'
name|'walk_class_hierarchy'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'FaultWrapper'
op|'.'
name|'_status_to_type'
op|'['
name|'clazz'
op|'.'
name|'code'
op|']'
op|'='
name|'clazz'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'FaultWrapper'
op|'.'
name|'_status_to_type'
op|'.'
name|'get'
op|'('
nl|'\n'
name|'status'
op|','
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_error
dedent|''
name|'def'
name|'_error'
op|'('
name|'self'
op|','
name|'inner'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Caught error: %s"'
op|')'
op|','
name|'unicode'
op|'('
name|'inner'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'safe'
op|'='
name|'getattr'
op|'('
name|'inner'
op|','
string|"'safe'"
op|','
name|'False'
op|')'
newline|'\n'
name|'headers'
op|'='
name|'getattr'
op|'('
name|'inner'
op|','
string|"'headers'"
op|','
name|'None'
op|')'
newline|'\n'
name|'status'
op|'='
name|'getattr'
op|'('
name|'inner'
op|','
string|"'code'"
op|','
number|'500'
op|')'
newline|'\n'
name|'if'
name|'status'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
number|'500'
newline|'\n'
nl|'\n'
dedent|''
name|'msg_dict'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'req'
op|'.'
name|'url'
op|','
name|'status'
op|'='
name|'status'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"%(url)s returned with HTTP %(status)d"'
op|')'
op|'%'
name|'msg_dict'
op|')'
newline|'\n'
name|'outer'
op|'='
name|'self'
op|'.'
name|'status_to_type'
op|'('
name|'status'
op|')'
newline|'\n'
name|'if'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'outer'
op|'.'
name|'headers'
op|'='
name|'headers'
newline|'\n'
comment|'# NOTE(johannes): We leave the explanation empty here on'
nl|'\n'
comment|'# purpose. It could possibly have sensitive information'
nl|'\n'
comment|'# that should not be returned back to the user. See'
nl|'\n'
comment|'# bugs 868360 and 874472'
nl|'\n'
comment|'# NOTE(eglynn): However, it would be over-conservative and'
nl|'\n'
comment|'# inconsistent with the EC2 API to hide every exception,'
nl|'\n'
comment|'# including those that are safe to expose, see bug 1021373'
nl|'\n'
dedent|''
name|'if'
name|'safe'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'inner'
op|'.'
name|'msg_fmt'
op|','
name|'gettextutils'
op|'.'
name|'Message'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'user_locale'
op|'='
name|'req'
op|'.'
name|'best_match_language'
op|'('
op|')'
newline|'\n'
name|'inner_msg'
op|'='
name|'gettextutils'
op|'.'
name|'translate'
op|'('
nl|'\n'
name|'inner'
op|'.'
name|'msg_fmt'
op|','
name|'user_locale'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'inner_msg'
op|'='
name|'unicode'
op|'('
name|'inner'
op|')'
newline|'\n'
dedent|''
name|'outer'
op|'.'
name|'explanation'
op|'='
string|"'%s: %s'"
op|'%'
op|'('
name|'inner'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'inner_msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'notifications'
op|'.'
name|'send_api_fault'
op|'('
name|'req'
op|'.'
name|'url'
op|','
name|'status'
op|','
name|'inner'
op|')'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'outer'
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
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'ex'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIMapper
dedent|''
dedent|''
dedent|''
name|'class'
name|'APIMapper'
op|'('
name|'routes'
op|'.'
name|'Mapper'
op|')'
op|':'
newline|'\n'
DECL|member|routematch
indent|'    '
name|'def'
name|'routematch'
op|'('
name|'self'
op|','
name|'url'
op|'='
name|'None'
op|','
name|'environ'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'url'
op|'=='
string|'""'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
string|'""'
op|','
name|'environ'
op|')'
newline|'\n'
name|'return'
name|'result'
op|'['
number|'0'
op|']'
op|','
name|'result'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'routematch'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'environ'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connect
dedent|''
name|'def'
name|'connect'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Default the format part of a route to only accept json'
nl|'\n'
comment|"#             and xml so it doesn't eat all characters after a '.'"
nl|'\n'
comment|'#             in the url.'
nl|'\n'
indent|'        '
name|'kargs'
op|'.'
name|'setdefault'
op|'('
string|"'requirements'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'kargs'
op|'['
string|"'requirements'"
op|']'
op|'.'
name|'get'
op|'('
string|"'format'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kargs'
op|'['
string|"'requirements'"
op|']'
op|'['
string|"'format'"
op|']'
op|'='
string|"'json|xml'"
newline|'\n'
dedent|''
name|'return'
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'connect'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectMapper
dedent|''
dedent|''
name|'class'
name|'ProjectMapper'
op|'('
name|'APIMapper'
op|')'
op|':'
newline|'\n'
DECL|member|resource
indent|'    '
name|'def'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
name|'collection_name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'parent_resource'"
name|'not'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'path_prefix'"
op|']'
op|'='
string|"'{project_id}/'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'parent_resource'
op|'='
name|'kwargs'
op|'['
string|"'parent_resource'"
op|']'
newline|'\n'
name|'p_collection'
op|'='
name|'parent_resource'
op|'['
string|"'collection_name'"
op|']'
newline|'\n'
name|'p_member'
op|'='
name|'parent_resource'
op|'['
string|"'member_name'"
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|"'path_prefix'"
op|']'
op|'='
string|"'{project_id}/%s/:%s_id'"
op|'%'
op|'('
name|'p_collection'
op|','
nl|'\n'
name|'p_member'
op|')'
newline|'\n'
dedent|''
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
nl|'\n'
name|'collection_name'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PlainMapper
dedent|''
dedent|''
name|'class'
name|'PlainMapper'
op|'('
name|'APIMapper'
op|')'
op|':'
newline|'\n'
DECL|member|resource
indent|'    '
name|'def'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
name|'collection_name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'parent_resource'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'parent_resource'
op|'='
name|'kwargs'
op|'['
string|"'parent_resource'"
op|']'
newline|'\n'
name|'p_collection'
op|'='
name|'parent_resource'
op|'['
string|"'collection_name'"
op|']'
newline|'\n'
name|'p_member'
op|'='
name|'parent_resource'
op|'['
string|"'member_name'"
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|"'path_prefix'"
op|']'
op|'='
string|"'%s/:%s_id'"
op|'%'
op|'('
name|'p_collection'
op|','
name|'p_member'
op|')'
newline|'\n'
dedent|''
name|'routes'
op|'.'
name|'Mapper'
op|'.'
name|'resource'
op|'('
name|'self'
op|','
name|'member_name'
op|','
nl|'\n'
name|'collection_name'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRouter
dedent|''
dedent|''
name|'class'
name|'APIRouter'
op|'('
name|'base_wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Routes requests on the OpenStack API to the appropriate controller\n    and method.\n    """'
newline|'\n'
DECL|variable|ExtensionManager
name|'ExtensionManager'
op|'='
name|'None'
comment|'# override in subclasses'
newline|'\n'
nl|'\n'
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
string|'"""Simple paste factory, :class:`nova.wsgi.Router` doesn\'t have one."""'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|','
name|'init_only'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ext_mgr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'ExtensionManager'
op|':'
newline|'\n'
indent|'                '
name|'ext_mgr'
op|'='
name|'self'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify an ExtensionManager class"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mapper'
op|'='
name|'ProjectMapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_setup_routes'
op|'('
name|'mapper'
op|','
name|'ext_mgr'
op|','
name|'init_only'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_ext_routes'
op|'('
name|'mapper'
op|','
name|'ext_mgr'
op|','
name|'init_only'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_extensions'
op|'('
name|'ext_mgr'
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
nl|'\n'
DECL|member|_setup_ext_routes
dedent|''
name|'def'
name|'_setup_ext_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|','
name|'ext_mgr'
op|','
name|'init_only'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'resource'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_resources'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extending resource: %s'"
op|')'
op|','
nl|'\n'
name|'resource'
op|'.'
name|'collection'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'init_only'
name|'is'
name|'not'
name|'None'
name|'and'
name|'resource'
op|'.'
name|'collection'
name|'not'
name|'in'
name|'init_only'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'inherits'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'resource'
op|'.'
name|'inherits'
op|':'
newline|'\n'
indent|'                '
name|'inherits'
op|'='
name|'self'
op|'.'
name|'resources'
op|'.'
name|'get'
op|'('
name|'resource'
op|'.'
name|'inherits'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'resource'
op|'.'
name|'controller'
op|':'
newline|'\n'
indent|'                    '
name|'resource'
op|'.'
name|'controller'
op|'='
name|'inherits'
op|'.'
name|'controller'
newline|'\n'
dedent|''
dedent|''
name|'wsgi_resource'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'resource'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'inherits'
op|'='
name|'inherits'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'['
name|'resource'
op|'.'
name|'collection'
op|']'
op|'='
name|'wsgi_resource'
newline|'\n'
name|'kargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'controller'
op|'='
name|'wsgi_resource'
op|','
nl|'\n'
name|'collection'
op|'='
name|'resource'
op|'.'
name|'collection_actions'
op|','
nl|'\n'
name|'member'
op|'='
name|'resource'
op|'.'
name|'member_actions'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'parent'
op|':'
newline|'\n'
indent|'                '
name|'kargs'
op|'['
string|"'parent_resource'"
op|']'
op|'='
name|'resource'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'resource'
op|'('
name|'resource'
op|'.'
name|'collection'
op|','
name|'resource'
op|'.'
name|'collection'
op|','
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'custom_routes_fn'
op|':'
newline|'\n'
indent|'                '
name|'resource'
op|'.'
name|'custom_routes_fn'
op|'('
name|'mapper'
op|','
name|'wsgi_resource'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_extensions
dedent|''
dedent|''
dedent|''
name|'def'
name|'_setup_extensions'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'extension'
name|'in'
name|'ext_mgr'
op|'.'
name|'get_controller_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'collection'
op|'='
name|'extension'
op|'.'
name|'collection'
newline|'\n'
name|'controller'
op|'='
name|'extension'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
name|'msg_format_dict'
op|'='
op|'{'
string|"'collection'"
op|':'
name|'collection'
op|','
nl|'\n'
string|"'ext_name'"
op|':'
name|'extension'
op|'.'
name|'extension'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'if'
name|'collection'
name|'not'
name|'in'
name|'self'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s: Cannot extend '"
nl|'\n'
string|"'resource %(collection)s: No such resource'"
op|')'
op|','
nl|'\n'
name|'msg_format_dict'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s extended resource: '"
nl|'\n'
string|"'%(collection)s'"
op|')'
op|','
nl|'\n'
name|'msg_format_dict'
op|')'
newline|'\n'
nl|'\n'
name|'resource'
op|'='
name|'self'
op|'.'
name|'resources'
op|'['
name|'collection'
op|']'
newline|'\n'
name|'resource'
op|'.'
name|'register_actions'
op|'('
name|'controller'
op|')'
newline|'\n'
name|'resource'
op|'.'
name|'register_extensions'
op|'('
name|'controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_routes
dedent|''
dedent|''
name|'def'
name|'_setup_routes'
op|'('
name|'self'
op|','
name|'mapper'
op|','
name|'ext_mgr'
op|','
name|'init_only'
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
DECL|class|APIRouterV3
dedent|''
dedent|''
name|'class'
name|'APIRouterV3'
op|'('
name|'base_wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Routes requests on the OpenStack v3 API to the appropriate controller\n    and method.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|API_EXTENSION_NAMESPACE
name|'API_EXTENSION_NAMESPACE'
op|'='
string|"'nova.api.v3.extensions'"
newline|'\n'
nl|'\n'
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
string|'"""Simple paste factory, :class:`nova.wsgi.Router` doesn\'t have one."""'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'init_only'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# TODO(cyeoh): bp v3-api-extension-framework. Currently load'
nl|'\n'
comment|'# all extensions but eventually should be able to exclude'
nl|'\n'
comment|'# based on a config file'
nl|'\n'
DECL|function|_check_load_extension
indent|'        '
name|'def'
name|'_check_load_extension'
op|'('
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'self'
op|'.'
name|'init_only'
name|'is'
name|'None'
name|'or'
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
name|'in'
nl|'\n'
name|'self'
op|'.'
name|'init_only'
op|')'
name|'and'
name|'isinstance'
op|'('
name|'ext'
op|'.'
name|'obj'
op|','
nl|'\n'
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Check whitelist is either empty or if not then the extension'
nl|'\n'
comment|'# is in the whitelist'
nl|'\n'
indent|'                '
name|'if'
op|'('
name|'not'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_whitelist'
name|'or'
nl|'\n'
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
name|'in'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_whitelist'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Check the extension is not in the blacklist'
nl|'\n'
indent|'                    '
name|'if'
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
name|'not'
name|'in'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_blacklist'
op|':'
newline|'\n'
indent|'                        '
name|'return'
name|'self'
op|'.'
name|'_register_extension'
op|'('
name|'ext'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Not loading %s because it is "'
nl|'\n'
string|'"in the blacklist"'
op|')'
op|','
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warning'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Not loading %s because it is not in the whitelist"'
op|')'
op|','
nl|'\n'
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'enabled'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"V3 API has been disabled by configuration"'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'init_only'
op|'='
name|'init_only'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"v3 API Extension Blacklist: %s"'
op|')'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_blacklist'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"v3 API Extension Whitelist: %s"'
op|')'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_whitelist'
op|')'
newline|'\n'
nl|'\n'
name|'in_blacklist_and_whitelist'
op|'='
name|'set'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_whitelist'
op|')'
op|'.'
name|'intersection'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'osapi_v3'
op|'.'
name|'extensions_blacklist'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'in_blacklist_and_whitelist'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Extensions in both blacklist and whitelist: %s"'
op|')'
op|','
nl|'\n'
name|'list'
op|'('
name|'in_blacklist_and_whitelist'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'api_extension_manager'
op|'='
name|'stevedore'
op|'.'
name|'enabled'
op|'.'
name|'EnabledExtensionManager'
op|'('
nl|'\n'
name|'namespace'
op|'='
name|'self'
op|'.'
name|'API_EXTENSION_NAMESPACE'
op|','
nl|'\n'
name|'check_func'
op|'='
name|'_check_load_extension'
op|','
nl|'\n'
name|'invoke_on_load'
op|'='
name|'True'
op|','
nl|'\n'
name|'invoke_kwds'
op|'='
op|'{'
string|'"extension_info"'
op|':'
name|'self'
op|'.'
name|'loaded_extension_info'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'='
name|'PlainMapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(cyeoh) Core API support is rewritten as extensions'
nl|'\n'
comment|'# but conceptually still have core'
nl|'\n'
name|'if'
name|'list'
op|'('
name|'self'
op|'.'
name|'api_extension_manager'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(cyeoh): Stevedore raises an exception if there are'
nl|'\n'
comment|'# no plugins detected. I wonder if this is a bug.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'api_extension_manager'
op|'.'
name|'map'
op|'('
name|'self'
op|'.'
name|'_register_resources'
op|','
nl|'\n'
name|'mapper'
op|'='
name|'mapper'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api_extension_manager'
op|'.'
name|'map'
op|'('
name|'self'
op|'.'
name|'_register_controllers'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'missing_core_extensions'
op|'='
name|'self'
op|'.'
name|'get_missing_core_extensions'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'loaded_extension_info'
op|'.'
name|'get_extensions'
op|'('
op|')'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'init_only'
name|'and'
name|'missing_core_extensions'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'critical'
op|'('
name|'_'
op|'('
string|'"Missing core API extensions: %s"'
op|')'
op|','
nl|'\n'
name|'missing_core_extensions'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'CoreAPIMissing'
op|'('
nl|'\n'
name|'missing_apis'
op|'='
name|'missing_core_extensions'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'APIRouterV3'
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
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_missing_core_extensions
name|'def'
name|'get_missing_core_extensions'
op|'('
name|'extensions_loaded'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'extensions_loaded'
op|'='
name|'set'
op|'('
name|'extensions_loaded'
op|')'
newline|'\n'
name|'missing_extensions'
op|'='
name|'API_V3_CORE_EXTENSIONS'
op|'-'
name|'extensions_loaded'
newline|'\n'
name|'return'
name|'list'
op|'('
name|'missing_extensions'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|loaded_extension_info
name|'def'
name|'loaded_extension_info'
op|'('
name|'self'
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
DECL|member|_register_extension
dedent|''
name|'def'
name|'_register_extension'
op|'('
name|'self'
op|','
name|'ext'
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
DECL|member|_register_resources
dedent|''
name|'def'
name|'_register_resources'
op|'('
name|'self'
op|','
name|'ext'
op|','
name|'mapper'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Register resources defined by the extensions\n\n        Extensions define what resources they want to add through a\n        get_resources function\n        """'
newline|'\n'
nl|'\n'
name|'handler'
op|'='
name|'ext'
op|'.'
name|'obj'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Running _register_resources on %s"'
op|')'
op|','
name|'ext'
op|'.'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'resource'
name|'in'
name|'handler'
op|'.'
name|'get_resources'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extended resource: %s'"
op|')'
op|','
name|'resource'
op|'.'
name|'collection'
op|')'
newline|'\n'
nl|'\n'
name|'inherits'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'resource'
op|'.'
name|'inherits'
op|':'
newline|'\n'
indent|'                '
name|'inherits'
op|'='
name|'self'
op|'.'
name|'resources'
op|'.'
name|'get'
op|'('
name|'resource'
op|'.'
name|'inherits'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'resource'
op|'.'
name|'controller'
op|':'
newline|'\n'
indent|'                    '
name|'resource'
op|'.'
name|'controller'
op|'='
name|'inherits'
op|'.'
name|'controller'
newline|'\n'
dedent|''
dedent|''
name|'wsgi_resource'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'resource'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'inherits'
op|'='
name|'inherits'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resources'
op|'['
name|'resource'
op|'.'
name|'collection'
op|']'
op|'='
name|'wsgi_resource'
newline|'\n'
name|'kargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'controller'
op|'='
name|'wsgi_resource'
op|','
nl|'\n'
name|'collection'
op|'='
name|'resource'
op|'.'
name|'collection_actions'
op|','
nl|'\n'
name|'member'
op|'='
name|'resource'
op|'.'
name|'member_actions'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'parent'
op|':'
newline|'\n'
indent|'                '
name|'kargs'
op|'['
string|"'parent_resource'"
op|']'
op|'='
name|'resource'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
comment|'# non core-API plugins use the collection name as the'
nl|'\n'
comment|'# member name, but the core-API plugins use the'
nl|'\n'
comment|'# singular/plural convention for member/collection names'
nl|'\n'
dedent|''
name|'if'
name|'resource'
op|'.'
name|'member_name'
op|':'
newline|'\n'
indent|'                '
name|'member_name'
op|'='
name|'resource'
op|'.'
name|'member_name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'member_name'
op|'='
name|'resource'
op|'.'
name|'collection'
newline|'\n'
dedent|''
name|'mapper'
op|'.'
name|'resource'
op|'('
name|'member_name'
op|','
name|'resource'
op|'.'
name|'collection'
op|','
nl|'\n'
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'resource'
op|'.'
name|'custom_routes_fn'
op|':'
newline|'\n'
indent|'                    '
name|'resource'
op|'.'
name|'custom_routes_fn'
op|'('
name|'mapper'
op|','
name|'wsgi_resource'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_register_controllers
dedent|''
dedent|''
dedent|''
name|'def'
name|'_register_controllers'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Register controllers defined by the extensions\n\n        Extensions define what resources they want to add through\n        a get_controller_extensions function\n        """'
newline|'\n'
nl|'\n'
name|'handler'
op|'='
name|'ext'
op|'.'
name|'obj'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Running _register_controllers on %s"'
op|')'
op|','
name|'ext'
op|'.'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'extension'
name|'in'
name|'handler'
op|'.'
name|'get_controller_extensions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ext_name'
op|'='
name|'extension'
op|'.'
name|'extension'
op|'.'
name|'name'
newline|'\n'
name|'collection'
op|'='
name|'extension'
op|'.'
name|'collection'
newline|'\n'
name|'controller'
op|'='
name|'extension'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
name|'if'
name|'collection'
name|'not'
name|'in'
name|'self'
op|'.'
name|'resources'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s: Cannot extend '"
nl|'\n'
string|"'resource %(collection)s: No such resource'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'ext_name'"
op|':'
name|'ext_name'
op|','
string|"'collection'"
op|':'
name|'collection'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Extension %(ext_name)s extending resource: '"
nl|'\n'
string|"'%(collection)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'ext_name'"
op|':'
name|'ext_name'
op|','
string|"'collection'"
op|':'
name|'collection'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'resource'
op|'='
name|'self'
op|'.'
name|'resources'
op|'['
name|'collection'
op|']'
newline|'\n'
name|'resource'
op|'.'
name|'register_actions'
op|'('
name|'controller'
op|')'
newline|'\n'
name|'resource'
op|'.'
name|'register_extensions'
op|'('
name|'controller'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
