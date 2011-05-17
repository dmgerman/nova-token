begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
nl|'\n'
string|'"""Base classes for our unit tests.\n\nAllows overriding of flags for use of fakes, and some black magic for\ninline callbacks.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
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
name|'fakerabbit'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'sqlite_clean_db'"
op|','
string|"'clean.sqlite'"
op|','
nl|'\n'
string|"'File name of clean sqlite db'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'fake_tests'"
op|','
name|'True'
op|','
nl|'\n'
string|"'should we use everything for testing'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|skip_if_fake
name|'def'
name|'skip_if_fake'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator that skips a test if running in fake mode."""'
newline|'\n'
DECL|function|_skipper
name|'def'
name|'_skipper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wrapped skipper function."""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'unittest'
op|'.'
name|'SkipTest'
op|'('
string|"'Test cannot be run in fake mode'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_skipper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCase
dedent|''
name|'class'
name|'TestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case base class for all unit tests."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run before each test method to initialize test environment."""'
newline|'\n'
name|'super'
op|'('
name|'TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): We need a better method for creating fixtures for tests'
nl|'\n'
comment|'#             now that we have some required db setup for the system'
nl|'\n'
comment|'#             to work properly.'
nl|'\n'
name|'self'
op|'.'
name|'start'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'state_path'
op|','
name|'FLAGS'
op|'.'
name|'sqlite_clean_db'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'state_path'
op|','
name|'FLAGS'
op|'.'
name|'sqlite_db'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# emulate some of the mox stuff, we can't use the metaclass"
nl|'\n'
comment|'# because it screws with our generators'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flag_overrides'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'injected'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_services'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_monkey_patch_attach'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_monkey_patch_wsgi'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_original_flags'
op|'='
name|'FLAGS'
op|'.'
name|'FlagValuesDict'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Runs after each test method to tear down test environment."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'SmartUnsetAll'
op|'('
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
name|'super'
op|'('
name|'TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|"# Clean out fake_rabbit's queue if we used it"
nl|'\n'
indent|'            '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'                '
name|'fakerabbit'
op|'.'
name|'reset_all'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Reset any overriden flags'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Reset our monkey-patches'
nl|'\n'
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
op|'='
name|'self'
op|'.'
name|'original_attach'
newline|'\n'
name|'wsgi'
op|'.'
name|'Server'
op|'.'
name|'start'
op|'='
name|'self'
op|'.'
name|'original_start'
newline|'\n'
nl|'\n'
comment|'# Stop any timers'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'injected'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'x'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AssertionError'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
nl|'\n'
comment|'# Kill any services'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'_services'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'x'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|flags
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'flags'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Override flag variables for a test."""'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kw'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'flag_overrides'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'reset_flags'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|"'trying to override already overriden flag: %s'"
op|'%'
name|'k'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flag_overrides'
op|'['
name|'k'
op|']'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|')'
newline|'\n'
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_flags
dedent|''
dedent|''
name|'def'
name|'reset_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resets all flag variables for the test.\n\n        Runs after each test.\n\n        """'
newline|'\n'
name|'FLAGS'
op|'.'
name|'Reset'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'_original_flags'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'FLAGS'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_service
dedent|''
dedent|''
name|'def'
name|'start_service'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'host'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'host'
name|'and'
name|'host'
name|'or'
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'host'"
op|','
name|'host'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'setdefault'
op|'('
string|"'binary'"
op|','
string|"'nova-%s'"
op|'%'
name|'name'
op|')'
newline|'\n'
name|'svc'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'svc'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_services'
op|'.'
name|'append'
op|'('
name|'svc'
op|')'
newline|'\n'
name|'return'
name|'svc'
newline|'\n'
nl|'\n'
DECL|member|_monkey_patch_attach
dedent|''
name|'def'
name|'_monkey_patch_attach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'original_attach'
op|'='
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
newline|'\n'
nl|'\n'
DECL|function|_wrapped
name|'def'
name|'_wrapped'
op|'('
name|'inner_self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'='
name|'self'
op|'.'
name|'original_attach'
op|'('
name|'inner_self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'injected'
op|'.'
name|'append'
op|'('
name|'rv'
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
dedent|''
name|'_wrapped'
op|'.'
name|'func_name'
op|'='
name|'self'
op|'.'
name|'original_attach'
op|'.'
name|'func_name'
newline|'\n'
name|'rpc'
op|'.'
name|'Consumer'
op|'.'
name|'attach_to_eventlet'
op|'='
name|'_wrapped'
newline|'\n'
nl|'\n'
DECL|member|_monkey_patch_wsgi
dedent|''
name|'def'
name|'_monkey_patch_wsgi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allow us to kill servers spawned by wsgi.Server."""'
newline|'\n'
name|'self'
op|'.'
name|'original_start'
op|'='
name|'wsgi'
op|'.'
name|'Server'
op|'.'
name|'start'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'self'
op|'.'
name|'original_start'
op|')'
newline|'\n'
DECL|function|_wrapped_start
name|'def'
name|'_wrapped_start'
op|'('
name|'inner_self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'original_spawn_n'
op|'='
name|'inner_self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'original_spawn_n'
op|')'
newline|'\n'
DECL|function|_wrapped_spawn_n
name|'def'
name|'_wrapped_spawn_n'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'='
name|'greenthread'
op|'.'
name|'spawn'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_services'
op|'.'
name|'append'
op|'('
name|'rv'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'inner_self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
op|'='
name|'_wrapped_spawn_n'
newline|'\n'
name|'self'
op|'.'
name|'original_start'
op|'('
name|'inner_self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'inner_self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
op|'='
name|'original_spawn_n'
newline|'\n'
nl|'\n'
dedent|''
name|'_wrapped_start'
op|'.'
name|'func_name'
op|'='
name|'self'
op|'.'
name|'original_start'
op|'.'
name|'func_name'
newline|'\n'
name|'wsgi'
op|'.'
name|'Server'
op|'.'
name|'start'
op|'='
name|'_wrapped_start'
newline|'\n'
nl|'\n'
comment|'# Useful assertions'
nl|'\n'
DECL|member|assertDictMatch
dedent|''
name|'def'
name|'assertDictMatch'
op|'('
name|'self'
op|','
name|'d1'
op|','
name|'d2'
op|','
name|'approx_equal'
op|'='
name|'False'
op|','
name|'tolerance'
op|'='
number|'0.001'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Assert two dicts are equivalent.\n\n        This is a \'deep\' match in the sense that it handles nested\n        dictionaries appropriately.\n\n        NOTE:\n\n            If you don\'t care (or don\'t know) a given value, you can specify\n            the string DONTCARE as the value. This will cause that dict-item\n            to be skipped.\n\n        """'
newline|'\n'
DECL|function|raise_assertion
name|'def'
name|'raise_assertion'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d1str'
op|'='
name|'str'
op|'('
name|'d1'
op|')'
newline|'\n'
name|'d2str'
op|'='
name|'str'
op|'('
name|'d2'
op|')'
newline|'\n'
name|'base_msg'
op|'='
op|'('
string|"'Dictionaries do not match. %(msg)s d1: %(d1str)s '"
nl|'\n'
string|"'d2: %(d2str)s'"
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'AssertionError'
op|'('
name|'base_msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d1keys'
op|'='
name|'set'
op|'('
name|'d1'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'d2keys'
op|'='
name|'set'
op|'('
name|'d2'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'d1keys'
op|'!='
name|'d2keys'
op|':'
newline|'\n'
indent|'            '
name|'d1only'
op|'='
name|'d1keys'
op|'-'
name|'d2keys'
newline|'\n'
name|'d2only'
op|'='
name|'d2keys'
op|'-'
name|'d1keys'
newline|'\n'
name|'raise_assertion'
op|'('
string|"'Keys in d1 and not d2: %(d1only)s. '"
nl|'\n'
string|"'Keys in d2 and not d1: %(d2only)s'"
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'d1keys'
op|':'
newline|'\n'
indent|'            '
name|'d1value'
op|'='
name|'d1'
op|'['
name|'key'
op|']'
newline|'\n'
name|'d2value'
op|'='
name|'d2'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'error'
op|'='
name|'abs'
op|'('
name|'float'
op|'('
name|'d1value'
op|')'
op|'-'
name|'float'
op|'('
name|'d2value'
op|')'
op|')'
newline|'\n'
name|'within_tolerance'
op|'='
name|'error'
op|'<='
name|'tolerance'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|"# If both values aren't convertable to float, just ignore"
nl|'\n'
indent|'                '
name|'within_tolerance'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'d1value'
op|','
string|"'keys'"
op|')'
name|'and'
name|'hasattr'
op|'('
name|'d2value'
op|','
string|"'keys'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'d1value'
op|','
name|'d2value'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'DONTCARE'"
name|'in'
op|'('
name|'d1value'
op|','
name|'d2value'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'approx_equal'
name|'and'
name|'within_tolerance'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'d1value'
op|'!='
name|'d2value'
op|':'
newline|'\n'
indent|'                '
name|'raise_assertion'
op|'('
string|'"d1[\'%(key)s\']=%(d1value)s != "'
nl|'\n'
string|'"d2[\'%(key)s\']=%(d2value)s"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertDictListMatch
dedent|''
dedent|''
dedent|''
name|'def'
name|'assertDictListMatch'
op|'('
name|'self'
op|','
name|'L1'
op|','
name|'L2'
op|','
name|'approx_equal'
op|'='
name|'False'
op|','
name|'tolerance'
op|'='
number|'0.001'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Assert a list of dicts are equivalent."""'
newline|'\n'
DECL|function|raise_assertion
name|'def'
name|'raise_assertion'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'L1str'
op|'='
name|'str'
op|'('
name|'L1'
op|')'
newline|'\n'
name|'L2str'
op|'='
name|'str'
op|'('
name|'L2'
op|')'
newline|'\n'
name|'base_msg'
op|'='
op|'('
string|"'List of dictionaries do not match: %(msg)s '"
nl|'\n'
string|"'L1: %(L1str)s L2: %(L2str)s'"
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'AssertionError'
op|'('
name|'base_msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'L1count'
op|'='
name|'len'
op|'('
name|'L1'
op|')'
newline|'\n'
name|'L2count'
op|'='
name|'len'
op|'('
name|'L2'
op|')'
newline|'\n'
name|'if'
name|'L1count'
op|'!='
name|'L2count'
op|':'
newline|'\n'
indent|'            '
name|'raise_assertion'
op|'('
string|"'Length mismatch: len(L1)=%(L1count)d != '"
nl|'\n'
string|"'len(L2)=%(L2count)d'"
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'d1'
op|','
name|'d2'
name|'in'
name|'zip'
op|'('
name|'L1'
op|','
name|'L2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'d1'
op|','
name|'d2'
op|','
name|'approx_equal'
op|'='
name|'approx_equal'
op|','
nl|'\n'
name|'tolerance'
op|'='
name|'tolerance'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
