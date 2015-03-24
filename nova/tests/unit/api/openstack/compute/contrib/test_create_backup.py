begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'admin_actions'
name|'as'
name|'create_backup_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'create_backup'
name|'as'
name|'create_backup_v21'
newline|'\n'
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
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'admin_only_action_common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
name|'class'
name|'CreateBackupTestsV21'
op|'('
name|'admin_only_action_common'
op|'.'
name|'CommonMixin'
op|','
nl|'\n'
DECL|class|CreateBackupTestsV21
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|create_backup
indent|'    '
name|'create_backup'
op|'='
name|'create_backup_v21'
newline|'\n'
DECL|variable|controller_name
name|'controller_name'
op|'='
string|"'CreateBackupController'"
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'CreateBackupTestsV21'
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
name|'controller'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'create_backup'
op|','
name|'self'
op|'.'
name|'controller_name'
op|')'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
newline|'\n'
nl|'\n'
DECL|function|_fake_controller
name|'def'
name|'_fake_controller'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'controller'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'create_backup'
op|','
name|'self'
op|'.'
name|'controller_name'
op|','
nl|'\n'
name|'_fake_controller'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'get'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'common'
op|','
nl|'\n'
string|"'check_img_metadata_properties_quota'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
string|"'backup'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_metadata
dedent|''
name|'def'
name|'test_create_backup_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'123'"
op|':'
string|"'asdf'"
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'metadata'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'fake-image-id'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
string|"'Backup 1'"
op|','
nl|'\n'
name|'properties'
op|'='
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'backup'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'Backup 1'"
op|','
nl|'\n'
string|"'daily'"
op|','
number|'1'
op|','
nl|'\n'
name|'extra_properties'
op|'='
name|'metadata'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'fake-image-id'"
op|','
name|'res'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_name
dedent|''
name|'def'
name|'test_create_backup_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Name is required for backups.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_rotation
dedent|''
name|'def'
name|'test_create_backup_no_rotation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Rotation is required for backup requests.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_negative_rotation
dedent|''
name|'def'
name|'test_create_backup_negative_rotation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rotation must be greater than or equal to zero\n        for backup requests\n        """'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_negative_rotation_with_string_number
dedent|''
name|'def'
name|'test_create_backup_negative_rotation_with_string_number'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
string|"'-1'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_no_backup_type
dedent|''
name|'def'
name|'test_create_backup_no_backup_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Backup Type (daily or weekly) is required for backup requests.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_non_dict_metadata
dedent|''
name|'def'
name|'test_create_backup_non_dict_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
string|"'non_dict'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_bad_entity
dedent|''
name|'def'
name|'test_create_backup_bad_entity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'createBackup'"
op|':'
string|"'go'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_rotation_is_zero
dedent|''
name|'def'
name|'test_create_backup_rotation_is_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The happy path for creating backups if rotation is zero.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'0'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'fake-image-id'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
string|"'Backup 1'"
op|','
nl|'\n'
name|'properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'backup'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'Backup 1'"
op|','
nl|'\n'
string|"'daily'"
op|','
number|'0'
op|','
nl|'\n'
name|'extra_properties'
op|'='
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'Location'"
op|','
name|'res'
op|'.'
name|'headers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_rotation_is_positive
dedent|''
name|'def'
name|'test_create_backup_rotation_is_positive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# The happy path for creating backups if rotation is positive.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'fake-image-id'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
string|"'Backup 1'"
op|','
nl|'\n'
name|'properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'backup'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'Backup 1'"
op|','
nl|'\n'
string|"'daily'"
op|','
number|'1'
op|','
nl|'\n'
name|'extra_properties'
op|'='
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'fake-image-id'"
op|','
name|'res'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_rotation_is_string_number
dedent|''
name|'def'
name|'test_create_backup_rotation_is_string_number'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
string|"'1'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'fake-image-id'"
op|','
name|'status'
op|'='
string|"'ACTIVE'"
op|','
name|'name'
op|'='
string|"'Backup 1'"
op|','
nl|'\n'
name|'properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'backup'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'Backup 1'"
op|','
nl|'\n'
string|"'daily'"
op|','
number|'1'
op|','
nl|'\n'
name|'extra_properties'
op|'='
op|'{'
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'fake-image-id'"
op|','
name|'res'
op|'.'
name|'headers'
op|'['
string|"'Location'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_raises_conflict_on_invalid_state
dedent|''
name|'def'
name|'test_create_backup_raises_conflict_on_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_map'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'args_map'
op|'='
op|'{'
nl|'\n'
string|"'_create_backup'"
op|':'
op|'('
nl|'\n'
op|'('
string|"'Backup 1'"
op|','
string|"'daily'"
op|','
number|'1'
op|')'
op|','
op|'{'
string|"'extra_properties'"
op|':'
op|'{'
op|'}'
op|'}'
nl|'\n'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_invalid_state'
op|'('
string|"'_create_backup'"
op|','
name|'method'
op|'='
string|"'backup'"
op|','
nl|'\n'
name|'body_map'
op|'='
name|'body_map'
op|','
nl|'\n'
name|'compute_api_args_map'
op|'='
name|'args_map'
op|','
nl|'\n'
name|'exception_arg'
op|'='
string|"'createBackup'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_non_existed_instance
dedent|''
name|'def'
name|'test_create_backup_with_non_existed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body_map'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_non_existing_instance'
op|'('
string|"'_create_backup'"
op|','
nl|'\n'
name|'body_map'
op|'='
name|'body_map'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_invalid_create_backup
dedent|''
name|'def'
name|'test_create_backup_with_invalid_create_backup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackupup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_backup_volume_backed_instance
dedent|''
name|'def'
name|'test_backup_volume_backed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'BackupMe'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'3'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_stub_instance_get'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'image_ref'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'backup'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'BackupMe'"
op|','
string|"'daily'"
op|','
number|'3'
op|','
nl|'\n'
name|'extra_properties'
op|'='
op|'{'
op|'}'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'InvalidRequest'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateBackupTestsV2
dedent|''
dedent|''
name|'class'
name|'CreateBackupTestsV2'
op|'('
name|'CreateBackupTestsV21'
op|')'
op|':'
newline|'\n'
DECL|variable|create_backup
indent|'    '
name|'create_backup'
op|'='
name|'create_backup_v2'
newline|'\n'
DECL|variable|controller_name
name|'controller_name'
op|'='
string|"'AdminActionsController'"
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_with_invalid_create_backup
name|'def'
name|'test_create_backup_with_invalid_create_backup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(gmann):V2 API does not raise bad request for below type of'
nl|'\n'
comment|'# invalid body in controller method.'
nl|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackupup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_non_dict_metadata
dedent|''
name|'def'
name|'test_create_backup_non_dict_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateBackupPolicyEnforcementv21
dedent|''
dedent|''
name|'class'
name|'CreateBackupPolicyEnforcementv21'
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
name|'CreateBackupPolicyEnforcementv21'
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
name|'controller'
op|'='
name|'create_backup_v21'
op|'.'
name|'CreateBackupController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_policy_failed
dedent|''
name|'def'
name|'test_create_backup_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-create-backup"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|"'123'"
op|':'
string|"'asdf'"
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'createBackup'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'Backup 1'"
op|','
nl|'\n'
string|"'backup_type'"
op|':'
string|"'daily'"
op|','
nl|'\n'
string|"'rotation'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'metadata'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create_backup'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
