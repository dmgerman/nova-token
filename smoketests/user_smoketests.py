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
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'unittest'
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
name|'flags'
newline|'\n'
name|'from'
name|'smoketests'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SUITE_NAMES
name|'SUITE_NAMES'
op|'='
string|"'[image, instance, volume]'"
newline|'\n'
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
string|"'suite'"
op|','
name|'None'
op|','
string|"'Specific test suite to run '"
op|'+'
name|'SUITE_NAMES'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'bundle_kernel'"
op|','
string|"'openwrt-x86-vmlinuz'"
op|','
nl|'\n'
string|"'Local kernel file to use for bundling tests'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'bundle_image'"
op|','
string|"'openwrt-x86-ext2.image'"
op|','
nl|'\n'
string|"'Local image file to use for bundling tests'"
op|')'
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
DECL|variable|TEST_GROUP
name|'TEST_GROUP'
op|'='
string|"'%s_group'"
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
DECL|class|UserSmokeTestCase
name|'class'
name|'UserSmokeTestCase'
op|'('
name|'base'
op|'.'
name|'SmokeTestCase'
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
name|'global'
name|'TEST_DATA'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connection_for_env'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'TEST_DATA'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageTests
dedent|''
dedent|''
name|'class'
name|'ImageTests'
op|'('
name|'UserSmokeTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_001_can_bundle_image
indent|'    '
name|'def'
name|'test_001_can_bundle_image'
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
name|'bundle_image'
op|'('
name|'FLAGS'
op|'.'
name|'bundle_image'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_can_upload_image
dedent|''
name|'def'
name|'test_002_can_upload_image'
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
name|'upload_image'
op|'('
name|'TEST_BUCKET'
op|','
name|'FLAGS'
op|'.'
name|'bundle_image'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_can_register_image
dedent|''
name|'def'
name|'test_003_can_register_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'register_image'
op|'('
string|"'%s/%s.manifest.xml'"
op|'%'
nl|'\n'
op|'('
name|'TEST_BUCKET'
op|','
name|'FLAGS'
op|'.'
name|'bundle_image'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'image_id'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_bundle_kernel
dedent|''
name|'def'
name|'test_004_can_bundle_kernel'
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
name|'bundle_image'
op|'('
name|'FLAGS'
op|'.'
name|'bundle_kernel'
op|','
name|'kernel'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_upload_kernel
dedent|''
name|'def'
name|'test_005_can_upload_kernel'
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
name|'upload_image'
op|'('
name|'TEST_BUCKET'
op|','
name|'FLAGS'
op|'.'
name|'bundle_kernel'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_006_can_register_kernel
dedent|''
name|'def'
name|'test_006_can_register_kernel'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kernel_id'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'register_image'
op|'('
string|"'%s/%s.manifest.xml'"
op|'%'
nl|'\n'
op|'('
name|'TEST_BUCKET'
op|','
name|'FLAGS'
op|'.'
name|'bundle_kernel'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'kernel_id'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'kernel_id'"
op|']'
op|'='
name|'kernel_id'
newline|'\n'
nl|'\n'
DECL|member|test_007_images_are_available_within_10_seconds
dedent|''
name|'def'
name|'test_007_images_are_available_within_10_seconds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_image'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'image'
name|'and'
name|'image'
op|'.'
name|'state'
op|'=='
string|"'available'"
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
name|'print'
name|'image'
op|'.'
name|'state'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'False'
op|')'
comment|"# wasn't available within 10 seconds"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'image'
op|'.'
name|'type'
op|'=='
string|"'machine'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kernel'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_image'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'kernel_id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'kernel'
name|'and'
name|'kernel'
op|'.'
name|'state'
op|'=='
string|"'available'"
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
name|'assert_'
op|'('
name|'False'
op|')'
comment|"# wasn't available within 10 seconds"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'kernel'
op|'.'
name|'type'
op|'=='
string|"'kernel'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_008_can_describe_image_attribute
dedent|''
name|'def'
name|'test_008_can_describe_image_attribute'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_image_attribute'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|','
nl|'\n'
string|"'launchPermission'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'attrs'
op|'.'
name|'name'
op|','
string|"'launch_permission'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_009_can_modify_image_launch_permission
dedent|''
name|'def'
name|'test_009_can_modify_image_launch_permission'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'modify_image_attribute'
op|'('
name|'image_id'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|','
nl|'\n'
name|'operation'
op|'='
string|"'add'"
op|','
nl|'\n'
name|'attribute'
op|'='
string|"'launchPermission'"
op|','
nl|'\n'
name|'groups'
op|'='
string|"'all'"
op|')'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_image'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'id'
op|','
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_010_can_see_launch_permission
dedent|''
name|'def'
name|'test_010_can_see_launch_permission'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'attrs'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_image_attribute'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|','
nl|'\n'
string|"'launchPermission'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'attrs'
op|'.'
name|'name'
op|','
string|"'launch_permission'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'attrs'
op|'.'
name|'attrs'
op|'['
string|"'groups'"
op|']'
op|'['
number|'0'
op|']'
op|','
string|"'all'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_011_user_can_deregister_kernel
dedent|''
name|'def'
name|'test_011_user_can_deregister_kernel'
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
name|'conn'
op|'.'
name|'deregister_image'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'kernel_id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_012_can_deregister_image
dedent|''
name|'def'
name|'test_012_can_deregister_image'
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
name|'conn'
op|'.'
name|'deregister_image'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_013_can_delete_bundle
dedent|''
name|'def'
name|'test_013_can_delete_bundle'
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
name|'delete_bundle_bucket'
op|'('
name|'TEST_BUCKET'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTests
dedent|''
dedent|''
name|'class'
name|'InstanceTests'
op|'('
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
DECL|member|test_002_can_create_instance_with_keypair
dedent|''
name|'def'
name|'test_002_can_create_instance_with_keypair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
DECL|member|test_003_instance_runs_within_60_seconds
dedent|''
name|'def'
name|'test_003_instance_runs_within_60_seconds'
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
indent|'                 '
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
name|'private_dns_name'
newline|'\n'
name|'self'
op|'.'
name|'failIf'
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
name|'print'
name|'self'
op|'.'
name|'data'
op|'['
string|"'private_ip'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_ping_private_ip
dedent|''
name|'def'
name|'test_004_can_ping_private_ip'
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
number|'120'
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
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ping instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_ssh_to_private_ip
dedent|''
dedent|''
name|'def'
name|'test_005_can_ssh_to_private_ip'
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
number|'30'
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
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_006_can_allocate_elastic_ip
dedent|''
dedent|''
name|'def'
name|'test_006_can_allocate_elastic_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'allocate_address'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'result'
op|','
string|"'public_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|'='
name|'result'
op|'.'
name|'public_ip'
newline|'\n'
nl|'\n'
DECL|member|test_007_can_associate_ip_with_instance
dedent|''
name|'def'
name|'test_007_can_associate_ip_with_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'associate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_008_can_ssh_with_public_ip
dedent|''
name|'def'
name|'test_008_can_ssh_with_public_ip'
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
number|'30'
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
string|"'public_ip'"
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
name|'socket'
op|'.'
name|'error'
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
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_009_can_disassociate_ip_from_instance
dedent|''
dedent|''
name|'def'
name|'test_009_can_disassociate_ip_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'disassociate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_010_can_deallocate_elastic_ip
dedent|''
name|'def'
name|'test_010_can_deallocate_elastic_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
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
name|'if'
name|'self'
op|'.'
name|'data'
op|'.'
name|'has_key'
op|'('
string|"'instance_id'"
op|')'
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
nl|'\n'
nl|'\n'
DECL|class|VolumeTests
dedent|''
dedent|''
dedent|''
name|'class'
name|'VolumeTests'
op|'('
name|'UserSmokeTestCase'
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
name|'VolumeTests'
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
name|'device'
op|'='
string|"'/dev/vdb'"
newline|'\n'
nl|'\n'
DECL|member|test_000_setUp
dedent|''
name|'def'
name|'test_000_setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|','
nl|'\n'
name|'key_name'
op|'='
name|'TEST_KEY'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'='
name|'instance'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'120'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'can_ping'
op|'('
name|'instance'
op|'.'
name|'private_dns_name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'unable to start instance'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_001_can_create_volume
dedent|''
dedent|''
name|'def'
name|'test_001_can_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_volume'
op|'('
number|'1'
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume'
op|'.'
name|'size'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'volume'"
op|']'
op|'='
name|'volume'
newline|'\n'
comment|'# Give network time to find volume.'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_can_attach_volume
dedent|''
name|'def'
name|'test_002_can_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'volume'"
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume'
op|'.'
name|'status'
op|'=='
string|"u'available'"
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
number|'5'
op|')'
newline|'\n'
name|'volume'
op|'.'
name|'update'
op|'('
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
string|"'cannot attach volume with state %s'"
op|'%'
name|'volume'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volume'
op|'.'
name|'attach'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|','
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
comment|'# Volumes seems to report "available" too soon.'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume'
op|'.'
name|'status'
op|'=='
string|"u'in-use'"
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
number|'5'
op|')'
newline|'\n'
name|'volume'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume'
op|'.'
name|'status'
op|','
string|"u'in-use'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Give instance time to recognize volume.'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_can_mount_volume
dedent|''
name|'def'
name|'test_003_can_mount_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'ip'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'commands'
op|'.'
name|'append'
op|'('
string|"'mkdir -p /mnt/vol'"
op|')'
newline|'\n'
name|'commands'
op|'.'
name|'append'
op|'('
string|"'mkfs.ext2 %s'"
op|'%'
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'commands'
op|'.'
name|'append'
op|'('
string|"'mount %s /mnt/vol'"
op|'%'
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'commands'
op|'.'
name|'append'
op|'('
string|"'echo success'"
op|')'
newline|'\n'
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'conn'
op|'.'
name|'exec_command'
op|'('
string|"' && '"
op|'.'
name|'join'
op|'('
name|'commands'
op|')'
op|')'
newline|'\n'
name|'out'
op|'='
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'endswith'
op|'('
string|"'success'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unable to mount: %s %s'"
op|'%'
op|'('
name|'out'
op|','
name|'stderr'
op|'.'
name|'read'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_write_to_volume
dedent|''
dedent|''
name|'def'
name|'test_004_can_write_to_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'ip'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
comment|"# FIXME(devcamcar): This doesn't fail if the volume hasn't been mounted"
nl|'\n'
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'conn'
op|'.'
name|'exec_command'
op|'('
nl|'\n'
string|"'echo hello > /mnt/vol/test.txt'"
op|')'
newline|'\n'
name|'err'
op|'='
name|'stderr'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'err'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unable to write to mount: %s'"
op|'%'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_volume_is_correct_size
dedent|''
dedent|''
name|'def'
name|'test_005_volume_is_correct_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'ip'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'conn'
op|'.'
name|'exec_command'
op|'('
nl|'\n'
string|'"df -h | grep %s | awk {\'print $2\'}"'
op|'%'
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'out'
op|'='
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
op|'=='
string|"'1008M'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Volume is not the right size: %s %s'"
op|'%'
nl|'\n'
op|'('
name|'out'
op|','
name|'stderr'
op|'.'
name|'read'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_006_me_can_umount_volume
dedent|''
dedent|''
name|'def'
name|'test_006_me_can_umount_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_dns_name'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'connect_ssh'
op|'('
name|'ip'
op|','
name|'TEST_KEY'
op|')'
newline|'\n'
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'conn'
op|'.'
name|'exec_command'
op|'('
string|"'umount /mnt/vol'"
op|')'
newline|'\n'
name|'err'
op|'='
name|'stderr'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'err'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unable to unmount: %s'"
op|'%'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_007_me_can_detach_volume
dedent|''
dedent|''
name|'def'
name|'test_007_me_can_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'detach_volume'
op|'('
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_008_me_can_delete_volume
dedent|''
name|'def'
name|'test_008_me_can_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'volume'"
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
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
name|'conn'
op|'.'
name|'terminate_instances'
op|'('
op|'['
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'id'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_key_pair'
op|'('
name|'TEST_KEY'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupTests
dedent|''
dedent|''
name|'class'
name|'SecurityGroupTests'
op|'('
name|'UserSmokeTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__public_instance_is_accessible
indent|'    '
name|'def'
name|'__public_instance_is_accessible'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id_url'
op|'='
string|'"latest/meta-data/instance-id"'
newline|'\n'
name|'options'
op|'='
string|'"-s --max-time 1"'
newline|'\n'
name|'command'
op|'='
string|'"curl %s %s/%s"'
op|'%'
op|'('
name|'options'
op|','
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|','
name|'id_url'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'commands'
op|'.'
name|'getoutput'
op|'('
name|'command'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'instance_id'
op|'!='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Wrong instance id"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_001_can_create_security_group
dedent|''
name|'def'
name|'test_001_can_create_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_security_group'
op|'('
name|'TEST_GROUP'
op|','
name|'description'
op|'='
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'TEST_GROUP'
name|'in'
op|'['
name|'group'
op|'.'
name|'name'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_can_launch_instance_in_security_group
dedent|''
name|'def'
name|'test_002_can_launch_instance_in_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'TEST_GROUP'
op|']'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.tiny'"
op|')'
newline|'\n'
nl|'\n'
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
DECL|member|test_003_can_authorize_security_group_ingress
dedent|''
name|'def'
name|'test_003_can_authorize_security_group_ingress'
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
name|'conn'
op|'.'
name|'authorize_security_group'
op|'('
name|'TEST_GROUP'
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'80'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'80'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_access_instance_over_public_ip
dedent|''
name|'def'
name|'test_004_can_access_instance_over_public_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'allocate_address'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'hasattr'
op|'('
name|'result'
op|','
string|"'public_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|'='
name|'result'
op|'.'
name|'public_ip'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'associate_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
newline|'\n'
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'while'
name|'not'
name|'self'
op|'.'
name|'__public_instance_is_accessible'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# 1 minute to launch'
nl|'\n'
indent|'            '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'start_time'
op|'>'
number|'60'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|'"Timeout"'
op|')'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_revoke_security_group_ingress
dedent|''
dedent|''
name|'def'
name|'test_005_can_revoke_security_group_ingress'
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
name|'conn'
op|'.'
name|'revoke_security_group'
op|'('
name|'TEST_GROUP'
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'from_port'
op|'='
number|'80'
op|','
nl|'\n'
name|'to_port'
op|'='
number|'80'
op|')'
op|')'
newline|'\n'
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'__public_instance_is_accessible'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# 1 minute to teardown'
nl|'\n'
indent|'            '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'start_time'
op|'>'
number|'60'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|'"Timeout"'
op|')'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_999_tearDown
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
name|'conn'
op|'.'
name|'delete_key_pair'
op|'('
name|'TEST_KEY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_security_group'
op|'('
name|'TEST_GROUP'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'TEST_GROUP'
name|'in'
op|'['
name|'group'
op|'.'
name|'name'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'release_address'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'public_ip'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
DECL|variable|suites
indent|'    '
name|'suites'
op|'='
op|'{'
string|"'image'"
op|':'
name|'unittest'
op|'.'
name|'makeSuite'
op|'('
name|'ImageTests'
op|')'
op|','
nl|'\n'
string|"'instance'"
op|':'
name|'unittest'
op|'.'
name|'makeSuite'
op|'('
name|'InstanceTests'
op|')'
op|','
nl|'\n'
string|"'security_group'"
op|':'
name|'unittest'
op|'.'
name|'makeSuite'
op|'('
name|'SecurityGroupTests'
op|')'
op|','
nl|'\n'
string|"'volume'"
op|':'
name|'unittest'
op|'.'
name|'makeSuite'
op|'('
name|'VolumeTests'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
name|'base'
op|'.'
name|'run_tests'
op|'('
name|'suites'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
