begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2011 OpenStack LLC'
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
string|'"""Test suite for IPv6."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'ipv6'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.test_ipv6'"
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPv6RFC2462TestCase
name|'class'
name|'IPv6RFC2462TestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for IPv6 rfc2462 backend operations."""'
newline|'\n'
DECL|member|setUp
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
name|'IPv6RFC2462TestCase'
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
name|'ipv6_backend'
op|'='
string|"'rfc2462'"
op|')'
newline|'\n'
name|'ipv6'
op|'.'
name|'reset_backend'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_global
dedent|''
name|'def'
name|'test_to_global'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'addr'
op|'='
name|'ipv6'
op|'.'
name|'to_global'
op|'('
string|"'2001:db8::'"
op|','
string|"'02:16:3e:33:44:55'"
op|','
string|"'test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'addr'
op|','
string|"'2001:db8::16:3eff:fe33:4455'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_mac
dedent|''
name|'def'
name|'test_to_mac'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'ipv6'
op|'.'
name|'to_mac'
op|'('
string|"'2001:db8::216:3eff:fe33:4455'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'mac'
op|','
string|"'00:16:3e:33:44:55'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_global_with_bad_mac
dedent|''
name|'def'
name|'test_to_global_with_bad_mac'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_mac'
op|'='
string|"'02:16:3e:33:44:5Z'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'ipv6'
op|'.'
name|'to_global'
op|','
nl|'\n'
string|"'2001:db8::'"
op|','
name|'bad_mac'
op|','
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_global_with_bad_prefix
dedent|''
name|'def'
name|'test_to_global_with_bad_prefix'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_prefix'
op|'='
string|"'82'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'ipv6'
op|'.'
name|'to_global'
op|','
nl|'\n'
name|'bad_prefix'
op|','
nl|'\n'
string|"'2001:db8::216:3eff:fe33:4455'"
op|','
nl|'\n'
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_global_with_bad_project
dedent|''
name|'def'
name|'test_to_global_with_bad_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_project'
op|'='
string|"'non-existent-project-name'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'ipv6'
op|'.'
name|'to_global'
op|','
nl|'\n'
string|"'2001:db8::'"
op|','
nl|'\n'
string|"'2001:db8::a94a:8fe5:ff33:4455'"
op|','
nl|'\n'
name|'bad_project'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPv6AccountIdentiferTestCase
dedent|''
dedent|''
name|'class'
name|'IPv6AccountIdentiferTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for IPv6 account_identifier backend operations."""'
newline|'\n'
DECL|member|setUp
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
name|'IPv6AccountIdentiferTestCase'
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
name|'ipv6_backend'
op|'='
string|"'account_identifier'"
op|')'
newline|'\n'
name|'ipv6'
op|'.'
name|'reset_backend'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_global
dedent|''
name|'def'
name|'test_to_global'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'addr'
op|'='
name|'ipv6'
op|'.'
name|'to_global'
op|'('
string|"'2001:db8::'"
op|','
string|"'02:16:3e:33:44:55'"
op|','
string|"'test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'addr'
op|','
string|"'2001:db8::a94a:8fe5:ff33:4455'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_mac
dedent|''
name|'def'
name|'test_to_mac'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'ipv6'
op|'.'
name|'to_mac'
op|'('
string|"'2001:db8::a94a:8fe5:ff33:4455'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'mac'
op|','
string|"'02:16:3e:33:44:55'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
