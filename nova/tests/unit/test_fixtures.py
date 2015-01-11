begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
name|'as'
name|'fx'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'conf_fixture'
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
DECL|class|TestConfFixture
name|'class'
name|'TestConfFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test the Conf fixtures in Nova.\n\n    This is a basic test that this fixture works like we expect.\n\n    Expectations:\n\n    1. before using the fixture, a default value (api_paste_config)\n       comes through untouched.\n\n    2. before using the fixture, a known default value that we\n       override is correct.\n\n    3. after using the fixture a known value that we override is the\n       new value.\n\n    4. after using the fixture we can set a default value to something\n       random, and it will be reset once we are done.\n\n    There are 2 copies of this test so that you can verify they do the\n    right thing with:\n\n       tox -e py27 test_fixtures -- --concurrency=1\n\n    As regardless of run order, their initial asserts would be\n    impacted if the reset behavior isn\'t working correctly.\n\n    """'
newline|'\n'
DECL|member|_test_override
name|'def'
name|'_test_override'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'api_paste_config'
op|','
string|"'api-paste.ini'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'fake_network'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'fake_network'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override1
dedent|''
name|'def'
name|'test_override1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override2
dedent|''
name|'def'
name|'test_override2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestOutputStream
dedent|''
dedent|''
name|'class'
name|'TestOutputStream'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure Output Stream capture works as expected.\n\n    This has the added benefit of providing a code example of how you\n    can manipulate the output stream in your own tests.\n    """'
newline|'\n'
DECL|member|test_output
name|'def'
name|'test_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'out'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'OutputStreamCapture'
op|'('
op|')'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
string|'"foo"'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'"bar"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'out'
op|'.'
name|'stdout'
op|','
string|'"foo"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'out'
op|'.'
name|'stderr'
op|','
string|'"bar"'
op|')'
newline|'\n'
comment|"# TODO(sdague): nuke the out and err buffers so it doesn't"
nl|'\n'
comment|'# make it to testr'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLogging
dedent|''
dedent|''
name|'class'
name|'TestLogging'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_default_logging
indent|'    '
name|'def'
name|'test_default_logging'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stdlog'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StandardLogging'
op|'('
op|')'
op|')'
newline|'\n'
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
comment|'# there should be a null handler as well at DEBUG'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'root'
op|'.'
name|'handlers'
op|')'
op|','
number|'2'
op|','
name|'root'
op|'.'
name|'handlers'
op|')'
newline|'\n'
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'info'
op|'('
string|'"at info"'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'debug'
op|'('
string|'"at debug"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"at debug"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
comment|'# broken debug messages should still explode, even though we'
nl|'\n'
comment|"# aren't logging them in the regular handler"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'log'
op|'.'
name|'debug'
op|','
string|'"this is broken %s %s"'
op|','
string|'"foo"'
op|')'
newline|'\n'
nl|'\n'
comment|"# and, ensure that one of the terrible log messages isn't"
nl|'\n'
comment|'# output at info'
nl|'\n'
name|'warn_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'migrate.versioning.api'"
op|')'
newline|'\n'
name|'warn_log'
op|'.'
name|'info'
op|'('
string|'"warn_log at info, should be skipped"'
op|')'
newline|'\n'
name|'warn_log'
op|'.'
name|'error'
op|'('
string|'"warn_log at error"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"warn_log at error"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"warn_log at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_debug_logging
dedent|''
name|'def'
name|'test_debug_logging'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fx'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'OS_DEBUG'"
op|','
string|"'1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'stdlog'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StandardLogging'
op|'('
op|')'
op|')'
newline|'\n'
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
comment|'# there should no longer be a null handler'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'root'
op|'.'
name|'handlers'
op|')'
op|','
number|'1'
op|','
name|'root'
op|'.'
name|'handlers'
op|')'
newline|'\n'
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'info'
op|'('
string|'"at info"'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'debug'
op|'('
string|'"at debug"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at info"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"at debug"'
op|','
name|'stdlog'
op|'.'
name|'logger'
op|'.'
name|'output'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTimeout
dedent|''
dedent|''
name|'class'
name|'TestTimeout'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests for our timeout fixture.\n\n    Testing the actual timeout mechanism is beyond the scope of this\n    test, because it\'s a pretty clear pass through to fixtures\'\n    timeout fixture, which tested in their tree.\n\n    """'
newline|'\n'
DECL|member|test_scaling
name|'def'
name|'test_scaling'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# a bad scaling factor'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'fixtures'
op|'.'
name|'Timeout'
op|','
number|'1'
op|','
number|'0.5'
op|')'
newline|'\n'
nl|'\n'
comment|'# various things that should work.'
nl|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'timeout'
op|'.'
name|'test_timeout'
op|','
number|'10'
op|')'
newline|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
string|'"10"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'timeout'
op|'.'
name|'test_timeout'
op|','
number|'10'
op|')'
newline|'\n'
name|'timeout'
op|'='
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
string|'"10"'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'timeout'
op|'.'
name|'test_timeout'
op|','
number|'20'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDatabaseFixture
dedent|''
dedent|''
name|'class'
name|'TestDatabaseFixture'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_fixture_reset
indent|'    '
name|'def'
name|'test_fixture_reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# because this sets up reasonable db connection strings'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'engine'
op|'='
name|'session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rows'
op|')'
op|','
number|'5'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# insert a 6th instance type, column 5 below is an int id'
nl|'\n'
comment|'# which has a constraint on it, so if new standard instance'
nl|'\n'
comment|'# types are added you have to bump it.'
nl|'\n'
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"insert into instance_types VALUES "'
nl|'\n'
string|'"(NULL, NULL, NULL, \'t1.test\', 6, 4096, 2, 0, NULL, \'87\'"'
nl|'\n'
string|'", 1.0, 40, 0, 0, 1, 0)"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rows'
op|')'
op|','
number|'6'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
nl|'\n'
comment|'# reset by invoking the fixture again'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# NOTE(sdague): it's important to reestablish the db"
nl|'\n'
comment|'# connection because otherwise we have a reference to the old'
nl|'\n'
comment|'# in mem db.'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'conn'
op|'.'
name|'execute'
op|'('
string|'"select * from instance_types"'
op|')'
newline|'\n'
name|'rows'
op|'='
name|'result'
op|'.'
name|'fetchall'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rows'
op|')'
op|','
number|'5'
op|','
string|'"Rows %s"'
op|'%'
name|'rows'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
