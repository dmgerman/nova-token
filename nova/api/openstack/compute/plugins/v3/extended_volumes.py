begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#   Copyright 2013 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
string|'"""The Extended Volumes API extension."""'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
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
name|'uuidutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-extended-volumes"'
newline|'\n'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_attach
name|'authorize_attach'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:attach'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
DECL|variable|authorize_detach
name|'authorize_detach'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
nl|'\n'
string|"'v3:%s:detach'"
op|'%'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesController
name|'class'
name|'ExtendedVolumesController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ExtendedVolumesController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
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
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extend_server
dedent|''
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdms'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance_bdms'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'volume_ids'
op|'='
op|'['
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
name|'for'
name|'bdm'
name|'in'
name|'bdms'
name|'if'
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
op|']'
newline|'\n'
name|'key'
op|'='
string|'"%s:volumes_attached"'
op|'%'
name|'ExtendedVolumes'
op|'.'
name|'alias'
newline|'\n'
name|'server'
op|'['
name|'key'
op|']'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'volume_id'
op|'}'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ExtendedVolumesServerTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'show' method."
nl|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ExtendedVolumesServersTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'db_instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'detail' method."
nl|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'db_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_volume_id
dedent|''
dedent|''
dedent|''
name|'def'
name|'_validate_volume_id'
op|'('
name|'self'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Bad volumeId format: volumeId is "'
nl|'\n'
string|'"not in proper format (%s)"'
op|')'
op|'%'
name|'volume_id'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'attach'"
op|')'
newline|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
name|'id'
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
name|'authorize_attach'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'attach'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|'"The request body invalid"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'body'
op|'['
string|"'attach'"
op|']'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|'"Could not find volume_id from request"'
nl|'\n'
string|'"parameter"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'device'
op|'='
name|'body'
op|'['
string|"'attach'"
op|']'
op|'.'
name|'get'
op|'('
string|"'device'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_validate_volume_id'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Attach volume %(volume_id)s to instance %(server_id)s "'
nl|'\n'
string|'"at %(device)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'volume_id'
op|','
nl|'\n'
string|"'device'"
op|':'
name|'device'
op|','
nl|'\n'
string|"'server_id'"
op|':'
name|'server_id'
op|'}'
op|','
nl|'\n'
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
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
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'attach_volume'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'exception'
op|'.'
name|'VolumeNotFound'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceInvalidState'
name|'as'
name|'state_error'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
nl|'\n'
name|'state_error'
op|','
string|"'attach_volume'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidVolume'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidDevicePath'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'detach'"
op|')'
newline|'\n'
DECL|member|detach
name|'def'
name|'detach'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
name|'id'
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
name|'authorize_detach'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'detach'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|'"The request body invalid"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'body'
op|'['
string|"'detach'"
op|']'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'_'
op|'('
string|'"Could not find volume_id from request"'
nl|'\n'
string|'"parameter"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_validate_volume_id'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Detach volume %(volume_id)s from "'
nl|'\n'
string|'"instance %(server_id)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|'"volume_id"'
op|':'
name|'volume_id'
op|','
nl|'\n'
string|'"server_id"'
op|':'
name|'id'
op|','
nl|'\n'
string|'"context"'
op|':'
name|'context'
op|'}'
op|')'
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
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
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
name|'volume'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'VolumeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bdms'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance_bdms'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'bdms'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Volume %(volume_id)s is not attached to the "'
nl|'\n'
string|'"instance %(server_id)s"'
op|')'
op|'%'
op|'{'
string|"'server_id'"
op|':'
name|'server_id'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume_id'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'bdm'
name|'in'
name|'bdms'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
op|'!='
name|'volume_id'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'detach_volume'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'volume'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'VolumeUnattached'
op|':'
newline|'\n'
comment|'# The volume is not attached.  Treat it as NotFound'
nl|'\n'
comment|'# by falling through.'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidVolume'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceInvalidState'
name|'as'
name|'state_error'
op|':'
newline|'\n'
indent|'                '
name|'common'
op|'.'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
nl|'\n'
name|'state_error'
op|','
string|"'detach_volume'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Volume %(volume_id)s is not attached to the "'
nl|'\n'
string|'"instance %(server_id)s"'
op|')'
op|'%'
op|'{'
string|"'server_id'"
op|':'
name|'server_id'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume_id'
op|'}'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumes
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtendedVolumes'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extended Volumes support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ExtendedVolumes"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"extended_volumes/api/v3"'
op|')'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'ExtendedVolumesController'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_server
dedent|''
dedent|''
name|'def'
name|'make_server'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volumes'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
nl|'\n'
name|'elem'
op|','
string|"'{%s}volume_attached'"
op|'%'
name|'ExtendedVolumes'
op|'.'
name|'namespace'
op|','
nl|'\n'
name|'selector'
op|'='
string|"'%s:volumes_attached'"
op|'%'
name|'ExtendedVolumes'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'volumes'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesServerTemplate
dedent|''
name|'class'
name|'ExtendedVolumesServerTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'server'"
op|','
name|'selector'
op|'='
string|"'server'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'ExtendedVolumes'
op|'.'
name|'alias'
op|':'
name|'ExtendedVolumes'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesServersTemplate
dedent|''
dedent|''
name|'class'
name|'ExtendedVolumesServersTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'servers'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'server'"
op|','
name|'selector'
op|'='
string|"'servers'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'ExtendedVolumes'
op|'.'
name|'alias'
op|':'
name|'ExtendedVolumes'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
