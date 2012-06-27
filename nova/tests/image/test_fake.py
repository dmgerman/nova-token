begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
nl|'\n'
comment|'#    Author: Soren Hansen'
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
name|'datetime'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeImageServiceTestCase
name|'class'
name|'FakeImageServiceTestCase'
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
name|'FakeImageServiceTestCase'
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
name|'image_service'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
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
name|'super'
op|'('
name|'FakeImageServiceTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
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
name|'res'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'for'
name|'image'
name|'in'
name|'res'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
name|'set'
op|'('
name|'image'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'keys'
op|','
name|'set'
op|'('
op|'['
string|"'id'"
op|','
string|"'name'"
op|','
string|"'created_at'"
op|','
nl|'\n'
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|','
string|"'deleted'"
op|','
nl|'\n'
string|"'status'"
op|','
string|"'is_public'"
op|','
string|"'properties'"
op|','
nl|'\n'
string|"'disk_format'"
op|','
string|"'container_format'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'image'
op|'['
string|"'created_at'"
op|']'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'image'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
op|'('
name|'isinstance'
op|'('
name|'image'
op|'['
string|"'deleted_at'"
op|']'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
name|'or'
nl|'\n'
name|'image'
op|'['
string|"'deleted_at'"
op|']'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'\'image\\\'s "deleted_at" attribute was neither a \''
nl|'\n'
string|"'datetime object nor None'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|check_is_bool
dedent|''
name|'def'
name|'check_is_bool'
op|'('
name|'image'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'val'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'deleted'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'val'
op|','
name|'bool'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'fail'
op|'('
string|'\'image\\\'s "%s" attribute wasn\\\'t \''
nl|'\n'
string|"'a bool: %r'"
op|'%'
op|'('
name|'key'
op|','
name|'val'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'check_is_bool'
op|'('
name|'image'
op|','
string|"'deleted'"
op|')'
newline|'\n'
name|'check_is_bool'
op|'('
name|'image'
op|','
string|"'is_public'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_raises_imagenotfound_for_invalid_id
dedent|''
dedent|''
name|'def'
name|'test_show_raises_imagenotfound_for_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'this image does not exist'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_adds_id
dedent|''
name|'def'
name|'test_create_adds_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'index'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'image_count'
op|'='
name|'len'
op|'('
name|'index'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'index'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'index'
op|')'
op|','
name|'image_count'
op|'+'
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'index'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_keeps_id
dedent|''
name|'def'
name|'test_create_keeps_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'34'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_rejects_duplicate_ids
dedent|''
name|'def'
name|'test_create_rejects_duplicate_ids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Duplicate'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|"# Make sure there's still one left"
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'34'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'34'"
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|','
string|"'foo'"
op|':'
string|"'baz'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'img'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'34'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'img'
op|'['
string|"'foo'"
op|']'
op|','
string|"'baz'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'34'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'34'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_all
dedent|''
name|'def'
name|'test_delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'32'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'33'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'id'"
op|':'
string|"'34'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'delete_all'
op|'('
op|')'
newline|'\n'
name|'index'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'index'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_then_get
dedent|''
name|'def'
name|'test_create_then_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'blob'
op|'='
string|"'some data'"
newline|'\n'
name|'s1'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
name|'blob'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'32'"
op|','
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
nl|'\n'
name|'data'
op|'='
name|'s1'
op|')'
newline|'\n'
name|'s2'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'32'"
op|','
name|'data'
op|'='
name|'s2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'s2'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
name|'blob'
op|','
string|"'Did not get blob back intact'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
