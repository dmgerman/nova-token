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
DECL|class|VirtCPUTopology
name|'class'
name|'VirtCPUTopology'
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
string|"'sockets'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'cores'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'threads'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(jaypipes): for backward compatibility, the virt CPU topology'
nl|'\n'
comment|'# data is stored in the database as a nested dict.'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
name|'sockets'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'sockets'"
op|')'
op|','
nl|'\n'
name|'cores'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'cores'"
op|')'
op|','
nl|'\n'
name|'threads'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'threads'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'sockets'"
op|':'
name|'self'
op|'.'
name|'sockets'
op|','
nl|'\n'
string|"'cores'"
op|':'
name|'self'
op|'.'
name|'cores'
op|','
nl|'\n'
string|"'threads'"
op|':'
name|'self'
op|'.'
name|'threads'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
