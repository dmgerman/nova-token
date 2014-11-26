begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
string|'"""Microversions Test Extension"""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
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
name|'import'
name|'validation'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'test_plugins'
name|'import'
name|'dummy_schema'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'test-microversions'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MicroversionsController
name|'class'
name|'MicroversionsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.1"'
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
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'val'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.2"'
op|')'
comment|'# noqa'
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
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'val2'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"3.0"'
op|')'
comment|'# noqa'
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
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# We have a second example controller here to help check'
nl|'\n'
comment|'# for accidental dependencies between API controllers'
nl|'\n'
comment|'# due to base class changes'
nl|'\n'
DECL|class|MicroversionsController2
dedent|''
dedent|''
name|'class'
name|'MicroversionsController2'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.2"'
op|','
string|'"2.5"'
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
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'controller2_val1'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.5"'
op|','
string|'"3.1"'
op|')'
comment|'# noqa'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
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
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'controller2_val2'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MicroversionsController3
dedent|''
dedent|''
name|'class'
name|'MicroversionsController3'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.1"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'dummy_schema'
op|'.'
name|'dummy'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'create_val1'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'Controller'
op|'.'
name|'api_version'
op|'('
string|'"2.1"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'dummy_schema'
op|'.'
name|'dummy'
op|','
string|'"2.3"'
op|','
string|'"2.8"'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'dummy_schema'
op|'.'
name|'dummy2'
op|','
string|'"2.9"'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
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
name|'data'
op|'='
op|'{'
string|"'param'"
op|':'
string|"'update_val1'"
op|'}'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Microversions
dedent|''
dedent|''
name|'class'
name|'Microversions'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Basic Microversions Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Microversions"'
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
name|'res1'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'microversions'"
op|','
nl|'\n'
name|'MicroversionsController'
op|'('
op|')'
op|')'
newline|'\n'
name|'res2'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'microversions2'"
op|','
nl|'\n'
name|'MicroversionsController2'
op|'('
op|')'
op|')'
newline|'\n'
name|'res3'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'microversions3'"
op|','
nl|'\n'
name|'MicroversionsController3'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res1'
op|','
name|'res2'
op|','
name|'res3'
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
dedent|''
dedent|''
endmarker|''
end_unit
