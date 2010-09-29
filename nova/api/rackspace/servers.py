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
name|'datetime'
newline|'\n'
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
name|'import'
name|'cloud'
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
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'wsgi'
name|'import'
name|'Serializer'
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
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'rs_network_manager'"
op|','
string|"'nova.network.manager.FlatManager'"
op|','
nl|'\n'
string|"'Networking for rackspace'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_instance_id_translator
name|'def'
name|'_instance_id_translator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Helper method for initializing an id translator for Rackspace instance\n    ids """'
newline|'\n'
name|'return'
name|'_id_translator'
op|'.'
name|'RackspaceAPIIdTranslator'
op|'('
string|'"instance"'
op|','
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_image_service
dedent|''
name|'def'
name|'_image_service'
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
op|'('
name|'service'
op|','
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
name|'dict'
op|'('
name|'name'
op|'='
string|"'name'"
op|','
name|'admin_pass'
op|'='
string|"'adminPass'"
op|')'
newline|'\n'
name|'new_attrs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'keys'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'inst_dict'
op|'.'
name|'has_key'
op|'('
name|'v'
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
name|'v'
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
name|'res'
op|'='
op|'['
name|'_entity_inst'
op|'('
name|'inst'
op|')'
op|'['
string|"'server'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'instance_list'
op|']'
newline|'\n'
name|'return'
name|'_entity_list'
op|'('
name|'res'
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
name|'res'
op|'='
op|'['
name|'_entity_detail'
op|'('
name|'inst'
op|')'
op|'['
string|"'server'"
op|']'
name|'for'
name|'inst'
name|'in'
nl|'\n'
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
name|'inst_id_trans'
op|'='
name|'_instance_id_translator'
op|'('
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'inst_id_trans'
op|'.'
name|'from_rs_id'
op|'('
name|'id'
op|')'
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
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_by_ec2_id'
op|'('
name|'None'
op|','
name|'inst_id'
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
name|'inst_id_trans'
op|'='
name|'_instance_id_translator'
op|'('
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'inst_id_trans'
op|'.'
name|'from_rs_id'
op|'('
name|'id'
op|')'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'instance_get_by_ec2_id'
op|'('
name|'None'
op|','
name|'inst_id'
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
nl|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'env'
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
comment|'#try:'
nl|'\n'
dedent|''
name|'inst'
op|'='
name|'self'
op|'.'
name|'_build_server_instance'
op|'('
name|'req'
op|','
name|'env'
op|')'
newline|'\n'
comment|'#except Exception, e:'
nl|'\n'
comment|'#    print e'
nl|'\n'
comment|'#    return exc.HTTPUnprocessableEntity()'
nl|'\n'
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
name|'inst_id_trans'
op|'='
name|'_instance_id_translator'
op|'('
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'inst_id_trans'
op|'.'
name|'from_rs_id'
op|'('
name|'id'
op|')'
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
nl|'\n'
name|'inst_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'inst_dict'
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
name|'instance_get_by_ec2_id'
op|'('
name|'None'
op|','
name|'inst_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
name|'or'
name|'instance'
op|'.'
name|'user_id'
op|'!='
name|'user_id'
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
nl|'\n'
name|'_filter_params'
op|'('
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|')'
op|')'
newline|'\n'
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
name|'input_dict'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'reboot_type'
op|'='
name|'input_dict'
op|'['
string|"'reboot'"
op|']'
op|'['
string|"'type'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'opaque_id'
op|'='
name|'_instance_id_translator'
op|'('
op|')'
op|'.'
name|'from_rsapi_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'cloud'
op|'.'
name|'reboot'
op|'('
name|'opaque_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_server_instance
dedent|''
name|'def'
name|'_build_server_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'env'
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
name|'inst_id_trans'
op|'='
name|'_instance_id_translator'
op|'('
op|')'
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
nl|'\n'
name|'instance_type'
op|','
name|'flavor'
op|'='
name|'None'
op|','
name|'None'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'['
string|"'flavorid'"
op|']'
op|'=='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'instance_type'
op|','
name|'flavor'
op|'='
name|'k'
op|','
name|'v'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'flavor'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|','
string|'"Flavor not found"'
newline|'\n'
nl|'\n'
dedent|''
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
nl|'\n'
name|'img_service'
op|','
name|'image_id_trans'
op|'='
name|'_image_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'opaque_image_id'
op|'='
name|'image_id_trans'
op|'.'
name|'to_rs_id'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'='
name|'img_service'
op|'.'
name|'show'
op|'('
name|'opaque_image_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|','
string|'"Image not found"'
newline|'\n'
nl|'\n'
dedent|''
name|'inst'
op|'['
string|"'server_name'"
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
name|'opaque_image_id'
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'user_id'
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
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'user_id'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'state_description'"
op|']'
op|'='
string|"'scheduling'"
newline|'\n'
name|'inst'
op|'['
string|"'kernel_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'kernelId'"
op|','
name|'FLAGS'
op|'.'
name|'default_kernel'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ramdisk_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'ramdiskId'"
op|','
name|'FLAGS'
op|'.'
name|'default_ramdisk'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(dietz) this may be ill advised'
nl|'\n'
name|'key_pair_ref'
op|'='
name|'self'
op|'.'
name|'db_driver'
op|'.'
name|'key_pair_get_all_by_user'
op|'('
nl|'\n'
name|'None'
op|','
name|'user_id'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'key_data'"
op|']'
op|'='
name|'key_pair_ref'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'key_name'"
op|']'
op|'='
name|'key_pair_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
comment|'#TODO(dietz) stolen from ec2 api, see TODO there'
nl|'\n'
name|'inst'
op|'['
string|"'security_group'"
op|']'
op|'='
string|"'default'"
newline|'\n'
nl|'\n'
comment|'# Flavor related attributes'
nl|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
name|'instance_type'
newline|'\n'
name|'inst'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'local_gb'"
op|']'
op|'='
name|'flavor'
op|'['
string|"'local_gb'"
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
name|'inst_id_trans'
op|'.'
name|'to_rs_id'
op|'('
name|'ref'
op|'.'
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
comment|'#self.network_manager = utils.import_object(FLAGS.rs_network_manager)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"#address = self.network_manager.allocate_fixed_ip( None, inst['id']) "
nl|'\n'
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
