begin_unit
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""\nTests of the new image services, both as a service layer,\nand as a WSGI layer\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
name|'urlparse'
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
name|'import'
name|'images'
name|'as'
name|'images_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'images_view'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
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
name|'image_fixtures'
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
nl|'\n'
DECL|variable|NS
name|'NS'
op|'='
string|'"{http://docs.openstack.org/compute/api/v1.1}"'
newline|'\n'
DECL|variable|ATOMNS
name|'ATOMNS'
op|'='
string|'"{http://www.w3.org/2005/Atom}"'
newline|'\n'
DECL|variable|NOW_API_FORMAT
name|'NOW_API_FORMAT'
op|'='
string|'"2010-10-11T10:30:22Z"'
newline|'\n'
DECL|variable|IMAGE_FIXTURES
name|'IMAGE_FIXTURES'
op|'='
name|'image_fixtures'
op|'.'
name|'get_image_fixtures'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesControllerTestV21
name|'class'
name|'ImagesControllerTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test of the OpenStack API /images application controller w/Glance.\n    """'
newline|'\n'
DECL|variable|image_controller_class
name|'image_controller_class'
op|'='
name|'images_v21'
op|'.'
name|'ImagesController'
newline|'\n'
DECL|variable|url_base
name|'url_base'
op|'='
string|"'/v3'"
newline|'\n'
DECL|variable|bookmark_base
name|'bookmark_base'
op|'='
string|"''"
newline|'\n'
DECL|variable|http_request
name|'http_request'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV21'
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
string|'"""Run before each test."""'
newline|'\n'
name|'super'
op|'('
name|'ImagesControllerTestV21'
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
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
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
name|'fakes'
op|'.'
name|'stub_out_compute_api_snapshot'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_compute_api_backup'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'image_controller_class'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'url_prefix'
op|'='
string|'"http://localhost%s/images"'
op|'%'
name|'self'
op|'.'
name|'url_base'
newline|'\n'
name|'self'
op|'.'
name|'bookmark_prefix'
op|'='
string|'"http://localhost%s/images"'
op|'%'
name|'self'
op|'.'
name|'bookmark_base'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
string|"'fa95aaf5-ab3b-4cd8-88c0-2be7dd051aaf'"
newline|'\n'
name|'self'
op|'.'
name|'server_uuid'
op|'='
string|'"aa640691-d1a7-4a67-9d3c-d35ee6b3cc74"'
newline|'\n'
name|'self'
op|'.'
name|'server_href'
op|'='
op|'('
nl|'\n'
string|'"http://localhost%s/servers/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'url_base'
op|','
nl|'\n'
name|'self'
op|'.'
name|'server_uuid'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'server_bookmark'
op|'='
op|'('
nl|'\n'
string|'"http://localhost%s/servers/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'bookmark_base'
op|','
nl|'\n'
name|'self'
op|'.'
name|'server_uuid'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'alternate'
op|'='
string|'"%s/images/%s"'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expected_image_123'
op|'='
op|'{'
nl|'\n'
string|'"image"'
op|':'
op|'{'
string|"'id'"
op|':'
string|"'123'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'public image'"
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|'}'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'NOW_API_FORMAT'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'NOW_API_FORMAT'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
string|"'minDisk'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'progress'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'minRam'"
op|':'
number|'128'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"%s/123"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
nl|'\n'
string|'"%s/123"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"alternate"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.image"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'alternate'
op|'%'
nl|'\n'
op|'('
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|','
nl|'\n'
number|'123'
op|')'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expected_image_124'
op|'='
op|'{'
nl|'\n'
string|'"image"'
op|':'
op|'{'
string|"'id'"
op|':'
string|"'124'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'queued snapshot'"
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"u'instance_uuid'"
op|':'
name|'self'
op|'.'
name|'server_uuid'
op|','
nl|'\n'
string|"u'user_id'"
op|':'
string|"u'fake'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'NOW_API_FORMAT'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'NOW_API_FORMAT'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'SAVING'"
op|','
nl|'\n'
string|"'progress'"
op|':'
number|'25'
op|','
nl|'\n'
string|"'minDisk'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'minRam'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'server_uuid'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'server_href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'server_bookmark'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"%s/124"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
nl|'\n'
string|'"%s/124"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"alternate"'
op|','
nl|'\n'
string|'"type"'
op|':'
nl|'\n'
string|'"application/vnd.openstack.image"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'alternate'
op|'%'
nl|'\n'
op|'('
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|','
nl|'\n'
number|'124'
op|')'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
DECL|member|test_get_image
name|'def'
name|'test_get_image'
op|'('
name|'self'
op|','
name|'get_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/123'"
op|')'
newline|'\n'
name|'actual_image'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'request'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'actual_image'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'self'
op|'.'
name|'expected_image_123'
op|')'
op|')'
newline|'\n'
name|'get_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'IMAGE_FIXTURES'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
DECL|member|test_get_image_with_custom_prefix
name|'def'
name|'test_get_image_with_custom_prefix'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_compute_link_prefix'
op|'='
string|"'https://zoo.com:42'"
op|','
nl|'\n'
name|'osapi_glance_link_prefix'
op|'='
string|"'http://circus.com:34'"
op|')'
newline|'\n'
name|'fake_req'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/124'"
op|')'
newline|'\n'
name|'actual_image'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'fake_req'
op|','
string|"'124'"
op|')'
newline|'\n'
nl|'\n'
name|'expected_image'
op|'='
name|'self'
op|'.'
name|'expected_image_124'
newline|'\n'
name|'expected_image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"https://zoo.com:42%s/images/124"'
op|'%'
name|'self'
op|'.'
name|'url_base'
op|')'
newline|'\n'
name|'expected_image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"https://zoo.com:42%s/images/124"'
op|'%'
name|'self'
op|'.'
name|'bookmark_base'
op|')'
newline|'\n'
name|'expected_image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"http://circus.com:34/images/124"'
op|')'
newline|'\n'
name|'expected_image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"server"'
op|']'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"https://zoo.com:42%s/servers/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'url_base'
op|','
nl|'\n'
name|'self'
op|'.'
name|'server_uuid'
op|')'
op|')'
newline|'\n'
name|'expected_image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"server"'
op|']'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"https://zoo.com:42%s/servers/%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'bookmark_base'
op|','
nl|'\n'
name|'self'
op|'.'
name|'server_uuid'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'actual_image'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected_image'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"''"
op|')'
op|')'
newline|'\n'
DECL|member|test_get_image_404
name|'def'
name|'test_get_image_404'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_req'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/unknown'"
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
name|'controller'
op|'.'
name|'show'
op|','
name|'fake_req'
op|','
string|"'unknown'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|','
name|'return_value'
op|'='
name|'IMAGE_FIXTURES'
op|')'
newline|'\n'
DECL|member|test_get_image_details
name|'def'
name|'test_get_image_details'
op|'('
name|'self'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
name|'get_all_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'response_list'
op|'='
name|'response'
op|'['
string|'"images"'
op|']'
newline|'\n'
nl|'\n'
name|'image_125'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_125'
op|'['
string|"'id'"
op|']'
op|'='
string|"'125'"
newline|'\n'
name|'image_125'
op|'['
string|"'name'"
op|']'
op|'='
string|"'saving snapshot'"
newline|'\n'
name|'image_125'
op|'['
string|"'progress'"
op|']'
op|'='
number|'50'
newline|'\n'
name|'image_125'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/125"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_125'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/125"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_125'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/125"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_126'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_126'
op|'['
string|"'id'"
op|']'
op|'='
string|"'126'"
newline|'\n'
name|'image_126'
op|'['
string|"'name'"
op|']'
op|'='
string|"'active snapshot'"
newline|'\n'
name|'image_126'
op|'['
string|"'status'"
op|']'
op|'='
string|"'ACTIVE'"
newline|'\n'
name|'image_126'
op|'['
string|"'progress'"
op|']'
op|'='
number|'100'
newline|'\n'
name|'image_126'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/126"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_126'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/126"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_126'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/126"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_127'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_127'
op|'['
string|"'id'"
op|']'
op|'='
string|"'127'"
newline|'\n'
name|'image_127'
op|'['
string|"'name'"
op|']'
op|'='
string|"'killed snapshot'"
newline|'\n'
name|'image_127'
op|'['
string|"'status'"
op|']'
op|'='
string|"'ERROR'"
newline|'\n'
name|'image_127'
op|'['
string|"'progress'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_127'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/127"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_127'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/127"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_127'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/127"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_128'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_128'
op|'['
string|"'id'"
op|']'
op|'='
string|"'128'"
newline|'\n'
name|'image_128'
op|'['
string|"'name'"
op|']'
op|'='
string|"'deleted snapshot'"
newline|'\n'
name|'image_128'
op|'['
string|"'status'"
op|']'
op|'='
string|"'DELETED'"
newline|'\n'
name|'image_128'
op|'['
string|"'progress'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_128'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/128"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_128'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/128"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_128'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/128"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_129'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_129'
op|'['
string|"'id'"
op|']'
op|'='
string|"'129'"
newline|'\n'
name|'image_129'
op|'['
string|"'name'"
op|']'
op|'='
string|"'pending_delete snapshot'"
newline|'\n'
name|'image_129'
op|'['
string|"'status'"
op|']'
op|'='
string|"'DELETED'"
newline|'\n'
name|'image_129'
op|'['
string|"'progress'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_129'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/129"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_129'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/129"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_129'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/129"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_130'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_123'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_130'
op|'['
string|"'id'"
op|']'
op|'='
string|"'130'"
newline|'\n'
name|'image_130'
op|'['
string|"'name'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'image_130'
op|'['
string|"'metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_130'
op|'['
string|"'minDisk'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_130'
op|'['
string|"'minRam'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_130'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/130"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_130'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/130"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_130'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/130"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_131'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'expected_image_123'
op|'['
string|'"image"'
op|']'
op|')'
newline|'\n'
name|'image_131'
op|'['
string|"'id'"
op|']'
op|'='
string|"'131'"
newline|'\n'
name|'image_131'
op|'['
string|"'name'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'image_131'
op|'['
string|"'metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_131'
op|'['
string|"'minDisk'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_131'
op|'['
string|"'minRam'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'image_131'
op|'['
string|'"links"'
op|']'
op|'['
number|'0'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/131"'
op|'%'
name|'self'
op|'.'
name|'url_prefix'
newline|'\n'
name|'image_131'
op|'['
string|'"links"'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
string|'"%s/131"'
op|'%'
name|'self'
op|'.'
name|'bookmark_prefix'
newline|'\n'
name|'image_131'
op|'['
string|'"links"'
op|']'
op|'['
number|'2'
op|']'
op|'['
string|'"href"'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s/images/131"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'self'
op|'.'
name|'expected_image_123'
op|'['
string|'"image"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_image_124'
op|'['
string|'"image"'
op|']'
op|','
nl|'\n'
name|'image_125'
op|','
name|'image_126'
op|','
name|'image_127'
op|','
nl|'\n'
name|'image_128'
op|','
name|'image_129'
op|','
name|'image_130'
op|','
nl|'\n'
name|'image_131'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'expected'
op|','
name|'matchers'
op|'.'
name|'DictListMatches'
op|'('
name|'response_list'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|')'
newline|'\n'
DECL|member|test_get_image_details_with_limit
name|'def'
name|'test_get_image_details_with_limit'
op|'('
name|'self'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
nl|'\n'
string|"'images/detail?limit=2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'request'
op|')'
newline|'\n'
name|'get_all_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'limit'
op|'='
number|'2'
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|')'
newline|'\n'
DECL|member|test_get_image_details_with_limit_and_page_size
name|'def'
name|'test_get_image_details_with_limit_and_page_size'
op|'('
name|'self'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?limit=2&page_size=1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'request'
op|')'
newline|'\n'
name|'get_all_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'limit'
op|'='
number|'2'
op|','
name|'filters'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'page_size'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|')'
newline|'\n'
DECL|member|_detail_request
name|'def'
name|'_detail_request'
op|'('
name|'self'
op|','
name|'filters'
op|','
name|'request'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'request'
op|')'
newline|'\n'
name|'get_all_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_with_name
dedent|''
name|'def'
name|'test_image_detail_filter_with_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'testname'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
nl|'\n'
string|"'?name=testname'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_with_status
dedent|''
name|'def'
name|'test_image_detail_filter_with_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'active'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
nl|'\n'
string|"'?status=ACTIVE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_with_property
dedent|''
name|'def'
name|'test_image_detail_filter_with_property'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'property-test'"
op|':'
string|"'3'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
nl|'\n'
string|"'?property-test=3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_server_href
dedent|''
name|'def'
name|'test_image_detail_filter_server_href'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'property-instance_uuid'"
op|':'
name|'self'
op|'.'
name|'uuid'
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?server='"
op|'+'
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_server_uuid
dedent|''
name|'def'
name|'test_image_detail_filter_server_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'property-instance_uuid'"
op|':'
name|'self'
op|'.'
name|'uuid'
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?server='"
op|'+'
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_changes_since
dedent|''
name|'def'
name|'test_image_detail_filter_changes_since'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'changes-since'"
op|':'
string|"'2011-01-24T17:08Z'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
nl|'\n'
string|"'?changes-since=2011-01-24T17:08Z'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_with_type
dedent|''
name|'def'
name|'test_image_detail_filter_with_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'property-image_type'"
op|':'
string|"'BASE'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?type=BASE'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_filter_not_supported
dedent|''
name|'def'
name|'test_image_detail_filter_not_supported'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
string|"'status'"
op|':'
string|"'active'"
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?status='"
nl|'\n'
string|"'ACTIVE&UNSUPPORTEDFILTER=testname'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_detail_no_filters
dedent|''
name|'def'
name|'test_image_detail_no_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detail_request'
op|'('
name|'filters'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|','
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'Invalid'
op|')'
newline|'\n'
DECL|member|test_image_detail_invalid_marker
name|'def'
name|'test_image_detail_invalid_marker'
op|'('
name|'self'
op|','
name|'_get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'?marker=invalid'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|','
nl|'\n'
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_alternate_link
dedent|''
name|'def'
name|'test_generate_alternate_link'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'view'
op|'='
name|'images_view'
op|'.'
name|'ViewBuilder'
op|'('
op|')'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/1'"
op|')'
newline|'\n'
name|'generated_url'
op|'='
name|'view'
op|'.'
name|'_get_alternate_link'
op|'('
name|'request'
op|','
number|'1'
op|')'
newline|'\n'
name|'actual_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'generated_url'
op|','
name|'actual_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_response
dedent|''
name|'def'
name|'_check_response'
op|'('
name|'self'
op|','
name|'controller_method'
op|','
name|'response'
op|','
name|'expected_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_code'
op|','
name|'controller_method'
op|'.'
name|'wsgi_code'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.delete'"
op|')'
newline|'\n'
DECL|member|test_delete_image
name|'def'
name|'test_delete_image'
op|'('
name|'self'
op|','
name|'delete_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/124'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'request'
op|','
string|"'124'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_response'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'response'
op|','
number|'204'
op|')'
newline|'\n'
name|'delete_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'124'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.delete'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|'('
name|'image_id'
op|'='
string|"'123'"
op|')'
op|')'
newline|'\n'
DECL|member|test_delete_deleted_image
name|'def'
name|'test_delete_deleted_image'
op|'('
name|'self'
op|','
name|'_delete_mocked'
op|')'
op|':'
newline|'\n'
comment|'# If you try to delete a deleted image, you get back 403 Forbidden.'
nl|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'request'
op|','
string|"'123'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.delete'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'123'"
op|')'
op|')'
newline|'\n'
DECL|member|test_delete_image_not_found
name|'def'
name|'test_delete_image_not_found'
op|'('
name|'self'
op|','
name|'_delete_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/300'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
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
name|'controller'
op|'.'
name|'delete'
op|','
name|'request'
op|','
string|"'300'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|','
name|'return_value'
op|'='
op|'['
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
DECL|member|test_get_image_next_link
name|'def'
name|'test_get_image_next_link'
op|'('
name|'self'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'imagesl?limit=1'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'request'
op|')'
newline|'\n'
name|'response_links'
op|'='
name|'response'
op|'['
string|"'images_links'"
op|']'
newline|'\n'
name|'href_parts'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'response_links'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'/images'"
op|','
name|'href_parts'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'href_parts'
op|'.'
name|'query'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
op|'{'
string|"'limit'"
op|':'
op|'['
string|"'1'"
op|']'
op|','
string|"'marker'"
op|':'
op|'['
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|']'
op|'}'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'params'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get_all'"
op|','
name|'return_value'
op|'='
op|'['
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|']'
op|')'
newline|'\n'
DECL|member|test_get_image_details_next_link
name|'def'
name|'test_get_image_details_next_link'
op|'('
name|'self'
op|','
name|'get_all_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'self'
op|'.'
name|'http_request'
op|'.'
name|'blank'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'images/detail?limit=1'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'request'
op|')'
newline|'\n'
name|'response_links'
op|'='
name|'response'
op|'['
string|"'images_links'"
op|']'
newline|'\n'
name|'href_parts'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'response_links'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'url_base'
op|'+'
string|"'/images/detail'"
op|','
name|'href_parts'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'params'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'href_parts'
op|'.'
name|'query'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
op|'{'
string|"'limit'"
op|':'
op|'['
string|"'1'"
op|']'
op|','
string|"'marker'"
op|':'
op|'['
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|']'
op|'}'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'params'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesControllerTestV2
dedent|''
dedent|''
name|'class'
name|'ImagesControllerTestV2'
op|'('
name|'ImagesControllerTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|image_controller_class
indent|'    '
name|'image_controller_class'
op|'='
name|'images'
op|'.'
name|'Controller'
newline|'\n'
DECL|variable|url_base
name|'url_base'
op|'='
string|"'/v2/fake'"
newline|'\n'
DECL|variable|bookmark_base
name|'bookmark_base'
op|'='
string|"'/fake'"
newline|'\n'
DECL|variable|http_request
name|'http_request'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
newline|'\n'
nl|'\n'
DECL|member|_check_response
name|'def'
name|'_check_response'
op|'('
name|'self'
op|','
name|'controller_method'
op|','
name|'response'
op|','
name|'expected_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_code'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
