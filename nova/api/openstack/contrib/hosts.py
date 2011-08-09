begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
name|'import'
name|'admin_only'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'api'
name|'as'
name|'scheduler_api'
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
string|'"nova.api.hosts"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_list_hosts
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
name|'hosts'
op|'='
name|'scheduler_api'
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
name|'raise'
name|'exception'
op|'.'
name|'HostNotFound'
op|'('
name|'host'
op|'='
name|'id'
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
DECL|member|index
dedent|''
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
comment|"# NOTE: (dabo) Right now only 'status' can be set, but other"
nl|'\n'
comment|'# settings may follow.'
nl|'\n'
name|'if'
name|'key'
op|'=='
string|'"status"'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'val'
op|'['
op|':'
number|'6'
op|']'
name|'in'
op|'('
string|'"enable"'
op|','
string|'"disabl"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'self'
op|'.'
name|'_set_enabled_status'
op|'('
name|'req'
op|','
name|'id'
op|','
nl|'\n'
name|'enabled'
op|'='
op|'('
name|'val'
op|'.'
name|'startswith'
op|'('
string|'"enable"'
op|')'
op|')'
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
DECL|member|_set_enabled_status
dedent|''
dedent|''
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
name|'compute_api'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'compute_api'
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
DECL|member|startup
dedent|''
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
DECL|member|shutdown
dedent|''
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
DECL|member|reboot
dedent|''
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
DECL|member|get_name
indent|'    '
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Hosts"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"os-hosts"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Host administration"'
newline|'\n'
nl|'\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://docs.openstack.org/ext/hosts/api/v1.1"'
newline|'\n'
nl|'\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"2011-06-29T00:00:00+00:00"'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'admin_only'
op|'.'
name|'admin_only'
newline|'\n'
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
