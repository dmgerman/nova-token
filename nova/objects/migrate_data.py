begin_unit
comment|'#    Copyright 2015 Red Hat, Inc.'
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
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
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
name|'as'
name|'obj_base'
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
name|'log'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register_if'
op|'('
name|'False'
op|')'
newline|'\n'
DECL|class|LiveMigrateData
name|'class'
name|'LiveMigrateData'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'is_volume_backed'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'migration'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Migration'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|to_legacy_dict
name|'def'
name|'to_legacy_dict'
op|'('
name|'self'
op|','
name|'pre_migration_result'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'legacy'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'is_volume_backed'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'is_volume_backed'"
op|']'
op|'='
name|'self'
op|'.'
name|'is_volume_backed'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migration'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'migration'"
op|']'
op|'='
name|'self'
op|'.'
name|'migration'
newline|'\n'
dedent|''
name|'if'
name|'pre_migration_result'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'legacy'
newline|'\n'
nl|'\n'
DECL|member|from_legacy_dict
dedent|''
name|'def'
name|'from_legacy_dict'
op|'('
name|'self'
op|','
name|'legacy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'is_volume_backed'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_volume_backed'
op|'='
name|'legacy'
op|'['
string|"'is_volume_backed'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'migration'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'migration'
op|'='
name|'legacy'
op|'['
string|"'migration'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|detect_implementation
name|'def'
name|'detect_implementation'
op|'('
name|'cls'
op|','
name|'legacy_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'instance_relative_path'"
name|'in'
name|'legacy_dict'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'LibvirtLiveMigrateData'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'image_type'"
name|'in'
name|'legacy_dict'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'LibvirtLiveMigrateData'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'migrate_data'"
name|'in'
name|'legacy_dict'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'XenapiLiveMigrateData'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'LiveMigrateData'
op|'('
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'.'
name|'from_legacy_dict'
op|'('
name|'legacy_dict'
op|')'
newline|'\n'
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|LibvirtLiveMigrateBDMInfo
name|'class'
name|'LibvirtLiveMigrateBDMInfo'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
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
comment|'# FIXME(danms): some of these can be enums?'
nl|'\n'
string|"'serial'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'bus'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'dev'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'format'"
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
string|"'connection_info_json'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|"# NOTE(danms): We don't have a connection_info object right"
nl|'\n'
comment|"# now, and instead mostly store/pass it as JSON that we're"
nl|'\n'
comment|'# careful with. When we get a connection_info object in the'
nl|'\n'
comment|'# future, we should use it here, so make this easy to convert'
nl|'\n'
comment|'# for later.'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|connection_info
name|'def'
name|'connection_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'connection_info_json'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'connection_info'
op|'.'
name|'setter'
newline|'\n'
DECL|member|connection_info
name|'def'
name|'connection_info'
op|'('
name|'self'
op|','
name|'info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection_info_json'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|as_disk_info
dedent|''
name|'def'
name|'as_disk_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info_dict'
op|'='
op|'{'
nl|'\n'
string|"'dev'"
op|':'
name|'self'
op|'.'
name|'dev'
op|','
nl|'\n'
string|"'bus'"
op|':'
name|'self'
op|'.'
name|'bus'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'self'
op|'.'
name|'type'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'format'"
op|')'
name|'and'
name|'self'
op|'.'
name|'format'
op|':'
newline|'\n'
indent|'            '
name|'info_dict'
op|'['
string|"'format'"
op|']'
op|'='
name|'self'
op|'.'
name|'format'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'boot_index'"
op|')'
name|'and'
name|'self'
op|'.'
name|'boot_index'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'info_dict'
op|'['
string|"'boot_index'"
op|']'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'boot_index'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'info_dict'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|LibvirtLiveMigrateData
name|'class'
name|'LibvirtLiveMigrateData'
op|'('
name|'LiveMigrateData'
op|')'
op|':'
newline|'\n'
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
string|"'filename'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
comment|'# FIXME: image_type should be enum?'
nl|'\n'
string|"'image_type'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'block_migration'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disk_over_commit'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disk_available_mb'"
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
string|"'is_shared_instance_path'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'is_shared_block_storage'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'instance_relative_path'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'graphics_listen_addr_vnc'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'graphics_listen_addr_spice'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'serial_listen_addr'"
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
string|"'bdms'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'LibvirtLiveMigrateBDMInfo'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_bdms_to_legacy
name|'def'
name|'_bdms_to_legacy'
op|'('
name|'self'
op|','
name|'legacy'
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
string|"'bdms'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'legacy'
op|'['
string|"'volume'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'bdmi'
name|'in'
name|'self'
op|'.'
name|'bdms'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'volume'"
op|']'
op|'['
name|'bdmi'
op|'.'
name|'serial'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'disk_info'"
op|':'
name|'bdmi'
op|'.'
name|'as_disk_info'
op|'('
op|')'
op|','
nl|'\n'
string|"'connection_info'"
op|':'
name|'bdmi'
op|'.'
name|'connection_info'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_bdms_from_legacy
dedent|''
dedent|''
name|'def'
name|'_bdms_from_legacy'
op|'('
name|'self'
op|','
name|'legacy_pre_result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdms'
op|'='
op|'['
op|']'
newline|'\n'
name|'volume'
op|'='
name|'legacy_pre_result'
op|'.'
name|'get'
op|'('
string|"'volume'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'serial'
name|'in'
name|'volume'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'volume'
op|'['
name|'serial'
op|']'
newline|'\n'
name|'bdmi'
op|'='
name|'objects'
op|'.'
name|'LibvirtLiveMigrateBDMInfo'
op|'('
name|'serial'
op|'='
name|'serial'
op|')'
newline|'\n'
name|'bdmi'
op|'.'
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'bdmi'
op|'.'
name|'bus'
op|'='
name|'vol'
op|'['
string|"'disk_info'"
op|']'
op|'['
string|"'bus'"
op|']'
newline|'\n'
name|'bdmi'
op|'.'
name|'dev'
op|'='
name|'vol'
op|'['
string|"'disk_info'"
op|']'
op|'['
string|"'dev'"
op|']'
newline|'\n'
name|'bdmi'
op|'.'
name|'type'
op|'='
name|'vol'
op|'['
string|"'disk_info'"
op|']'
op|'['
string|"'type'"
op|']'
newline|'\n'
name|'if'
string|"'format'"
name|'in'
name|'vol'
op|':'
newline|'\n'
indent|'                '
name|'bdmi'
op|'.'
name|'format'
op|'='
name|'vol'
op|'['
string|"'disk_info'"
op|']'
op|'['
string|"'format'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'boot_index'"
name|'in'
name|'vol'
op|':'
newline|'\n'
indent|'                '
name|'bdmi'
op|'.'
name|'boot_index'
op|'='
name|'int'
op|'('
name|'vol'
op|'['
string|"'disk_info'"
op|']'
op|'['
string|"'boot_index'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'bdms'
op|'.'
name|'append'
op|'('
name|'bdmi'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_legacy_dict
dedent|''
dedent|''
name|'def'
name|'to_legacy_dict'
op|'('
name|'self'
op|','
name|'pre_migration_result'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Converting to legacy: %s'"
op|'%'
name|'self'
op|')'
newline|'\n'
name|'legacy'
op|'='
name|'super'
op|'('
name|'LibvirtLiveMigrateData'
op|','
name|'self'
op|')'
op|'.'
name|'to_legacy_dict'
op|'('
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
name|'set'
op|'('
name|'self'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'-'
nl|'\n'
name|'set'
op|'('
name|'LiveMigrateData'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'-'
op|'{'
string|"'bdms'"
op|'}'
op|')'
newline|'\n'
name|'legacy'
op|'.'
name|'update'
op|'('
op|'{'
name|'k'
op|':'
name|'getattr'
op|'('
name|'self'
op|','
name|'k'
op|')'
name|'for'
name|'k'
name|'in'
name|'keys'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'k'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'graphics_vnc'
op|'='
name|'legacy'
op|'.'
name|'pop'
op|'('
string|"'graphics_listen_addr_vnc'"
op|','
name|'None'
op|')'
newline|'\n'
name|'graphics_spice'
op|'='
name|'legacy'
op|'.'
name|'pop'
op|'('
string|"'graphics_listen_addr_spice'"
op|','
name|'None'
op|')'
newline|'\n'
name|'live_result'
op|'='
op|'{'
nl|'\n'
string|"'graphics_listen_addrs'"
op|':'
op|'{'
nl|'\n'
string|"'vnc'"
op|':'
name|'graphics_vnc'
name|'and'
name|'str'
op|'('
name|'graphics_vnc'
op|')'
op|','
nl|'\n'
string|"'spice'"
op|':'
name|'graphics_spice'
name|'and'
name|'str'
op|'('
name|'graphics_spice'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'serial_listen_addr'"
op|':'
name|'legacy'
op|'.'
name|'pop'
op|'('
string|"'serial_listen_addr'"
op|','
name|'None'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'pre_migration_result'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
op|'='
name|'live_result'
newline|'\n'
name|'self'
op|'.'
name|'_bdms_to_legacy'
op|'('
name|'live_result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Legacy result: %s'"
op|'%'
name|'legacy'
op|')'
newline|'\n'
name|'return'
name|'legacy'
newline|'\n'
nl|'\n'
DECL|member|from_legacy_dict
dedent|''
name|'def'
name|'from_legacy_dict'
op|'('
name|'self'
op|','
name|'legacy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Converting legacy dict to obj: %s'"
op|'%'
name|'legacy'
op|')'
newline|'\n'
name|'super'
op|'('
name|'LibvirtLiveMigrateData'
op|','
name|'self'
op|')'
op|'.'
name|'from_legacy_dict'
op|'('
name|'legacy'
op|')'
newline|'\n'
name|'keys'
op|'='
name|'set'
op|'('
name|'self'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'-'
name|'set'
op|'('
name|'LiveMigrateData'
op|'.'
name|'fields'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'keys'
op|'-'
op|'{'
string|"'bdms'"
op|'}'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'legacy'
op|'['
name|'k'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
string|"'pre_live_migration_result'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'pre_result'
op|'='
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'graphics_listen_addr_vnc'
op|'='
name|'pre_result'
op|'['
string|"'graphics_listen_addrs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'vnc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'graphics_listen_addr_spice'
op|'='
name|'pre_result'
op|'['
string|"'graphics_listen_addrs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'spice'"
op|')'
newline|'\n'
name|'if'
string|"'serial_listen_addr'"
name|'in'
name|'pre_result'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'serial_listen_addr'
op|'='
name|'pre_result'
op|'['
string|"'serial_listen_addr'"
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_bdms_from_legacy'
op|'('
name|'pre_result'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Converted object: %s'"
op|'%'
name|'self'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'obj_base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|XenapiLiveMigrateData
name|'class'
name|'XenapiLiveMigrateData'
op|'('
name|'LiveMigrateData'
op|')'
op|':'
newline|'\n'
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
string|"'block_migration'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'destination_sr_ref'"
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
string|"'migrate_send_data'"
op|':'
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'sr_uuid_map'"
op|':'
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'kernel_file'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'ramdisk_file'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|to_legacy_dict
name|'def'
name|'to_legacy_dict'
op|'('
name|'self'
op|','
name|'pre_migration_result'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'legacy'
op|'='
name|'super'
op|'('
name|'XenapiLiveMigrateData'
op|','
name|'self'
op|')'
op|'.'
name|'to_legacy_dict'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'block_migration'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'block_migration'"
op|']'
op|'='
name|'self'
op|'.'
name|'block_migration'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'migrate_send_data'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'migrate_data'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'migrate_send_data'"
op|':'
name|'self'
op|'.'
name|'migrate_send_data'
op|','
nl|'\n'
string|"'destination_sr_ref'"
op|':'
name|'self'
op|'.'
name|'destination_sr_ref'
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'live_result'
op|'='
op|'{'
nl|'\n'
string|"'sr_uuid_map'"
op|':'
op|'('
string|"'sr_uuid_map'"
name|'in'
name|'self'
name|'and'
name|'self'
op|'.'
name|'sr_uuid_map'
nl|'\n'
name|'or'
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'pre_migration_result'
op|':'
newline|'\n'
indent|'            '
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
op|'='
name|'live_result'
newline|'\n'
dedent|''
name|'return'
name|'legacy'
newline|'\n'
nl|'\n'
DECL|member|from_legacy_dict
dedent|''
name|'def'
name|'from_legacy_dict'
op|'('
name|'self'
op|','
name|'legacy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'XenapiLiveMigrateData'
op|','
name|'self'
op|')'
op|'.'
name|'from_legacy_dict'
op|'('
name|'legacy'
op|')'
newline|'\n'
name|'if'
string|"'block_migration'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'block_migration'
op|'='
name|'legacy'
op|'['
string|"'block_migration'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'block_migration'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'if'
string|"'migrate_data'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'migrate_send_data'
op|'='
name|'legacy'
op|'['
string|"'migrate_data'"
op|']'
op|'['
string|"'migrate_send_data'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'destination_sr_ref'
op|'='
name|'legacy'
op|'['
string|"'migrate_data'"
op|']'
op|'['
string|"'destination_sr_ref'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'pre_live_migration_result'"
name|'in'
name|'legacy'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sr_uuid_map'
op|'='
name|'legacy'
op|'['
string|"'pre_live_migration_result'"
op|']'
op|'['
string|"'sr_uuid_map'"
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
