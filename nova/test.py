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
nl|'\n'
string|'"""Base classes for our unit tests.\n\nAllows overriding of flags for use of fakes, and some black magic for\ninline callbacks.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
name|'os'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'logging'
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
nl|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'concurrency'
name|'import'
name|'lockutils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'fixture'
name|'as'
name|'config_fixture'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'messaging'
name|'import'
name|'conffixture'
name|'as'
name|'messaging_conffixture'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'testtools'
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
op|'.'
name|'db'
name|'import'
name|'migration'
newline|'\n'
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
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'fixture'
name|'import'
name|'logging'
name|'as'
name|'log_fixture'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'fixture'
name|'import'
name|'moxstubout'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'nova_logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
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
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'conf_fixture'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'policy_fixture'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|test_opts
name|'test_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'sqlite_clean_db'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'clean.sqlite'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'File name of clean sqlite db'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'test_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enabled'"
op|','
string|"'nova.api.openstack'"
op|','
name|'group'
op|'='
string|"'osapi_v3'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'use_stderr'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'nova_logging'
op|'.'
name|'setup'
op|'('
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(comstud): Make sure we have all of the objects loaded. We do this'
nl|'\n'
comment|'# at module import time, because we may be using mock decorators in our'
nl|'\n'
comment|'# tests that run at import time.'
nl|'\n'
name|'objects'
op|'.'
name|'register_all'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DB_CACHE
name|'_DB_CACHE'
op|'='
name|'None'
newline|'\n'
DECL|variable|_TRUE_VALUES
name|'_TRUE_VALUES'
op|'='
op|'('
string|"'True'"
op|','
string|"'true'"
op|','
string|"'1'"
op|','
string|"'yes'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Database
name|'class'
name|'Database'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'db_session'
op|','
name|'db_migrate'
op|','
name|'sql_connection'
op|','
nl|'\n'
name|'sqlite_db'
op|','
name|'sqlite_clean_db'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sql_connection'
op|'='
name|'sql_connection'
newline|'\n'
name|'self'
op|'.'
name|'sqlite_db'
op|'='
name|'sqlite_db'
newline|'\n'
name|'self'
op|'.'
name|'sqlite_clean_db'
op|'='
name|'sqlite_clean_db'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|'='
name|'db_session'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'db_migrate'
op|'.'
name|'db_version'
op|'('
op|')'
op|'>'
name|'db_migrate'
op|'.'
name|'db_initial_version'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'testdb'
op|'='
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'sqlite_db'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'testdb'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'db_migrate'
op|'.'
name|'db_sync'
op|'('
op|')'
newline|'\n'
name|'if'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_DB'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'line'
name|'for'
name|'line'
name|'in'
name|'conn'
op|'.'
name|'connection'
op|'.'
name|'iterdump'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'engine'
op|'.'
name|'dispose'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cleandb'
op|'='
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'sqlite_clean_db'
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'testdb'
op|','
name|'cleandb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
dedent|''
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
name|'Database'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'self'
op|'.'
name|'engine'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'connection'
op|'.'
name|'executescript'
op|'('
name|'self'
op|'.'
name|'_DB'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'engine'
op|'.'
name|'dispose'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'copyfile'
op|'('
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'self'
op|'.'
name|'sqlite_clean_db'
op|')'
op|','
nl|'\n'
name|'paths'
op|'.'
name|'state_path_rel'
op|'('
name|'self'
op|'.'
name|'sqlite_db'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SampleNetworks
dedent|''
dedent|''
dedent|''
name|'class'
name|'SampleNetworks'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Create sample networks in the database."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'SampleNetworks'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'network_manager'
op|'.'
name|'VlanManager'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'bridge_interface'
op|'='
name|'CONF'
op|'.'
name|'flat_interface'
name|'or'
name|'CONF'
op|'.'
name|'vlan_interface'
newline|'\n'
name|'network'
op|'.'
name|'create_networks'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'label'
op|'='
string|"'test'"
op|','
nl|'\n'
name|'cidr'
op|'='
string|"'10.0.0.0/8'"
op|','
nl|'\n'
name|'multi_host'
op|'='
name|'CONF'
op|'.'
name|'multi_host'
op|','
nl|'\n'
name|'num_networks'
op|'='
name|'CONF'
op|'.'
name|'num_networks'
op|','
nl|'\n'
name|'network_size'
op|'='
name|'CONF'
op|'.'
name|'network_size'
op|','
nl|'\n'
name|'cidr_v6'
op|'='
name|'CONF'
op|'.'
name|'fixed_range_v6'
op|','
nl|'\n'
name|'gateway'
op|'='
name|'CONF'
op|'.'
name|'gateway'
op|','
nl|'\n'
name|'gateway_v6'
op|'='
name|'CONF'
op|'.'
name|'gateway_v6'
op|','
nl|'\n'
name|'bridge'
op|'='
name|'CONF'
op|'.'
name|'flat_network_bridge'
op|','
nl|'\n'
name|'bridge_interface'
op|'='
name|'bridge_interface'
op|','
nl|'\n'
name|'vpn_start'
op|'='
name|'CONF'
op|'.'
name|'vpn_start'
op|','
nl|'\n'
name|'vlan_start'
op|'='
name|'CONF'
op|'.'
name|'vlan_start'
op|','
nl|'\n'
name|'dns1'
op|'='
name|'CONF'
op|'.'
name|'flat_network_dns'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'db'
op|'.'
name|'network_get_all'
op|'('
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'.'
name|'set_network_host'
op|'('
name|'ctxt'
op|','
name|'net'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceFixture
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServiceFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run a service as a test fixture."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
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
name|'name'
op|'='
name|'name'
newline|'\n'
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
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ServiceFixture'
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
name|'service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'kill'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TranslationFixture
dedent|''
dedent|''
name|'class'
name|'TranslationFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use gettext NullTranslation objects in tests."""'
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
name|'super'
op|'('
name|'TranslationFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'nulltrans'
op|'='
name|'gettext'
op|'.'
name|'NullTranslations'
op|'('
op|')'
newline|'\n'
name|'gettext_fixture'
op|'='
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'gettext.translation'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'x'
op|','
op|'**'
name|'y'
op|':'
name|'nulltrans'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'gettext_patcher'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'gettext_fixture'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestingException
dedent|''
dedent|''
name|'class'
name|'TestingException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullHandler
dedent|''
name|'class'
name|'NullHandler'
op|'('
name|'logging'
op|'.'
name|'Handler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""custom default NullHandler to attempt to format the record.\n\n    Used in conjunction with\n    log_fixture.get_logging_handle_error_fixture to detect formatting errors in\n    debug level logs without saving the logs.\n    """'
newline|'\n'
DECL|member|handle
name|'def'
name|'handle'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'format'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
DECL|member|emit
dedent|''
name|'def'
name|'emit'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|createLock
dedent|''
name|'def'
name|'createLock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'lock'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCase
dedent|''
dedent|''
name|'class'
name|'TestCase'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case base class for all unit tests.\n\n    Due to the slowness of DB access, please consider deriving from\n    `NoDBTestCase` first.\n    """'
newline|'\n'
DECL|variable|USES_DB
name|'USES_DB'
op|'='
name|'True'
newline|'\n'
DECL|variable|REQUIRES_LOCKING
name|'REQUIRES_LOCKING'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|variable|TIMEOUT_SCALING_FACTOR
name|'TIMEOUT_SCALING_FACTOR'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_setup_timeouts
name|'def'
name|'_setup_timeouts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup per test timeouts.\n\n        In order to avoid test deadlocks we support setting up a test\n        timeout parameter read from the environment. In almost all\n        cases where the timeout is reached this means a deadlock.\n\n        A class level TIMEOUT_SCALING_FACTOR also exists, which allows\n        extremely long tests to specify they need more time.\n        """'
newline|'\n'
name|'test_timeout'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_TEST_TIMEOUT'"
op|','
number|'0'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'test_timeout'
op|'='
name|'int'
op|'('
name|'test_timeout'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# If timeout value is invalid do not set a timeout.'
nl|'\n'
indent|'            '
name|'test_timeout'
op|'='
number|'0'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'TIMEOUT_SCALING_FACTOR'
op|'>='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'test_timeout'
op|'*='
name|'self'
op|'.'
name|'TIMEOUT_SCALING_FACTOR'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
string|"'TIMEOUT_SCALING_FACTOR value must be >= 1'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'test_timeout'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Timeout'
op|'('
name|'test_timeout'
op|','
name|'gentle'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_logging
dedent|''
dedent|''
name|'def'
name|'_setup_logging'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup Logging redirection for tests.\n\n        There are a number of things we want to handle with logging in tests:\n\n        * Redirect the logging to somewhere that we can test or dump it later.\n\n        * Ensure that as many DEBUG messages as possible are actually\n          executed, to ensure they are actually syntactically valid\n          (they often have not been).\n\n        * Ensure that we create useful output for tests that doesn\'t\n          overwhelm the testing system (which means we can\'t capture\n          the 100 MB of debug logging on every run).\n\n        To do this we create a logger fixture at the root level, which\n        defaults to INFO and create a Null Logger at DEBUG which lets\n        us execute log messages at DEBUG but not keep the output.\n\n        To support local debugging OS_DEBUG=True can be set in the\n        environment, which will print out the full debug logging.\n\n        There are also a set of overrides for particularly verbose\n        modules to be even less than INFO.\n\n        """'
newline|'\n'
comment|'# set root logger to debug'
nl|'\n'
name|'root'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'root'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
comment|'# supports collecting debug level for local runs'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_DEBUG'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'level'
op|'='
name|'logging'
op|'.'
name|'DEBUG'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'level'
op|'='
name|'logging'
op|'.'
name|'INFO'
newline|'\n'
nl|'\n'
comment|'# Collect logs'
nl|'\n'
dedent|''
name|'fs'
op|'='
string|"'%(asctime)s %(levelname)s [%(name)s] %(message)s'"
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'FakeLogger'
op|'('
name|'format'
op|'='
name|'fs'
op|','
name|'level'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'handlers'
op|'['
number|'0'
op|']'
op|'.'
name|'setLevel'
op|'('
name|'level'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'level'
op|'>'
name|'logging'
op|'.'
name|'DEBUG'
op|':'
newline|'\n'
comment|"# Just attempt to format debug level logs, but don't save them"
nl|'\n'
indent|'            '
name|'handler'
op|'='
name|'NullHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'LogHandler'
op|'('
name|'handler'
op|','
name|'nuke_handlers'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
comment|"# Don't log every single DB migration step"
nl|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
nl|'\n'
string|"'migrate.versioning.api'"
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARNING'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
dedent|''
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
name|'self'
op|'.'
name|'_setup_timeouts'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'NestedTempfile'
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
name|'TempHomeDir'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'TranslationFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'log_fixture'
op|'.'
name|'get_logging_handle_error_fixture'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDOUT_CAPTURE'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'stdout'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StringStream'
op|'('
string|"'stdout'"
op|')'
op|')'
op|'.'
name|'stream'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stdout'"
op|','
name|'stdout'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'OS_STDERR_CAPTURE'"
op|')'
name|'in'
name|'_TRUE_VALUES'
op|':'
newline|'\n'
indent|'            '
name|'stderr'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'StringStream'
op|'('
string|"'stderr'"
op|')'
op|')'
op|'.'
name|'stream'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'sys.stderr'"
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'add_extra_exmods'
op|'('
string|"'nova.test'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'rpc'
op|'.'
name|'clear_extra_exmods'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'rpc'
op|'.'
name|'cleanup'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_setup_logging'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sdague): because of the way we were using the lock'
nl|'\n'
comment|'# wrapper we eneded up with a lot of tests that started'
nl|'\n'
comment|'# relying on global external locking being set up for them. We'
nl|'\n'
comment|'# consider all of these to be *bugs*. Tests should not require'
nl|'\n'
comment|'# global external locking, or if they do, they should'
nl|'\n'
comment|'# explicitly set it up themselves.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The following REQUIRES_LOCKING class parameter is provided'
nl|'\n'
comment|'# as a bridge to get us there. No new tests should be added'
nl|'\n'
comment|'# that require it, and existing classes and tests should be'
nl|'\n'
comment|'# fixed to not need it.'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'REQUIRES_LOCKING'
op|':'
newline|'\n'
indent|'            '
name|'lock_path'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'config_fixture'
op|'.'
name|'Config'
op|'('
name|'lockutils'
op|'.'
name|'CONF'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fixture'
op|'.'
name|'config'
op|'('
name|'lock_path'
op|'='
name|'lock_path'
op|','
nl|'\n'
name|'group'
op|'='
string|"'oslo_concurrency'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'conf_fixture'
op|'.'
name|'ConfFixture'
op|'('
name|'CONF'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'messaging_conf'
op|'='
name|'messaging_conffixture'
op|'.'
name|'ConfFixture'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'messaging_conf'
op|'.'
name|'transport_driver'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'self'
op|'.'
name|'messaging_conf'
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'init'
op|'('
name|'CONF'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'USES_DB'
op|':'
newline|'\n'
indent|'            '
name|'global'
name|'_DB_CACHE'
newline|'\n'
name|'if'
name|'not'
name|'_DB_CACHE'
op|':'
newline|'\n'
indent|'                '
name|'_DB_CACHE'
op|'='
name|'Database'
op|'('
name|'session'
op|','
name|'migration'
op|','
nl|'\n'
name|'sql_connection'
op|'='
name|'CONF'
op|'.'
name|'database'
op|'.'
name|'connection'
op|','
nl|'\n'
name|'sqlite_db'
op|'='
name|'CONF'
op|'.'
name|'database'
op|'.'
name|'sqlite_db'
op|','
nl|'\n'
name|'sqlite_clean_db'
op|'='
name|'CONF'
op|'.'
name|'sqlite_clean_db'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'_DB_CACHE'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): Make sure to reset us back to non-remote objects'
nl|'\n'
comment|'# for each test to avoid interactions. Also, backup the object'
nl|'\n'
comment|'# registry.'
nl|'\n'
dedent|''
name|'objects_base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_base_test_obj_backup'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
nl|'\n'
name|'objects_base'
op|'.'
name|'NovaObject'
op|'.'
name|'_obj_classes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_restore_obj_registry'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mnaser): All calls to utils.is_neutron() are cached in'
nl|'\n'
comment|'# nova.utils._IS_NEUTRON.  We set it to None to avoid any'
nl|'\n'
comment|'# caching of that value.'
nl|'\n'
name|'utils'
op|'.'
name|'_IS_NEUTRON'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'mox_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'moxstubout'
op|'.'
name|'MoxStubout'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox_fixture'
op|'.'
name|'mox'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'mox_fixture'
op|'.'
name|'stubs'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_clear_attrs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'EnvironmentVariable'
op|'('
string|"'http_proxy'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'PolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'fatal_exception_format_errors'"
op|','
name|'True'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'enabled'"
op|','
name|'True'
op|','
string|"'osapi_v3'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'force_dhcp_release'"
op|','
name|'False'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'periodic_enable'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_restore_obj_registry
dedent|''
name|'def'
name|'_restore_obj_registry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'objects_base'
op|'.'
name|'NovaObject'
op|'.'
name|'_obj_classes'
op|'='
name|'self'
op|'.'
name|'_base_test_obj_backup'
newline|'\n'
nl|'\n'
DECL|member|_clear_attrs
dedent|''
name|'def'
name|'_clear_attrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Delete attributes that don't start with _ so they don't pin"
nl|'\n'
comment|'# memory around unnecessarily for the duration of the test'
nl|'\n'
comment|'# suite'
nl|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'keys'
op|'('
op|')'
name|'if'
name|'k'
op|'['
number|'0'
op|']'
op|'!='
string|"'_'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'.'
name|'__dict__'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|flags
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
name|'group'
op|'='
name|'kw'
op|'.'
name|'pop'
op|'('
string|"'group'"
op|','
name|'None'
op|')'
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
name|'CONF'
op|'.'
name|'set_override'
op|'('
name|'k'
op|','
name|'v'
op|','
name|'group'
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
name|'svc'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'ServiceFixture'
op|'('
name|'name'
op|','
name|'host'
op|','
op|'**'
name|'kwargs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'svc'
op|'.'
name|'service'
newline|'\n'
nl|'\n'
DECL|member|assertPublicAPISignatures
dedent|''
name|'def'
name|'assertPublicAPISignatures'
op|'('
name|'self'
op|','
name|'baseinst'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
DECL|function|get_public_apis
indent|'        '
name|'def'
name|'get_public_apis'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'methods'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
op|'('
name|'name'
op|','
name|'value'
op|')'
name|'in'
name|'inspect'
op|'.'
name|'getmembers'
op|'('
name|'inst'
op|','
name|'inspect'
op|'.'
name|'ismethod'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'name'
op|'.'
name|'startswith'
op|'('
string|'"_"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'methods'
op|'['
name|'name'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'methods'
newline|'\n'
nl|'\n'
dedent|''
name|'baseclass'
op|'='
name|'baseinst'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'basemethods'
op|'='
name|'get_public_apis'
op|'('
name|'baseinst'
op|')'
newline|'\n'
name|'implmethods'
op|'='
name|'get_public_apis'
op|'('
name|'inst'
op|')'
newline|'\n'
nl|'\n'
name|'extranames'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'sorted'
op|'('
name|'implmethods'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
name|'not'
name|'in'
name|'basemethods'
op|':'
newline|'\n'
indent|'                '
name|'extranames'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'extranames'
op|','
nl|'\n'
string|'"public APIs not listed in base class %s"'
op|'%'
nl|'\n'
name|'baseclass'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'name'
name|'in'
name|'sorted'
op|'('
name|'implmethods'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'baseargs'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'basemethods'
op|'['
name|'name'
op|']'
op|')'
newline|'\n'
name|'implargs'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'implmethods'
op|'['
name|'name'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'baseargs'
op|','
name|'implargs'
op|','
nl|'\n'
string|'"%s args don\'t match base class %s"'
op|'%'
nl|'\n'
op|'('
name|'name'
op|','
name|'baseclass'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APICoverage
dedent|''
dedent|''
dedent|''
name|'class'
name|'APICoverage'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|cover_api
indent|'    '
name|'cover_api'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|test_api_methods
name|'def'
name|'test_api_methods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'cover_api'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'api_methods'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'dir'
op|'('
name|'self'
op|'.'
name|'cover_api'
op|')'
nl|'\n'
name|'if'
name|'not'
name|'x'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|']'
newline|'\n'
name|'test_methods'
op|'='
op|'['
name|'x'
op|'['
number|'5'
op|':'
op|']'
name|'for'
name|'x'
name|'in'
name|'dir'
op|'('
name|'self'
op|')'
nl|'\n'
name|'if'
name|'x'
op|'.'
name|'startswith'
op|'('
string|"'test_'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
nl|'\n'
name|'test_methods'
op|','
nl|'\n'
name|'testtools'
op|'.'
name|'matchers'
op|'.'
name|'ContainsAll'
op|'('
name|'api_methods'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimeOverride
dedent|''
dedent|''
name|'class'
name|'TimeOverride'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixture to start and remove time override."""'
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
name|'super'
op|'('
name|'TimeOverride'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'timeutils'
op|'.'
name|'clear_time_override'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoDBTestCase
dedent|''
dedent|''
name|'class'
name|'NoDBTestCase'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""`NoDBTestCase` differs from TestCase in that DB access is not supported.\n    This makes tests run significantly faster. If possible, all new tests\n    should derive from this class.\n    """'
newline|'\n'
DECL|variable|USES_DB
name|'USES_DB'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseHookTestCase
dedent|''
name|'class'
name|'BaseHookTestCase'
op|'('
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|assert_has_hook
indent|'    '
name|'def'
name|'assert_has_hook'
op|'('
name|'self'
op|','
name|'expected_name'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'func'
op|','
string|"'__hook_name__'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_name'
op|','
name|'func'
op|'.'
name|'__hook_name__'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
