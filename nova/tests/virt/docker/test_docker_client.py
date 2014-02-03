begin_unit
comment|'# Copyright (c) 2013 dotCloud, Inc.'
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
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
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeResponse
name|'class'
name|'FakeResponse'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'status'
op|','
name|'data'
op|'='
string|"''"
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'status'
op|'='
name|'status'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'='
name|'data'
newline|'\n'
name|'self'
op|'.'
name|'_headers'
op|'='
name|'headers'
name|'or'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'_size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_data'
newline|'\n'
nl|'\n'
DECL|member|getheader
dedent|''
name|'def'
name|'getheader'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_headers'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DockerHTTPClientTestCase
dedent|''
dedent|''
name|'class'
name|'DockerHTTPClientTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_list_containers
indent|'    '
name|'def'
name|'test_list_containers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'GET'"
op|','
string|"'/v1.4/containers/ps?all=1&limit=50'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
name|'data'
op|'='
string|"'[]'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'containers'
op|'='
name|'client'
op|'.'
name|'list_containers'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'containers'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container
dedent|''
name|'def'
name|'test_create_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'expected_uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'expected_body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|"'Hostname'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'User'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'Memory'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'MemorySwap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'AttachStdin'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStdout'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStderr'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'PortSpecs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Tty'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'OpenStdin'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'StdinOnce'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'Env'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Cmd'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Dns'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Image'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Volumes'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'VolumesFrom'"
op|':'
string|"''"
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.7/containers/create?name={0}'"
op|'.'
name|'format'
op|'('
nl|'\n'
name|'expected_uuid'
op|')'
op|','
nl|'\n'
name|'body'
op|'='
name|'expected_body'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'201'
op|','
name|'data'
op|'='
string|'\'{"id": "XXX"}\''
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'container_id'
op|'='
name|'client'
op|'.'
name|'create_container'
op|'('
op|'{'
op|'}'
op|','
name|'expected_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'XXX'"
op|','
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container_with_args
dedent|''
name|'def'
name|'test_create_container_with_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'expected_uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
name|'expected_body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|"'Hostname'"
op|':'
string|"'marco'"
op|','
nl|'\n'
string|"'User'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'Memory'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'MemorySwap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'AttachStdin'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStdout'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStderr'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'PortSpecs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Tty'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'OpenStdin'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'StdinOnce'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'Env'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Cmd'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Dns'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Image'"
op|':'
string|"'example'"
op|','
nl|'\n'
string|"'Volumes'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'VolumesFrom'"
op|':'
string|"''"
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.7/containers/create?name={0}'"
op|'.'
name|'format'
op|'('
nl|'\n'
name|'expected_uuid'
op|')'
op|','
nl|'\n'
name|'body'
op|'='
name|'expected_body'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'201'
op|','
name|'data'
op|'='
string|'\'{"id": "XXX"}\''
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'args'
op|'='
op|'{'
nl|'\n'
string|"'Hostname'"
op|':'
string|"'marco'"
op|','
nl|'\n'
string|"'Memory'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'Image'"
op|':'
string|"'example'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'container_id'
op|'='
name|'client'
op|'.'
name|'create_container'
op|'('
name|'args'
op|','
name|'expected_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'XXX'"
op|','
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container_no_id_in_response
dedent|''
name|'def'
name|'test_create_container_no_id_in_response'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'expected_uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.7/containers/create?name={0}'"
op|'.'
name|'format'
op|'('
nl|'\n'
name|'expected_uuid'
op|')'
op|','
nl|'\n'
name|'body'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'201'
op|','
name|'data'
op|'='
string|'\'{"ping": "pong"}\''
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'container_id'
op|'='
name|'client'
op|'.'
name|'create_container'
op|'('
op|'{'
op|'}'
op|','
name|'expected_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_container_bad_return_code
dedent|''
name|'def'
name|'test_create_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'expected_uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.7/containers/create?name={0}'"
op|'.'
name|'format'
op|'('
nl|'\n'
name|'expected_uuid'
op|')'
op|','
nl|'\n'
name|'body'
op|'='
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'container_id'
op|'='
name|'client'
op|'.'
name|'create_container'
op|'('
op|'{'
op|'}'
op|','
name|'expected_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_container
dedent|''
name|'def'
name|'test_start_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/containers/XXX/start'"
op|','
nl|'\n'
name|'body'
op|'='
string|"'{}'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'start_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_container_bad_return_code
dedent|''
name|'def'
name|'test_start_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/containers/XXX/start'"
op|','
nl|'\n'
name|'body'
op|'='
string|"'{}'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'start_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inspect_image
dedent|''
name|'def'
name|'test_inspect_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'GET'"
op|','
string|"'/v1.4/images/XXX/json'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
name|'data'
op|'='
string|'\'{"name": "XXX"}\''
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'image'
op|'='
name|'client'
op|'.'
name|'inspect_image'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'name'"
op|':'
string|"'XXX'"
op|'}'
op|','
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inspect_image_bad_return_code
dedent|''
name|'def'
name|'test_inspect_image_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'GET'"
op|','
string|"'/v1.4/images/XXX/json'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'404'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'image'
op|'='
name|'client'
op|'.'
name|'inspect_image'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inspect_container
dedent|''
name|'def'
name|'test_inspect_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'GET'"
op|','
string|"'/v1.4/containers/XXX/json'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
name|'data'
op|'='
string|'\'{"id": "XXX"}\''
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'container'
op|'='
name|'client'
op|'.'
name|'inspect_container'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'id'"
op|':'
string|"'XXX'"
op|'}'
op|','
name|'container'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inspect_container_bad_return_code
dedent|''
name|'def'
name|'test_inspect_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'GET'"
op|','
string|"'/v1.4/containers/XXX/json'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'404'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'container'
op|'='
name|'client'
op|'.'
name|'inspect_container'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'container'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_container
dedent|''
name|'def'
name|'test_stop_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/containers/XXX/stop?t=5'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'204'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'stop_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_container_bad_return_code
dedent|''
name|'def'
name|'test_stop_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/containers/XXX/stop?t=5'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'stop_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_container
dedent|''
name|'def'
name|'test_destroy_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'DELETE'"
op|','
string|"'/v1.4/containers/XXX'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'204'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'destroy_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy_container_bad_return_code
dedent|''
name|'def'
name|'test_destroy_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'DELETE'"
op|','
string|"'/v1.4/containers/XXX'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'destroy_container'
op|'('
string|"'XXX'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pull_repository
dedent|''
name|'def'
name|'test_pull_repository'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/images/create?fromImage=ping'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'pull_repository'
op|'('
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pull_repository_tag
dedent|''
name|'def'
name|'test_pull_repository_tag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|"'/v1.4/images/create?fromImage=ping&tag=pong'"
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
name|'url'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'pull_repository'
op|'('
string|"'ping:pong'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pull_repository_bad_return_code
dedent|''
name|'def'
name|'test_pull_repository_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/images/create?fromImage=ping'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'pull_repository'
op|'('
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_push_repository
dedent|''
name|'def'
name|'test_push_repository'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'('
string|'\'{"username":"foo","password":"bar",\''
nl|'\n'
string|'\'"auth":"","email":"foo@bar.bar"}\''
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/images/ping/push'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'push_repository'
op|'('
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_push_repository_bad_return_code
dedent|''
name|'def'
name|'test_push_repository_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'('
string|'\'{"username":"foo","password":"bar",\''
nl|'\n'
string|'\'"auth":"","email":"foo@bar.bar"}\''
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/images/ping/push'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'push_repository'
op|'('
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_commit_container
dedent|''
name|'def'
name|'test_commit_container'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/commit?container=XXX&repo=ping'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'201'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'client'
op|'.'
name|'commit_container'
op|'('
string|"'XXX'"
op|','
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_commit_container_bad_return_code
dedent|''
name|'def'
name|'test_commit_container_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
string|"'/v1.4/commit?container=XXX&repo=ping'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'400'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'client'
op|'.'
name|'commit_container'
op|'('
string|"'XXX'"
op|','
string|"'ping'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_container_logs
dedent|''
name|'def'
name|'test_get_container_logs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|"'/v1.4/containers/XXX/attach?logs=1&stream=0&stdout=1&stderr=1'"
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
name|'url'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'200'
op|','
name|'data'
op|'='
string|"'ping pong'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'client'
op|'.'
name|'get_container_logs'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ping pong'"
op|','
name|'logs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_container_logs_bad_return_code
dedent|''
name|'def'
name|'test_get_container_logs_bad_return_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_conn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
string|"'/v1.4/containers/XXX/attach?logs=1&stream=0&stdout=1&stderr=1'"
newline|'\n'
name|'mock_conn'
op|'.'
name|'request'
op|'('
string|"'POST'"
op|','
name|'url'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'FakeResponse'
op|'('
number|'404'
op|')'
newline|'\n'
name|'mock_conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'response'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'client'
op|'='
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'DockerHTTPClient'
op|'('
name|'mock_conn'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'client'
op|'.'
name|'get_container_logs'
op|'('
string|"'XXX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'logs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
