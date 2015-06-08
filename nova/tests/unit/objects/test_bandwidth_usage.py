begin_unit
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
nl|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
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
name|'objects'
name|'import'
name|'bandwidth_usage'
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
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestBandwidthUsage
name|'class'
name|'_TestBandwidthUsage'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'_TestBandwidthUsage'
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
name|'user_id'
op|'='
string|"'fake_user'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake_project'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'now'
op|','
name|'start_period'
op|'='
name|'self'
op|'.'
name|'_time_now_and_start_period'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'expected_bw_usage'
op|'='
name|'self'
op|'.'
name|'_fake_bw_usage'
op|'('
nl|'\n'
name|'time'
op|'='
name|'now'
op|','
name|'start_period'
op|'='
name|'start_period'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_compare
name|'def'
name|'_compare'
op|'('
name|'test'
op|','
name|'db'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
op|','
name|'value'
name|'in'
name|'db'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'obj_field'
op|'='
name|'field'
newline|'\n'
name|'if'
name|'obj_field'
op|'=='
string|"'uuid'"
op|':'
newline|'\n'
indent|'                '
name|'obj_field'
op|'='
string|"'instance_uuid'"
newline|'\n'
dedent|''
name|'test'
op|'.'
name|'assertEqual'
op|'('
name|'db'
op|'['
name|'field'
op|']'
op|','
name|'obj'
op|'['
name|'obj_field'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_fake_bw_usage
name|'def'
name|'_fake_bw_usage'
op|'('
name|'time'
op|'='
name|'None'
op|','
name|'start_period'
op|'='
name|'None'
op|','
name|'bw_in'
op|'='
number|'100'
op|','
nl|'\n'
name|'bw_out'
op|'='
number|'200'
op|','
name|'last_ctr_in'
op|'='
number|'12345'
op|','
name|'last_ctr_out'
op|'='
number|'67890'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_bw_usage'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake_uuid1'"
op|','
nl|'\n'
string|"'mac'"
op|':'
string|"'fake_mac1'"
op|','
nl|'\n'
string|"'start_period'"
op|':'
name|'start_period'
op|','
nl|'\n'
string|"'bw_in'"
op|':'
name|'bw_in'
op|','
nl|'\n'
string|"'bw_out'"
op|':'
name|'bw_out'
op|','
nl|'\n'
string|"'last_ctr_in'"
op|':'
name|'last_ctr_in'
op|','
nl|'\n'
string|"'last_ctr_out'"
op|':'
name|'last_ctr_out'
op|','
nl|'\n'
string|"'last_refreshed'"
op|':'
name|'time'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'fake_bw_usage'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_time_now_and_start_period
name|'def'
name|'_time_now_and_start_period'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|','
nl|'\n'
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
name|'start_period'
op|'='
name|'now'
op|'-'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
number|'10'
op|')'
newline|'\n'
name|'return'
name|'now'
op|','
name|'start_period'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'bw_usage_get'"
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid_and_mac
name|'def'
name|'test_get_by_instance_uuid_and_mac'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
newline|'\n'
name|'bw_usage'
op|'='
name|'bandwidth_usage'
op|'.'
name|'BandwidthUsage'
op|'.'
name|'get_by_instance_uuid_and_mac'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_uuid'"
op|','
string|"'fake_mac'"
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'expected_bw_usage'
op|','
name|'bw_usage'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'bw_usage_get_by_uuids'"
op|')'
newline|'\n'
DECL|member|test_get_by_uuids
name|'def'
name|'test_get_by_uuids'
op|'('
name|'self'
op|','
name|'mock_get_by_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_by_uuids'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'expected_bw_usage'
op|']'
newline|'\n'
nl|'\n'
name|'bw_usages'
op|'='
name|'bandwidth_usage'
op|'.'
name|'BandwidthUsageList'
op|'.'
name|'get_by_uuids'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'['
string|"'fake_uuid'"
op|']'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'bw_usages'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'expected_bw_usage'
op|','
name|'bw_usages'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'bw_usage_update'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'mock_create'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_create'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
newline|'\n'
nl|'\n'
name|'bw_usage'
op|'='
name|'bandwidth_usage'
op|'.'
name|'BandwidthUsage'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bw_usage'
op|'.'
name|'create'
op|'('
string|"'fake_uuid'"
op|','
string|"'fake_mac'"
op|','
nl|'\n'
number|'100'
op|','
number|'200'
op|','
number|'12345'
op|','
number|'67890'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'expected_bw_usage'
op|','
name|'bw_usage'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'bw_usage_update'"
op|')'
newline|'\n'
DECL|member|test_update
name|'def'
name|'test_update'
op|'('
name|'self'
op|','
name|'mock_update'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_bw_usage1'
op|'='
name|'self'
op|'.'
name|'_fake_bw_usage'
op|'('
nl|'\n'
name|'time'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'last_refreshed'"
op|']'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|','
nl|'\n'
name|'last_ctr_in'
op|'='
number|'42'
op|','
name|'last_ctr_out'
op|'='
number|'42'
op|')'
newline|'\n'
nl|'\n'
name|'mock_update'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'expected_bw_usage1'
op|','
name|'self'
op|'.'
name|'expected_bw_usage'
op|']'
newline|'\n'
nl|'\n'
name|'bw_usage'
op|'='
name|'bandwidth_usage'
op|'.'
name|'BandwidthUsage'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'bw_usage'
op|'.'
name|'create'
op|'('
string|"'fake_uuid1'"
op|','
string|"'fake_mac1'"
op|','
nl|'\n'
number|'100'
op|','
number|'200'
op|','
number|'42'
op|','
number|'42'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'expected_bw_usage1'
op|','
name|'bw_usage'
op|')'
newline|'\n'
name|'bw_usage'
op|'.'
name|'create'
op|'('
string|"'fake_uuid1'"
op|','
string|"'fake_mac1'"
op|','
nl|'\n'
number|'100'
op|','
number|'200'
op|','
number|'12345'
op|','
number|'67890'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'self'
op|'.'
name|'expected_bw_usage'
op|'['
string|"'start_period'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'expected_bw_usage'
op|','
name|'bw_usage'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestBandwidthUsageObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestBandwidthUsageObject
name|'_TestBandwidthUsage'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteBandwidthUsageObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteBandwidthUsageObject
name|'_TestBandwidthUsage'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
