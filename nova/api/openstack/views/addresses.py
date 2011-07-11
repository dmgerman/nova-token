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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
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
string|"''' Models a server addresses response as a python dictionary.'''"
newline|'\n'
nl|'\n'
DECL|member|build
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
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
DECL|member|build
indent|'    '
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'private_ips'
op|'='
name|'self'
op|'.'
name|'build_private_parts'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'public_ips'
op|'='
name|'self'
op|'.'
name|'build_public_parts'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'public'
op|'='
name|'public_ips'
op|','
name|'private'
op|'='
name|'private_ips'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_public_parts
dedent|''
name|'def'
name|'build_public_parts'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ips/floating_ips/address'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_private_parts
dedent|''
name|'def'
name|'build_private_parts'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ips/address'"
op|')'
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
DECL|member|build
indent|'    '
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
comment|"# TODO(tr3buchet) - this shouldn't be hard coded to 4..."
nl|'\n'
indent|'        '
name|'private_ips'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ips/address'"
op|')'
newline|'\n'
name|'private_ips'
op|'='
op|'['
name|'dict'
op|'('
name|'version'
op|'='
number|'4'
op|','
name|'addr'
op|'='
name|'a'
op|')'
name|'for'
name|'a'
name|'in'
name|'private_ips'
op|']'
newline|'\n'
name|'public_ips'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
nl|'\n'
string|"'fixed_ips/floating_ips/address'"
op|')'
newline|'\n'
name|'public_ips'
op|'='
op|'['
name|'dict'
op|'('
name|'version'
op|'='
number|'4'
op|','
name|'addr'
op|'='
name|'a'
op|')'
name|'for'
name|'a'
name|'in'
name|'public_ips'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'public'
op|'='
name|'public_ips'
op|','
name|'private'
op|'='
name|'private_ips'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
