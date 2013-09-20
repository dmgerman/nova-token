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
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'agents'
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
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|fake_agents_list
name|'fake_agents_list'
op|'='
op|'['
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'linux'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'16.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx1'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f546'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'xen'"
op|','
string|"'os'"
op|':'
string|"'linux'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'16.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx2'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f547'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'3'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'xen'"
op|','
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'power'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx3'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f548'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'4'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_agent_build_get_all
name|'def'
name|'fake_agent_build_get_all'
op|'('
name|'context'
op|','
name|'hypervisor'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'agent_build_all'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'agent'
name|'in'
name|'fake_agents_list'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hypervisor'
name|'and'
name|'hypervisor'
op|'!='
name|'agent'
op|'['
string|"'hypervisor'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'agent_build_ref'
op|'='
name|'models'
op|'.'
name|'AgentBuild'
op|'('
op|')'
newline|'\n'
name|'agent_build_ref'
op|'.'
name|'update'
op|'('
name|'agent'
op|')'
newline|'\n'
name|'agent_build_all'
op|'.'
name|'append'
op|'('
name|'agent_build_ref'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'agent_build_all'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_agent_build_update
dedent|''
name|'def'
name|'fake_agent_build_update'
op|'('
name|'context'
op|','
name|'agent_build_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_agent_build_destroy
dedent|''
name|'def'
name|'fake_agent_build_destroy'
op|'('
name|'context'
op|','
name|'agent_update_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_agent_build_create
dedent|''
name|'def'
name|'fake_agent_build_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'values'
op|'['
string|"'id'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'agent_build_ref'
op|'='
name|'models'
op|'.'
name|'AgentBuild'
op|'('
op|')'
newline|'\n'
name|'agent_build_ref'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'agent_build_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
dedent|''
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestWithHypervisor
dedent|''
name|'class'
name|'FakeRequestWithHypervisor'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_agent_build_create_with_exited_agent
dedent|''
name|'def'
name|'fake_agent_build_create_with_exited_agent'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'AgentBuildExists'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AgentsTest
dedent|''
name|'class'
name|'AgentsTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'AgentsTest'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"agent_build_get_all"'
op|','
nl|'\n'
name|'fake_agent_build_get_all'
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
string|'"agent_build_update"'
op|','
nl|'\n'
name|'fake_agent_build_update'
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
string|'"agent_build_destroy"'
op|','
nl|'\n'
name|'fake_agent_build_destroy'
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
string|'"agent_build_create"'
op|','
nl|'\n'
name|'fake_agent_build_create'
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
name|'controller'
op|'='
name|'agents'
op|'.'
name|'AgentController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create
dedent|''
name|'def'
name|'test_agents_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'res_dict'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'.'
name|'wsgi_code'
op|','
number|'201'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_with_existed_agent
dedent|''
name|'def'
name|'test_agents_create_with_existed_agent'
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
name|'db'
op|','
string|"'agent_build_create'"
op|','
nl|'\n'
name|'fake_agent_build_create_with_exited_agent'
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_md5hash
dedent|''
name|'def'
name|'test_agents_create_without_md5hash'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_url
dedent|''
name|'def'
name|'test_agents_create_without_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_version
dedent|''
name|'def'
name|'test_agents_create_without_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_architecture
dedent|''
name|'def'
name|'test_agents_create_without_architecture'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_os
dedent|''
name|'def'
name|'test_agents_create_without_os'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_without_hypervisor
dedent|''
name|'def'
name|'test_agents_create_without_hypervisor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_with_wrong_type
dedent|''
name|'def'
name|'test_agents_create_with_wrong_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_create_with_empty_type
dedent|''
name|'def'
name|'test_agents_create_with_empty_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_delete
dedent|''
name|'def'
name|'test_agents_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_list
dedent|''
name|'def'
name|'test_agents_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
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
op|')'
newline|'\n'
name|'agents_list'
op|'='
op|'['
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'linux'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'16.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx1'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f546'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'2'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'xen'"
op|','
string|"'os'"
op|':'
string|"'linux'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'16.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx2'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f547'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'3'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'xen'"
op|','
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'power'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx3'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f548'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'4'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
op|'{'
string|"'agents'"
op|':'
name|'agents_list'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_list_with_hypervisor
dedent|''
name|'def'
name|'test_agents_list_with_hypervisor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequestWithHypervisor'
op|'('
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
op|')'
newline|'\n'
name|'response'
op|'='
op|'['
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'win'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
string|"'kvm'"
op|','
string|"'os'"
op|':'
string|"'linux'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'16.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx1'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f546'"
op|','
nl|'\n'
string|"'agent_id'"
op|':'
number|'2'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
op|'{'
string|"'agents'"
op|':'
name|'response'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update
dedent|''
name|'def'
name|'test_agents_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'agent_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
op|'}'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update_without_md5hash
dedent|''
name|'def'
name|'test_agents_update_without_md5hash'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'xxx://xxxx/xxx/xxx'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update_without_url
dedent|''
name|'def'
name|'test_agents_update_without_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
string|"'version'"
op|':'
string|"'7.0'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update_without_version
dedent|''
name|'def'
name|'test_agents_update_without_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update_with_wrong_type
dedent|''
name|'def'
name|'test_agents_update_with_wrong_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'agent'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agents_update_with_empty
dedent|''
name|'def'
name|'test_agents_update_with_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
