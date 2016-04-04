begin_unit
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
DECL|variable|glance_group
name|'glance_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
nl|'\n'
string|"'glance'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Glance Options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|glance_opts
name|'glance_opts'
op|'='
op|'['
nl|'\n'
comment|'# NOTE(sdague): there is intentionally no default here. This'
nl|'\n'
comment|'# requires configuration. Eventually this will come from the'
nl|'\n'
comment|"# service catalog, however we don't have a good path there atm."
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'api_servers'"
op|','
nl|'\n'
name|'help'
op|'='
string|'\'\'\'\nA list of the glance api servers endpoints available to nova. These\nshould be fully qualified urls of the form\n"scheme://hostname:port[/path]" (i.e. "http://10.0.1.0:9292" or\n"https://my.glance.server/image")\'\'\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'api_insecure'"
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
string|"'Allow to perform insecure SSL (https) requests to '"
nl|'\n'
string|"'glance'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'num_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of retries when uploading / downloading an image '"
nl|'\n'
string|"'to / from glance.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'allowed_direct_url_schemes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of url scheme that can be downloaded directly '"
nl|'\n'
string|"'via the direct_url.  Currently supported schemes: '"
nl|'\n'
string|"'[file].'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'verify_glance_signatures'"
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
string|"'Require Nova to perform signature verification on '"
nl|'\n'
string|"'each image downloaded from Glance.'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'glance_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'glance_opts'
op|','
name|'group'
op|'='
name|'glance_group'
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
name|'glance_group'
op|':'
name|'glance_opts'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit