begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nDatastore Model objects for Compute Instances, with\nInstanceDirectory manager.\n\n# Create a new instance?\n>>> InstDir = InstanceDirectory()\n>>> inst = InstDir.new()\n>>> inst.destroy()\nTrue\n>>> inst = InstDir[\'i-123\']\n>>> inst[\'ip\'] = "192.168.0.3"\n>>> inst[\'project_id\'] = "projectA"\n>>> inst.save()\nTrue\n\n>>> InstDir[\'i-123\']\n<Instance:i-123>\n>>> InstDir.all.next()\n<Instance:i-123>\n\n>>> inst.destroy()\nTrue\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'redis'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(todd): Implement this at the class level for Instance'
nl|'\n'
DECL|class|InstanceDirectory
name|'class'
name|'InstanceDirectory'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""an api for interacting with the global state of instances"""'
newline|'\n'
nl|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns an instance object for a given id"""'
newline|'\n'
name|'return'
name|'Instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'get'
op|'('
name|'item'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'datastore'
op|'.'
name|'absorb_connection_error'
newline|'\n'
DECL|member|by_project
name|'def'
name|'by_project'
op|'('
name|'self'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns a list of instance objects for a project"""'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
string|"'project:%s:instances'"
op|'%'
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'Instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|by_node
dedent|''
dedent|''
name|'def'
name|'by_node'
op|'('
name|'self'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns a list of instances for a node"""'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'self'
op|'.'
name|'all'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'['
string|"'node_name'"
op|']'
op|'=='
name|'node_id'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|by_ip
dedent|''
dedent|''
dedent|''
name|'def'
name|'by_ip'
op|'('
name|'self'
op|','
name|'ip_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns an instance object that is using the IP"""'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'self'
op|'.'
name|'all'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance'
op|'['
string|"'private_dns_name'"
op|']'
op|'=='
name|'ip_address'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'instance'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|by_volume
dedent|''
name|'def'
name|'by_volume'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns the instance a volume is attached to"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'datastore'
op|'.'
name|'absorb_connection_error'
newline|'\n'
DECL|member|exists
name|'def'
name|'exists'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sismember'
op|'('
string|"'instances'"
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
op|'@'
name|'datastore'
op|'.'
name|'absorb_connection_error'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns a list of all instances"""'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'smembers'
op|'('
string|"'instances'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'Instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|new
dedent|''
dedent|''
name|'def'
name|'new'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns an empty Instance object, with ID"""'
newline|'\n'
name|'instance_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'i'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Instance
dedent|''
dedent|''
name|'class'
name|'Instance'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around stored properties of an instance"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""loads an instance from the datastore if exists"""'
newline|'\n'
comment|'# set instance data before super call since it uses default_state'
nl|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'instance_id'
newline|'\n'
name|'super'
op|'('
name|'Instance'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'state'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'state_description'"
op|':'
string|"'pending'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'self'
op|'.'
name|'instance_id'
op|','
nl|'\n'
string|"'node_name'"
op|':'
string|"'unassigned'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'unassigned'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'unassigned'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|project
name|'def'
name|'project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'state'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'state'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'get'
op|'('
string|"'owner_id'"
op|','
string|"'unassigned'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|volumes
name|'def'
name|'volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns a list of attached volumes"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|reservation
name|'def'
name|'reservation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a reservation object"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call into superclass to save object, then save associations"""'
newline|'\n'
comment|"# NOTE(todd): doesn't track migration between projects/nodes,"
nl|'\n'
comment|'#             it just adds the first one'
nl|'\n'
name|'should_update_project'
op|'='
name|'self'
op|'.'
name|'is_new_record'
op|'('
op|')'
newline|'\n'
name|'should_update_node'
op|'='
name|'self'
op|'.'
name|'is_new_record'
op|'('
op|')'
newline|'\n'
name|'success'
op|'='
name|'super'
op|'('
name|'Instance'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'if'
name|'success'
name|'and'
name|'should_update_project'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'associate_with'
op|'('
string|'"project"'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'success'
name|'and'
name|'should_update_node'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'associate_with'
op|'('
string|'"node"'
op|','
name|'self'
op|'['
string|"'node_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy associations, then destroy the object"""'
newline|'\n'
name|'self'
op|'.'
name|'unassociate_with'
op|'('
string|'"project"'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unassociate_with'
op|'('
string|'"node"'
op|','
name|'self'
op|'['
string|"'node_name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'Instance'
op|','
name|'self'
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|Host
dedent|''
dedent|''
name|'class'
name|'Host'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Host is the machine where a Daemon is running."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'hostname'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""loads an instance from the datastore if exists"""'
newline|'\n'
comment|'# set instance data before super call since it uses default_state'
nl|'\n'
name|'self'
op|'.'
name|'hostname'
op|'='
name|'hostname'
newline|'\n'
name|'super'
op|'('
name|'Host'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|'"hostname"'
op|':'
name|'self'
op|'.'
name|'hostname'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'hostname'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Daemon
dedent|''
dedent|''
name|'class'
name|'Daemon'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Daemon is a job (compute, api, network, ...) that runs on a host."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host_or_combined'
op|','
name|'binpath'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""loads an instance from the datastore if exists"""'
newline|'\n'
comment|'# set instance data before super call since it uses default_state'
nl|'\n'
comment|'# since loading from datastore expects a combined key that'
nl|'\n'
comment|'# is equivilent to identifier, we need to expect that, while'
nl|'\n'
comment|'# maintaining meaningful semantics (2 arguments) when creating'
nl|'\n'
comment|'# from within other code like the bin/nova-* scripts'
nl|'\n'
name|'if'
name|'binpath'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hostname'
op|'='
name|'host_or_combined'
newline|'\n'
name|'self'
op|'.'
name|'binary'
op|'='
name|'binpath'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hostname'
op|','
name|'self'
op|'.'
name|'binary'
op|'='
name|'host_or_combined'
op|'.'
name|'split'
op|'('
string|'":"'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'Daemon'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|'"hostname"'
op|':'
name|'self'
op|'.'
name|'hostname'
op|','
nl|'\n'
string|'"binary"'
op|':'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s:%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'hostname'
op|','
name|'self'
op|'.'
name|'binary'
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call into superclass to save object, then save associations"""'
newline|'\n'
comment|'# NOTE(todd): this makes no attempt to destroy itsself,'
nl|'\n'
comment|'#             so after termination a record w/ old timestmap remains'
nl|'\n'
name|'success'
op|'='
name|'super'
op|'('
name|'Daemon'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'if'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'associate_with'
op|'('
string|'"host"'
op|','
name|'self'
op|'.'
name|'hostname'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy associations, then destroy the object"""'
newline|'\n'
name|'self'
op|'.'
name|'unassociate_with'
op|'('
string|'"host"'
op|','
name|'self'
op|'.'
name|'hostname'
op|')'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'Daemon'
op|','
name|'self'
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|heartbeat
dedent|''
name|'def'
name|'heartbeat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'['
string|"'updated_at'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|by_host
name|'def'
name|'by_host'
op|'('
name|'cls'
op|','
name|'hostname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'cls'
op|'.'
name|'associated_to'
op|'('
string|'"host"'
op|','
name|'hostname'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'x'
newline|'\n'
nl|'\n'
DECL|class|SessionToken
dedent|''
dedent|''
dedent|''
name|'class'
name|'SessionToken'
op|'('
name|'datastore'
op|'.'
name|'BasicModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This is a short-lived auth token that is passed through web requests"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session_token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'token'
op|'='
name|'session_token'
newline|'\n'
name|'super'
op|'('
name|'SessionToken'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|identifier
name|'def'
name|'identifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'token'
newline|'\n'
nl|'\n'
DECL|member|default_state
dedent|''
name|'def'
name|'default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'diff'
op|'='
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'hours'
op|'='
number|'1'
op|')'
newline|'\n'
name|'expires'
op|'='
name|'now'
op|'+'
name|'diff'
newline|'\n'
name|'return'
op|'{'
string|"'user'"
op|':'
name|'None'
op|','
string|"'session_type'"
op|':'
name|'None'
op|','
string|"'token'"
op|':'
name|'self'
op|'.'
name|'token'
op|','
nl|'\n'
string|"'expiry'"
op|':'
name|'expires'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call into superclass to save object, then save associations"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'['
string|"'user'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
string|'"SessionToken requires a User association"'
op|')'
newline|'\n'
dedent|''
name|'success'
op|'='
name|'super'
op|'('
name|'SessionToken'
op|','
name|'self'
op|')'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'if'
name|'success'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'associate_with'
op|'('
string|'"user"'
op|','
name|'self'
op|'['
string|"'user'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup
name|'def'
name|'lookup'
op|'('
name|'cls'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
name|'super'
op|'('
name|'SessionToken'
op|','
name|'cls'
op|')'
op|'.'
name|'lookup'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'expires_at'
op|'='
name|'utils'
op|'.'
name|'parse_isotime'
op|'('
name|'token'
op|'['
string|"'expiry'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'>='
name|'expires_at'
op|':'
newline|'\n'
indent|'                '
name|'token'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'token'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|generate
name|'def'
name|'generate'
op|'('
name|'cls'
op|','
name|'userid'
op|','
name|'session_type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""make a new token for the given user"""'
newline|'\n'
name|'token'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'while'
name|'cls'
op|'.'
name|'lookup'
op|'('
name|'token'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'token'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'='
name|'cls'
op|'('
name|'token'
op|')'
newline|'\n'
name|'instance'
op|'['
string|"'user'"
op|']'
op|'='
name|'userid'
newline|'\n'
name|'instance'
op|'['
string|"'session_type'"
op|']'
op|'='
name|'session_type'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|update_expiry
dedent|''
name|'def'
name|'update_expiry'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""updates the expirty attribute, but doesn\'t save"""'
newline|'\n'
name|'if'
name|'not'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'hours'"
op|']'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'time'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'diff'
op|'='
name|'datetime'
op|'.'
name|'timedelta'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'expires'
op|'='
name|'time'
op|'+'
name|'diff'
newline|'\n'
name|'self'
op|'['
string|"'expiry'"
op|']'
op|'='
name|'expires'
op|'.'
name|'strftime'
op|'('
name|'utils'
op|'.'
name|'TIME_FORMAT'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'doctest'
newline|'\n'
name|'doctest'
op|'.'
name|'testmod'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
