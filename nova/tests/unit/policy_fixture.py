begin_unit
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
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
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'fixtures'
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
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'policy'
name|'as'
name|'common_policy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'policy'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_policy'
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
DECL|class|PolicyFixture
name|'class'
name|'PolicyFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
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
name|'PolicyFixture'
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
name|'policy_dir'
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
newline|'\n'
name|'self'
op|'.'
name|'policy_file_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'policy_dir'
op|'.'
name|'path'
op|','
nl|'\n'
string|"'policy.json'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'policy_file_name'
op|','
string|"'w'"
op|')'
name|'as'
name|'policy_file'
op|':'
newline|'\n'
indent|'            '
name|'policy_file'
op|'.'
name|'write'
op|'('
name|'fake_policy'
op|'.'
name|'policy_data'
op|')'
newline|'\n'
dedent|''
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'policy_file'"
op|','
name|'self'
op|'.'
name|'policy_file_name'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'reset'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_rules
dedent|''
name|'def'
name|'set_rules'
op|'('
name|'self'
op|','
name|'rules'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policy'
op|'='
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'_ENFORCER'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'k'
op|':'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
name|'v'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'rules'
op|'.'
name|'items'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RoleBasedPolicyFixture
dedent|''
dedent|''
name|'class'
name|'RoleBasedPolicyFixture'
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
name|'role'
op|'='
string|'"admin"'
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
name|'super'
op|'('
name|'RoleBasedPolicyFixture'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
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
name|'role'
op|'='
name|'role'
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
string|'"""Copy live policy.json file and convert all actions to\n           allow users of the specified role only\n        """'
newline|'\n'
name|'super'
op|'('
name|'RoleBasedPolicyFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'='
name|'jsonutils'
op|'.'
name|'load'
op|'('
name|'open'
op|'('
name|'CONF'
op|'.'
name|'policy_file'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Convert all actions to require specified role'
nl|'\n'
name|'for'
name|'action'
op|','
name|'rule'
name|'in'
name|'policy'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'policy'
op|'['
name|'action'
op|']'
op|'='
string|"'role:%s'"
op|'%'
name|'self'
op|'.'
name|'role'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'policy_dir'
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
newline|'\n'
name|'self'
op|'.'
name|'policy_file_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'policy_dir'
op|'.'
name|'path'
op|','
nl|'\n'
string|"'policy.json'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'policy_file_name'
op|','
string|"'w'"
op|')'
name|'as'
name|'policy_file'
op|':'
newline|'\n'
indent|'            '
name|'jsonutils'
op|'.'
name|'dump'
op|'('
name|'policy'
op|','
name|'policy_file'
op|')'
newline|'\n'
dedent|''
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'policy_file'"
op|','
name|'self'
op|'.'
name|'policy_file_name'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'nova'
op|'.'
name|'policy'
op|'.'
name|'reset'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
