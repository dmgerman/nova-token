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
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
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
name|'views'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavor controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"flavor"'
op|':'
op|'['
string|'"id"'
op|','
string|'"name"'
op|','
string|'"ram"'
op|','
string|'"disk"'
op|']'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'['
string|'"rel"'
op|','
string|'"type"'
op|','
string|'"href"'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
string|'"""Return all flavors in brief."""'
newline|'\n'
name|'items'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'req'
op|','
name|'is_detail'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
name|'items'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all flavors in detail."""'
newline|'\n'
name|'items'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'req'
op|','
name|'is_detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavors'
op|'='
name|'items'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flavors
dedent|''
name|'def'
name|'_get_flavors'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'is_detail'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Helper function that returns a list of flavor dicts."""'
newline|'\n'
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'flavors'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'items'
op|'='
op|'['
name|'builder'
op|'.'
name|'build'
op|'('
name|'flavor'
op|','
name|'is_detail'
op|'='
name|'is_detail'
op|')'
nl|'\n'
name|'for'
name|'flavor'
name|'in'
name|'flavors'
op|'.'
name|'values'
op|'('
op|')'
op|']'
newline|'\n'
name|'return'
name|'items'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given flavor id."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'flavor'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_type_get_by_flavor_id'
op|'('
name|'ctxt'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'builder'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'values'
op|'='
name|'builder'
op|'.'
name|'build'
op|'('
name|'flavor'
op|','
name|'is_detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'flavor'
op|'='
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV10
dedent|''
dedent|''
name|'class'
name|'ControllerV10'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_get_view_builder
indent|'    '
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'views'
op|'.'
name|'flavors'
op|'.'
name|'ViewBuilder'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV11
dedent|''
dedent|''
name|'class'
name|'ControllerV11'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_get_view_builder
indent|'    '
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
name|'req'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'views'
op|'.'
name|'flavors'
op|'.'
name|'ViewBuilderV11'
op|'('
name|'base_url'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
