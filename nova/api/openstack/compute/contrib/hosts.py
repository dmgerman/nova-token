begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'hosts'"
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
DECL|class|HostUpdateDeserializer
dedent|''
dedent|''
name|'class'
name|'HostUpdateDeserializer'
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
name|'node'
op|'='
name|'xmlutil'
op|'.'
name|'safe_minidom_parse_string'
op|'('
name|'string'
op|')'
newline|'\n'
nl|'\n'
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'updates_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'updates'"
op|')'
newline|'\n'
name|'if'
name|'updates_node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'maintenance'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'updates_node'
op|','
nl|'\n'
string|"'maintenance_mode'"
op|')'
newline|'\n'
name|'if'
name|'maintenance'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'maintenance'
op|'.'
name|'tagName'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'maintenance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'status'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'updates_node'
op|','
string|"'status'"
op|')'
newline|'\n'
name|'if'
name|'status'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'status'
op|'.'
name|'tagName'
op|']'
op|'='
name|'self'
op|'.'
name|'extract_text'
op|'('
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
DECL|class|HostController
dedent|''
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
name|'compute'
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
string|'"""\n        :returns: A dict in the format:\n\n            {\'hosts\': [{\'host_name\': \'some.host.name\',\n               \'service\': \'cells\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'some.other.host.name\',\n               \'service\': \'cells\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'some.celly.host.name\',\n               \'service\': \'cells\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'console1.host.com\',\n               \'service\': \'consoleauth\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'network1.host.com\',\n               \'service\': \'network\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'netwwork2.host.com\',\n               \'service\': \'network\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'compute1.host.com\',\n               \'service\': \'compute\',\n               \'zone\': \'nova\'},\n              {\'host_name\': \'compute2.host.com\',\n               \'service\': \'compute\',\n               \'zone\': \'nova\'},\n              {\'host_name\': \'sched1.host.com\',\n               \'service\': \'scheduler\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'sched2.host.com\',\n               \'service\': \'scheduler\',\n               \'zone\': \'internal\'},\n              {\'host_name\': \'vol1.host.com\',\n               \'service\': \'volume\'},\n               \'zone\': \'internal\']}\n        """'
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
name|'filters'
op|'='
op|'{'
string|"'disabled'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'zone'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'zone'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'zone'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'zone'
newline|'\n'
dedent|''
name|'services'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|','
nl|'\n'
name|'set_zones'
op|'='
name|'True'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'hosts'
op|'.'
name|'append'
op|'('
op|'{'
string|"'host_name'"
op|':'
name|'service'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
op|'['
string|"'topic'"
op|']'
op|','
nl|'\n'
string|"'zone'"
op|':'
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'hosts'"
op|':'
name|'hosts'
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
name|'HostUpdateDeserializer'
op|')'
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
string|'"""\n        :param body: example format {\'status\': \'enable\',\n                                     \'maintenance_mode\': \'enable\'}\n        :returns:\n        """'
newline|'\n'
DECL|function|read_enabled
name|'def'
name|'read_enabled'
op|'('
name|'orig_val'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""\n            :param orig_val: A string with either \'enable\' or \'disable\'. May\n                             be surrounded by whitespace, and case doesn\'t\n                             matter\n            :param msg: The message to be passed to HTTPBadRequest. A single\n                        %s will be replaced with orig_val.\n            :returns:   True for \'enabled\' and False for \'disabled\'\n            """'
newline|'\n'
name|'val'
op|'='
name|'orig_val'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
name|'val'
op|'=='
string|'"enable"'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'val'
op|'=='
string|'"disable"'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
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
name|'explanation'
op|'='
name|'msg'
op|'%'
name|'orig_val'
op|')'
newline|'\n'
dedent|''
dedent|''
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
comment|"# See what the user wants to 'update'"
nl|'\n'
name|'params'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'body'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'orig_status'
op|'='
name|'status'
op|'='
name|'params'
op|'.'
name|'pop'
op|'('
string|"'status'"
op|','
name|'None'
op|')'
newline|'\n'
name|'orig_maint_mode'
op|'='
name|'maint_mode'
op|'='
name|'params'
op|'.'
name|'pop'
op|'('
string|"'maintenance_mode'"
op|','
name|'None'
op|')'
newline|'\n'
comment|'# Validate the request'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'params'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
comment|'# Some extra param was passed. Fail.'
nl|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid update setting: \'%s\'"'
op|')'
op|'%'
name|'params'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
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
name|'if'
name|'orig_status'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
name|'read_enabled'
op|'('
name|'orig_status'
op|','
name|'_'
op|'('
string|'"Invalid status: \'%s\'"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'orig_maint_mode'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'maint_mode'
op|'='
name|'read_enabled'
op|'('
name|'orig_maint_mode'
op|','
name|'_'
op|'('
string|'"Invalid mode: \'%s\'"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'status'
name|'is'
name|'None'
name|'and'
name|'maint_mode'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"\'status\' or \'maintenance_mode\' needed for "'
nl|'\n'
string|'"host update"'
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
name|'explanation'
op|')'
newline|'\n'
comment|'# Make the calls and merge the results'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'{'
string|"'host'"
op|':'
name|'id'
op|'}'
newline|'\n'
name|'if'
name|'status'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'['
string|"'status'"
op|']'
op|'='
name|'self'
op|'.'
name|'_set_enabled_status'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'status'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'maint_mode'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'['
string|"'maintenance_mode'"
op|']'
op|'='
name|'self'
op|'.'
name|'_set_host_maintenance'
op|'('
name|'context'
op|','
nl|'\n'
name|'id'
op|','
name|'maint_mode'
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
name|'context'
op|','
name|'host_name'
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
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Putting host %(host_name)s in maintenance "'
nl|'\n'
string|'"mode %(mode)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'set_host_maintenance'
op|'('
name|'context'
op|','
name|'host_name'
op|','
name|'mode'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Virt driver does not implement host maintenance mode."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
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
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_set_enabled_status
dedent|''
name|'def'
name|'_set_enabled_status'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the specified host\'s ability to accept new instances.\n        :param enabled: a boolean - if False no new VMs will be able to start\n        on the host"""'
newline|'\n'
name|'if'
name|'enabled'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Enabling host %s."'
op|')'
op|'%'
name|'host_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Disabling host %s."'
op|')'
op|'%'
name|'host_name'
op|')'
newline|'\n'
dedent|''
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
name|'set_host_enabled'
op|'('
name|'context'
op|','
name|'host_name'
op|'='
name|'host_name'
op|','
nl|'\n'
name|'enabled'
op|'='
name|'enabled'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Virt driver does not implement host disabled status."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
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
name|'result'
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
name|'host_name'
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
name|'host_name'
op|'='
name|'host_name'
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
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Virt driver does not implement host power management."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"host"'
op|':'
name|'host_name'
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
name|'host_name'
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
name|'host_name'
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
name|'host_name'
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
name|'staticmethod'
newline|'\n'
DECL|member|_get_total_resources
name|'def'
name|'_get_total_resources'
op|'('
name|'host_name'
op|','
name|'compute_node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host_name'
op|','
nl|'\n'
string|"'project'"
op|':'
string|"'(total)'"
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'compute_node'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_node'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'compute_node'
op|'['
string|"'local_gb'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_used_now_resources
name|'def'
name|'_get_used_now_resources'
op|'('
name|'host_name'
op|','
name|'compute_node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host_name'
op|','
nl|'\n'
string|"'project'"
op|':'
string|"'(used_now)'"
op|','
nl|'\n'
string|"'cpu'"
op|':'
name|'compute_node'
op|'['
string|"'vcpus_used'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_node'
op|'['
string|"'memory_mb_used'"
op|']'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'compute_node'
op|'['
string|"'local_gb_used'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_resource_totals_from_instances
name|'def'
name|'_get_resource_totals_from_instances'
op|'('
name|'host_name'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'cpu_sum'
op|'+='
name|'instance'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'mem_sum'
op|'+='
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'hdd_sum'
op|'+='
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'resource'"
op|':'
op|'{'
string|"'host'"
op|':'
name|'host_name'
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
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_resources_by_project
name|'def'
name|'_get_resources_by_project'
op|'('
name|'host_name'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
comment|'# Getting usage resource per project'
nl|'\n'
indent|'        '
name|'project_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'resource'
op|'='
name|'project_map'
op|'.'
name|'setdefault'
op|'('
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'host_name'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'cpu'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'resource'
op|'['
string|"'cpu'"
op|']'
op|'+='
name|'instance'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'resource'
op|'['
string|"'memory_mb'"
op|']'
op|'+='
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'resource'
op|'['
string|"'disk_gb'"
op|']'
op|'+='
op|'('
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'+'
nl|'\n'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'project_map'
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
string|'"""Shows the physical/usage resource given by hosts.\n\n        :param id: hostname\n        :returns: expected to use HostShowTemplate.\n            ex.::\n\n                {\'host\': {\'resource\':D},..}\n                D: {\'host\': \'hostname\',\'project\': \'admin\',\n                    \'cpu\': 1, \'memory_mb\': 2048, \'disk_gb\': 30}\n        """'
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
name|'host_name'
op|'='
name|'id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
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
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AdminRequired'
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
dedent|''
name|'compute_node'
op|'='
name|'service'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host_name'
op|')'
newline|'\n'
name|'resources'
op|'='
op|'['
name|'self'
op|'.'
name|'_get_total_resources'
op|'('
name|'host_name'
op|','
name|'compute_node'
op|')'
op|']'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_get_used_now_resources'
op|'('
name|'host_name'
op|','
nl|'\n'
name|'compute_node'
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_get_resource_totals_from_instances'
op|'('
name|'host_name'
op|','
nl|'\n'
name|'instances'
op|')'
op|')'
newline|'\n'
name|'by_proj_resources'
op|'='
name|'self'
op|'.'
name|'_get_resources_by_project'
op|'('
name|'host_name'
op|','
nl|'\n'
name|'instances'
op|')'
newline|'\n'
name|'for'
name|'resource'
name|'in'
name|'by_proj_resources'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'.'
name|'append'
op|'('
op|'{'
string|"'resource'"
op|':'
name|'resource'
op|'}'
op|')'
newline|'\n'
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
string|'"""Admin-only host administration."""'
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
