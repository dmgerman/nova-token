begin_unit
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
nl|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'accounts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'User'
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
DECL|function|fake_init
name|'def'
name|'fake_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'manager'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_admin_check
dedent|''
name|'def'
name|'fake_admin_check'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccountsTest
dedent|''
name|'class'
name|'AccountsTest'
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
name|'AccountsTest'
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
name|'allow_admin_api'
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
name|'accounts'
op|'.'
name|'Controller'
op|','
string|"'__init__'"
op|','
nl|'\n'
name|'fake_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'accounts'
op|'.'
name|'Controller'
op|','
string|"'_check_admin'"
op|','
nl|'\n'
name|'fake_admin_check'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'clear_fakes'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_auth'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'fakemgr'
op|'='
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
name|'joeuser'
op|'='
name|'User'
op|'('
string|"'id1'"
op|','
string|"'guy1'"
op|','
string|"'acc1'"
op|','
string|"'secret1'"
op|','
name|'False'
op|')'
newline|'\n'
name|'superuser'
op|'='
name|'User'
op|'('
string|"'id2'"
op|','
string|"'guy2'"
op|','
string|"'acc2'"
op|','
string|"'secret2'"
op|','
name|'True'
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'add_user'
op|'('
name|'joeuser'
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'add_user'
op|'('
name|'superuser'
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'create_project'
op|'('
string|"'test1'"
op|','
name|'joeuser'
op|')'
newline|'\n'
name|'fakemgr'
op|'.'
name|'create_project'
op|'('
string|"'test2'"
op|','
name|'superuser'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_account
dedent|''
name|'def'
name|'test_get_account'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/accounts/test1'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'manager'"
op|']'
op|','
string|"'id1'"
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_account_delete
dedent|''
name|'def'
name|'test_account_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/accounts/test1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'test1'"
name|'not'
name|'in'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'projects'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_account_create
dedent|''
name|'def'
name|'test_account_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'account'
op|'='
name|'dict'
op|'('
name|'description'
op|'='
string|"'test account'"
op|','
nl|'\n'
name|'manager'
op|'='
string|"'id1'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/accounts/newacct'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'newacct'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'newacct'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'description'"
op|']'
op|','
string|"'test account'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'manager'"
op|']'
op|','
string|"'id1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'newacct'"
name|'in'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'values'
op|'('
op|')'
op|')'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_account_update
dedent|''
name|'def'
name|'test_account_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'account'
op|'='
name|'dict'
op|'('
name|'description'
op|'='
string|"'test account'"
op|','
nl|'\n'
name|'manager'
op|'='
string|"'id2'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/accounts/test1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'description'"
op|']'
op|','
string|"'test account'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'account'"
op|']'
op|'['
string|"'manager'"
op|']'
op|','
string|"'id2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'projects'
op|'.'
name|'values'
op|'('
op|')'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
