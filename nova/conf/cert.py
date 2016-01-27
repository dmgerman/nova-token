begin_unit
comment|'# Copyright 2016 IBM Corp.'
nl|'\n'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|cert_topic_opt
name|'cert_topic_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"cert_topic"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"cert"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The topic cert nodes listen on"'
op|')'
newline|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"cert"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Set a version cap for messages sent to cert services"'
op|')'
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
name|'register_opts'
op|'('
op|'['
name|'cert_topic_opt'
op|']'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|'"upgrade_levels"'
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
string|'"DEFAULT"'
op|':'
op|'['
name|'cert_topic_opt'
op|']'
op|','
nl|'\n'
string|'"upgrade_levels"'
op|':'
op|'['
name|'rpcapi_cap_opt'
op|']'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
