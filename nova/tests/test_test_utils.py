begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
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
name|'nova'
name|'import'
name|'db'
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
name|'import'
name|'utils'
name|'as'
name|'test_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestUtilsTestCase
name|'class'
name|'TestUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_test_admin_context
indent|'    '
name|'def'
name|'test_get_test_admin_context'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""get_test_admin_context\'s return value behaves like admin context"""'
newline|'\n'
name|'ctxt'
op|'='
name|'test_utils'
op|'.'
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(soren): This should verify the full interface context'
nl|'\n'
comment|'# objects expose.'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ctxt'
op|'.'
name|'is_admin'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_test_instance
dedent|''
name|'def'
name|'test_get_test_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""get_test_instance\'s return value looks like an instance_ref"""'
newline|'\n'
name|'instance_ref'
op|'='
name|'test_utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'test_utils'
op|'.'
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'ctxt'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_get_test_network_info
dedent|''
name|'def'
name|'_test_get_test_network_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Does the return value match a real network_info structure"""'
newline|'\n'
comment|'# The challenge here is to define what exactly such a structure'
nl|'\n'
comment|'# must look like.'
nl|'\n'
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
