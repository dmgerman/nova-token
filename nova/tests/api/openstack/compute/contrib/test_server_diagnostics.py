begin_unit
comment|'# Copyright 2011 Eldar Nugaev'
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
name|'compute'
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
name|'server_diagnostics'
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
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
nl|'\n'
nl|'\n'
DECL|variable|UUID
name|'UUID'
op|'='
string|"'abc'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_diagnostics
name|'def'
name|'fake_get_diagnostics'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'data'"
op|':'
string|"'Some diagnostic info'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get
dedent|''
name|'def'
name|'fake_instance_get'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'instance_uuid'
op|'!='
name|'UUID'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"Invalid UUID"'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerDiagnosticsTest
dedent|''
name|'class'
name|'ServerDiagnosticsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'ServerDiagnosticsTest'
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
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Server_diagnostics'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'fake_get_diagnostics'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'router'
op|'='
name|'compute'
op|'.'
name|'APIRouter'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
string|"'diagnostics'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_diagnostics
dedent|''
name|'def'
name|'test_get_diagnostics'
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
string|"'/fake/servers/%s/diagnostics'"
op|'%'
name|'UUID'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'data'"
op|':'
string|"'Some diagnostic info'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestServerDiagnosticsXMLSerializer
dedent|''
dedent|''
name|'class'
name|'TestServerDiagnosticsXMLSerializer'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|namespace
indent|'    '
name|'namespace'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
newline|'\n'
nl|'\n'
DECL|member|_tag
name|'def'
name|'_tag'
op|'('
name|'self'
op|','
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tagname'
op|'='
name|'elem'
op|'.'
name|'tag'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tagname'
op|'['
number|'0'
op|']'
op|','
string|"'{'"
op|')'
newline|'\n'
name|'tmp'
op|'='
name|'tagname'
op|'.'
name|'partition'
op|'('
string|"'}'"
op|')'
newline|'\n'
name|'namespace'
op|'='
name|'tmp'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'namespace'
op|','
name|'self'
op|'.'
name|'namespace'
op|')'
newline|'\n'
name|'return'
name|'tmp'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'server_diagnostics'
op|'.'
name|'ServerDiagnosticsTemplate'
op|'('
op|')'
newline|'\n'
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'diag1'
op|'='
string|"'foo'"
op|','
name|'diag2'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'diagnostics'"
op|','
name|'self'
op|'.'
name|'_tag'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'tree'
op|')'
op|','
name|'len'
op|'('
name|'exemplar'
op|')'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'tag'
op|'='
name|'self'
op|'.'
name|'_tag'
op|'('
name|'child'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'tag'
name|'in'
name|'exemplar'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'text'
op|','
name|'exemplar'
op|'['
name|'tag'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
