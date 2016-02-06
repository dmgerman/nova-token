begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
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
name|'import'
name|'fake_server_actions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'utils'
name|'as'
name|'test_utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerActionsSampleJsonTest
name|'class'
name|'ServerActionsSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|microversion
indent|'    '
name|'microversion'
op|'='
name|'None'
newline|'\n'
DECL|variable|ADMIN_API
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|"'os-instance-actions'"
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'ServerActionsSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.instance_actions.Instance_actions'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_fake_get
dedent|''
name|'def'
name|'_fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
nl|'\n'
name|'None'
op|','
op|'**'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ServerActionsSampleJsonTest'
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
name|'actions'
op|'='
name|'fake_server_actions'
op|'.'
name|'FAKE_ACTIONS'
newline|'\n'
name|'self'
op|'.'
name|'events'
op|'='
name|'fake_server_actions'
op|'.'
name|'FAKE_EVENTS'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'test_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_action_get_by_request_id
name|'def'
name|'fake_instance_action_get_by_request_id'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'actions'
op|'['
name|'uuid'
op|']'
op|'['
name|'request_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_server_actions_get
dedent|''
name|'def'
name|'fake_server_actions_get'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'value'
op|')'
name|'for'
name|'value'
name|'in'
nl|'\n'
name|'six'
op|'.'
name|'itervalues'
op|'('
name|'self'
op|'.'
name|'actions'
op|'['
name|'uuid'
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_action_events_get
dedent|''
name|'def'
name|'fake_instance_action_events_get'
op|'('
name|'context'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'events'
op|'['
name|'action_id'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
dedent|''
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.action_get_by_request_id'"
op|','
nl|'\n'
name|'fake_instance_action_get_by_request_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.actions_get'"
op|','
name|'fake_server_actions_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.action_events_get'"
op|','
nl|'\n'
name|'fake_instance_action_events_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_get_by_uuid'"
op|','
nl|'\n'
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.compute.api.API.get'"
op|','
name|'self'
op|'.'
name|'_fake_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_action_get
dedent|''
name|'def'
name|'test_instance_action_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_uuid'
op|'='
name|'fake_server_actions'
op|'.'
name|'FAKE_UUID'
newline|'\n'
name|'fake_request_id'
op|'='
name|'fake_server_actions'
op|'.'
name|'FAKE_REQUEST_ID1'
newline|'\n'
name|'fake_action'
op|'='
name|'self'
op|'.'
name|'actions'
op|'['
name|'fake_uuid'
op|']'
op|'['
name|'fake_request_id'
op|']'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-instance-actions/%s'"
op|'%'
nl|'\n'
op|'('
name|'fake_uuid'
op|','
name|'fake_request_id'
op|')'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'['
string|"'action'"
op|']'
op|'='
string|"'(reboot)|(resize)'"
newline|'\n'
name|'subs'
op|'['
string|"'instance_uuid'"
op|']'
op|'='
name|'fake_uuid'
newline|'\n'
name|'subs'
op|'['
string|"'integer_id'"
op|']'
op|'='
string|"'[0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'request_id'"
op|']'
op|'='
name|'fake_action'
op|'['
string|"'request_id'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'start_time'"
op|']'
op|'='
name|'fake_action'
op|'['
string|"'start_time'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'result'"
op|']'
op|'='
string|"'(Success)|(Error)'"
newline|'\n'
name|'subs'
op|'['
string|"'event'"
op|']'
op|'='
string|"'(schedule)|(compute_create)'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'instance-action-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_actions_list
dedent|''
name|'def'
name|'test_instance_actions_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_uuid'
op|'='
name|'fake_server_actions'
op|'.'
name|'FAKE_UUID'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-instance-actions'"
op|'%'
op|'('
name|'fake_uuid'
op|')'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'microversion'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'['
string|"'action'"
op|']'
op|'='
string|"'(reboot)|(resize)'"
newline|'\n'
name|'subs'
op|'['
string|"'integer_id'"
op|']'
op|'='
string|"'[0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'request_id'"
op|']'
op|'='
op|'('
string|"'req-[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}'"
nl|'\n'
string|"'-[0-9a-f]{4}-[0-9a-f]{12}'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'instance-actions-list-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerActionsV221SampleJsonTest
dedent|''
dedent|''
name|'class'
name|'ServerActionsV221SampleJsonTest'
op|'('
name|'ServerActionsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|microversion
indent|'    '
name|'microversion'
op|'='
string|"'2.21'"
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_21'"
op|','
op|'{'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_fake_get
name|'def'
name|'_fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'yes'"
op|','
name|'context'
op|'.'
name|'read_deleted'
op|')'
newline|'\n'
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
nl|'\n'
name|'None'
op|','
op|'**'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
