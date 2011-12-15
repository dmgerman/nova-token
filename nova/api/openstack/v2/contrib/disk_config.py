begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
comment|'#    under the License'
nl|'\n'
nl|'\n'
string|'"""Disk Config extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
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
name|'db'
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
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.contrib.disk_config'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'RAX-DCF'"
newline|'\n'
DECL|variable|XMLNS_DCF
name|'XMLNS_DCF'
op|'='
string|'"http://docs.rackspacecloud.com/servers/api/ext/diskConfig/v1.0"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiskConfigTemplate
name|'class'
name|'ServerDiskConfigTemplate'
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
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
string|"'%s:diskConfig'"
op|'%'
name|'ALIAS'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ServersDiskConfigTemplate'
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
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
string|"'%s:diskConfig'"
op|'%'
name|'ALIAS'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ImageDiskConfigTemplate'
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
string|"'image'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
string|"'%s:diskConfig'"
op|'%'
name|'ALIAS'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesDiskConfigTemplate
dedent|''
dedent|''
name|'class'
name|'ImagesDiskConfigTemplate'
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
string|"'images'"
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
string|"'image'"
op|','
name|'selector'
op|'='
string|"'images'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}diskConfig'"
op|'%'
name|'XMLNS_DCF'
op|','
string|"'%s:diskConfig'"
op|'%'
name|'ALIAS'
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
name|'ALIAS'
op|':'
name|'XMLNS_DCF'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|disk_config_to_api
dedent|''
dedent|''
name|'def'
name|'disk_config_to_api'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'AUTO'"
name|'if'
name|'value'
name|'else'
string|"'MANUAL'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|disk_config_from_api
dedent|''
name|'def'
name|'disk_config_from_api'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'value'
op|'=='
string|"'AUTO'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'value'
op|'=='
string|"'MANUAL'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"RAX-DCF:diskConfig must be either \'MANUAL\' or \'AUTO\'."'
op|')'
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
nl|'\n'
DECL|class|Disk_config
dedent|''
dedent|''
name|'class'
name|'Disk_config'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disk Management Extension"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"DiskConfig"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
name|'XMLNS_DCF'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-09-27:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|variable|API_DISK_CONFIG
name|'API_DISK_CONFIG'
op|'='
string|'"%s:diskConfig"'
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|INTERNAL_DISK_CONFIG
name|'INTERNAL_DISK_CONFIG'
op|'='
string|'"auto_disk_config"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Disk_config'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ext_mgr'
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
nl|'\n'
DECL|member|_extract_resource_from_body
dedent|''
name|'def'
name|'_extract_resource_from_body'
op|'('
name|'self'
op|','
name|'res'
op|','
name|'body'
op|','
nl|'\n'
name|'singular'
op|','
name|'singular_template'
op|','
name|'plural'
op|','
name|'plural_template'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of the given resources from the request body.\n\n        The templates passed in are used for XML serialization.\n        """'
newline|'\n'
name|'template'
op|'='
name|'res'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'nova.template'"
op|')'
newline|'\n'
name|'if'
name|'plural'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'='
name|'body'
op|'['
name|'plural'
op|']'
newline|'\n'
name|'if'
name|'template'
op|':'
newline|'\n'
indent|'                '
name|'template'
op|'.'
name|'attach'
op|'('
name|'plural_template'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'singular'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'='
op|'['
name|'body'
op|'['
name|'singular'
op|']'
op|']'
newline|'\n'
name|'if'
name|'template'
op|':'
newline|'\n'
indent|'                '
name|'template'
op|'.'
name|'attach'
op|'('
name|'singular_template'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|_GET_servers
dedent|''
name|'def'
name|'_GET_servers'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'res'
op|','
name|'body'
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
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'_extract_resource_from_body'
op|'('
name|'res'
op|','
name|'body'
op|','
nl|'\n'
name|'singular'
op|'='
string|"'server'"
op|','
name|'singular_template'
op|'='
name|'ServerDiskConfigTemplate'
op|'('
op|')'
op|','
nl|'\n'
name|'plural'
op|'='
string|"'servers'"
op|','
name|'plural_template'
op|'='
name|'ServersDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Filter out any servers that already have the key set (most likely'
nl|'\n'
comment|'# from a remote zone)'
nl|'\n'
name|'servers'
op|'='
name|'filter'
op|'('
name|'lambda'
name|'s'
op|':'
name|'self'
op|'.'
name|'API_DISK_CONFIG'
name|'not'
name|'in'
name|'s'
op|','
name|'servers'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get DB information for servers'
nl|'\n'
name|'uuids'
op|'='
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'db_servers'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
op|'{'
string|"'uuid'"
op|':'
name|'uuids'
op|'}'
op|')'
newline|'\n'
name|'db_servers'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'s'
op|'['
string|"'uuid'"
op|']'
op|','
name|'s'
op|')'
name|'for'
name|'s'
name|'in'
name|'db_servers'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'db_server'
op|'='
name|'db_servers'
op|'.'
name|'get'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'db_server'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'db_server'
op|'['
name|'self'
op|'.'
name|'INTERNAL_DISK_CONFIG'
op|']'
newline|'\n'
name|'server'
op|'['
name|'self'
op|'.'
name|'API_DISK_CONFIG'
op|']'
op|'='
name|'disk_config_to_api'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_GET_images
dedent|''
name|'def'
name|'_GET_images'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'res'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'_extract_resource_from_body'
op|'('
name|'res'
op|','
name|'body'
op|','
nl|'\n'
name|'singular'
op|'='
string|"'image'"
op|','
name|'singular_template'
op|'='
name|'ImageDiskConfigTemplate'
op|'('
op|')'
op|','
nl|'\n'
name|'plural'
op|'='
string|"'images'"
op|','
name|'plural_template'
op|'='
name|'ImagesDiskConfigTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'image'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'INTERNAL_DISK_CONFIG'
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'                '
name|'raw_value'
op|'='
name|'metadata'
op|'['
name|'self'
op|'.'
name|'INTERNAL_DISK_CONFIG'
op|']'
newline|'\n'
name|'value'
op|'='
name|'utils'
op|'.'
name|'bool_from_str'
op|'('
name|'raw_value'
op|')'
newline|'\n'
name|'image'
op|'['
name|'self'
op|'.'
name|'API_DISK_CONFIG'
op|']'
op|'='
name|'disk_config_to_api'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_POST_servers
dedent|''
name|'def'
name|'_POST_servers'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'res'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_GET_servers'
op|'('
name|'req'
op|','
name|'res'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_pre_POST_servers
dedent|''
name|'def'
name|'_pre_POST_servers'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): deserialization currently occurs *after* pre-processing'
nl|'\n'
comment|'# extensions are called. Until extensions are refactored so that'
nl|'\n'
comment|'# deserialization occurs earlier, we have to perform the'
nl|'\n'
comment|'# deserialization ourselves.'
nl|'\n'
indent|'        '
name|'content_type'
op|'='
name|'req'
op|'.'
name|'content_type'
newline|'\n'
nl|'\n'
name|'if'
string|"'xml'"
name|'in'
name|'content_type'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'server'
op|'='
name|'node'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'server'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'api_value'
op|'='
name|'server'
op|'.'
name|'getAttribute'
op|'('
name|'self'
op|'.'
name|'API_DISK_CONFIG'
op|')'
newline|'\n'
name|'if'
name|'api_value'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'disk_config_from_api'
op|'('
name|'api_value'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'setAttribute'
op|'('
name|'self'
op|'.'
name|'INTERNAL_DISK_CONFIG'
op|','
name|'str'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'str'
op|'('
name|'node'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
name|'utils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'server'
op|'='
name|'body'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'api_value'
op|'='
name|'server'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'API_DISK_CONFIG'
op|')'
newline|'\n'
name|'if'
name|'api_value'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'disk_config_from_api'
op|'('
name|'api_value'
op|')'
newline|'\n'
name|'server'
op|'['
name|'self'
op|'.'
name|'INTERNAL_DISK_CONFIG'
op|']'
op|'='
name|'value'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'utils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_pre_PUT_servers
dedent|''
dedent|''
dedent|''
name|'def'
name|'_pre_PUT_servers'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_pre_POST_servers'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_request_extensions
dedent|''
name|'def'
name|'get_request_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ReqExt'
op|'='
name|'extensions'
op|'.'
name|'RequestExtension'
newline|'\n'
name|'return'
op|'['
nl|'\n'
name|'ReqExt'
op|'('
name|'method'
op|'='
string|"'GET'"
op|','
nl|'\n'
name|'url_route'
op|'='
string|"'/:(project_id)/servers/:(id)'"
op|','
nl|'\n'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_GET_servers'
op|')'
op|','
nl|'\n'
name|'ReqExt'
op|'('
name|'method'
op|'='
string|"'POST'"
op|','
nl|'\n'
name|'url_route'
op|'='
string|"'/:(project_id)/servers'"
op|','
nl|'\n'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_POST_servers'
op|','
nl|'\n'
name|'pre_handler'
op|'='
name|'self'
op|'.'
name|'_pre_POST_servers'
op|')'
op|','
nl|'\n'
name|'ReqExt'
op|'('
name|'method'
op|'='
string|"'PUT'"
op|','
nl|'\n'
name|'url_route'
op|'='
string|"'/:(project_id)/servers/:(id)'"
op|','
nl|'\n'
name|'pre_handler'
op|'='
name|'self'
op|'.'
name|'_pre_PUT_servers'
op|')'
op|','
nl|'\n'
name|'ReqExt'
op|'('
name|'method'
op|'='
string|"'GET'"
op|','
nl|'\n'
name|'url_route'
op|'='
string|"'/:(project_id)/images/:(id)'"
op|','
nl|'\n'
name|'handler'
op|'='
name|'self'
op|'.'
name|'_GET_images'
op|')'
nl|'\n'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
