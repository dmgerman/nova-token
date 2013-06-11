begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata <yamahata@valinux co jp>'
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
name|'re'
newline|'\n'
nl|'\n'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
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
string|"'default_ephemeral_format'"
op|','
string|"'nova.virt.driver'"
op|')'
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
DECL|variable|DEFAULT_ROOT_DEV_NAME
name|'DEFAULT_ROOT_DEV_NAME'
op|'='
string|"'/dev/sda1'"
newline|'\n'
DECL|variable|_DEFAULT_MAPPINGS
name|'_DEFAULT_MAPPINGS'
op|'='
op|'{'
string|"'ami'"
op|':'
string|"'sda1'"
op|','
nl|'\n'
string|"'ephemeral0'"
op|':'
string|"'sda2'"
op|','
nl|'\n'
string|"'root'"
op|':'
name|'DEFAULT_ROOT_DEV_NAME'
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'sda3'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|bdm_legacy_fields
name|'bdm_legacy_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'device_name'"
op|','
string|"'delete_on_termination'"
op|','
nl|'\n'
string|"'virtual_name'"
op|','
string|"'snapshot_id'"
op|','
nl|'\n'
string|"'volume_id'"
op|','
string|"'volume_size'"
op|','
string|"'no_device'"
op|','
nl|'\n'
string|"'connection_info'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|bdm_new_fields
name|'bdm_new_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'source_type'"
op|','
string|"'destination_type'"
op|','
nl|'\n'
string|"'guest_format'"
op|','
string|"'device_type'"
op|','
string|"'disk_bus'"
op|','
string|"'boot_index'"
op|','
nl|'\n'
string|"'device_name'"
op|','
string|"'delete_on_termination'"
op|','
string|"'snapshot_id'"
op|','
nl|'\n'
string|"'volume_id'"
op|','
string|"'volume_size'"
op|','
string|"'image_id'"
op|','
string|"'no_device'"
op|','
nl|'\n'
string|"'connection_info'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|bdm_db_only_fields
name|'bdm_db_only_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'id'"
op|','
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|bdm_db_inherited_fields
name|'bdm_db_inherited_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
nl|'\n'
string|"'deleted_at'"
op|','
string|"'deleted'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BlockDeviceDict
name|'class'
name|'BlockDeviceDict'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a Block Device Mapping in Nova."""'
newline|'\n'
nl|'\n'
DECL|variable|_fields
name|'_fields'
op|'='
name|'bdm_new_fields'
newline|'\n'
DECL|variable|_db_only_fields
name|'_db_only_fields'
op|'='
op|'('
name|'bdm_db_only_fields'
op|'|'
nl|'\n'
name|'bdm_db_inherited_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'bdm_dict'
op|'='
name|'None'
op|','
name|'do_not_default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BlockDeviceDict'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'bdm_dict'
op|'='
name|'bdm_dict'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'do_not_default'
op|'='
name|'do_not_default'
name|'or'
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_validate'
op|'('
name|'bdm_dict'
op|')'
newline|'\n'
comment|'# NOTE (ndipanov): Never default db fields'
nl|'\n'
name|'self'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'dict'
op|'('
op|'('
name|'field'
op|','
name|'None'
op|')'
nl|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'_fields'
op|'-'
name|'do_not_default'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update'
op|'('
name|'bdm_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate
dedent|''
name|'def'
name|'_validate'
op|'('
name|'self'
op|','
name|'bdm_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Basic data format validations."""'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'set'
op|'('
name|'key'
name|'for'
name|'key'
op|','
name|'_'
name|'in'
name|'bdm_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|'<='
nl|'\n'
op|'('
name|'self'
op|'.'
name|'_fields'
op|'|'
name|'self'
op|'.'
name|'_db_only_fields'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|'('
op|')'
newline|'\n'
comment|'# TODO(ndipanov): Validate must-have fields!'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_legacy
name|'def'
name|'from_legacy'
op|'('
name|'cls'
op|','
name|'legacy_bdm'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'copy_over_fields'
op|'='
name|'bdm_legacy_fields'
op|'&'
name|'bdm_new_fields'
newline|'\n'
name|'copy_over_fields'
op|'|='
op|'('
name|'bdm_db_only_fields'
op|'|'
nl|'\n'
name|'bdm_db_inherited_fields'
op|')'
newline|'\n'
comment|'# NOTE (ndipanov): These fields cannot be computed'
nl|'\n'
comment|'# from legacy bdm, so do not default them'
nl|'\n'
comment|'# to avoid overwriting meaningful values in the db'
nl|'\n'
name|'non_computable_fields'
op|'='
name|'set'
op|'('
op|'['
string|"'boot_index'"
op|','
string|"'disk_bus'"
op|','
nl|'\n'
string|"'guest_format'"
op|','
string|"'device_type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'new_bdm'
op|'='
name|'dict'
op|'('
op|'('
name|'fld'
op|','
name|'val'
op|')'
name|'for'
name|'fld'
op|','
name|'val'
name|'in'
name|'legacy_bdm'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'fld'
name|'in'
name|'copy_over_fields'
op|')'
newline|'\n'
nl|'\n'
name|'virt_name'
op|'='
name|'legacy_bdm'
op|'.'
name|'get'
op|'('
string|"'virtual_name'"
op|')'
newline|'\n'
name|'volume_size'
op|'='
name|'legacy_bdm'
op|'.'
name|'get'
op|'('
string|"'volume_size'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'is_swap_or_ephemeral'
op|'('
name|'virt_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_bdm'
op|'['
string|"'source_type'"
op|']'
op|'='
string|"'blank'"
newline|'\n'
name|'new_bdm'
op|'['
string|"'delete_on_termination'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'new_bdm'
op|'['
string|"'destination_type'"
op|']'
op|'='
string|"'local'"
newline|'\n'
nl|'\n'
name|'if'
name|'virt_name'
op|'=='
string|"'swap'"
op|':'
newline|'\n'
indent|'                '
name|'new_bdm'
op|'['
string|"'guest_format'"
op|']'
op|'='
string|"'swap'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'new_bdm'
op|'['
string|"'guest_format'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'default_ephemeral_format'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'legacy_bdm'
op|'.'
name|'get'
op|'('
string|"'snapshot_id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_bdm'
op|'['
string|"'source_type'"
op|']'
op|'='
string|"'snapshot'"
newline|'\n'
name|'new_bdm'
op|'['
string|"'destination_type'"
op|']'
op|'='
string|"'volume'"
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'legacy_bdm'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_bdm'
op|'['
string|"'source_type'"
op|']'
op|'='
string|"'volume'"
newline|'\n'
name|'new_bdm'
op|'['
string|"'destination_type'"
op|']'
op|'='
string|"'volume'"
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'legacy_bdm'
op|'.'
name|'get'
op|'('
string|"'no_device'"
op|')'
op|':'
newline|'\n'
comment|'# NOTE (ndipanov): Just keep the BDM for now,'
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
name|'new_bdm'
op|','
name|'non_computable_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|member|legacy
dedent|''
name|'def'
name|'legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'copy_over_fields'
op|'='
name|'bdm_legacy_fields'
op|'-'
name|'set'
op|'('
op|'['
string|"'virtual_name'"
op|']'
op|')'
newline|'\n'
name|'copy_over_fields'
op|'|='
op|'('
name|'bdm_db_only_fields'
op|'|'
nl|'\n'
name|'bdm_db_inherited_fields'
op|')'
newline|'\n'
nl|'\n'
name|'legacy_block_device'
op|'='
name|'dict'
op|'('
op|'('
name|'field'
op|','
name|'self'
op|'.'
name|'get'
op|'('
name|'field'
op|')'
op|')'
nl|'\n'
name|'for'
name|'field'
name|'in'
name|'copy_over_fields'
name|'if'
name|'field'
name|'in'
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'source_type'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
string|"'source_type'"
op|')'
newline|'\n'
name|'no_device'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
string|"'no_device'"
op|')'
newline|'\n'
name|'if'
name|'source_type'
op|'=='
string|"'blank'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'['
string|"'guest_format'"
op|']'
op|'=='
string|"'swap'"
op|':'
newline|'\n'
indent|'                '
name|'legacy_block_device'
op|'['
string|"'virtual_name'"
op|']'
op|'='
string|"'swap'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE (ndipanov): Always label as 0, it is up to'
nl|'\n'
comment|'# the calling routine to re-enumerate them'
nl|'\n'
indent|'                '
name|'legacy_block_device'
op|'['
string|"'virtual_name'"
op|']'
op|'='
string|"'ephemeral0'"
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'source_type'
name|'in'
op|'('
string|"'volume'"
op|','
string|"'snapshot'"
op|')'
name|'or'
name|'no_device'
op|':'
newline|'\n'
indent|'            '
name|'legacy_block_device'
op|'['
string|"'virtual_name'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'source_type'
op|'=='
string|"'image'"
op|':'
newline|'\n'
comment|'# NOTE(ndipanov): Image bdms have no meaning in'
nl|'\n'
comment|'# the legacy format - raise'
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidBDMForLegacy'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'legacy_block_device'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_safe_for_update
dedent|''
dedent|''
name|'def'
name|'is_safe_for_update'
op|'('
name|'block_device_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine if passed dict is a safe subset for update.\n\n    Safe subset in this case means a safe subset of both legacy\n    and new versions of data, that can be passed to an UPDATE query\n    without any transformation.\n    """'
newline|'\n'
name|'fields'
op|'='
name|'set'
op|'('
name|'block_device_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'fields'
op|'<='
op|'('
name|'bdm_new_fields'
op|'|'
nl|'\n'
name|'bdm_db_inherited_fields'
op|'|'
nl|'\n'
name|'bdm_db_only_fields'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image_bdm
dedent|''
name|'def'
name|'create_image_bdm'
op|'('
name|'image_ref'
op|','
name|'boot_index'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a block device dict based on the image_ref.\n\n    This is useful in the API layer to keep the compatibility\n    with having an image_ref as a field in the instance requests\n    """'
newline|'\n'
name|'return'
name|'BlockDeviceDict'
op|'('
nl|'\n'
op|'{'
string|"'source_type'"
op|':'
string|"'image'"
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_ref'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
name|'boot_index'
op|','
nl|'\n'
string|"'device_type'"
op|':'
string|"'disk'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|legacy_mapping
dedent|''
name|'def'
name|'legacy_mapping'
op|'('
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Transform a list of block devices of an instance back to the\n    legacy data format."""'
newline|'\n'
nl|'\n'
name|'legacy_block_device_mapping'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'legacy_block_device'
op|'='
name|'BlockDeviceDict'
op|'('
name|'bdm'
op|')'
op|'.'
name|'legacy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidBDMForLegacy'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'legacy_block_device_mapping'
op|'.'
name|'append'
op|'('
name|'legacy_block_device'
op|')'
newline|'\n'
nl|'\n'
comment|'# Re-enumerate the ephemeral devices'
nl|'\n'
dedent|''
name|'for'
name|'i'
op|','
name|'dev'
name|'in'
name|'enumerate'
op|'('
name|'dev'
name|'for'
name|'dev'
name|'in'
name|'legacy_block_device_mapping'
nl|'\n'
name|'if'
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
name|'and'
nl|'\n'
name|'is_ephemeral'
op|'('
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
op|'='
name|'dev'
op|'['
string|"'virtual_name'"
op|']'
op|'['
op|':'
op|'-'
number|'1'
op|']'
op|'+'
name|'str'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'legacy_block_device_mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|properties_root_device_name
dedent|''
name|'def'
name|'properties_root_device_name'
op|'('
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""get root device name from image meta data.\n    If it isn\'t specified, return None.\n    """'
newline|'\n'
name|'root_device_name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# NOTE(yamahata): see image_service.s3.s3create()'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'mappings'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdm'
op|'['
string|"'virtual'"
op|']'
op|'=='
string|"'root'"
op|':'
newline|'\n'
indent|'            '
name|'root_device_name'
op|'='
name|'bdm'
op|'['
string|"'device'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): register_image's command line can override"
nl|'\n'
comment|'#                 <machine>.manifest.xml'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'root_device_name'"
name|'in'
name|'properties'
op|':'
newline|'\n'
indent|'        '
name|'root_device_name'
op|'='
name|'properties'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'root_device_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_ephemeral
dedent|''
name|'_ephemeral'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^ephemeral(\\d|[1-9]\\d+)$'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_ephemeral
name|'def'
name|'is_ephemeral'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_ephemeral'
op|'.'
name|'match'
op|'('
name|'device_name'
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ephemeral_num
dedent|''
name|'def'
name|'ephemeral_num'
op|'('
name|'ephemeral_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'is_ephemeral'
op|'('
name|'ephemeral_name'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'_ephemeral'
op|'.'
name|'sub'
op|'('
string|"'\\\\1'"
op|','
name|'ephemeral_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_swap_or_ephemeral
dedent|''
name|'def'
name|'is_swap_or_ephemeral'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
name|'device_name'
name|'and'
nl|'\n'
op|'('
name|'device_name'
op|'=='
string|"'swap'"
name|'or'
name|'is_ephemeral'
op|'('
name|'device_name'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mappings_prepend_dev
dedent|''
name|'def'
name|'mappings_prepend_dev'
op|'('
name|'mappings'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Prepend \'/dev/\' to \'device\' entry of swap/ephemeral virtual type."""'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'mappings'
op|':'
newline|'\n'
indent|'        '
name|'virtual'
op|'='
name|'m'
op|'['
string|"'virtual'"
op|']'
newline|'\n'
name|'if'
op|'('
name|'is_swap_or_ephemeral'
op|'('
name|'virtual'
op|')'
name|'and'
nl|'\n'
op|'('
name|'not'
name|'m'
op|'['
string|"'device'"
op|']'
op|'.'
name|'startswith'
op|'('
string|"'/'"
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'m'
op|'['
string|"'device'"
op|']'
op|'='
string|"'/dev/'"
op|'+'
name|'m'
op|'['
string|"'device'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_dev
dedent|''
name|'_dev'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^/dev/'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|strip_dev
name|'def'
name|'strip_dev'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""remove leading \'/dev/\'."""'
newline|'\n'
name|'return'
name|'_dev'
op|'.'
name|'sub'
op|'('
string|"''"
op|','
name|'device_name'
op|')'
name|'if'
name|'device_name'
name|'else'
name|'device_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_pref
dedent|''
name|'_pref'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^((x?v|s)d)'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|strip_prefix
name|'def'
name|'strip_prefix'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""remove both leading /dev/ and xvd or sd or vd."""'
newline|'\n'
name|'device_name'
op|'='
name|'strip_dev'
op|'('
name|'device_name'
op|')'
newline|'\n'
name|'return'
name|'_pref'
op|'.'
name|'sub'
op|'('
string|"''"
op|','
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_block_mapping
dedent|''
name|'def'
name|'instance_block_mapping'
op|'('
name|'instance'
op|','
name|'bdms'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'root_device_name'
op|'='
name|'instance'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
comment|'# NOTE(clayg): remove this when xenapi is setting default_root_device'
nl|'\n'
name|'if'
name|'root_device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'driver'
op|'.'
name|'compute_driver_matches'
op|'('
string|"'xenapi.XenAPIDriver'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_device_name'
op|'='
string|"'/dev/xvda'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_DEFAULT_MAPPINGS'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mappings'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mappings'
op|'['
string|"'ami'"
op|']'
op|'='
name|'strip_dev'
op|'('
name|'root_device_name'
op|')'
newline|'\n'
name|'mappings'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_device_name'
newline|'\n'
name|'default_ephemeral_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_ephemeral_device'"
op|')'
newline|'\n'
name|'if'
name|'default_ephemeral_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'ephemeral0'"
op|']'
op|'='
name|'default_ephemeral_device'
newline|'\n'
dedent|''
name|'default_swap_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_swap_device'"
op|')'
newline|'\n'
name|'if'
name|'default_swap_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'swap'"
op|']'
op|'='
name|'default_swap_device'
newline|'\n'
dedent|''
name|'ebs_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# 'ephemeralN', 'swap' and ebs"
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'bdms'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdm'
op|'['
string|"'no_device'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# ebs volume case'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
name|'or'
name|'bdm'
op|'['
string|"'snapshot_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ebs_devices'
op|'.'
name|'append'
op|'('
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'virtual_name'
op|'='
name|'bdm'
op|'['
string|"'virtual_name'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'virtual_name'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'is_swap_or_ephemeral'
op|'('
name|'virtual_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
name|'virtual_name'
op|']'
op|'='
name|'bdm'
op|'['
string|"'device_name'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): I'm not sure how ebs device should be numbered."
nl|'\n'
comment|'#                 Right now sort by device name for deterministic'
nl|'\n'
comment|'#                 result.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'        '
name|'nebs'
op|'='
number|'0'
newline|'\n'
name|'ebs_devices'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'ebs'
name|'in'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
string|"'ebs%d'"
op|'%'
name|'nebs'
op|']'
op|'='
name|'ebs'
newline|'\n'
name|'nebs'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|match_device
dedent|''
name|'def'
name|'match_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Matches device name and returns prefix, suffix."""'
newline|'\n'
name|'match'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
string|'"(^/dev/x{0,1}[a-z]{0,1}d{0,1})([a-z]+)[0-9]*$"'
op|','
name|'device'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_in_mapping
dedent|''
name|'def'
name|'volume_in_mapping'
op|'('
name|'mount_device'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'block_device_list'
op|'='
op|'['
name|'strip_dev'
op|'('
name|'vol'
op|'['
string|"'mount_device'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'vol'
name|'in'
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'swap'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
name|'swap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'block_device_list'
op|'.'
name|'append'
op|'('
name|'strip_dev'
op|'('
name|'swap'
op|'['
string|"'device_name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'block_device_list'
op|'+='
op|'['
name|'strip_dev'
op|'('
name|'ephemeral'
op|'['
string|"'device_name'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'ephemeral'
name|'in'
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"block_device_list %s"'
op|')'
op|','
name|'block_device_list'
op|')'
newline|'\n'
name|'return'
name|'strip_dev'
op|'('
name|'mount_device'
op|')'
name|'in'
name|'block_device_list'
newline|'\n'
dedent|''
endmarker|''
end_unit
