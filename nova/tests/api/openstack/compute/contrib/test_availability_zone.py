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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'availability_zone'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'availability_zones'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
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
op|'{'
string|"'binary'"
op|':'
name|'binary'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'available_zones'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'created_at'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'updated_at'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'disabled'
op|'}'
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
DECL|class|AvailabilityZoneApiTest
dedent|''
name|'class'
name|'AvailabilityZoneApiTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'AvailabilityZoneApiTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'service_get_all'"
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
name|'az'
op|'='
name|'availability_zone'
op|'.'
name|'AvailabilityZoneController'
op|'('
op|')'
newline|'\n'
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
name|'az'
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
name|'az'
op|'.'
name|'_get_filtered_availability_zones'
op|'('
name|'zones'
op|','
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
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-availability-zone'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'availabilityZoneInfo'"
name|'in'
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
DECL|function|_formatZone
indent|'        '
name|'def'
name|'_formatZone'
op|'('
name|'zone_dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Zone tree view item'
nl|'\n'
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zoneName'"
op|':'
name|'zone_dict'
op|'['
string|"'zoneName'"
op|']'
op|','
nl|'\n'
string|"'zoneState'"
op|':'
string|"u'available'"
nl|'\n'
name|'if'
name|'zone_dict'
op|'['
string|"'zoneState'"
op|']'
op|'['
string|"'available'"
op|']'
name|'else'
nl|'\n'
string|"u'not available'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'zone_dict'
op|'['
string|"'hosts'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'for'
op|'('
name|'host'
op|','
name|'services'
op|')'
name|'in'
name|'zone_dict'
op|'['
string|"'hosts'"
op|']'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Host tree view item'
nl|'\n'
indent|'                    '
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zoneName'"
op|':'
string|"u'|- %s'"
op|'%'
name|'host'
op|','
nl|'\n'
string|"'zoneState'"
op|':'
string|"u''"
op|'}'
op|')'
newline|'\n'
name|'for'
op|'('
name|'svc'
op|','
name|'state'
op|')'
name|'in'
name|'services'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Service tree view item'
nl|'\n'
indent|'                        '
name|'result'
op|'.'
name|'append'
op|'('
op|'{'
string|"'zoneName'"
op|':'
string|"u'| |- %s'"
op|'%'
name|'svc'
op|','
nl|'\n'
string|"'zoneState'"
op|':'
string|"u'%s %s %s'"
op|'%'
op|'('
nl|'\n'
string|"'enabled'"
name|'if'
name|'state'
op|'['
string|"'active'"
op|']'
name|'else'
nl|'\n'
string|"'disabled'"
op|','
nl|'\n'
string|"':-)'"
name|'if'
name|'state'
op|'['
string|"'available'"
op|']'
name|'else'
nl|'\n'
string|"'XXX'"
op|','
nl|'\n'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'state'
op|'['
string|"'updated_at'"
op|']'
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|function|_assertZone
dedent|''
name|'def'
name|'_assertZone'
op|'('
name|'zone'
op|','
name|'name'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'zone'
op|'['
string|"'zoneName'"
op|']'
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'zone'
op|'['
string|"'zoneState'"
op|']'
op|','
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'availabilityZone'
op|'='
name|'availability_zone'
op|'.'
name|'AvailabilityZoneController'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-availability-zone/detail'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'availabilityZone'
op|'.'
name|'detail'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'availabilityZoneInfo'"
name|'in'
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
nl|'\n'
string|"''' availabilityZoneInfo field content in response body:\n        [{'zoneName': 'zone-1',\n          'zoneState': {'available': True},\n          'hosts': {'fake_host-1': {\n                        'nova-compute': {'active': True, 'available': True,\n                          'updated_at': datetime(2012, 12, 26, 14, 45, 25)}}}},\n         {'zoneName': 'internal',\n          'zoneState': {'available': True},\n          'hosts': {'fake_host-1': {\n                        'nova-sched': {'active': True, 'available': True,\n                          'updated_at': datetime(2012, 12, 26, 14, 45, 25)}},\n                    'fake_host-2': {\n                        'nova-network': {'active': True, 'available': False,\n                          'updated_at': datetime(2012, 12, 26, 14, 45, 24)}}}},\n         {'zoneName': 'zone-2',\n          'zoneState': {'available': False},\n          'hosts': None}]\n        '''"
newline|'\n'
nl|'\n'
name|'l0'
op|'='
op|'['
string|"u'zone-1'"
op|','
string|"u'available'"
op|']'
newline|'\n'
name|'l1'
op|'='
op|'['
string|"u'|- fake_host-1'"
op|','
string|"u''"
op|']'
newline|'\n'
name|'l2'
op|'='
op|'['
string|"u'| |- nova-compute'"
op|','
string|"u'enabled :-) 2012-12-26T14:45:25.000000'"
op|']'
newline|'\n'
name|'l3'
op|'='
op|'['
string|"u'internal'"
op|','
string|"u'available'"
op|']'
newline|'\n'
name|'l4'
op|'='
op|'['
string|"u'|- fake_host-1'"
op|','
string|"u''"
op|']'
newline|'\n'
name|'l5'
op|'='
op|'['
string|"u'| |- nova-sched'"
op|','
string|"u'enabled :-) 2012-12-26T14:45:25.000000'"
op|']'
newline|'\n'
name|'l6'
op|'='
op|'['
string|"u'|- fake_host-2'"
op|','
string|"u''"
op|']'
newline|'\n'
name|'l7'
op|'='
op|'['
string|"u'| |- nova-network'"
op|','
string|"u'enabled XXX 2012-12-26T14:45:24.000000'"
op|']'
newline|'\n'
name|'l8'
op|'='
op|'['
string|"u'zone-2'"
op|','
string|"u'not available'"
op|']'
newline|'\n'
nl|'\n'
name|'z0'
op|'='
name|'_formatZone'
op|'('
name|'zones'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'z1'
op|'='
name|'_formatZone'
op|'('
name|'zones'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'z2'
op|'='
name|'_formatZone'
op|'('
name|'zones'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'z0'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'z1'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'z2'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'_assertZone'
op|'('
name|'z0'
op|'['
number|'0'
op|']'
op|','
name|'l0'
op|'['
number|'0'
op|']'
op|','
name|'l0'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z0'
op|'['
number|'1'
op|']'
op|','
name|'l1'
op|'['
number|'0'
op|']'
op|','
name|'l1'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z0'
op|'['
number|'2'
op|']'
op|','
name|'l2'
op|'['
number|'0'
op|']'
op|','
name|'l2'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z1'
op|'['
number|'0'
op|']'
op|','
name|'l3'
op|'['
number|'0'
op|']'
op|','
name|'l3'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z1'
op|'['
number|'1'
op|']'
op|','
name|'l4'
op|'['
number|'0'
op|']'
op|','
name|'l4'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z1'
op|'['
number|'2'
op|']'
op|','
name|'l5'
op|'['
number|'0'
op|']'
op|','
name|'l5'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z1'
op|'['
number|'3'
op|']'
op|','
name|'l6'
op|'['
number|'0'
op|']'
op|','
name|'l6'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z1'
op|'['
number|'4'
op|']'
op|','
name|'l7'
op|'['
number|'0'
op|']'
op|','
name|'l7'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'_assertZone'
op|'('
name|'z2'
op|'['
number|'0'
op|']'
op|','
name|'l8'
op|'['
number|'0'
op|']'
op|','
name|'l8'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZoneSerializerTest
dedent|''
dedent|''
name|'class'
name|'AvailabilityZoneSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_availability_zone_index_detail_serializer
indent|'    '
name|'def'
name|'test_availability_zone_index_detail_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_verify_zone
indent|'        '
name|'def'
name|'_verify_zone'
op|'('
name|'zone_dict'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'tag'
op|','
string|"'availabilityZone'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'zone_dict'
op|'['
string|"'zoneName'"
op|']'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'zone_dict'
op|'['
string|"'zoneState'"
op|']'
op|'['
string|"'available'"
op|']'
op|')'
op|','
nl|'\n'
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'available'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'_idx'
op|','
name|'host_child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|'['
number|'1'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'host_child'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
name|'in'
name|'zone_dict'
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
name|'svcs'
op|'='
name|'zone_dict'
op|'['
string|"'hosts'"
op|']'
op|'['
name|'host_child'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|']'
newline|'\n'
name|'for'
name|'_idx'
op|','
name|'svc_child'
name|'in'
name|'enumerate'
op|'('
name|'host_child'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'svc_child'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
name|'in'
name|'svcs'
op|')'
newline|'\n'
name|'svc'
op|'='
name|'svcs'
op|'['
name|'svc_child'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'svc_child'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'svc'
op|'['
string|"'available'"
op|']'
op|')'
op|','
nl|'\n'
name|'svc_child'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'available'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'svc'
op|'['
string|"'active'"
op|']'
op|')'
op|','
nl|'\n'
name|'svc_child'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'active'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'svc'
op|'['
string|"'updated_at'"
op|']'
op|')'
op|','
nl|'\n'
name|'svc_child'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'updated_at'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'serializer'
op|'='
name|'availability_zone'
op|'.'
name|'AvailabilityZonesTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_availability_zones'
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
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
nl|'\n'
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
op|')'
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
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
nl|'\n'
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
op|')'
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
nl|'\n'
name|'datetime'
op|'.'
name|'datetime'
op|'('
nl|'\n'
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
op|')'
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
nl|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'availabilityZoneInfo'
op|'='
name|'raw_availability_zones'
op|')'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'availabilityZones'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'raw_availability_zones'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_verify_zone'
op|'('
name|'raw_availability_zones'
op|'['
name|'idx'
op|']'
op|','
name|'child'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
