begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License'
nl|'\r\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\r\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'create_instance_helper'
name|'as'
name|'helper'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'servers'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|CreateInstanceHelperEx
name|'class'
name|'CreateInstanceHelperEx'
op|'('
name|'helper'
op|'.'
name|'CreateInstanceHelper'
op|')'
op|':'
newline|'\r\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'super'
op|'('
name|'CreateInstanceHelperEx'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'controller'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|create_instance
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|','
name|'create_method'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Creates a new server for the given user as per\r\n        the network information if it is provided\r\n        """'
newline|'\r\n'
name|'if'
name|'not'
name|'body'
op|':'
newline|'\r\n'
indent|'            '
name|'raise'
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
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\r\n'
nl|'\r\n'
name|'password'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_server_admin_password'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'key_name'
op|'='
name|'None'
newline|'\r\n'
name|'key_data'
op|'='
name|'None'
newline|'\r\n'
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
newline|'\r\n'
name|'if'
name|'key_pairs'
op|':'
newline|'\r\n'
indent|'            '
name|'key_pair'
op|'='
name|'key_pairs'
op|'['
number|'0'
op|']'
newline|'\r\n'
name|'key_name'
op|'='
name|'key_pair'
op|'['
string|"'name'"
op|']'
newline|'\r\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'image_href'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_image_ref_from_req_data'
op|'('
name|'body'
op|')'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'image_service'
op|','
name|'image_id'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_image_service'
op|'('
name|'image_href'
op|')'
newline|'\r\n'
name|'kernel_id'
op|','
name|'ramdisk_id'
op|'='
name|'self'
op|'.'
name|'_get_kernel_ramdisk_from_image'
op|'('
nl|'\r\n'
name|'req'
op|','
name|'image_id'
op|')'
newline|'\r\n'
name|'images'
op|'='
name|'set'
op|'('
op|'['
name|'str'
op|'('
name|'x'
op|'['
string|"'id'"
op|']'
op|')'
name|'for'
name|'x'
name|'in'
name|'image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|')'
op|']'
op|')'
newline|'\r\n'
name|'assert'
name|'str'
op|'('
name|'image_id'
op|')'
name|'in'
name|'images'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot find requested image %(image_href)s: %(e)s"'
op|'%'
nl|'\r\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'personality'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'personality'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'injected_files'
op|'='
op|'['
op|']'
newline|'\r\n'
name|'if'
name|'personality'
op|':'
newline|'\r\n'
indent|'            '
name|'injected_files'
op|'='
name|'self'
op|'.'
name|'_get_injected_files'
op|'('
name|'personality'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'requested_networks'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'networks'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'if'
name|'requested_networks'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\r\n'
indent|'            '
name|'requested_networks'
op|'='
name|'self'
op|'.'
name|'_get_requested_networks'
op|'('
nl|'\r\n'
name|'requested_networks'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'flavor_id'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_flavor_id_from_req_data'
op|'('
name|'body'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'if'
name|'not'
string|"'name'"
name|'in'
name|'body'
op|'['
string|"'server'"
op|']'
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Server name is not defined"'
op|')'
newline|'\r\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'zone_blob'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|')'
newline|'\r\n'
name|'name'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\r\n'
name|'self'
op|'.'
name|'_validate_server_name'
op|'('
name|'name'
op|')'
newline|'\r\n'
name|'name'
op|'='
name|'name'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
name|'reservation_id'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'reservation_id'"
op|')'
newline|'\r\n'
name|'min_count'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'min_count'"
op|')'
newline|'\r\n'
name|'max_count'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
string|"'max_count'"
op|')'
newline|'\r\n'
comment|'# min_count and max_count are optional.  If they exist, they come'
nl|'\r\n'
comment|"# in as strings.  We want to default 'min_count' to 1, and default"
nl|'\r\n'
comment|"# 'max_count' to be 'min_count'."
nl|'\r\n'
name|'min_count'
op|'='
name|'int'
op|'('
name|'min_count'
op|')'
name|'if'
name|'min_count'
name|'else'
number|'1'
newline|'\r\n'
name|'max_count'
op|'='
name|'int'
op|'('
name|'max_count'
op|')'
name|'if'
name|'max_count'
name|'else'
name|'min_count'
newline|'\r\n'
name|'if'
name|'min_count'
op|'>'
name|'max_count'
op|':'
newline|'\r\n'
indent|'            '
name|'min_count'
op|'='
name|'max_count'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
newline|'\r\n'
name|'extra_values'
op|'='
op|'{'
nl|'\r\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\r\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\r\n'
string|"'password'"
op|':'
name|'password'
op|'}'
newline|'\r\n'
nl|'\r\n'
name|'return'
op|'('
name|'extra_values'
op|','
nl|'\r\n'
name|'create_method'
op|'('
name|'context'
op|','
nl|'\r\n'
name|'inst_type'
op|','
nl|'\r\n'
name|'image_id'
op|','
nl|'\r\n'
name|'kernel_id'
op|'='
name|'kernel_id'
op|','
nl|'\r\n'
name|'ramdisk_id'
op|'='
name|'ramdisk_id'
op|','
nl|'\r\n'
name|'display_name'
op|'='
name|'name'
op|','
nl|'\r\n'
name|'display_description'
op|'='
name|'name'
op|','
nl|'\r\n'
name|'key_name'
op|'='
name|'key_name'
op|','
nl|'\r\n'
name|'key_data'
op|'='
name|'key_data'
op|','
nl|'\r\n'
name|'metadata'
op|'='
name|'body'
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
nl|'\r\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\r\n'
name|'admin_password'
op|'='
name|'password'
op|','
nl|'\r\n'
name|'zone_blob'
op|'='
name|'zone_blob'
op|','
nl|'\r\n'
name|'reservation_id'
op|'='
name|'reservation_id'
op|','
nl|'\r\n'
name|'min_count'
op|'='
name|'min_count'
op|','
nl|'\r\n'
name|'max_count'
op|'='
name|'max_count'
op|','
nl|'\r\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'quota'
op|'.'
name|'QuotaError'
name|'as'
name|'error'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'_handle_quota_error'
op|'('
name|'error'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotFound'
name|'as'
name|'error'
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Can not find requested image"'
op|')'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
name|'as'
name|'err'
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
string|'"%(err_type)s: %(err_msg)s"'
op|'%'
op|'{'
string|"'err_type'"
op|':'
name|'err'
op|'.'
name|'exc_type'
op|','
string|"'err_msg'"
op|':'
name|'err'
op|'.'
name|'value'
op|'}'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# Let the caller deal with unhandled exceptions.'
nl|'\r\n'
nl|'\r\n'
DECL|member|_validate_fixed_ip
dedent|''
dedent|''
name|'def'
name|'_validate_fixed_ip'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'value'
op|','
name|'basestring'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP is not a string or unicode"'
op|')'
newline|'\r\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'if'
name|'value'
op|'.'
name|'strip'
op|'('
op|')'
op|'=='
string|"''"
op|':'
newline|'\r\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fixed IP is an empty string"'
op|')'
newline|'\r\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|_get_requested_networks
dedent|''
dedent|''
name|'def'
name|'_get_requested_networks'
op|'('
name|'self'
op|','
name|'requested_networks'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Create a list of requested networks from the networks attribute\r\n        """'
newline|'\r\n'
name|'networks'
op|'='
op|'['
op|']'
newline|'\r\n'
name|'for'
name|'network'
name|'in'
name|'requested_networks'
op|':'
newline|'\r\n'
indent|'            '
name|'try'
op|':'
newline|'\r\n'
indent|'                '
name|'network_id'
op|'='
name|'network'
op|'['
string|"'id'"
op|']'
newline|'\r\n'
name|'network_id'
op|'='
name|'int'
op|'('
name|'network_id'
op|')'
newline|'\r\n'
comment|'#fixed IP address is optional'
nl|'\r\n'
comment|'#if the fixed IP address is not provided then'
nl|'\r\n'
comment|'#it will use one of the available IP address from the network'
nl|'\r\n'
name|'fixed_ip'
op|'='
name|'network'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|','
name|'None'
op|')'
newline|'\r\n'
name|'if'
name|'fixed_ip'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\r\n'
indent|'                    '
name|'self'
op|'.'
name|'_validate_fixed_ip'
op|'('
name|'fixed_ip'
op|')'
newline|'\r\n'
comment|'# check if the network id is already present in the list,'
nl|'\r\n'
comment|"# we don't want duplicate networks to be passed"
nl|'\r\n'
comment|'# at the boot time'
nl|'\r\n'
dedent|''
name|'for'
name|'id'
op|','
name|'ip'
name|'in'
name|'networks'
op|':'
newline|'\r\n'
indent|'                    '
name|'if'
name|'id'
op|'=='
name|'network_id'
op|':'
newline|'\r\n'
indent|'                        '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Duplicate networks (%s) are not allowed"'
op|')'
op|'%'
name|'network_id'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\r\n'
name|'explanation'
op|'='
name|'expl'
op|')'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
dedent|''
name|'networks'
op|'.'
name|'append'
op|'('
op|'('
name|'network_id'
op|','
name|'fixed_ip'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'KeyError'
name|'as'
name|'key'
op|':'
newline|'\r\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Bad network format: missing %s'"
op|')'
op|'%'
name|'key'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\r\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|'"Bad networks format: network id should "'
nl|'\r\n'
string|'"be integer (%s)"'
op|')'
op|'%'
name|'network_id'
newline|'\r\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\r\n'
indent|'                '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Bad networks format'"
op|')'
newline|'\r\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
dedent|''
name|'return'
name|'networks'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|CreateServerExtController
dedent|''
dedent|''
name|'class'
name|'CreateServerExtController'
op|'('
name|'servers'
op|'.'
name|'ControllerV11'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""This is the controller for the extended version\r\n    of the create server OS V1.1\r\n    """'
newline|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'super'
op|'('
name|'CreateServerExtController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'helper'
op|'='
name|'CreateInstanceHelperEx'
op|'('
name|'self'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|Createserverext
dedent|''
dedent|''
name|'class'
name|'Createserverext'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""The servers create ext\r\n\r\n    Exposes addFixedIp and removeFixedIp actions on servers.\r\n\r\n    """'
newline|'\r\n'
DECL|member|get_name
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"Createserverext"'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"os-servers-create-ext"'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"Extended support to the Create Server v1.1 API"'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_namespace
dedent|''
name|'def'
name|'get_namespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"http://docs.openstack.org/ext/createserverext/api/v1.1"'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_updated
dedent|''
name|'def'
name|'get_updated'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"2011-07-19T00:00:00+00:00"'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\r\n'
nl|'\r\n'
name|'headers_serializer'
op|'='
name|'servers'
op|'.'
name|'HeadersSerializer'
op|'('
op|')'
newline|'\r\n'
name|'metadata'
op|'='
name|'servers'
op|'.'
name|'_get_metadata'
op|'('
op|')'
newline|'\r\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\r\n'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\r\n'
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
op|','
nl|'\r\n'
op|'}'
newline|'\r\n'
nl|'\r\n'
name|'body_deserializers'
op|'='
op|'{'
nl|'\r\n'
string|"'application/xml'"
op|':'
name|'helper'
op|'.'
name|'ServerXMLDeserializer'
op|'('
op|')'
op|','
nl|'\r\n'
op|'}'
newline|'\r\n'
nl|'\r\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'body_serializers'
op|','
nl|'\r\n'
name|'headers_serializer'
op|')'
newline|'\r\n'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'RequestDeserializer'
op|'('
name|'body_deserializers'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-servers-create-ext'"
op|','
nl|'\r\n'
name|'controller'
op|'='
name|'CreateServerExtController'
op|'('
op|')'
op|','
nl|'\r\n'
name|'deserializer'
op|'='
name|'deserializer'
op|','
nl|'\r\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\r\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'resources'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
