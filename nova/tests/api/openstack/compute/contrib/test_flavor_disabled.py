begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'flavor_disabled'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_FLAVORS
name|'FAKE_FLAVORS'
op|'='
op|'{'
nl|'\n'
string|"'flavor 1'"
op|':'
op|'{'
nl|'\n'
string|'"flavorid"'
op|':'
string|"'1'"
op|','
nl|'\n'
string|'"name"'
op|':'
string|"'flavor 1'"
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
string|"'256'"
op|','
nl|'\n'
string|'"root_gb"'
op|':'
string|"'10'"
op|','
nl|'\n'
string|'"disabled"'
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'flavor 2'"
op|':'
op|'{'
nl|'\n'
string|'"flavorid"'
op|':'
string|"'2'"
op|','
nl|'\n'
string|'"name"'
op|':'
string|"'flavor 2'"
op|','
nl|'\n'
string|'"memory_mb"'
op|':'
string|"'512'"
op|','
nl|'\n'
string|'"root_gb"'
op|':'
string|"'20'"
op|','
nl|'\n'
string|'"disabled"'
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_by_flavor_id
name|'def'
name|'fake_instance_type_get_by_flavor_id'
op|'('
name|'flavorid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FAKE_FLAVORS'
op|'['
string|"'flavor %s'"
op|'%'
name|'flavorid'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_type_get_all
dedent|''
name|'def'
name|'fake_instance_type_get_all'
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
name|'FAKE_FLAVORS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorDisabledTest
dedent|''
name|'class'
name|'FlavorDisabledTest'
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
DECL|variable|prefix
name|'prefix'
op|'='
string|"'%s:'"
op|'%'
name|'flavor_disabled'
op|'.'
name|'Flavor_disabled'
op|'.'
name|'alias'
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
name|'FlavorDisabledTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext'
op|'='
op|'('
string|"'nova.api.openstack.compute.contrib'"
nl|'\n'
string|"'.flavor_disabled.Flavor_disabled'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_compute_extension'
op|'='
op|'['
name|'ext'
op|']'
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
name|'instance_types'
op|','
string|'"get_all_types"'
op|','
nl|'\n'
name|'fake_instance_type_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
nl|'\n'
string|'"get_instance_type_by_flavor_id"'
op|','
nl|'\n'
name|'fake_instance_type_get_by_flavor_id'
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
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor
dedent|''
name|'def'
name|'_get_flavor'
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
string|"'flavor'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flavors
dedent|''
name|'def'
name|'_get_flavors'
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
string|"'flavors'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorDisabled
dedent|''
name|'def'
name|'assertFlavorDisabled'
op|'('
name|'self'
op|','
name|'flavor'
op|','
name|'disabled'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'flavor'
op|'.'
name|'get'
op|'('
string|"'%sdisabled'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|')'
op|','
name|'disabled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
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
string|"'/v2/fake/flavors/1'"
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
name|'self'
op|'.'
name|'assertFlavorDisabled'
op|'('
name|'self'
op|'.'
name|'_get_flavor'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|','
string|"'False'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
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
string|"'/v2/fake/flavors/detail'"
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
name|'flavors'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorDisabled'
op|'('
name|'flavors'
op|'['
number|'0'
op|']'
op|','
string|"'False'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorDisabled'
op|'('
name|'flavors'
op|'['
number|'1'
op|']'
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorDisabledXmlTest
dedent|''
dedent|''
name|'class'
name|'FlavorDisabledXmlTest'
op|'('
name|'FlavorDisabledTest'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'{%s}'"
op|'%'
name|'flavor_disabled'
op|'.'
name|'Flavor_disabled'
op|'.'
name|'namespace'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor
name|'def'
name|'_get_flavor'
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
DECL|member|_get_flavors
dedent|''
name|'def'
name|'_get_flavors'
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
dedent|''
dedent|''
endmarker|''
end_unit
