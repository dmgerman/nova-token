begin_unit
comment|'#    Copyright 2014 Red Hat Inc.'
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
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
name|'virt'
name|'import'
name|'hardware'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
name|'class'
name|'NUMACell'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|NUMACell
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added pinned_cpus and siblings fields'
nl|'\n'
comment|'# Version 1.2: Added mempages field'
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
string|"'cpuset'"
op|':'
name|'fields'
op|'.'
name|'SetOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
string|"'memory'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cpu_usage'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'default'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
string|"'memory_usage'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'default'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
string|"'pinned_cpus'"
op|':'
name|'fields'
op|'.'
name|'SetOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
string|"'siblings'"
op|':'
name|'fields'
op|'.'
name|'ListOfSetsOfIntegersField'
op|'('
op|')'
op|','
nl|'\n'
string|"'mempages'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'NUMAPagesTopology'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'NUMAPagesTopology'"
op|':'
op|'['
op|'('
string|"'1.2'"
op|','
string|"'1.0'"
op|')'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|free_cpus
name|'def'
name|'free_cpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'cpuset'
op|'-'
name|'self'
op|'.'
name|'pinned_cpus'
name|'or'
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|free_siblings
name|'def'
name|'free_siblings'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'sibling_set'
op|'&'
name|'self'
op|'.'
name|'free_cpus'
nl|'\n'
name|'for'
name|'sibling_set'
name|'in'
name|'self'
op|'.'
name|'siblings'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|avail_cpus
name|'def'
name|'avail_cpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'free_cpus'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|avail_memory
name|'def'
name|'avail_memory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'memory'
op|'-'
name|'self'
op|'.'
name|'memory_usage'
newline|'\n'
nl|'\n'
DECL|member|pin_cpus
dedent|''
name|'def'
name|'pin_cpus'
op|'('
name|'self'
op|','
name|'cpus'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'pinned_cpus'
op|'&'
name|'cpus'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|'('
name|'requested'
op|'='
name|'list'
op|'('
name|'cpus'
op|')'
op|','
nl|'\n'
name|'pinned'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'pinned_cpus'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'pinned_cpus'
op|'|='
name|'cpus'
newline|'\n'
nl|'\n'
DECL|member|unpin_cpus
dedent|''
name|'def'
name|'unpin_cpus'
op|'('
name|'self'
op|','
name|'cpus'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'self'
op|'.'
name|'pinned_cpus'
op|'&'
name|'cpus'
op|')'
op|'!='
name|'cpus'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CPUPinningInvalid'
op|'('
name|'requested'
op|'='
name|'list'
op|'('
name|'cpus'
op|')'
op|','
nl|'\n'
name|'pinned'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'pinned_cpus'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'pinned_cpus'
op|'-='
name|'cpus'
newline|'\n'
nl|'\n'
DECL|member|_to_dict
dedent|''
name|'def'
name|'_to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'hardware'
op|'.'
name|'format_cpu_spec'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'cpuset'
op|','
name|'allow_ranges'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'mem'"
op|':'
op|'{'
nl|'\n'
string|"'total'"
op|':'
name|'self'
op|'.'
name|'memory'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'self'
op|'.'
name|'memory_usage'
op|'}'
op|','
nl|'\n'
string|"'cpu_usage'"
op|':'
name|'self'
op|'.'
name|'cpu_usage'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_from_dict
name|'def'
name|'_from_dict'
op|'('
name|'cls'
op|','
name|'data_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cpuset'
op|'='
name|'hardware'
op|'.'
name|'parse_cpu_spec'
op|'('
nl|'\n'
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'cpus'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'cpu_usage'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'cpu_usage'"
op|','
number|'0'
op|')'
newline|'\n'
name|'memory'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'mem'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'total'"
op|','
number|'0'
op|')'
newline|'\n'
name|'memory_usage'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'mem'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'used'"
op|','
number|'0'
op|')'
newline|'\n'
name|'cell_id'
op|'='
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'id'
op|'='
name|'cell_id'
op|','
name|'cpuset'
op|'='
name|'cpuset'
op|','
name|'memory'
op|'='
name|'memory'
op|','
nl|'\n'
name|'cpu_usage'
op|'='
name|'cpu_usage'
op|','
name|'memory_usage'
op|'='
name|'memory_usage'
op|','
nl|'\n'
name|'mempages'
op|'='
op|'['
op|']'
op|','
name|'pinned_cpus'
op|'='
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'siblings'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|can_fit_hugepages
dedent|''
name|'def'
name|'can_fit_hugepages'
op|'('
name|'self'
op|','
name|'pagesize'
op|','
name|'memory'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns whether memory can fit into hugepages size\n\n        :param pagesize: a page size in KibB\n        :param memory: a memory size asked to fit in KiB\n\n        :returns: whether memory can fit in hugepages\n        :raises: MemoryPageSizeNotSupported if page size not supported\n        """'
newline|'\n'
name|'for'
name|'pages'
name|'in'
name|'self'
op|'.'
name|'mempages'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'pages'
op|'.'
name|'size_kb'
op|'=='
name|'pagesize'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'('
name|'memory'
op|'<='
name|'pages'
op|'.'
name|'free_kb'
name|'and'
nl|'\n'
op|'('
name|'memory'
op|'%'
name|'pages'
op|'.'
name|'size_kb'
op|')'
op|'=='
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'MemoryPageSizeNotSupported'
op|'('
name|'pagesize'
op|'='
name|'pagesize'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'NUMAPagesTopology'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|NUMAPagesTopology
name|'base'
op|'.'
name|'NovaObjectDictCompat'
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
string|"'size_kb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'total'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'default'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|free
name|'def'
name|'free'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the number of avail pages."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'total'
op|'-'
name|'self'
op|'.'
name|'used'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|free_kb
name|'def'
name|'free_kb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the avail memory size in KiB."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'free'
op|'*'
name|'self'
op|'.'
name|'size_kb'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'NUMATopology'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|NUMATopology
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Update NUMACell to 1.1'
nl|'\n'
comment|'# Version 1.2: Update NUMACell to 1.2'
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
string|"'cells'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'NUMACell'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'NUMACell'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|','
op|'('
string|"'1.1'"
op|','
string|"'1.1'"
op|')'
op|','
op|'('
string|"'1.2'"
op|','
string|"'1.2'"
op|')'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_primitive
name|'def'
name|'obj_from_primitive'
op|'('
name|'cls'
op|','
name|'primitive'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'nova_object.name'"
name|'in'
name|'primitive'
op|':'
newline|'\n'
indent|'            '
name|'obj_topology'
op|'='
name|'super'
op|'('
name|'NUMATopology'
op|','
name|'cls'
op|')'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'primitive'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(sahid): This compatibility code needs to stay until we can'
nl|'\n'
comment|'# guarantee that there are no cases of the old format stored in'
nl|'\n'
comment|'# the database (or forever, if we can never guarantee that).'
nl|'\n'
indent|'            '
name|'obj_topology'
op|'='
name|'NUMATopology'
op|'.'
name|'_from_dict'
op|'('
name|'primitive'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'obj_topology'
newline|'\n'
nl|'\n'
DECL|member|_to_json
dedent|''
name|'def'
name|'_to_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'self'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_from_db_obj
name|'def'
name|'obj_from_db_obj'
op|'('
name|'cls'
op|','
name|'db_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'obj_from_primitive'
op|'('
nl|'\n'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'db_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Defined so that boolean testing works the same as for lists."""'
newline|'\n'
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_dict
dedent|''
name|'def'
name|'_to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(sahid): needs to be removed.'
nl|'\n'
indent|'        '
name|'return'
op|'{'
string|"'cells'"
op|':'
op|'['
name|'cell'
op|'.'
name|'_to_dict'
op|'('
op|')'
name|'for'
name|'cell'
name|'in'
name|'self'
op|'.'
name|'cells'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_from_dict
name|'def'
name|'_from_dict'
op|'('
name|'cls'
op|','
name|'data_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
name|'cells'
op|'='
op|'['
nl|'\n'
name|'NUMACell'
op|'.'
name|'_from_dict'
op|'('
name|'cell_dict'
op|')'
nl|'\n'
name|'for'
name|'cell_dict'
name|'in'
name|'data_dict'
op|'.'
name|'get'
op|'('
string|"'cells'"
op|','
op|'['
op|']'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
