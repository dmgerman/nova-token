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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
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
DECL|class|AgentsJsonTest
name|'class'
name|'AgentsJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-agents"'
newline|'\n'
comment|"# TODO(gmann): Overriding '_api_version' till all functional tests"
nl|'\n'
comment|'# are merged between v2 and v2.1. After that base class variable'
nl|'\n'
comment|"# itself can be changed to 'v2'"
nl|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
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
name|'AgentsJsonTest'
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
nl|'\n'
string|"'nova.api.openstack.compute.contrib.agents.Agents'"
op|')'
newline|'\n'
name|'return'
name|'f'
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
name|'AgentsJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'fake_agents_list'
op|'='
op|'['
op|'{'
string|"'url'"
op|':'
string|"'http://example.com/path/to/resource'"
op|','
nl|'\n'
string|"'hypervisor'"
op|':'
string|"'hypervisor'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'os'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'8.0'"
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
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_agent_build_create
name|'def'
name|'fake_agent_build_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
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
DECL|function|fake_agent_build_get_all
dedent|''
name|'def'
name|'fake_agent_build_get_all'
op|'('
name|'context'
op|','
name|'hypervisor'
op|')'
op|':'
newline|'\n'
indent|'            '
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
indent|'                '
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
indent|'                    '
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
indent|'            '
name|'pass'
newline|'\n'
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
indent|'            '
name|'pass'
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
string|'"agent_build_create"'
op|','
nl|'\n'
name|'fake_agent_build_create'
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
nl|'\n'
DECL|member|test_agent_create
dedent|''
name|'def'
name|'test_agent_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Creates a new agent build.'
nl|'\n'
indent|'        '
name|'project'
op|'='
op|'{'
string|"'url'"
op|':'
string|"'http://example.com/path/to/resource'"
op|','
nl|'\n'
string|"'hypervisor'"
op|':'
string|"'hypervisor'"
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86'"
op|','
nl|'\n'
string|"'os'"
op|':'
string|"'os'"
op|','
nl|'\n'
string|"'version'"
op|':'
string|"'8.0'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-agents'"
op|','
string|"'agent-post-req'"
op|','
nl|'\n'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'agent-post-resp'"
op|','
name|'project'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_list
dedent|''
name|'def'
name|'test_agent_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Return a list of all agent builds.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-agents'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'agents-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_update
dedent|''
name|'def'
name|'test_agent_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Update an existing agent build.'
nl|'\n'
indent|'        '
name|'agent_id'
op|'='
number|'1'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'version'"
op|':'
string|"'7.0'"
op|','
nl|'\n'
string|"'url'"
op|':'
string|"'http://example.com/path/to/resource'"
op|','
nl|'\n'
string|"'md5hash'"
op|':'
string|"'add6bb58e139be103324d04d82d8f545'"
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-agents/%s'"
op|'%'
name|'agent_id'
op|','
nl|'\n'
string|"'agent-update-put-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'agent-update-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_delete
dedent|''
name|'def'
name|'test_agent_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Deletes an existing agent build.'
nl|'\n'
indent|'        '
name|'agent_id'
op|'='
number|'1'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-agents/%s'"
op|'%'
name|'agent_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit