begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nTests For ZoneManager\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'novatools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'zone_manager'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeZone
name|'class'
name|'FakeZone'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a fake zone from the db"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kwargs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|exploding_novatools
dedent|''
dedent|''
dedent|''
name|'def'
name|'exploding_novatools'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used when we want to simulate a novatools call failing."""'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
string|'"kaboom"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneManagerTestCase
dedent|''
name|'class'
name|'ZoneManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for zone manager"""'
newline|'\n'
DECL|member|test_ping
name|'def'
name|'test_ping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zm'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'zm'
op|','
string|"'_refresh_from_db'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'zm'
op|','
string|"'_poll_zones'"
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_refresh_from_db'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_poll_zones'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'ping'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_from_db_new
dedent|''
name|'def'
name|'test_refresh_from_db_new'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zm'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
nl|'\n'
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'user1'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'pass1'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_refresh_from_db'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'1'
op|']'
op|'.'
name|'username'
op|','
string|"'user1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_from_db_replace_existing
dedent|''
name|'def'
name|'test_refresh_from_db_replace_existing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zm'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneState'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'update_credentials'
op|'('
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'user1'"
op|','
name|'password'
op|'='
string|"'pass1'"
op|')'
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'1'
op|']'
op|'='
name|'zone_state'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
nl|'\n'
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'user2'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'pass2'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_refresh_from_db'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'1'
op|']'
op|'.'
name|'username'
op|','
string|"'user2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_from_db_missing
dedent|''
name|'def'
name|'test_refresh_from_db_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zm'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneState'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'update_credentials'
op|'('
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'user1'"
op|','
name|'password'
op|'='
string|"'pass1'"
op|')'
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'1'
op|']'
op|'='
name|'zone_state'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_refresh_from_db'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_from_db_add_and_delete
dedent|''
name|'def'
name|'test_refresh_from_db_add_and_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'zm'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneState'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'update_credentials'
op|'('
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'user1'"
op|','
name|'password'
op|'='
string|"'pass1'"
op|')'
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'1'
op|']'
op|'='
name|'zone_state'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
nl|'\n'
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'user2'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'pass2'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zm'
op|'.'
name|'_refresh_from_db'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zm'
op|'.'
name|'zone_states'
op|'['
number|'2'
op|']'
op|'.'
name|'username'
op|','
string|"'user2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_poll_zone
dedent|''
name|'def'
name|'test_poll_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'zone_manager'
op|','
string|"'_call_novatools'"
op|')'
newline|'\n'
name|'zone_manager'
op|'.'
name|'_call_novatools'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'name'
op|'='
string|"'zohan'"
op|','
name|'capabilities'
op|'='
string|"'hairdresser'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'zone_state'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneState'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'update_credentials'
op|'('
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'user2'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'pass2'"
op|')'
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'attempt'
op|'='
number|'1'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zone_manager'
op|'.'
name|'_poll_zone'
op|'('
name|'zone_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zone_state'
op|'.'
name|'attempt'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zone_state'
op|'.'
name|'name'
op|','
string|"'zohan'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_poll_zone_fails
dedent|''
name|'def'
name|'test_poll_zone_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'zone_manager'
op|','
string|'"_call_novatools"'
op|','
name|'exploding_novatools'
op|')'
newline|'\n'
nl|'\n'
name|'zone_state'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneState'
op|'('
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'update_credentials'
op|'('
name|'FakeZone'
op|'('
name|'id'
op|'='
number|'2'
op|','
nl|'\n'
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'user2'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'pass2'"
op|')'
op|')'
newline|'\n'
name|'zone_state'
op|'.'
name|'attempt'
op|'='
name|'FLAGS'
op|'.'
name|'zone_failures_to_offline'
op|'-'
number|'1'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'zone_manager'
op|'.'
name|'_poll_zone'
op|'('
name|'zone_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zone_state'
op|'.'
name|'attempt'
op|','
number|'3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'zone_state'
op|'.'
name|'is_active'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'zone_state'
op|'.'
name|'name'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
