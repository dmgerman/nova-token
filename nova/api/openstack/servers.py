begin_unit
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
name|'hashlib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'traceback'
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
name|'compute'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
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
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
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
string|"'server'"
op|')'
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
DECL|function|_translate_detail_keys
name|'def'
name|'_translate_detail_keys'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces into dictionary format, mapping everything to Rackspace-like\n    attributes for return"""'
newline|'\n'
name|'power_mapping'
op|'='
op|'{'
nl|'\n'
name|'None'
op|':'
string|"'build'"
op|','
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
name|'SUSPENDED'
op|':'
string|"'suspended'"
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'PAUSED'
op|':'
string|"'paused'"
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
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'FAILED'
op|':'
string|"'error'"
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
string|"'display_name'"
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
nl|'\n'
comment|'# grab single private fixed ip'
nl|'\n'
name|'private_ips'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ip/address'"
op|')'
newline|'\n'
name|'inst_dict'
op|'['
string|"'addresses'"
op|']'
op|'['
string|"'private'"
op|']'
op|'='
name|'private_ips'
newline|'\n'
nl|'\n'
comment|'# grab all public floating ips'
nl|'\n'
name|'public_ips'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
op|'('
name|'inst'
op|','
string|"'fixed_ip/floating_ips/address'"
op|')'
newline|'\n'
name|'inst_dict'
op|'['
string|"'addresses'"
op|']'
op|'['
string|"'public'"
op|']'
op|'='
name|'public_ips'
newline|'\n'
nl|'\n'
comment|'# Return the metadata as a dictionary'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'inst'
op|'['
string|"'metadata'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'['
name|'item'
op|'['
string|"'key'"
op|']'
op|']'
op|'='
name|'item'
op|'['
string|"'value'"
op|']'
newline|'\n'
dedent|''
name|'inst_dict'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'inst'
op|'['
string|"'host'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'inst_dict'
op|'['
string|"'hostId'"
op|']'
op|'='
name|'hashlib'
op|'.'
name|'sha224'
op|'('
name|'inst'
op|'['
string|"'host'"
op|']'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'server'
op|'='
name|'inst_dict'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_keys
dedent|''
name|'def'
name|'_translate_keys'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Coerces into dictionary format, excluding all model attributes\n    save for id and name """'
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
string|"'display_name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
string|'""" The Server API controller for the OpenStack API """'
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
op|']'
op|'}'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'image_service'
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
name|'_translate_keys'
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
name|'_translate_detail_keys'
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
string|'"""Returns a list of servers for a given user.\n\n        entity_maker - either _translate_detail_keys or _translate_keys\n        """'
newline|'\n'
name|'instance_list'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
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
name|'dict'
op|'('
name|'servers'
op|'='
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
name|'return'
name|'_translate_detail_keys'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
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
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'key_pairs'
op|'='
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'.'
name|'get_key_pairs'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'key_pairs'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|'"No keypairs defined"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'key_pair'
op|'='
name|'key_pairs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'common'
op|'.'
name|'get_image_id_from_image_hash'
op|'('
name|'self'
op|'.'
name|'_image_service'
op|','
nl|'\n'
name|'context'
op|','
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageId'"
op|']'
op|')'
newline|'\n'
name|'kernel_id'
op|','
name|'ramdisk_id'
op|'='
name|'self'
op|'.'
name|'_get_kernel_ramdisk_from_image'
op|'('
nl|'\n'
name|'req'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Metadata is a list, not a Dictionary, because we allow duplicate keys'
nl|'\n'
comment|"# (even though JSON can't encode this)"
nl|'\n'
comment|'# In future, we may not allow duplicate keys.'
nl|'\n'
comment|'# However, the CloudServers API is not definitive on this front,'
nl|'\n'
comment|'#  and we want to be compatible.'
nl|'\n'
name|'metadata'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'env'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'.'
name|'append'
op|'('
op|'{'
string|"'key'"
op|':'
name|'k'
op|','
string|"'value'"
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'flavorId'"
op|']'
op|')'
op|','
nl|'\n'
name|'image_id'
op|','
nl|'\n'
name|'kernel_id'
op|'='
name|'kernel_id'
op|','
nl|'\n'
name|'ramdisk_id'
op|'='
name|'ramdisk_id'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'display_description'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_pair'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'onset_files'
op|'='
name|'env'
op|'.'
name|'get'
op|'('
string|"'onset_files'"
op|','
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'_translate_keys'
op|'('
name|'instances'
op|'['
number|'0'
op|']'
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
name|'if'
name|'not'
name|'inst_dict'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'update_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'adminPass'"
name|'in'
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'update_dict'
op|'['
string|"'admin_pass'"
op|']'
op|'='
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'adminPass'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'set_admin_password'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'TimeoutException'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'exc'
op|'.'
name|'HTTPRequestTimeout'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
string|"'name'"
name|'in'
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'update_dict'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'inst_dict'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'update'
op|'('
name|'ctxt'
op|','
name|'id'
op|','
op|'**'
name|'update_dict'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
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
string|'""" Multi-purpose method used to reboot, rebuild, or\n        resize a server """'
newline|'\n'
nl|'\n'
name|'actions'
op|'='
op|'{'
nl|'\n'
string|"'reboot'"
op|':'
name|'self'
op|'.'
name|'_action_reboot'
op|','
nl|'\n'
string|"'resize'"
op|':'
name|'self'
op|'.'
name|'_action_resize'
op|','
nl|'\n'
string|"'confirmResize'"
op|':'
name|'self'
op|'.'
name|'_action_confirm_resize'
op|','
nl|'\n'
string|"'revertResize'"
op|':'
name|'self'
op|'.'
name|'_action_revert_resize'
op|','
nl|'\n'
string|"'rebuild'"
op|':'
name|'self'
op|'.'
name|'_action_rebuild'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
name|'for'
name|'key'
name|'in'
name|'actions'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'input_dict'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'actions'
op|'['
name|'key'
op|']'
op|'('
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_action_confirm_resize
dedent|''
name|'def'
name|'_action_confirm_resize'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'confirm_resize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Error in confirm-resize %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
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
DECL|member|_action_revert_resize
dedent|''
name|'def'
name|'_action_revert_resize'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'revert_resize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Error in revert-resize %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_action_rebuild
dedent|''
name|'def'
name|'_action_rebuild'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_action_resize
dedent|''
name|'def'
name|'_action_resize'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Resizes a given instance to the flavor size requested """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'resize'"
name|'in'
name|'input_dict'
name|'and'
string|"'flavorId'"
name|'in'
name|'input_dict'
op|'['
string|"'resize'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'flavor_id'
op|'='
name|'input_dict'
op|'['
string|"'resize'"
op|']'
op|'['
string|"'flavorId'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'resize'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|','
nl|'\n'
name|'flavor_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Missing arguments for resize"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Error in resize %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_action_reboot
dedent|''
name|'def'
name|'_action_reboot'
op|'('
name|'self'
op|','
name|'input_dict'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# TODO(gundlach): pass reboot_type, support soft reboot in'
nl|'\n'
comment|'# virt driver'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'reboot'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|lock
dedent|''
name|'def'
name|'lock'
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
string|'"""\n        lock the instance with id\n        admin only operation\n\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'lock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::lock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unlock
dedent|''
name|'def'
name|'unlock'
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
string|'"""\n        unlock the instance with id\n        admin only operation\n\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unlock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::unlock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_lock
dedent|''
name|'def'
name|'get_lock'
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
string|'"""\n        return the boolean state of (instance with id)\'s lock\n\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_lock'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::get_lock %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_network
dedent|''
name|'def'
name|'reset_network'
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
string|'"""\n        Reset networking on an instance (admin only).\n\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'reset_network'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::reset_network %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_network_info
dedent|''
name|'def'
name|'inject_network_info'
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
string|'"""\n        Inject network info for an instance (admin only).\n\n        """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'inject_network_info'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::inject_network_info %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
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
string|'""" Permit Admins to Pause the server. """'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'pause'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::pause %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
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
string|'""" Permit Admins to Unpause the server. """'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unpause'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Compute.api::unpause %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
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
string|'"""permit admins to suspend the server"""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'suspend'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"compute.api::suspend %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
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
string|'"""permit admins to resume the server from suspend"""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'resume'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'readable'
op|'='
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"compute.api::resume %s"'
op|')'
op|','
name|'readable'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_ajax_console
dedent|''
name|'def'
name|'get_ajax_console'
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
string|'""" Returns a url to an instance\'s ajaxterm console. """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_ajax_console'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
nl|'\n'
name|'int'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'exc'
op|'.'
name|'HTTPAccepted'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|diagnostics
dedent|''
name|'def'
name|'diagnostics'
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
string|'"""Permit Admins to retrieve server diagnostics."""'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_diagnostics'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|actions
dedent|''
name|'def'
name|'actions'
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
string|'"""Permit Admins to retrieve server actions."""'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'items'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_actions'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
name|'actions'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# TODO(jk0): Do not do pre-serialization here once the default'
nl|'\n'
comment|'# serializer is updated'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'actions'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
nl|'\n'
name|'created_at'
op|'='
name|'str'
op|'('
name|'item'
op|'.'
name|'created_at'
op|')'
op|','
nl|'\n'
name|'action'
op|'='
name|'item'
op|'.'
name|'action'
op|','
nl|'\n'
name|'error'
op|'='
name|'item'
op|'.'
name|'error'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'actions'
op|'='
name|'actions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_kernel_ramdisk_from_image
dedent|''
name|'def'
name|'_get_kernel_ramdisk_from_image'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrevies kernel and ramdisk IDs from Glance\n\n        Only \'machine\' (ami) type use kernel and ramdisk outside of the\n        image.\n        """'
newline|'\n'
comment|"# FIXME(sirp): Since we're retrieving the kernel_id from an"
nl|'\n'
comment|'# image_property, this means only Glance is supported.'
nl|'\n'
comment|'# The BaseImageService needs to expose a consistent way of accessing'
nl|'\n'
comment|'# kernel_id and ramdisk_id'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'show'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'image'
op|'['
string|"'status'"
op|']'
op|'!='
string|"'active'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Cannot build from image %(image_id)s, status not active"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'image'
op|'['
string|"'type'"
op|']'
op|'!='
string|"'machine'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kernel_id'
op|'='
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'kernel_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Kernel not found for image %(image_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk_id'
op|'='
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'ramdisk_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Ramdisk not found for image %(image_id)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'kernel_id'
op|','
name|'ramdisk_id'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
