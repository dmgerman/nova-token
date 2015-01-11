begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'record'"
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
string|"'Record sessions to FILE.[session_number]'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'daemon'"
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
string|"'Become a daemon (background process)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'ssl_only'"
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
string|"'Disallow non-encrypted connections'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'source_is_ipv6'"
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
string|"'Source is ipv6'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'self.pem'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'SSL certificate file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'key'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'SSL key file (if separate from cert)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'web'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/usr/share/spice-html5'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Run webserver on same port. Serve files from DIR.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_cli_opts'
op|'('
name|'opts'
op|')'
newline|'\n'
endmarker|''
end_unit
