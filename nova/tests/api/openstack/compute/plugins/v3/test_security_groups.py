begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2012 Justin Santa Barbara'
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
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'security_groups'
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
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
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
name|'jsonutils'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|FAKE_UUID1
name|'FAKE_UUID1'
op|'='
string|"'a47ae74e-ab08-447f-8eee-ffd43fc46c16'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server
name|'def'
name|'return_server'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'int'
op|'('
name|'server_id'
op|')'
op|','
nl|'\n'
string|"'power_state'"
op|':'
number|'0x01'
op|','
nl|'\n'
string|"'host'"
op|':'
string|'"localhost"'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'asdf'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_by_uuid
dedent|''
name|'def'
name|'return_server_by_uuid'
op|'('
name|'context'
op|','
name|'server_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'power_state'"
op|':'
number|'0x01'
op|','
nl|'\n'
string|"'host'"
op|':'
string|'"localhost"'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'server_uuid'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'asdf'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_non_running_server
dedent|''
name|'def'
name|'return_non_running_server'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'server_id'
op|','
string|"'power_state'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID1'
op|','
string|"'host'"
op|':'
string|'"localhost"'
op|','
string|"'name'"
op|':'
string|"'asdf'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_security_group_by_name
dedent|''
name|'def'
name|'return_security_group_by_name'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'group_name'
op|','
nl|'\n'
string|'"instances"'
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
name|'FAKE_UUID1'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_security_group_without_instances
dedent|''
name|'def'
name|'return_security_group_without_instances'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'group_name'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_nonexistent
dedent|''
name|'def'
name|'return_server_nonexistent'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSecurityGroups
dedent|''
name|'class'
name|'TestSecurityGroups'
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
name|'TestSecurityGroups'
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
name|'manager'
op|'='
name|'security_groups'
op|'.'
name|'SecurityGroupActionController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_by_non_existing_security_group_name
dedent|''
name|'def'
name|'test_associate_by_non_existing_security_group_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'return_server'
op|'('
name|'None'
op|','
string|"'1'"
op|')'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'None'
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'non-existing'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_by_invalid_server_id
dedent|''
name|'def'
name|'test_associate_by_invalid_server_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'test'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/invalid/action'"
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
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'invalid'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_without_body
dedent|''
name|'def'
name|'test_associate_without_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_no_security_group_name
dedent|''
name|'def'
name|'test_associate_no_security_group_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_security_group_name_with_whitespaces
dedent|''
name|'def'
name|'test_associate_security_group_name_with_whitespaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"   "'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_non_existing_instance
dedent|''
name|'def'
name|'test_associate_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_nonexistent'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_non_running_instance
dedent|''
name|'def'
name|'test_associate_non_running_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_non_running_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_non_running_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_without_instances'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|'('
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_already_associated_security_group_to_instance
dedent|''
name|'def'
name|'test_associate_already_associated_security_group_to_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_by_name'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate
dedent|''
name|'def'
name|'test_associate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_add_security_group'"
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_add_security_group'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_without_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_addSecurityGroup'
op|'('
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_by_non_existing_security_group_name
dedent|''
name|'def'
name|'test_disassociate_by_non_existing_security_group_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'return_server'
op|'('
name|'None'
op|','
string|"'1'"
op|')'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'None'
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'non-existing'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_by_invalid_server_id
dedent|''
name|'def'
name|'test_disassociate_by_invalid_server_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_by_name'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'test'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/invalid/action'"
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
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'invalid'"
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_without_body
dedent|''
name|'def'
name|'test_disassociate_without_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_no_security_group_name
dedent|''
name|'def'
name|'test_disassociate_no_security_group_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_security_group_name_with_whitespaces
dedent|''
name|'def'
name|'test_disassociate_security_group_name_with_whitespaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"   "'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_non_existing_instance
dedent|''
name|'def'
name|'test_disassociate_non_existing_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_by_name'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_non_running_instance
dedent|''
name|'def'
name|'test_disassociate_non_running_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_non_running_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_non_running_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_by_name'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|'('
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate_already_associated_security_group_to_instance
dedent|''
name|'def'
name|'test_disassociate_already_associated_security_group_to_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_without_instances'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
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
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|','
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disassociate
dedent|''
name|'def'
name|'test_disassociate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get'"
op|','
name|'return_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_by_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'instance_remove_security_group'"
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_remove_security_group'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'security_group_get_by_name'"
op|','
nl|'\n'
name|'return_security_group_by_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeSecurityGroup'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers/1/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_removeSecurityGroup'
op|'('
name|'req'
op|','
string|"'1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|UUID1
dedent|''
dedent|''
name|'UUID1'
op|'='
string|"'00000000-0000-0000-0000-000000000001'"
newline|'\n'
DECL|variable|UUID2
name|'UUID2'
op|'='
string|"'00000000-0000-0000-0000-000000000002'"
newline|'\n'
DECL|variable|UUID3
name|'UUID3'
op|'='
string|"'00000000-0000-0000-0000-000000000003'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get_all
name|'def'
name|'fake_compute_get_all'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-0-0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'fake-0-1'"
op|'}'
op|']'
op|')'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'2'
op|','
name|'uuid'
op|'='
name|'UUID2'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-1-0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'fake-1-1'"
op|'}'
op|']'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get
dedent|''
name|'def'
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID3'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-2-0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'fake-2-1'"
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_create
dedent|''
name|'def'
name|'fake_compute_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
op|'['
name|'fake_compute_get'
op|'('
op|')'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instances_security_groups_bindings
dedent|''
name|'def'
name|'fake_get_instances_security_groups_bindings'
op|'('
name|'inst'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'UUID1'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-0-0'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'fake-0-1'"
op|'}'
op|']'
op|','
nl|'\n'
name|'UUID2'
op|':'
op|'['
op|'{'
string|"'name'"
op|':'
string|"'fake-1-0'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'fake-1-1'"
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupsOutputTest
dedent|''
name|'class'
name|'SecurityGroupsOutputTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/json'"
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
name|'SecurityGroupsOutputTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get_all'"
op|','
name|'fake_compute_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'fake_compute_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-security-groups'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_request
dedent|''
name|'def'
name|'_make_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'body'
op|'='
name|'None'
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
name|'url'
op|')'
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'self'
op|'.'
name|'_encode_body'
op|'('
name|'body'
op|')'
newline|'\n'
dedent|''
name|'req'
op|'.'
name|'content_type'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_encode_body
dedent|''
name|'def'
name|'_encode_body'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_server
dedent|''
name|'def'
name|'_get_server'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_servers
dedent|''
name|'def'
name|'_get_servers'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'servers'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_groups
dedent|''
name|'def'
name|'_get_groups'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'server'
op|'.'
name|'get'
op|'('
string|"'security_groups'"
op|')'
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
name|'url'
op|'='
string|"'/v3/servers'"
newline|'\n'
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
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'fake-2-%s'"
op|'%'
name|'i'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v3/servers/%s'"
op|'%'
name|'UUID3'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'fake-2-%s'"
op|'%'
name|'i'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v3/servers/detail'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'server'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_servers'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'j'
op|','
name|'group'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_groups'
op|'('
name|'server'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
string|"'fake-%s-%s'"
op|'%'
op|'('
name|'i'
op|','
name|'j'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_instance_passthrough_404
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_no_instance_passthrough_404'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_get
indent|'        '
name|'def'
name|'fake_compute_get'
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
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'fake'"
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v3/servers/70f6db34-de8d-4fbd-aafb-4065bdfa6115'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupsOutputXmlTest
dedent|''
dedent|''
name|'class'
name|'SecurityGroupsOutputXmlTest'
op|'('
name|'SecurityGroupsOutputTest'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
nl|'\n'
DECL|class|MinimalCreateServerTemplate
name|'class'
name|'MinimalCreateServerTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'        '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'server'"
op|','
name|'selector'
op|'='
string|"'server'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'imageRef'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'flavorRef'"
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
nl|'\n'
name|'nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_encode_body
dedent|''
dedent|''
name|'def'
name|'_encode_body'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'self'
op|'.'
name|'MinimalCreateServerTemplate'
op|'('
op|')'
newline|'\n'
name|'return'
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_server
dedent|''
name|'def'
name|'_get_server'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_servers
dedent|''
name|'def'
name|'_get_servers'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
op|')'
op|'.'
name|'getchildren'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_groups
dedent|''
name|'def'
name|'_get_groups'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): we are adding security groups without an extension'
nl|'\n'
comment|"#             namespace so we don't break people using the existing"
nl|'\n'
comment|'#             functionality, but that means we need to use find with'
nl|'\n'
comment|'#             the existing server namespace.'
nl|'\n'
indent|'        '
name|'namespace'
op|'='
name|'server'
op|'.'
name|'nsmap'
op|'['
name|'None'
op|']'
newline|'\n'
name|'return'
name|'server'
op|'.'
name|'find'
op|'('
string|"'{%s}security_groups'"
op|'%'
name|'namespace'
op|')'
op|'.'
name|'getchildren'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
