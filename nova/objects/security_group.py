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
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroup
name|'class'
name|'SecurityGroup'
op|'('
name|'base'
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
string|"'id'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'str'
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
name|'secgroup'
op|','
name|'db_secgroup'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): These are identical right now'
nl|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'secgroup'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'secgroup'
op|'['
name|'field'
op|']'
op|'='
name|'db_secgroup'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'secgroup'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'secgroup'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'secgroup_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'context'
op|','
name|'secgroup_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'cls'
op|'('
op|')'
op|','
name|'db_secgroup'
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
name|'project_id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'context'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'group_name'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'cls'
op|'('
op|')'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|in_use
name|'def'
name|'in_use'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'security_group_in_use'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
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
name|'if'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'db_secgroup'
op|'='
name|'db'
op|'.'
name|'security_group_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
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
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|','
nl|'\n'
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_secgroup_list
dedent|''
dedent|''
name|'def'
name|'_make_secgroup_list'
op|'('
name|'context'
op|','
name|'secgroup_list'
op|','
name|'db_secgroup_list'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'secgroup_list'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'db_secgroup'
name|'in'
name|'db_secgroup_list'
op|':'
newline|'\n'
indent|'        '
name|'secgroup'
op|'='
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
name|'SecurityGroup'
op|'('
op|')'
op|','
name|'db_secgroup'
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'secgroup_list'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'secgroup'
op|')'
newline|'\n'
dedent|''
name|'secgroup_list'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'secgroup_list'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupList
dedent|''
name|'class'
name|'SecurityGroupList'
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
name|'return'
name|'_make_secgroup_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
nl|'\n'
name|'db'
op|'.'
name|'security_group_get_all'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_project
name|'def'
name|'get_by_project'
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
name|'return'
name|'_make_secgroup_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
nl|'\n'
name|'db'
op|'.'
name|'security_group_get_by_project'
op|'('
nl|'\n'
name|'context'
op|','
name|'project_id'
op|')'
op|')'
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
name|'return'
name|'_make_secgroup_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
nl|'\n'
name|'db'
op|'.'
name|'security_group_get_by_instance'
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
nl|'\n'
nl|'\n'
DECL|function|make_secgroup_list
dedent|''
dedent|''
name|'def'
name|'make_secgroup_list'
op|'('
name|'security_groups'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A helper to make security group objects from a list of names.\n\n    Note that this does not make them save-able or have the rest of the\n    attributes they would normally have, but provides a quick way to fill,\n    for example, an instance object during create.\n    """'
newline|'\n'
name|'secgroups'
op|'='
name|'SecurityGroupList'
op|'('
op|')'
newline|'\n'
name|'secgroups'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'        '
name|'secgroup'
op|'='
name|'SecurityGroup'
op|'('
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'secgroups'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'secgroup'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'secgroups'
newline|'\n'
dedent|''
endmarker|''
end_unit
