begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
string|'"""Config Drive extension."""'
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
name|'config_drive'
name|'as'
name|'schema_config_drive'
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
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-config-drive"'
newline|'\n'
DECL|variable|ATTRIBUTE_NAME
name|'ATTRIBUTE_NAME'
op|'='
string|'"config_drive"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_soft_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDriveController
name|'class'
name|'ConfigDriveController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_add_config_drive
indent|'    '
name|'def'
name|'_add_config_drive'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'db_server'
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
comment|"# the core API adding it in its 'show'/'detail' methods."
nl|'\n'
name|'server'
op|'['
name|'ATTRIBUTE_NAME'
op|']'
op|'='
name|'db_server'
op|'['
string|"'config_drive'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_show
dedent|''
dedent|''
name|'def'
name|'_show'
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
name|'if'
string|"'server'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_config_drive'
op|'('
name|'req'
op|','
op|'['
name|'server'
op|']'
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
indent|'            '
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
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
string|"'servers'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
name|'and'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_config_drive'
op|'('
name|'req'
op|','
name|'servers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDrive
dedent|''
dedent|''
dedent|''
name|'class'
name|'ConfigDrive'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Config Drive Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ConfigDrive"'
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
name|'ConfigDriveController'
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
indent|'        '
name|'create_kwargs'
op|'['
string|"'config_drive'"
op|']'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'ATTRIBUTE_NAME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_server_create_schema
dedent|''
name|'def'
name|'get_server_create_schema'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'schema_config_drive'
op|'.'
name|'server_create'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
