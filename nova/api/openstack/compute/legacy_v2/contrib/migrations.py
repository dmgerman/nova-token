begin_unit
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
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XMLNS
name|'XMLNS'
op|'='
string|'"http://docs.openstack.org/compute/ext/migrations/api/v2.0"'
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
string|"'migrations:%s'"
op|'%'
name|'action_name'
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
DECL|function|output
dedent|''
name|'def'
name|'output'
op|'('
name|'migrations_obj'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the desired output of the API from an object.\n\n    From a MigrationsList\'s object this method returns a list of\n    primitive objects with the only necessary fields.\n    """'
newline|'\n'
name|'detail_keys'
op|'='
op|'['
string|"'memory_total'"
op|','
string|"'memory_processed'"
op|','
string|"'memory_remaining'"
op|','
nl|'\n'
string|"'disk_total'"
op|','
string|"'disk_processed'"
op|','
string|"'disk_remaining'"
op|']'
newline|'\n'
comment|'# Note(Shaohe Feng): We need to leverage the oslo.versionedobjects.'
nl|'\n'
comment|"# Then we can pass the target version to it's obj_to_primitive."
nl|'\n'
name|'objects'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'migrations_obj'
op|')'
newline|'\n'
name|'objects'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'objects'
name|'if'
name|'not'
name|'x'
op|'['
string|"'hidden'"
op|']'
op|']'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'objects'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'obj'
op|'['
string|"'deleted'"
op|']'
newline|'\n'
name|'del'
name|'obj'
op|'['
string|"'deleted_at'"
op|']'
newline|'\n'
name|'del'
name|'obj'
op|'['
string|"'migration_type'"
op|']'
newline|'\n'
name|'del'
name|'obj'
op|'['
string|"'hidden'"
op|']'
newline|'\n'
name|'if'
string|"'memory_total'"
name|'in'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'detail_keys'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'obj'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'objects'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsController
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
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
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
name|'output'
op|'('
name|'migrations'
op|')'
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
name|'ExtensionDescriptor'
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
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-05-30T00:00:00Z"'
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
dedent|''
dedent|''
endmarker|''
end_unit
