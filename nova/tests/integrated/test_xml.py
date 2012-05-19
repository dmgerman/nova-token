begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
name|'import'
name|'integrated_helpers'
newline|'\n'
nl|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|class|XmlTests
name|'class'
name|'XmlTests'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""""Some basic XML sanity checks."""'
newline|'\n'
nl|'\n'
DECL|member|test_namespace_limits
name|'def'
name|'test_namespace_limits'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/xml'"
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_request'
op|'('
string|"'/limits'"
op|','
name|'headers'
op|'='
name|'headers'
op|')'
newline|'\n'
name|'data'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"data: %s"'
op|'%'
name|'data'
op|')'
newline|'\n'
name|'root'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'nsmap'
op|'.'
name|'get'
op|'('
name|'None'
op|')'
op|','
name|'xmlutil'
op|'.'
name|'XMLNS_COMMON_V10'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_namespace_servers
dedent|''
name|'def'
name|'test_namespace_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""/servers should have v1.1 namespace (has changed in 1.1)."""'
newline|'\n'
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/xml'"
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_request'
op|'('
string|"'/servers'"
op|','
name|'headers'
op|'='
name|'headers'
op|')'
newline|'\n'
name|'data'
op|'='
name|'response'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"data: %s"'
op|'%'
name|'data'
op|')'
newline|'\n'
name|'root'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'nsmap'
op|'.'
name|'get'
op|'('
name|'None'
op|')'
op|','
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
