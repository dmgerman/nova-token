begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
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
DECL|variable|api_paste_config_opt
name|'api_paste_config_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'api_paste_config'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"api-paste.ini"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File name for the paste.deploy config for nova-api'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|wsgi_log_format_opt
name|'wsgi_log_format_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'wsgi_log_format'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'\'%(client_ip)s "%(request_line)s" status: %(status_code)s\''
nl|'\n'
string|"' len: %(body_length)s time: %(wall_seconds).7f'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A python format string that is used as the template to '"
nl|'\n'
string|"'generate log lines. The following values can be formatted '"
nl|'\n'
string|"'into it: client_ip, date_time, request_line, status_code, '"
nl|'\n'
string|"'body_length, wall_seconds.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|secure_proxy_ssl_header_opt
name|'secure_proxy_ssl_header_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'secure_proxy_ssl_header'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The HTTP header used to determine the scheme for the '"
nl|'\n'
string|"'original request, even if it was removed by an SSL '"
nl|'\n'
string|"'terminating proxy. Typical value is '"
nl|'\n'
string|'\'"HTTP_X_FORWARDED_PROTO".\''
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ssl_ca_file_opt
name|'ssl_ca_file_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_ca_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"CA certificate file to use to verify "'
nl|'\n'
string|'"connecting clients"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ssl_cert_file_opt
name|'ssl_cert_file_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_cert_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"SSL certificate of API server"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ssl_key_file_opt
name|'ssl_key_file_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ssl_key_file'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"SSL private key of API server"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|tcp_keepidle_opt
name|'tcp_keepidle_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tcp_keepidle'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Sets the value of TCP_KEEPIDLE in seconds for each "'
nl|'\n'
string|'"server socket. Not supported on OS X."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|wsgi_default_pool_size_opt
name|'wsgi_default_pool_size_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'wsgi_default_pool_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Size of the pool of greenthreads used by wsgi"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|max_header_line_opt
name|'max_header_line_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_header_line'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'16384'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Maximum line size of message headers to be accepted. "'
nl|'\n'
string|'"max_header_line may need to be increased when using "'
nl|'\n'
string|'"large tokens (typically those generated by the "'
nl|'\n'
string|'"Keystone v3 API with big service catalogs)."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|wsgi_keep_alive_opt
name|'wsgi_keep_alive_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'wsgi_keep_alive'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"If False, closes the client socket connection "'
nl|'\n'
string|'"explicitly."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|client_socket_timeout_opt
name|'client_socket_timeout_opt'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'client_socket_timeout'"
op|','
name|'default'
op|'='
number|'900'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Timeout for client connections\' socket operations. "'
nl|'\n'
string|'"If an incoming connection is idle for this number of "'
nl|'\n'
string|'"seconds it will be closed. A value of \'0\' means "'
nl|'\n'
string|'"wait forever."'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'api_paste_config_opt'
op|','
nl|'\n'
name|'wsgi_log_format_opt'
op|','
nl|'\n'
name|'secure_proxy_ssl_header_opt'
op|','
nl|'\n'
name|'ssl_ca_file_opt'
op|','
nl|'\n'
name|'ssl_cert_file_opt'
op|','
nl|'\n'
name|'ssl_key_file_opt'
op|','
nl|'\n'
name|'tcp_keepidle_opt'
op|','
nl|'\n'
name|'wsgi_default_pool_size_opt'
op|','
nl|'\n'
name|'max_header_line_opt'
op|','
nl|'\n'
name|'wsgi_keep_alive_opt'
op|','
nl|'\n'
name|'client_socket_timeout_opt'
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
name|'register_opts'
op|'('
name|'ALL_OPTS'
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
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
