begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
name|'webob'
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
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'external_event'
name|'as'
name|'external_event_obj'
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
nl|'\n'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'os-server-external-events'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EventTemplate
name|'class'
name|'EventTemplate'
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
string|"'events'"
op|')'
newline|'\n'
name|'elem1'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'event'"
op|','
name|'selector'
op|'='
string|"'events'"
op|')'
newline|'\n'
name|'elem2'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem1'
op|','
name|'xmlutil'
op|'.'
name|'Selector'
op|'('
number|'0'
op|')'
op|','
nl|'\n'
name|'selector'
op|'='
name|'xmlutil'
op|'.'
name|'get_items'
op|')'
newline|'\n'
name|'elem2'
op|'.'
name|'text'
op|'='
number|'1'
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
DECL|class|EventDeserializer
dedent|''
dedent|''
name|'class'
name|'EventDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
DECL|member|_extract_event
indent|'    '
name|'def'
name|'_extract_event'
op|'('
name|'self'
op|','
name|'event_node'
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
op|'('
string|"'name'"
op|','
string|"'tag'"
op|','
string|"'server_uuid'"
op|','
string|"'status'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'event_node'
op|','
name|'key'
op|')'
newline|'\n'
name|'event'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'event'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'events'
op|'='
op|'['
op|']'
newline|'\n'
name|'dom'
op|'='
name|'xmlutil'
op|'.'
name|'safe_minidom_parse_string'
op|'('
name|'string'
op|')'
newline|'\n'
name|'events_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'dom'
op|','
string|"'events'"
op|')'
newline|'\n'
name|'for'
name|'event_node'
name|'in'
name|'self'
op|'.'
name|'find_children_named'
op|'('
name|'events_node'
op|','
string|"'event'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'events'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_extract_event'
op|'('
name|'event_node'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'events'"
op|':'
name|'events'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerExternalEventsController
dedent|''
dedent|''
name|'class'
name|'ServerExternalEventsController'
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
name|'super'
op|'('
name|'ServerExternalEventsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'EventDeserializer'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'EventTemplate'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new instance event."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'create'"
op|')'
newline|'\n'
nl|'\n'
name|'events'
op|'='
op|'['
op|']'
newline|'\n'
name|'accepted'
op|'='
op|'['
op|']'
newline|'\n'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'result'
op|'='
number|'200'
newline|'\n'
nl|'\n'
name|'body_events'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'events'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'body_events'
op|','
name|'list'
op|')'
name|'or'
name|'not'
name|'len'
op|'('
name|'body_events'
op|')'
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
name|'for'
name|'_event'
name|'in'
name|'body_events'
op|':'
newline|'\n'
indent|'            '
name|'client_event'
op|'='
name|'dict'
op|'('
name|'_event'
op|')'
newline|'\n'
name|'event'
op|'='
name|'objects'
op|'.'
name|'InstanceExternalEvent'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'event'
op|'.'
name|'instance_uuid'
op|'='
name|'client_event'
op|'.'
name|'pop'
op|'('
string|"'server_uuid'"
op|')'
newline|'\n'
name|'event'
op|'.'
name|'name'
op|'='
name|'client_event'
op|'.'
name|'pop'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'event'
op|'.'
name|'status'
op|'='
name|'client_event'
op|'.'
name|'pop'
op|'('
string|"'status'"
op|','
string|"'completed'"
op|')'
newline|'\n'
name|'event'
op|'.'
name|'tag'
op|'='
name|'client_event'
op|'.'
name|'pop'
op|'('
string|"'tag'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
name|'as'
name|'missing_key'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'event entity requires key %(key)s'"
op|')'
op|'%'
name|'missing_key'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'client_event'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'event entity contains unsupported items: %s'"
op|')'
op|'%'
nl|'\n'
string|"', '"
op|'.'
name|'join'
op|'('
name|'client_event'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'event'
op|'.'
name|'status'
name|'not'
name|'in'
name|'external_event_obj'
op|'.'
name|'EVENT_STATUSES'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Invalid event status `%s\\''"
op|')'
op|'%'
name|'event'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'events'
op|'.'
name|'append'
op|'('
name|'_event'
op|')'
newline|'\n'
name|'if'
name|'event'
op|'.'
name|'instance_uuid'
name|'not'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'context'
op|','
name|'event'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'instances'
op|'['
name|'event'
op|'.'
name|'instance_uuid'
op|']'
op|'='
name|'instance'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Dropping event %(name)s:%(tag)s for unknown '"
nl|'\n'
string|"'instance %(instance_uuid)s'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'event'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'_event'
op|'['
string|"'status'"
op|']'
op|'='
string|"'failed'"
newline|'\n'
name|'_event'
op|'['
string|"'code'"
op|']'
op|'='
number|'404'
newline|'\n'
name|'result'
op|'='
number|'207'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'event'
op|'.'
name|'instance_uuid'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'                '
name|'accepted'
op|'.'
name|'append'
op|'('
name|'event'
op|')'
newline|'\n'
name|'_event'
op|'['
string|"'code'"
op|']'
op|'='
number|'200'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Create event %(name)s:%(tag)s for instance '"
nl|'\n'
string|"'%(instance_uuid)s'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'event'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'accepted'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'external_instance_event'
op|'('
name|'context'
op|','
nl|'\n'
name|'instances'
op|'.'
name|'values'
op|'('
op|')'
op|','
nl|'\n'
name|'accepted'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'No instances found for any event'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(cyeoh): This needs some infrastructure support so that'
nl|'\n'
comment|'# we have a general way to do this'
nl|'\n'
dedent|''
name|'robj'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
op|'{'
string|"'events'"
op|':'
name|'events'
op|'}'
op|')'
newline|'\n'
name|'robj'
op|'.'
name|'_code'
op|'='
name|'result'
newline|'\n'
name|'return'
name|'robj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Server_external_events
dedent|''
dedent|''
name|'class'
name|'Server_external_events'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server External Event Triggers."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ServerExternalEvents"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-server-external-events"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"server-external-events/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2014-02-18T00:00:00Z"'
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
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-server-external-events'"
op|','
nl|'\n'
name|'ServerExternalEventsController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'resource'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
