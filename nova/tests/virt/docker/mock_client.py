begin_unit
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
name|'time'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MockClient
name|'class'
name|'MockClient'
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
name|'endpoint'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_containers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_fake_id
dedent|''
name|'def'
name|'_fake_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
op|'+'
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
nl|'\n'
DECL|member|is_daemon_running
dedent|''
name|'def'
name|'is_daemon_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'filter_data'
newline|'\n'
DECL|member|list_containers
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
name|'containers'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'container_id'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|'.'
name|'iterkeys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'containers'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|"'Status'"
op|':'
string|"'Exit 0'"
op|','
nl|'\n'
string|"'Created'"
op|':'
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'Image'"
op|':'
string|"'ubuntu:12.04'"
op|','
nl|'\n'
string|"'Ports'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'Command'"
op|':'
string|"'bash '"
op|','
nl|'\n'
string|"'Id'"
op|':'
name|'container_id'
nl|'\n'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'containers'
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
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
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
name|'None'
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
name|'container_id'
op|'='
name|'self'
op|'.'
name|'_fake_id'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'container_id'
op|','
nl|'\n'
string|"'running'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'config'"
op|':'
name|'args'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'container_id'
newline|'\n'
nl|'\n'
DECL|member|start_container
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
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
op|'['
string|"'running'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'filter_data'
newline|'\n'
DECL|member|inspect_image
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
name|'return'
op|'{'
string|"'container_config'"
op|':'
op|'{'
string|"'Cmd'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
op|'.'
name|'client'
op|'.'
name|'filter_data'
newline|'\n'
DECL|member|inspect_container
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
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'container'
op|'='
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
newline|'\n'
name|'info'
op|'='
op|'{'
nl|'\n'
string|"'Args'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'Config'"
op|':'
name|'container'
op|'['
string|"'config'"
op|']'
op|','
nl|'\n'
string|"'Created'"
op|':'
name|'str'
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'ID'"
op|':'
name|'container_id'
op|','
nl|'\n'
string|"'Image'"
op|':'
name|'self'
op|'.'
name|'_fake_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'NetworkSettings'"
op|':'
op|'{'
nl|'\n'
string|"'Bridge'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'Gateway'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'IPAddress'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'IPPrefixLen'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'PortMapping'"
op|':'
name|'None'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'Path'"
op|':'
string|"'bash'"
op|','
nl|'\n'
string|"'ResolvConfPath'"
op|':'
string|"'/etc/resolv.conf'"
op|','
nl|'\n'
string|"'State'"
op|':'
op|'{'
nl|'\n'
string|"'ExitCode'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'Ghost'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'Pid'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'Running'"
op|':'
name|'container'
op|'['
string|"'running'"
op|']'
op|','
nl|'\n'
string|"'StartedAt'"
op|':'
name|'str'
op|'('
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'SysInitPath'"
op|':'
string|"'/tmp/docker'"
op|','
nl|'\n'
string|"'Volumes'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'info'
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
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
op|'['
string|"'running'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|kill_container
dedent|''
name|'def'
name|'kill_container'
op|'('
name|'self'
op|','
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
op|'['
string|"'running'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'return'
name|'True'
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
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|"# Docker doesn't allow to destroy a running container."
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
op|'['
string|"'running'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
name|'self'
op|'.'
name|'_containers'
op|'['
name|'container_id'
op|']'
newline|'\n'
name|'return'
name|'True'
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
name|'return'
name|'True'
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
name|'return'
name|'True'
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
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
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
name|'if'
name|'container_id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_containers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
op|'['
nl|'\n'
string|"'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '"
op|','
nl|'\n'
string|"'Vivamus ornare mi sit amet orci feugiat, nec luctus magna '"
op|','
nl|'\n'
string|"'vehicula. Quisque diam nisl, dictum vitae pretium id, '"
op|','
nl|'\n'
string|"'consequat eget sapien. Ut vehicula tortor non ipsum '"
op|','
nl|'\n'
string|"'consectetur, at tincidunt elit posuere. In ut ligula leo. '"
op|','
nl|'\n'
string|"'Donec eleifend accumsan mi, in accumsan metus. Nullam nec '"
op|','
nl|'\n'
string|"'nulla eu risus vehicula porttitor. Sed purus ligula, '"
op|','
nl|'\n'
string|"'placerat nec metus a, imperdiet viverra turpis. Praesent '"
op|','
nl|'\n'
string|"'dapibus ornare massa. Nam ut hendrerit nunc. Interdum et '"
op|','
nl|'\n'
string|"'malesuada fames ac ante ipsum primis in faucibus. '"
op|','
nl|'\n'
string|"'Fusce nec pellentesque nisl.'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
