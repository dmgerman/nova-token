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
name|'import'
name|'traceback'
newline|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceAction
name|'class'
name|'InstanceAction'
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
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
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
string|"'action'"
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
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'request_id'"
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
string|"'start_time'"
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
string|"'finish_time'"
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
string|"'message'"
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
name|'action'
op|','
name|'db_action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'action'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'['
name|'field'
op|']'
op|'='
name|'db_action'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'action'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'action'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'action'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|pack_action_start
name|'def'
name|'pack_action_start'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'action_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'request_id'"
op|':'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'action'"
op|':'
name|'action_name'
op|','
nl|'\n'
string|"'start_time'"
op|':'
name|'context'
op|'.'
name|'timestamp'
op|'}'
newline|'\n'
name|'return'
name|'values'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|pack_action_finish
name|'def'
name|'pack_action_finish'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'request_id'"
op|':'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'finish_time'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'}'
newline|'\n'
name|'return'
name|'values'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_request_id
name|'def'
name|'get_by_request_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_action'
op|'='
name|'db'
op|'.'
name|'action_get_by_request_id'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'request_id'
op|')'
newline|'\n'
name|'if'
name|'db_action'
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
name|'db_action'
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
DECL|member|action_start
name|'def'
name|'action_start'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'action_name'
op|','
nl|'\n'
name|'want_result'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'cls'
op|'.'
name|'pack_action_start'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'action_name'
op|')'
newline|'\n'
name|'db_action'
op|'='
name|'db'
op|'.'
name|'action_start'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'if'
name|'want_result'
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
name|'db_action'
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
DECL|member|action_finish
name|'def'
name|'action_finish'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'want_result'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'cls'
op|'.'
name|'pack_action_finish'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'db_action'
op|'='
name|'db'
op|'.'
name|'action_finish'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'if'
name|'want_result'
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
name|'db_action'
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
DECL|member|finish
name|'def'
name|'finish'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'pack_action_finish'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'db_action'
op|'='
name|'db'
op|'.'
name|'action_finish'
op|'('
name|'context'
op|','
name|'values'
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
name|'db_action'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionList
dedent|''
dedent|''
name|'class'
name|'InstanceActionList'
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
comment|'#              InstanceAction <= version 1.1'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
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
string|"'InstanceAction'"
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
string|"'1.1'"
op|','
nl|'\n'
comment|'# NOTE(danms): InstanceAction was at 1.1 before we added this'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
name|'db_actions'
op|'='
name|'db'
op|'.'
name|'actions_get'
op|'('
name|'context'
op|','
name|'instance_uuid'
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
op|')'
op|','
name|'InstanceAction'
op|','
name|'db_actions'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionEvent
dedent|''
dedent|''
name|'class'
name|'InstanceActionEvent'
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
DECL|variable|fields
indent|'    '
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
string|"'event'"
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
string|"'action_id'"
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
string|"'start_time'"
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
string|"'finish_time'"
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
string|"'result'"
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
string|"'traceback'"
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
name|'event'
op|','
name|'db_event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'event'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'['
name|'field'
op|']'
op|'='
name|'db_event'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'event'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'event'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'event'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|pack_action_event_start
name|'def'
name|'pack_action_event_start'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'event_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'event'"
op|':'
name|'event_name'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'start_time'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'}'
newline|'\n'
name|'return'
name|'values'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|pack_action_event_finish
name|'def'
name|'pack_action_event_finish'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'event_name'
op|','
nl|'\n'
name|'exc_val'
op|'='
name|'None'
op|','
name|'exc_tb'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'event'"
op|':'
name|'event_name'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'request_id'"
op|':'
name|'context'
op|'.'
name|'request_id'
op|','
nl|'\n'
string|"'finish_time'"
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'}'
newline|'\n'
name|'if'
name|'exc_tb'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'result'"
op|']'
op|'='
string|"'Success'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'result'"
op|']'
op|'='
string|"'Error'"
newline|'\n'
name|'values'
op|'['
string|"'message'"
op|']'
op|'='
name|'str'
op|'('
name|'exc_val'
op|')'
newline|'\n'
name|'values'
op|'['
string|"'traceback'"
op|']'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'traceback'
op|'.'
name|'format_tb'
op|'('
name|'exc_tb'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'values'
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
name|'action_id'
op|','
name|'event_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_event'
op|'='
name|'db'
op|'.'
name|'action_event_get_by_id'
op|'('
name|'context'
op|','
name|'action_id'
op|','
name|'event_id'
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
name|'db_event'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|event_start
name|'def'
name|'event_start'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'event_name'
op|','
name|'want_result'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'cls'
op|'.'
name|'pack_action_event_start'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'event_name'
op|')'
newline|'\n'
name|'db_event'
op|'='
name|'db'
op|'.'
name|'action_event_start'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'if'
name|'want_result'
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
name|'db_event'
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
DECL|member|event_finish_with_failure
name|'def'
name|'event_finish_with_failure'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'event_name'
op|','
nl|'\n'
name|'exc_val'
op|'='
name|'None'
op|','
name|'exc_tb'
op|'='
name|'None'
op|','
name|'want_result'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'cls'
op|'.'
name|'pack_action_event_finish'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'event_name'
op|','
name|'exc_val'
op|'='
name|'exc_val'
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'exc_tb'
op|')'
newline|'\n'
name|'db_event'
op|'='
name|'db'
op|'.'
name|'action_event_finish'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'if'
name|'want_result'
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
name|'db_event'
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
DECL|member|event_finish
name|'def'
name|'event_finish'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'event_name'
op|','
nl|'\n'
name|'want_result'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'event_finish_with_failure'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'event_name'
op|','
name|'exc_val'
op|'='
name|'None'
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_result'
op|'='
name|'want_result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|finish_with_failure
name|'def'
name|'finish_with_failure'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'exc_val'
op|','
name|'exc_tb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'pack_action_event_finish'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'event'
op|','
name|'exc_val'
op|'='
name|'exc_val'
op|','
nl|'\n'
name|'exc_tb'
op|'='
name|'exc_tb'
op|')'
newline|'\n'
name|'db_event'
op|'='
name|'db'
op|'.'
name|'action_event_finish'
op|'('
name|'context'
op|','
name|'values'
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
name|'db_event'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|finish
name|'def'
name|'finish'
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
name|'finish_with_failure'
op|'('
name|'context'
op|','
name|'exc_val'
op|'='
name|'None'
op|','
name|'exc_tb'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceActionEventList
dedent|''
dedent|''
name|'class'
name|'InstanceActionEventList'
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
DECL|variable|fields
indent|'    '
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
string|"'InstanceActionEvent'"
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
string|"'1.0'"
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
DECL|member|get_by_action
name|'def'
name|'get_by_action'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'action_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_events'
op|'='
name|'db'
op|'.'
name|'action_events_get'
op|'('
name|'context'
op|','
name|'action_id'
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
op|')'
op|','
name|'InstanceActionEvent'
op|','
nl|'\n'
name|'db_events'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
