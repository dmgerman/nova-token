begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata <yamahata@valinux co jp>'
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
name|'import'
name|'re'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|properties_root_device_name
name|'def'
name|'properties_root_device_name'
op|'('
name|'properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""get root device name from image meta data.\n    If it isn\'t specified, return None.\n    """'
newline|'\n'
name|'root_device_name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# NOTE(yamahata): see image_service.s3.s3create()'
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'mappings'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdm'
op|'['
string|"'virtual'"
op|']'
op|'=='
string|"'root'"
op|':'
newline|'\n'
indent|'            '
name|'root_device_name'
op|'='
name|'bdm'
op|'['
string|"'device'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): register_image's command line can override"
nl|'\n'
comment|'#                 <machine>.manifest.xml'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'root_device_name'"
name|'in'
name|'properties'
op|':'
newline|'\n'
indent|'        '
name|'root_device_name'
op|'='
name|'properties'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'root_device_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_ephemeral
dedent|''
name|'_ephemeral'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^ephemeral(\\d|[1-9]\\d+)$'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_ephemeral
name|'def'
name|'is_ephemeral'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_ephemeral'
op|'.'
name|'match'
op|'('
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ephemeral_num
dedent|''
name|'def'
name|'ephemeral_num'
op|'('
name|'ephemeral_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'is_ephemeral'
op|'('
name|'ephemeral_name'
op|')'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'_ephemeral'
op|'.'
name|'sub'
op|'('
string|"'\\\\1'"
op|','
name|'ephemeral_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_swap_or_ephemeral
dedent|''
name|'def'
name|'is_swap_or_ephemeral'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'device_name'
op|'=='
string|"'swap'"
name|'or'
name|'is_ephemeral'
op|'('
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mappings_prepend_dev
dedent|''
name|'def'
name|'mappings_prepend_dev'
op|'('
name|'mappings'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Prepend \'/dev/\' to \'device\' entry of swap/ephemeral virtual type"""'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'mappings'
op|':'
newline|'\n'
indent|'        '
name|'virtual'
op|'='
name|'m'
op|'['
string|"'virtual'"
op|']'
newline|'\n'
name|'if'
op|'('
name|'is_swap_or_ephemeral'
op|'('
name|'virtual'
op|')'
name|'and'
nl|'\n'
op|'('
name|'not'
name|'m'
op|'['
string|"'device'"
op|']'
op|'.'
name|'startswith'
op|'('
string|"'/'"
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'m'
op|'['
string|"'device'"
op|']'
op|'='
string|"'/dev/'"
op|'+'
name|'m'
op|'['
string|"'device'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_dev
dedent|''
name|'_dev'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^/dev/'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|strip_dev
name|'def'
name|'strip_dev'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""remove leading \'/dev/\'"""'
newline|'\n'
name|'return'
name|'_dev'
op|'.'
name|'sub'
op|'('
string|"''"
op|','
name|'device_name'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
