begin_unit
comment|'# Copyright 2010-2011 OpenStack Foundation'
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
name|'as'
name|'stdlib_uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
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
name|'views'
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
name|'matchers'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NS
name|'NS'
op|'='
op|'{'
nl|'\n'
string|"'atom'"
op|':'
string|"'http://www.w3.org/2005/Atom'"
op|','
nl|'\n'
string|"'ns'"
op|':'
string|"'http://docs.openstack.org/common/api/v1.0'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|EXP_LINKS
name|'EXP_LINKS'
op|'='
op|'{'
nl|'\n'
string|"'v2.0'"
op|':'
op|'{'
nl|'\n'
string|"'html'"
op|':'
string|"'http://docs.openstack.org/'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'v2.1'"
op|':'
op|'{'
nl|'\n'
string|"'html'"
op|':'
string|"'http://docs.openstack.org/'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|EXP_VERSIONS
name|'EXP_VERSIONS'
op|'='
op|'{'
nl|'\n'
string|'"v2.0"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"text/html"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'EXP_LINKS'
op|'['
string|"'v2.0'"
op|']'
op|'['
string|"'html'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json;version=2"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"v2.1"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'"2.11"'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'"2.1"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2013-07-23T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2.1/"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"text/html"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'EXP_LINKS'
op|'['
string|"'v2.1'"
op|']'
op|'['
string|"'html'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json;version=2.1"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_self_href
name|'def'
name|'_get_self_href'
op|'('
name|'response'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract the URL to self from response data."""'
newline|'\n'
name|'data'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'for'
name|'link'
name|'in'
name|'data'
op|'['
string|"'versions'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'links'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'link'
op|'['
string|"'rel'"
op|']'
op|'=='
string|"'self'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'link'
op|'['
string|"'href'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsTestV20
dedent|''
name|'class'
name|'VersionsTestV20'
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
name|'VersionsTestV20'
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
name|'wsgi_app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_list
dedent|''
name|'def'
name|'test_get_version_list'
op|'('
name|'self'
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
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'versions'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|'"versions"'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2/"'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'"2.11"'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'"2.1"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2013-07-23T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2.1/"'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'versions'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_list_302
dedent|''
name|'def'
name|'test_get_version_list_302'
op|'('
name|'self'
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
string|"'/v2'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'302'
op|')'
newline|'\n'
name|'redirect_req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'location'
op|','
name|'redirect_req'
op|'.'
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_get_version_2_detail
dedent|''
name|'def'
name|'_test_get_version_2_detail'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'accept'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'accept'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
dedent|''
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
name|'req'
op|'.'
name|'accept'
op|'='
name|'accept'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'version'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"version"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2/"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"text/html"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'EXP_LINKS'
op|'['
string|"'v2.0'"
op|']'
op|'['
string|"'html'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/"'
nl|'\n'
string|'"vnd.openstack.compute+json;version=2"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_2_detail
dedent|''
name|'def'
name|'test_get_version_2_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_get_version_2_detail'
op|'('
string|"'/v2/'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_2_detail_content_type
dedent|''
name|'def'
name|'test_get_version_2_detail_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'accept'
op|'='
string|'"application/json;version=2"'
newline|'\n'
name|'self'
op|'.'
name|'_test_get_version_2_detail'
op|'('
string|"'/'"
op|','
name|'accept'
op|'='
name|'accept'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_2_versions_invalid
dedent|''
name|'def'
name|'test_get_version_2_versions_invalid'
op|'('
name|'self'
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
string|"'/v2/versions/1234'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_choice_image
dedent|''
name|'def'
name|'test_multi_choice_image'
op|'('
name|'self'
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
string|"'/images/1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"choices"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2/images/1"'
op|','
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json"'
nl|'\n'
string|'";version=2"'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2.1/images/1"'
op|','
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
nl|'\n'
string|'"application/vnd.openstack.compute+json;version=2.1"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_choice_server_atom
dedent|''
name|'def'
name|'test_multi_choice_server_atom'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure multi choice responses do not have content-type\n        application/atom+xml (should use default of json)\n        """'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/servers'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/atom+xml"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_choice_server
dedent|''
name|'def'
name|'test_multi_choice_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'str'
op|'('
name|'stdlib_uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/servers/'"
op|'+'
name|'uuid'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'wsgi_app'
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
number|'300'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"choices"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2/servers/"'
op|'+'
name|'uuid'
op|','
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json"'
nl|'\n'
string|'";version=2"'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v2.1/servers/"'
op|'+'
name|'uuid'
op|','
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
nl|'\n'
string|'"application/vnd.openstack.compute+json;version=2.1"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsViewBuilderTests
dedent|''
dedent|''
name|'class'
name|'VersionsViewBuilderTests'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_view_builder
indent|'    '
name|'def'
name|'test_view_builder'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"http://example.org/"'
newline|'\n'
nl|'\n'
name|'version_data'
op|'='
op|'{'
nl|'\n'
string|'"v3.2.1"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"3.2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'"2.3"'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'"2.1"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-07-18T11:30:00Z"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"versions"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"3.2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'"2.3"'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'"2.1"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-07-18T11:30:00Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://example.org/v2/"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'views'
op|'.'
name|'versions'
op|'.'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
name|'output'
op|'='
name|'builder'
op|'.'
name|'build_versions'
op|'('
name|'version_data'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_href
dedent|''
name|'def'
name|'test_generate_href'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"http://example.org/app/"'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
string|'"http://example.org/app/v2/"'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'views'
op|'.'
name|'versions'
op|'.'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'builder'
op|'.'
name|'generate_href'
op|'('
string|"'v2'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_href_v21
dedent|''
name|'def'
name|'test_generate_href_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"http://example.org/app/"'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
string|'"http://example.org/app/v2.1/"'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'views'
op|'.'
name|'versions'
op|'.'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'builder'
op|'.'
name|'generate_href'
op|'('
string|"'v2.1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_href_unknown
dedent|''
name|'def'
name|'test_generate_href_unknown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"http://example.org/app/"'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
string|'"http://example.org/app/v2/"'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'views'
op|'.'
name|'versions'
op|'.'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'builder'
op|'.'
name|'generate_href'
op|'('
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(oomichi): Now version API of v2.0 covers "/"(root).'
nl|'\n'
comment|'# So this class tests "/v2.1" only for v2.1 API.'
nl|'\n'
DECL|class|VersionsTestV21
dedent|''
dedent|''
name|'class'
name|'VersionsTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|exp_versions
indent|'    '
name|'exp_versions'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'EXP_VERSIONS'
op|')'
newline|'\n'
name|'exp_versions'
op|'['
string|"'v2.0'"
op|']'
op|'['
string|"'links'"
op|']'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
nl|'\n'
op|'{'
string|"'href'"
op|':'
string|"'http://localhost/v2.1/'"
op|','
string|"'rel'"
op|':'
string|"'self'"
op|'}'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_list_302
name|'def'
name|'test_get_version_list_302'
op|'('
name|'self'
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
string|"'/v2.1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'302'
op|')'
newline|'\n'
name|'redirect_req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2.1/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'location'
op|','
name|'redirect_req'
op|'.'
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_21_detail
dedent|''
name|'def'
name|'test_get_version_21_detail'
op|'('
name|'self'
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
string|"'/v2.1/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'version'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"version"'
op|':'
name|'self'
op|'.'
name|'exp_versions'
op|'['
string|"'v2.1'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_21_versions_v21_detail
dedent|''
name|'def'
name|'test_get_version_21_versions_v21_detail'
op|'('
name|'self'
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
string|"'/v2.1/fake/versions/v2.1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'version'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"version"'
op|':'
name|'self'
op|'.'
name|'exp_versions'
op|'['
string|"'v2.1'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_21_versions_v20_detail
dedent|''
name|'def'
name|'test_get_version_21_versions_v20_detail'
op|'('
name|'self'
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
string|"'/v2.1/fake/versions/v2.0'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'version'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"version"'
op|':'
name|'self'
op|'.'
name|'exp_versions'
op|'['
string|"'v2.0'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_21_versions_invalid
dedent|''
name|'def'
name|'test_get_version_21_versions_invalid'
op|'('
name|'self'
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
string|"'/v2.1/versions/1234'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_version_21_detail_content_type
dedent|''
name|'def'
name|'test_get_version_21_detail_content_type'
op|'('
name|'self'
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
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json;version=2.1"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
op|')'
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
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'version'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|'"version"'
op|':'
name|'self'
op|'.'
name|'exp_versions'
op|'['
string|"'v2.1'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionBehindSslTestCase
dedent|''
dedent|''
name|'class'
name|'VersionBehindSslTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'VersionBehindSslTestCase'
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
name|'flags'
op|'('
name|'secure_proxy_ssl_header'
op|'='
string|"'HTTP_X_FORWARDED_PROTO'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_versions_without_headers
dedent|''
name|'def'
name|'test_versions_without_headers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'href'
op|'='
name|'_get_self_href'
op|'('
name|'res'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'href'
op|'.'
name|'startswith'
op|'('
string|"'http://'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_versions_with_header
dedent|''
name|'def'
name|'test_versions_with_header'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-Forwarded-Proto'"
op|']'
op|'='
string|"'https'"
newline|'\n'
name|'res'
op|'='
name|'req'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'href'
op|'='
name|'_get_self_href'
op|'('
name|'res'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'href'
op|'.'
name|'startswith'
op|'('
string|"'https://'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsTestV21WithV2CompatibleWrapper
dedent|''
dedent|''
name|'class'
name|'VersionsTestV21WithV2CompatibleWrapper'
op|'('
name|'VersionsTestV20'
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
name|'VersionsTestV21WithV2CompatibleWrapper'
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
name|'wsgi_app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'v2_compatible'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
