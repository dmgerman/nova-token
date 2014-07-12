begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
nl|'\n'
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
name|'_'
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
DECL|class|LoadedExtensionInfo
name|'class'
name|'LoadedExtensionInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keep track of all loaded API extensions."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|register_extension
dedent|''
name|'def'
name|'register_extension'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_check_extension'
op|'('
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'alias'
op|'='
name|'ext'
op|'.'
name|'alias'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Loaded extension %s"'
op|')'
op|','
name|'alias'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'alias'
name|'in'
name|'self'
op|'.'
name|'extensions'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
string|'"Found duplicate extension: %s"'
nl|'\n'
op|'%'
name|'alias'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'extensions'
op|'['
name|'alias'
op|']'
op|'='
name|'ext'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_check_extension
dedent|''
name|'def'
name|'_check_extension'
op|'('
name|'self'
op|','
name|'extension'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks for required methods in extension objects."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext name: %s'"
op|','
name|'extension'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext alias: %s'"
op|','
name|'extension'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext description: %s'"
op|','
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'extension'
op|'.'
name|'__doc__'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Ext version: %i'"
op|','
name|'extension'
op|'.'
name|'version'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Exception loading extension: %s"'
op|')'
op|','
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_extensions
dedent|''
name|'def'
name|'get_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'extensions'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
