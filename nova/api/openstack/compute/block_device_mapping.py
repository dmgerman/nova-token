begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
string|'"""The block device mappings extension."""'
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
name|'compute'
op|'.'
name|'schemas'
name|'import'
name|'block_device_mapping'
name|'as'
name|'schema_block_device_mapping'
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
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-block-device-mapping"'
newline|'\n'
DECL|variable|ATTRIBUTE_NAME
name|'ATTRIBUTE_NAME'
op|'='
string|'"block_device_mapping_v2"'
newline|'\n'
DECL|variable|LEGACY_ATTRIBUTE_NAME
name|'LEGACY_ATTRIBUTE_NAME'
op|'='
string|'"block_device_mapping"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BlockDeviceMapping
name|'class'
name|'BlockDeviceMapping'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Block device mapping boot support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"BlockDeviceMapping"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
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
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
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
comment|'# use nova.api.extensions.server.extensions entry point to modify'
nl|'\n'
comment|'# server create kwargs'
nl|'\n'
comment|"# NOTE(gmann): This function is not supposed to use 'body_deprecated_param'"
nl|'\n'
comment|'# parameter as this is placed to handle scheduler_hint extension for V2.1.'
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|','
name|'body_deprecated_param'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Have to check whether --image is given, see bug 1433609'
nl|'\n'
indent|'        '
name|'image_href'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'imageRef'"
op|')'
newline|'\n'
name|'image_uuid_specified'
op|'='
name|'image_href'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
name|'bdm'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'ATTRIBUTE_NAME'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'legacy_bdm'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'LEGACY_ATTRIBUTE_NAME'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'bdm'
name|'and'
name|'legacy_bdm'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Using different block_device_mapping syntaxes '"
nl|'\n'
string|"'is not allowed in the same request.'"
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
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'block_device_mapping'
op|'='
op|'['
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'.'
name|'from_api'
op|'('
name|'bdm_dict'
op|','
nl|'\n'
name|'image_uuid_specified'
op|')'
nl|'\n'
name|'for'
name|'bdm_dict'
name|'in'
name|'bdm'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidBDMFormat'
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
name|'if'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'            '
name|'create_kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|'='
name|'block_device_mapping'
newline|'\n'
comment|'# Unset the legacy_bdm flag if we got a block device mapping.'
nl|'\n'
name|'create_kwargs'
op|'['
string|"'legacy_bdm'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|get_server_create_schema
dedent|''
dedent|''
name|'def'
name|'get_server_create_schema'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'schema_block_device_mapping'
op|'.'
name|'server_create'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
