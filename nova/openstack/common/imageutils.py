begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nHelper methods to deal with images.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
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
name|'strutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QemuImgInfo
name|'class'
name|'QemuImgInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|BACKING_FILE_RE
indent|'    '
name|'BACKING_FILE_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
op|'('
string|'r"^(.*?)\\s*\\(actual\\s+path\\s*:"'
nl|'\n'
string|'r"\\s+(.*?)\\)\\s*$"'
op|')'
op|','
name|'re'
op|'.'
name|'I'
op|')'
newline|'\n'
DECL|variable|TOP_LEVEL_RE
name|'TOP_LEVEL_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"^([\\w\\d\\s\\_\\-]+):(.*)$"'
op|')'
newline|'\n'
DECL|variable|SIZE_RE
name|'SIZE_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"(\\d*\\.?\\d+)(\\w+)?(\\s*\\(\\s*(\\d+)\\s+bytes\\s*\\))?"'
op|','
nl|'\n'
name|'re'
op|'.'
name|'I'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cmd_output'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'details'
op|'='
name|'self'
op|'.'
name|'_parse'
op|'('
name|'cmd_output'
name|'or'
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backing_file'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'backing_file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'file_format'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'file_format'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'virtual_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'virtual_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cluster_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'cluster_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk_size'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'disk_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'snapshots'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'snapshot_list'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'encrypted'
op|'='
name|'details'
op|'.'
name|'get'
op|'('
string|"'encrypted'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lines'
op|'='
op|'['
nl|'\n'
string|"'image: %s'"
op|'%'
name|'self'
op|'.'
name|'image'
op|','
nl|'\n'
string|"'file_format: %s'"
op|'%'
name|'self'
op|'.'
name|'file_format'
op|','
nl|'\n'
string|"'virtual_size: %s'"
op|'%'
name|'self'
op|'.'
name|'virtual_size'
op|','
nl|'\n'
string|"'disk_size: %s'"
op|'%'
name|'self'
op|'.'
name|'disk_size'
op|','
nl|'\n'
string|"'cluster_size: %s'"
op|'%'
name|'self'
op|'.'
name|'cluster_size'
op|','
nl|'\n'
string|"'backing_file: %s'"
op|'%'
name|'self'
op|'.'
name|'backing_file'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'snapshots'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'.'
name|'append'
op|'('
string|'"snapshots: %s"'
op|'%'
name|'self'
op|'.'
name|'snapshots'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'encrypted'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'.'
name|'append'
op|'('
string|'"encrypted: %s"'
op|'%'
name|'self'
op|'.'
name|'encrypted'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_canonicalize
dedent|''
name|'def'
name|'_canonicalize'
op|'('
name|'self'
op|','
name|'field'
op|')'
op|':'
newline|'\n'
comment|'# Standardize on underscores/lc/no dash and no spaces'
nl|'\n'
comment|'# since qemu seems to have mixed outputs here... and'
nl|'\n'
comment|'# this format allows for better integration with python'
nl|'\n'
comment|'# - ie for usage in kwargs and such...'
nl|'\n'
indent|'        '
name|'field'
op|'='
name|'field'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'for'
name|'c'
name|'in'
op|'('
string|'" "'
op|','
string|'"-"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'field'
op|'='
name|'field'
op|'.'
name|'replace'
op|'('
name|'c'
op|','
string|"'_'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'field'
newline|'\n'
nl|'\n'
DECL|member|_extract_bytes
dedent|''
name|'def'
name|'_extract_bytes'
op|'('
name|'self'
op|','
name|'details'
op|')'
op|':'
newline|'\n'
comment|'# Replace it with the byte amount'
nl|'\n'
indent|'        '
name|'real_size'
op|'='
name|'self'
op|'.'
name|'SIZE_RE'
op|'.'
name|'search'
op|'('
name|'details'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'real_size'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'\'Invalid input value "%s".\''
op|')'
op|'%'
name|'details'
op|')'
newline|'\n'
dedent|''
name|'magnitude'
op|'='
name|'real_size'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
newline|'\n'
name|'unit_of_measure'
op|'='
name|'real_size'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
newline|'\n'
name|'bytes_info'
op|'='
name|'real_size'
op|'.'
name|'group'
op|'('
number|'3'
op|')'
newline|'\n'
name|'if'
name|'bytes_info'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'real_size'
op|'.'
name|'group'
op|'('
number|'4'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'unit_of_measure'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'magnitude'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'strutils'
op|'.'
name|'string_to_bytes'
op|'('
string|"'%s%sB'"
op|'%'
op|'('
name|'magnitude'
op|','
name|'unit_of_measure'
op|')'
op|','
nl|'\n'
name|'return_int'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extract_details
dedent|''
name|'def'
name|'_extract_details'
op|'('
name|'self'
op|','
name|'root_cmd'
op|','
name|'root_details'
op|','
name|'lines_after'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'real_details'
op|'='
name|'root_details'
newline|'\n'
name|'if'
name|'root_cmd'
op|'=='
string|"'backing_file'"
op|':'
newline|'\n'
comment|'# Replace it with the real backing file'
nl|'\n'
indent|'            '
name|'backing_match'
op|'='
name|'self'
op|'.'
name|'BACKING_FILE_RE'
op|'.'
name|'match'
op|'('
name|'root_details'
op|')'
newline|'\n'
name|'if'
name|'backing_match'
op|':'
newline|'\n'
indent|'                '
name|'real_details'
op|'='
name|'backing_match'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'root_cmd'
name|'in'
op|'['
string|"'virtual_size'"
op|','
string|"'cluster_size'"
op|','
string|"'disk_size'"
op|']'
op|':'
newline|'\n'
comment|'# Replace it with the byte amount (if we can convert it)'
nl|'\n'
indent|'            '
name|'if'
name|'root_details'
op|'=='
string|"'None'"
op|':'
newline|'\n'
indent|'                '
name|'real_details'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'real_details'
op|'='
name|'self'
op|'.'
name|'_extract_bytes'
op|'('
name|'root_details'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'root_cmd'
op|'=='
string|"'file_format'"
op|':'
newline|'\n'
indent|'            '
name|'real_details'
op|'='
name|'real_details'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'root_cmd'
op|'=='
string|"'snapshot_list'"
op|':'
newline|'\n'
comment|"# Next line should be a header, starting with 'ID'"
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'lines_after'
name|'or'
name|'not'
name|'lines_after'
op|'['
number|'0'
op|']'
op|'.'
name|'startswith'
op|'('
string|'"ID"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Snapshot list encountered but no header found!"'
op|')'
newline|'\n'
name|'raise'
name|'ValueError'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'del'
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
name|'real_details'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# This is the sprintf pattern we will try to match'
nl|'\n'
comment|'# "%-10s%-20s%7s%20s%15s"'
nl|'\n'
comment|'# ID TAG VM SIZE DATE VM CLOCK (current header)'
nl|'\n'
name|'while'
name|'lines_after'
op|':'
newline|'\n'
indent|'                '
name|'line'
op|'='
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
name|'line_pieces'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'line_pieces'
op|')'
op|'!='
number|'6'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
comment|'# Check against this pattern in the final position'
nl|'\n'
comment|'# "%02d:%02d:%02d.%03d"'
nl|'\n'
dedent|''
name|'date_pieces'
op|'='
name|'line_pieces'
op|'['
number|'5'
op|']'
op|'.'
name|'split'
op|'('
string|'":"'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'date_pieces'
op|')'
op|'!='
number|'3'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'real_details'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'line_pieces'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
string|"'tag'"
op|':'
name|'line_pieces'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'vm_size'"
op|':'
name|'line_pieces'
op|'['
number|'2'
op|']'
op|','
nl|'\n'
string|"'date'"
op|':'
name|'line_pieces'
op|'['
number|'3'
op|']'
op|','
nl|'\n'
string|"'vm_clock'"
op|':'
name|'line_pieces'
op|'['
number|'4'
op|']'
op|'+'
string|'" "'
op|'+'
name|'line_pieces'
op|'['
number|'5'
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'del'
name|'lines_after'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'real_details'
newline|'\n'
nl|'\n'
DECL|member|_parse
dedent|''
name|'def'
name|'_parse'
op|'('
name|'self'
op|','
name|'cmd_output'
op|')'
op|':'
newline|'\n'
comment|'# Analysis done of qemu-img.c to figure out what is going on here'
nl|'\n'
comment|"# Find all points start with some chars and then a ':' then a newline"
nl|'\n'
comment|"# and then handle the results of those 'top level' items in a separate"
nl|'\n'
comment|'# function.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# TODO(harlowja): newer versions might have a json output format'
nl|'\n'
comment|'#                 we should switch to that whenever possible.'
nl|'\n'
comment|'#                 see: http://bit.ly/XLJXDX'
nl|'\n'
indent|'        '
name|'contents'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'lines'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'cmd_output'
op|'.'
name|'splitlines'
op|'('
op|')'
name|'if'
name|'x'
op|'.'
name|'strip'
op|'('
op|')'
op|']'
newline|'\n'
name|'while'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'lines'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'top_level'
op|'='
name|'self'
op|'.'
name|'TOP_LEVEL_RE'
op|'.'
name|'match'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
name|'top_level'
op|':'
newline|'\n'
indent|'                '
name|'root'
op|'='
name|'self'
op|'.'
name|'_canonicalize'
op|'('
name|'top_level'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'root'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'root_details'
op|'='
name|'top_level'
op|'.'
name|'group'
op|'('
number|'2'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'details'
op|'='
name|'self'
op|'.'
name|'_extract_details'
op|'('
name|'root'
op|','
name|'root_details'
op|','
name|'lines'
op|')'
newline|'\n'
name|'contents'
op|'['
name|'root'
op|']'
op|'='
name|'details'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'contents'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
