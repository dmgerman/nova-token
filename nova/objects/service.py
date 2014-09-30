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
name|'availability_zones'
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
name|'import'
name|'utils'
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
DECL|class|Service
name|'class'
name|'Service'
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
comment|'# Version 1.1: Added compute_node nested object'
nl|'\n'
comment|'# Version 1.2: String attributes updated to support unicode'
nl|'\n'
comment|'# Version 1.3: ComputeNode version 1.5'
nl|'\n'
comment|'# Version 1.4: Added use_slave to get_by_compute_host'
nl|'\n'
comment|'# Version 1.5: ComputeNode version 1.6'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.5'"
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
string|"'host'"
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
string|"'binary'"
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
string|"'topic'"
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
string|"'report_count'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
op|','
nl|'\n'
string|"'disabled_reason'"
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
string|"'availability_zone'"
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
string|"'compute_node'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ComputeNode'"
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
number|'3'
op|')'
name|'and'
string|"'compute_node'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_node'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'compute_node'"
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.4'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'compute_node'"
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.4'"
newline|'\n'
dedent|''
name|'elif'
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'5'
op|')'
name|'and'
string|"'compute_node'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_node'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'primitive'
op|'['
string|"'compute_node'"
op|']'
op|'['
string|"'nova_object.data'"
op|']'
op|','
string|"'1.5'"
op|')'
newline|'\n'
name|'primitive'
op|'['
string|"'compute_node'"
op|']'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'1.5'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_do_compute_node
name|'def'
name|'_do_compute_node'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'db_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(danms): The service.compute_node relationship returns'
nl|'\n'
comment|"# a list, which should only have one item in it. If it's empty"
nl|'\n'
comment|'# or otherwise malformed, ignore it.'
nl|'\n'
indent|'            '
name|'db_compute'
op|'='
name|'db_service'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'service'
op|'.'
name|'compute_node'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'context'
op|','
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
op|')'
op|','
name|'db_compute'
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
name|'service'
op|','
name|'db_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'allow_missing'
op|'='
op|'('
string|"'availability_zone'"
op|','
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'service'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'allow_missing'
name|'and'
name|'key'
name|'not'
name|'in'
name|'db_service'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'=='
string|"'compute_node'"
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'.'
name|'_do_compute_node'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'db_service'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'['
name|'key'
op|']'
op|'='
name|'db_service'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'service'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'service'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'service'
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
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Lazy-loading `%(attr)s\' on %(name)s id %(id)s"'
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
string|"'id'"
op|':'
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'attrname'
op|'!='
string|"'compute_node'"
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
name|'self'
op|'.'
name|'compute_node'
op|'='
name|'objects'
op|'.'
name|'ComputeNode'
op|'.'
name|'get_by_service_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
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
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
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
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_topic
name|'def'
name|'get_by_host_and_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_host_and_topic'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'topic'
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
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_compute_host
name|'def'
name|'get_by_compute_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
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
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_args
name|'def'
name|'get_by_args'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
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
name|'db_service'
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
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'updates'
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
name|'db_service'
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
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
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
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_update'
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
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_service'
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
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceList
dedent|''
dedent|''
name|'class'
name|'ServiceList'
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
comment|'#              Service <= version 1.2'
nl|'\n'
comment|'# Version 1.1  Service version 1.3'
nl|'\n'
comment|'# Version 1.2: Service version 1.4'
nl|'\n'
comment|'# Version 1.3: Service version 1.5'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.3'"
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
string|"'Service'"
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
string|"'1.2'"
op|','
nl|'\n'
comment|'# NOTE(danms): Service was at 1.2 before we added this'
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.3'"
op|','
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.4'"
op|','
nl|'\n'
string|"'1.3'"
op|':'
string|"'1.5'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_topic
name|'def'
name|'get_by_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
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
name|'Service'
op|','
nl|'\n'
name|'db_services'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
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
name|'Service'
op|','
nl|'\n'
name|'db_services'
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
op|','
name|'disabled'
op|'='
name|'None'
op|','
name|'set_zones'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'disabled'
op|')'
newline|'\n'
name|'if'
name|'set_zones'
op|':'
newline|'\n'
indent|'            '
name|'db_services'
op|'='
name|'availability_zones'
op|'.'
name|'set_availability_zones'
op|'('
nl|'\n'
name|'context'
op|','
name|'db_services'
op|')'
newline|'\n'
dedent|''
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
name|'Service'
op|','
nl|'\n'
name|'db_services'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
