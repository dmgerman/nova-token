begin_unit
comment|'#  Copyright 2014 Cloudbase Solutions Srl'
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
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeutils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'volume_attach_retry_count'"
op|','
string|"'nova.virt.hyperv.volumeops'"
op|','
nl|'\n'
string|"'hyperv'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeUtilsTestCase
name|'class'
name|'VolumeUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VolumeUtils class."""'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_PORTAL_ADDR
name|'_FAKE_PORTAL_ADDR'
op|'='
string|"'10.1.1.1'"
newline|'\n'
DECL|variable|_FAKE_PORTAL_PORT
name|'_FAKE_PORTAL_PORT'
op|'='
string|"'3260'"
newline|'\n'
DECL|variable|_FAKE_LUN
name|'_FAKE_LUN'
op|'='
number|'0'
newline|'\n'
DECL|variable|_FAKE_TARGET
name|'_FAKE_TARGET'
op|'='
string|"'iqn.2010-10.org.openstack:fake_target'"
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'VolumeUtilsTestCase'
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
name|'_volutils'
op|'='
name|'volumeutils'
op|'.'
name|'VolumeUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'_conn_wmi'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'volume_attach_retry_count'
op|'='
number|'4'
op|','
name|'group'
op|'='
string|"'hyperv'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'volume_attach_retry_interval'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'hyperv'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_login_target_portal
dedent|''
name|'def'
name|'_test_login_target_portal'
op|'('
name|'self'
op|','
name|'portal_connected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_portal'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_FAKE_PORTAL_ADDR'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_PORTAL_PORT'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'if'
name|'portal_connected'
op|':'
newline|'\n'
indent|'            '
name|'exec_output'
op|'='
string|"'Address and Socket: %s %s'"
op|'%'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_PORTAL_ADDR'
op|','
name|'self'
op|'.'
name|'_FAKE_PORTAL_PORT'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'exec_output'
op|'='
string|"''"
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'return_value'
op|'='
name|'exec_output'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'_login_target_portal'
op|'('
name|'fake_portal'
op|')'
newline|'\n'
nl|'\n'
name|'call_list'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'call_args_list'
newline|'\n'
name|'all_call_args'
op|'='
op|'['
name|'arg'
name|'for'
name|'call'
name|'in'
name|'call_list'
name|'for'
name|'arg'
name|'in'
name|'call'
op|'['
number|'0'
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'portal_connected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'RefreshTargetPortal'"
op|','
name|'all_call_args'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'AddTargetPortal'"
op|','
name|'all_call_args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_login_connected_portal
dedent|''
dedent|''
name|'def'
name|'test_login_connected_portal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_login_target_portal'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_login_new_portal
dedent|''
name|'def'
name|'test_login_new_portal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_login_target_portal'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_login_target
dedent|''
name|'def'
name|'_test_login_target'
op|'('
name|'self'
op|','
name|'target_connected'
op|','
name|'raise_exception'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_portal'
op|'='
string|"'%s:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_FAKE_PORTAL_ADDR'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_PORTAL_PORT'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'_login_target_portal'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'target_connected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_TARGET'
newline|'\n'
dedent|''
name|'elif'
name|'raise_exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'return_value'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'side_effect'
op|'='
op|'('
nl|'\n'
op|'['
string|"''"
op|','
string|"''"
op|','
string|"''"
op|','
name|'self'
op|'.'
name|'_FAKE_TARGET'
op|','
string|"''"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'raise_exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'login_storage_target'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_LUN'
op|','
name|'self'
op|'.'
name|'_FAKE_TARGET'
op|','
name|'fake_portal'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'login_storage_target'
op|'('
name|'self'
op|'.'
name|'_FAKE_LUN'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_TARGET'
op|','
nl|'\n'
name|'fake_portal'
op|')'
newline|'\n'
nl|'\n'
name|'call_list'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'.'
name|'call_args_list'
newline|'\n'
name|'all_call_args'
op|'='
op|'['
name|'arg'
name|'for'
name|'call'
name|'in'
name|'call_list'
name|'for'
name|'arg'
name|'in'
name|'call'
op|'['
number|'0'
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'target_connected'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'qlogintarget'"
op|','
name|'all_call_args'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'qlogintarget'"
op|','
name|'all_call_args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_login_connected_target
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_login_connected_target'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_login_target'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_login_disconncted_target
dedent|''
name|'def'
name|'test_login_disconncted_target'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_login_target'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_login_target_exception
dedent|''
name|'def'
name|'test_login_target_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_login_target'
op|'('
name|'False'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_execute_wrapper
dedent|''
name|'def'
name|'_test_execute_wrapper'
op|'('
name|'self'
op|','
name|'raise_exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_cmd'
op|'='
op|'('
string|"'iscsicli.exe'"
op|','
string|"'ListTargetPortals'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'raise_exception'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"'fake error'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"'The operation completed successfully'"
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
name|'as'
name|'fake_execute'
op|':'
newline|'\n'
indent|'            '
name|'fake_execute'
op|'.'
name|'return_value'
op|'='
op|'('
name|'output'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'raise_exception'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|','
nl|'\n'
op|'*'
name|'fake_cmd'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'ret_val'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'fake_cmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
name|'ret_val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_execute_raise_exception
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_execute_raise_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_execute_wrapper'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_execute_exception
dedent|''
name|'def'
name|'test_execute_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_execute_wrapper'
op|'('
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
