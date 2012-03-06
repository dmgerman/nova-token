begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'base64'
newline|'\n'
nl|'\n'
name|'from'
name|'xml'
op|'.'
name|'etree'
name|'import'
name|'ElementTree'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'vsa'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'volume_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'vsa'
name|'import'
name|'utils'
name|'as'
name|'vsa_utils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaTestCase
name|'class'
name|'VsaTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'VsaTestCase'
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
name|'vsa_api'
op|'='
name|'vsa'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'quota_volumes'
op|'='
number|'100'
op|','
name|'quota_gigabytes'
op|'='
number|'10000'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'SATA_500_7200'"
op|','
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'type'"
op|':'
string|"'vsa_drive'"
op|','
nl|'\n'
string|"'drive_name'"
op|':'
string|"'SATA_500_7200'"
op|','
nl|'\n'
string|"'drive_type'"
op|':'
string|"'SATA'"
op|','
nl|'\n'
string|"'drive_size'"
op|':'
string|"'500'"
op|','
nl|'\n'
string|"'drive_rpm'"
op|':'
string|"'7200'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_show_by_name
name|'def'
name|'fake_show_by_name'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
string|"'wrong_image_name'"
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Test: Emulate wrong VSA name. Raise"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
number|'1'
op|','
string|"'ramdisk_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
nl|'\n'
string|"'show_by_name'"
op|','
nl|'\n'
name|'fake_show_by_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_delete_defaults
dedent|''
name|'def'
name|'test_vsa_create_delete_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'display_name'"
op|':'
string|"'VSA name test'"
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'display_name'"
op|']'
op|','
name|'param'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_delete_check_in_db
dedent|''
name|'def'
name|'test_vsa_create_delete_check_in_db'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vsa_list1'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'vsa_list2'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vsa_list2'
op|')'
op|','
name|'len'
op|'('
name|'vsa_list1'
op|')'
op|'+'
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'vsa_list3'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vsa_list3'
op|')'
op|','
name|'len'
op|'('
name|'vsa_list2'
op|')'
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_delete_high_vc_count
dedent|''
name|'def'
name|'test_vsa_create_delete_high_vc_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'vc_count'"
op|':'
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|'+'
number|'1'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'vc_count'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_wrong_image_name
dedent|''
name|'def'
name|'test_vsa_create_wrong_image_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'param'
op|'='
op|'{'
string|"'image_name'"
op|':'
string|"'wrong_image_name'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_db_error
dedent|''
name|'def'
name|'test_vsa_create_db_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_vsa_create
indent|'        '
name|'def'
name|'fake_vsa_create'
op|'('
name|'context'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Test: Emulate DB error. Raise"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'vsa_create'"
op|','
name|'fake_vsa_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_wrong_storage_params
dedent|''
name|'def'
name|'test_vsa_create_wrong_storage_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vsa_list1'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'param'
op|'='
op|'{'
string|"'storage'"
op|':'
op|'['
op|'{'
string|"'stub'"
op|':'
number|'1'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'vsa_list2'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vsa_list2'
op|')'
op|','
name|'len'
op|'('
name|'vsa_list1'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'param'
op|'='
op|'{'
string|"'storage'"
op|':'
op|'['
op|'{'
string|"'drive_name'"
op|':'
string|"'wrong name'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_with_storage
dedent|''
name|'def'
name|'test_vsa_create_with_storage'
op|'('
name|'self'
op|','
name|'multi_vol_creation'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test creation of VSA with BE storage"""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'vsa_multi_vol_creation'
op|'='
name|'multi_vol_creation'
op|')'
newline|'\n'
nl|'\n'
name|'param'
op|'='
op|'{'
string|"'storage'"
op|':'
op|'['
op|'{'
string|"'drive_name'"
op|':'
string|"'SATA_500_7200'"
op|','
nl|'\n'
string|"'num_drives'"
op|':'
number|'3'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'vol_count'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'param'
op|'='
op|'{'
string|"'storage'"
op|':'
op|'['
op|'{'
string|"'drive_name'"
op|':'
string|"'SATA_500_7200'"
op|','
nl|'\n'
string|"'num_drives'"
op|':'
number|'3'
op|'}'
op|']'
op|','
nl|'\n'
string|"'shared'"
op|':'
name|'True'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'vol_count'"
op|']'
op|','
number|'15'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_create_with_storage_single_volumes
dedent|''
name|'def'
name|'test_vsa_create_with_storage_single_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_vsa_create_with_storage'
op|'('
name|'multi_vol_creation'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_update
dedent|''
name|'def'
name|'test_vsa_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'param'
op|'='
op|'{'
string|"'vc_count'"
op|':'
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|'+'
number|'1'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'vc_count'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|')'
newline|'\n'
nl|'\n'
name|'param'
op|'='
op|'{'
string|"'vc_count'"
op|':'
number|'2'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vsa_ref'
op|'['
string|"'vc_count'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_generate_user_data
dedent|''
name|'def'
name|'test_vsa_generate_user_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'vsa_multi_vol_creation'
op|'='
name|'False'
op|')'
newline|'\n'
name|'param'
op|'='
op|'{'
string|"'display_name'"
op|':'
string|"'VSA name test'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'VSA desc test'"
op|','
nl|'\n'
string|"'vc_count'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'storage'"
op|':'
op|'['
op|'{'
string|"'drive_name'"
op|':'
string|"'SATA_500_7200'"
op|','
nl|'\n'
string|"'num_drives'"
op|':'
number|'3'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'param'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_all_vsa_drives'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'user_data'
op|'='
name|'vsa_utils'
op|'.'
name|'generate_user_data'
op|'('
name|'vsa_ref'
op|','
name|'volumes'
op|')'
newline|'\n'
name|'user_data'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'user_data'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Test: user_data = %s"'
op|')'
op|','
name|'user_data'
op|')'
newline|'\n'
nl|'\n'
name|'elem'
op|'='
name|'ElementTree'
op|'.'
name|'fromstring'
op|'('
name|'user_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'elem'
op|'.'
name|'findtext'
op|'('
string|"'name'"
op|')'
op|','
nl|'\n'
name|'param'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'elem'
op|'.'
name|'findtext'
op|'('
string|"'description'"
op|')'
op|','
nl|'\n'
name|'param'
op|'['
string|"'display_description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'elem'
op|'.'
name|'findtext'
op|'('
string|"'vc_count'"
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'param'
op|'['
string|"'vc_count'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
