begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (C) 2012 Yahoo! Inc. All Rights Reserved.'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageUtilsTestCase
name|'class'
name|'ImageUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_qemu_info_canon
indent|'    '
name|'def'
name|'test_qemu_info_canon'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|'"disk.config"'
newline|'\n'
name|'example_output'
op|'='
string|'"""image: disk.config\nfile format: raw\nvirtual size: 64M (67108864 bytes)\ncluster_size: 65536\ndisk size: 96K\nblah BLAH: bb\n"""'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'example_output'
op|','
string|"''"
op|')'
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
name|'image_info'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'disk.config'"
op|','
name|'image_info'
op|'.'
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'raw'"
op|','
name|'image_info'
op|'.'
name|'file_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'67108864'
op|','
name|'image_info'
op|'.'
name|'virtual_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'98304'
op|','
name|'image_info'
op|'.'
name|'disk_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'65536'
op|','
name|'image_info'
op|'.'
name|'cluster_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_qemu_info_canon2
dedent|''
name|'def'
name|'test_qemu_info_canon2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|'"disk.config"'
newline|'\n'
name|'example_output'
op|'='
string|'"""image: disk.config\nfile format: QCOW2\nvirtual size: 67108844\ncluster_size: 65536\ndisk size: 963434\nbacking file: /var/lib/nova/a328c7998805951a_2\n"""'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'example_output'
op|','
string|"''"
op|')'
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
name|'image_info'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'disk.config'"
op|','
name|'image_info'
op|'.'
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'qcow2'"
op|','
name|'image_info'
op|'.'
name|'file_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'67108844'
op|','
name|'image_info'
op|'.'
name|'virtual_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'963434'
op|','
name|'image_info'
op|'.'
name|'disk_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'65536'
op|','
name|'image_info'
op|'.'
name|'cluster_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'/var/lib/nova/a328c7998805951a_2'"
op|','
nl|'\n'
name|'image_info'
op|'.'
name|'backing_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_qemu_backing_file_actual
dedent|''
name|'def'
name|'test_qemu_backing_file_actual'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|'"disk.config"'
newline|'\n'
name|'example_output'
op|'='
string|'"""image: disk.config\nfile format: raw\nvirtual size: 64M (67108864 bytes)\ncluster_size: 65536\ndisk size: 96K\nSnapshot list:\nID        TAG                 VM SIZE                DATE       VM CLOCK\n1     d9a9784a500742a7bb95627bb3aace38      0 2012-08-20 10:52:46 00:00:00.000\nbacking file: /var/lib/nova/a328c7998805951a_2 (actual path: /b/3a988059e51a_2)\n"""'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'example_output'
op|','
string|"''"
op|')'
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
name|'image_info'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'disk.config'"
op|','
name|'image_info'
op|'.'
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'raw'"
op|','
name|'image_info'
op|'.'
name|'file_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'67108864'
op|','
name|'image_info'
op|'.'
name|'virtual_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'98304'
op|','
name|'image_info'
op|'.'
name|'disk_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'image_info'
op|'.'
name|'snapshots'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'/b/3a988059e51a_2'"
op|','
nl|'\n'
name|'image_info'
op|'.'
name|'backing_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_qemu_info_convert
dedent|''
name|'def'
name|'test_qemu_info_convert'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|'"disk.config"'
newline|'\n'
name|'example_output'
op|'='
string|'"""image: disk.config\nfile format: raw\nvirtual size: 64M\ndisk size: 96K\nSnapshot list:\nID        TAG                 VM SIZE                DATE       VM CLOCK\n1        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\n3        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\n4        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\njunk stuff: bbb\n"""'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'example_output'
op|','
string|"''"
op|')'
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
name|'image_info'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'disk.config'"
op|','
name|'image_info'
op|'.'
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'raw'"
op|','
name|'image_info'
op|'.'
name|'file_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'67108864'
op|','
name|'image_info'
op|'.'
name|'virtual_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'98304'
op|','
name|'image_info'
op|'.'
name|'disk_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_qemu_info_snaps
dedent|''
name|'def'
name|'test_qemu_info_snaps'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
string|'"disk.config"'
newline|'\n'
name|'example_output'
op|'='
string|'"""image: disk.config\nfile format: raw\nvirtual size: 64M (67108864 bytes)\ndisk size: 96K\nSnapshot list:\nID        TAG                 VM SIZE                DATE       VM CLOCK\n1        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\n3        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\n4        d9a9784a500742a7bb95627bb3aace38    0 2012-08-20 10:52:46 00:00:00.000\n"""'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'example_output'
op|','
string|"''"
op|')'
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
name|'image_info'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'disk.config'"
op|','
name|'image_info'
op|'.'
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'raw'"
op|','
name|'image_info'
op|'.'
name|'file_format'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'67108864'
op|','
name|'image_info'
op|'.'
name|'virtual_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'98304'
op|','
name|'image_info'
op|'.'
name|'disk_size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'image_info'
op|'.'
name|'snapshots'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
