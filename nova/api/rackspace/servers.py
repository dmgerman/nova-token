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
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'_id_translator'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'service'
newline|'\n'
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
nl|'\n'
DECL|function|translator_instance
name|'def'
name|'translator_instance'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Helper method for initializing the image id translator """'
newline|'\n'
name|'service'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'service'
op|'.'
name|'ImageService'
op|'.'
name|'load'
op|'('
op|')'
newline|'\n'
name|'return'
name|'_id_translator'
op|'.'
name|'RackspaceAPIIdTranslator'
op|'('
nl|'\n'
string|'"image"'
op|','
name|'service'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_filter_params
dedent|''
name|'def'
name|'_filter_params'
op|'('
name|'inst_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Extracts all updatable parameters for a server update request """'
newline|'\n'
name|'keys'
op|'='
op|'['
string|"'name'"
op|','
string|"'adminPass'"
op|']'
newline|'\n'
name|'new_attrs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'inst_dict'
op|'.'
name|'has_key'
op|'('
name|'k'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_attrs'
op|'['
name|'k'
op|']'
op|'='
name|'inst_dict'
op|'['
name|'k'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'new_attrs'
newline|'\n'
nl|'\n'
DECL|function|_entity_list
dedent|''
name|'def'
name|'_entity_list'
op|'('
name|'entities'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces a list of servers into proper dictionary format """'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'servers'
op|'='
name|'entities'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_entity_detail
dedent|''
name|'def'
name|'_entity_detail'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Maps everything to Rackspace-like attributes for return"""'
newline|'\n'
name|'power_mapping'
op|'='
op|'{'
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|':'
string|"'build'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'BLOCKED'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'PAUSED'
op|':'
string|"'suspended'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTOFF'
op|':'
string|"'active'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'CRASHED'
op|':'
string|"'error'"
nl|'\n'
op|'}'
newline|'\n'
name|'inst_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'mapped_keys'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
string|"'state'"
op|','
name|'imageId'
op|'='
string|"'image_id'"
op|','
nl|'\n'
name|'flavorId'
op|'='
string|"'instance_type'"
op|','
name|'name'
op|'='
string|"'server_name'"
op|','
name|'id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'mapped_keys'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_dict'
op|'['
name|'k'
op|']'
op|'='
name|'inst'
op|'['
name|'v'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|'='
name|'power_mapping'
op|'['
name|'inst_dict'
op|'['
string|"'status'"
op|']'
op|']'
newline|'\n'
name|'inst_dict'
op|'['
string|"'addresses'"
op|']'
op|'='
name|'dict'
op|'('
name|'public'
op|'='
op|'['
op|']'
op|','
name|'private'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'inst_dict'
op|'['
string|"'metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
name|'return'
name|'dict'
op|'('
name|'server'
op|'='
name|'inst_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_entity_inst
dedent|''
name|'def'
name|'_entity_inst'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Filters all model attributes save for id and name """'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'inst'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'inst'
op|'['
string|"'server_name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" The Server API controller for the Openstack API """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'['
string|'"id"'
op|','
string|'"imageId"'
op|','
string|'"name"'
op|','
string|'"flavorId"'
op|','
string|'"hostId"'
op|','
nl|'\n'
string|'"status"'
op|','
string|'"progress"'
op|','
string|'"progress"'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'db_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'db_driver'
op|':'
newline|'\n'
indent|'            '
name|'db_driver'
op|'='
name|'FLAGS'
op|'.'
name|'db_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db_driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'db_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'Controller'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Returns a list of server names and ids for a given user """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_entity_inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Returns a list of server details for a given user """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_entity_detail'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of servers for a given user.\n\n        entity_maker - either _entity_detail or _entity_inst\n        """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_all_by_user'
op|'('
name|'None'
op|','
name|'user_id'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
op|'.'
name|'limited'
op|'('
name|'instance_list'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'inst'
op|')'
op|'['
string|"'server'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
name|'_entity_list'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Returns server details by server id """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get'
op|'('
name|'None'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'inst'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'inst'
op|'.'
name|'user_id'
op|'=='
name|'user_id'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_entity_detail'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
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
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Destroys a server """'
newline|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get'
op|'('
name|'None'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'instance'
name|'and'
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|'=='
name|'user_id'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_destroy'
op|'('
name|'None'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Creates a new server for a given user """'
newline|'\n'
name|'if'
name|'not'
name|'req'
op|'.'
name|'environ'
op|'.'
name|'has_key'
op|'('
string|"'inst_dict'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'inst'
op|'='
name|'self'
op|'.'
name|'_build_server_instance'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
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
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'_entity_inst'
op|'('
name|'inst'
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
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Updates the server name or password """'
newline|'\n'
name|'if'
name|'not'
name|'req'
op|'.'
name|'environ'
op|'.'
name|'has_key'
op|'('
string|"'inst_dict'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get'
op|'('
name|'None'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'attrs'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'get'
op|'('
string|"'model_attributes'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'attrs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_update'
op|'('
name|'None'
op|','
name|'id'
op|','
name|'_filter_params'
op|'('
name|'attrs'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPNoContent'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|action
dedent|''
name|'def'
name|'action'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" multi-purpose method used to reboot, rebuild, and \n        resize a server """'
newline|'\n'
name|'if'
name|'not'
name|'req'
op|'.'
name|'environ'
op|'.'
name|'has_key'
op|'('
string|"'inst_dict'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_server_instance
dedent|''
dedent|''
name|'def'
name|'_build_server_instance'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Build instance data structure and save it to the data store."""'
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
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'env'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'inst_dict'"
op|']'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
newline|'\n'
name|'opaque_id'
op|'='
name|'translator_instance'
op|'('
op|')'
op|'.'
name|'from_rs_id'
op|'('
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
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
string|"'server_name'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'opaque_id'
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
nl|'\n'
name|'user_id'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'['
string|"'user'"
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'user_id'
newline|'\n'
nl|'\n'
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
nl|'\n'
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
name|'reservation'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
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
nl|'\n'
name|'ref'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_create'
op|'('
name|'None'
op|','
name|'inst'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'id'"
op|']'
op|'='
name|'ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
