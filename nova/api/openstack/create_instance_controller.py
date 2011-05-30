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
name|'re'
newline|'\n'
name|'from'
name|'urlparse'
name|'import'
name|'urlparse'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
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
name|'quota'
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
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.create_instance_controller'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OpenstackCreateInstanceController
name|'class'
name|'OpenstackCreateInstanceController'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This is the base class for OS API Controllers that\n    are capable of creating instances (currently Servers and Zones).\n\n    Once we stabilize the Zones portion of the API we may be able\n    to move this code back into servers.py\n    """'
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
string|'"""We need the image service to create an instance."""'
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
name|'OpenstackCreateInstanceController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'create_method'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new server for the given user. The approach\n        used depends on the create_method. For example, the standard\n        POST /server call uses compute.api.create(), while \n        POST /zones/server uses compute.api.create_all_at_once().\n\n        The problem is, both approaches return different values (i.e.\n        [instance dicts] vs. reservation_id). So the handling of the\n        return type from this method is left to the caller. \n        """'
newline|'\n'
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize_create'
op|'('
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
nl|'\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'_get_server_admin_password'
op|'('
name|'env'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'key_name'
op|'='
name|'None'
newline|'\n'
name|'key_data'
op|'='
name|'None'
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
name|'key_pairs'
op|':'
newline|'\n'
indent|'            '
name|'key_pair'
op|'='
name|'key_pairs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'key_name'
op|'='
name|'key_pair'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'requested_image_id'
op|'='
name|'self'
op|'.'
name|'_image_id_from_req_data'
op|'('
name|'env'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'requested_image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Can not find requested image"'
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
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'personality'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'personality'"
op|')'
newline|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'personality'
op|':'
newline|'\n'
indent|'            '
name|'injected_files'
op|'='
name|'self'
op|'.'
name|'_get_injected_files'
op|'('
name|'personality'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'flavor_id'
op|'='
name|'self'
op|'.'
name|'_flavor_id_from_req_data'
op|'('
name|'env'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
string|"'name'"
name|'in'
name|'env'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server name is not defined"'
op|')'
newline|'\n'
name|'return'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'zone_blob'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|')'
newline|'\n'
name|'reservation_id'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'reservation_id'"
op|')'
newline|'\n'
name|'name'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_validate_server_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'name'
op|'='
name|'name'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
newline|'\n'
name|'extra_values'
op|'='
op|'{'
nl|'\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'requested_image_id'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'password'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'extra_values'
op|','
nl|'\n'
name|'create_method'
op|'('
name|'context'
op|','
nl|'\n'
name|'inst_type'
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
name|'name'
op|','
nl|'\n'
name|'display_description'
op|'='
name|'name'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'key_name'
op|','
nl|'\n'
name|'key_data'
op|'='
name|'key_data'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'env'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'password'
op|','
nl|'\n'
name|'zone_blob'
op|'='
name|'zone_blob'
op|','
nl|'\n'
name|'reservation_id'
op|'='
name|'reservation_id'
nl|'\n'
op|')'
nl|'\n'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'quota'
op|'.'
name|'QuotaError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_handle_quota_error'
op|'('
name|'error'
op|')'
newline|'\n'
nl|'\n'
comment|'# Let the caller deal with unhandled exceptions.'
nl|'\n'
nl|'\n'
DECL|member|_handle_quota_error
dedent|''
dedent|''
name|'def'
name|'_handle_quota_error'
op|'('
name|'self'
op|','
name|'error'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Reraise quota errors as api-specific http exceptions\n        """'
newline|'\n'
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFileLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file limit exceeded"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFilePathLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file path too long"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'error'
op|'.'
name|'code'
op|'=='
string|'"OnsetFileContentLimitExceeded"'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Personality file content too long"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
comment|'# if the original error is okay, just reraise it'
nl|'\n'
dedent|''
name|'raise'
name|'error'
newline|'\n'
nl|'\n'
DECL|member|_deserialize_create
dedent|''
name|'def'
name|'_deserialize_create'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deserialize a create request\n\n        Overrides normal behavior in the case of xml content\n        """'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'content_type'
op|'=='
string|'"application/xml"'
op|':'
newline|'\n'
indent|'            '
name|'deserializer'
op|'='
name|'ServerCreateRequestXMLDeserializer'
op|'('
op|')'
newline|'\n'
name|'return'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'request'
op|'.'
name|'body'
op|','
name|'request'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_server_admin_password
dedent|''
dedent|''
name|'def'
name|'_get_server_admin_password'
op|'('
name|'self'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Determine the admin password for a server on creation """'
newline|'\n'
name|'password'
op|'='
name|'server'
op|'.'
name|'get'
op|'('
string|"'adminPass'"
op|')'
newline|'\n'
name|'if'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'generate_password'
op|'('
number|'16'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'password'
op|','
name|'basestring'
op|')'
name|'or'
name|'password'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid adminPass"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'password'
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
string|'"""Fetch an image from the ImageService, then if present, return the\n        associated kernel and ramdisk image IDs.\n        """'
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
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
comment|'# NOTE(sirp): extracted to a separate method to aid unit-testing, the'
nl|'\n'
comment|"# new method doesn't need a request obj or an ImageService stub"
nl|'\n'
name|'kernel_id'
op|','
name|'ramdisk_id'
op|'='
name|'self'
op|'.'
name|'_do_get_kernel_ramdisk_from_image'
op|'('
nl|'\n'
name|'image_meta'
op|')'
newline|'\n'
name|'return'
name|'kernel_id'
op|','
name|'ramdisk_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_do_get_kernel_ramdisk_from_image
name|'def'
name|'_do_get_kernel_ramdisk_from_image'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Given an ImageService image_meta, return kernel and ramdisk image\n        ids if present.\n\n        This is only valid for `ami` style images.\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'image_meta'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'if'
name|'image_meta'
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
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"status is not active"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'container_format'"
op|')'
op|'!='
string|"'ami'"
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
name|'image_meta'
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
name|'KernelNotFoundForImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
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
name|'image_meta'
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
name|'RamdiskNotFoundForImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'kernel_id'
op|','
name|'ramdisk_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerCreateRequestXMLDeserializer
dedent|''
dedent|''
name|'class'
name|'ServerCreateRequestXMLDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Deserializer to handle xml-formatted server create requests.\n\n    Handles standard server attributes as well as optional metadata\n    and personality attributes\n    """'
newline|'\n'
nl|'\n'
DECL|member|deserialize
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deserialize an xml-formatted server create request"""'
newline|'\n'
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'string'
op|')'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_extract_server'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_extract_server
dedent|''
name|'def'
name|'_extract_server'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the server attribute of a parsed request"""'
newline|'\n'
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'server_node'
op|'='
name|'self'
op|'.'
name|'_find_first_child_named'
op|'('
name|'node'
op|','
string|"'server'"
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'['
string|'"name"'
op|','
string|'"imageId"'
op|','
string|'"flavorId"'
op|','
string|'"imageRef"'
op|','
string|'"flavorRef"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'server_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'server'
op|'['
name|'attr'
op|']'
op|'='
name|'server_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_extract_metadata'
op|'('
name|'server_node'
op|')'
newline|'\n'
name|'if'
name|'metadata'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'['
string|'"metadata"'
op|']'
op|'='
name|'metadata'
newline|'\n'
dedent|''
name|'personality'
op|'='
name|'self'
op|'.'
name|'_extract_personality'
op|'('
name|'server_node'
op|')'
newline|'\n'
name|'if'
name|'personality'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'['
string|'"personality"'
op|']'
op|'='
name|'personality'
newline|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|_extract_metadata
dedent|''
name|'def'
name|'_extract_metadata'
op|'('
name|'self'
op|','
name|'server_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the metadata attribute of a parsed request"""'
newline|'\n'
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'_find_first_child_named'
op|'('
name|'server_node'
op|','
string|'"metadata"'
op|')'
newline|'\n'
name|'if'
name|'metadata_node'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'meta_node'
name|'in'
name|'self'
op|'.'
name|'_find_children_named'
op|'('
name|'metadata_node'
op|','
string|'"meta"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
name|'meta_node'
op|'.'
name|'getAttribute'
op|'('
string|'"key"'
op|')'
newline|'\n'
name|'metadata'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'_extract_text'
op|'('
name|'meta_node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|member|_extract_personality
dedent|''
name|'def'
name|'_extract_personality'
op|'('
name|'self'
op|','
name|'server_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the personality attribute of a parsed request"""'
newline|'\n'
name|'personality_node'
op|'='
name|'self'
op|'.'
name|'_find_first_child_named'
op|'('
name|'server_node'
op|','
string|'"personality"'
op|')'
newline|'\n'
name|'if'
name|'personality_node'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'personality'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'file_node'
name|'in'
name|'self'
op|'.'
name|'_find_children_named'
op|'('
name|'personality_node'
op|','
string|'"file"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'file_node'
op|'.'
name|'hasAttribute'
op|'('
string|'"path"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'item'
op|'['
string|'"path"'
op|']'
op|'='
name|'file_node'
op|'.'
name|'getAttribute'
op|'('
string|'"path"'
op|')'
newline|'\n'
dedent|''
name|'item'
op|'['
string|'"contents"'
op|']'
op|'='
name|'self'
op|'.'
name|'_extract_text'
op|'('
name|'file_node'
op|')'
newline|'\n'
name|'personality'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'personality'
newline|'\n'
nl|'\n'
DECL|member|_find_first_child_named
dedent|''
name|'def'
name|'_find_first_child_named'
op|'('
name|'self'
op|','
name|'parent'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Search a nodes children for the first child with a given name"""'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'parent'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
op|'.'
name|'nodeName'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'node'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_find_children_named
dedent|''
name|'def'
name|'_find_children_named'
op|'('
name|'self'
op|','
name|'parent'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all of a nodes children who have the given name"""'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'parent'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'node'
op|'.'
name|'nodeName'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'node'
newline|'\n'
nl|'\n'
DECL|member|_extract_text
dedent|''
dedent|''
dedent|''
name|'def'
name|'_extract_text'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the text field contained by the given node"""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'node'
op|'.'
name|'childNodes'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'child'
op|'='
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'child'
op|'.'
name|'nodeType'
op|'=='
name|'child'
op|'.'
name|'TEXT_NODE'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'child'
op|'.'
name|'nodeValue'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|'""'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
