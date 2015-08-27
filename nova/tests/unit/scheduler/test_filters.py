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
string|'"""\nTests For Scheduler Host Filters.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'range'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'loadables'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Filter1
name|'class'
name|'Filter1'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Filter class #1."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Filter2
dedent|''
name|'class'
name|'Filter2'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Filter class #2."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FiltersTestCase
dedent|''
name|'class'
name|'FiltersTestCase'
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
name|'FiltersTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|','
string|'"__init__"'
op|')'
name|'as'
name|'mock_load'
op|':'
newline|'\n'
indent|'            '
name|'mock_load'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_all
dedent|''
dedent|''
name|'def'
name|'test_filter_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_obj_list'
op|'='
op|'['
string|"'obj1'"
op|','
string|"'obj2'"
op|','
string|"'obj3'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
newline|'\n'
name|'base_filter'
op|'='
name|'filters'
op|'.'
name|'BaseFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'base_filter'
op|','
string|"'_filter_one'"
op|')'
newline|'\n'
nl|'\n'
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj1'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj2'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj3'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'base_filter'
op|'.'
name|'filter_all'
op|'('
name|'filter_obj_list'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'obj1'"
op|','
string|"'obj3'"
op|']'
op|','
name|'list'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_all_recursive_yields
dedent|''
name|'def'
name|'test_filter_all_recursive_yields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test filter_all() allows generators from previous filter_all()s.'
nl|'\n'
comment|'# filter_all() yields results.  We want to make sure that we can'
nl|'\n'
comment|'# call filter_all() with generators returned from previous calls'
nl|'\n'
comment|'# to filter_all().'
nl|'\n'
indent|'        '
name|'filter_obj_list'
op|'='
op|'['
string|"'obj1'"
op|','
string|"'obj2'"
op|','
string|"'obj3'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
newline|'\n'
name|'base_filter'
op|'='
name|'filters'
op|'.'
name|'BaseFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'base_filter'
op|','
string|"'_filter_one'"
op|')'
newline|'\n'
nl|'\n'
name|'total_iterations'
op|'='
number|'200'
newline|'\n'
nl|'\n'
comment|'# The order that _filter_one is going to get called gets'
nl|'\n'
comment|'# confusing because we will be recursively yielding things..'
nl|'\n'
comment|'# We are going to simulate the first call to filter_all()'
nl|'\n'
comment|"# returning False for 'obj2'.  So, 'obj1' will get yielded"
nl|'\n'
comment|"# 'total_iterations' number of times before the first filter_all()"
nl|'\n'
comment|"# call gets to processing 'obj2'.  We then return 'False' for it."
nl|'\n'
comment|"# After that, 'obj3' gets yielded 'total_iterations' number of"
nl|'\n'
comment|'# times.'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'total_iterations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj1'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
dedent|''
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj2'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'total_iterations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'.'
name|'_filter_one'
op|'('
string|"'obj3'"
op|','
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'objs'
op|'='
name|'iter'
op|'('
name|'filter_obj_list'
op|')'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'total_iterations'
op|')'
op|':'
newline|'\n'
comment|'# Pass in generators returned from previous calls.'
nl|'\n'
indent|'            '
name|'objs'
op|'='
name|'base_filter'
op|'.'
name|'filter_all'
op|'('
name|'objs'
op|','
name|'filter_properties'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'inspect'
op|'.'
name|'isgenerator'
op|'('
name|'objs'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'obj1'"
op|','
string|"'obj3'"
op|']'
op|','
name|'list'
op|'('
name|'objs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_objects
dedent|''
name|'def'
name|'test_get_filtered_objects'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_objs_initial'
op|'='
op|'['
string|"'initial'"
op|','
string|"'filter1'"
op|','
string|"'objects1'"
op|']'
newline|'\n'
name|'filter_objs_second'
op|'='
op|'['
string|"'second'"
op|','
string|"'filter2'"
op|','
string|"'objects2'"
op|']'
newline|'\n'
name|'filter_objs_last'
op|'='
op|'['
string|"'last'"
op|','
string|"'filter3'"
op|','
string|"'objects3'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
newline|'\n'
nl|'\n'
DECL|function|_fake_base_loader_init
name|'def'
name|'_fake_base_loader_init'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|','
string|"'__init__'"
op|','
nl|'\n'
name|'_fake_base_loader_init'
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter1'
op|')'
newline|'\n'
name|'filt2_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter1'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'run_filter_for_index'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter2'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt2_mock'
op|','
string|"'run_filter_for_index'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt2_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'.'
name|'run_filter_for_index'
op|'('
number|'0'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'filt1_mock'
op|'.'
name|'filter_all'
op|'('
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'filter_objs_second'
op|')'
newline|'\n'
name|'filt2_mock'
op|'.'
name|'run_filter_for_index'
op|'('
number|'0'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'filt2_mock'
op|'.'
name|'filter_all'
op|'('
name|'filter_objs_second'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'filter_objs_last'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
newline|'\n'
name|'filter_mocks'
op|'='
op|'['
name|'filt1_mock'
op|','
name|'filt2_mock'
op|']'
newline|'\n'
name|'result'
op|'='
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'filter_mocks'
op|','
nl|'\n'
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filter_objs_last'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_objects_for_index
dedent|''
name|'def'
name|'test_get_filtered_objects_for_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that we don\'t call a filter when its\n        run_filter_for_index() method returns false\n        """'
newline|'\n'
name|'filter_objs_initial'
op|'='
op|'['
string|"'initial'"
op|','
string|"'filter1'"
op|','
string|"'objects1'"
op|']'
newline|'\n'
name|'filter_objs_second'
op|'='
op|'['
string|"'second'"
op|','
string|"'filter2'"
op|','
string|"'objects2'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
newline|'\n'
nl|'\n'
DECL|function|_fake_base_loader_init
name|'def'
name|'_fake_base_loader_init'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|','
string|"'__init__'"
op|','
nl|'\n'
name|'_fake_base_loader_init'
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter1'
op|')'
newline|'\n'
name|'filt2_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter1'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'run_filter_for_index'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter2'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt2_mock'
op|','
string|"'run_filter_for_index'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt2_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'.'
name|'run_filter_for_index'
op|'('
number|'0'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'filt1_mock'
op|'.'
name|'filter_all'
op|'('
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'filter_objs_second'
op|')'
newline|'\n'
comment|'# return false so filter_all will not be called'
nl|'\n'
name|'filt2_mock'
op|'.'
name|'run_filter_for_index'
op|'('
number|'0'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
newline|'\n'
name|'filter_mocks'
op|'='
op|'['
name|'filt1_mock'
op|','
name|'filt2_mock'
op|']'
newline|'\n'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'filter_mocks'
op|','
nl|'\n'
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_objects_none_response
dedent|''
name|'def'
name|'test_get_filtered_objects_none_response'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_objs_initial'
op|'='
op|'['
string|"'initial'"
op|','
string|"'filter1'"
op|','
string|"'objects1'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
newline|'\n'
nl|'\n'
DECL|function|_fake_base_loader_init
name|'def'
name|'_fake_base_loader_init'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|','
string|"'__init__'"
op|','
nl|'\n'
name|'_fake_base_loader_init'
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter1'
op|')'
newline|'\n'
name|'filt2_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'Filter2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter1'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'run_filter_for_index'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt1_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
comment|"# Shouldn't be called."
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'Filter2'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'filt2_mock'
op|','
string|"'filter_all'"
op|')'
newline|'\n'
nl|'\n'
name|'filt1_mock'
op|'.'
name|'run_filter_for_index'
op|'('
number|'0'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'filt1_mock'
op|'.'
name|'filter_all'
op|'('
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
newline|'\n'
name|'filter_mocks'
op|'='
op|'['
name|'filt1_mock'
op|','
name|'filt2_mock'
op|']'
newline|'\n'
name|'result'
op|'='
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'filter_mocks'
op|','
nl|'\n'
name|'filter_objs_initial'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_objects_info_log_none_returned
dedent|''
name|'def'
name|'test_get_filtered_objects_info_log_none_returned'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'='
name|'filters'
op|'.'
name|'LOG'
newline|'\n'
nl|'\n'
DECL|class|FilterA
name|'class'
name|'FilterA'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
DECL|member|filter_all
indent|'            '
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'list_objs'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
comment|'# return all but the first object'
nl|'\n'
indent|'                '
name|'return'
name|'list_objs'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|class|FilterB
dedent|''
dedent|''
name|'class'
name|'FilterB'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
DECL|member|filter_all
indent|'            '
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'list_objs'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
comment|'# return an empty list'
nl|'\n'
indent|'                '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'filter_a'
op|'='
name|'FilterA'
op|'('
op|')'
newline|'\n'
name|'filter_b'
op|'='
name|'FilterB'
op|'('
op|')'
newline|'\n'
name|'all_filters'
op|'='
op|'['
name|'filter_a'
op|','
name|'filter_b'
op|']'
newline|'\n'
name|'hosts'
op|'='
op|'['
string|'"Host0"'
op|','
string|'"Host1"'
op|','
string|'"Host2"'
op|']'
newline|'\n'
name|'fake_uuid'
op|'='
string|'"uuid"'
newline|'\n'
name|'filt_props'
op|'='
op|'{'
string|'"request_spec"'
op|':'
op|'{'
string|'"instance_properties"'
op|':'
op|'{'
nl|'\n'
string|'"uuid"'
op|':'
name|'fake_uuid'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'LOG'
op|','
string|'"info"'
op|')'
name|'as'
name|'mock_log'
op|':'
newline|'\n'
DECL|variable|result
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
nl|'\n'
name|'all_filters'
op|','
name|'hosts'
op|','
name|'filt_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
comment|'# FilterA should leave Host1 and Host2; FilterB should leave None.'
nl|'\n'
DECL|variable|exp_output
name|'exp_output'
op|'='
op|'('
string|'"[\'FilterA: (start: 3, end: 2)\', "'
nl|'\n'
string|'"\'FilterB: (start: 2, end: 0)\']"'
op|')'
newline|'\n'
DECL|variable|cargs
name|'cargs'
op|'='
name|'mock_log'
op|'.'
name|'call_args'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"with instance ID \'%s\'"'
op|'%'
name|'fake_uuid'
op|','
name|'cargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'exp_output'
op|','
name|'cargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_filtered_objects_debug_log_none_returned
dedent|''
dedent|''
name|'def'
name|'test_get_filtered_objects_debug_log_none_returned'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'='
name|'filters'
op|'.'
name|'LOG'
newline|'\n'
nl|'\n'
DECL|class|FilterA
name|'class'
name|'FilterA'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
DECL|member|filter_all
indent|'            '
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'list_objs'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
comment|'# return all but the first object'
nl|'\n'
indent|'                '
name|'return'
name|'list_objs'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|class|FilterB
dedent|''
dedent|''
name|'class'
name|'FilterB'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
DECL|member|filter_all
indent|'            '
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'list_objs'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
comment|'# return an empty list'
nl|'\n'
indent|'                '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'filter_a'
op|'='
name|'FilterA'
op|'('
op|')'
newline|'\n'
name|'filter_b'
op|'='
name|'FilterB'
op|'('
op|')'
newline|'\n'
name|'all_filters'
op|'='
op|'['
name|'filter_a'
op|','
name|'filter_b'
op|']'
newline|'\n'
name|'hosts'
op|'='
op|'['
string|'"Host0"'
op|','
string|'"Host1"'
op|','
string|'"Host2"'
op|']'
newline|'\n'
name|'fake_uuid'
op|'='
string|'"uuid"'
newline|'\n'
name|'filt_props'
op|'='
op|'{'
string|'"request_spec"'
op|':'
op|'{'
string|'"instance_properties"'
op|':'
op|'{'
nl|'\n'
string|'"uuid"'
op|':'
name|'fake_uuid'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'LOG'
op|','
string|'"debug"'
op|')'
name|'as'
name|'mock_log'
op|':'
newline|'\n'
DECL|variable|result
indent|'            '
name|'result'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
nl|'\n'
name|'all_filters'
op|','
name|'hosts'
op|','
name|'filt_props'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'result'
op|')'
newline|'\n'
comment|'# FilterA should leave Host1 and Host2; FilterB should leave None.'
nl|'\n'
DECL|variable|exp_output
name|'exp_output'
op|'='
op|'('
string|'"[(\'FilterA\', [(\'Host1\', \'\'), (\'Host2\', \'\')]), "'
op|'+'
nl|'\n'
string|'"(\'FilterB\', None)]"'
op|')'
newline|'\n'
DECL|variable|cargs
name|'cargs'
op|'='
name|'mock_log'
op|'.'
name|'call_args'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"with instance ID \'%s\'"'
op|'%'
name|'fake_uuid'
op|','
name|'cargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'exp_output'
op|','
name|'cargs'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
