begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'httplib'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'read_write_util'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ReadWriteUtilTestCase
name|'class'
name|'ReadWriteUtilTestCase'
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
name|'ReadWriteUtilTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ipv6_host
dedent|''
name|'def'
name|'test_ipv6_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ipv6_host'
op|'='
string|"'fd8c:215d:178e:c51e:200:c9ff:fed1:584c'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'httplib'
op|'.'
name|'HTTPConnection'
op|','
string|"'endheaders'"
op|')'
newline|'\n'
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'.'
name|'endheaders'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'file'
op|'='
name|'read_write_util'
op|'.'
name|'VMwareHTTPWriteFile'
op|'('
name|'ipv6_host'
op|','
nl|'\n'
string|"'fake_dc'"
op|','
nl|'\n'
string|"'fake_ds'"
op|','
nl|'\n'
name|'dict'
op|'('
op|')'
op|','
nl|'\n'
string|"'/tmp/fake.txt'"
op|','
nl|'\n'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ipv6_host'
op|','
name|'file'
op|'.'
name|'conn'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'443'
op|','
name|'file'
op|'.'
name|'conn'
op|'.'
name|'port'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
