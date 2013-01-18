begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Grid Dynamics'
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
name|'fixtures'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_libvirt_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'imagebackend'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
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
DECL|class|_ImageTestCase
name|'class'
name|'_ImageTestCase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|INSTANCES_PATH
indent|'    '
name|'INSTANCES_PATH'
op|'='
string|"'/fake'"
newline|'\n'
nl|'\n'
DECL|member|mock_create_image
name|'def'
name|'mock_create_image'
op|'('
name|'self'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
DECL|function|create_image
indent|'        '
name|'def'
name|'create_image'
op|'('
name|'fn'
op|','
name|'base'
op|','
name|'size'
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
name|'fn'
op|'('
name|'target'
op|'='
name|'base'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'image'
op|'.'
name|'create_image'
op|'='
name|'create_image'
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
name|'_ImageTestCase'
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
name|'flags'
op|'('
name|'disable_process_locking'
op|'='
name|'True'
op|','
nl|'\n'
name|'instances_path'
op|'='
name|'self'
op|'.'
name|'INSTANCES_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'INSTANCE'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'instance'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'NAME'
op|'='
string|"'fake.vm'"
newline|'\n'
name|'self'
op|'.'
name|'TEMPLATE'
op|'='
string|"'template'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'libvirt_utils'
op|'.'
name|'get_instance_path'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|')'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
nl|'\n'
string|"'_base'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|','
string|"'template'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.libvirt.imagebackend.libvirt_utils'"
op|','
nl|'\n'
name|'fake_libvirt_utils'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache
dedent|''
name|'def'
name|'test_cache'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'fileutils'
op|','
string|"'ensure_tree'"
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_create_image'
op|'('
name|'image'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'cache'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache_image_exists
dedent|''
name|'def'
name|'test_cache_image_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'cache'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'TEMPLATE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache_base_dir_exists
dedent|''
name|'def'
name|'test_cache_base_dir_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'fileutils'
op|','
string|"'ensure_tree'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_create_image'
op|'('
name|'image'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'cache'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache_template_exists
dedent|''
name|'def'
name|'test_cache_template_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_DIR'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_create_image'
op|'('
name|'image'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'cache'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RawTestCase
dedent|''
dedent|''
name|'class'
name|'RawTestCase'
op|'('
name|'_ImageTestCase'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|SIZE
indent|'    '
name|'SIZE'
op|'='
number|'1024'
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
name|'self'
op|'.'
name|'image_class'
op|'='
name|'imagebackend'
op|'.'
name|'Raw'
newline|'\n'
name|'super'
op|'('
name|'RawTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|prepare_mocks
dedent|''
name|'def'
name|'prepare_mocks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'lockutils'
op|'.'
name|'synchronized'
op|','
nl|'\n'
string|"'__call__'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|','
string|"'copy_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'disk'
op|','
string|"'extend'"
op|')'
newline|'\n'
name|'return'
name|'fn'
newline|'\n'
nl|'\n'
DECL|member|test_create_image
dedent|''
name|'def'
name|'test_create_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'image_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|'.'
name|'copy_image'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_generated
dedent|''
name|'def'
name|'test_create_image_generated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_extend
dedent|''
name|'def'
name|'test_create_image_extend'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'image_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|'.'
name|'copy_image'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'disk'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|','
name|'image_id'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Qcow2TestCase
dedent|''
dedent|''
name|'class'
name|'Qcow2TestCase'
op|'('
name|'_ImageTestCase'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|SIZE
indent|'    '
name|'SIZE'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
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
name|'self'
op|'.'
name|'image_class'
op|'='
name|'imagebackend'
op|'.'
name|'Qcow2'
newline|'\n'
name|'super'
op|'('
name|'Qcow2TestCase'
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
name|'QCOW2_BASE'
op|'='
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|'+'
nl|'\n'
string|"'_%d'"
op|'%'
op|'('
name|'self'
op|'.'
name|'SIZE'
op|'/'
op|'('
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prepare_mocks
dedent|''
name|'def'
name|'prepare_mocks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'lockutils'
op|'.'
name|'synchronized'
op|','
nl|'\n'
string|"'__call__'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|','
nl|'\n'
string|"'create_cow_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|','
string|"'copy_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'imagebackend'
op|'.'
name|'disk'
op|','
string|"'extend'"
op|')'
newline|'\n'
name|'return'
name|'fn'
newline|'\n'
nl|'\n'
DECL|member|test_create_image
dedent|''
name|'def'
name|'test_create_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_cow_image'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_with_size
dedent|''
name|'def'
name|'test_create_image_with_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_cow_image'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'imagebackend'
op|'.'
name|'disk'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LvmTestCase
dedent|''
dedent|''
name|'class'
name|'LvmTestCase'
op|'('
name|'_ImageTestCase'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|VG
indent|'    '
name|'VG'
op|'='
string|"'FakeVG'"
newline|'\n'
DECL|variable|TEMPLATE_SIZE
name|'TEMPLATE_SIZE'
op|'='
number|'512'
newline|'\n'
DECL|variable|SIZE
name|'SIZE'
op|'='
number|'1024'
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
name|'self'
op|'.'
name|'image_class'
op|'='
name|'imagebackend'
op|'.'
name|'Lvm'
newline|'\n'
name|'super'
op|'('
name|'LvmTestCase'
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
name|'flags'
op|'('
name|'libvirt_images_volume_group'
op|'='
name|'self'
op|'.'
name|'VG'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'LV'
op|'='
string|"'%s_%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|'['
string|"'name'"
op|']'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'/dev'"
op|','
name|'self'
op|'.'
name|'VG'
op|','
name|'self'
op|'.'
name|'LV'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'disk'
op|'='
name|'imagebackend'
op|'.'
name|'disk'
newline|'\n'
name|'self'
op|'.'
name|'utils'
op|'='
name|'imagebackend'
op|'.'
name|'utils'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'='
name|'imagebackend'
op|'.'
name|'libvirt_utils'
newline|'\n'
nl|'\n'
DECL|member|prepare_mocks
dedent|''
name|'def'
name|'prepare_mocks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'disk'
op|','
string|"'resize2fs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'libvirt_utils'
op|','
string|"'create_lvm_image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'disk'
op|','
string|"'get_disk_size'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'return'
name|'fn'
newline|'\n'
nl|'\n'
DECL|member|_create_image
dedent|''
name|'def'
name|'_create_image'
op|'('
name|'self'
op|','
name|'sparse'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'VG'
op|','
nl|'\n'
name|'self'
op|'.'
name|'LV'
op|','
nl|'\n'
name|'self'
op|'.'
name|'TEMPLATE_SIZE'
op|','
nl|'\n'
name|'sparse'
op|'='
name|'sparse'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk'
op|'.'
name|'get_disk_size'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_SIZE'
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'dd'"
op|','
string|"'if=%s'"
op|'%'
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
nl|'\n'
string|"'of=%s'"
op|'%'
name|'self'
op|'.'
name|'PATH'
op|','
string|"'bs=4M'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_image_generated
dedent|''
name|'def'
name|'_create_image_generated'
op|'('
name|'self'
op|','
name|'sparse'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'VG'
op|','
name|'self'
op|'.'
name|'LV'
op|','
nl|'\n'
name|'self'
op|'.'
name|'SIZE'
op|','
name|'sparse'
op|'='
name|'sparse'
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'PATH'
op|','
name|'ephemeral_size'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'SIZE'
op|','
name|'ephemeral_size'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_image_resize
dedent|''
name|'def'
name|'_create_image_resize'
op|'('
name|'self'
op|','
name|'sparse'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'VG'
op|','
name|'self'
op|'.'
name|'LV'
op|','
nl|'\n'
name|'self'
op|'.'
name|'SIZE'
op|','
name|'sparse'
op|'='
name|'sparse'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk'
op|'.'
name|'get_disk_size'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_SIZE'
op|')'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'dd'"
op|','
string|"'if=%s'"
op|'%'
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
nl|'\n'
string|"'of=%s'"
op|'%'
name|'self'
op|'.'
name|'PATH'
op|','
string|"'bs=4M'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk'
op|'.'
name|'resize2fs'
op|'('
name|'self'
op|'.'
name|'PATH'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'create_image'
op|'('
name|'fn'
op|','
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image
dedent|''
name|'def'
name|'test_create_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_image'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_sparsed
dedent|''
name|'def'
name|'test_create_image_sparsed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'libvirt_sparse_logical_volumes'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_image'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_generated
dedent|''
name|'def'
name|'test_create_image_generated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_image_generated'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_generated_sparsed
dedent|''
name|'def'
name|'test_create_image_generated_sparsed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'libvirt_sparse_logical_volumes'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_image_generated'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_resize
dedent|''
name|'def'
name|'test_create_image_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_image_resize'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_resize_sparsed
dedent|''
name|'def'
name|'test_create_image_resize_sparsed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'libvirt_sparse_logical_volumes'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_image_resize'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_negative
dedent|''
name|'def'
name|'test_create_image_negative'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'VG'
op|','
nl|'\n'
name|'self'
op|'.'
name|'LV'
op|','
nl|'\n'
name|'self'
op|'.'
name|'SIZE'
op|','
nl|'\n'
name|'sparse'
op|'='
name|'False'
nl|'\n'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'RuntimeError'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'disk'
op|'.'
name|'get_disk_size'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_PATH'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'TEMPLATE_SIZE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'libvirt_utils'
op|','
string|"'remove_logical_volumes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'remove_logical_volumes'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RuntimeError'
op|','
name|'image'
op|'.'
name|'create_image'
op|','
name|'fn'
op|','
nl|'\n'
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
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
nl|'\n'
DECL|member|test_create_image_generated_negative
dedent|''
name|'def'
name|'test_create_image_generated_negative'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn'
op|'='
name|'self'
op|'.'
name|'prepare_mocks'
op|'('
op|')'
newline|'\n'
name|'fn'
op|'('
name|'target'
op|'='
name|'self'
op|'.'
name|'PATH'
op|','
nl|'\n'
name|'ephemeral_size'
op|'='
name|'None'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'RuntimeError'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'create_lvm_image'
op|'('
name|'self'
op|'.'
name|'VG'
op|','
nl|'\n'
name|'self'
op|'.'
name|'LV'
op|','
nl|'\n'
name|'self'
op|'.'
name|'SIZE'
op|','
nl|'\n'
name|'sparse'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'libvirt_utils'
op|','
string|"'remove_logical_volumes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'libvirt_utils'
op|'.'
name|'remove_logical_volumes'
op|'('
name|'self'
op|'.'
name|'PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'image_class'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RuntimeError'
op|','
name|'image'
op|'.'
name|'create_image'
op|','
name|'fn'
op|','
nl|'\n'
name|'self'
op|'.'
name|'TEMPLATE_PATH'
op|','
name|'self'
op|'.'
name|'SIZE'
op|','
nl|'\n'
name|'ephemeral_size'
op|'='
name|'None'
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
nl|'\n'
nl|'\n'
DECL|class|BackendTestCase
dedent|''
dedent|''
name|'class'
name|'BackendTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|INSTANCE
indent|'    '
name|'INSTANCE'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'fake-instance'"
op|'}'
newline|'\n'
DECL|variable|NAME
name|'NAME'
op|'='
string|"'fake-name.suffix'"
newline|'\n'
nl|'\n'
DECL|member|get_image
name|'def'
name|'get_image'
op|'('
name|'self'
op|','
name|'use_cow'
op|','
name|'image_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'imagebackend'
op|'.'
name|'Backend'
op|'('
name|'use_cow'
op|')'
op|'.'
name|'image'
op|'('
name|'self'
op|'.'
name|'INSTANCE'
op|','
nl|'\n'
name|'self'
op|'.'
name|'NAME'
op|','
nl|'\n'
name|'image_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_image
dedent|''
name|'def'
name|'_test_image'
op|'('
name|'self'
op|','
name|'image_type'
op|','
name|'image_not_cow'
op|','
name|'image_cow'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image1'
op|'='
name|'self'
op|'.'
name|'get_image'
op|'('
name|'False'
op|','
name|'image_type'
op|')'
newline|'\n'
name|'image2'
op|'='
name|'self'
op|'.'
name|'get_image'
op|'('
name|'True'
op|','
name|'image_type'
op|')'
newline|'\n'
nl|'\n'
DECL|function|assertIsInstance
name|'def'
name|'assertIsInstance'
op|'('
name|'instance'
op|','
name|'class_object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'failure'
op|'='
op|'('
string|"'Expected %s,'"
op|'+'
nl|'\n'
string|"' but got %s.'"
op|')'
op|'%'
op|'('
name|'class_object'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'instance'
op|','
name|'class_object'
op|')'
op|','
name|'failure'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'assertIsInstance'
op|'('
name|'image1'
op|','
name|'image_not_cow'
op|')'
newline|'\n'
name|'assertIsInstance'
op|'('
name|'image2'
op|','
name|'image_cow'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_raw
dedent|''
name|'def'
name|'test_image_raw'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_image'
op|'('
string|"'raw'"
op|','
name|'imagebackend'
op|'.'
name|'Raw'
op|','
name|'imagebackend'
op|'.'
name|'Raw'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_qcow2
dedent|''
name|'def'
name|'test_image_qcow2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_image'
op|'('
string|"'qcow2'"
op|','
name|'imagebackend'
op|'.'
name|'Qcow2'
op|','
name|'imagebackend'
op|'.'
name|'Qcow2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_lvm
dedent|''
name|'def'
name|'test_image_lvm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'libvirt_images_volume_group'
op|'='
string|"'FakeVG'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_image'
op|'('
string|"'lvm'"
op|','
name|'imagebackend'
op|'.'
name|'Lvm'
op|','
name|'imagebackend'
op|'.'
name|'Lvm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_default
dedent|''
name|'def'
name|'test_image_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_image'
op|'('
string|"'default'"
op|','
name|'imagebackend'
op|'.'
name|'Raw'
op|','
name|'imagebackend'
op|'.'
name|'Qcow2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
