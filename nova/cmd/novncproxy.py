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
string|'"""\nWebsocket proxy that is compatible with OpenStack Nova\nnoVNC consoles. Leverages websockify.py by Joel Martin\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'print_function'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'websocketproxy'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
name|'import'
name|'guru_meditation_report'
name|'as'
name|'gmr'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'novncproxy_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'0.0.0.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Host on which to listen for incoming requests'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'novncproxy_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'6080'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Port on which to listen for incoming requests'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_cli_opts'
op|'('
name|'opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'record'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'daemon'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'ssl_only'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'source_is_ipv6'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'cert'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'key'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'web'"
op|','
string|"'nova.cmd.novnc'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Setup flags'
nl|'\n'
indent|'    '
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'web'"
op|','
string|"'/usr/share/novnc'"
op|')'
newline|'\n'
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'ssl_only'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'CONF'
op|'.'
name|'cert'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|'"SSL only and %s not found"'
op|'%'
name|'CONF'
op|'.'
name|'cert'
op|')'
newline|'\n'
name|'return'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check to see if novnc html/js/css files are present'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'CONF'
op|'.'
name|'web'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
op|'('
string|'"Can not find novnc html/js/css files at %s."'
op|'%'
name|'CONF'
op|'.'
name|'web'
op|')'
newline|'\n'
name|'return'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
nl|'\n'
name|'gmr'
op|'.'
name|'TextGuruMeditation'
op|'.'
name|'setup_autorun'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create and start the NovaWebSockets proxy'
nl|'\n'
name|'server'
op|'='
name|'websocketproxy'
op|'.'
name|'NovaWebSocketProxy'
op|'('
nl|'\n'
name|'listen_host'
op|'='
name|'CONF'
op|'.'
name|'novncproxy_host'
op|','
nl|'\n'
name|'listen_port'
op|'='
name|'CONF'
op|'.'
name|'novncproxy_port'
op|','
nl|'\n'
name|'source_is_ipv6'
op|'='
name|'CONF'
op|'.'
name|'source_is_ipv6'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'CONF'
op|'.'
name|'verbose'
op|','
nl|'\n'
name|'cert'
op|'='
name|'CONF'
op|'.'
name|'cert'
op|','
nl|'\n'
name|'key'
op|'='
name|'CONF'
op|'.'
name|'key'
op|','
nl|'\n'
name|'ssl_only'
op|'='
name|'CONF'
op|'.'
name|'ssl_only'
op|','
nl|'\n'
name|'daemon'
op|'='
name|'CONF'
op|'.'
name|'daemon'
op|','
nl|'\n'
name|'record'
op|'='
name|'CONF'
op|'.'
name|'record'
op|','
nl|'\n'
name|'traffic'
op|'='
name|'CONF'
op|'.'
name|'verbose'
name|'and'
name|'not'
name|'CONF'
op|'.'
name|'daemon'
op|','
nl|'\n'
name|'web'
op|'='
name|'CONF'
op|'.'
name|'web'
op|','
nl|'\n'
name|'file_only'
op|'='
name|'True'
op|','
nl|'\n'
name|'RequestHandlerClass'
op|'='
name|'websocketproxy'
op|'.'
name|'NovaProxyRequestHandler'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start_server'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
