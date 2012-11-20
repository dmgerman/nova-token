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
string|'"""\n:mod:`nova.tests` -- Nova Unittests\n=====================================================\n\n.. automodule:: nova.tests\n   :platform: Unix\n"""'
newline|'\n'
nl|'\n'
comment|'# See http://code.google.com/p/python-nose/issues/detail?id=373'
nl|'\n'
comment|'# The code below enables nosetests to work with i18n _() blocks'
nl|'\n'
name|'import'
name|'__builtin__'
newline|'\n'
name|'setattr'
op|'('
name|'__builtin__'
op|','
string|"'_'"
op|','
name|'lambda'
name|'x'
op|':'
name|'x'
op|')'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_engine'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'logging'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
nl|'\n'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
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
name|'logging'
op|'.'
name|'setup'
op|'('
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DB
name|'_DB'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_db
name|'def'
name|'reset_db'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'CONF'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'        '
name|'engine'
op|'='
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'engine'
op|'.'
name|'dispose'
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
name|'if'
name|'_DB'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'.'
name|'connection'
op|'.'
name|'executescript'
op|'('
name|'_DB'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setup'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
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
name|'CONF'
op|'.'
name|'state_path'
op|','
name|'CONF'
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
name|'CONF'
op|'.'
name|'state_path'
op|','
name|'CONF'
op|'.'
name|'sqlite_db'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'mox'
comment|"# Fail fast if you don't have mox. Workaround for bug 810424"
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
name|'network'
name|'import'
name|'manager'
name|'as'
name|'network_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_flags'
newline|'\n'
name|'fake_flags'
op|'.'
name|'set_defaults'
op|'('
name|'CONF'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'migration'
op|'.'
name|'db_version'
op|'('
op|')'
op|'>'
name|'migration'
op|'.'
name|'INIT_VERSION'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'testdb'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'state_path'
op|','
name|'CONF'
op|'.'
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
indent|'            '
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'migration'
op|'.'
name|'db_sync'
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
name|'CONF'
op|'.'
name|'fixed_range'
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
indent|'        '
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
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'sql_connection'
op|'=='
string|'"sqlite://"'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'_DB'
newline|'\n'
name|'engine'
op|'='
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'cleandb'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'state_path'
op|','
name|'CONF'
op|'.'
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
dedent|''
dedent|''
endmarker|''
end_unit
