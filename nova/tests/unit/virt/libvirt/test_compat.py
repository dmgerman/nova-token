begin_unit
comment|'#  Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#  not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#  a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#  Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#  License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#  under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
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
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'fakelibvirt'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'compat'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'host'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CompatTestCase
name|'class'
name|'CompatTestCase'
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
name|'CompatTestCase'
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
name|'useFixture'
op|'('
name|'fakelibvirt'
op|'.'
name|'FakeLibvirtFixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host'
op|'.'
name|'Host'
op|','
string|"'has_min_version'"
op|')'
newline|'\n'
DECL|member|test_get_domain_info
name|'def'
name|'test_get_domain_info'
op|'('
name|'self'
op|','
name|'mock_has_min_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_host'
op|'='
name|'host'
op|'.'
name|'Host'
op|'('
string|'"qemu:///system"'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'power_state'
op|'.'
name|'RUNNING'
op|','
number|'512'
op|','
number|'512'
op|','
name|'None'
op|','
name|'None'
op|']'
newline|'\n'
name|'race'
op|'='
name|'fakelibvirt'
op|'.'
name|'make_libvirtError'
op|'('
nl|'\n'
name|'fakelibvirt'
op|'.'
name|'libvirtError'
op|','
nl|'\n'
string|"'ERR'"
op|','
nl|'\n'
name|'error_code'
op|'='
name|'fakelibvirt'
op|'.'
name|'VIR_ERR_OPERATION_FAILED'
op|','
nl|'\n'
name|'error_message'
op|'='
string|"'cannot read cputime for domain'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_has_min_version'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'return_value'
op|'='
name|'expected'
newline|'\n'
name|'actual'
op|'='
name|'compat'
op|'.'
name|'get_domain_info'
op|'('
name|'fakelibvirt'
op|','
name|'test_host'
op|','
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'domain'
op|'.'
name|'info'
op|'.'
name|'call_count'
op|','
number|'1'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'side_effect'
op|'='
name|'race'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'fakelibvirt'
op|'.'
name|'libvirtError'
op|','
nl|'\n'
name|'compat'
op|'.'
name|'get_domain_info'
op|','
nl|'\n'
name|'fakelibvirt'
op|','
name|'test_host'
op|','
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'domain'
op|'.'
name|'info'
op|'.'
name|'call_count'
op|','
number|'1'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_has_min_version'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'race'
op|','
name|'expected'
op|']'
newline|'\n'
name|'actual'
op|'='
name|'compat'
op|'.'
name|'get_domain_info'
op|'('
name|'fakelibvirt'
op|','
name|'test_host'
op|','
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'domain'
op|'.'
name|'info'
op|'.'
name|'call_count'
op|','
number|'2'
op|')'
newline|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'domain'
op|'.'
name|'info'
op|'.'
name|'side_effect'
op|'='
name|'race'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'fakelibvirt'
op|'.'
name|'libvirtError'
op|','
nl|'\n'
name|'compat'
op|'.'
name|'get_domain_info'
op|','
nl|'\n'
name|'fakelibvirt'
op|','
name|'test_host'
op|','
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'domain'
op|'.'
name|'info'
op|'.'
name|'call_count'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
