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
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'shutil'
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
string|"'bundle_kernel'"
op|','
string|"'random.kernel'"
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
string|"'random.image'"
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
nl|'\n'
nl|'\n'
DECL|class|ImageTests
name|'class'
name|'ImageTests'
op|'('
name|'base'
op|'.'
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
name|'data'
op|'['
string|"'tempdir'"
op|']'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'tempdir'"
op|']'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
name|'FLAGS'
op|'.'
name|'bundle_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'data'
op|'['
string|"'tempdir'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'tempdir'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'tempdir'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_can_register_image
dedent|''
dedent|''
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
DECL|member|test_009_can_add_image_launch_permission
dedent|''
name|'def'
name|'test_009_can_add_image_launch_permission'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'is_public'
op|','
name|'False'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'is_public'
op|','
name|'True'
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
name|'assertEqual'
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
name|'assertEqual'
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
DECL|member|test_011_can_remove_image_launch_permission
dedent|''
name|'def'
name|'test_011_can_remove_image_launch_permission'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'is_public'
op|','
name|'True'
op|')'
newline|'\n'
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
string|"'remove'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'is_public'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_012_private_image_shows_in_list
dedent|''
name|'def'
name|'test_012_private_image_shows_in_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_images'
op|'('
op|')'
newline|'\n'
name|'image_ids'
op|'='
op|'['
name|'image'
op|'.'
name|'id'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'image_id'"
op|']'
name|'in'
name|'image_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_013_user_can_deregister_kernel
dedent|''
name|'def'
name|'test_013_user_can_deregister_kernel'
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
DECL|member|test_014_can_deregister_image
dedent|''
name|'def'
name|'test_014_can_deregister_image'
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
DECL|member|test_015_can_delete_bundle
dedent|''
name|'def'
name|'test_015_can_delete_bundle'
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
string|"'instance'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
newline|'\n'
comment|'# allow 60 seconds to exit pending with IP'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_running'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|')'
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
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'ip'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_ip_address'
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
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'ipv6'
op|'='
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'dns_name_v6'
newline|'\n'
name|'self'
op|'.'
name|'failIf'
op|'('
name|'ipv6'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_can_ping_private_ip
dedent|''
dedent|''
name|'def'
name|'test_004_can_ping_private_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ping'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_ip_address'
op|')'
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
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ping'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'dns_name_v6'
op|','
nl|'\n'
string|'"ping6"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ping instance v6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_can_ssh_to_private_ip
dedent|''
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_ip_address'
op|','
nl|'\n'
name|'TEST_KEY'
op|')'
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
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'dns_name_v6'
op|','
nl|'\n'
name|'TEST_KEY'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'could not ssh to instance v6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_999_tearDown
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
nl|'\n'
nl|'\n'
DECL|class|VolumeTests
dedent|''
dedent|''
name|'class'
name|'VolumeTests'
op|'('
name|'base'
op|'.'
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
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'='
name|'reservation'
op|'.'
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_running'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|')'
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
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ping'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_ip_address'
op|')'
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
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'wait_for_ssh'
op|'('
name|'self'
op|'.'
name|'data'
op|'['
string|"'instance'"
op|']'
op|'.'
name|'private_ip_address'
op|','
nl|'\n'
name|'TEST_KEY'
op|')'
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
name|'volume'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'volume'
op|'.'
name|'status'
op|'.'
name|'startswith'
op|'('
string|"'available'"
op|')'
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
string|"'cannot attach volume with state %s'"
op|'%'
name|'volume'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
comment|'# Give volume some time to be ready.'
nl|'\n'
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
comment|'# wait'
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
name|'volume'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
name|'if'
name|'volume'
op|'.'
name|'status'
op|'.'
name|'startswith'
op|'('
string|"'in-use'"
op|')'
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
string|"'volume never got to in use'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'volume'
op|'.'
name|'status'
op|'.'
name|'startswith'
op|'('
string|"'in-use'"
op|')'
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
name|'private_ip_address'
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
comment|"# NOTE(vish): this will create a dev for images that don't have"
nl|'\n'
comment|'#             udev rules'
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
string|"'grep %s /proc/partitions | '"
nl|'\n'
string|'\'`awk \\\'{print "mknod /dev/"\\\\$4" b "\\\\$1" "\\\\$2}\\\'`\''
nl|'\n'
op|'%'
name|'self'
op|'.'
name|'device'
op|'.'
name|'rpartition'
op|'('
string|"'/'"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'exec_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'exec_list'
op|'.'
name|'append'
op|'('
string|"'mkdir -p /mnt/vol'"
op|')'
newline|'\n'
name|'exec_list'
op|'.'
name|'append'
op|'('
string|"'/sbin/mke2fs %s'"
op|'%'
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'exec_list'
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
name|'exec_list'
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
name|'exec_list'
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
name|'private_ip_address'
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
name|'private_ip_address'
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
string|'"cat /sys/class/block/%s/size"'
op|'%'
name|'self'
op|'.'
name|'device'
op|'.'
name|'rpartition'
op|'('
string|"'/'"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'out'
op|'='
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): 1G bytes / 512 bytes per block'
nl|'\n'
name|'expected_size'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'/'
number|'512'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'%s'"
op|'%'
op|'('
name|'expected_size'
op|','
op|')'
op|','
name|'out'
op|','
nl|'\n'
string|"'Volume is not the right size: %s %s. Expected: %s'"
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
op|','
name|'expected_size'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_006_me_can_umount_volume
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
name|'private_ip_address'
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
dedent|''
dedent|''
endmarker|''
end_unit
