begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'model'
name|'as'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'base'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|variable|entity_name
indent|'    '
name|'entity_name'
op|'='
string|"'servers'"
newline|'\n'
nl|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'inst'
name|'in'
name|'compute'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'all'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'.'
name|'append'
op|'('
name|'instance_details'
op|'('
name|'inst'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'kwargs'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'return'
name|'compute'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'kwargs'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'compute'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ServerNotFound'
op|'('
string|'"The requested server was not found"'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'self'
op|'.'
name|'build_server_instance'
op|'('
name|'kwargs'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
op|'{'
nl|'\n'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'inst'
op|'.'
name|'instance_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'kwargs'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'compute'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ServerNotFound'
op|'('
string|'"The requested server was not found"'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_server_instance
dedent|''
name|'def'
name|'build_server_instance'
op|'('
name|'self'
op|','
name|'env'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Build instance data structure and save it to the data store."""'
newline|'\n'
name|'reservation'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
newline|'\n'
name|'ltime'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'name'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'env'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'env'
op|'['
string|"'project'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
name|'reservation'
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
name|'ltime'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_ip'
op|'('
nl|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'mac'
op|'='
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'private_dns_name'"
op|']'
op|'='
name|'str'
op|'('
name|'address'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'bridge_name'"
op|']'
op|'='
name|'network'
op|'.'
name|'BridgedNetwork'
op|'.'
name|'get_network_for_project'
op|'('
nl|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'default'"
op|')'
op|'['
string|"'bridge_name'"
op|']'
newline|'\n'
comment|'# key_data, key_name, ami_launch_index'
nl|'\n'
comment|'# TODO(todd): key data or root password'
nl|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'inst'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
