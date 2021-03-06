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
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
DECL|class|ServerExternalEventsController
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
DECL|member|create
dedent|''
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
name|'response_events'
op|'='
op|'['
op|']'
newline|'\n'
name|'accepted_events'
op|'='
op|'['
op|']'
newline|'\n'
name|'accepted_instances'
op|'='
name|'set'
op|'('
op|')'
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
name|'status'
op|'='
name|'client_event'
op|'.'
name|'get'
op|'('
string|"'status'"
op|','
string|"'completed'"
op|')'
newline|'\n'
name|'if'
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
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'client_event'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
name|'not'
name|'in'
name|'external_event_obj'
op|'.'
name|'EVENT_NAMES'
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
string|"'Invalid event name %s'"
op|')'
op|'%'
name|'client_event'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'instance'
op|'='
name|'instances'
op|'.'
name|'get'
op|'('
name|'event'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
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
op|'{'
string|"'name'"
op|':'
name|'event'
op|'.'
name|'name'
op|','
string|"'tag'"
op|':'
name|'event'
op|'.'
name|'tag'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'event'
op|'.'
name|'instance_uuid'
op|'}'
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
comment|'# NOTE: before accepting the event, make sure the instance'
nl|'\n'
comment|'# for which the event is sent is assigned to a host; otherwise'
nl|'\n'
comment|'# it will not be possible to dispatch the event'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'instance'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                    '
name|'accepted_events'
op|'.'
name|'append'
op|'('
name|'event'
op|')'
newline|'\n'
name|'accepted_instances'
op|'.'
name|'add'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Creating event %(name)s:%(tag)s for '"
nl|'\n'
string|"'instance %(instance_uuid)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
name|'event'
op|'.'
name|'name'
op|','
string|"'tag'"
op|':'
name|'event'
op|'.'
name|'tag'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'event'
op|'.'
name|'instance_uuid'
op|'}'
op|')'
newline|'\n'
comment|'# NOTE: as the event is processed asynchronously verify'
nl|'\n'
comment|'# whether 202 is a more suitable response code than 200'
nl|'\n'
name|'_event'
op|'['
string|"'status'"
op|']'
op|'='
string|"'completed'"
newline|'\n'
name|'_event'
op|'['
string|"'code'"
op|']'
op|'='
number|'200'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Unable to find a host for instance "'
nl|'\n'
string|'"%(instance)s. Dropping event %(event)s"'
op|','
nl|'\n'
op|'{'
string|"'instance'"
op|':'
name|'event'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
string|"'event'"
op|':'
name|'event'
op|'.'
name|'name'
op|'}'
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
number|'422'
newline|'\n'
name|'result'
op|'='
number|'207'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'response_events'
op|'.'
name|'append'
op|'('
name|'_event'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'accepted_events'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'external_instance_event'
op|'('
nl|'\n'
name|'context'
op|','
name|'accepted_instances'
op|','
name|'accepted_events'
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
name|'response_events'
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
