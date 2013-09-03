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
name|'vhdutilsv2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VHDUtilsV2TestCase
name|'class'
name|'VHDUtilsV2TestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V VHDUtilsV2 class."""'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_VHD_PATH
name|'_FAKE_VHD_PATH'
op|'='
string|'"C:\\\\fake_path.vhdx"'
newline|'\n'
DECL|variable|_FAKE_PARENT_VHD_PATH
name|'_FAKE_PARENT_VHD_PATH'
op|'='
string|'"C:\\\\fake_parent_path.vhdx"'
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
DECL|variable|_FAKE_TYPE
name|'_FAKE_TYPE'
op|'='
number|'3'
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
name|'vhdutilsv2'
op|'.'
name|'VHDUtilsV2'
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
nl|'\n'
name|'self'
op|'.'
name|'_fake_vhd_info_xml'
op|'='
op|'('
nl|'\n'
string|'\'<INSTANCE CLASSNAME="Msvm_VirtualHardDiskSettingData">\''
nl|'\n'
string|'\'<PROPERTY NAME="BlockSize" TYPE="uint32">\''
nl|'\n'
string|"'<VALUE>33554432</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="Caption" TYPE="string">\''
nl|'\n'
string|"'<VALUE>Virtual Hard Disk Setting Data</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="Description" TYPE="string">\''
nl|'\n'
string|"'<VALUE>Setting Data for a Virtual Hard Disk.</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="ElementName" TYPE="string">\''
nl|'\n'
string|"'<VALUE>fake_path.vhdx</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="Format" TYPE="uint16">\''
nl|'\n'
string|"'<VALUE>%(format)s</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="InstanceID" TYPE="string">\''
nl|'\n'
string|"'<VALUE>52794B89-AC06-4349-AC57-486CAAD52F69</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="LogicalSectorSize" TYPE="uint32">\''
nl|'\n'
string|"'<VALUE>512</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="MaxInternalSize" TYPE="uint64">\''
nl|'\n'
string|"'<VALUE>%(max_internal_size)s</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="ParentPath" TYPE="string">\''
nl|'\n'
string|"'<VALUE>%(parent_path)s</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="Path" TYPE="string">\''
nl|'\n'
string|"'<VALUE>%(path)s</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="PhysicalSectorSize" TYPE="uint32">\''
nl|'\n'
string|"'<VALUE>4096</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|'\'<PROPERTY NAME="Type" TYPE="uint16">\''
nl|'\n'
string|"'<VALUE>%(type)s</VALUE>'"
nl|'\n'
string|"'</PROPERTY>'"
nl|'\n'
string|"'</INSTANCE>'"
op|'%'
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
string|"'parent_path'"
op|':'
name|'self'
op|'.'
name|'_FAKE_PARENT_VHD_PATH'
op|','
nl|'\n'
string|"'format'"
op|':'
name|'self'
op|'.'
name|'_FAKE_FORMAT'
op|','
nl|'\n'
string|"'max_internal_size'"
op|':'
name|'self'
op|'.'
name|'_FAKE_MAK_INTERNAL_SIZE'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'self'
op|'.'
name|'_FAKE_TYPE'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'VHDUtilsV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vhd_info
dedent|''
name|'def'
name|'test_get_vhd_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'GetVirtualHardDiskSettingData'
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
op|','
name|'self'
op|'.'
name|'_fake_vhd_info_xml'
op|')'
newline|'\n'
nl|'\n'
name|'vhd_info'
op|'='
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'get_vhd_info'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
name|'vhd_info'
op|'['
string|"'Path'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'_FAKE_PARENT_VHD_PATH'
op|','
name|'vhd_info'
op|'['
string|"'ParentPath'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'_FAKE_FORMAT'
op|','
name|'vhd_info'
op|'['
string|"'Format'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'_FAKE_MAK_INTERNAL_SIZE'
op|','
nl|'\n'
name|'vhd_info'
op|'['
string|"'MaxInternalSize'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'_FAKE_TYPE'
op|','
name|'vhd_info'
op|'['
string|"'Type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_differencing_vhd
dedent|''
name|'def'
name|'test_create_differencing_vhd'
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
string|"'ParentPath'"
op|':'
name|'self'
op|'.'
name|'_FAKE_PARENT_VHD_PATH'
op|','
nl|'\n'
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
name|'CreateVirtualHardDisk'
op|'.'
name|'return_value'
op|'='
op|'('
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
op|','
nl|'\n'
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
name|'create_differencing_vhd'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_PARENT_VHD_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'mock_img_svc'
op|'.'
name|'CreateVirtualHardDisk'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reconnect_parent_vhd
dedent|''
name|'def'
name|'test_reconnect_parent_vhd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
nl|'\n'
name|'self'
op|'.'
name|'_vhdutils'
op|'.'
name|'_get_vhd_info_xml'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_fake_vhd_info_xml'
op|')'
newline|'\n'
nl|'\n'
name|'mock_img_svc'
op|'.'
name|'SetVirtualHardDiskSettingData'
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
name|'reconnect_parent_vhd'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_PARENT_VHD_PATH'
op|')'
newline|'\n'
nl|'\n'
name|'mock_img_svc'
op|'.'
name|'SetVirtualHardDiskSettingData'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'VirtualDiskSettingData'
op|'='
name|'self'
op|'.'
name|'_fake_vhd_info_xml'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resize_vhd
dedent|''
name|'def'
name|'test_resize_vhd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'ResizeVirtualHardDisk'
op|'.'
name|'return_value'
op|'='
op|'('
name|'self'
op|'.'
name|'_FAKE_JOB_PATH'
op|','
nl|'\n'
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
name|'resize_vhd'
op|'('
name|'self'
op|'.'
name|'_FAKE_VHD_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_MAK_INTERNAL_SIZE'
op|')'
newline|'\n'
nl|'\n'
name|'mock_img_svc'
op|'.'
name|'ResizeVirtualHardDisk'
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
dedent|''
dedent|''
endmarker|''
end_unit
