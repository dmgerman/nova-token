begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
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
name|'instance_fault'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance_info_cache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'security_group'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'utils'
name|'as'
name|'obj_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# These are fields that can be specified as expected_attrs'
nl|'\n'
DECL|variable|INSTANCE_OPTIONAL_FIELDS
name|'INSTANCE_OPTIONAL_FIELDS'
op|'='
op|'['
string|"'metadata'"
op|','
string|"'system_metadata'"
op|','
string|"'fault'"
op|']'
newline|'\n'
comment|'# These are fields that are always joined by the db right now'
nl|'\n'
DECL|variable|INSTANCE_IMPLIED_FIELDS
name|'INSTANCE_IMPLIED_FIELDS'
op|'='
op|'['
string|"'info_cache'"
op|','
string|"'security_groups'"
op|']'
newline|'\n'
comment|"# These are fields that are optional but don't translate to db columns"
nl|'\n'
DECL|variable|INSTANCE_OPTIONAL_NON_COLUMNS
name|'INSTANCE_OPTIONAL_NON_COLUMNS'
op|'='
op|'['
string|"'fault'"
op|']'
newline|'\n'
comment|'# These are all fields that most query calls load by default'
nl|'\n'
DECL|variable|INSTANCE_DEFAULT_FIELDS
name|'INSTANCE_DEFAULT_FIELDS'
op|'='
name|'INSTANCE_OPTIONAL_FIELDS'
op|'+'
name|'INSTANCE_IMPLIED_FIELDS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Instance
name|'class'
name|'Instance'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added info_cache'
nl|'\n'
comment|'# Version 1.2: Added security_groups'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'int'
op|','
nl|'\n'
nl|'\n'
string|"'user_id'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'image_ref'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'hostname'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'launch_index'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
string|"'key_name'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'key_data'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'power_state'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'memory_mb'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'host'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'node'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'instance_type_id'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'user_data'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'reservation_id'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'obj_utils'
op|'.'
name|'datetime_or_str_or_none'
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'obj_utils'
op|'.'
name|'datetime_or_str_or_none'
op|','
nl|'\n'
string|"'terminated_at'"
op|':'
name|'obj_utils'
op|'.'
name|'datetime_or_str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'availability_zone'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'display_name'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'launched_on'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'locked'"
op|':'
name|'bool'
op|','
nl|'\n'
nl|'\n'
string|"'os_type'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'architecture'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'vm_mode'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'root_device_name'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'default_ephemeral_device'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'default_swap_device'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'config_drive'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'obj_utils'
op|'.'
name|'ip_or_none'
op|'('
number|'4'
op|')'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'obj_utils'
op|'.'
name|'ip_or_none'
op|'('
number|'6'
op|')'
op|','
nl|'\n'
nl|'\n'
string|"'auto_disk_config'"
op|':'
name|'bool'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'obj_utils'
op|'.'
name|'int_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'shutdown_terminate'"
op|':'
name|'bool'
op|','
nl|'\n'
string|"'disable_terminate'"
op|':'
name|'bool'
op|','
nl|'\n'
nl|'\n'
string|"'cell_name'"
op|':'
name|'obj_utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
nl|'\n'
string|"'metadata'"
op|':'
name|'dict'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'dict'
op|','
nl|'\n'
nl|'\n'
string|"'info_cache'"
op|':'
name|'obj_utils'
op|'.'
name|'nested_object_or_none'
op|'('
nl|'\n'
name|'instance_info_cache'
op|'.'
name|'InstanceInfoCache'
op|')'
op|','
nl|'\n'
nl|'\n'
string|"'security_groups'"
op|':'
name|'obj_utils'
op|'.'
name|'nested_object_or_none'
op|'('
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroupList'
op|')'
op|','
nl|'\n'
nl|'\n'
string|"'fault'"
op|':'
name|'obj_utils'
op|'.'
name|'nested_object_or_none'
op|'('
nl|'\n'
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_extra_fields
name|'obj_extra_fields'
op|'='
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|name
name|'def'
name|'name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'base_name'
op|'='
name|'CONF'
op|'.'
name|'instance_name_template'
op|'%'
name|'self'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|'# Support templates like "uuid-%(uuid)s", etc.'
nl|'\n'
indent|'            '
name|'info'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|"# NOTE(russellb): Don't use self.iteritems() here, as it will"
nl|'\n'
comment|'# result in infinite recursion on the name property.'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
comment|'# prevent recursion if someone specifies %(name)s'
nl|'\n'
comment|'# %(name)s will not be valid.'
nl|'\n'
indent|'                '
name|'if'
name|'key'
op|'=='
string|"'name'"
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'info'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'base_name'
op|'='
name|'CONF'
op|'.'
name|'instance_name_template'
op|'%'
name|'info'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'base_name'
op|'='
name|'self'
op|'.'
name|'uuid'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'base_name'
newline|'\n'
nl|'\n'
DECL|member|_attr_access_ip_v4_to_primitive
dedent|''
name|'def'
name|'_attr_access_ip_v4_to_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'access_ip_v4'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'access_ip_v4'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_attr_access_ip_v6_to_primitive
dedent|''
dedent|''
name|'def'
name|'_attr_access_ip_v6_to_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'access_ip_v6'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'access_ip_v6'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|_attr_scheduled_at_to_primitive
dedent|''
dedent|''
name|'_attr_scheduled_at_to_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_serializer'
op|'('
string|"'scheduled_at'"
op|')'
newline|'\n'
DECL|variable|_attr_launched_at_to_primitive
name|'_attr_launched_at_to_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_serializer'
op|'('
string|"'launched_at'"
op|')'
newline|'\n'
DECL|variable|_attr_terminated_at_to_primitive
name|'_attr_terminated_at_to_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_serializer'
op|'('
string|"'terminated_at'"
op|')'
newline|'\n'
DECL|variable|_attr_info_cache_to_primitive
name|'_attr_info_cache_to_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'obj_serializer'
op|'('
string|"'info_cache'"
op|')'
newline|'\n'
DECL|variable|_attr_security_groups_to_primitive
name|'_attr_security_groups_to_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'obj_serializer'
op|'('
nl|'\n'
string|"'security_groups'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_attr_scheduled_at_from_primitive
name|'_attr_scheduled_at_from_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_deserializer'
newline|'\n'
DECL|variable|_attr_launched_at_from_primitive
name|'_attr_launched_at_from_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_deserializer'
newline|'\n'
DECL|variable|_attr_terminated_at_from_primitive
name|'_attr_terminated_at_from_primitive'
op|'='
name|'obj_utils'
op|'.'
name|'dt_deserializer'
newline|'\n'
nl|'\n'
DECL|member|_attr_info_cache_from_primitive
name|'def'
name|'_attr_info_cache_from_primitive'
op|'('
name|'self'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'obj_from_primitive'
op|'('
name|'val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attr_security_groups_from_primitive
dedent|''
name|'def'
name|'_attr_security_groups_from_primitive'
op|'('
name|'self'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'obj_from_primitive'
op|'('
name|'val'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'db_inst'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Method to help with migration to objects.\n\n        Converts a database entity to a formal object.\n        """'
newline|'\n'
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
comment|'# Most of the field names match right now, so be quick'
nl|'\n'
dedent|''
name|'for'
name|'field'
name|'in'
name|'instance'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'in'
name|'INSTANCE_OPTIONAL_FIELDS'
op|'+'
name|'INSTANCE_IMPLIED_FIELDS'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'deleted'"
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'deleted'
op|'='
name|'db_inst'
op|'['
string|"'deleted'"
op|']'
op|'=='
name|'db_inst'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'['
name|'field'
op|']'
op|'='
name|'db_inst'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'metadata'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'utils'
op|'.'
name|'metadata_to_dict'
op|'('
name|'db_inst'
op|'['
string|"'metadata'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'system_metadata'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'utils'
op|'.'
name|'metadata_to_dict'
op|'('
nl|'\n'
name|'db_inst'
op|'['
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'fault'"
name|'in'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'fault'"
op|']'
op|'='
op|'('
nl|'\n'
name|'instance_fault'
op|'.'
name|'InstanceFault'
op|'.'
name|'get_latest_for_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'.'
name|'uuid'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(danms): info_cache and security_groups are almost always joined'
nl|'\n'
comment|"# in the DB layer right now, so check to see if they're filled instead"
nl|'\n'
comment|'# of looking at expected_attrs'
nl|'\n'
dedent|''
name|'if'
name|'db_inst'
op|'['
string|"'info_cache'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'info_cache'"
op|']'
op|'='
name|'instance_info_cache'
op|'.'
name|'InstanceInfoCache'
op|'('
op|')'
newline|'\n'
name|'instance_info_cache'
op|'.'
name|'InstanceInfoCache'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'info_cache'"
op|']'
op|','
name|'db_inst'
op|'['
string|"'info_cache'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'db_inst'
op|'['
string|"'security_groups'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'['
string|"'security_groups'"
op|']'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroupList'
op|'('
op|')'
newline|'\n'
name|'security_group'
op|'.'
name|'_make_secgroup_list'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'security_groups'"
op|']'
op|','
nl|'\n'
name|'db_inst'
op|'['
string|"'security_groups'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_attrs_to_columns
name|'def'
name|'_attrs_to_columns'
op|'('
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Translate instance attributes into columns needing joining."""'
newline|'\n'
name|'columns_to_join'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
string|"'metadata'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'            '
name|'columns_to_join'
op|'.'
name|'append'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'system_metadata'"
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'            '
name|'columns_to_join'
op|'.'
name|'append'
op|'('
string|"'system_metadata'"
op|')'
newline|'\n'
comment|'# NOTE(danms): The DB API currently always joins info_cache and'
nl|'\n'
comment|"# security_groups for get operations, so don't add them to the"
nl|'\n'
comment|'# list of columns'
nl|'\n'
dedent|''
name|'return'
name|'columns_to_join'
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
name|'uuid'
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
name|'columns_to_join'
op|'='
name|'cls'
op|'.'
name|'_attrs_to_columns'
op|'('
name|'expected_attrs'
op|')'
newline|'\n'
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'columns_to_join'
op|')'
newline|'\n'
name|'return'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
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
name|'inst_id'
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
name|'columns_to_join'
op|'='
name|'cls'
op|'.'
name|'_attrs_to_columns'
op|'('
name|'expected_attrs'
op|')'
newline|'\n'
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'inst_id'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'columns_to_join'
op|')'
newline|'\n'
name|'return'
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_save_info_cache
dedent|''
name|'def'
name|'_save_info_cache'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'info_cache'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_save_security_groups
dedent|''
name|'def'
name|'_save_security_groups'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'secgroup'
name|'in'
name|'self'
op|'.'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'secgroup'
op|'.'
name|'save'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_save_instance_fault
dedent|''
dedent|''
name|'def'
name|'_save_instance_fault'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(danms): I don't think we need to worry about this, do we?"
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
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
op|','
name|'context'
op|','
name|'expected_task_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Save updates to this instance\n\n        Column-wise updates will be made based on the result of\n        self.what_changed(). If expected_task_state is provided,\n        it will be checked against the in-database copy of the\n        instance before updates are made.\n        :param context: Security context\n        :param expected_task_state: Optional tuple of valid task states\n                                    for the instance to be in.\n        """'
newline|'\n'
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'changes'
op|'='
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'hasattr'
op|'('
name|'self'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'field'
op|')'
op|')'
name|'and'
nl|'\n'
name|'isinstance'
op|'('
name|'self'
op|'['
name|'field'
op|']'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'getattr'
op|'('
name|'self'
op|','
string|"'_save_%s'"
op|'%'
name|'field'
op|')'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'field'
name|'in'
name|'changes'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'field'
op|']'
op|'='
name|'self'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'expected_task_state'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'expected_task_state'"
op|']'
op|'='
name|'expected_task_state'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'old_ref'
op|','
name|'inst_ref'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
name|'expected_attrs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'INSTANCE_OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'hasattr'
op|'('
name|'self'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'attr'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'expected_attrs'
op|'.'
name|'append'
op|'('
name|'attr'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'inst_ref'
op|','
name|'expected_attrs'
op|')'
newline|'\n'
name|'if'
string|"'vm_state'"
name|'in'
name|'changes'
name|'or'
string|"'task_state'"
name|'in'
name|'changes'
op|':'
newline|'\n'
indent|'                '
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'inst_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|refresh
name|'def'
name|'refresh'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'extra'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'INSTANCE_OPTIONAL_FIELDS'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hasattr'
op|'('
name|'self'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'field'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'extra'
op|'.'
name|'append'
op|'('
name|'field'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'current'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|'='
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'extra'
op|')'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'hasattr'
op|'('
name|'self'
op|','
name|'base'
op|'.'
name|'get_attrname'
op|'('
name|'field'
op|')'
op|')'
name|'and'
nl|'\n'
name|'self'
op|'['
name|'field'
op|']'
op|'!='
name|'current'
op|'['
name|'field'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'['
name|'field'
op|']'
op|'='
name|'current'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'obj_reset_changes'
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
name|'extra'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'attrname'
op|'=='
string|"'system_metadata'"
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'append'
op|'('
string|"'system_metadata'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'attrname'
op|'=='
string|"'metadata'"
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'append'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'attrname'
op|'=='
string|"'info_cache'"
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'append'
op|'('
string|"'info_cache'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'attrname'
op|'=='
string|"'security_groups'"
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'append'
op|'('
string|"'security_groups'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'attrname'
op|'=='
string|"'fault'"
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'.'
name|'append'
op|'('
string|"'fault'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'extra'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'\'Cannot load "%s" from instance\''
op|'%'
name|'attrname'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): This could be optimized to just load the bits we need'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'extra'
op|')'
newline|'\n'
name|'self'
op|'['
name|'attrname'
op|']'
op|'='
name|'instance'
op|'['
name|'attrname'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_instance_list
dedent|''
dedent|''
name|'def'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'inst_list'
op|','
name|'db_inst_list'
op|','
name|'expected_attrs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'get_fault'
op|'='
name|'expected_attrs'
name|'and'
string|"'fault'"
name|'in'
name|'expected_attrs'
newline|'\n'
name|'inst_faults'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'get_fault'
op|':'
newline|'\n'
comment|'# Build an instance_uuid:latest-fault mapping'
nl|'\n'
indent|'        '
name|'expected_attrs'
op|'.'
name|'remove'
op|'('
string|"'fault'"
op|')'
newline|'\n'
name|'instance_uuids'
op|'='
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'db_inst_list'
op|']'
newline|'\n'
name|'faults'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFaultList'
op|'.'
name|'get_by_instance_uuids'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'for'
name|'fault'
name|'in'
name|'faults'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fault'
op|'.'
name|'instance_uuid'
name|'not'
name|'in'
name|'inst_faults'
op|':'
newline|'\n'
indent|'                '
name|'inst_faults'
op|'['
name|'fault'
op|'.'
name|'instance_uuid'
op|']'
op|'='
name|'fault'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'inst_list'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'db_inst'
name|'in'
name|'db_inst_list'
op|':'
newline|'\n'
indent|'        '
name|'inst_obj'
op|'='
name|'Instance'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'Instance'
op|'('
op|')'
op|','
name|'db_inst'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'expected_attrs'
op|')'
newline|'\n'
name|'if'
name|'get_fault'
op|':'
newline|'\n'
indent|'            '
name|'inst_obj'
op|'.'
name|'fault'
op|'='
name|'inst_faults'
op|'.'
name|'get'
op|'('
name|'inst_obj'
op|'.'
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'inst_list'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'inst_obj'
op|')'
newline|'\n'
dedent|''
name|'inst_list'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst_list'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|expected_cols
dedent|''
name|'def'
name|'expected_cols'
op|'('
name|'expected_attrs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return expected_attrs that are columns needing joining."""'
newline|'\n'
name|'if'
name|'expected_attrs'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'list'
op|'('
name|'set'
op|'('
name|'expected_attrs'
op|')'
op|'-'
name|'set'
op|'('
name|'INSTANCE_OPTIONAL_NON_COLUMNS'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'expected_attrs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceList
dedent|''
dedent|''
name|'class'
name|'InstanceList'
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
indent|'    '
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_filters
name|'def'
name|'get_by_filters'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|'='
name|'None'
op|','
name|'sort_dir'
op|'='
name|'None'
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst_list'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|','
name|'sort_key'
op|','
name|'sort_dir'
op|','
name|'limit'
op|'='
name|'limit'
op|','
name|'marker'
op|'='
name|'marker'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'expected_cols'
op|'('
name|'expected_attrs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst_list'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host
name|'def'
name|'get_by_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst_list'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'columns_to_join'
op|'='
name|'expected_cols'
op|'('
name|'expected_attrs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst_list'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_node
name|'def'
name|'get_by_host_and_node'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'node'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst_list'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host_and_node'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'return'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst_list'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_not_type
name|'def'
name|'get_by_host_and_not_type'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'type_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst_list'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host_and_not_type'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'type_id'
op|'='
name|'type_id'
op|')'
newline|'\n'
name|'return'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst_list'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_hung_in_rebooting
name|'def'
name|'get_hung_in_rebooting'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'reboot_window'
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst_list'
op|'='
name|'db'
op|'.'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'context'
op|','
nl|'\n'
name|'reboot_window'
op|')'
newline|'\n'
name|'return'
name|'_make_instance_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_inst_list'
op|','
nl|'\n'
name|'expected_attrs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fill_faults
dedent|''
name|'def'
name|'fill_faults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Batch query the database for our instances\' faults.\n\n        :returns: A list of instance uuids for which faults were found.\n        """'
newline|'\n'
name|'uuids'
op|'='
op|'['
name|'inst'
op|'.'
name|'uuid'
name|'for'
name|'inst'
name|'in'
name|'self'
op|']'
newline|'\n'
name|'faults'
op|'='
name|'instance_fault'
op|'.'
name|'InstanceFaultList'
op|'.'
name|'get_by_instance_uuids'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'uuids'
op|')'
newline|'\n'
name|'faults_by_uuid'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'fault'
name|'in'
name|'faults'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fault'
op|'.'
name|'instance_uuid'
name|'not'
name|'in'
name|'faults_by_uuid'
op|':'
newline|'\n'
indent|'                '
name|'faults_by_uuid'
op|'['
name|'fault'
op|'.'
name|'instance_uuid'
op|']'
op|'='
name|'fault'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'instance'
name|'in'
name|'self'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'.'
name|'uuid'
name|'in'
name|'faults_by_uuid'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'fault'
op|'='
name|'faults_by_uuid'
op|'['
name|'instance'
op|'.'
name|'uuid'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(danms): Otherwise the caller will cause a lazy-load'
nl|'\n'
comment|'# when checking it, and we know there are none'
nl|'\n'
indent|'                '
name|'instance'
op|'.'
name|'fault'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'instance'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'fault'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'faults_by_uuid'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
