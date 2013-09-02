begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 2013 dotCloud, Inc.'
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
name|'functools'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
op|'.'
name|'green'
name|'import'
name|'httplib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|function|filter_data
name|'def'
name|'filter_data'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator that post-processes data returned by Docker to avoid any\n       surprises with different versions of Docker\n    """'
newline|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|'='
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_filter
name|'def'
name|'_filter'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'new_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'o'
name|'in'
name|'obj'
op|':'
newline|'\n'
indent|'                    '
name|'new_list'
op|'.'
name|'append'
op|'('
name|'_filter'
op|'('
name|'o'
op|')'
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'='
name|'new_list'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'obj'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'isinstance'
op|'('
name|'k'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'obj'
op|'['
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
op|']'
op|'='
name|'_filter'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'obj'
newline|'\n'
dedent|''
name|'return'
name|'_filter'
op|'('
name|'out'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Response
dedent|''
name|'class'
name|'Response'
op|'('
name|'object'
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
name|'http_response'
op|','
name|'skip_body'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_response'
op|'='
name|'http_response'
newline|'\n'
name|'self'
op|'.'
name|'code'
op|'='
name|'int'
op|'('
name|'http_response'
op|'.'
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'http_response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'json'
op|'='
name|'self'
op|'.'
name|'_decode_json'
op|'('
name|'self'
op|'.'
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_response'
op|'.'
name|'read'
op|'('
name|'size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'filter_data'
newline|'\n'
DECL|member|_decode_json
name|'def'
name|'_decode_json'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_response'
op|'.'
name|'getheader'
op|'('
string|"'Content-Type'"
op|')'
op|'!='
string|"'application/json'"
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'data'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnixHTTPConnection
dedent|''
dedent|''
dedent|''
name|'class'
name|'UnixHTTPConnection'
op|'('
name|'httplib'
op|'.'
name|'HTTPConnection'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
string|"'localhost'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unix_socket'
op|'='
string|"'/var/run/docker.sock'"
newline|'\n'
nl|'\n'
DECL|member|connect
dedent|''
name|'def'
name|'connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_UNIX'
op|','
name|'socket'
op|'.'
name|'SOCK_STREAM'
op|')'
newline|'\n'
name|'sock'
op|'.'
name|'connect'
op|'('
name|'self'
op|'.'
name|'unix_socket'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'sock'
op|'='
name|'sock'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DockerHTTPClient
dedent|''
dedent|''
name|'class'
name|'DockerHTTPClient'
op|'('
name|'object'
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
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_connection'
op|'='
name|'connection'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|connection
name|'def'
name|'connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_connection'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_connection'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'UnixHTTPConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|make_request
dedent|''
dedent|''
name|'def'
name|'make_request'
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
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'headers'"
name|'in'
name|'kwargs'
name|'and'
name|'kwargs'
op|'['
string|"'headers'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'='
name|'kwargs'
op|'['
string|"'headers'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'Content-Type'"
name|'not'
name|'in'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'kwargs'
op|'['
string|"'headers'"
op|']'
op|'='
name|'headers'
newline|'\n'
dedent|''
name|'conn'
op|'='
name|'self'
op|'.'
name|'connection'
newline|'\n'
name|'conn'
op|'.'
name|'request'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'Response'
op|'('
name|'conn'
op|'.'
name|'getresponse'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_containers
dedent|''
name|'def'
name|'list_containers'
op|'('
name|'self'
op|','
name|'_all'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.4/containers/ps?all={0}&limit=50'"
op|'.'
name|'format'
op|'('
name|'int'
op|'('
name|'_all'
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'resp'
op|'.'
name|'json'
newline|'\n'
nl|'\n'
DECL|member|create_container
dedent|''
name|'def'
name|'create_container'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
nl|'\n'
string|"'Hostname'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'User'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'Memory'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'MemorySwap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'AttachStdin'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStdout'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'AttachStderr'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'PortSpecs'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Tty'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'OpenStdin'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'StdinOnce'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'Env'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Cmd'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Dns'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Image'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'Volumes'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'VolumesFrom'"
op|':'
string|"''"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'data'
op|'.'
name|'update'
op|'('
name|'args'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
nl|'\n'
string|"'/v1.4/containers/create'"
op|','
nl|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'.'
name|'code'
op|'!='
number|'201'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'obj'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'data'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'obj'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'id'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'v'
newline|'\n'
nl|'\n'
DECL|member|start_container
dedent|''
dedent|''
dedent|''
name|'def'
name|'start_container'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
nl|'\n'
string|"'/v1.4/containers/{0}/start'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|','
nl|'\n'
name|'body'
op|'='
string|"'{}'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inspect_image
dedent|''
name|'def'
name|'inspect_image'
op|'('
name|'self'
op|','
name|'image_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.4/images/{0}/json'"
op|'.'
name|'format'
op|'('
name|'image_name'
op|')'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'.'
name|'code'
op|'!='
number|'200'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'resp'
op|'.'
name|'json'
newline|'\n'
nl|'\n'
DECL|member|inspect_container
dedent|''
name|'def'
name|'inspect_container'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.4/containers/{0}/json'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'.'
name|'code'
op|'!='
number|'200'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'resp'
op|'.'
name|'json'
newline|'\n'
nl|'\n'
DECL|member|stop_container
dedent|''
name|'def'
name|'stop_container'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeout'
op|'='
number|'5'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
nl|'\n'
string|"'/v1.4/containers/{0}/stop?t={1}'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|','
name|'timeout'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'204'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy_container
dedent|''
name|'def'
name|'destroy_container'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'DELETE'"
op|','
nl|'\n'
string|"'/v1.4/containers/{0}'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'204'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pull_repository
dedent|''
name|'def'
name|'pull_repository'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
name|'name'
op|'.'
name|'rsplit'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v1.4/images/create?fromImage={0}'"
op|'.'
name|'format'
op|'('
name|'parts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'url'
op|'+='
string|"'&tag={0}'"
op|'.'
name|'format'
op|'('
name|'parts'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
string|"'POST'"
op|','
name|'url'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'buf'
op|'='
name|'resp'
op|'.'
name|'read'
op|'('
number|'1024'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'buf'
op|':'
newline|'\n'
comment|'# Image pull completed'
nl|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|push_repository
dedent|''
name|'def'
name|'push_repository'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v1.4/images/{0}/push'"
op|'.'
name|'format'
op|'('
name|'name'
op|')'
newline|'\n'
comment|'# NOTE(samalba): docker requires the credentials fields even if'
nl|'\n'
comment|"# they're not needed here."
nl|'\n'
name|'body'
op|'='
op|'('
string|'\'{"username":"foo","password":"bar",\''
nl|'\n'
string|'\'"auth":"","email":"foo@bar.bar"}\''
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
string|"'POST'"
op|','
name|'url'
op|','
name|'headers'
op|'='
name|'headers'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'buf'
op|'='
name|'resp'
op|'.'
name|'read'
op|'('
number|'1024'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'buf'
op|':'
newline|'\n'
comment|'# Image push completed'
nl|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|commit_container
dedent|''
name|'def'
name|'commit_container'
op|'('
name|'self'
op|','
name|'container_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
name|'name'
op|'.'
name|'rsplit'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'url'
op|'='
string|"'/v1.4/commit?container={0}&repo={1}'"
op|'.'
name|'format'
op|'('
name|'container_id'
op|','
nl|'\n'
name|'parts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'url'
op|'+='
string|"'&tag={0}'"
op|'.'
name|'format'
op|'('
name|'parts'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
string|"'POST'"
op|','
name|'url'
op|')'
newline|'\n'
name|'return'
op|'('
name|'resp'
op|'.'
name|'code'
op|'=='
number|'201'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_container_logs
dedent|''
name|'def'
name|'get_container_logs'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'self'
op|'.'
name|'make_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
nl|'\n'
op|'('
string|"'/v1.4/containers/{0}/attach'"
nl|'\n'
string|"'?logs=1&stream=0&stdout=1&stderr=1'"
op|')'
op|'.'
name|'format'
op|'('
name|'container_id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'resp'
op|'.'
name|'code'
op|'!='
number|'200'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'resp'
op|'.'
name|'data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
