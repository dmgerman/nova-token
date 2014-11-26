begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
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
name|'server_external_events'
name|'as'
name|'server_external_events_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'server_external_events'
name|'as'
name|'server_external_events_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
nl|'\n'
DECL|variable|fake_instances
name|'fake_instances'
op|'='
op|'{'
nl|'\n'
string|"'00000000-0000-0000-0000-000000000001'"
op|':'
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'uuid'
op|'='
string|"'00000000-0000-0000-0000-000000000001'"
op|','
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
string|"'00000000-0000-0000-0000-000000000002'"
op|':'
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'uuid'
op|'='
string|"'00000000-0000-0000-0000-000000000002'"
op|','
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
string|"'00000000-0000-0000-0000-000000000003'"
op|':'
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'uuid'
op|'='
string|"'00000000-0000-0000-0000-000000000003'"
op|','
name|'host'
op|'='
string|"'host2'"
op|')'
op|','
nl|'\n'
string|"'00000000-0000-0000-0000-000000000004'"
op|':'
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'uuid'
op|'='
string|"'00000000-0000-0000-0000-000000000004'"
op|','
name|'host'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|fake_instance_uuids
name|'fake_instance_uuids'
op|'='
name|'sorted'
op|'('
name|'fake_instances'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
DECL|variable|MISSING_UUID
name|'MISSING_UUID'
op|'='
string|"'00000000-0000-0000-0000-000000000005'"
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_get_by_uuid
name|'def'
name|'fake_get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_instances'
op|'['
name|'uuid'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.instance.Instance.get_by_uuid'"
op|','
name|'fake_get_by_uuid'
op|')'
newline|'\n'
DECL|class|ServerExternalEventsTestV21
name|'class'
name|'ServerExternalEventsTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|server_external_events
indent|'    '
name|'server_external_events'
op|'='
name|'server_external_events_v21'
newline|'\n'
DECL|variable|invalid_error
name|'invalid_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'ServerExternalEventsTestV21'
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
name|'api'
op|'='
name|'self'
op|'.'
name|'server_external_events'
op|'.'
name|'ServerExternalEventsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'event_1'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'network-vif-plugged'"
op|','
nl|'\n'
string|"'tag'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'server_uuid'"
op|':'
name|'fake_instance_uuids'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'completed'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'event_2'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'network-changed'"
op|','
nl|'\n'
string|"'server_uuid'"
op|':'
name|'fake_instance_uuids'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'completed'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'default_body'
op|'='
op|'{'
string|"'events'"
op|':'
op|'['
name|'self'
op|'.'
name|'event_1'
op|','
name|'self'
op|'.'
name|'event_2'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'resp_event_1'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'event_1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_event_1'
op|'['
string|"'code'"
op|']'
op|'='
number|'200'
newline|'\n'
name|'self'
op|'.'
name|'resp_event_2'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'event_2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_event_2'
op|'['
string|"'code'"
op|']'
op|'='
number|'200'
newline|'\n'
name|'self'
op|'.'
name|'default_resp_body'
op|'='
op|'{'
string|"'events'"
op|':'
op|'['
name|'self'
op|'.'
name|'resp_event_1'
op|','
nl|'\n'
name|'self'
op|'.'
name|'resp_event_2'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_create_req
dedent|''
name|'def'
name|'_create_req'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-server-external-events'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|_assert_call
dedent|''
name|'def'
name|'_assert_call'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|','
name|'expected_uuids'
op|','
name|'expected_events'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'api'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|"'external_instance_event'"
op|')'
name|'as'
name|'api_method'
op|':'
newline|'\n'
indent|'            '
name|'response'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'response'
op|'.'
name|'obj'
newline|'\n'
name|'code'
op|'='
name|'response'
op|'.'
name|'_code'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'api_method'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'for'
name|'inst'
name|'in'
name|'api_method'
op|'.'
name|'call_args_list'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'expected_uuids'
op|'.'
name|'remove'
op|'('
name|'inst'
op|'.'
name|'uuid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'expected_uuids'
op|')'
newline|'\n'
name|'for'
name|'event'
name|'in'
name|'api_method'
op|'.'
name|'call_args_list'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
number|'2'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'expected_events'
op|'.'
name|'remove'
op|'('
name|'event'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'expected_events'
op|')'
newline|'\n'
name|'return'
name|'result'
op|','
name|'code'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'self'
op|'.'
name|'default_body'
op|')'
newline|'\n'
name|'result'
op|','
name|'code'
op|'='
name|'self'
op|'.'
name|'_assert_call'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'default_body'
op|','
nl|'\n'
name|'fake_instance_uuids'
op|'['
op|':'
number|'2'
op|']'
op|','
nl|'\n'
op|'['
string|"'network-vif-plugged'"
op|','
nl|'\n'
string|"'network-changed'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'default_resp_body'
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_one_bad_instance
dedent|''
name|'def'
name|'test_create_one_bad_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'default_body'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'server_uuid'"
op|']'
op|'='
name|'MISSING_UUID'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'result'
op|','
name|'code'
op|'='
name|'self'
op|'.'
name|'_assert_call'
op|'('
name|'req'
op|','
name|'body'
op|','
op|'['
name|'fake_instance_uuids'
op|'['
number|'0'
op|']'
op|']'
op|','
nl|'\n'
op|'['
string|"'network-vif-plugged'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'failed'"
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'code'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'code'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'207'
op|','
name|'code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_event_instance_has_no_host
dedent|''
name|'def'
name|'test_create_event_instance_has_no_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'default_body'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'server_uuid'"
op|']'
op|'='
name|'fake_instance_uuids'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
comment|'# the instance without host should not be passed to the compute layer'
nl|'\n'
name|'result'
op|','
name|'code'
op|'='
name|'self'
op|'.'
name|'_assert_call'
op|'('
name|'req'
op|','
name|'body'
op|','
nl|'\n'
op|'['
name|'fake_instance_uuids'
op|'['
number|'1'
op|']'
op|']'
op|','
nl|'\n'
op|'['
string|"'network-changed'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'422'
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'code'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'failed'"
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'result'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'code'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'207'
op|','
name|'code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_no_good_instances
dedent|''
name|'def'
name|'test_create_no_good_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'default_body'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'server_uuid'"
op|']'
op|'='
name|'MISSING_UUID'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'server_uuid'"
op|']'
op|'='
name|'MISSING_UUID'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
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
DECL|member|test_create_bad_status
dedent|''
name|'def'
name|'test_create_bad_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'default_body'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'status'"
op|']'
op|'='
string|"'foo'"
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
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
DECL|member|test_create_extra_gorp
dedent|''
name|'def'
name|'test_create_extra_gorp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'default_body'
newline|'\n'
name|'body'
op|'['
string|"'events'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'foobar'"
op|']'
op|'='
string|"'bad stuff'"
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
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
DECL|member|test_create_bad_events
dedent|''
name|'def'
name|'test_create_bad_events'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'events'"
op|':'
string|"'foo'"
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
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
DECL|member|test_create_bad_body
dedent|''
name|'def'
name|'test_create_bad_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_req'
op|'('
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
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
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.instance.Instance.get_by_uuid'"
op|','
name|'fake_get_by_uuid'
op|')'
newline|'\n'
DECL|class|ServerExternalEventsTestV2
name|'class'
name|'ServerExternalEventsTestV2'
op|'('
name|'ServerExternalEventsTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|server_external_events
indent|'    '
name|'server_external_events'
op|'='
name|'server_external_events_v2'
newline|'\n'
DECL|variable|invalid_error
name|'invalid_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
dedent|''
endmarker|''
end_unit
