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
name|'import'
name|'uuid'
name|'as'
name|'uuid_lib'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
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
name|'import'
name|'cloudpipe'
name|'as'
name|'cloudpipe_v21'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
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
DECL|variable|project_id
name|'project_id'
op|'='
name|'str'
op|'('
name|'uuid_lib'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
op|')'
newline|'\n'
DECL|variable|uuid
name|'uuid'
op|'='
name|'str'
op|'('
name|'uuid_lib'
op|'.'
name|'uuid4'
op|'('
op|')'
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
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'id'
op|'='
number|'7'
op|','
name|'image_ref'
op|'='
name|'CONF'
op|'.'
name|'vpn_image_id'
op|','
name|'vm_state'
op|'='
string|"'active'"
op|','
nl|'\n'
name|'created_at'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
string|"'1981-10-20T00:00:00.000000'"
op|')'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|','
name|'project_id'
op|'='
name|'project_id'
op|')'
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
op|','
name|'want_objects'
op|'='
name|'True'
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
op|','
name|'want_objects'
op|'='
name|'True'
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
DECL|class|CloudpipeTestV21
dedent|''
name|'class'
name|'CloudpipeTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|cloudpipe
indent|'    '
name|'cloudpipe'
op|'='
name|'cloudpipe_v21'
newline|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'/v2/fake/os-cloudpipe'"
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
name|'CloudpipeTestV21'
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
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
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
name|'project_id'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'uuid'
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
name|'project_id'
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
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
name|'project_id'
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
name|'uuid'
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
name|'project_id'
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
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'uuid'
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
name|'project_id'
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
name|'self'
op|'.'
name|'url'
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
op|'='
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
name|'project_id'
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
name|'self'
op|'.'
name|'url'
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
op|'='
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'uuid'
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
DECL|member|test_cloudpipe_create_with_bad_project_id_failed
dedent|''
name|'def'
name|'test_cloudpipe_create_with_bad_project_id_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'cloudpipe'"
op|':'
op|'{'
string|"'project_id'"
op|':'
string|"'bad.project.id'"
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
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
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
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CloudpipePolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'CloudpipePolicyEnforcementV21'
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
name|'CloudpipePolicyEnforcementV21'
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
name|'cloudpipe_v21'
op|'.'
name|'CloudpipeController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_common_policy_check
dedent|''
name|'def'
name|'_common_policy_check'
op|'('
name|'self'
op|','
name|'func'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-cloudpipe"'
newline|'\n'
name|'rule'
op|'='
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rule'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'func'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwarg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_policy_failed
dedent|''
name|'def'
name|'test_list_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_policy_failed
dedent|''
name|'def'
name|'test_create_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'cloudpipe'"
op|':'
op|'{'
string|"'project_id'"
op|':'
name|'uuid'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_policy_failed
dedent|''
name|'def'
name|'test_update_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"configure_project"'
op|':'
op|'{'
string|"'vpn_ip'"
op|':'
string|"'192.168.1.1'"
op|','
nl|'\n'
string|"'vpn_port'"
op|':'
number|'2000'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_common_policy_check'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'uuid'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
