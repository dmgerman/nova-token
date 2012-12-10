begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
comment|'#    under the License'
nl|'\n'
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
name|'quota'
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
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XMLNS
name|'XMLNS'
op|'='
string|'"http://docs.openstack.org/compute/ext/used_limits/api/v1.1"'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-used-limits"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'used_limits'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsedLimitsTemplate
name|'class'
name|'UsedLimitsTemplate'
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
string|"'limits'"
op|','
name|'selector'
op|'='
string|"'limits'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'{%s}usedLimits'"
op|'%'
name|'XMLNS'
op|','
string|"'%s:usedLimits'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
name|'ALIAS'
op|':'
name|'XMLNS'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsedLimitsController
dedent|''
dedent|''
name|'class'
name|'UsedLimitsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_reserved
name|'def'
name|'_reserved'
op|'('
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
name|'int'
op|'('
name|'req'
op|'.'
name|'GET'
op|'['
string|"'reserved'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'UsedLimitsTemplate'
op|'('
op|')'
op|')'
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
name|'quotas'
op|'='
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
op|')'
newline|'\n'
name|'quota_map'
op|'='
op|'{'
nl|'\n'
string|"'totalRAMUsed'"
op|':'
string|"'ram'"
op|','
nl|'\n'
string|"'totalCoresUsed'"
op|':'
string|"'cores'"
op|','
nl|'\n'
string|"'totalInstancesUsed'"
op|':'
string|"'instances'"
op|','
nl|'\n'
string|"'totalVolumesUsed'"
op|':'
string|"'volumes'"
op|','
nl|'\n'
string|"'totalVolumeGigabytesUsed'"
op|':'
string|"'gigabytes'"
op|','
nl|'\n'
string|"'totalSecurityGroupsUsed'"
op|':'
string|"'floating_ips'"
op|','
nl|'\n'
string|"'totalKeyPairsUsed'"
op|':'
string|"'key_pairs'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'used_limits'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'display_name'
op|','
name|'quota'
name|'in'
name|'quota_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'quota'
name|'in'
name|'quotas'
op|':'
newline|'\n'
indent|'                '
name|'reserved'
op|'='
op|'('
name|'quotas'
op|'['
name|'quota'
op|']'
op|'['
string|"'reserved'"
op|']'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_reserved'
op|'('
name|'req'
op|')'
name|'else'
number|'0'
op|')'
newline|'\n'
name|'used_limits'
op|'['
name|'display_name'
op|']'
op|'='
name|'quotas'
op|'['
name|'quota'
op|']'
op|'['
string|"'in_use'"
op|']'
op|'+'
name|'reserved'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'limits'"
op|']'
op|'['
string|"'absolute'"
op|']'
op|'.'
name|'update'
op|'('
name|'used_limits'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Used_limits
dedent|''
dedent|''
name|'class'
name|'Used_limits'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide data on limited resources that are being used."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"UsedLimits"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
name|'XMLNS'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-07-13T00:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'UsedLimitsController'
op|'('
op|')'
newline|'\n'
name|'limits_ext'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'limits'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'limits_ext'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
