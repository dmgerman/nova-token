begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
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
nl|'\n'
DECL|class|Versions
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"version"'
op|':'
op|'['
string|'"status"'
op|','
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'['
string|'"rel"'
op|','
string|'"href"'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'Versions'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'None'
op|','
name|'serializers'
op|'='
name|'serializers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dispatch
dedent|''
name|'def'
name|'dispatch'
op|'('
name|'self'
op|','
name|'request'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Respond to a request for all OpenStack API versions."""'
newline|'\n'
name|'version_objs'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v1.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v1.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"DEPRECATED"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
op|'.'
name|'get_view_builder'
op|'('
name|'request'
op|')'
newline|'\n'
name|'versions'
op|'='
op|'['
name|'builder'
op|'.'
name|'build'
op|'('
name|'version'
op|')'
name|'for'
name|'version'
name|'in'
name|'version_objs'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'versions'
op|'='
name|'versions'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
