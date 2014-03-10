begin_unit
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'imagehandler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|IMAGE_ID
name|'IMAGE_ID'
op|'='
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
newline|'\n'
DECL|variable|IMAGE_PATH
name|'IMAGE_PATH'
op|'='
string|"'/var/run/instances/_base/img'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RBDTestCase
name|'class'
name|'RBDTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'RBDTestCase'
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
name|'imagehandler'
op|'='
name|'imagehandler'
op|'.'
name|'RBDCloneImageHandler'
op|'('
nl|'\n'
name|'rbd'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
op|','
nl|'\n'
name|'rados'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'clone'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
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
name|'RBDTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_image_no_snapshot
dedent|''
name|'def'
name|'test_fetch_image_no_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://old_image'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_fetch_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'rbd'"
op|','
nl|'\n'
name|'backend_location'
op|'='
op|'('
string|"'a'"
op|','
string|"'b'"
op|')'
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'assert_called_once_with'
op|'('
name|'url'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'clone'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_image_non_rbd_backend
dedent|''
name|'def'
name|'test_fetch_image_non_rbd_backend'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://fsid/pool/image/snap'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_fetch_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'lvm'"
op|','
nl|'\n'
name|'backend_location'
op|'='
string|"'/path'"
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'clone'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_image_rbd_not_cloneable
dedent|''
name|'def'
name|'test_fetch_image_rbd_not_cloneable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://fsid/pool/image/snap'"
newline|'\n'
name|'dest_pool'
op|'='
string|"'foo'"
newline|'\n'
name|'dest_image'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_fetch_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'rbd'"
op|','
nl|'\n'
name|'backend_location'
op|'='
op|'('
name|'dest_pool'
op|','
nl|'\n'
name|'dest_image'
op|')'
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'assert_called_once_with'
op|'('
name|'url'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'handled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_image_cloneable
dedent|''
name|'def'
name|'test_fetch_image_cloneable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://fsid/pool/image/snap'"
newline|'\n'
name|'dest_pool'
op|'='
string|"'foo'"
newline|'\n'
name|'dest_image'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_fetch_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'rbd'"
op|','
nl|'\n'
name|'backend_location'
op|'='
op|'('
name|'dest_pool'
op|','
nl|'\n'
name|'dest_image'
op|')'
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'assert_called_once_with'
op|'('
name|'url'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'clone'
op|'.'
name|'assert_called_once_with'
op|'('
name|'dest_pool'
op|','
nl|'\n'
name|'dest_image'
op|','
nl|'\n'
string|"'pool'"
op|','
nl|'\n'
string|"'image'"
op|','
nl|'\n'
string|"'snap'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_image
dedent|''
name|'def'
name|'test_remove_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://fsid/pool/image/snap'"
newline|'\n'
name|'pool'
op|'='
string|"'foo'"
newline|'\n'
name|'image'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'remove'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_remove_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'rbd'"
op|','
nl|'\n'
name|'backend_location'
op|'='
op|'('
name|'pool'
op|','
nl|'\n'
name|'image'
op|')'
op|','
nl|'\n'
name|'backend_dest'
op|'='
string|"'baz'"
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'assert_called_once_with'
op|'('
name|'url'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'remove'
op|'.'
name|'assert_called_once_with'
op|'('
name|'image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handled'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_move_image
dedent|''
name|'def'
name|'test_move_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|"'rbd://fsid/pool/image/snap'"
newline|'\n'
name|'pool'
op|'='
string|"'foo'"
newline|'\n'
name|'image'
op|'='
string|"'bar'"
newline|'\n'
name|'dest_image'
op|'='
string|"'baz'"
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'rename'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'handled'
op|'='
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'_move_image'
op|'('
name|'None'
op|','
name|'IMAGE_ID'
op|','
nl|'\n'
name|'dict'
op|'('
name|'disk_format'
op|'='
string|"'raw'"
op|')'
op|','
nl|'\n'
name|'IMAGE_PATH'
op|','
name|'IMAGE_PATH'
op|','
nl|'\n'
name|'backend_type'
op|'='
string|"'rbd'"
op|','
nl|'\n'
name|'backend_location'
op|'='
op|'('
name|'pool'
op|','
name|'image'
op|')'
op|','
nl|'\n'
name|'backend_dest'
op|'='
string|"'baz'"
op|','
nl|'\n'
name|'location'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'url'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'is_cloneable'
op|'.'
name|'assert_called_once_with'
op|'('
name|'url'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'imagehandler'
op|'.'
name|'driver'
op|'.'
name|'rename'
op|'.'
name|'assert_called_once_with'
op|'('
name|'image'
op|','
nl|'\n'
name|'dest_image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handled'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
