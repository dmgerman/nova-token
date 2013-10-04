begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 VMware, Inc.'
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
name|'fixtures'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MissingObject
name|'class'
name|'MissingObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|'='
string|"'fake-path'"
op|','
name|'message'
op|'='
string|"'fake_message'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'fault'
op|'='
name|'fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fault'
op|'.'
name|'localizedMessage'
op|'='
name|'message'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_get_object_properties
dedent|''
dedent|''
name|'def'
name|'_fake_get_object_properties'
op|'('
name|'vim'
op|','
name|'collector'
op|','
name|'mobj'
op|','
nl|'\n'
name|'type'
op|','
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'ObjectContent'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
name|'return'
name|'fake_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_get_object_properties_missing
dedent|''
name|'def'
name|'_fake_get_object_properties_missing'
op|'('
name|'vim'
op|','
name|'collector'
op|','
name|'mobj'
op|','
nl|'\n'
name|'type'
op|','
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fake_objects'
op|'='
name|'fake'
op|'.'
name|'FakeRetrieveResult'
op|'('
op|')'
newline|'\n'
name|'ml'
op|'='
op|'['
name|'MissingObject'
op|'('
op|')'
op|']'
newline|'\n'
name|'fake_objects'
op|'.'
name|'add_object'
op|'('
name|'fake'
op|'.'
name|'ObjectContent'
op|'('
name|'None'
op|','
name|'missing_list'
op|'='
name|'ml'
op|')'
op|')'
newline|'\n'
name|'return'
name|'fake_objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareVIMUtilTestCase
dedent|''
name|'class'
name|'VMwareVIMUtilTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_get_dynamic_properties_missing
indent|'    '
name|'def'
name|'test_get_dynamic_properties_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.vmwareapi.vim_util.get_object_properties'"
op|','
nl|'\n'
name|'_fake_get_object_properties'
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'vim_util'
op|'.'
name|'get_dynamic_property'
op|'('
string|"'fake-vim'"
op|','
string|"'fake-obj'"
op|','
nl|'\n'
string|"'fake-type'"
op|','
string|"'fake-property'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dynamic_properties_missing_path_exists
dedent|''
name|'def'
name|'test_get_dynamic_properties_missing_path_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.vmwareapi.vim_util.get_object_properties'"
op|','
nl|'\n'
name|'_fake_get_object_properties_missing'
op|')'
op|')'
newline|'\n'
name|'res'
op|'='
name|'vim_util'
op|'.'
name|'get_dynamic_property'
op|'('
string|"'fake-vim'"
op|','
string|"'fake-obj'"
op|','
nl|'\n'
string|"'fake-type'"
op|','
string|"'fake-property'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'res'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
