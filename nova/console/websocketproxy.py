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
name|'import'
name|'urlparse'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
DECL|class|NovaProxyRequestHandlerBase
name|'class'
name|'NovaProxyRequestHandlerBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|new_websocket_client
indent|'    '
name|'def'
name|'new_websocket_client'
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
comment|'# The nova expected behavior is to have token'
nl|'\n'
comment|'# passed to the method GET of the request'
nl|'\n'
name|'query'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'self'
op|'.'
name|'path'
op|')'
op|'.'
name|'query'
newline|'\n'
name|'token'
op|'='
name|'urlparse'
op|'.'
name|'parse_qs'
op|'('
name|'query'
op|')'
op|'.'
name|'get'
op|'('
string|'"token"'
op|','
op|'['
string|'""'
op|']'
op|')'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
comment|"# NoVNC uses it's own convention that forward token"
nl|'\n'
comment|'# from the request to a cookie header, we should check'
nl|'\n'
comment|'# also for this behavior'
nl|'\n'
indent|'            '
name|'hcookie'
op|'='
name|'self'
op|'.'
name|'headers'
op|'.'
name|'getheader'
op|'('
string|"'cookie'"
op|')'
newline|'\n'
name|'if'
name|'hcookie'
op|':'
newline|'\n'
indent|'                '
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
name|'hcookie'
op|')'
newline|'\n'
name|'if'
string|"'token'"
name|'in'
name|'cookie'
op|':'
newline|'\n'
indent|'                    '
name|'token'
op|'='
name|'cookie'
op|'['
string|"'token'"
op|']'
op|'.'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
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
name|'raise'
name|'exception'
op|'.'
name|'InvalidToken'
op|'('
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'msg'
op|'('
name|'_'
op|'('
string|"'connect info: %s'"
op|')'
op|','
name|'str'
op|'('
name|'connect_info'
op|')'
op|')'
newline|'\n'
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
name|'_'
op|'('
string|'"connecting to: %(host)s:%(port)s"'
op|')'
op|'%'
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
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
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
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
comment|'# Start proxying'
nl|'\n'
dedent|''
dedent|''
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
name|'_'
op|'('
string|'"%(host)s:%(port)s: Target closed"'
op|')'
op|'%'
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
nl|'\n'
nl|'\n'
comment|'# TODO(sross): when the websockify version is bumped to be >=0.6,'
nl|'\n'
comment|'#              remove the if-else statement and make the if branch'
nl|'\n'
comment|'#              contents the only code.'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'getattr'
op|'('
name|'websockify'
op|','
string|"'ProxyRequestHandler'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'    '
name|'class'
name|'NovaProxyRequestHandler'
op|'('
name|'NovaProxyRequestHandlerBase'
op|','
nl|'\n'
DECL|class|NovaProxyRequestHandler
name|'websockify'
op|'.'
name|'ProxyRequestHandler'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
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
indent|'            '
name|'websockify'
op|'.'
name|'ProxyRequestHandler'
op|'.'
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
newline|'\n'
nl|'\n'
DECL|member|socket
dedent|''
name|'def'
name|'socket'
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
indent|'            '
name|'return'
name|'websockify'
op|'.'
name|'WebSocketServer'
op|'.'
name|'socket'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|class|NovaWebSocketProxy
dedent|''
dedent|''
name|'class'
name|'NovaWebSocketProxy'
op|'('
name|'websockify'
op|'.'
name|'WebSocketProxy'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_logger
name|'def'
name|'get_logger'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'LOG'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'class'
name|'NovaWebSocketProxy'
op|'('
name|'NovaProxyRequestHandlerBase'
op|','
nl|'\n'
DECL|class|NovaWebSocketProxy
name|'websockify'
op|'.'
name|'WebSocketProxy'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
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
indent|'            '
name|'del'
name|'kwargs'
op|'['
string|"'traffic'"
op|']'
newline|'\n'
name|'del'
name|'kwargs'
op|'['
string|"'RequestHandlerClass'"
op|']'
newline|'\n'
name|'websockify'
op|'.'
name|'WebSocketProxy'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
nl|'\n'
name|'target_host'
op|'='
string|"'ignore'"
op|','
nl|'\n'
name|'target_port'
op|'='
string|"'ignore'"
op|','
nl|'\n'
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
nl|'\n'
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
indent|'            '
name|'self'
op|'.'
name|'new_websocket_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|msg
dedent|''
name|'def'
name|'msg'
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
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|vmsg
dedent|''
name|'def'
name|'vmsg'
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
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|warn
dedent|''
name|'def'
name|'warn'
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
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|print_traffic
dedent|''
name|'def'
name|'print_traffic'
op|'('
name|'self'
op|','
name|'token'
op|'='
string|'"."'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'traffic'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'token'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|NovaProxyRequestHandler
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaProxyRequestHandler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
