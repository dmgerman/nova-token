begin_unit
comment|'# Copyright 2012 IBM Corp.'
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
name|'datetime'
newline|'\n'
name|'import'
name|'iso8601'
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
name|'import'
name|'availability_zone'
name|'as'
name|'az_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
name|'as'
name|'servers_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'availability_zones'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'matchers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_service'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_get_all
name|'def'
name|'fake_service_get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|function|__fake_service
indent|'    '
name|'def'
name|'__fake_service'
op|'('
name|'binary'
op|','
name|'availability_zone'
op|','
nl|'\n'
name|'created_at'
op|','
name|'updated_at'
op|','
name|'host'
op|','
name|'disabled'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'test_service'
op|'.'
name|'fake_service'
op|','
nl|'\n'
name|'binary'
op|'='
name|'binary'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'availability_zone'
op|','
nl|'\n'
name|'available_zones'
op|'='
name|'availability_zone'
op|','
nl|'\n'
name|'created_at'
op|'='
name|'created_at'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'updated_at'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'disabled'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'disabled'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'__fake_service'
op|'('
string|'"nova-compute"'
op|','
string|'"zone-2"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'14'
op|','
number|'9'
op|','
number|'53'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-1"'
op|','
name|'True'
op|')'
op|','
nl|'\n'
name|'__fake_service'
op|'('
string|'"nova-scheduler"'
op|','
string|'"internal"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'14'
op|','
number|'9'
op|','
number|'57'
op|','
number|'3'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-1"'
op|','
name|'True'
op|')'
op|','
nl|'\n'
name|'__fake_service'
op|'('
string|'"nova-network"'
op|','
string|'"internal"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'16'
op|','
number|'7'
op|','
number|'25'
op|','
number|'46'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'24'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-2"'
op|','
name|'True'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'__fake_service'
op|'('
string|'"nova-compute"'
op|','
string|'"zone-1"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'14'
op|','
number|'9'
op|','
number|'53'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-1"'
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'__fake_service'
op|'('
string|'"nova-sched"'
op|','
string|'"internal"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'14'
op|','
number|'9'
op|','
number|'57'
op|','
number|'3'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'25'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-1"'
op|','
name|'False'
op|')'
op|','
nl|'\n'
name|'__fake_service'
op|'('
string|'"nova-network"'
op|','
string|'"internal"'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'16'
op|','
number|'7'
op|','
number|'25'
op|','
number|'46'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'12'
op|','
number|'26'
op|','
number|'14'
op|','
number|'45'
op|','
number|'24'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"fake_host-2"'
op|','
name|'False'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_is_up
dedent|''
dedent|''
name|'def'
name|'fake_service_is_up'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'service'
op|'['
string|"'binary'"
op|']'
op|'!='
string|'u"nova-network"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_set_availability_zones
dedent|''
name|'def'
name|'fake_set_availability_zones'
op|'('
name|'context'
op|','
name|'services'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'services'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_availability_zones
dedent|''
name|'def'
name|'fake_get_availability_zones'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
string|"'nova'"
op|']'
op|','
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
dedent|''
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZoneApiTestV21
name|'class'
name|'AvailabilityZoneApiTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|availability_zone
indent|'    '
name|'availability_zone'
op|'='
name|'az_v21'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'AvailabilityZoneApiTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'availability_zones'
op|'.'
name|'reset_cache'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.service_get_all'"
op|','
name|'fake_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'availability_zones'
op|','
string|"'set_availability_zones'"
op|','
nl|'\n'
name|'fake_set_availability_zones'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'servicegroup'
op|'.'
name|'API'
op|','
string|"'service_is_up'"
op|','
name|'fake_service_is_up'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'availability_zone'
op|'.'
name|'AvailabilityZoneController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filtered_availability_zones
dedent|''
name|'def'
name|'test_filtered_availability_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zones'
op|'='
op|'['
string|"'zone1'"
op|','
string|"'internal'"
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'zoneName'"
op|':'
string|"'zone1'"
op|','
nl|'\n'
string|"'zoneState'"
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
name|'None'
op|'}'
op|']'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_filtered_availability_zones'
op|'('
name|'zones'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'zoneName'"
op|':'
string|"'zone1'"
op|','
nl|'\n'
string|"'zoneState'"
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
op|']'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_filtered_availability_zones'
op|'('
name|'zones'
op|','
nl|'\n'
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_availability_zone_index
dedent|''
name|'def'
name|'test_availability_zone_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'availabilityZoneInfo'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'zones'
op|'='
name|'resp_dict'
op|'['
string|"'availabilityZoneInfo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'zones'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'zones'
op|'['
number|'0'
op|']'
op|'['
string|"'zoneName'"
op|']'
op|','
string|"u'zone-1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'zones'
op|'['
number|'0'
op|']'
op|'['
string|"'zoneState'"
op|']'
op|'['
string|"'available'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'zones'
op|'['
number|'0'
op|']'
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'zones'
op|'['
number|'1'
op|']'
op|'['
string|"'zoneName'"
op|']'
op|','
string|"u'zone-2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'zones'
op|'['
number|'1'
op|']'
op|'['
string|"'zoneState'"
op|']'
op|'['
string|"'available'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'zones'
op|'['
number|'1'
op|']'
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_availability_zone_detail
dedent|''
name|'def'
name|'test_availability_zone_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'availabilityZoneInfo'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'zones'
op|'='
name|'resp_dict'
op|'['
string|"'availabilityZoneInfo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'zones'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'timestamp'
op|'='
name|'iso8601'
op|'.'
name|'parse_date'
op|'('
string|'"2012-12-26T14:45:25Z"'
op|')'
newline|'\n'
name|'nova_network_timestamp'
op|'='
name|'iso8601'
op|'.'
name|'parse_date'
op|'('
string|'"2012-12-26T14:45:24Z"'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'zoneName'"
op|':'
string|"'zone-1'"
op|','
nl|'\n'
string|"'zoneState'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'{'
string|"'fake_host-1'"
op|':'
op|'{'
nl|'\n'
string|"'nova-compute'"
op|':'
op|'{'
string|"'active'"
op|':'
name|'True'
op|','
string|"'available'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|'}'
op|'}'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'zoneName'"
op|':'
string|"'internal'"
op|','
nl|'\n'
string|"'zoneState'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'{'
string|"'fake_host-1'"
op|':'
op|'{'
nl|'\n'
string|"'nova-sched'"
op|':'
op|'{'
string|"'active'"
op|':'
name|'True'
op|','
string|"'available'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|'}'
op|'}'
op|','
nl|'\n'
string|"'fake_host-2'"
op|':'
op|'{'
nl|'\n'
string|"'nova-network'"
op|':'
op|'{'
nl|'\n'
string|"'active'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'available'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'nova_network_timestamp'
op|'}'
op|'}'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'zoneName'"
op|':'
string|"'zone-2'"
op|','
nl|'\n'
string|"'zoneState'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
string|"'hosts'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'zones'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_availability_zone_detail_no_services
dedent|''
name|'def'
name|'test_availability_zone_detail_no_services'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_response'
op|'='
op|'{'
string|"'availabilityZoneInfo'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'zoneState'"
op|':'
op|'{'
string|"'available'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'zoneName'"
op|':'
string|"'nova'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'availability_zones'
op|','
string|"'get_availability_zones'"
op|','
nl|'\n'
name|'fake_get_availability_zones'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'resp_dict'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected_response'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersControllerCreateTestV21
dedent|''
dedent|''
name|'class'
name|'ServersControllerCreateTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|base_url
indent|'    '
name|'base_url'
op|'='
string|"'/v2/fake/'"
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shared implementation for tests below that create instance."""'
newline|'\n'
name|'super'
op|'('
name|'ServersControllerCreateTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_up_controller'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_create
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
number|'3'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'def_image_ref'
op|'='
string|"'http://localhost/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'+='
number|'1'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|'**'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'instance_cache_num'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
name|'or'
string|"'test'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fead::1234'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'def_image_ref'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"task_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"root_device_name"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|','
string|"'vda'"
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_create'"
op|','
name|'instance_create'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_up_controller
dedent|''
name|'def'
name|'_set_up_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
nl|'\n'
string|"'os-availability-zone'"
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_availability_zone_controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_extra
dedent|''
name|'def'
name|'_test_create_extra'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'controller'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageRef'
op|'='
name|'image_uuid'
op|','
name|'flavorRef'
op|'='
number|'2'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
newline|'\n'
name|'server'
op|'='
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_availability_zone_disabled
dedent|''
name|'def'
name|'test_create_instance_with_availability_zone_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'availability_zone'"
op|':'
string|"'foo'"
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'kwargs'
op|'['
string|"'availability_zone'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|','
name|'self'
op|'.'
name|'no_availability_zone_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_with_availability_zone
dedent|''
name|'def'
name|'_create_instance_with_availability_zone'
op|'('
name|'self'
op|','
name|'zone_name'
op|')'
op|':'
newline|'\n'
DECL|function|create
indent|'        '
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'availability_zone'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'nova'"
op|','
name|'kwargs'
op|'['
string|"'availability_zone'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
op|'('
string|"'http://localhost'"
op|'+'
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'flavors/3'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'zone_name'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'admin_context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'host1_zones'"
op|','
nl|'\n'
string|"'binary'"
op|':'
string|'"nova-compute"'
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|'}'
op|')'
newline|'\n'
name|'agg'
op|'='
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'admin_context'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'agg1'"
op|'}'
op|','
op|'{'
string|"'availability_zone'"
op|':'
string|"'nova'"
op|'}'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'aggregate_host_add'
op|'('
name|'admin_context'
op|','
name|'agg'
op|'['
string|"'id'"
op|']'
op|','
string|"'host1_zones'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'req'
op|','
name|'body'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_availability_zone
dedent|''
name|'def'
name|'test_create_instance_with_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zone_name'
op|'='
string|"'nova'"
newline|'\n'
name|'req'
op|','
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_availability_zone'
op|'('
name|'zone_name'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'server'
op|'='
name|'res'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_invalid_availability_zone_too_long
dedent|''
name|'def'
name|'test_create_instance_with_invalid_availability_zone_too_long'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zone_name'
op|'='
string|"'a'"
op|'*'
number|'256'
newline|'\n'
name|'req'
op|','
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_availability_zone'
op|'('
name|'zone_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_invalid_availability_zone_too_short
dedent|''
name|'def'
name|'test_create_instance_with_invalid_availability_zone_too_short'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zone_name'
op|'='
string|"''"
newline|'\n'
name|'req'
op|','
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_availability_zone'
op|'('
name|'zone_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_invalid_availability_zone_not_str
dedent|''
name|'def'
name|'test_create_instance_with_invalid_availability_zone_not_str'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zone_name'
op|'='
number|'111'
newline|'\n'
name|'req'
op|','
name|'body'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_availability_zone'
op|'('
name|'zone_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_without_availability_zone
dedent|''
name|'def'
name|'test_create_instance_without_availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
op|'('
string|"'http://localhost'"
op|'+'
name|'self'
op|'.'
name|'base_url'
op|'+'
string|"'flavors/3'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'server'
op|'='
name|'res'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
