begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|mks_group
name|'mks_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
string|"'mks'"
op|','
name|'title'
op|'='
string|"'MKS Options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|mks_opts
name|'mks_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'mksproxy_base_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http://127.0.0.1:6090/'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location of MKS web console proxy, in the form '"
nl|'\n'
string|'\'"http://127.0.0.1:6090/"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enabled'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Enable MKS related features'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ALL_MKS_OPTS
name|'ALL_MKS_OPTS'
op|'='
name|'mks_opts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_group'
op|'('
name|'mks_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_MKS_OPTS'
op|','
name|'group'
op|'='
name|'mks_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'mks_group'
op|':'
name|'ALL_MKS_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit