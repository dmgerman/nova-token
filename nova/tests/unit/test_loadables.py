begin_unit
comment|'# Copyright 2012 OpenStack Foundation  # All Rights Reserved.'
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
string|'"""\nTests For Loadable class handling.\n"""'
newline|'\n'
nl|'\n'
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
name|'unit'
name|'import'
name|'fake_loadables'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoadablesTestCase
name|'class'
name|'LoadablesTestCase'
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
name|'LoadablesTestCase'
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
name|'fake_loader'
op|'='
name|'fake_loadables'
op|'.'
name|'FakeLoader'
op|'('
op|')'
newline|'\n'
comment|'# The name that we imported above for testing'
nl|'\n'
name|'self'
op|'.'
name|'test_package'
op|'='
string|"'nova.tests.unit.fake_loadables'"
newline|'\n'
nl|'\n'
DECL|member|test_loader_init
dedent|''
name|'def'
name|'test_loader_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'package'
op|','
name|'self'
op|'.'
name|'test_package'
op|')'
newline|'\n'
comment|'# Test the path of the module'
nl|'\n'
name|'ending_path'
op|'='
string|"'/'"
op|'+'
name|'self'
op|'.'
name|'test_package'
op|'.'
name|'replace'
op|'('
string|"'.'"
op|','
string|"'/'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'path'
op|'.'
name|'endswith'
op|'('
name|'ending_path'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'loadable_cls_type'
op|','
nl|'\n'
name|'fake_loadables'
op|'.'
name|'FakeLoadable'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_compare_classes
dedent|''
name|'def'
name|'_compare_classes'
op|'('
name|'self'
op|','
name|'classes'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'class_names'
op|'='
op|'['
name|'cls'
op|'.'
name|'__name__'
name|'for'
name|'cls'
name|'in'
name|'classes'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'class_names'
op|')'
op|','
name|'set'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_classes
dedent|''
name|'def'
name|'test_get_all_classes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'classes'
op|'='
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_all_classes'
op|'('
op|')'
newline|'\n'
name|'expected_class_names'
op|'='
op|'['
string|"'FakeLoadableSubClass1'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass2'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass5'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass6'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_compare_classes'
op|'('
name|'classes'
op|','
name|'expected_class_names'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes
dedent|''
name|'def'
name|'test_get_matching_classes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.FakeLoadableSubClass1'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.FakeLoadableSubClass5'"
op|']'
newline|'\n'
name|'classes'
op|'='
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|'('
name|'test_classes'
op|')'
newline|'\n'
name|'expected_class_names'
op|'='
op|'['
string|"'FakeLoadableSubClass1'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass5'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_compare_classes'
op|'('
name|'classes'
op|','
name|'expected_class_names'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_underscore
dedent|''
name|'def'
name|'test_get_matching_classes_with_underscore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.FakeLoadableSubClass1'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2._FakeLoadableSubClass7'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ClassNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|','
nl|'\n'
name|'test_classes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_wrong_type1
dedent|''
name|'def'
name|'test_get_matching_classes_with_wrong_type1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.FakeLoadableSubClass4'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.FakeLoadableSubClass5'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ClassNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|','
nl|'\n'
name|'test_classes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_wrong_type2
dedent|''
name|'def'
name|'test_get_matching_classes_with_wrong_type2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.FakeLoadableSubClass1'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.FakeLoadableSubClass8'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ClassNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|','
nl|'\n'
name|'test_classes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_one_function
dedent|''
name|'def'
name|'test_get_matching_classes_with_one_function'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.return_valid_classes'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.FakeLoadableSubClass5'"
op|']'
newline|'\n'
name|'classes'
op|'='
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|'('
name|'test_classes'
op|')'
newline|'\n'
name|'expected_class_names'
op|'='
op|'['
string|"'FakeLoadableSubClass1'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass2'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass5'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_compare_classes'
op|'('
name|'classes'
op|','
name|'expected_class_names'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_two_functions
dedent|''
name|'def'
name|'test_get_matching_classes_with_two_functions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.return_valid_classes'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.return_valid_class'"
op|']'
newline|'\n'
name|'classes'
op|'='
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|'('
name|'test_classes'
op|')'
newline|'\n'
name|'expected_class_names'
op|'='
op|'['
string|"'FakeLoadableSubClass1'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass2'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass6'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_compare_classes'
op|'('
name|'classes'
op|','
name|'expected_class_names'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_matching_classes_with_function_including_invalids
dedent|''
name|'def'
name|'test_get_matching_classes_with_function_including_invalids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# When using a method, no checking is done on valid classes.'
nl|'\n'
indent|'        '
name|'prefix'
op|'='
name|'self'
op|'.'
name|'test_package'
newline|'\n'
name|'test_classes'
op|'='
op|'['
name|'prefix'
op|'+'
string|"'.fake_loadable1.return_invalid_classes'"
op|','
nl|'\n'
name|'prefix'
op|'+'
string|"'.fake_loadable2.return_valid_class'"
op|']'
newline|'\n'
name|'classes'
op|'='
name|'self'
op|'.'
name|'fake_loader'
op|'.'
name|'get_matching_classes'
op|'('
name|'test_classes'
op|')'
newline|'\n'
name|'expected_class_names'
op|'='
op|'['
string|"'FakeLoadableSubClass1'"
op|','
nl|'\n'
string|"'_FakeLoadableSubClass3'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass4'"
op|','
nl|'\n'
string|"'FakeLoadableSubClass6'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_compare_classes'
op|'('
name|'classes'
op|','
name|'expected_class_names'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
