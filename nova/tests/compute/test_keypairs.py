begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
string|'"""Tests for keypair API."""'
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
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'compute'
name|'import'
name|'test_compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_keypair'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeypairAPITestCase
name|'class'
name|'KeypairAPITestCase'
op|'('
name|'test_compute'
op|'.'
name|'BaseTestCase'
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
name|'KeypairAPITestCase'
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
name|'keypair_api'
op|'='
name|'compute_api'
op|'.'
name|'KeypairAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ctxt'
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
name|'_keypair_db_call_stubs'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|'='
string|"'fake existing key name'"
newline|'\n'
name|'self'
op|'.'
name|'pub_key'
op|'='
op|'('
string|"'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLnVkqJu9WVf'"
nl|'\n'
string|"'/5StU3JCrBR2r1s1j8K1tux+5XeSvdqaM8lMFNorzbY5iyoBbR'"
nl|'\n'
string|"'S56gy1jmm43QsMPJsrpfUZKcJpRENSe3OxIIwWXRoiapZe78u/'"
nl|'\n'
string|"'a9xKwj0avFYMcws9Rk9iAB7W4K1nEJbyCPl5lRBoyqeHBqrnnu'"
nl|'\n'
string|"'XWEgGxJCK0Ah6wcOzwlEiVjdf4kxzXrwPHyi7Ea1qvnNXTziF8'"
nl|'\n'
string|"'yYmUlH4C8UXfpTQckwSwpDyxZUc63P8q+vPbs3Q2kw+/7vvkCK'"
nl|'\n'
string|"'HJAXVI+oCiyMMfffoTq16M1xfV58JstgtTqAXG+ZFpicGajREU'"
nl|'\n'
string|"'E/E3hO5MGgcHmyzIrWHKpe1n3oEGuz'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fingerprint'
op|'='
string|"'4e:48:c6:a0:4a:f9:dd:b5:4c:85:54:5a:af:43:47:5a'"
newline|'\n'
name|'self'
op|'.'
name|'key_destroyed'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_keypair_db_call_stubs
dedent|''
name|'def'
name|'_keypair_db_call_stubs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|db_key_pair_get_all_by_user
indent|'        '
name|'def'
name|'db_key_pair_get_all_by_user'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'dict'
op|'('
name|'test_keypair'
op|'.'
name|'fake_keypair'
op|','
nl|'\n'
name|'name'
op|'='
name|'self'
op|'.'
name|'existing_key_name'
op|','
nl|'\n'
name|'public_key'
op|'='
name|'self'
op|'.'
name|'pub_key'
op|','
nl|'\n'
name|'fingerprint'
op|'='
name|'self'
op|'.'
name|'fingerprint'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|db_key_pair_create
dedent|''
name|'def'
name|'db_key_pair_create'
op|'('
name|'context'
op|','
name|'keypair'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'test_keypair'
op|'.'
name|'fake_keypair'
op|','
op|'**'
name|'keypair'
op|')'
newline|'\n'
nl|'\n'
DECL|function|db_key_pair_destroy
dedent|''
name|'def'
name|'db_key_pair_destroy'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
name|'self'
op|'.'
name|'existing_key_name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'key_destroyed'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|db_key_pair_get
dedent|''
dedent|''
name|'def'
name|'db_key_pair_get'
op|'('
name|'context'
op|','
name|'user_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
name|'self'
op|'.'
name|'existing_key_name'
name|'and'
name|'not'
name|'self'
op|'.'
name|'key_destroyed'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'dict'
op|'('
name|'test_keypair'
op|'.'
name|'fake_keypair'
op|','
nl|'\n'
name|'name'
op|'='
name|'self'
op|'.'
name|'existing_key_name'
op|','
nl|'\n'
name|'public_key'
op|'='
name|'self'
op|'.'
name|'pub_key'
op|','
nl|'\n'
name|'fingerprint'
op|'='
name|'self'
op|'.'
name|'fingerprint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'KeypairNotFound'
op|'('
name|'user_id'
op|'='
name|'user_id'
op|','
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_get_all_by_user"'
op|','
nl|'\n'
name|'db_key_pair_get_all_by_user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_create"'
op|','
nl|'\n'
name|'db_key_pair_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_destroy"'
op|','
nl|'\n'
name|'db_key_pair_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_get"'
op|','
nl|'\n'
name|'db_key_pair_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_notifications
dedent|''
name|'def'
name|'_check_notifications'
op|'('
name|'self'
op|','
name|'action'
op|'='
string|"'create'"
op|','
name|'key_name'
op|'='
string|"'foo'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'n1'
op|'='
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'INFO'"
op|','
name|'n1'
op|'.'
name|'priority'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'keypair.%s.start'"
op|'%'
name|'action'
op|','
name|'n1'
op|'.'
name|'event_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'api.%s'"
op|'%'
name|'CONF'
op|'.'
name|'host'
op|','
name|'n1'
op|'.'
name|'publisher_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake'"
op|','
name|'n1'
op|'.'
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake'"
op|','
name|'n1'
op|'.'
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'key_name'
op|','
name|'n1'
op|'.'
name|'payload'
op|'['
string|"'key_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'n2'
op|'='
name|'fake_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'INFO'"
op|','
name|'n2'
op|'.'
name|'priority'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'keypair.%s.end'"
op|'%'
name|'action'
op|','
name|'n2'
op|'.'
name|'event_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'api.%s'"
op|'%'
name|'CONF'
op|'.'
name|'host'
op|','
name|'n2'
op|'.'
name|'publisher_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake'"
op|','
name|'n2'
op|'.'
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake'"
op|','
name|'n2'
op|'.'
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'key_name'
op|','
name|'n2'
op|'.'
name|'payload'
op|'['
string|"'key_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateImportSharedTestMixIn
dedent|''
dedent|''
name|'class'
name|'CreateImportSharedTestMixIn'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests shared between create and import_key.\n\n    Mix-in pattern is used here so that these `test_*` methods aren\'t picked\n    up by the test runner unless they are part of a \'concrete\' test case.\n    """'
newline|'\n'
nl|'\n'
DECL|member|assertKeyNameRaises
name|'def'
name|'assertKeyNameRaises'
op|'('
name|'self'
op|','
name|'exc_class'
op|','
name|'expected_message'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'keypair_api'
op|','
name|'self'
op|'.'
name|'func_name'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'func_name'
op|'=='
string|"'import_key_pair'"
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'pub_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc_class'
op|','
name|'func'
op|','
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'name'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_message'
op|','
name|'unicode'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertInvalidKeypair
dedent|''
name|'def'
name|'assertInvalidKeypair'
op|'('
name|'self'
op|','
name|'expected_message'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Keypair data is invalid'"
op|')'
op|'+'
string|"': '"
op|'+'
name|'expected_message'
newline|'\n'
name|'self'
op|'.'
name|'assertKeyNameRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidKeypair'
op|','
name|'msg'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_name_too_short
dedent|''
name|'def'
name|'test_name_too_short'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Keypair name must be between 1 and 255 characters long'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertInvalidKeypair'
op|'('
name|'msg'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_name_too_long
dedent|''
name|'def'
name|'test_name_too_long'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Keypair name must be between 1 and 255 characters long'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertInvalidKeypair'
op|'('
name|'msg'
op|','
string|"'x'"
op|'*'
number|'256'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_chars
dedent|''
name|'def'
name|'test_invalid_chars'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Keypair name contains unsafe characters"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertInvalidKeypair'
op|'('
name|'msg'
op|','
string|"'* BAD CHARACTERS!  *'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_already_exists
dedent|''
name|'def'
name|'test_already_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|db_key_pair_create_duplicate
indent|'        '
name|'def'
name|'db_key_pair_create_duplicate'
op|'('
name|'context'
op|','
name|'keypair'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'KeyPairExists'
op|'('
name|'key_name'
op|'='
name|'keypair'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|'"key_pair_create"'
op|','
name|'db_key_pair_create_duplicate'
op|')'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Key pair \'%(key_name)s\' already exists."'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'key_name'"
op|':'
name|'self'
op|'.'
name|'existing_key_name'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertKeyNameRaises'
op|'('
name|'exception'
op|'.'
name|'KeyPairExists'
op|','
name|'msg'
op|','
nl|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quota_limit
dedent|''
name|'def'
name|'test_quota_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_quotas_count
indent|'        '
name|'def'
name|'fake_quotas_count'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'resource'
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
name|'return'
name|'CONF'
op|'.'
name|'quota_key_pairs'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'QUOTAS'
op|','
string|'"count"'
op|','
name|'fake_quotas_count'
op|')'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Maximum number of key pairs exceeded"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertKeyNameRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairLimitExceeded'
op|','
name|'msg'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateKeypairTestCase
dedent|''
dedent|''
name|'class'
name|'CreateKeypairTestCase'
op|'('
name|'KeypairAPITestCase'
op|','
name|'CreateImportSharedTestMixIn'
op|')'
op|':'
newline|'\n'
DECL|variable|func_name
indent|'    '
name|'func_name'
op|'='
string|"'create_key_pair'"
newline|'\n'
nl|'\n'
DECL|member|test_success
name|'def'
name|'test_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keypair'
op|','
name|'private_key'
op|'='
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'create_key_pair'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'keypair'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_notifications'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImportKeypairTestCase
dedent|''
dedent|''
name|'class'
name|'ImportKeypairTestCase'
op|'('
name|'KeypairAPITestCase'
op|','
name|'CreateImportSharedTestMixIn'
op|')'
op|':'
newline|'\n'
DECL|variable|func_name
indent|'    '
name|'func_name'
op|'='
string|"'import_key_pair'"
newline|'\n'
nl|'\n'
DECL|member|test_success
name|'def'
name|'test_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keypair'
op|'='
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'import_key_pair'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'foo'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'pub_key'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'foo'"
op|','
name|'keypair'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'fingerprint'
op|','
name|'keypair'
op|'['
string|"'fingerprint'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pub_key'
op|','
name|'keypair'
op|'['
string|"'public_key'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_notifications'
op|'('
name|'action'
op|'='
string|"'import'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_key_data
dedent|''
name|'def'
name|'test_bad_key_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidKeypair'
op|','
nl|'\n'
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'import_key_pair'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
string|"'foo'"
op|','
nl|'\n'
string|"'bad key data'"
op|')'
newline|'\n'
name|'msg'
op|'='
string|"u'Keypair data is invalid: failed to generate fingerprint'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
name|'unicode'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetKeypairTestCase
dedent|''
dedent|''
name|'class'
name|'GetKeypairTestCase'
op|'('
name|'KeypairAPITestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_success
indent|'    '
name|'def'
name|'test_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keypair'
op|'='
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'get_key_pair'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'existing_key_name'
op|','
name|'keypair'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetKeypairsTestCase
dedent|''
dedent|''
name|'class'
name|'GetKeypairsTestCase'
op|'('
name|'KeypairAPITestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_success
indent|'    '
name|'def'
name|'test_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keypairs'
op|'='
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'get_key_pairs'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'existing_key_name'
op|']'
op|','
nl|'\n'
op|'['
name|'k'
op|'['
string|"'name'"
op|']'
name|'for'
name|'k'
name|'in'
name|'keypairs'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeleteKeypairTestCase
dedent|''
dedent|''
name|'class'
name|'DeleteKeypairTestCase'
op|'('
name|'KeypairAPITestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_success
indent|'    '
name|'def'
name|'test_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'keypair'
op|'='
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'get_key_pair'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'delete_key_pair'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'KeypairNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'keypair_api'
op|'.'
name|'get_key_pair'
op|','
name|'self'
op|'.'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'ctxt'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_check_notifications'
op|'('
name|'action'
op|'='
string|"'delete'"
op|','
nl|'\n'
name|'key_name'
op|'='
name|'self'
op|'.'
name|'existing_key_name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
