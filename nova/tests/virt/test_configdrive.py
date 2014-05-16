begin_unit
comment|'#    Copyright 2014 IBM Corp.'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'configdrive'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDriveTestCase
name|'class'
name|'ConfigDriveTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_valid_string_values
indent|'    '
name|'def'
name|'test_valid_string_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'value'
name|'in'
op|'('
name|'strutils'
op|'.'
name|'TRUE_STRINGS'
op|'+'
op|'('
string|"'always'"
op|','
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'force_config_drive'
op|'='
name|'value'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'configdrive'
op|'.'
name|'required_by'
op|'('
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_string_values
dedent|''
dedent|''
name|'def'
name|'test_invalid_string_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'value'
name|'in'
op|'('
name|'strutils'
op|'.'
name|'FALSE_STRINGS'
op|'+'
op|'('
string|"'foo'"
op|','
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'force_config_drive'
op|'='
name|'value'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'configdrive'
op|'.'
name|'required_by'
op|'('
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
