begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
name|'unittest'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
name|'import'
name|'integrated_helpers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.integrated'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumesTest
name|'class'
name|'VolumesTest'
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
name|'VolumesTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'image_service'
op|'='
string|"'nova.image.fake.MockImageService'"
op|','
nl|'\n'
name|'volume_driver'
op|'='
string|"'nova.volume.driver.LoggingVolumeDriver'"
op|')'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'integrated_helpers'
op|'.'
name|'IntegratedUnitTestContext'
op|'.'
name|'startup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'context'
op|'.'
name|'test_user'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'openstack_api'
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
name|'integrated_helpers'
op|'.'
name|'IntegratedUnitTestContext'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumesTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volumes
dedent|''
name|'def'
name|'test_get_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check that listing volumes works"""'
newline|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volumes'
op|'('
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"volume: %s"'
op|'%'
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_volume
dedent|''
dedent|''
name|'def'
name|'test_create_and_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and deletes a volume"""'
newline|'\n'
nl|'\n'
comment|'# Create volume with name'
nl|'\n'
name|'created_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_volume'
op|'('
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'size'"
op|':'
number|'1'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_volume: %s"'
op|'%'
name|'created_volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_volume_id'
op|'='
name|'created_volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Check it's there"
nl|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_volume_id'
op|','
name|'found_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should also be in the all-volume list'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volumes'
op|'('
op|')'
newline|'\n'
name|'volume_names'
op|'='
op|'['
name|'volume'
op|'['
string|"'id'"
op|']'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_volume_id'
name|'in'
name|'volume_names'
op|')'
newline|'\n'
nl|'\n'
comment|"# Wait (briefly) for creation. Delay is due to the 'message queue'"
nl|'\n'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'found_volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'creating'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Found %s"'
op|'%'
name|'found_volume'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
name|'retries'
op|'='
name|'retries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'retries'
op|'>'
number|'5'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'available'"
op|','
name|'found_volume'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the volume'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
nl|'\n'
comment|"# Wait (briefly) for deletion. Delay is due to the 'message queue'"
nl|'\n'
name|'for'
name|'retries'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'found_volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_volume'
op|'('
name|'created_volume_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|':'
newline|'\n'
indent|'                '
name|'found_volume'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got 404, proceeding"'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Found_volume=%s"'
op|'%'
name|'found_volume'
op|')'
newline|'\n'
name|'if'
name|'found_volume'
op|'['
string|"'status'"
op|']'
op|'!='
string|"'deleting'"
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be gone'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_volume'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logs: %s"'
op|'%'
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'all_logs'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'create_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'create_volume'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Create_Actions: %s"'
op|'%'
name|'create_actions'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'create_actions'
op|')'
op|')'
newline|'\n'
name|'create_action'
op|'='
name|'create_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'availability_zone'"
op|']'
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'create_action'
op|'['
string|"'size'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'export_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'create_export'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'export_actions'
op|')'
op|')'
newline|'\n'
name|'export_action'
op|'='
name|'export_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'export_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'export_action'
op|'['
string|"'availability_zone'"
op|']'
op|','
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
name|'delete_actions'
op|'='
name|'driver'
op|'.'
name|'LoggingVolumeDriver'
op|'.'
name|'logs_like'
op|'('
nl|'\n'
string|"'delete_volume'"
op|','
nl|'\n'
name|'id'
op|'='
name|'created_volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'delete_actions'
op|')'
op|')'
newline|'\n'
name|'delete_action'
op|'='
name|'export_actions'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'delete_action'
op|'['
string|"'id'"
op|']'
op|','
name|'created_volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
dedent|''
endmarker|''
end_unit
