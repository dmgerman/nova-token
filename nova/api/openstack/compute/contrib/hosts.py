begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""The hosts admin extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'parsers'
name|'import'
name|'expat'
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
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
op|'.'
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
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
string|"'hosts'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostIndexTemplate
name|'class'
name|'HostIndexTemplate'
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
DECL|function|shimmer
indent|'        '
name|'def'
name|'shimmer'
op|'('
name|'obj'
op|','
name|'do_raise'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# A bare list is passed in; we need to wrap it in a dict'
nl|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'hosts'
op|'='
name|'obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'hosts'"
op|','
name|'selector'
op|'='
name|'shimmer'
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
string|"'host'"
op|','
name|'selector'
op|'='
string|"'hosts'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'host_name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'service'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|class|HostUpdateTemplate
dedent|''
dedent|''
name|'class'
name|'HostUpdateTemplate'
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
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'maintenance_mode'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|class|HostActionTemplate
dedent|''
dedent|''
name|'class'
name|'HostActionTemplate'
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
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'power_action'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|class|HostShowTemplate
dedent|''
dedent|''
name|'class'
name|'HostShowTemplate'
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
string|"'host'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'make_flat_dict'
op|'('
string|"'resource'"
op|','
name|'selector'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'subselector'
op|'='
string|"'resource'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'elem'
op|')'
newline|'\n'
nl|'\n'
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
DECL|class|HostDeserializer
dedent|''
dedent|''
name|'class'
name|'HostDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|')'
op|':'
newline|'\n'
DECL|member|default
indent|'    '
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'string'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'expat'
op|'.'
name|'ExpatError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"cannot understand XML"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MalformedRequestBody'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
name|'child'
op|'.'
name|'tagName'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'child'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'body'
op|'='
name|'updates'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_list_hosts
dedent|''
dedent|''
name|'def'
name|'_list_hosts'
op|'('
name|'req'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a summary list of hosts, optionally filtering\n    by service type.\n    """'
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
name|'rpcapi'
op|'='
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'rpcapi'
op|'.'
name|'get_host_list'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'service'
op|':'
newline|'\n'
indent|'        '
name|'hosts'
op|'='
op|'['
name|'host'
name|'for'
name|'host'
name|'in'
name|'hosts'
nl|'\n'
name|'if'
name|'host'
op|'['
string|'"service"'
op|']'
op|'=='
name|'service'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'hosts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_host
dedent|''
name|'def'
name|'check_host'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Makes sure that the host exists."""'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'service'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'listed_hosts'
op|'='
name|'_list_hosts'
op|'('
name|'req'
op|','
name|'service'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
name|'h'
op|'['
string|'"host_name"'
op|']'
name|'for'
name|'h'
name|'in'
name|'listed_hosts'
op|']'
newline|'\n'
name|'if'
name|'id'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fn'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
name|'_'
op|'('
string|'"Host \'%s\' could not be found."'
op|')'
op|'%'
name|'id'
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
name|'message'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostController
dedent|''
name|'class'
name|'HostController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Hosts API controller for the OpenStack API."""'
newline|'\n'
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
name|'api'
op|'='
name|'compute_api'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'HostController'
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
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostIndexTemplate'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'authorize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'hosts'"
op|':'
name|'_list_hosts'
op|'('
name|'req'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostUpdateTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'HostDeserializer'
op|')'
newline|'\n'
op|'@'
name|'check_host'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'authorize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'update_values'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'raw_key'
op|','
name|'raw_val'
name|'in'
name|'body'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'raw_key'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'val'
op|'='
name|'raw_val'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'key'
op|'=='
string|'"status"'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'val'
name|'in'
op|'('
string|'"enable"'
op|','
string|'"disable"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'update_values'
op|'['
string|"'status'"
op|']'
op|'='
name|'val'
op|'.'
name|'startswith'
op|'('
string|'"enable"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid status: \'%s\'"'
op|')'
op|'%'
name|'raw_val'
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
name|'explanation'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'key'
op|'=='
string|'"maintenance_mode"'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'val'
name|'not'
name|'in'
op|'['
string|"'enable'"
op|','
string|"'disable'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid mode: \'%s\'"'
op|')'
op|'%'
name|'raw_val'
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
name|'explanation'
op|')'
newline|'\n'
dedent|''
name|'update_values'
op|'['
string|"'maintenance_mode'"
op|']'
op|'='
name|'val'
op|'=='
string|"'enable'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid update setting: \'%s\'"'
op|')'
op|'%'
name|'raw_key'
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
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
comment|'# this is for handling multiple settings at the same time:'
nl|'\n'
comment|'# the result dictionaries are merged in the first one.'
nl|'\n'
comment|"# Note: the 'host' key will always be the same so it's"
nl|'\n'
comment|'# okay that it gets overwritten.'
nl|'\n'
dedent|''
dedent|''
name|'update_setters'
op|'='
op|'{'
string|"'status'"
op|':'
name|'self'
op|'.'
name|'_set_enabled_status'
op|','
nl|'\n'
string|"'maintenance_mode'"
op|':'
name|'self'
op|'.'
name|'_set_host_maintenance'
op|'}'
newline|'\n'
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'update_values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'update'
op|'('
name|'update_setters'
op|'['
name|'key'
op|']'
op|'('
name|'req'
op|','
name|'id'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_set_host_maintenance
dedent|''
name|'def'
name|'_set_host_maintenance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'host'
op|','
name|'mode'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start/Stop host maintenance window. On start, it triggers\n        guest VMs evacuation."""'
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
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Putting host %(host)s in maintenance "'
nl|'\n'
string|'"mode %(mode)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'set_host_maintenance'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'mode'
op|')'
newline|'\n'
name|'if'
name|'result'
name|'not'
name|'in'
op|'('
string|'"on_maintenance"'
op|','
string|'"off_maintenance"'
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
name|'explanation'
op|'='
name|'result'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"host"'
op|':'
name|'host'
op|','
string|'"maintenance_mode"'
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_set_enabled_status
dedent|''
name|'def'
name|'_set_enabled_status'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the specified host\'s ability to accept new instances."""'
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
name|'state'
op|'='
string|'"enabled"'
name|'if'
name|'enabled'
name|'else'
string|'"disabled"'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Setting host %(host)s to %(state)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'set_host_enabled'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'enabled'
op|'='
name|'enabled'
op|')'
newline|'\n'
name|'if'
name|'result'
name|'not'
name|'in'
op|'('
string|'"enabled"'
op|','
string|'"disabled"'
op|')'
op|':'
newline|'\n'
comment|'# An error message was returned'
nl|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'result'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"host"'
op|':'
name|'host'
op|','
string|'"status"'
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_host_power_action
dedent|''
name|'def'
name|'_host_power_action'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboots, shuts down or powers up the host."""'
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
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'host_power_action'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'action'
op|'='
name|'action'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
name|'as'
name|'e'
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
name|'explanation'
op|'='
name|'e'
op|'.'
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"host"'
op|':'
name|'host'
op|','
string|'"power_action"'
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostActionTemplate'
op|')'
newline|'\n'
DECL|member|startup
name|'def'
name|'startup'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_host_power_action'
op|'('
name|'req'
op|','
name|'host'
op|'='
name|'id'
op|','
name|'action'
op|'='
string|'"startup"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostActionTemplate'
op|')'
newline|'\n'
DECL|member|shutdown
name|'def'
name|'shutdown'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_host_power_action'
op|'('
name|'req'
op|','
name|'host'
op|'='
name|'id'
op|','
name|'action'
op|'='
string|'"shutdown"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostActionTemplate'
op|')'
newline|'\n'
DECL|member|reboot
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_host_power_action'
op|'('
name|'req'
op|','
name|'host'
op|'='
name|'id'
op|','
name|'action'
op|'='
string|'"reboot"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'HostShowTemplate'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shows the physical/usage resource given by hosts.\n\n        :param context: security context\n        :param host: hostname\n        :returns: expected to use HostShowTemplate.\n            ex.::\n\n                {\'host\': {\'resource\':D},..}\n                D: {\'host\': \'hostname\',\'project\': \'admin\',\n                    \'cpu\': 1, \'memory_mb\': 2048, \'disk_gb\': 30}\n        """'
newline|'\n'
name|'host'
op|'='
name|'id'
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
name|'if'
name|'not'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Describe-resource is admin only functionality"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting compute node info and related instances info'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'compute_ref'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'compute_ref'
op|'='
name|'compute_ref'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
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
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Host not found"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'compute_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting total available/used resource'
nl|'\n'
name|'compute_ref'
op|'='
name|'compute_ref'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'resources'
op|'='
op|'['
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'project'"
op|':'
string|"'(total)'"
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb'"
op|']'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'project'"
op|':'
string|"'(used_now)'"
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus_used'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb_used'"
op|']'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb_used'"
op|']'
op|'}'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'cpu_sum'
op|'='
number|'0'
newline|'\n'
name|'mem_sum'
op|'='
number|'0'
newline|'\n'
name|'hdd_sum'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|':'
newline|'\n'
indent|'            '
name|'cpu_sum'
op|'+='
name|'i'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'mem_sum'
op|'+='
name|'i'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'hdd_sum'
op|'+='
name|'i'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'i'
op|'['
string|"'ephemeral_gb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'resources'
op|'.'
name|'append'
op|'('
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'project'"
op|':'
string|"'(used_max)'"
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'cpu_sum'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'mem_sum'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'hdd_sum'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting usage resource per project'
nl|'\n'
name|'project_ids'
op|'='
op|'['
name|'i'
op|'['
string|"'project_id'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|']'
newline|'\n'
name|'project_ids'
op|'='
name|'list'
op|'('
name|'set'
op|'('
name|'project_ids'
op|')'
op|')'
newline|'\n'
name|'for'
name|'project_id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'vcpus'
op|'='
op|'['
name|'i'
op|'['
string|"'vcpus'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'mem'
op|'='
op|'['
name|'i'
op|'['
string|"'memory_mb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'disk'
op|'='
op|'['
name|'i'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'i'
op|'['
string|"'ephemeral_gb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
nl|'\n'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'project_id'
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'reduce'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'+'
name|'y'
op|','
name|'vcpus'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'reduce'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'+'
name|'y'
op|','
name|'mem'
op|')'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'reduce'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'+'
name|'y'
op|','
name|'disk'
op|')'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'host'"
op|':'
name|'resources'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Hosts
dedent|''
dedent|''
name|'class'
name|'Hosts'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only host administration"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Hosts"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-hosts"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/hosts/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-06-29T00:00:00+00:00"'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-hosts'"
op|','
nl|'\n'
name|'HostController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'update'"
op|':'
string|"'PUT'"
op|'}'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|'"startup"'
op|':'
string|'"GET"'
op|','
string|'"shutdown"'
op|':'
string|'"GET"'
op|','
nl|'\n'
string|'"reboot"'
op|':'
string|'"GET"'
op|'}'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
