begin_unit
comment|'#  Copyright 2014 IBM Corp.'
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
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOpsTestCase
name|'class'
name|'VMOpsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VMOps class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'test_case_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMOpsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'test_case_name'
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
name|'VMOpsTestCase'
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
name|'context'
op|'='
string|"'fake-context'"
newline|'\n'
nl|'\n'
comment|'# utilsfactory will check the host OS version via get_hostutils,'
nl|'\n'
comment|'# in order to return the proper Utils Class, so it must be mocked.'
nl|'\n'
name|'patched_func'
op|'='
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vmops'
op|'.'
name|'utilsfactory'
op|','
nl|'\n'
string|'"get_hostutils"'
op|')'
newline|'\n'
name|'patched_func'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'patched_func'
op|'.'
name|'stop'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'vmops'
op|'.'
name|'VMOps'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_config_drive
dedent|''
name|'def'
name|'test_attach_config_drive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidDiskFormat'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'attach_config_drive'
op|','
nl|'\n'
name|'instance'
op|','
string|"'C:/fake_instance_dir/configdrive.xxx'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
