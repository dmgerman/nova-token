begin_unit
comment|'# Copyright 2010-2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'image'
name|'import'
name|'glance'
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
nl|'\n'
DECL|variable|_collection_name
indent|'    '
name|'_collection_name'
op|'='
string|'"images"'
newline|'\n'
nl|'\n'
DECL|member|basic
name|'def'
name|'basic'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary with basic image attributes."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"image"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'.'
name|'get'
op|'('
string|'"id"'
op|')'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'.'
name|'get'
op|'('
string|'"name"'
op|')'
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
name|'image'
op|'['
string|'"id"'
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
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary with image details."""'
newline|'\n'
name|'image_dict'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'.'
name|'get'
op|'('
string|'"id"'
op|')'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'.'
name|'get'
op|'('
string|'"name"'
op|')'
op|','
nl|'\n'
string|'"minRam"'
op|':'
name|'int'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"min_ram"'
op|')'
name|'or'
number|'0'
op|')'
op|','
nl|'\n'
string|'"minDisk"'
op|':'
name|'int'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"min_disk"'
op|')'
name|'or'
number|'0'
op|')'
op|','
nl|'\n'
string|'"metadata"'
op|':'
name|'image'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'self'
op|'.'
name|'_format_date'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"created_at"'
op|')'
op|')'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'self'
op|'.'
name|'_format_date'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"updated_at"'
op|')'
op|')'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'self'
op|'.'
name|'_get_status'
op|'('
name|'image'
op|')'
op|','
nl|'\n'
string|'"progress"'
op|':'
name|'self'
op|'.'
name|'_get_progress'
op|'('
name|'image'
op|')'
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
name|'image'
op|'['
string|'"id"'
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
newline|'\n'
nl|'\n'
name|'instance_uuid'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|'"instance_uuid"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance_uuid'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'server_ref'
op|'='
name|'self'
op|'.'
name|'_get_href_link'
op|'('
name|'request'
op|','
name|'instance_uuid'
op|','
string|"'servers'"
op|')'
newline|'\n'
name|'image_dict'
op|'['
string|'"server"'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'server_ref'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_bookmark_link'
op|'('
name|'request'
op|','
nl|'\n'
name|'instance_uuid'
op|','
nl|'\n'
string|"'servers'"
op|')'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'image_dict'
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
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Show a list of images with details."""'
newline|'\n'
name|'list_func'
op|'='
name|'self'
op|'.'
name|'show'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_list_view'
op|'('
name|'list_func'
op|','
name|'request'
op|','
name|'images'
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
name|'request'
op|','
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Show a list of images with basic attributes."""'
newline|'\n'
name|'list_func'
op|'='
name|'self'
op|'.'
name|'basic'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_list_view'
op|'('
name|'list_func'
op|','
name|'request'
op|','
name|'images'
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
name|'list_func'
op|','
name|'request'
op|','
name|'images'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provide a view for a list of images."""'
newline|'\n'
name|'image_list'
op|'='
op|'['
name|'list_func'
op|'('
name|'request'
op|','
name|'image'
op|')'
op|'['
string|'"image"'
op|']'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
newline|'\n'
name|'images_links'
op|'='
name|'self'
op|'.'
name|'_get_collection_links'
op|'('
name|'request'
op|','
nl|'\n'
name|'images'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|')'
newline|'\n'
name|'images_dict'
op|'='
name|'dict'
op|'('
name|'images'
op|'='
name|'image_list'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'images_links'
op|':'
newline|'\n'
indent|'            '
name|'images_dict'
op|'['
string|'"images_links"'
op|']'
op|'='
name|'images_links'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'images_dict'
newline|'\n'
nl|'\n'
DECL|member|_get_links
dedent|''
name|'def'
name|'_get_links'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|','
name|'collection_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of links for this image."""'
newline|'\n'
name|'return'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_href_link'
op|'('
name|'request'
op|','
name|'identifier'
op|','
name|'collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_bookmark_link'
op|'('
name|'request'
op|','
nl|'\n'
name|'identifier'
op|','
nl|'\n'
name|'collection_name'
op|')'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"alternate"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.image"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'self'
op|'.'
name|'_get_alternate_link'
op|'('
name|'request'
op|','
name|'identifier'
op|')'
op|','
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_alternate_link
dedent|''
name|'def'
name|'_get_alternate_link'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'identifier'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an alternate link for a specific image id."""'
newline|'\n'
name|'glance_url'
op|'='
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'glance_url'
op|'='
name|'self'
op|'.'
name|'_update_glance_link_prefix'
op|'('
name|'glance_url'
op|')'
newline|'\n'
name|'return'
string|"'/'"
op|'.'
name|'join'
op|'('
op|'['
name|'glance_url'
op|','
nl|'\n'
name|'request'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_collection_name'
op|','
nl|'\n'
name|'str'
op|'('
name|'identifier'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_format_date
name|'def'
name|'_format_date'
op|'('
name|'dt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return standard format for a given datetime object."""'
newline|'\n'
name|'if'
name|'dt'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'dt'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_status
name|'def'
name|'_get_status'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the status field to standardize format."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'active'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
string|"'queued'"
op|':'
string|"'SAVING'"
op|','
nl|'\n'
string|"'saving'"
op|':'
string|"'SAVING'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
string|"'DELETED'"
op|','
nl|'\n'
string|"'pending_delete'"
op|':'
string|"'DELETED'"
op|','
nl|'\n'
string|"'killed'"
op|':'
string|"'ERROR'"
op|','
nl|'\n'
op|'}'
op|'.'
name|'get'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"status"'
op|')'
op|','
string|"'UNKNOWN'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_progress
name|'def'
name|'_get_progress'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"queued"'
op|':'
number|'25'
op|','
nl|'\n'
string|'"saving"'
op|':'
number|'50'
op|','
nl|'\n'
string|'"active"'
op|':'
number|'100'
op|','
nl|'\n'
op|'}'
op|'.'
name|'get'
op|'('
name|'image'
op|'.'
name|'get'
op|'('
string|'"status"'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
