begin_unit
comment|'# Copyright 2012 IBM'
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
name|'cloudpipe_update'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'fake_network'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_networks
name|'fake_networks'
op|'='
op|'['
name|'fake_network'
op|'.'
name|'fake_network'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'fake_network'
op|'.'
name|'fake_network'
op|'('
number|'2'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_project_get_networks
name|'def'
name|'fake_project_get_networks'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'associate'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'fake_networks'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network_update
dedent|''
name|'def'
name|'fake_network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'network'
name|'in'
name|'fake_networks'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'network'
op|'['
string|"'id'"
op|']'
op|'=='
name|'network_id'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'                '
name|'network'
op|'['
name|'key'
op|']'
op|'='
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipeUpdateTest
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'CloudpipeUpdateTest'
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
name|'CloudpipeUpdateTest'
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
name|'cloudpipe_update'
op|'.'
name|'CloudpipeUpdateController'
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
string|'"project_get_networks"'
op|','
name|'fake_project_get_networks'
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
string|'"network_update"'
op|','
name|'fake_network_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cloudpipe_configure_project
dedent|''
name|'def'
name|'test_cloudpipe_configure_project'
op|'('
name|'self'
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
nl|'\n'
string|"'/v2/fake/os-cloudpipe/configure-project'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"configure_project"'
op|':'
op|'{'
string|'"vpn_ip"'
op|':'
string|'"1.2.3.4"'
op|','
string|'"vpn_port"'
op|':'
number|'222'
op|'}'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|"'configure-project'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'202 Accepted'"
op|','
name|'result'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_networks'
op|'['
number|'0'
op|']'
op|'['
string|"'vpn_public_address'"
op|']'
op|','
string|'"1.2.3.4"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_networks'
op|'['
number|'0'
op|']'
op|'['
string|"'vpn_public_port'"
op|']'
op|','
number|'222'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cloudpipe_configure_project_bad_url
dedent|''
name|'def'
name|'test_cloudpipe_configure_project_bad_url'
op|'('
name|'self'
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
nl|'\n'
string|"'/v2/fake/os-cloudpipe/configure-projectx'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"vpn_ip"'
op|':'
string|'"1.2.3.4"'
op|','
string|'"vpn_port"'
op|':'
number|'222'
op|'}'
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
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
nl|'\n'
string|"'configure-projectx'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cloudpipe_configure_project_bad_data
dedent|''
name|'def'
name|'test_cloudpipe_configure_project_bad_data'
op|'('
name|'self'
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
nl|'\n'
string|"'/v2/fake/os-cloudpipe/configure-project'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"vpn_ipxx"'
op|':'
string|'"1.2.3.4"'
op|','
string|'"vpn_port"'
op|':'
number|'222'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
nl|'\n'
string|"'configure-project'"
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
