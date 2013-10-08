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
name|'import'
name|'commands'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
comment|'# If ../nova/__init__.py exists, add ../ to Python search path, so that'
nl|'\n'
comment|'# it will override what happens to be installed in /usr/(local/)lib/python...'
nl|'\n'
DECL|variable|possible_topdir
name|'possible_topdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|')'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'possible_topdir'
op|','
string|"'nova'"
op|','
string|"'__init__.py'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'possible_topdir'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'smoketests'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'smoketests'
name|'import'
name|'flags'
newline|'\n'
nl|'\n'
comment|'#Note that this test should run from'
nl|'\n'
comment|'#public network (outside of private network segments)'
nl|'\n'
comment|'#Please set EC2_URL correctly'
nl|'\n'
comment|'#You should use admin account in this test'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|TEST_PREFIX
name|'TEST_PREFIX'
op|'='
string|"'test%s'"
op|'%'
name|'int'
op|'('
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'*'
number|'1000000'
op|')'
newline|'\n'
DECL|variable|TEST_BUCKET
name|'TEST_BUCKET'
op|'='
string|"'%s_bucket'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
DECL|variable|TEST_KEY
name|'TEST_KEY'
op|'='
string|"'%s_key'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
DECL|variable|TEST_KEY2
name|'TEST_KEY2'
op|'='
string|"'%s_key2'"
op|'%'
name|'TEST_PREFIX'
newline|'\n'
DECL|variable|TEST_DATA
name|'TEST_DATA'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTestsFromPublic
name|'class'
name|'InstanceTestsFromPublic'
op|'('
name|'base'
op|'.'
name|'UserSmokeTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_001_can_create_keypair
indent|'    '
name|'def'
name|'test_001_can_create_keypair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'self'
op|'.'
name|'create_key_pair'
op|'('
name|'self'
op|'.'
name|'conn'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'key'
op|'.'
name|'name'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_security_group
dedent|''
name|'def'
name|'test_002_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'security_group_name'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_security_group'
op|'('
name|'security_group_name'
op|','
nl|'\n'
string|"'test group'"
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'conn'
newline|'\n'
name|'group'
op|'.'
name|'authorize'
op|'('
string|"'tcp'"
op|','
number|'22'
op|','
number|'22'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'.'
name|'authorize'
op|'('
string|"'tcp'"
op|','
number|'22'
op|','
number|'22'
op|','
string|"'::/0'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'reservation'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'run_instances'
op|'('
name|'FLAGS'
op|'.'
name|'test_image'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'TEST_KEY'
op|','
nl|'\n'
name|'security_groups'
op|'='
op|'['
name|'security_group_name'
op|']'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'security_group_name'"
op|']'
op|'='
name|'security_group_name'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'group'"
op|']'
op|'='
name|'group'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|test_003_instance_with_group_runs_within_60_seconds
dedent|''
name|'def'
name|'test_003_instance_with_group_runs_within_60_seconds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reservations'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|']'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'# allow 60 seconds to exit pending with IP'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'60'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'state'
op|'=='
string|"u'running'"
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'instance failed to start'"
op|')'
newline|'\n'
dedent|''
name|'ip'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'private_ip_address'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ip'
op|'=='
string|"'0.0.0.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'private_ip'"
op|']'
op|'='
name|'ip'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'ipv6'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'dns_name_v6'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ipv6'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'ip_v6'"
op|']'
op|'='
name|'ipv6'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_ssh_to_ipv6
dedent|''
dedent|''
name|'def'
name|'test_004_can_ssh_to_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'20'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'ip_v6'"
op|']'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_012_can_create_instance_with_keypair
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_012_can_create_instance_with_keypair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'instance_id'"
name|'in'
name|'self'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'terminate_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
name|'reservation'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'run_instances'
op|'('
name|'FLAGS'
op|'.'
name|'test_image'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'TEST_KEY'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'reservation'
op|'.'
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|test_013_instance_runs_within_60_seconds
dedent|''
name|'def'
name|'test_013_instance_runs_within_60_seconds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'reservations'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|']'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'# allow 60 seconds to exit pending with IP'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'60'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'state'
op|'=='
string|"u'running'"
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'instance failed to start'"
op|')'
newline|'\n'
dedent|''
name|'ip'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'private_ip_address'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ip'
op|'=='
string|"'0.0.0.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'private_ip'"
op|']'
op|'='
name|'ip'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'ipv6'
op|'='
name|'reservations'
op|'['
number|'0'
op|']'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'dns_name_v6'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ipv6'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'ip_v6'"
op|']'
op|'='
name|'ipv6'
newline|'\n'
nl|'\n'
DECL|member|test_014_can_not_ping_private_ip
dedent|''
dedent|''
name|'def'
name|'test_014_can_not_ping_private_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'4'
op|')'
op|':'
newline|'\n'
comment|'# ping waits for 1 second'
nl|'\n'
indent|'            '
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
nl|'\n'
string|"'ping -c1 %s'"
op|'%'
name|'self'
op|'.'
name|'data'
op|'['
string|"'private_ip'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'can ping private ip from public network'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'status'
op|','
name|'output'
op|'='
name|'commands'
op|'.'
name|'getstatusoutput'
op|'('
nl|'\n'
string|"'ping6 -c1 %s'"
op|'%'
name|'self'
op|'.'
name|'data'
op|'['
string|"'ip_v6'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'can ping ipv6 from public network'"
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_015_can_not_ssh_to_private_ip
dedent|''
dedent|''
name|'def'
name|'test_015_can_not_ssh_to_private_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'private_ip'"
op|']'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'can ssh for ipv4 address from public network'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'ip_v6'"
op|']'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'can ssh for ipv6 address from public network'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_999_tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'delete_key_pair'
op|'('
name|'self'
op|'.'
name|'conn'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'security_group_name'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'security_group_name'"
op|']'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'group'"
op|']'
newline|'\n'
name|'if'
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'.'
name|'revoke'
op|'('
string|"'tcp'"
op|','
number|'22'
op|','
number|'22'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                '
name|'group'
op|'.'
name|'revoke'
op|'('
string|"'tcp'"
op|','
number|'22'
op|','
number|'22'
op|','
string|"'::/0'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_security_group'
op|'('
name|'security_group_name'
op|')'
newline|'\n'
name|'if'
string|"'instance_id'"
name|'in'
name|'self'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'terminate_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
