begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'volume'
op|'.'
name|'contrib'
name|'import'
name|'types_manage'
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
name|'volume'
name|'import'
name|'volume_types'
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
DECL|function|stub_volume_type
name|'def'
name|'stub_volume_type'
op|'('
name|'id'
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
name|'dict'
op|'('
name|'id'
op|'='
name|'id'
op|','
name|'name'
op|'='
string|"'vol_type_%s'"
op|'%'
name|'str'
op|'('
name|'id'
op|')'
op|','
name|'extra_specs'
op|'='
name|'specs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_volume_types_get_volume_type
dedent|''
name|'def'
name|'return_volume_types_get_volume_type'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'id'
op|'=='
string|'"777"'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'VolumeTypeNotFound'
op|'('
name|'volume_type_id'
op|'='
name|'id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'stub_volume_type'
op|'('
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_volume_types_destroy
dedent|''
name|'def'
name|'return_volume_types_destroy'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'name'
op|'=='
string|'"777"'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'VolumeTypeNotFoundByName'
op|'('
name|'volume_type_name'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_volume_types_create
dedent|''
name|'def'
name|'return_volume_types_create'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_volume_types_get_by_name
dedent|''
name|'def'
name|'return_volume_types_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'name'
op|'=='
string|'"777"'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'VolumeTypeNotFoundByName'
op|'('
name|'volume_type_name'
op|'='
name|'name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'stub_volume_type'
op|'('
name|'int'
op|'('
name|'name'
op|'.'
name|'split'
op|'('
string|'"_"'
op|')'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTypesManageApiTest
dedent|''
name|'class'
name|'VolumeTypesManageApiTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'VolumeTypesManageApiTest'
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
name|'types_manage'
op|'.'
name|'VolumeTypesManageController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_types_delete
dedent|''
name|'def'
name|'test_volume_types_delete'
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
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'get_volume_type'"
op|','
nl|'\n'
name|'return_volume_types_get_volume_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'destroy'"
op|','
nl|'\n'
name|'return_volume_types_destroy'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v1/fake/types/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_types_delete_not_found
dedent|''
name|'def'
name|'test_volume_types_delete_not_found'
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
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'get_volume_type'"
op|','
nl|'\n'
name|'return_volume_types_get_volume_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'destroy'"
op|','
nl|'\n'
name|'return_volume_types_destroy'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v1/fake/types/777'"
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
name|'_delete'
op|','
nl|'\n'
name|'req'
op|','
string|"'777'"
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'create'"
op|','
nl|'\n'
name|'return_volume_types_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'get_volume_type_by_name'"
op|','
nl|'\n'
name|'return_volume_types_get_by_name'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|'"volume_type"'
op|':'
op|'{'
string|'"name"'
op|':'
string|'"vol_type_1"'
op|','
nl|'\n'
string|'"extra_specs"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
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
string|"'/v1/fake/types'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'res_dict'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'vol_type_1'"
op|','
name|'res_dict'
op|'['
string|"'volume_type'"
op|']'
op|'['
string|"'name'"
op|']'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'create'"
op|','
nl|'\n'
name|'return_volume_types_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_types'
op|','
string|"'get_volume_type_by_name'"
op|','
nl|'\n'
name|'return_volume_types_get_by_name'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v1/fake/types'"
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
name|'HTTPUnprocessableEntity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create'
op|','
name|'req'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
