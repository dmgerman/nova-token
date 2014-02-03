begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'error_util'
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
nl|'\n'
nl|'\n'
DECL|class|ExpectedMethodFault
name|'class'
name|'ExpectedMethodFault'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ErrorUtilTestCase
dedent|''
name|'class'
name|'ErrorUtilTestCase'
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
name|'ErrorUtilTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fault_checker_empty_response
dedent|''
name|'def'
name|'test_fault_checker_empty_response'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# assertRaises as a Context Manager would have been a good choice to'
nl|'\n'
comment|'# perform additional checks on the exception raised, instead of'
nl|'\n'
comment|"# try/catch block in the below tests, but it's available"
nl|'\n'
comment|'# only from  Py 2.7.'
nl|'\n'
indent|'        '
name|'exp_fault_list'
op|'='
op|'['
name|'error_util'
op|'.'
name|'FAULT_NOT_AUTHENTICATED'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'error_util'
op|'.'
name|'FaultCheckers'
op|'.'
name|'retrievepropertiesex_fault_checker'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_fault_list'
op|','
name|'e'
op|'.'
name|'fault_list'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"VimFaultException was not raised."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fault_checker_missing_props
dedent|''
dedent|''
name|'def'
name|'test_fault_checker_missing_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'fake'
op|'.'
name|'MissingProperty'
op|'('
name|'method_fault'
op|'='
name|'ExpectedMethodFault'
op|'('
op|')'
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
nl|'\n'
name|'exp_fault_list'
op|'='
op|'['
string|"'ExpectedMethodFault'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'error_util'
op|'.'
name|'FaultCheckers'
op|'.'
name|'retrievepropertiesex_fault_checker'
op|'('
nl|'\n'
name|'fake_objects'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_fault_list'
op|','
name|'e'
op|'.'
name|'fault_list'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"VimFaultException was not raised."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fault_checker_no_missing_props
dedent|''
dedent|''
name|'def'
name|'test_fault_checker_no_missing_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'.'
name|'assertIsNone'
op|'('
nl|'\n'
name|'error_util'
op|'.'
name|'FaultCheckers'
op|'.'
name|'retrievepropertiesex_fault_checker'
op|'('
nl|'\n'
name|'fake_objects'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
