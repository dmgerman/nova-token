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
name|'copy'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'versions'
name|'as'
name|'compute_views'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_view_builder
name|'def'
name|'get_view_builder'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'base_url'
op|'='
name|'req'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'ViewBuilder'
op|'('
name|'base_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
dedent|''
name|'class'
name|'ViewBuilder'
op|'('
name|'compute_views'
op|'.'
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|generate_href
indent|'    '
name|'def'
name|'generate_href'
op|'('
name|'self'
op|','
name|'path'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an url that refers to a specific version_number."""'
newline|'\n'
name|'version_number'
op|'='
string|"'v1'"
newline|'\n'
name|'if'
name|'path'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'path'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'version_number'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'base_url'
op|','
name|'version_number'
op|')'
op|'+'
string|"'/'"
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
