begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2011 Piston Cloud Computing, Inc.'
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
nl|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'addresses'
name|'as'
name|'views_addresses'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'flavors'
name|'as'
name|'views_flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'views_images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'common'
op|'.'
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model a server API response as a python dictionary."""'
newline|'\n'
nl|'\n'
DECL|variable|_collection_name
name|'_collection_name'
op|'='
string|'"servers"'
newline|'\n'
nl|'\n'
DECL|variable|_progress_statuses
name|'_progress_statuses'
op|'='
op|'('
nl|'\n'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"BUILD"'
op|','
nl|'\n'
string|'"REBUILD"'
op|','
nl|'\n'
string|'"RESIZE"'
op|','
nl|'\n'
string|'"VERIFY_RESIZE"'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_fault_statuses
name|'_fault_statuses'
op|'='
op|'('
nl|'\n'
string|'"ERROR"'
op|','
nl|'\n'
op|')'
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
string|'"""Initialize view builder."""'
newline|'\n'
name|'super'
op|'('
name|'ViewBuilder'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_address_builder'
op|'='
name|'views_addresses'
op|'.'
name|'ViewBuilder'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_flavor_builder'
op|'='
name|'views_flavors'
op|'.'
name|'ViewBuilder'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_builder'
op|'='
name|'views_images'
op|'.'
name|'ViewBuilder'
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
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""View that should be returned when an instance is created."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|basic
dedent|''
name|'def'
name|'basic'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generic, non-detailed view of an instance."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'instance'
op|'['
string|'"display_name"'
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detailed view of a single instance."""'
newline|'\n'
name|'ip_v4'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v4'"
op|')'
newline|'\n'
name|'ip_v6'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v6'"
op|')'
newline|'\n'
name|'server'
op|'='
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'instance'
op|'['
string|'"display_name"'
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'self'
op|'.'
name|'_get_vm_state'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|'"tenant_id"'
op|':'
name|'instance'
op|'.'
name|'get'
op|'('
string|'"project_id"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"user_id"'
op|':'
name|'instance'
op|'.'
name|'get'
op|'('
string|'"user_id"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"metadata"'
op|':'
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|'"hostId"'
op|':'
name|'self'
op|'.'
name|'_get_host_id'
op|'('
name|'instance'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"image"'
op|':'
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'self'
op|'.'
name|'_get_flavor'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'instance'
op|'['
string|'"created_at"'
op|']'
op|')'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'instance'
op|'['
string|'"updated_at"'
op|']'
op|')'
op|','
nl|'\n'
string|'"addresses"'
op|':'
name|'self'
op|'.'
name|'_get_addresses'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"accessIPv4"'
op|':'
name|'str'
op|'('
name|'ip_v4'
op|')'
name|'if'
name|'ip_v4'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|','
nl|'\n'
string|'"accessIPv6"'
op|':'
name|'str'
op|'('
name|'ip_v6'
op|')'
name|'if'
name|'ip_v6'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"status"'
op|']'
name|'in'
name|'self'
op|'.'
name|'_fault_statuses'
op|':'
newline|'\n'
indent|'            '
name|'_inst_fault'
op|'='
name|'self'
op|'.'
name|'_get_fault'
op|'('
name|'request'
op|','
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'_inst_fault'
op|':'
newline|'\n'
indent|'                '
name|'server'
op|'['
string|"'server'"
op|']'
op|'['
string|"'fault'"
op|']'
op|'='
name|'_inst_fault'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"status"'
op|']'
name|'in'
name|'self'
op|'.'
name|'_progress_statuses'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"progress"'
op|']'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|'"progress"'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Show a list of servers without many details."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_list_view'
op|'('
name|'self'
op|'.'
name|'basic'
op|','
name|'request'
op|','
name|'instances'
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
name|'request'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detailed view of a list of instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_list_view'
op|'('
name|'self'
op|'.'
name|'show'
op|','
name|'request'
op|','
name|'instances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_list_view
dedent|''
name|'def'
name|'_list_view'
op|'('
name|'self'
op|','
name|'func'
op|','
name|'request'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provide a view for a list of servers."""'
newline|'\n'
name|'server_list'
op|'='
op|'['
name|'func'
op|'('
name|'request'
op|','
name|'server'
op|')'
op|'['
string|'"server"'
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'servers_links'
op|'='
name|'self'
op|'.'
name|'_get_collection_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'servers'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
newline|'\n'
name|'servers_dict'
op|'='
name|'dict'
op|'('
name|'servers'
op|'='
name|'server_list'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'servers_links'
op|':'
newline|'\n'
indent|'            '
name|'servers_dict'
op|'['
string|'"servers_links"'
op|']'
op|'='
name|'servers_links'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'servers_dict'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_metadata
name|'def'
name|'_get_metadata'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# FIXME(danms): Transitional support for objects'
nl|'\n'
indent|'        '
name|'metadata'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'instance_obj'
op|'.'
name|'Instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'metadata'
name|'or'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'instance_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_vm_state
name|'def'
name|'_get_vm_state'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'common'
op|'.'
name|'status_from_state'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|'"vm_state"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'get'
op|'('
string|'"task_state"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_host_id
name|'def'
name|'_get_host_id'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
newline|'\n'
name|'project'
op|'='
name|'str'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|'"project_id"'
op|')'
op|')'
newline|'\n'
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'sha_hash'
op|'='
name|'hashlib'
op|'.'
name|'sha224'
op|'('
name|'project'
op|'+'
name|'host'
op|')'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'return'
name|'sha_hash'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_addresses
dedent|''
dedent|''
name|'def'
name|'_get_addresses'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'networks'
op|'='
name|'common'
op|'.'
name|'get_networks_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_address_builder'
op|'.'
name|'index'
op|'('
name|'networks'
op|')'
op|'['
string|'"addresses"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_image
dedent|''
name|'def'
name|'_get_image'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_ref'
op|'='
name|'instance'
op|'['
string|'"image_ref"'
op|']'
newline|'\n'
name|'if'
name|'image_ref'
op|':'
newline|'\n'
indent|'            '
name|'image_id'
op|'='
name|'str'
op|'('
name|'common'
op|'.'
name|'get_id_from_href'
op|'('
name|'image_ref'
op|')'
op|')'
newline|'\n'
name|'bookmark'
op|'='
name|'self'
op|'.'
name|'_image_builder'
op|'.'
name|'_get_bookmark_link'
op|'('
name|'request'
op|','
nl|'\n'
name|'image_id'
op|','
nl|'\n'
string|'"images"'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image_id'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'bookmark'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'""'
newline|'\n'
nl|'\n'
DECL|member|_get_flavor
dedent|''
dedent|''
name|'def'
name|'_get_flavor'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Instance has had its instance_type removed "'
nl|'\n'
string|'"from the DB"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'flavor_id'
op|'='
name|'instance_type'
op|'['
string|'"flavorid"'
op|']'
newline|'\n'
name|'flavor_bookmark'
op|'='
name|'self'
op|'.'
name|'_flavor_builder'
op|'.'
name|'_get_bookmark_link'
op|'('
name|'request'
op|','
nl|'\n'
name|'flavor_id'
op|','
nl|'\n'
string|'"flavors"'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'str'
op|'('
name|'flavor_id'
op|')'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'flavor_bookmark'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_fault
dedent|''
name|'def'
name|'_get_fault'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# This can result in a lazy load of the fault information'
nl|'\n'
indent|'        '
name|'fault'
op|'='
name|'instance'
op|'.'
name|'fault'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'fault'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'fault_dict'
op|'='
op|'{'
nl|'\n'
string|'"code"'
op|':'
name|'fault'
op|'['
string|'"code"'
op|']'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'fault'
op|'['
string|'"created_at"'
op|']'
op|')'
op|','
nl|'\n'
string|'"message"'
op|':'
name|'fault'
op|'['
string|'"message"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'fault'
op|'.'
name|'get'
op|'('
string|"'details'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'is_admin'
op|'='
name|'False'
newline|'\n'
name|'context'
op|'='
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'if'
name|'context'
op|':'
newline|'\n'
indent|'                '
name|'is_admin'
op|'='
name|'getattr'
op|'('
name|'context'
op|','
string|"'is_admin'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'is_admin'
name|'or'
name|'fault'
op|'['
string|"'code'"
op|']'
op|'!='
number|'500'
op|':'
newline|'\n'
indent|'                '
name|'fault_dict'
op|'['
string|"'details'"
op|']'
op|'='
name|'fault'
op|'['
string|'"details"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'fault_dict'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV3
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV3'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Model a server V3 API response as a python dictionary."""'
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
string|'"""Initialize view builder."""'
newline|'\n'
name|'super'
op|'('
name|'ViewBuilderV3'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_address_builder'
op|'='
name|'views_addresses'
op|'.'
name|'ViewBuilderV3'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_builder'
op|'='
name|'views_images'
op|'.'
name|'ViewBuilderV3'
op|'('
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
name|'request'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detailed view of a single instance."""'
newline|'\n'
name|'ip_v4'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v4'"
op|')'
newline|'\n'
name|'ip_v6'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'access_ip_v6'"
op|')'
newline|'\n'
name|'server'
op|'='
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'instance'
op|'['
string|'"display_name"'
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'self'
op|'.'
name|'_get_vm_state'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|'"tenant_id"'
op|':'
name|'instance'
op|'.'
name|'get'
op|'('
string|'"project_id"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"user_id"'
op|':'
name|'instance'
op|'.'
name|'get'
op|'('
string|'"user_id"'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"metadata"'
op|':'
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|'"host_id"'
op|':'
name|'self'
op|'.'
name|'_get_host_id'
op|'('
name|'instance'
op|')'
name|'or'
string|'""'
op|','
nl|'\n'
string|'"image"'
op|':'
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"flavor"'
op|':'
name|'self'
op|'.'
name|'_get_flavor'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'instance'
op|'['
string|'"created_at"'
op|']'
op|')'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'instance'
op|'['
string|'"updated_at"'
op|']'
op|')'
op|','
nl|'\n'
string|'"addresses"'
op|':'
name|'self'
op|'.'
name|'_get_addresses'
op|'('
name|'request'
op|','
name|'instance'
op|')'
op|','
nl|'\n'
string|'"access_ip_v4"'
op|':'
name|'str'
op|'('
name|'ip_v4'
op|')'
name|'if'
name|'ip_v4'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|','
nl|'\n'
string|'"access_ip_v6"'
op|':'
name|'str'
op|'('
name|'ip_v6'
op|')'
name|'if'
name|'ip_v6'
name|'is'
name|'not'
name|'None'
name|'else'
string|"''"
op|','
nl|'\n'
string|'"links"'
op|':'
name|'self'
op|'.'
name|'_get_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"status"'
op|']'
name|'in'
name|'self'
op|'.'
name|'_fault_statuses'
op|':'
newline|'\n'
indent|'            '
name|'_inst_fault'
op|'='
name|'self'
op|'.'
name|'_get_fault'
op|'('
name|'request'
op|','
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'_inst_fault'
op|':'
newline|'\n'
indent|'                '
name|'server'
op|'['
string|"'server'"
op|']'
op|'['
string|"'fault'"
op|']'
op|'='
name|'_inst_fault'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"status"'
op|']'
name|'in'
name|'self'
op|'.'
name|'_progress_statuses'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'['
string|'"server"'
op|']'
op|'['
string|'"progress"'
op|']'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|'"progress"'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
