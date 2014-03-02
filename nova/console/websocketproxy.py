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
string|"'''\nWebsocket proxy that is compatible with OpenStack Nova.\nLeverages websockify.py by Joel Martin\n'''"
newline|'\n'
nl|'\n'
name|'import'
name|'Cookie'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'import'
name|'websockify'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'consoleauth'
name|'import'
name|'rpcapi'
name|'as'
name|'consoleauth_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaWebSocketProxy
name|'class'
name|'NovaWebSocketProxy'
op|'('
name|'websockify'
op|'.'
name|'WebSocketProxy'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'websockify'
op|'.'
name|'WebSocketProxy'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'unix_target'
op|'='
name|'None'
op|','
nl|'\n'
name|'target_cfg'
op|'='
name|'None'
op|','
nl|'\n'
name|'ssl_target'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|new_client
dedent|''
name|'def'
name|'new_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called after a new WebSocket connection has been established."""'
newline|'\n'
comment|"# Reopen the eventlet hub to make sure we don't share an epoll"
nl|'\n'
comment|'# fd with parent and/or siblings, which would be bad'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'hubs'
newline|'\n'
name|'hubs'
op|'.'
name|'use_hub'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'cookie'
op|'='
name|'Cookie'
op|'.'
name|'SimpleCookie'
op|'('
op|')'
newline|'\n'
name|'cookie'
op|'.'
name|'load'
op|'('
name|'self'
op|'.'
name|'headers'
op|'.'
name|'getheader'
op|'('
string|"'cookie'"
op|')'
op|')'
newline|'\n'
name|'token'
op|'='
name|'cookie'
op|'['
string|"'token'"
op|']'
op|'.'
name|'value'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'rpcapi'
op|'='
name|'consoleauth_rpcapi'
op|'.'
name|'ConsoleAuthAPI'
op|'('
op|')'
newline|'\n'
name|'connect_info'
op|'='
name|'rpcapi'
op|'.'
name|'check_token'
op|'('
name|'ctxt'
op|','
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'connect_info'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Invalid Token: %s"'
op|')'
op|','
name|'token'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Invalid Token"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'host'
op|'='
name|'connect_info'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'port'
op|'='
name|'int'
op|'('
name|'connect_info'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Connect to the target'
nl|'\n'
name|'self'
op|'.'
name|'msg'
op|'('
string|'"connecting to: %s:%s"'
op|'%'
op|'('
name|'host'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"connecting to: %(host)s:%(port)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'port'"
op|':'
name|'port'
op|'}'
op|')'
newline|'\n'
name|'tsock'
op|'='
name|'self'
op|'.'
name|'socket'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'connect'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Handshake as necessary'
nl|'\n'
name|'if'
name|'connect_info'
op|'.'
name|'get'
op|'('
string|"'internal_access_path'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'tsock'
op|'.'
name|'send'
op|'('
string|'"CONNECT %s HTTP/1.1\\r\\n\\r\\n"'
op|'%'
nl|'\n'
name|'connect_info'
op|'['
string|"'internal_access_path'"
op|']'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'='
name|'tsock'
op|'.'
name|'recv'
op|'('
number|'4096'
op|','
name|'socket'
op|'.'
name|'MSG_PEEK'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'find'
op|'('
string|'"\\r\\n\\r\\n"'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'data'
op|'.'
name|'split'
op|'('
string|'"\\r\\n"'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'find'
op|'('
string|'"200"'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Invalid Connection Info %s"'
op|')'
op|','
name|'token'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Invalid Connection Info"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'tsock'
op|'.'
name|'recv'
op|'('
name|'len'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'verbose'
name|'and'
name|'not'
name|'self'
op|'.'
name|'daemon'
op|':'
newline|'\n'
indent|'            '
name|'print'
op|'('
name|'self'
op|'.'
name|'traffic_legend'
op|')'
newline|'\n'
nl|'\n'
comment|'# Start proxying'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'do_proxy'
op|'('
name|'tsock'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tsock'
op|':'
newline|'\n'
indent|'                '
name|'tsock'
op|'.'
name|'shutdown'
op|'('
name|'socket'
op|'.'
name|'SHUT_RDWR'
op|')'
newline|'\n'
name|'tsock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vmsg'
op|'('
string|'"%s:%s: Target closed"'
op|'%'
op|'('
name|'host'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"%(host)s:%(port)s: Target closed"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'port'"
op|':'
name|'port'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
