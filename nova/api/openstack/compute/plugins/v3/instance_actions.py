begin_unit
comment|'# Copyright 2013 Rackspace Hosting'
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
name|'from'
name|'webob'
name|'import'
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
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-instance-actions"'
newline|'\n'
DECL|variable|authorize_actions
name|'authorize_actions'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_events
name|'authorize_events'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:'"
op|'+'
name|'ALIAS'
op|'+'
string|"':events'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ACTION_KEYS
name|'ACTION_KEYS'
op|'='
op|'['
string|"'action'"
op|','
string|"'instance_uuid'"
op|','
string|"'request_id'"
op|','
string|"'user_id'"
op|','
nl|'\n'
string|"'project_id'"
op|','
string|"'start_time'"
op|','
string|"'message'"
op|']'
newline|'\n'
DECL|variable|EVENT_KEYS
name|'EVENT_KEYS'
op|'='
op|'['
string|"'event'"
op|','
string|"'start_time'"
op|','
string|"'finish_time'"
op|','
string|"'result'"
op|','
string|"'traceback'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_actions
name|'def'
name|'make_actions'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'key'
name|'in'
name|'ACTION_KEYS'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'.'
name|'set'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_action
dedent|''
dedent|''
name|'def'
name|'make_action'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'key'
name|'in'
name|'ACTION_KEYS'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'.'
name|'set'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'event'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'events'"
op|','
name|'selector'
op|'='
string|"'events'"
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'EVENT_KEYS'
op|':'
newline|'\n'
indent|'        '
name|'event'
op|'.'
name|'set'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'elem'
op|'.'
name|'append'
op|'('
name|'event'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionsTemplate
dedent|''
name|'class'
name|'InstanceActionsTemplate'
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
string|"'instance_actions'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'instance_action'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'instance_actions'"
op|')'
newline|'\n'
name|'make_actions'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionTemplate
dedent|''
dedent|''
name|'class'
name|'InstanceActionTemplate'
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
string|"'instance_action'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'instance_action'"
op|')'
newline|'\n'
name|'make_action'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionsController
dedent|''
dedent|''
name|'class'
name|'InstanceActionsController'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'InstanceActionsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'action_api'
op|'='
name|'compute'
op|'.'
name|'InstanceActionAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_action
dedent|''
name|'def'
name|'_format_action'
op|'('
name|'self'
op|','
name|'action_raw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'ACTION_KEYS'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'['
name|'key'
op|']'
op|'='
name|'action_raw'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'action'
newline|'\n'
nl|'\n'
DECL|member|_format_event
dedent|''
name|'def'
name|'_format_event'
op|'('
name|'self'
op|','
name|'event_raw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'event'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'EVENT_KEYS'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'['
name|'key'
op|']'
op|'='
name|'event_raw'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'event'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'InstanceActionsTemplate'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of actions recorded for a given instance."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'err'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'authorize_actions'
op|'('
name|'context'
op|','
name|'target'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'actions_raw'
op|'='
name|'self'
op|'.'
name|'action_api'
op|'.'
name|'actions_get'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'actions'
op|'='
op|'['
name|'self'
op|'.'
name|'_format_action'
op|'('
name|'action'
op|')'
name|'for'
name|'action'
name|'in'
name|'actions_raw'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'instance_actions'"
op|':'
name|'actions'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'InstanceActionTemplate'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given instance action."""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'err'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'authorize_actions'
op|'('
name|'context'
op|','
name|'target'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'action_api'
op|'.'
name|'action_get_by_request_id'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'id'
op|')'
newline|'\n'
name|'if'
name|'action'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Action %s not found"'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'action_id'
op|'='
name|'action'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'_format_action'
op|'('
name|'action'
op|')'
newline|'\n'
name|'if'
name|'authorize_events'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'events_raw'
op|'='
name|'self'
op|'.'
name|'action_api'
op|'.'
name|'action_events_get'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'action_id'
op|')'
newline|'\n'
name|'action'
op|'['
string|"'events'"
op|']'
op|'='
op|'['
name|'self'
op|'.'
name|'_format_event'
op|'('
name|'evt'
op|')'
name|'for'
name|'evt'
name|'in'
name|'events_raw'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'instance_action'"
op|':'
name|'action'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActions
dedent|''
dedent|''
name|'class'
name|'InstanceActions'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""View a log of actions and events taken on an instance."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"InstanceActions"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"instance-actions/api/v3"'
op|')'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-instance-actions'"
op|','
nl|'\n'
name|'InstanceActionsController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
nl|'\n'
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
name|'return'
op|'['
name|'ext'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""It\'s an abstract function V3APIExtensionBase and the extension\n        will not be loaded without it.\n        """'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
