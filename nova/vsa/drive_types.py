begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
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
string|'"""\nHandles all requests relating to Virtual Storage Arrays (VSAs).\n"""'
newline|'\n'
nl|'\n'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'drive_type_template_short'"
op|','
string|"'%s_%sGB_%sRPM'"
op|','
nl|'\n'
string|"'Template string for generation of drive type name'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'drive_type_template_long'"
op|','
string|"'%s_%sGB_%sRPM_%s'"
op|','
nl|'\n'
string|"'Template string for generation of drive type name'"
op|')'
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
string|"'nova.drive_types'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_generate_default_drive_name
name|'def'
name|'_generate_default_drive_name'
op|'('
name|'type'
op|','
name|'size_gb'
op|','
name|'rpm'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'capabilities'
name|'is'
name|'None'
name|'or'
name|'capabilities'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'drive_type_template_short'
op|'%'
op|'('
name|'type'
op|','
name|'str'
op|'('
name|'size_gb'
op|')'
op|','
name|'rpm'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'drive_type_template_long'
op|'%'
op|'('
name|'type'
op|','
name|'str'
op|'('
name|'size_gb'
op|')'
op|','
name|'rpm'
op|','
name|'capabilities'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_create
dedent|''
dedent|''
name|'def'
name|'drive_type_create'
op|'('
name|'context'
op|','
name|'type'
op|','
name|'size_gb'
op|','
name|'rpm'
op|','
nl|'\n'
name|'capabilities'
op|'='
string|"''"
op|','
name|'visible'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
name|'_generate_default_drive_name'
op|'('
name|'type'
op|','
name|'size_gb'
op|','
name|'rpm'
op|','
nl|'\n'
name|'capabilities'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Creating drive type %(name)s: "'
string|'"%(type)s %(size_gb)s %(rpm)s %(capabilities)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'values'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
name|'type'
op|','
nl|'\n'
string|"'size_gb'"
op|':'
name|'size_gb'
op|','
nl|'\n'
string|"'rpm'"
op|':'
name|'rpm'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'capabilities'
op|','
nl|'\n'
string|"'visible'"
op|':'
name|'visible'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'drive_type_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_update
dedent|''
name|'def'
name|'drive_type_update'
op|'('
name|'context'
op|','
name|'name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Updating drive type %(name)s: "'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'drive_type_update'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_rename
dedent|''
name|'def'
name|'drive_type_rename'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'new_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'if'
name|'new_name'
name|'is'
name|'None'
name|'or'
name|'new_name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'        '
name|'disk'
op|'='
name|'db'
op|'.'
name|'drive_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
name|'new_name'
op|'='
name|'_generate_default_drive_name'
op|'('
name|'disk'
op|'['
string|"'type'"
op|']'
op|','
nl|'\n'
name|'disk'
op|'['
string|"'size_gb'"
op|']'
op|','
name|'disk'
op|'['
string|"'rpm'"
op|']'
op|','
name|'disk'
op|'['
string|"'capabilities'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Renaming drive type %(name)s to %(new_name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'values'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
name|'new_name'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'drive_type_update'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_delete
dedent|''
name|'def'
name|'drive_type_delete'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Deleting drive type %(name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'drive_type_destroy'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_get
dedent|''
name|'def'
name|'drive_type_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'drive_type_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_get_by_name
dedent|''
name|'def'
name|'drive_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'drive_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|drive_type_get_all
dedent|''
name|'def'
name|'drive_type_get_all'
op|'('
name|'context'
op|','
name|'visible'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'drive_type_get_all'
op|'('
name|'context'
op|','
name|'visible'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
