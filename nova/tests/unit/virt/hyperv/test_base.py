begin_unit
comment|'# Copyright 2014 Cloudbase Solutions Srl'
nl|'\n'
comment|'#'
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
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HyperVBaseTestCase
name|'class'
name|'HyperVBaseTestCase'
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
name|'HyperVBaseTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'wmi_patcher'
op|'='
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'__builtin__.wmi'"
op|','
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
name|'platform_patcher'
op|'='
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'sys.platform'"
op|','
string|"'win32'"
op|')'
newline|'\n'
name|'hostutils_patcher'
op|'='
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utilsfactory'
op|','
string|"'utils'"
op|')'
newline|'\n'
nl|'\n'
name|'platform_patcher'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'wmi_patcher'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'patched_hostutils'
op|'='
name|'hostutils_patcher'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'patched_hostutils'
op|'.'
name|'check_min_windows_version'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'wmi_patcher'
op|'.'
name|'stop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'platform_patcher'
op|'.'
name|'stop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'hostutils_patcher'
op|'.'
name|'stop'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
