begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Piston Cloud Computing, Inc.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
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
string|'"""Test of Policy Engine For Nova"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'urllib2'
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
name|'exception'
newline|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PolicyFileTestCase
name|'class'
name|'PolicyFileTestCase'
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
name|'PolicyFileTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'target'
op|'='
op|'{'
op|'}'
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
name|'super'
op|'('
name|'PolicyFileTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modified_policy_reloads
dedent|''
name|'def'
name|'test_modified_policy_reloads'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'tmpfilename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'policy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'policy_file'
op|'='
name|'tmpfilename'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(uni): context construction invokes policy check to determin'
nl|'\n'
comment|'# is_admin or not. As a side-effect, policy reset is needed here'
nl|'\n'
comment|'# to flush existing policy cache.'
nl|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'action'
op|'='
string|'"example:test"'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'tmpfilename'
op|','
string|'"w"'
op|')'
name|'as'
name|'policyfile'
op|':'
newline|'\n'
indent|'                '
name|'policyfile'
op|'.'
name|'write'
op|'('
string|'"""{"example:test": ""}"""'
op|')'
newline|'\n'
dedent|''
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'tmpfilename'
op|','
string|'"w"'
op|')'
name|'as'
name|'policyfile'
op|':'
newline|'\n'
indent|'                '
name|'policyfile'
op|'.'
name|'write'
op|'('
string|'"""{"example:test": "!"}"""'
op|')'
newline|'\n'
comment|"# NOTE(vish): reset stored policy cache so we don't have to"
nl|'\n'
comment|'# sleep(1)'
nl|'\n'
dedent|''
name|'policy'
op|'.'
name|'_POLICY_CACHE'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PolicyTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'PolicyTestCase'
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
name|'PolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): preload rules to circumvent reloading from file'
nl|'\n'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
name|'rules'
op|'='
op|'{'
nl|'\n'
string|'"true"'
op|':'
string|"'@'"
op|','
nl|'\n'
string|'"example:allowed"'
op|':'
string|"'@'"
op|','
nl|'\n'
string|'"example:denied"'
op|':'
string|'"!"'
op|','
nl|'\n'
string|'"example:get_http"'
op|':'
string|'"http://www.example.com"'
op|','
nl|'\n'
string|'"example:my_file"'
op|':'
string|'"role:compute_admin or "'
nl|'\n'
string|'"project_id:%(project_id)s"'
op|','
nl|'\n'
string|'"example:early_and_fail"'
op|':'
string|'"! and @"'
op|','
nl|'\n'
string|'"example:early_or_success"'
op|':'
string|'"@ or !"'
op|','
nl|'\n'
string|'"example:lowercase_admin"'
op|':'
string|'"role:admin or role:sysadmin"'
op|','
nl|'\n'
string|'"example:uppercase_admin"'
op|':'
string|'"role:ADMIN or role:sysadmin"'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'# NOTE(vish): then overload underlying brain'
nl|'\n'
name|'common_policy'
op|'.'
name|'set_rules'
op|'('
name|'common_policy'
op|'.'
name|'Rules'
op|'('
nl|'\n'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
name|'v'
op|')'
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
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'roles'
op|'='
op|'['
string|"'member'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'target'
op|'='
op|'{'
op|'}'
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
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'PolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_nonexistent_action_throws
dedent|''
name|'def'
name|'test_enforce_nonexistent_action_throws'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:noexist"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_bad_action_throws
dedent|''
name|'def'
name|'test_enforce_bad_action_throws'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:denied"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_bad_action_noraise
dedent|''
name|'def'
name|'test_enforce_bad_action_noraise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:denied"'
newline|'\n'
name|'result'
op|'='
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_good_action
dedent|''
name|'def'
name|'test_enforce_good_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:allowed"'
newline|'\n'
name|'result'
op|'='
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_http_true
dedent|''
name|'def'
name|'test_enforce_http_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fakeurlopen
indent|'        '
name|'def'
name|'fakeurlopen'
op|'('
name|'url'
op|','
name|'post_data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"True"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'urllib2'
op|','
string|"'urlopen'"
op|','
name|'fakeurlopen'
op|')'
newline|'\n'
name|'action'
op|'='
string|'"example:get_http"'
newline|'\n'
name|'target'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enforce_http_false
dedent|''
name|'def'
name|'test_enforce_http_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fakeurlopen
indent|'        '
name|'def'
name|'fakeurlopen'
op|'('
name|'url'
op|','
name|'post_data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
string|'"False"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'urllib2'
op|','
string|"'urlopen'"
op|','
name|'fakeurlopen'
op|')'
newline|'\n'
name|'action'
op|'='
string|'"example:get_http"'
newline|'\n'
name|'target'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_templatized_enforcement
dedent|''
name|'def'
name|'test_templatized_enforcement'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target_mine'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
name|'target_not_mine'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'another'"
op|'}'
newline|'\n'
name|'action'
op|'='
string|'"example:my_file"'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'target_mine'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'target_not_mine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_early_AND_enforcement
dedent|''
name|'def'
name|'test_early_AND_enforcement'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:early_and_fail"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_early_OR_enforcement
dedent|''
name|'def'
name|'test_early_OR_enforcement'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
string|'"example:early_or_success"'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ignore_case_role_check
dedent|''
name|'def'
name|'test_ignore_case_role_check'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lowercase_action'
op|'='
string|'"example:lowercase_admin"'
newline|'\n'
name|'uppercase_action'
op|'='
string|'"example:uppercase_admin"'
newline|'\n'
comment|'# NOTE(dprince) we mix case in the Admin role here to ensure'
nl|'\n'
comment|'# case is ignored'
nl|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'admin'"
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
name|'roles'
op|'='
op|'['
string|"'AdMiN'"
op|']'
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'admin_context'
op|','
name|'lowercase_action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'admin_context'
op|','
name|'uppercase_action'
op|','
name|'self'
op|'.'
name|'target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DefaultPolicyTestCase
dedent|''
dedent|''
name|'class'
name|'DefaultPolicyTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'DefaultPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'rules'
op|'='
op|'{'
nl|'\n'
string|'"default"'
op|':'
string|"''"
op|','
nl|'\n'
string|'"example:exist"'
op|':'
string|'"!"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_set_rules'
op|'('
string|"'default'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_rules
dedent|''
name|'def'
name|'_set_rules'
op|'('
name|'self'
op|','
name|'default_rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
name|'common_policy'
op|'.'
name|'Rules'
op|'('
nl|'\n'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
name|'v'
op|')'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'self'
op|'.'
name|'rules'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|','
name|'default_rule'
op|')'
newline|'\n'
name|'common_policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
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
name|'super'
op|'('
name|'DefaultPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_policy_called
dedent|''
name|'def'
name|'test_policy_called'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|'"example:exist"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_found_policy_calls_default
dedent|''
name|'def'
name|'test_not_found_policy_calls_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|'"example:noexist"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_not_found
dedent|''
name|'def'
name|'test_default_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_set_rules'
op|'('
string|'"default_noexist"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'policy'
op|'.'
name|'enforce'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|'"example:noexist"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IsAdminCheckTestCase
dedent|''
dedent|''
name|'class'
name|'IsAdminCheckTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_init_true
indent|'    '
name|'def'
name|'test_init_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check'
op|'='
name|'policy'
op|'.'
name|'IsAdminCheck'
op|'('
string|"'is_admin'"
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'kind'
op|','
string|"'is_admin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'match'
op|','
string|"'True'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'expected'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_init_false
dedent|''
name|'def'
name|'test_init_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check'
op|'='
name|'policy'
op|'.'
name|'IsAdminCheck'
op|'('
string|"'is_admin'"
op|','
string|"'nottrue'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'kind'
op|','
string|"'is_admin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'match'
op|','
string|"'False'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'.'
name|'expected'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_true
dedent|''
name|'def'
name|'test_call_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check'
op|'='
name|'policy'
op|'.'
name|'IsAdminCheck'
op|'('
string|"'is_admin'"
op|','
string|"'True'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
string|"'target'"
op|','
name|'dict'
op|'('
name|'is_admin'
op|'='
name|'True'
op|')'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
string|"'target'"
op|','
name|'dict'
op|'('
name|'is_admin'
op|'='
name|'False'
op|')'
op|')'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_false
dedent|''
name|'def'
name|'test_call_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check'
op|'='
name|'policy'
op|'.'
name|'IsAdminCheck'
op|'('
string|"'is_admin'"
op|','
string|"'False'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
string|"'target'"
op|','
name|'dict'
op|'('
name|'is_admin'
op|'='
name|'True'
op|')'
op|')'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
string|"'target'"
op|','
name|'dict'
op|'('
name|'is_admin'
op|'='
name|'False'
op|')'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
