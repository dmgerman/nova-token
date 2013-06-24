begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, 2013 IBM Corp.'
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
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-fixed-ips"'
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
DECL|class|FixedIPController
name|'class'
name|'FixedIPController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
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
string|'"""Return data about the given fixed ip."""'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address_detailed'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
name|'as'
name|'ex'
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
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fixed_ip_info'
op|'='
op|'{'
string|'"fixed_ip"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP %s has been deleted"'
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
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'fixed_ip'
op|'['
number|'1'
op|']'
op|'['
string|"'cidr'"
op|']'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'address'"
op|']'
op|'='
name|'fixed_ip'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'fixed_ip'
op|'['
number|'2'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'fixed_ip'
op|'['
number|'2'
op|']'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'host'"
op|']'
op|'='
name|'fixed_ip'
op|'['
number|'2'
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'hostname'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'fixed_ip_info'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'host'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fixed_ip_info'
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
op|')'
op|')'
newline|'\n'
DECL|member|action
name|'def'
name|'action'
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
name|'if'
string|"'reserve'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reserving IP address %s"'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_set_reserved'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'unreserve'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Unreserving IP address %s"'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_set_reserved'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
name|'else'
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
nl|'\n'
name|'explanation'
op|'='
string|'"No valid action specified"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_reserved
dedent|''
dedent|''
name|'def'
name|'_set_reserved'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'reserved'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'reserved'"
op|':'
name|'reserved'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP %s not found"'
op|')'
op|'%'
name|'address'
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
dedent|''
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIPs
dedent|''
dedent|''
name|'class'
name|'FixedIPs'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixed IPs support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FixedIPs"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/fixed_ips/api/v3"'
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
name|'member_actions'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
newline|'\n'
name|'resources'
op|'='
op|'['
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-fixed-ips'"
op|','
nl|'\n'
name|'FixedIPController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
name|'member_actions'
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
