begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#  Copyright 2013 Cloudbase Solutions Srl'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutils'
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
nl|'\n'
nl|'\n'
DECL|class|VHDUtilsTestCase
name|'class'
name|'VHDUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VHDUtils class."""'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_VHD_PATH
name|'_FAKE_VHD_PATH'
op|'='
string|'"C:\\\\fake_path.vhdx"'
newline|'\n'
DECL|variable|_FAKE_FORMAT
name|'_FAKE_FORMAT'
op|'='
number|'3'
newline|'\n'
DECL|variable|_FAKE_MAK_INTERNAL_SIZE
name|'_FAKE_MAK_INTERNAL_SIZE'
op|'='
number|'1000'
newline|'\n'
DECL|variable|_FAKE_JOB_PATH
name|'_FAKE_JOB_PATH'
op|'='
string|"'fake_job_path'"
newline|'\n'
DECL|variable|_FAKE_RET_VAL
name|'_FAKE_RET_VAL'
op|'='
number|'0'
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
name|'self'
op|'.'
name|'_vhdutils'
op|'='
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'_conn'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'_vmutils'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VHDUtilsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_dynamic_vhd
dedent|''
name|'def'
name|'test_create_dynamic_vhd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'Format'"
op|':'
name|'self'
op|'.'
name|'_FAKE_FORMAT'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'mock_img_svc'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ImageManagementService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_img_svc'
op|'.'
name|'CreateDynamicVirtualHardDisk'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
op|','
name|'self'
op|'.'
name|'_FAKE_RET_VAL'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'create_dynamic_vhd'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_MAK_INTERNAL_SIZE'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'DISK_FORMAT_VHD'
op|')'
newline|'\n'
nl|'\n'
name|'mock_img_svc'
op|'.'
name|'CreateDynamicVirtualHardDisk'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'Path'
op|'='
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
name|'MaxInternalSize'
op|'='
name|'self'
op|'.'
name|'_FAKE_MAK_INTERNAL_SIZE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_internal_vhd_size_by_file_size_fixed
dedent|''
name|'def'
name|'test_get_internal_vhd_size_by_file_size_fixed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhdutil'
op|'='
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|'('
op|')'
newline|'\n'
name|'root_vhd_size'
op|'='
number|'1'
op|'*'
number|'1024'
op|'**'
number|'3'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'Type'"
op|':'
name|'constants'
op|'.'
name|'VHD_TYPE_FIXED'
op|'}'
newline|'\n'
nl|'\n'
name|'real_size'
op|'='
name|'vhdutil'
op|'.'
name|'_get_internal_vhd_size_by_file_size'
op|'('
name|'None'
op|','
nl|'\n'
name|'root_vhd_size'
op|')'
newline|'\n'
name|'expected_vhd_size'
op|'='
number|'1'
op|'*'
number|'1024'
op|'**'
number|'3'
op|'-'
number|'512'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_vhd_size'
op|','
name|'real_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_internal_vhd_size_by_file_size_dynamic
dedent|''
name|'def'
name|'test_get_internal_vhd_size_by_file_size_dynamic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhdutil'
op|'='
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|'('
op|')'
newline|'\n'
name|'root_vhd_size'
op|'='
number|'20'
op|'*'
number|'1024'
op|'**'
number|'3'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'Type'"
op|':'
nl|'\n'
name|'constants'
op|'.'
name|'VHD_TYPE_DYNAMIC'
op|'}'
newline|'\n'
name|'vhdutil'
op|'.'
name|'_get_vhd_dynamic_blk_size'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'vhdutil'
op|'.'
name|'_get_vhd_dynamic_blk_size'
op|'.'
name|'return_value'
op|'='
number|'2097152'
newline|'\n'
nl|'\n'
name|'real_size'
op|'='
name|'vhdutil'
op|'.'
name|'_get_internal_vhd_size_by_file_size'
op|'('
name|'None'
op|','
nl|'\n'
name|'root_vhd_size'
op|')'
newline|'\n'
name|'expected_vhd_size'
op|'='
number|'20'
op|'*'
number|'1024'
op|'**'
number|'3'
op|'-'
number|'43008'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_vhd_size'
op|','
name|'real_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_internal_vhd_size_by_file_size_unsupported
dedent|''
name|'def'
name|'test_get_internal_vhd_size_by_file_size_unsupported'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vhdutil'
op|'='
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|'('
op|')'
newline|'\n'
name|'root_vhd_size'
op|'='
number|'20'
op|'*'
number|'1024'
op|'**'
number|'3'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'vhdutil'
op|'.'
name|'get_vhd_info'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'Type'"
op|':'
number|'5'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'vhdutil'
op|'.'
name|'_get_internal_vhd_size_by_file_size'
op|','
nl|'\n'
name|'None'
op|','
name|'root_vhd_size'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
