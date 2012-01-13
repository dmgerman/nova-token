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
name|'vsa'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
string|"'nova.tests.vsa.volumes'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaVolumesTestCase
name|'class'
name|'VsaVolumesTestCase'
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
name|'VsaVolumesTestCase'
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
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'default_vol_type'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get_vsa_volume_type'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'vsa_id'
op|'='
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'vsa_id'
op|':'
newline|'\n'
indent|'            '
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
name|'self'
op|'.'
name|'vsa_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VsaVolumesTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_default_volume_param
dedent|''
name|'def'
name|'_default_volume_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'Test volume name'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Test volume desc name'"
op|','
nl|'\n'
string|"'volume_type'"
op|':'
name|'self'
op|'.'
name|'default_vol_type'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'from_vsa_id'"
op|':'
name|'self'
op|'.'
name|'vsa_id'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_all_volumes_by_vsa
dedent|''
name|'def'
name|'_get_all_volumes_by_vsa'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
string|'"from_vsa_id"'
op|':'
name|'str'
op|'('
name|'self'
op|'.'
name|'vsa_id'
op|')'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_create_delete
dedent|''
name|'def'
name|'test_vsa_volume_create_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Check if volume properly created and deleted. """'
newline|'\n'
name|'volume_param'
op|'='
name|'self'
op|'.'
name|'_default_volume_param'
op|'('
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'volume_param'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'display_description'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|"'creating'"
op|')'
newline|'\n'
nl|'\n'
name|'vols2'
op|'='
name|'self'
op|'.'
name|'_get_all_volumes_by_vsa'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'vols2'
op|')'
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'vols2'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'display_description'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'volume_param'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|"'creating'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vols3'
op|'='
name|'self'
op|'.'
name|'_get_all_volumes_by_vsa'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'vols2'
op|')'
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'vols3'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
string|"'deleting'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_delete_nonavail_volume
dedent|''
name|'def'
name|'test_vsa_volume_delete_nonavail_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Check volume deleton in different states. """'
newline|'\n'
name|'volume_param'
op|'='
name|'self'
op|'.'
name|'_default_volume_param'
op|'('
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'volume_param'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'in-use'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ApiError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vsa_volume_delete_vsa_with_volumes
dedent|''
name|'def'
name|'test_vsa_volume_delete_vsa_with_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Check volume deleton in different states. """'
newline|'\n'
nl|'\n'
name|'vols1'
op|'='
name|'self'
op|'.'
name|'_get_all_volumes_by_vsa'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'3'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_param'
op|'='
name|'self'
op|'.'
name|'_default_volume_param'
op|'('
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'**'
name|'volume_param'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vols2'
op|'='
name|'self'
op|'.'
name|'_get_all_volumes_by_vsa'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vols1'
op|')'
op|'+'
number|'3'
op|','
name|'len'
op|'('
name|'vols2'
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
name|'self'
op|'.'
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
name|'vols3'
op|'='
name|'self'
op|'.'
name|'_get_all_volumes_by_vsa'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'vols1'
op|')'
op|','
name|'len'
op|'('
name|'vols3'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
