begin_unit
comment|'# Copyright 2014 Red Hat Inc.'
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
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|EC2InstanceMapping
name|'class'
name|'EC2InstanceMapping'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'imap'
op|','
name|'db_imap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'imap'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'imap'
op|','
name|'field'
op|','
name|'db_imap'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'imap'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'imap'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'imap'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'db_imap'
op|'='
name|'db'
op|'.'
name|'ec2_instance_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_imap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_imap'
op|'='
name|'db'
op|'.'
name|'ec2_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'if'
name|'db_imap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_imap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_imap'
op|'='
name|'db'
op|'.'
name|'ec2_instance_get_by_id'
op|'('
name|'context'
op|','
name|'ec2_id'
op|')'
newline|'\n'
name|'if'
name|'db_imap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_imap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|EC2VolumeMapping
name|'class'
name|'EC2VolumeMapping'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'vmap'
op|','
name|'db_vmap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'vmap'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'vmap'
op|','
name|'field'
op|','
name|'db_vmap'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'vmap'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'vmap'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'vmap'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'db_vmap'
op|'='
name|'db'
op|'.'
name|'ec2_volume_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_vmap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'volume_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_vmap'
op|'='
name|'db'
op|'.'
name|'ec2_volume_get_by_uuid'
op|'('
name|'context'
op|','
name|'volume_uuid'
op|')'
newline|'\n'
name|'if'
name|'db_vmap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_vmap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_vmap'
op|'='
name|'db'
op|'.'
name|'ec2_volume_get_by_id'
op|'('
name|'context'
op|','
name|'ec2_id'
op|')'
newline|'\n'
name|'if'
name|'db_vmap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_vmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|EC2SnapshotMapping
name|'class'
name|'EC2SnapshotMapping'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'smap'
op|','
name|'db_smap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'smap'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'smap'
op|','
name|'field'
op|','
name|'db_smap'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'smap'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'smap'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'smap'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'db_smap'
op|'='
name|'db'
op|'.'
name|'ec2_snapshot_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_smap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'snapshot_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_smap'
op|'='
name|'db'
op|'.'
name|'ec2_snapshot_get_by_uuid'
op|'('
name|'context'
op|','
name|'snapshot_uuid'
op|')'
newline|'\n'
name|'if'
name|'db_smap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_smap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_smap'
op|'='
name|'db'
op|'.'
name|'ec2_snapshot_get_by_ec2_id'
op|'('
name|'context'
op|','
name|'ec2_id'
op|')'
newline|'\n'
name|'if'
name|'db_smap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_smap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|S3ImageMapping
name|'class'
name|'S3ImageMapping'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'s3imap'
op|','
name|'db_s3imap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'s3imap'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'s3imap'
op|','
name|'field'
op|','
name|'db_s3imap'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'s3imap'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'s3imap'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'s3imap'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'db_s3imap'
op|'='
name|'db'
op|'.'
name|'s3_image_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_s3imap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuid
name|'def'
name|'get_by_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'s3_image_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_s3imap'
op|'='
name|'db'
op|'.'
name|'s3_image_get_by_uuid'
op|'('
name|'context'
op|','
name|'s3_image_uuid'
op|')'
newline|'\n'
name|'if'
name|'db_s3imap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_s3imap'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'s3_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_s3imap'
op|'='
name|'db'
op|'.'
name|'s3_image_get'
op|'('
name|'context'
op|','
name|'s3_id'
op|')'
newline|'\n'
name|'if'
name|'db_s3imap'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'db_s3imap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|EC2Ids
name|'class'
name|'EC2Ids'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'instance_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'ami_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_dict
name|'def'
name|'_from_dict'
op|'('
name|'ec2ids'
op|','
name|'dict_ec2ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'ec2ids'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'ec2ids'
op|','
name|'field'
op|','
name|'dict_ec2ids'
op|'['
name|'field'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ec2ids'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_ec2_ids
name|'def'
name|'_get_ec2_ids'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ec2_ids'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'ec2_ids'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_inst_id'
op|'('
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'ec2_ids'
op|'['
string|"'ami_id'"
op|']'
op|'='
name|'ec2utils'
op|'.'
name|'glance_id_to_ec2_id'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'image_ref'
op|')'
newline|'\n'
name|'for'
name|'image_type'
name|'in'
op|'['
string|"'kernel'"
op|','
string|"'ramdisk'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'getattr'
op|'('
name|'instance'
op|','
string|"'%s_id'"
op|'%'
name|'image_type'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'image_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ec2_image_type'
op|'='
name|'ec2utils'
op|'.'
name|'image_type'
op|'('
name|'image_type'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'glance_id_to_ec2_id'
op|'('
name|'context'
op|','
name|'image_id'
op|','
nl|'\n'
name|'ec2_image_type'
op|')'
newline|'\n'
dedent|''
name|'ec2_ids'
op|'['
string|"'%s_id'"
op|'%'
name|'image_type'
op|']'
op|'='
name|'ec2_id'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ec2_ids'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance
name|'def'
name|'get_by_instance'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ec2_ids'
op|'='
name|'cls'
op|'.'
name|'_get_ec2_ids'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_dict'
op|'('
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'ec2_ids'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
