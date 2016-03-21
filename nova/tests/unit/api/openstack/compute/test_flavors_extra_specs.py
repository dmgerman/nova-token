begin_unit
comment|'# Copyright 2011 University of Southern California'
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
name|'mock'
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
name|'flavors_extraspecs'
name|'as'
name|'flavorextraspecs_v21'
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
op|'.'
name|'contrib'
name|'import'
name|'flavorextraspecs'
name|'as'
name|'flavorextraspecs_v2'
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
op|'.'
name|'objects'
name|'import'
name|'test_flavor'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_create_flavor_extra_specs
name|'def'
name|'return_create_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'extra_specs'
op|','
nl|'\n'
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
name|'stub_flavor_extra_specs'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_flavor_extra_specs
dedent|''
name|'def'
name|'return_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_flavor_extra_specs'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_flavor_extra_specs_item
dedent|''
name|'def'
name|'return_flavor_extra_specs_item'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'key'
op|':'
name|'stub_flavor_extra_specs'
op|'('
op|')'
op|'['
name|'key'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_empty_flavor_extra_specs
dedent|''
name|'def'
name|'return_empty_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_flavor_extra_specs
dedent|''
name|'def'
name|'delete_flavor_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_flavor_extra_specs
dedent|''
name|'def'
name|'stub_flavor_extra_specs'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'specs'
op|'='
op|'{'
nl|'\n'
string|'"key1"'
op|':'
string|'"value1"'
op|','
nl|'\n'
string|'"key2"'
op|':'
string|'"value2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"value3"'
op|','
nl|'\n'
string|'"key4"'
op|':'
string|'"value4"'
op|','
nl|'\n'
string|'"key5"'
op|':'
string|'"value5"'
op|'}'
newline|'\n'
name|'return'
name|'specs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsExtraSpecsTestV21
dedent|''
name|'class'
name|'FlavorsExtraSpecsTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|bad_request
indent|'    '
name|'bad_request'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
newline|'\n'
DECL|variable|flavorextraspecs
name|'flavorextraspecs'
op|'='
name|'flavorextraspecs_v21'
newline|'\n'
nl|'\n'
DECL|member|_get_request
name|'def'
name|'_get_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'use_admin_context'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req_url'
op|'='
string|"'/v2/fake/flavors/'"
op|'+'
name|'url'
newline|'\n'
name|'return'
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'req_url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'use_admin_context'
op|')'
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
name|'FlavorsExtraSpecsTestV21'
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
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'flavorextraspecs'
op|'.'
name|'FlavorExtraSpecsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'dict'
op|'('
name|'test_flavor'
op|'.'
name|'fake_flavor'
op|','
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor._flavor_get_by_flavor_id_from_db'"
nl|'\n'
op|')'
name|'as'
name|'mock_get'
op|':'
newline|'\n'
indent|'            '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'flavor'
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
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
newline|'\n'
DECL|member|test_index_no_data
name|'def'
name|'test_index_no_data'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'flavorid'
op|'='
string|"'1'"
op|','
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'flavor'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
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
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
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
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
newline|'\n'
DECL|member|test_index_flavor_not_found
name|'def'
name|'test_index_flavor_not_found'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"'1'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
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
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'flavorid'
op|'='
string|"'1'"
op|','
name|'extra_specs'
op|'='
op|'{'
string|"'key5'"
op|':'
string|"'value5'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key5'"
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
name|'as'
name|'mock_get'
op|':'
newline|'\n'
indent|'            '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'flavor'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value5'"
op|','
name|'res_dict'
op|'['
string|"'key5'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
newline|'\n'
DECL|member|test_show_spec_not_found
name|'def'
name|'test_show_spec_not_found'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'extra_specs'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key6'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_found_because_flavor
dedent|''
name|'def'
name|'test_not_found_because_flavor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key5'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
name|'as'
name|'mock_get'
op|':'
newline|'\n'
indent|'            '
name|'mock_get'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"'1'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
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
string|"'key5'"
op|','
name|'body'
op|'='
op|'{'
string|"'key5'"
op|':'
string|"'value5'"
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.get_by_flavor_id'"
op|')'
name|'as'
name|'mock_get'
op|':'
newline|'\n'
indent|'            '
name|'mock_get'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"'1'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|'='
op|'{'
string|"'extra_specs'"
op|':'
op|'{'
string|"'key5'"
op|':'
string|"'value5'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor._flavor_get_by_flavor_id_from_db'"
op|')'
newline|'\n'
DECL|member|test_delete
name|'def'
name|'test_delete'
op|'('
name|'self'
op|','
name|'mock_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'dict'
op|'('
name|'test_flavor'
op|'.'
name|'fake_flavor'
op|','
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'key5'"
op|':'
string|"'value5'"
op|'}'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key5'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mock_get'
op|'.'
name|'return_value'
op|'='
name|'flavor'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.save'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
op|','
string|"'key5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_no_admin
dedent|''
dedent|''
name|'def'
name|'test_delete_no_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.objects.flavor._flavor_extra_specs_del'"
op|','
nl|'\n'
name|'delete_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key5'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key 5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_spec_not_found
dedent|''
name|'def'
name|'test_delete_spec_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key6'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|','
string|'"key2"'
op|':'
number|'0.5'
op|','
string|'"key3"'
op|':'
number|'5'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0.5'
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'5'
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
string|"'key3'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_no_admin
dedent|''
name|'def'
name|'test_create_no_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
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
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_not_found
dedent|''
name|'def'
name|'test_create_flavor_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.save'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"''"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_db_duplicate
dedent|''
dedent|''
name|'def'
name|'test_create_flavor_db_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
nl|'\n'
string|"'nova.objects.Flavor.save'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
op|'('
nl|'\n'
name|'id'
op|'='
string|"''"
op|','
name|'retries'
op|'='
number|'10'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
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
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_bad_request
dedent|''
dedent|''
name|'def'
name|'_test_create_bad_request'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.objects.flavor._flavor_extra_specs_add'"
op|','
nl|'\n'
name|'return_create_flavor_extra_specs'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
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
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_empty_body
dedent|''
name|'def'
name|'test_create_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_non_dict_extra_specs
dedent|''
name|'def'
name|'test_create_non_dict_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
string|'"non_dict"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_non_string_key
dedent|''
name|'def'
name|'test_create_non_string_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'None'
op|':'
string|'"value1"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_non_string_value
dedent|''
name|'def'
name|'test_create_non_string_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
name|'None'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_zero_length_key
dedent|''
name|'def'
name|'test_create_zero_length_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'""'
op|':'
string|'"value1"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_long_key
dedent|''
name|'def'
name|'test_create_long_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"a"'
op|'*'
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_long_value
dedent|''
name|'def'
name|'test_create_long_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
string|'"a"'
op|'*'
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_bad_request'
op|'('
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_really_long_integer_value
dedent|''
name|'def'
name|'test_create_really_long_integer_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'10'
op|'**'
number|'1000'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'create'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
name|'value'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_invalid_specs_key
dedent|''
name|'def'
name|'test_create_invalid_specs_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'invalid_keys'
op|'='
op|'('
string|'"key1/"'
op|','
string|'"<key>"'
op|','
string|'"$$akey$"'
op|','
string|'"!akey"'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'invalid_keys'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
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
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.flavor._flavor_extra_specs_add'"
op|')'
newline|'\n'
DECL|member|test_create_valid_specs_key
name|'def'
name|'test_create_valid_specs_key'
op|'('
name|'self'
op|','
name|'mock_flavor_extra_specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'valid_keys'
op|'='
op|'('
string|'"key1"'
op|','
string|'"month.price"'
op|','
string|'"I_am-a Key"'
op|','
string|'"finance:g2"'
op|')'
newline|'\n'
name|'mock_flavor_extra_specs'
op|'.'
name|'side_effects'
op|'='
name|'return_create_flavor_extra_specs'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'valid_keys'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
op|'{'
string|'"extra_specs"'
op|':'
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
number|'1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'extra_specs'"
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.flavor._flavor_extra_specs_add'"
op|')'
newline|'\n'
DECL|member|test_update_item
name|'def'
name|'test_update_item'
op|'('
name|'self'
op|','
name|'mock_add'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_add'
op|'.'
name|'side_effect'
op|'='
name|'return_create_flavor_extra_specs'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
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
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_no_admin
dedent|''
name|'def'
name|'test_update_item_no_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Forbidden'
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
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_update_item_bad_request
dedent|''
name|'def'
name|'_test_update_item_bad_request'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'bad_request'
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
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_empty_body
dedent|''
name|'def'
name|'test_update_item_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_too_many_keys
dedent|''
name|'def'
name|'test_update_item_too_many_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|','
string|'"key2"'
op|':'
string|'"value2"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_non_dict_extra_specs
dedent|''
name|'def'
name|'test_update_item_non_dict_extra_specs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
string|'"non_dict"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_non_string_key
dedent|''
name|'def'
name|'test_update_item_non_string_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
op|'{'
name|'None'
op|':'
string|'"value1"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_non_string_value
dedent|''
name|'def'
name|'test_update_item_non_string_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
op|'{'
string|'"key1"'
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_zero_length_key
dedent|''
name|'def'
name|'test_update_item_zero_length_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
op|'{'
string|'""'
op|':'
string|'"value1"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_long_key
dedent|''
name|'def'
name|'test_update_item_long_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"a"'
op|'*'
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
op|'{'
name|'key'
op|':'
string|'"value1"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_long_value
dedent|''
name|'def'
name|'test_update_item_long_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
string|'"a"'
op|'*'
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'_test_update_item_bad_request'
op|'('
op|'{'
string|'"key1"'
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_body_uri_mismatch
dedent|''
name|'def'
name|'test_update_item_body_uri_mismatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/bad'"
op|','
name|'use_admin_context'
op|'='
name|'True'
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
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'bad'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_flavor_not_found
dedent|''
name|'def'
name|'test_update_flavor_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.Flavor.save'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorNotFound'
op|'('
name|'flavor_id'
op|'='
string|"''"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
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
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_flavor_db_duplicate
dedent|''
dedent|''
name|'def'
name|'test_update_flavor_db_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
nl|'\n'
string|"'nova.objects.Flavor.save'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
name|'retries'
op|'='
number|'5'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
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
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_really_long_integer_value
dedent|''
dedent|''
name|'def'
name|'test_update_really_long_integer_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
number|'10'
op|'**'
number|'1000'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
string|"'1/os-extra_specs/key1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
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
name|'update'
op|','
nl|'\n'
name|'req'
op|','
number|'1'
op|','
string|"'key1'"
op|','
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
name|'value'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsExtraSpecsTestV2
dedent|''
dedent|''
name|'class'
name|'FlavorsExtraSpecsTestV2'
op|'('
name|'FlavorsExtraSpecsTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|bad_request
indent|'    '
name|'bad_request'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
DECL|variable|flavorextraspecs
name|'flavorextraspecs'
op|'='
name|'flavorextraspecs_v2'
newline|'\n'
dedent|''
endmarker|''
end_unit
