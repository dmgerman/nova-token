begin_unit
comment|'# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.'
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
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
name|'class'
name|'HVSpec'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|HVSpec
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
string|"'arch'"
op|':'
name|'fields'
op|'.'
name|'ArchitectureField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hv_type'"
op|':'
name|'fields'
op|'.'
name|'HVTypeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vm_mode'"
op|':'
name|'fields'
op|'.'
name|'VMModeField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(pmurray): for backward compatibility, the supported instance'
nl|'\n'
comment|'# data is stored in the database as a list.'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_list
name|'def'
name|'from_list'
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
name|'arch'
op|'='
name|'data'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'hv_type'
op|'='
name|'data'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'vm_mode'
op|'='
name|'data'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_list
dedent|''
name|'def'
name|'to_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'arch'
op|','
name|'self'
op|'.'
name|'hv_type'
op|','
name|'self'
op|'.'
name|'vm_mode'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
