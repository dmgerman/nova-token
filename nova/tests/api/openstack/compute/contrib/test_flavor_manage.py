begin_unit
comment|'# Copyright 2011 Andrew Bogott for the Wikimedia Foundation'
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
name|'datetime'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'flavormanage'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance_type_by_flavor_id
name|'def'
name|'fake_get_instance_type_by_flavor_id'
op|'('
name|'flavorid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'flavorid'
op|'=='
string|'"failtest"'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Not found sucka!"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'root_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"u'frob'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'19'
op|','
number|'18'
op|','
number|'49'
op|','
number|'30'
op|','
number|'877329'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'256'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'flavorid'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'7'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_purge
dedent|''
name|'def'
name|'fake_purge'
op|'('
name|'flavorname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_destroy
dedent|''
name|'def'
name|'fake_destroy'
op|'('
name|'flavorname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_create
dedent|''
name|'def'
name|'fake_create'
op|'('
name|'name'
op|','
name|'memory_mb'
op|','
name|'vcpus'
op|','
name|'root_gb'
op|','
name|'ephemeral_gb'
op|','
nl|'\n'
name|'flavorid'
op|','
name|'swap'
op|','
name|'rxtx_factor'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'newflavor'
op|'='
name|'fake_get_instance_type_by_flavor_id'
op|'('
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
name|'newflavor'
op|'['
string|'"name"'
op|']'
op|'='
name|'name'
newline|'\n'
name|'newflavor'
op|'['
string|'"memory_mb"'
op|']'
op|'='
name|'int'
op|'('
name|'memory_mb'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"vcpus"'
op|']'
op|'='
name|'int'
op|'('
name|'vcpus'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"root_gb"'
op|']'
op|'='
name|'int'
op|'('
name|'root_gb'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"ephemeral_gb"'
op|']'
op|'='
name|'int'
op|'('
name|'ephemeral_gb'
op|')'
newline|'\n'
name|'newflavor'
op|'['
string|'"swap"'
op|']'
op|'='
name|'swap'
newline|'\n'
name|'newflavor'
op|'['
string|'"rxtx_factor"'
op|']'
op|'='
name|'float'
op|'('
name|'rxtx_factor'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'newflavor'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorManageTest
dedent|''
name|'class'
name|'FlavorManageTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FlavorManageTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
nl|'\n'
string|'"get_instance_type_by_flavor_id"'
op|','
nl|'\n'
name|'fake_get_instance_type_by_flavor_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|'"destroy"'
op|','
name|'fake_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|'"create"'
op|','
name|'fake_create'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'flavormanage'
op|'.'
name|'FlavorManageController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FlavorManageTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/flavor/delete/1234'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|'('
name|'req'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|','
name|'req'
op|','
string|'"failtest"'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/flavor/delete/1234'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_delete'
op|'('
name|'req'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"test"'
op|','
nl|'\n'
string|'"ram"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"disk"'
op|':'
number|'10'
op|','
nl|'\n'
string|'"id"'
op|':'
number|'1235'
op|','
nl|'\n'
string|'"swap"'
op|':'
number|'512'
op|','
nl|'\n'
string|'"rxtx_factor"'
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/flavor/create/'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'body'
op|'['
string|'"flavor"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'res'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|','
name|'body'
op|'['
string|'"flavor"'
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/123/flavor/create/'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_create'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
