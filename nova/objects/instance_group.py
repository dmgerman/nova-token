begin_unit
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
name|'class'
name|'InstanceGroup'
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
DECL|class|InstanceGroup
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.2: Use list/dict helpers for policies, metadetails, members'
nl|'\n'
comment|'# Version 1.3: Make uuid a non-None real string'
nl|'\n'
comment|'# Version 1.4: Add add_members()'
nl|'\n'
comment|'# Version 1.5: Add get_hosts()'
nl|'\n'
comment|'# Version 1.6: Add get_by_name()'
nl|'\n'
comment|'# Version 1.7: Deprecate metadetails'
nl|'\n'
comment|'# Version 1.8: Add count_members_by_user()'
nl|'\n'
comment|'# Version 1.9: Add get_by_instance_uuid()'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.9'"
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
nl|'\n'
string|"'user_id'"
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
string|"'project_id'"
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
string|"'name'"
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
nl|'\n'
string|"'policies'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'members'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
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
DECL|member|obj_make_compatible
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'7'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Before 1.7, we had an always-empty'
nl|'\n'
comment|'# metadetails property'
nl|'\n'
indent|'            '
name|'primitive'
op|'['
string|"'metadetails'"
op|']'
op|'='
op|'{'
op|'}'
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
name|'instance_group'
op|','
name|'db_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Method to help with migration to objects.\n\n        Converts a database entity to a formal object.\n        """'
newline|'\n'
comment|'# Most of the field names match right now, so be quick'
nl|'\n'
name|'for'
name|'field'
name|'in'
name|'instance_group'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
op|'=='
string|"'deleted'"
op|':'
newline|'\n'
indent|'                '
name|'instance_group'
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
name|'instance_group'
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
name|'instance_group'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'instance_group'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance_group'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'context'
op|','
name|'uuid'
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
name|'db_inst'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_name
name|'def'
name|'get_by_name'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
comment|"# TODO(russellb) We need to get the group by name here.  There's no"
nl|'\n'
comment|'# db.api method for this yet.  Come back and optimize this by'
nl|'\n'
comment|'# adding a new query by name.  This is unnecessarily expensive if a'
nl|'\n'
comment|'# tenant has lots of groups.'
nl|'\n'
indent|'        '
name|'igs'
op|'='
name|'objects'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_by_project_id'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'for'
name|'ig'
name|'in'
name|'igs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ig'
op|'.'
name|'name'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ig'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
op|'('
name|'group_uuid'
op|'='
name|'name'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_group_get_by_instance'
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
name|'db_inst'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_hint
name|'def'
name|'get_by_hint'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'hint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'hint'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'hint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'get_by_name'
op|'('
name|'context'
op|','
name|'hint'
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
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Save updates to this instance group."""'
newline|'\n'
nl|'\n'
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'dict'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'payload'
op|'['
string|"'server_group_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_group_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'updates'
op|')'
newline|'\n'
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'context'
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
name|'context'
op|','
name|'self'
op|','
name|'db_inst'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_server_group_update'
op|'('
name|'context'
op|','
nl|'\n'
string|'"update"'
op|','
name|'payload'
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
string|'"""Refreshes the instance group."""'
newline|'\n'
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
name|'self'
op|'.'
name|'uuid'
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
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'field'
op|')'
name|'and'
name|'self'
op|'['
name|'field'
op|']'
op|'!='
name|'current'
op|'['
name|'field'
op|']'
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
op|','
name|'context'
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
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'policies'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'policies'"
op|','
name|'None'
op|')'
newline|'\n'
name|'members'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'members'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'db_inst'
op|'='
name|'db'
op|'.'
name|'instance_group_create'
op|'('
name|'context'
op|','
name|'updates'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_inst'
op|')'
newline|'\n'
name|'payload'
op|'['
string|"'server_group_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'uuid'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_server_group_update'
op|'('
name|'context'
op|','
nl|'\n'
string|'"create"'
op|','
name|'payload'
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
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'='
op|'{'
string|"'server_group_id'"
op|':'
name|'self'
op|'.'
name|'uuid'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_group_delete'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_server_group_update'
op|'('
name|'context'
op|','
nl|'\n'
string|'"delete"'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|add_members
name|'def'
name|'add_members'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'group_uuid'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'='
op|'{'
string|"'server_group_id'"
op|':'
name|'group_uuid'
op|','
nl|'\n'
string|"'instance_uuids'"
op|':'
name|'instance_uuids'
op|'}'
newline|'\n'
name|'members'
op|'='
name|'db'
op|'.'
name|'instance_group_members_add'
op|'('
name|'context'
op|','
name|'group_uuid'
op|','
nl|'\n'
name|'instance_uuids'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_server_group_update'
op|'('
name|'context'
op|','
nl|'\n'
string|'"addmember"'
op|','
name|'payload'
op|')'
newline|'\n'
name|'return'
name|'list'
op|'('
name|'members'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|get_hosts
name|'def'
name|'get_hosts'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'exclude'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of hosts for non-deleted instances in the group\n\n        This method allows you to get a list of the hosts where instances in\n        this group are currently running.  There\'s also an option to exclude\n        certain instance UUIDs from this calculation.\n\n        """'
newline|'\n'
name|'filter_uuids'
op|'='
name|'self'
op|'.'
name|'members'
newline|'\n'
name|'if'
name|'exclude'
op|':'
newline|'\n'
indent|'            '
name|'filter_uuids'
op|'='
name|'set'
op|'('
name|'filter_uuids'
op|')'
op|'-'
name|'set'
op|'('
name|'exclude'
op|')'
newline|'\n'
dedent|''
name|'filters'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'filter_uuids'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'instances'
op|'='
name|'objects'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_filters'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'return'
name|'list'
op|'('
name|'set'
op|'('
op|'['
name|'instance'
op|'.'
name|'host'
name|'for'
name|'instance'
name|'in'
name|'instances'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'host'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|count_members_by_user
name|'def'
name|'count_members_by_user'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Count the number of instances in a group belonging to a user."""'
newline|'\n'
name|'filter_uuids'
op|'='
name|'self'
op|'.'
name|'members'
newline|'\n'
name|'filters'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'filter_uuids'
op|','
string|"'user_id'"
op|':'
name|'user_id'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'instances'
op|'='
name|'objects'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_filters'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'return'
name|'len'
op|'('
name|'instances'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceGroupList
dedent|''
dedent|''
name|'class'
name|'InstanceGroupList'
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
comment|'#              InstanceGroup <= version 1.3'
nl|'\n'
comment|'# Version 1.1: InstanceGroup <= version 1.4'
nl|'\n'
comment|'# Version 1.2: InstanceGroup <= version 1.5'
nl|'\n'
comment|'# Version 1.3: InstanceGroup <= version 1.6'
nl|'\n'
comment|'# Version 1.4: InstanceGroup <= version 1.7'
nl|'\n'
comment|'# Version 1.5: InstanceGroup <= version 1.8'
nl|'\n'
comment|'# Version 1.6: InstanceGroup <= version 1.9'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.6'"
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
string|"'InstanceGroup'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
comment|'# NOTE(danms): InstanceGroup was at 1.3 before we added this'
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.4'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'1.3'"
op|':'
string|"'1.6'"
op|','
nl|'\n'
string|"'1.4'"
op|':'
string|"'1.7'"
op|','
nl|'\n'
string|"'1.5'"
op|':'
string|"'1.8'"
op|','
nl|'\n'
string|"'1.6'"
op|':'
string|"'1.9'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_project_id
name|'def'
name|'get_by_project_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all_by_project_id'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
nl|'\n'
name|'groups'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'InstanceGroup'
op|','
nl|'\n'
name|'groups'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
