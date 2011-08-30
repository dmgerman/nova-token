begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'base64'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
name|'import'
name|'createserverext'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rpc'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
DECL|variable|FAKE_NETWORKS
name|'FAKE_NETWORKS'
op|'='
op|'['
op|'('
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
string|"'10.0.1.12'"
op|')'
op|','
nl|'\n'
op|'('
string|"'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'"
op|','
string|"'10.0.2.12'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|DUPLICATE_NETWORKS
name|'DUPLICATE_NETWORKS'
op|'='
op|'['
op|'('
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
string|"'10.0.1.12'"
op|')'
op|','
nl|'\n'
op|'('
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
string|"'10.0.1.12'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|INVALID_NETWORKS
name|'INVALID_NETWORKS'
op|'='
op|'['
op|'('
string|"'invalid'"
op|','
string|"'invalid-ip-address'"
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateserverextTest
name|'class'
name|'CreateserverextTest'
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
name|'CreateserverextTest'
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
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_auth'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'allow_admin'
op|'='
name|'FLAGS'
op|'.'
name|'allow_admin_api'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
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
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'self'
op|'.'
name|'allow_admin'
newline|'\n'
name|'super'
op|'('
name|'CreateserverextTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_mock_compute_api
dedent|''
name|'def'
name|'_setup_mock_compute_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|MockComputeAPI
indent|'        '
name|'class'
name|'MockComputeAPI'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'injected_files'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'networks'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'injected_files'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'injected_files'
op|'='
name|'kwargs'
op|'['
string|"'injected_files'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'injected_files'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'requested_networks'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'networks'
op|'='
name|'kwargs'
op|'['
string|"'requested_networks'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'networks'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'1234'"
op|','
string|"'display_name'"
op|':'
string|"'fakeinstance'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|'""'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|'""'
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|make_stub_method
dedent|''
dedent|''
name|'def'
name|'make_stub_method'
op|'('
name|'canned_return'
op|')'
op|':'
newline|'\n'
DECL|function|stub_method
indent|'            '
name|'def'
name|'stub_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'canned_return'
newline|'\n'
dedent|''
name|'return'
name|'stub_method'
newline|'\n'
nl|'\n'
dedent|''
name|'compute_api'
op|'='
name|'MockComputeAPI'
op|'('
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
name|'compute'
op|','
string|"'API'"
op|','
name|'make_stub_method'
op|'('
name|'compute_api'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'create_instance_helper'
op|'.'
name|'CreateInstanceHelper'
op|','
nl|'\n'
string|"'_get_kernel_ramdisk_from_image'"
op|','
name|'make_stub_method'
op|'('
op|'('
number|'1'
op|','
number|'1'
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'compute_api'
newline|'\n'
nl|'\n'
DECL|member|_create_networks_request_dict
dedent|''
name|'def'
name|'_create_networks_request_dict'
op|'('
name|'self'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
string|"'new-server-test'"
newline|'\n'
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'if'
name|'networks'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'network_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'uuid'
op|','
name|'fixed_ip'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'                '
name|'network_list'
op|'.'
name|'append'
op|'('
op|'{'
string|"'uuid'"
op|':'
name|'uuid'
op|','
string|"'fixed_ip'"
op|':'
name|'fixed_ip'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'['
string|"'networks'"
op|']'
op|'='
name|'network_list'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_create_request_json
dedent|''
name|'def'
name|'_get_create_request_json'
op|'('
name|'self'
op|','
name|'body_dict'
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
string|"'/v1.1/123/os-create-server-ext'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
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
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|_run_create_instance_with_mock_compute_api
dedent|''
name|'def'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute_api'
op|'='
name|'self'
op|'.'
name|'_setup_mock_compute_api'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'compute_api'
op|','
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_format_xml_request_body
dedent|''
name|'def'
name|'_format_xml_request_body'
op|'('
name|'self'
op|','
name|'body_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'body_dict'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'body_parts'
op|'='
op|'['
op|']'
newline|'\n'
name|'body_parts'
op|'.'
name|'extend'
op|'('
op|'['
nl|'\n'
string|'\'<?xml version="1.0" encoding="UTF-8"?>\''
op|','
nl|'\n'
string|'\'<server xmlns="http://docs.rackspacecloud.com/servers/api/v1.1"\''
op|','
nl|'\n'
string|'\' name="%s" imageRef="%s" flavorRef="%s">\''
op|'%'
op|'('
nl|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|','
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|','
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|')'
op|']'
op|')'
newline|'\n'
name|'if'
string|"'metadata'"
name|'in'
name|'server'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'server'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'<metadata>'"
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'body_parts'
op|'.'
name|'append'
op|'('
string|'\'<meta key="%s">%s</meta>\''
op|'%'
name|'item'
op|')'
newline|'\n'
dedent|''
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'</metadata>'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'personality'"
name|'in'
name|'server'
op|':'
newline|'\n'
indent|'            '
name|'personalities'
op|'='
name|'server'
op|'['
string|"'personality'"
op|']'
newline|'\n'
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'<personality>'"
op|')'
newline|'\n'
name|'for'
name|'file'
name|'in'
name|'personalities'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'='
op|'('
name|'file'
op|'['
string|"'path'"
op|']'
op|','
name|'file'
op|'['
string|"'contents'"
op|']'
op|')'
newline|'\n'
name|'body_parts'
op|'.'
name|'append'
op|'('
string|'\'<file path="%s">%s</file>\''
op|'%'
name|'item'
op|')'
newline|'\n'
dedent|''
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'</personality>'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'networks'"
name|'in'
name|'server'
op|':'
newline|'\n'
indent|'            '
name|'networks'
op|'='
name|'server'
op|'['
string|"'networks'"
op|']'
newline|'\n'
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'<networks>'"
op|')'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'='
op|'('
name|'network'
op|'['
string|"'uuid'"
op|']'
op|','
name|'network'
op|'['
string|"'fixed_ip'"
op|']'
op|')'
newline|'\n'
name|'body_parts'
op|'.'
name|'append'
op|'('
string|'\'<network uuid="%s" fixed_ip="%s"></network>\''
nl|'\n'
op|'%'
name|'item'
op|')'
newline|'\n'
dedent|''
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'</networks>'"
op|')'
newline|'\n'
dedent|''
name|'body_parts'
op|'.'
name|'append'
op|'('
string|"'</server>'"
op|')'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'body_parts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_create_request_xml
dedent|''
name|'def'
name|'_get_create_request_xml'
op|'('
name|'self'
op|','
name|'body_dict'
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
string|"'/v1.1/123/os-create-server-ext'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|"'application/xml'"
newline|'\n'
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
name|'_format_xml_request_body'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_with_networks_json
dedent|''
name|'def'
name|'_create_instance_with_networks_json'
op|'('
name|'self'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
name|'networks'
op|')'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_json'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'return'
name|'request'
op|','
name|'response'
op|','
name|'compute_api'
op|'.'
name|'networks'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_with_networks_xml
dedent|''
name|'def'
name|'_create_instance_with_networks_xml'
op|'('
name|'self'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
name|'networks'
op|')'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_xml'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'return'
name|'request'
op|','
name|'response'
op|','
name|'compute_api'
op|'.'
name|'networks'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_no_networks
dedent|''
name|'def'
name|'test_create_instance_with_no_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'networks'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_no_networks_xml
dedent|''
name|'def'
name|'test_create_instance_with_no_networks_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
name|'networks'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_one_network
dedent|''
name|'def'
name|'test_create_instance_with_one_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_one_network_xml
dedent|''
name|'def'
name|'test_create_instance_with_one_network_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_two_networks
dedent|''
name|'def'
name|'test_create_instance_with_two_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_two_networks_xml
dedent|''
name|'def'
name|'test_create_instance_with_two_networks_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'FAKE_NETWORKS'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_duplicate_networks
dedent|''
name|'def'
name|'test_create_instance_with_duplicate_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'DUPLICATE_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_duplicate_networks_xml
dedent|''
name|'def'
name|'test_create_instance_with_duplicate_networks_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
name|'DUPLICATE_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_no_id
dedent|''
name|'def'
name|'test_create_instance_with_network_no_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'del'
name|'body_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'networks'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_json'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'compute_api'
op|'.'
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_no_id_xml
dedent|''
name|'def'
name|'test_create_instance_with_network_no_id_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_xml'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|'\' uuid="aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa"\''
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'request'
op|'.'
name|'body'
op|'.'
name|'replace'
op|'('
name|'uuid'
op|','
string|"''"
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'compute_api'
op|'.'
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_invalid_id
dedent|''
name|'def'
name|'test_create_instance_with_network_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'INVALID_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_invalid_id_xml
dedent|''
name|'def'
name|'test_create_instance_with_network_invalid_id_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
name|'INVALID_NETWORKS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_empty_fixed_ip
dedent|''
name|'def'
name|'test_create_instance_with_network_empty_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'='
op|'['
op|'('
string|"'1'"
op|','
string|"''"
op|')'
op|']'
newline|'\n'
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_non_string_fixed_ip
dedent|''
name|'def'
name|'test_create_instance_with_network_non_string_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'='
op|'['
op|'('
string|"'1'"
op|','
number|'12345'
op|')'
op|']'
newline|'\n'
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_json'
op|'('
name|'networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_empty_fixed_ip_xml
dedent|''
name|'def'
name|'test_create_instance_with_network_empty_fixed_ip_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'='
op|'['
op|'('
string|"'1'"
op|','
string|"''"
op|')'
op|']'
newline|'\n'
name|'request'
op|','
name|'response'
op|','
name|'networks'
op|'='
name|'self'
op|'.'
name|'_create_instance_with_networks_xml'
op|'('
name|'networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'networks'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_no_fixed_ip
dedent|''
name|'def'
name|'test_create_instance_with_network_no_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'del'
name|'body_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'networks'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'fixed_ip'"
op|']'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_json'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'compute_api'
op|'.'
name|'networks'
op|','
nl|'\n'
op|'['
op|'('
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
name|'None'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_network_no_fixed_ip_xml
dedent|''
name|'def'
name|'test_create_instance_with_network_no_fixed_ip_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_dict'
op|'='
name|'self'
op|'.'
name|'_create_networks_request_dict'
op|'('
op|'['
name|'FAKE_NETWORKS'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'_get_create_request_xml'
op|'('
name|'body_dict'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'request'
op|'.'
name|'body'
op|'.'
name|'replace'
op|'('
string|'\' fixed_ip="10.0.1.12"\''
op|','
string|"''"
op|')'
newline|'\n'
name|'compute_api'
op|','
name|'response'
op|'='
name|'self'
op|'.'
name|'_run_create_instance_with_mock_compute_api'
op|'('
name|'request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'compute_api'
op|'.'
name|'networks'
op|','
nl|'\n'
op|'['
op|'('
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
op|','
name|'None'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
