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
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
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
name|'import'
name|'extensions'
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
name|'server_action_list'
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
name|'import'
name|'nova'
op|'.'
name|'compute'
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
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|dt
name|'dt'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_actions
name|'def'
name|'fake_get_actions'
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
op|'['
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'rebuild'"
op|','
string|"'error'"
op|':'
name|'None'
op|','
string|"'created_at'"
op|':'
name|'dt'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'reboot'"
op|','
string|"'error'"
op|':'
string|"'Failed!'"
op|','
string|"'created_at'"
op|':'
name|'dt'
op|'}'
op|','
nl|'\n'
op|']'
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
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerActionsTest
dedent|''
name|'class'
name|'ServerActionsTest'
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
name|'ServerActionsTest'
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
name|'allow_admin_api'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
string|"'get_actions'"
op|','
name|'fake_get_actions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|'('
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_actions
dedent|''
name|'def'
name|'test_get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'gen_uuid'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/fake/servers/%s/actions'"
op|'%'
name|'uuid'
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
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'actions'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'rebuild'"
op|','
string|"'error'"
op|':'
name|'None'
op|','
string|"'created_at'"
op|':'
name|'str'
op|'('
name|'dt'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'reboot'"
op|','
string|"'error'"
op|':'
string|"'Failed!'"
op|','
string|"'created_at'"
op|':'
name|'str'
op|'('
name|'dt'
op|')'
op|'}'
op|','
nl|'\n'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestServerActionsXMLSerializer
dedent|''
dedent|''
name|'class'
name|'TestServerActionsXMLSerializer'
op|'('
name|'unittest'
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
name|'server_action_list'
op|'.'
name|'ServerActionsTemplate'
op|'('
op|')'
newline|'\n'
name|'exemplar'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
op|','
nl|'\n'
name|'action'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'error'
op|'='
string|"'quxx'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
op|','
nl|'\n'
name|'action'
op|'='
string|"'bar'"
op|','
nl|'\n'
name|'error'
op|'='
string|"'xxuq'"
op|')'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'actions'
op|'='
name|'exemplar'
op|')'
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
string|"'actions'"
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
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'action'"
op|','
name|'self'
op|'.'
name|'_tag'
op|'('
name|'child'
op|')'
op|')'
newline|'\n'
name|'for'
name|'field'
name|'in'
op|'('
string|"'created_at'"
op|','
string|"'action'"
op|','
string|"'error'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'exemplar'
op|'['
name|'idx'
op|']'
op|'['
name|'field'
op|']'
op|')'
op|','
name|'child'
op|'.'
name|'get'
op|'('
name|'field'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
