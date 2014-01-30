begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'availability_zones'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-availability-zone"'
newline|'\n'
DECL|variable|ATTRIBUTE_NAME
name|'ATTRIBUTE_NAME'
op|'='
string|'"%s:availability_zone"'
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|authorize_list
name|'authorize_list'
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
op|'+'
string|"':list'"
op|')'
newline|'\n'
DECL|variable|authorize_detail
name|'authorize_detail'
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
op|'+'
string|"':detail'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZoneController
name|'class'
name|'AvailabilityZoneController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Availability Zone API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'AvailabilityZoneController'
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
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_filtered_availability_zones
dedent|''
name|'def'
name|'_get_filtered_availability_zones'
op|'('
name|'self'
op|','
name|'zones'
op|','
name|'is_available'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'zone'
name|'in'
name|'zones'
op|':'
newline|'\n'
comment|'# Hide internal_service_availability_zone'
nl|'\n'
indent|'            '
name|'if'
name|'zone'
op|'=='
name|'CONF'
op|'.'
name|'internal_service_availability_zone'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zone_name'"
op|':'
name|'zone'
op|','
nl|'\n'
string|"'zone_state'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'is_available'
op|'}'
op|','
nl|'\n'
string|'"hosts"'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_describe_availability_zones
dedent|''
name|'def'
name|'_describe_availability_zones'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'available_zones'
op|','
name|'not_available_zones'
op|'='
name|'availability_zones'
op|'.'
name|'get_availability_zones'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'filtered_available_zones'
op|'='
name|'self'
op|'.'
name|'_get_filtered_availability_zones'
op|'('
name|'available_zones'
op|','
name|'True'
op|')'
newline|'\n'
name|'filtered_not_available_zones'
op|'='
name|'self'
op|'.'
name|'_get_filtered_availability_zones'
op|'('
name|'not_available_zones'
op|','
name|'False'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'availability_zone_info'"
op|':'
name|'filtered_available_zones'
op|'+'
nl|'\n'
name|'filtered_not_available_zones'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_describe_availability_zones_verbose
dedent|''
name|'def'
name|'_describe_availability_zones_verbose'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'available_zones'
op|','
name|'not_available_zones'
op|'='
name|'availability_zones'
op|'.'
name|'get_availability_zones'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
comment|'# Available services'
nl|'\n'
name|'enabled_services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'False'
op|')'
newline|'\n'
name|'enabled_services'
op|'='
name|'availability_zones'
op|'.'
name|'set_availability_zones'
op|'('
name|'context'
op|','
nl|'\n'
name|'enabled_services'
op|')'
newline|'\n'
name|'zone_hosts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'host_services'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'enabled_services'
op|':'
newline|'\n'
indent|'            '
name|'zone_hosts'
op|'.'
name|'setdefault'
op|'('
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'service'
op|'['
string|"'host'"
op|']'
name|'not'
name|'in'
name|'zone_hosts'
op|'['
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'zone_hosts'
op|'['
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'host_services'
op|'.'
name|'setdefault'
op|'('
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'+'
nl|'\n'
name|'service'
op|'['
string|"'host'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'host_services'
op|'['
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'+'
name|'service'
op|'['
string|"'host'"
op|']'
op|']'
op|'.'
name|'append'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'zone'
name|'in'
name|'available_zones'
op|':'
newline|'\n'
indent|'            '
name|'hosts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'host'
name|'in'
name|'zone_hosts'
op|'.'
name|'get'
op|'('
name|'zone'
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'hosts'
op|'['
name|'host'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'host_services'
op|'['
name|'zone'
op|'+'
name|'host'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'alive'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
newline|'\n'
name|'hosts'
op|'['
name|'host'
op|']'
op|'['
name|'service'
op|'['
string|"'binary'"
op|']'
op|']'
op|'='
op|'{'
string|"'available'"
op|':'
name|'alive'
op|','
nl|'\n'
string|"'active'"
op|':'
name|'True'
op|'!='
name|'service'
op|'['
string|"'disabled'"
op|']'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'service'
op|'['
string|"'updated_at'"
op|']'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zone_name'"
op|':'
name|'zone'
op|','
nl|'\n'
string|"'zone_state'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
string|'"hosts"'
op|':'
name|'hosts'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'zone'
name|'in'
name|'not_available_zones'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zone_name'"
op|':'
name|'zone'
op|','
nl|'\n'
string|"'zone_state'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
string|'"hosts"'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'availability_zone_info'"
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
string|'"""Returns a summary list of availability zone."""'
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
name|'authorize_list'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_describe_availability_zones'
op|'('
name|'context'
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
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a detailed list of availability zone."""'
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
name|'authorize_detail'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_describe_availability_zones_verbose'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZone
dedent|''
dedent|''
name|'class'
name|'AvailabilityZone'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""1. Add availability_zone to the Create Server API.\n       2. Add availability zones describing.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"AvailabilityZone"'
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
string|'"availabilityzone/api/v3"'
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
name|'resource'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'AvailabilityZoneController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resource'
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
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'create_kwargs'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'ATTRIBUTE_NAME'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
