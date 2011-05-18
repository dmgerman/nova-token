begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Openstack API base limits view builder."""'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limits
name|'def'
name|'_build_rate_limits'
op|'('
name|'self'
op|','
name|'rate_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limit
dedent|''
name|'def'
name|'_build_rate_limit'
op|'('
name|'self'
op|','
name|'rate_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_absolute_limits
dedent|''
name|'def'
name|'_build_absolute_limits'
op|'('
name|'self'
op|','
name|'absolute_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|build
dedent|''
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'rate_limits'
op|','
name|'absolute_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rate_limits'
op|'='
name|'self'
op|'.'
name|'_build_rate_limits'
op|'('
name|'rate_limits'
op|')'
newline|'\n'
name|'absolute_limits'
op|'='
name|'self'
op|'.'
name|'_build_absolute_limits'
op|'('
name|'absolute_limits'
op|')'
newline|'\n'
nl|'\n'
name|'output'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
name|'rate_limits'
op|','
nl|'\n'
string|'"absolute"'
op|':'
name|'absolute_limits'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'output'
newline|'\n'
nl|'\n'
DECL|member|_build_absolute_limits
dedent|''
name|'def'
name|'_build_absolute_limits'
op|'('
name|'self'
op|','
name|'absolute_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limits
dedent|''
name|'def'
name|'_build_rate_limits'
op|'('
name|'self'
op|','
name|'rate_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limit
dedent|''
name|'def'
name|'_build_rate_limit'
op|'('
name|'self'
op|','
name|'rate_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV10
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV10'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Openstack API v1.0 limits view builder."""'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limits
name|'def'
name|'_build_rate_limits'
op|'('
name|'self'
op|','
name|'rate_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_build_rate_limit'
op|'('
name|'r'
op|')'
name|'for'
name|'r'
name|'in'
name|'rate_limits'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limit
dedent|''
name|'def'
name|'_build_rate_limit'
op|'('
name|'self'
op|','
name|'rate_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"verb"'
op|':'
name|'rate_limit'
op|'['
string|'"verb"'
op|']'
op|','
nl|'\n'
string|'"URI"'
op|':'
name|'rate_limit'
op|'['
string|'"URI"'
op|']'
op|','
nl|'\n'
string|'"regex"'
op|':'
name|'rate_limit'
op|'['
string|'"regex"'
op|']'
op|','
nl|'\n'
string|'"value"'
op|':'
name|'rate_limit'
op|'['
string|'"value"'
op|']'
op|','
nl|'\n'
string|'"remaining"'
op|':'
name|'int'
op|'('
name|'rate_limit'
op|'['
string|'"remaining"'
op|']'
op|')'
op|','
nl|'\n'
string|'"unit"'
op|':'
name|'rate_limit'
op|'['
string|'"unit"'
op|']'
op|','
nl|'\n'
string|'"resetTime"'
op|':'
name|'rate_limit'
op|'['
string|'"resetTime"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_build_absolute_limits
dedent|''
name|'def'
name|'_build_absolute_limits'
op|'('
name|'self'
op|','
name|'absolute_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV11
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV11'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Openstack API v1.1 limits view builder."""'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limits
name|'def'
name|'_build_rate_limits'
op|'('
name|'self'
op|','
name|'rate_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'rate_limit'
name|'in'
name|'rate_limits'
op|':'
newline|'\n'
indent|'            '
name|'_rate_limit_key'
op|'='
name|'None'
newline|'\n'
name|'_rate_limit'
op|'='
name|'self'
op|'.'
name|'_build_rate_limit'
op|'('
name|'rate_limit'
op|')'
newline|'\n'
nl|'\n'
comment|'# check for existing key'
nl|'\n'
name|'for'
name|'limit'
name|'in'
name|'limits'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'limit'
op|'['
string|'"uri"'
op|']'
op|'=='
name|'rate_limit'
op|'['
string|'"URI"'
op|']'
name|'and'
name|'limit'
op|'['
string|'"regex"'
op|']'
op|'=='
name|'limit'
op|'['
string|'"regex"'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'_rate_limit_key'
op|'='
name|'limit'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
comment|"# ensure we have a key if we didn't find one"
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'_rate_limit_key'
op|':'
newline|'\n'
indent|'                '
name|'_rate_limit_key'
op|'='
op|'{'
nl|'\n'
string|'"uri"'
op|':'
name|'rate_limit'
op|'['
string|'"URI"'
op|']'
op|','
nl|'\n'
string|'"regex"'
op|':'
name|'rate_limit'
op|'['
string|'"regex"'
op|']'
op|','
nl|'\n'
string|'"limit"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'limits'
op|'.'
name|'append'
op|'('
name|'_rate_limit_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_rate_limit_key'
op|'['
string|'"limit"'
op|']'
op|'.'
name|'append'
op|'('
name|'_rate_limit'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'limits'
newline|'\n'
nl|'\n'
DECL|member|_build_rate_limit
dedent|''
name|'def'
name|'_build_rate_limit'
op|'('
name|'self'
op|','
name|'rate_limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"verb"'
op|':'
name|'rate_limit'
op|'['
string|'"verb"'
op|']'
op|','
nl|'\n'
string|'"value"'
op|':'
name|'rate_limit'
op|'['
string|'"value"'
op|']'
op|','
nl|'\n'
string|'"remaining"'
op|':'
name|'int'
op|'('
name|'rate_limit'
op|'['
string|'"remaining"'
op|']'
op|')'
op|','
nl|'\n'
string|'"unit"'
op|':'
name|'rate_limit'
op|'['
string|'"unit"'
op|']'
op|','
nl|'\n'
string|'"next-available"'
op|':'
name|'rate_limit'
op|'['
string|'"resetTime"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_build_absolute_limits
dedent|''
name|'def'
name|'_build_absolute_limits'
op|'('
name|'self'
op|','
name|'absolute_limits'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Builder for absolute limits\n\n        absolute_limits should be given as a dict of limits.\n        For example: {"ram": 512, "gigabytes": 1024}.\n\n        """'
newline|'\n'
name|'limit_names'
op|'='
op|'{'
nl|'\n'
string|'"ram"'
op|':'
op|'['
string|'"maxTotalRAMSize"'
op|']'
op|','
nl|'\n'
string|'"instances"'
op|':'
op|'['
string|'"maxTotalInstances"'
op|']'
op|','
nl|'\n'
string|'"cores"'
op|':'
op|'['
string|'"maxTotalCores"'
op|']'
op|','
nl|'\n'
string|'"metadata_items"'
op|':'
op|'['
string|'"maxServerMeta"'
op|','
string|'"maxImageMeta"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'name'
op|','
name|'value'
name|'in'
name|'absolute_limits'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
name|'in'
name|'limit_names'
name|'and'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'name'
name|'in'
name|'limit_names'
op|'['
name|'name'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'limits'
op|'['
name|'name'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'limits'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
