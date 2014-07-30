begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
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
name|'cloudpipe'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'matchers'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
string|"'vpn_image_id'"
op|','
string|"'nova.cloudpipe.pipelib'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_vpn_instance
name|'def'
name|'fake_vpn_instance'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'7'
op|','
string|"'image_ref'"
op|':'
name|'CONF'
op|'.'
name|'vpn_image_id'
op|','
string|"'vm_state'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
string|"'1981-10-20T00:00:00.000000'"
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
number|'7777'
op|','
string|"'project_id'"
op|':'
string|"'other'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get_all_empty
dedent|''
name|'def'
name|'compute_api_get_all_empty'
op|'('
name|'context'
op|','
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get_all
dedent|''
name|'def'
name|'compute_api_get_all'
op|'('
name|'context'
op|','
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'fake_vpn_instance'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utils_vpn_ping
dedent|''
name|'def'
name|'utils_vpn_ping'
op|'('
name|'addr'
op|','
name|'port'
op|','
name|'timoeout'
op|'='
number|'0.05'
op|','
name|'session_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipeTest
dedent|''
name|'class'
name|'CloudpipeTest'
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
name|'CloudpipeTest'
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
name|'cloudpipe'
op|'.'
name|'CloudpipeController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|'"get_all"'
op|','
nl|'\n'
name|'compute_api_get_all_empty'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'vpn_ping'"
op|','
name|'utils_vpn_ping'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cloudpipe_list_no_network
dedent|''
name|'def'
name|'test_cloudpipe_list_no_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_get_nw_info_for_instance
indent|'        '
name|'def'
name|'fake_get_nw_info_for_instance'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
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
name|'compute_utils'
op|','
string|'"get_nw_info_for_instance"'
op|','
nl|'\n'
name|'fake_get_nw_info_for_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|'"get_all"'
op|','
nl|'\n'
name|'compute_api_get_all'
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
string|"'/v2/fake/os-cloudpipe'"
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
op|'{'
string|"'cloudpipes'"
op|':'
op|'['
op|'{'
string|"'project_id'"
op|':'
string|"'other'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'7777'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'1981-10-20T00:00:00Z'"
op|'}'
op|']'
op|'}'
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
DECL|member|test_cloudpipe_list
dedent|''
name|'def'
name|'test_cloudpipe_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|network_api_get
indent|'        '
name|'def'
name|'network_api_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
string|"'other'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'vpn_public_address'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'vpn_public_port'"
op|':'
number|'22'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_get_nw_info_for_instance
dedent|''
name|'def'
name|'fake_get_nw_info_for_instance'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake_network'
op|'.'
name|'fake_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'compute_utils'
op|','
string|'"get_nw_info_for_instance"'
op|','
nl|'\n'
name|'fake_get_nw_info_for_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'network_api'
op|','
string|'"get"'
op|','
nl|'\n'
name|'network_api_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|'"get_all"'
op|','
nl|'\n'
name|'compute_api_get_all'
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
string|"'/v2/fake/os-cloudpipe'"
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
op|'{'
string|"'cloudpipes'"
op|':'
op|'['
op|'{'
string|"'project_id'"
op|':'
string|"'other'"
op|','
nl|'\n'
string|"'internal_ip'"
op|':'
string|"'192.168.1.100'"
op|','
nl|'\n'
string|"'public_ip'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'public_port'"
op|':'
number|'22'
op|','
nl|'\n'
string|"'state'"
op|':'
string|"'running'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'7777'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'1981-10-20T00:00:00Z'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'res_dict'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'response'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cloudpipe_create
dedent|''
name|'def'
name|'test_cloudpipe_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|launch_vpn_instance
indent|'        '
name|'def'
name|'launch_vpn_instance'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
op|'['
name|'fake_vpn_instance'
op|'('
op|')'
op|']'
op|','
string|"'fake-reservation'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cloudpipe'
op|','
string|"'launch_vpn_instance'"
op|','
nl|'\n'
name|'launch_vpn_instance'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'cloudpipe'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-cloudpipe'"
op|')'
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
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'instance_id'"
op|':'
number|'7777'
op|'}'
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
DECL|member|test_cloudpipe_create_no_networks
dedent|''
name|'def'
name|'test_cloudpipe_create_no_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|launch_vpn_instance
indent|'        '
name|'def'
name|'launch_vpn_instance'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoMoreNetworks'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cloudpipe'
op|','
string|"'launch_vpn_instance'"
op|','
nl|'\n'
name|'launch_vpn_instance'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'cloudpipe'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-cloudpipe'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
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
DECL|member|test_cloudpipe_create_already_running
dedent|''
name|'def'
name|'test_cloudpipe_create_already_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|launch_vpn_instance
indent|'        '
name|'def'
name|'launch_vpn_instance'
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
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Method should not have been called"'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cloudpipe'
op|','
string|"'launch_vpn_instance'"
op|','
nl|'\n'
name|'launch_vpn_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|'"get_all"'
op|','
nl|'\n'
name|'compute_api_get_all'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'cloudpipe'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-cloudpipe'"
op|')'
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
name|'response'
op|'='
op|'{'
string|"'instance_id'"
op|':'
number|'7777'
op|'}'
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
nl|'\n'
DECL|class|CloudpipesXMLSerializerTest
dedent|''
dedent|''
name|'class'
name|'CloudpipesXMLSerializerTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_default_serializer
indent|'    '
name|'def'
name|'test_default_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'cloudpipe'
op|'.'
name|'CloudpipeTemplate'
op|'('
op|')'
newline|'\n'
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'cloudpipe'
op|'='
name|'dict'
op|'('
name|'instance_id'
op|'='
string|"'1234-1234-1234-1234'"
op|')'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cloudpipe'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'child'
op|'.'
name|'tag'
op|','
name|'exemplar'
op|'['
string|"'cloudpipe'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'text'
op|','
name|'exemplar'
op|'['
string|"'cloudpipe'"
op|']'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'cloudpipe'
op|'.'
name|'CloudpipesTemplate'
op|'('
op|')'
newline|'\n'
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'cloudpipes'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'project_id'
op|'='
string|"'1234'"
op|','
nl|'\n'
name|'public_ip'
op|'='
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'public_port'
op|'='
string|"'321'"
op|','
nl|'\n'
name|'instance_id'
op|'='
string|"'1234-1234-1234-1234'"
op|','
nl|'\n'
name|'created_at'
op|'='
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|','
nl|'\n'
name|'state'
op|'='
string|"'running'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'project_id'
op|'='
string|"'4321'"
op|','
nl|'\n'
name|'public_ip'
op|'='
string|"'4.3.2.1'"
op|','
nl|'\n'
name|'public_port'
op|'='
string|"'123'"
op|','
nl|'\n'
name|'state'
op|'='
string|"'pending'"
op|')'
op|']'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cloudpipes'"
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
name|'exemplar'
op|'['
string|"'cloudpipes'"
op|']'
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
name|'cl_pipe'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kp_data'
op|'='
name|'exemplar'
op|'['
string|"'cloudpipes'"
op|']'
op|'['
name|'idx'
op|']'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'cl_pipe'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'child'
op|'.'
name|'tag'
op|','
name|'kp_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'text'
op|','
name|'kp_data'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserializer
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
op|')'
newline|'\n'
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'cloudpipe'
op|'='
name|'dict'
op|'('
name|'project_id'
op|'='
string|"'4321'"
op|')'
op|')'
newline|'\n'
name|'intext'
op|'='
op|'('
string|'"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\\n"'
nl|'\n'
string|"'<cloudpipe><project_id>4321</project_id></cloudpipe>'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
op|'['
string|"'body'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'exemplar'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
