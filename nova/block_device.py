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
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_ROOT_DEV_NAME
name|'DEFAULT_ROOT_DEV_NAME'
op|'='
string|"'/dev/sda1'"
newline|'\n'
DECL|variable|_DEFAULT_MAPPINGS
name|'_DEFAULT_MAPPINGS'
op|'='
op|'{'
string|"'ami'"
op|':'
string|"'sda1'"
op|','
nl|'\n'
string|"'ephemeral0'"
op|':'
string|"'sda2'"
op|','
nl|'\n'
string|"'root'"
op|':'
name|'DEFAULT_ROOT_DEV_NAME'
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'sda3'"
op|'}'
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
name|'if'
name|'device_name'
name|'else'
name|'device_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_pref
dedent|''
name|'_pref'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^((x?v|s)d)'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|strip_prefix
name|'def'
name|'strip_prefix'
op|'('
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" remove both leading /dev/ and xvd or sd or vd """'
newline|'\n'
name|'device_name'
op|'='
name|'strip_dev'
op|'('
name|'device_name'
op|')'
newline|'\n'
name|'return'
name|'_pref'
op|'.'
name|'sub'
op|'('
string|"''"
op|','
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_block_mapping
dedent|''
name|'def'
name|'instance_block_mapping'
op|'('
name|'instance'
op|','
name|'bdms'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'root_device_name'
op|'='
name|'instance'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
comment|'# NOTE(clayg): remove this when xenapi is setting default_root_device'
nl|'\n'
name|'if'
name|'root_device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'compute_driver'
op|'.'
name|'endswith'
op|'('
string|"'xenapi.XenAPIDriver'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_device_name'
op|'='
string|"'/dev/xvda'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_DEFAULT_MAPPINGS'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mappings'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mappings'
op|'['
string|"'ami'"
op|']'
op|'='
name|'strip_dev'
op|'('
name|'root_device_name'
op|')'
newline|'\n'
name|'mappings'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_device_name'
newline|'\n'
name|'default_ephemeral_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_ephemeral_device'"
op|')'
newline|'\n'
name|'if'
name|'default_ephemeral_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'ephemeral0'"
op|']'
op|'='
name|'default_ephemeral_device'
newline|'\n'
dedent|''
name|'default_swap_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_swap_device'"
op|')'
newline|'\n'
name|'if'
name|'default_swap_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'swap'"
op|']'
op|'='
name|'default_swap_device'
newline|'\n'
dedent|''
name|'ebs_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# 'ephemeralN', 'swap' and ebs"
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'bdms'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdm'
op|'['
string|"'no_device'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# ebs volume case'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
name|'or'
name|'bdm'
op|'['
string|"'snapshot_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ebs_devices'
op|'.'
name|'append'
op|'('
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'virtual_name'
op|'='
name|'bdm'
op|'['
string|"'virtual_name'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'virtual_name'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'is_swap_or_ephemeral'
op|'('
name|'virtual_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
name|'virtual_name'
op|']'
op|'='
name|'bdm'
op|'['
string|"'device_name'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): I'm not sure how ebs device should be numbered."
nl|'\n'
comment|'#                 Right now sort by device name for deterministic'
nl|'\n'
comment|'#                 result.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'        '
name|'nebs'
op|'='
number|'0'
newline|'\n'
name|'ebs_devices'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'ebs'
name|'in'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
string|"'ebs%d'"
op|'%'
name|'nebs'
op|']'
op|'='
name|'ebs'
newline|'\n'
name|'nebs'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|match_device
dedent|''
name|'def'
name|'match_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Matches device name and returns prefix, suffix"""'
newline|'\n'
name|'match'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
string|'"(^/dev/x{0,1}[a-z]{0,1}d{0,1})([a-z]+)[0-9]*$"'
op|','
name|'device'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
