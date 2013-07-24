begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|XMLNS
name|'XMLNS'
op|'='
string|'"http://docs.openstack.org/compute/ext/migrations/api/v3"'
newline|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-migrations"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|authorize
name|'def'
name|'authorize'
op|'('
name|'context'
op|','
name|'action_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'action'
op|'='
string|"'v3:%s:%s'"
op|'%'
op|'('
name|'ALIAS'
op|','
name|'action_name'
op|')'
newline|'\n'
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
name|'action'
op|')'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsTemplate
dedent|''
name|'class'
name|'MigrationsTemplate'
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
string|"'migrations'"
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
string|"'migration'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'migrations'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'source_node'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'dest_node'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'source_compute'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'dest_compute'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'dest_host'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'instance_uuid'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'old_instance_type_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'new_instance_type_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'created_at'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'updated_at'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsController
dedent|''
dedent|''
name|'class'
name|'MigrationsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Controller for accessing migrations in OpenStack API."""'
newline|'\n'
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
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'MigrationsTemplate'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""Return all migrations in progress."""'
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
name|'authorize'
op|'('
name|'context'
op|','
string|'"index"'
op|')'
newline|'\n'
name|'migrations'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_migrations'
op|'('
name|'context'
op|','
name|'req'
op|'.'
name|'GET'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'migrations'"
op|':'
name|'migrations'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Migrations
dedent|''
dedent|''
name|'class'
name|'Migrations'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide data on migrations."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Migrations"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
name|'XMLNS'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-migrations'"
op|','
nl|'\n'
name|'MigrationsController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
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
dedent|''
dedent|''
endmarker|''
end_unit
