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
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'hosts'
newline|'\n'
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
name|'import'
name|'validation'
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
name|'import'
name|'objects'
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
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-hosts'"
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
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostController
name|'class'
name|'HostController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
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
string|'"""Returns a dict in the format\n\n        |   {\'hosts\': [{\'host_name\': \'some.host.name\',\n        |     \'service\': \'cells\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'some.other.host.name\',\n        |     \'service\': \'cells\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'some.celly.host.name\',\n        |     \'service\': \'cells\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'console1.host.com\',\n        |     \'service\': \'consoleauth\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'network1.host.com\',\n        |     \'service\': \'network\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'netwwork2.host.com\',\n        |     \'service\': \'network\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'compute1.host.com\',\n        |     \'service\': \'compute\',\n        |     \'zone\': \'nova\'},\n        |    {\'host_name\': \'compute2.host.com\',\n        |     \'service\': \'compute\',\n        |     \'zone\': \'nova\'},\n        |    {\'host_name\': \'sched1.host.com\',\n        |     \'service\': \'scheduler\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'sched2.host.com\',\n        |     \'service\': \'scheduler\',\n        |     \'zone\': \'internal\'},\n        |    {\'host_name\': \'vol1.host.com\',\n        |     \'service\': \'volume\',\n        |     \'zone\': \'internal\'}]}\n\n        """'
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
name|'service'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'service'"
op|')'
newline|'\n'
name|'if'
name|'service'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'['
string|"'topic'"
op|']'
op|'='
name|'service'
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'hosts'
op|'.'
name|'update'
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
string|'""":param body: example format {\'status\': \'enable\',\n                                     \'maintenance_mode\': \'enable\'}\n           :returns:\n        """'
newline|'\n'
DECL|function|read_enabled
name|'def'
name|'read_enabled'
op|'('
name|'orig_val'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'""":param orig_val: A string with either \'enable\' or \'disable\'. May\n                                be surrounded by whitespace, and case doesn\'t\n                                matter\n               :returns: True for \'enabled\' and False for \'disabled\'\n            """'
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
name|'return'
name|'val'
op|'=='
string|'"enable"'
newline|'\n'
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
name|'status'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'maint_mode'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'maintenance_mode'"
op|')'
newline|'\n'
name|'if'
name|'status'
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
name|'maint_mode'
op|'='
name|'read_enabled'
op|'('
name|'maint_mode'
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
nl|'\n'
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
string|'"""Start/Stop host maintenance window. On start, it triggers\n        guest VMs evacuation.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Putting host %(host_name)s in maintenance mode "'
nl|'\n'
string|'"%(mode)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host_name'"
op|':'
name|'host_name'
op|','
string|"'mode'"
op|':'
name|'mode'
op|'}'
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
name|'HostNotFound'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
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
name|'format_message'
op|'('
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
string|'"""Sets the specified host\'s ability to accept new instances.\n        :param enabled: a boolean - if False no new VMs will be able to start\n                        on the host.\n        """'
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
op|','
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
op|','
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
name|'HostNotFound'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
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
name|'format_message'
op|'('
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
name|'HostNotFound'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
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
name|'format_message'
op|'('
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'501'
op|')'
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'501'
op|')'
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'501'
op|')'
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
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'403'
op|','
number|'404'
op|')'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'host_name'
op|'='
name|'id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
op|'='
op|'('
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_first_node_by_host_for_old_compat'
op|'('
nl|'\n'
name|'context'
op|','
name|'host_name'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
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
name|'e'
op|'.'
name|'format_message'
op|'('
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
comment|'# TODO(Alex Xu): The authorization is done by policy,'
nl|'\n'
comment|'# db layer checking is needless. The db layer checking should'
nl|'\n'
comment|'# be removed'
nl|'\n'
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
name|'V3APIExtensionBase'
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
name|'ALIAS'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'HostController'
op|'('
op|')'
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
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
