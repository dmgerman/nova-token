begin_unit
comment|'# Copyright 2013 Rackspace Hosting'
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
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'webob'
name|'import'
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
name|'contrib'
name|'import'
name|'instance_actions'
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
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
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
name|'policy'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_instance_actions'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fake_instance_actions'
op|'.'
name|'FAKE_UUID'
newline|'\n'
DECL|variable|FAKE_REQUEST_ID
name|'FAKE_REQUEST_ID'
op|'='
name|'fake_instance_actions'
op|'.'
name|'FAKE_REQUEST_ID1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|format_action
name|'def'
name|'format_action'
op|'('
name|'action'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Remove keys that aren't serialized.'''"
newline|'\n'
name|'if'
string|"'id'"
name|'in'
name|'action'
op|':'
newline|'\n'
indent|'        '
name|'del'
op|'('
name|'action'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'finish_time'"
name|'in'
name|'action'
op|':'
newline|'\n'
indent|'        '
name|'del'
op|'('
name|'action'
op|'['
string|"'finish_time'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'action'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|format_event
dedent|''
name|'def'
name|'format_event'
op|'('
name|'event'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Remove keys that aren't serialized.'''"
newline|'\n'
name|'if'
string|"'id'"
name|'in'
name|'event'
op|':'
newline|'\n'
indent|'        '
name|'del'
op|'('
name|'event'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'event'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionsPolicyTest
dedent|''
name|'class'
name|'InstanceActionsPolicyTest'
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
name|'InstanceActionsPolicyTest'
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
name|'controller'
op|'='
name|'instance_actions'
op|'.'
name|'InstanceActionsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_actions_restricted_by_project
dedent|''
name|'def'
name|'test_list_actions_restricted_by_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
name|'policy'
op|'.'
name|'Rules'
op|'('
op|'{'
string|"'compute:get'"
op|':'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:instance_actions'"
op|':'
nl|'\n'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"'project_id:%(project_id)s'"
op|')'
op|'}'
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake'"
op|','
string|"'project_id'"
op|':'
string|"'%s_unequal'"
op|'%'
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|'}'
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
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/123/servers/12/os-instance-actions'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|','
nl|'\n'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_action_restricted_by_project
dedent|''
name|'def'
name|'test_get_action_restricted_by_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
name|'policy'
op|'.'
name|'Rules'
op|'('
op|'{'
string|"'compute:get'"
op|':'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:instance_actions'"
op|':'
nl|'\n'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"'project_id:%(project_id)s'"
op|')'
op|'}'
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'name'"
op|':'
string|"'fake'"
op|','
string|"'project_id'"
op|':'
string|"'%s_unequal'"
op|'%'
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|'}'
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
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/servers/12/os-instance-actions/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
nl|'\n'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionsTest
dedent|''
dedent|''
name|'class'
name|'InstanceActionsTest'
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
name|'InstanceActionsTest'
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
name|'controller'
op|'='
name|'instance_actions'
op|'.'
name|'InstanceActionsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_actions'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_instance_actions'
op|'.'
name|'FAKE_ACTIONS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_events'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_instance_actions'
op|'.'
name|'FAKE_EVENTS'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
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
op|'{'
string|"'name'"
op|':'
string|"'fake'"
op|','
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
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
string|"'get'"
op|','
name|'fake_get'
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
string|"'instance_get_by_uuid'"
op|','
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_actions
dedent|''
name|'def'
name|'test_list_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_actions
indent|'        '
name|'def'
name|'fake_get_actions'
op|'('
name|'context'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'act'
name|'in'
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'uuid'
op|']'
op|'.'
name|'itervalues'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'action'
op|'='
name|'models'
op|'.'
name|'InstanceAction'
op|'('
op|')'
newline|'\n'
name|'action'
op|'.'
name|'update'
op|'('
name|'act'
op|')'
newline|'\n'
name|'actions'
op|'.'
name|'append'
op|'('
name|'action'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'actions'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'actions_get'"
op|','
name|'fake_get_actions'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/123/servers/12/os-instance-actions'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'for'
name|'res'
name|'in'
name|'res_dict'
op|'['
string|"'instanceActions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'fake_action'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'res'
op|'['
string|"'request_id'"
op|']'
op|']'
newline|'\n'
name|'fake_action'
op|'='
name|'format_action'
op|'('
name|'fake_action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_action'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_action_with_events_allowed
dedent|''
dedent|''
name|'def'
name|'test_get_action_with_events_allowed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_action
indent|'        '
name|'def'
name|'fake_get_action'
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
name|'action'
op|'='
name|'models'
op|'.'
name|'InstanceAction'
op|'('
op|')'
newline|'\n'
name|'action'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'uuid'
op|']'
op|'['
name|'request_id'
op|']'
op|')'
newline|'\n'
name|'return'
name|'action'
newline|'\n'
nl|'\n'
DECL|function|fake_get_events
dedent|''
name|'def'
name|'fake_get_events'
op|'('
name|'context'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'events'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'evt'
name|'in'
name|'self'
op|'.'
name|'fake_events'
op|'['
name|'action_id'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'event'
op|'='
name|'models'
op|'.'
name|'InstanceActionEvent'
op|'('
op|')'
newline|'\n'
name|'event'
op|'.'
name|'update'
op|'('
name|'evt'
op|')'
newline|'\n'
name|'events'
op|'.'
name|'append'
op|'('
name|'event'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'events'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'action_get_by_request_id'"
op|','
name|'fake_get_action'
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
string|"'action_events_get'"
op|','
name|'fake_get_events'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/servers/12/os-instance-actions/1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'FAKE_REQUEST_ID'
op|')'
newline|'\n'
name|'fake_action'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'FAKE_REQUEST_ID'
op|']'
newline|'\n'
name|'fake_events'
op|'='
name|'self'
op|'.'
name|'fake_events'
op|'['
name|'fake_action'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
name|'fake_events'
op|'='
op|'['
name|'format_event'
op|'('
name|'event'
op|')'
name|'for'
name|'event'
name|'in'
name|'fake_events'
op|']'
newline|'\n'
name|'fake_action'
op|'='
name|'format_action'
op|'('
name|'fake_action'
op|')'
newline|'\n'
name|'fake_action'
op|'['
string|"'events'"
op|']'
op|'='
name|'fake_events'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_action'
op|','
name|'res_dict'
op|'['
string|"'instanceAction'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_action_with_events_not_allowed
dedent|''
name|'def'
name|'test_get_action_with_events_not_allowed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_action
indent|'        '
name|'def'
name|'fake_get_action'
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
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'uuid'
op|']'
op|'['
name|'request_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_get_events
dedent|''
name|'def'
name|'fake_get_events'
op|'('
name|'context'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'fake_events'
op|'['
name|'action_id'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'action_get_by_request_id'"
op|','
name|'fake_get_action'
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
string|"'action_events_get'"
op|','
name|'fake_get_events'
op|')'
newline|'\n'
name|'rules'
op|'='
name|'policy'
op|'.'
name|'Rules'
op|'('
op|'{'
string|"'compute:get'"
op|':'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:instance_actions'"
op|':'
nl|'\n'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"''"
op|')'
op|','
nl|'\n'
string|"'compute_extension:instance_actions:events'"
op|':'
nl|'\n'
name|'policy'
op|'.'
name|'parse_rule'
op|'('
string|"'is_admin:True'"
op|')'
op|'}'
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/servers/12/os-instance-actions/1'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'FAKE_REQUEST_ID'
op|')'
newline|'\n'
name|'fake_action'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'FAKE_REQUEST_ID'
op|']'
newline|'\n'
name|'fake_action'
op|'='
name|'format_action'
op|'('
name|'fake_action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_action'
op|','
name|'res_dict'
op|'['
string|"'instanceAction'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_action_not_found
dedent|''
name|'def'
name|'test_action_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_no_action
indent|'        '
name|'def'
name|'fake_no_action'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'action_get_by_request_id'"
op|','
name|'fake_no_action'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/servers/12/os-instance-actions/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|','
name|'FAKE_REQUEST_ID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_not_found
dedent|''
name|'def'
name|'test_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get
indent|'        '
name|'def'
name|'fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
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
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/123/servers/12/os-instance-actions'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionsSerializerTest
dedent|''
dedent|''
name|'class'
name|'InstanceActionsSerializerTest'
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
name|'InstanceActionsSerializerTest'
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
name|'fake_actions'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_instance_actions'
op|'.'
name|'FAKE_ACTIONS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_events'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'fake_instance_actions'
op|'.'
name|'FAKE_EVENTS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_instance_action_attachment
dedent|''
name|'def'
name|'_verify_instance_action_attachment'
op|'('
name|'self'
op|','
name|'attach'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'attach'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'!='
string|"'events'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'attach'
op|'['
name|'key'
op|']'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|','
nl|'\n'
string|"'%s did not match'"
op|'%'
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_instance_action_event_attachment
dedent|''
dedent|''
dedent|''
name|'def'
name|'_verify_instance_action_event_attachment'
op|'('
name|'self'
op|','
name|'attach'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'attach'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'attach'
op|'['
name|'key'
op|']'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|','
nl|'\n'
string|"'%s did not match'"
op|'%'
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_action_serializer
dedent|''
dedent|''
name|'def'
name|'test_instance_action_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'instance_actions'
op|'.'
name|'InstanceActionTemplate'
op|'('
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'FAKE_REQUEST_ID'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
string|"'instanceAction'"
op|':'
name|'action'
op|'}'
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
name|'action'
op|'='
name|'format_action'
op|'('
name|'action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'instanceAction'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_instance_action_attachment'
op|'('
name|'action'
op|','
name|'tree'
op|')'
newline|'\n'
name|'found_events'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'events'"
op|':'
newline|'\n'
indent|'                '
name|'found_events'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_events'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_action_events_serializer
dedent|''
name|'def'
name|'test_instance_action_events_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'instance_actions'
op|'.'
name|'InstanceActionTemplate'
op|'('
op|')'
newline|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'FAKE_REQUEST_ID'
op|']'
newline|'\n'
name|'event'
op|'='
name|'self'
op|'.'
name|'fake_events'
op|'['
name|'action'
op|'['
string|"'id'"
op|']'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'action'
op|'['
string|"'events'"
op|']'
op|'='
op|'['
name|'event'
op|','
name|'event'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
string|"'instanceAction'"
op|':'
name|'action'
op|'}'
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
name|'action'
op|'='
name|'format_action'
op|'('
name|'action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'instanceAction'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_instance_action_attachment'
op|'('
name|'action'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
name|'event'
op|'='
name|'format_event'
op|'('
name|'event'
op|')'
newline|'\n'
name|'found_events'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'events'"
op|':'
newline|'\n'
indent|'                '
name|'found_events'
op|'='
name|'True'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'event'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'event'
op|'['
name|'key'
op|']'
op|','
name|'child'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found_events'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_actions_serializer
dedent|''
name|'def'
name|'test_instance_actions_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'instance_actions'
op|'.'
name|'InstanceActionsTemplate'
op|'('
op|')'
newline|'\n'
name|'action_list'
op|'='
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
string|"'instanceActions'"
op|':'
name|'action_list'
op|'}'
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
name|'action_list'
op|'='
op|'['
name|'format_action'
op|'('
name|'action'
op|')'
name|'for'
name|'action'
name|'in'
name|'action_list'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'instanceActions'"
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
name|'action_list'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'instanceAction'"
op|','
name|'child'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'request_id'
op|'='
name|'child'
op|'.'
name|'get'
op|'('
string|"'request_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_instance_action_attachment'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_actions'
op|'['
name|'FAKE_UUID'
op|']'
op|'['
name|'request_id'
op|']'
op|','
nl|'\n'
name|'child'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
