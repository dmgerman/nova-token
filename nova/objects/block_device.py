begin_unit
comment|'#    Copyright 2013 Red Hat Inc.'
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'opts'
name|'as'
name|'cells_opts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'rpcapi'
name|'as'
name|'cells_rpcapi'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
DECL|variable|_BLOCK_DEVICE_OPTIONAL_JOINED_FIELD
name|'_BLOCK_DEVICE_OPTIONAL_JOINED_FIELD'
op|'='
op|'['
string|"'instance'"
op|']'
newline|'\n'
DECL|variable|BLOCK_DEVICE_OPTIONAL_ATTRS
name|'BLOCK_DEVICE_OPTIONAL_ATTRS'
op|'='
name|'_BLOCK_DEVICE_OPTIONAL_JOINED_FIELD'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_expected_cols
name|'def'
name|'_expected_cols'
op|'('
name|'expected_attrs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'attr'
name|'for'
name|'attr'
name|'in'
name|'expected_attrs'
nl|'\n'
name|'if'
name|'attr'
name|'in'
name|'_BLOCK_DEVICE_OPTIONAL_JOINED_FIELD'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'BlockDeviceMapping'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|BlockDeviceMapping
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add instance_uuid to get_by_volume_id method'
nl|'\n'
comment|'# Version 1.2: Instance version 1.14'
nl|'\n'
comment|'# Version 1.3: Instance version 1.15'
nl|'\n'
comment|'# Version 1.4: Instance version 1.16'
nl|'\n'
comment|'# Version 1.5: Instance version 1.17'
nl|'\n'
comment|'# Version 1.6: Instance version 1.18'
nl|'\n'
comment|'# Version 1.7: Add update_or_create method'
nl|'\n'
comment|'# Version 1.8: Instance version 1.19'
nl|'\n'
comment|'# Version 1.9: Instance version 1.20'
nl|'\n'
comment|'# Version 1.10: Changed source_type field to BlockDeviceSourceTypeField.'
nl|'\n'
comment|'# Version 1.11: Changed destination_type field to'
nl|'\n'
comment|'#               BlockDeviceDestinationTypeField.'
nl|'\n'
comment|'# Version 1.12: Changed device_type field to BlockDeviceTypeField.'
nl|'\n'
comment|'# Version 1.13: Instance version 1.21'
nl|'\n'
comment|'# Version 1.14: Instance version 1.22'
nl|'\n'
comment|'# Version 1.15: Instance version 1.23'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.15'"
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
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Instance'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'source_type'"
op|':'
name|'fields'
op|'.'
name|'BlockDeviceSourceTypeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'destination_type'"
op|':'
name|'fields'
op|'.'
name|'BlockDeviceDestinationTypeField'
op|'('
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'guest_format'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'device_type'"
op|':'
name|'fields'
op|'.'
name|'BlockDeviceTypeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'disk_bus'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'device_name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'volume_size'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'connection_info'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
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
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'block_device_obj'
op|','
nl|'\n'
name|'db_block_device'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'expected_attrs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'block_device_obj'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'BLOCK_DEVICE_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'block_device_obj'
op|'['
name|'key'
op|']'
op|'='
name|'db_block_device'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'instance'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'my_inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|')'
newline|'\n'
name|'my_inst'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'my_inst'
op|','
nl|'\n'
name|'db_block_device'
op|'['
string|"'instance'"
op|']'
op|')'
newline|'\n'
name|'block_device_obj'
op|'.'
name|'instance'
op|'='
name|'my_inst'
newline|'\n'
nl|'\n'
dedent|''
name|'block_device_obj'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'block_device_obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'block_device_obj'
newline|'\n'
nl|'\n'
DECL|member|_create
dedent|''
name|'def'
name|'_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'update_or_create'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the block device record in the database.\n\n        In case the id field is set on the object, and if the instance is set\n        raise an ObjectActionError. Resets all the changes on the object.\n\n        Returns None\n\n        :param context: security context used for database calls\n        :param update_or_create: consider existing block devices for the\n                instance based on the device name and swap, and only update\n                the ones that match. Normally only used when creating the\n                instance for the first time.\n        """'
newline|'\n'
name|'cell_type'
op|'='
name|'cells_opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
newline|'\n'
name|'if'
name|'cell_type'
op|'=='
string|"'api'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'BlockDeviceMapping cannot be '"
nl|'\n'
string|"'created in the API cell.'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'instance'"
name|'in'
name|'updates'
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
string|"'instance assigned'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cells_create'
op|'='
name|'update_or_create'
name|'or'
name|'None'
newline|'\n'
name|'if'
name|'update_or_create'
op|':'
newline|'\n'
indent|'            '
name|'db_bdm'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
nl|'\n'
name|'context'
op|','
name|'updates'
op|','
name|'legacy'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'db_bdm'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_create'
op|'('
nl|'\n'
name|'context'
op|','
name|'updates'
op|','
name|'legacy'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_bdm'
op|')'
newline|'\n'
comment|'# NOTE(alaski): bdms are looked up by instance uuid and device_name'
nl|'\n'
comment|'# so if we sync up with no device_name an entry will be created that'
nl|'\n'
comment|'# will not be found on a later update_or_create call and a second bdm'
nl|'\n'
comment|'# create will occur.'
nl|'\n'
name|'if'
name|'cell_type'
op|'=='
string|"'compute'"
name|'and'
name|'db_bdm'
op|'.'
name|'get'
op|'('
string|"'device_name'"
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cells_api'
op|'='
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
newline|'\n'
name|'cells_api'
op|'.'
name|'bdm_update_or_create_at_top'
op|'('
nl|'\n'
name|'context'
op|','
name|'self'
op|','
name|'create'
op|'='
name|'cells_create'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'self'
op|'.'
name|'_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|update_or_create
name|'def'
name|'update_or_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'update_or_create'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
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
string|"'destroy'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already destroyed'"
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'block_device_mapping_destroy'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'delattr'
op|'('
name|'self'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cell_type'
op|'='
name|'cells_opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
newline|'\n'
name|'if'
name|'cell_type'
op|'=='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'cells_api'
op|'='
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
newline|'\n'
name|'cells_api'
op|'.'
name|'bdm_destroy_at_top'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'self'
op|'.'
name|'device_name'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'if'
string|"'instance'"
name|'in'
name|'updates'
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
string|"'save'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'instance changed'"
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'updated'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
name|'updates'
op|','
name|'legacy'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'updated'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'BDMNotFound'
op|'('
name|'id'
op|'='
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
dedent|''
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
name|'updated'
op|')'
newline|'\n'
name|'cell_type'
op|'='
name|'cells_opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
newline|'\n'
name|'if'
name|'cell_type'
op|'=='
string|"'compute'"
op|':'
newline|'\n'
indent|'            '
name|'create'
op|'='
name|'False'
newline|'\n'
comment|'# NOTE(alaski): If the device name has just been set this bdm'
nl|'\n'
comment|'# likely does not exist in the parent cell and we should create it.'
nl|'\n'
comment|'# If this is a modification of the device name we should update'
nl|'\n'
comment|'# rather than create which is why None is used here instead of True'
nl|'\n'
name|'if'
string|"'device_name'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'                '
name|'create'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'cells_api'
op|'='
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
newline|'\n'
name|'cells_api'
op|'.'
name|'bdm_update_or_create_at_top'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
nl|'\n'
name|'create'
op|'='
name|'create'
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
DECL|member|get_by_volume_id
name|'def'
name|'get_by_volume_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'None'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'expected_attrs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'db_bdm'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_get_by_volume_id'
op|'('
nl|'\n'
name|'context'
op|','
name|'volume_id'
op|','
name|'_expected_cols'
op|'('
name|'expected_attrs'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_bdm'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeBDMNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
comment|'# NOTE (ndipanov): Move this to the db layer into a'
nl|'\n'
comment|'# get_by_instance_and_volume_id method'
nl|'\n'
dedent|''
name|'if'
name|'instance_uuid'
name|'and'
name|'instance_uuid'
op|'!='
name|'db_bdm'
op|'['
string|"'instance_uuid'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Volume does not belong to the "'
nl|'\n'
string|'"requested instance."'
op|')'
op|')'
newline|'\n'
dedent|''
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
name|'db_bdm'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_root
name|'def'
name|'is_root'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'boot_index'
op|'=='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_volume
name|'def'
name|'is_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'self'
op|'.'
name|'destination_type'
op|'=='
nl|'\n'
name|'fields'
op|'.'
name|'BlockDeviceDestinationType'
op|'.'
name|'VOLUME'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_image
name|'def'
name|'is_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'source_type'
op|'=='
name|'fields'
op|'.'
name|'BlockDeviceSourceType'
op|'.'
name|'IMAGE'
newline|'\n'
nl|'\n'
DECL|member|get_image_mapping
dedent|''
name|'def'
name|'get_image_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'self'
op|')'
op|'.'
name|'get_image_mapping'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
dedent|''
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attrname'
name|'not'
name|'in'
name|'BLOCK_DEVICE_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'attribute %s not lazy-loadable'"
op|'%'
name|'attrname'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_context'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OrphanedObjectError'
op|'('
name|'method'
op|'='
string|"'obj_load_attr'"
op|','
nl|'\n'
name|'objtype'
op|'='
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Lazy-loading `%(attr)s\' on %(name)s uuid %(uuid)s"'
op|','
nl|'\n'
op|'{'
string|"'attr'"
op|':'
name|'attrname'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
name|'fields'
op|'='
op|'['
string|"'instance'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|BlockDeviceMappingList
name|'class'
name|'BlockDeviceMappingList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: BlockDeviceMapping <= version 1.1'
nl|'\n'
comment|'# Version 1.2: Added use_slave to get_by_instance_uuid'
nl|'\n'
comment|'# Version 1.3: BlockDeviceMapping <= version 1.2'
nl|'\n'
comment|'# Version 1.4: BlockDeviceMapping <= version 1.3'
nl|'\n'
comment|'# Version 1.5: BlockDeviceMapping <= version 1.4'
nl|'\n'
comment|'# Version 1.6: BlockDeviceMapping <= version 1.5'
nl|'\n'
comment|'# Version 1.7: BlockDeviceMapping <= version 1.6'
nl|'\n'
comment|'# Version 1.8: BlockDeviceMapping <= version 1.7'
nl|'\n'
comment|'# Version 1.9: BlockDeviceMapping <= version 1.8'
nl|'\n'
comment|'# Version 1.10: BlockDeviceMapping <= version 1.9'
nl|'\n'
comment|'# Version 1.11: BlockDeviceMapping <= version 1.10'
nl|'\n'
comment|'# Version 1.12: BlockDeviceMapping <= version 1.11'
nl|'\n'
comment|'# Version 1.13: BlockDeviceMapping <= version 1.12'
nl|'\n'
comment|'# Version 1.14: BlockDeviceMapping <= version 1.13'
nl|'\n'
comment|'# Version 1.15: BlockDeviceMapping <= version 1.14'
nl|'\n'
comment|'# Version 1.16: BlockDeviceMapping <= version 1.15'
nl|'\n'
comment|'# Version 1.17: Add get_by_instance_uuids()'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.17'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'BlockDeviceMapping'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|instance_uuids
name|'def'
name|'instance_uuids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
nl|'\n'
name|'bdm'
op|'.'
name|'instance_uuid'
name|'for'
name|'bdm'
name|'in'
name|'self'
nl|'\n'
name|'if'
name|'bdm'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'instance_uuid'"
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|bdms_by_instance_uuid
name|'def'
name|'bdms_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdms'
op|'='
name|'cls'
op|'.'
name|'get_by_instance_uuids'
op|'('
name|'context'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_dict_of_lists'
op|'('
nl|'\n'
name|'context'
op|','
name|'cls'
op|','
name|'bdms'
op|','
string|"'instance_uuid'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuids
name|'def'
name|'get_by_instance_uuids'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuids'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_bdms'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance_uuids'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuids'
op|','
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
nl|'\n'
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|','
name|'db_bdms'
name|'or'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_bdms'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
nl|'\n'
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|','
name|'db_bdms'
name|'or'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|root_bdm
dedent|''
name|'def'
name|'root_bdm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""It only makes sense to call this method when the\n        BlockDeviceMappingList contains BlockDeviceMappings from\n        exactly one instance rather than BlockDeviceMappings from\n        multiple instances.\n\n        For example, you should not call this method from a\n        BlockDeviceMappingList created by get_by_instance_uuids(),\n        but you may call this method from a BlockDeviceMappingList\n        created by get_by_instance_uuid().\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'self'
op|'.'
name|'instance_uuids'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'UndefinedRootBDM'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'next'
op|'('
name|'bdm_obj'
name|'for'
name|'bdm_obj'
name|'in'
name|'self'
name|'if'
name|'bdm_obj'
op|'.'
name|'is_root'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_make_list
dedent|''
dedent|''
dedent|''
name|'def'
name|'block_device_make_list'
op|'('
name|'context'
op|','
name|'db_list'
op|','
op|'**'
name|'extra_args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMappingList'
op|'('
name|'context'
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|','
name|'db_list'
op|','
nl|'\n'
op|'**'
name|'extra_args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_device_make_list_from_dicts
dedent|''
name|'def'
name|'block_device_make_list_from_dicts'
op|'('
name|'context'
op|','
name|'bdm_dicts_list'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'bdm_objects'
op|'='
op|'['
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
name|'context'
op|'='
name|'context'
op|','
op|'**'
name|'bdm'
op|')'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'bdm_dicts_list'
op|']'
newline|'\n'
name|'return'
name|'BlockDeviceMappingList'
op|'('
name|'objects'
op|'='
name|'bdm_objects'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
