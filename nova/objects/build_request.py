begin_unit
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_versionedobjects'
name|'import'
name|'exception'
name|'as'
name|'ovoo_exc'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'orm'
name|'import'
name|'joinedload'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api_models'
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
name|'_LE'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
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
DECL|variable|OBJECT_FIELDS
name|'OBJECT_FIELDS'
op|'='
op|'['
string|"'info_cache'"
op|','
string|"'security_groups'"
op|','
string|"'instance'"
op|']'
newline|'\n'
DECL|variable|JSON_FIELDS
name|'JSON_FIELDS'
op|'='
op|'['
string|"'instance_metadata'"
op|']'
newline|'\n'
DECL|variable|IP_FIELDS
name|'IP_FIELDS'
op|'='
op|'['
string|"'access_ip_v4'"
op|','
string|"'access_ip_v6'"
op|']'
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
DECL|class|BuildRequest
name|'class'
name|'BuildRequest'
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
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'display_name'"
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
string|"'instance_metadata'"
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
string|"'progress'"
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
string|"'vm_state'"
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
string|"'task_state'"
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
string|"'image_ref'"
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
string|"'access_ip_v4'"
op|':'
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'fields'
op|'.'
name|'IPV6AddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'info_cache'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'InstanceInfoCache'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'SecurityGroupList'"
op|')'
op|','
nl|'\n'
string|"'config_drive'"
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
string|"'key_name'"
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
string|"'locked_by'"
op|':'
name|'fields'
op|'.'
name|'EnumField'
op|'('
op|'['
string|"'owner'"
op|','
string|"'admin'"
op|']'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'request_spec'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'RequestSpec'"
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
op|')'
op|','
nl|'\n'
comment|'# NOTE(alaski): Normally these would come from the NovaPersistentObject'
nl|'\n'
comment|"# mixin but they're being set explicitly because we only need"
nl|'\n'
comment|'# created_at/updated_at. There is no soft delete for this object.'
nl|'\n'
comment|'# These fields should be carried over to the instance when it is'
nl|'\n'
comment|'# scheduled and created in a cell database.'
nl|'\n'
string|"'created_at'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
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
DECL|member|_load_request_spec
name|'def'
name|'_load_request_spec'
op|'('
name|'self'
op|','
name|'db_spec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request_spec'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
op|')'
op|','
name|'db_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_info_cache
dedent|''
name|'def'
name|'_load_info_cache'
op|'('
name|'self'
op|','
name|'db_info_cache'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'info_cache'
op|'='
name|'objects'
op|'.'
name|'InstanceInfoCache'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_info_cache'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_security_groups
dedent|''
name|'def'
name|'_load_security_groups'
op|'('
name|'self'
op|','
name|'db_sec_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'security_groups'
op|'='
name|'objects'
op|'.'
name|'SecurityGroupList'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_sec_group'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_load_instance
dedent|''
name|'def'
name|'_load_instance'
op|'('
name|'self'
op|','
name|'db_instance'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(alaski): Be very careful with instance loading because it'
nl|'\n'
comment|'# changes more than most objects.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_instance'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Failed to load instance from BuildRequest with uuid '"
nl|'\n'
string|"'%s because it is None'"
op|'%'
op|'('
name|'self'
op|'.'
name|'instance_uuid'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'BuildRequestNotFound'
op|'('
name|'uuid'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ovoo_exc'
op|'.'
name|'IncompatibleObjectVersion'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# This should only happen if proper service upgrade strategies are'
nl|'\n'
comment|'# not followed. Log the exception and raise BuildRequestNotFound.'
nl|'\n'
comment|"# If the instance can't be loaded this object is useless and may"
nl|'\n'
comment|'# as well not exist.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Could not deserialize instance store in BuildRequest '"
nl|'\n'
string|"'with uuid %(instance_uuid)s. Found version %(version)s '"
nl|'\n'
string|"'which is not supported here.'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'version'
op|'='
name|'exc'
op|'.'
name|'objver'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Could not deserialize instance in '"
nl|'\n'
string|"'BuildRequest'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'BuildRequestNotFound'
op|'('
name|'uuid'
op|'='
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'req'
op|','
name|'db_req'
op|')'
op|':'
newline|'\n'
comment|'# Set this up front so that it can be pulled for error messages or'
nl|'\n'
comment|'# logging at any point.'
nl|'\n'
indent|'        '
name|'req'
op|'.'
name|'instance_uuid'
op|'='
name|'db_req'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'req'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'req'
op|'.'
name|'fields'
op|'['
name|'key'
op|']'
op|','
name|'fields'
op|'.'
name|'ObjectField'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'getattr'
op|'('
name|'req'
op|','
string|"'_load_%s'"
op|'%'
name|'key'
op|')'
op|'('
name|'db_req'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'No load handler for %s'"
op|')'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'key'
name|'in'
name|'JSON_FIELDS'
name|'and'
name|'db_req'
op|'['
name|'key'
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'req'
op|','
name|'key'
op|','
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_req'
op|'['
name|'key'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'req'
op|','
name|'key'
op|','
name|'db_req'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'req'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'req'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'db'
op|'.'
name|'api_context_manager'
op|'.'
name|'reader'
newline|'\n'
DECL|member|_get_by_instance_uuid_from_db
name|'def'
name|'_get_by_instance_uuid_from_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_req'
op|'='
op|'('
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'BuildRequest'
op|')'
nl|'\n'
op|'.'
name|'options'
op|'('
name|'joinedload'
op|'('
string|"'request_spec'"
op|')'
op|')'
nl|'\n'
op|'.'
name|'filter_by'
op|'('
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_req'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'BuildRequestNotFound'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'db_req'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_req'
op|'='
name|'cls'
op|'.'
name|'_get_by_instance_uuid_from_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
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
name|'db_req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'db'
op|'.'
name|'api_context_manager'
op|'.'
name|'writer'
newline|'\n'
DECL|member|_create_in_db
name|'def'
name|'_create_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_req'
op|'='
name|'api_models'
op|'.'
name|'BuildRequest'
op|'('
op|')'
newline|'\n'
name|'db_req'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'db_req'
op|'.'
name|'save'
op|'('
name|'context'
op|'.'
name|'session'
op|')'
newline|'\n'
comment|'# NOTE: This is done because a later access will trigger a lazy load'
nl|'\n'
comment|"# outside of the db session so it will fail. We don't lazy load"
nl|'\n'
comment|'# request_spec on the object later because we never need a BuildRequest'
nl|'\n'
comment|'# without the RequestSpec.'
nl|'\n'
name|'db_req'
op|'.'
name|'request_spec'
newline|'\n'
name|'return'
name|'db_req'
newline|'\n'
nl|'\n'
DECL|member|_get_update_primitives
dedent|''
name|'def'
name|'_get_update_primitives'
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
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'OBJECT_FIELDS'
name|'and'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'value'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'key'
name|'in'
name|'JSON_FIELDS'
name|'and'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'key'
name|'in'
name|'IP_FIELDS'
name|'and'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
comment|'# These are stored as a string in the db and must be converted'
nl|'\n'
indent|'                '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'req_spec_obj'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'request_spec'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'req_spec_obj'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'request_spec_id'"
op|']'
op|'='
name|'req_spec_obj'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'return'
name|'updates'
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'instance_uuid'"
op|')'
op|':'
newline|'\n'
comment|"# We can't guarantee this is not null in the db so check here"
nl|'\n'
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
string|"'instance_uuid must be set'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'updates'
op|'='
name|'self'
op|'.'
name|'_get_update_primitives'
op|'('
op|')'
newline|'\n'
name|'db_req'
op|'='
name|'self'
op|'.'
name|'_create_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
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
name|'db_req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
op|'@'
name|'db'
op|'.'
name|'api_context_manager'
op|'.'
name|'writer'
newline|'\n'
DECL|member|_destroy_in_db
name|'def'
name|'_destroy_in_db'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'.'
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'BuildRequest'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'id'
op|'='
name|'id'
op|')'
op|'.'
name|'delete'
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
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_destroy_in_db'
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
dedent|''
dedent|''
endmarker|''
end_unit
