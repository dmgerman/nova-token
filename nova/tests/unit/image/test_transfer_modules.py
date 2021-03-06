begin_unit
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
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'urllib'
op|'.'
name|'parse'
name|'as'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'download'
name|'import'
name|'file'
name|'as'
name|'tm_file'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFileTransferModule
name|'class'
name|'TestFileTransferModule'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.utils.copy_image'"
op|')'
newline|'\n'
DECL|member|test_filesystem_success
name|'def'
name|'test_filesystem_success'
op|'('
name|'self'
op|','
name|'copy_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'allowed_direct_url_schemes'
op|'='
op|'['
string|"'file'"
op|']'
op|','
name|'group'
op|'='
string|"'glance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url'"
op|','
name|'filesystems'
op|'='
op|'['
string|"'gluster'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mountpoint'
op|'='
string|"'/gluster'"
newline|'\n'
name|'url'
op|'='
string|"'file:///gluster/my/image/path'"
newline|'\n'
name|'url_parts'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'fs_id'
op|'='
string|"'someid'"
newline|'\n'
name|'loc_meta'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fs_id'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'mountpoint'
nl|'\n'
op|'}'
newline|'\n'
name|'dst_file'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'tm'
op|'='
name|'tm_file'
op|'.'
name|'FileTransfer'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(Jbresnah) The following options must be added after the module'
nl|'\n'
comment|'# has added the specific groups.'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'id'
op|'='
name|'fs_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'mountpoint'
op|'='
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
name|'tm'
op|'.'
name|'download'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'url_parts'
op|','
name|'dst_file'
op|','
name|'loc_meta'
op|')'
newline|'\n'
name|'copy_mock'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'/gluster/my/image/path'"
op|','
name|'dst_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.utils.copy_image'"
op|')'
newline|'\n'
DECL|member|test_filesystem_mismatched_mountpoint
name|'def'
name|'test_filesystem_mismatched_mountpoint'
op|'('
name|'self'
op|','
name|'copy_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'allowed_direct_url_schemes'
op|'='
op|'['
string|"'file'"
op|']'
op|','
name|'group'
op|'='
string|"'glance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url'"
op|','
name|'filesystems'
op|'='
op|'['
string|"'gluster'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mountpoint'
op|'='
string|"'/gluster'"
newline|'\n'
comment|'# Should include the mountpoint before my/image/path'
nl|'\n'
name|'url'
op|'='
string|"'file:///my/image/path'"
newline|'\n'
name|'url_parts'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'fs_id'
op|'='
string|"'someid'"
newline|'\n'
name|'loc_meta'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fs_id'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'mountpoint'
nl|'\n'
op|'}'
newline|'\n'
name|'dst_file'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'tm'
op|'='
name|'tm_file'
op|'.'
name|'FileTransfer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'id'
op|'='
name|'fs_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'mountpoint'
op|'='
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageDownloadModuleMetaDataError'
op|','
nl|'\n'
name|'tm'
op|'.'
name|'download'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'url_parts'
op|','
nl|'\n'
name|'dst_file'
op|','
name|'loc_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'copy_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.utils.copy_image'"
op|')'
newline|'\n'
DECL|member|test_filesystem_mismatched_filesystem
name|'def'
name|'test_filesystem_mismatched_filesystem'
op|'('
name|'self'
op|','
name|'copy_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'allowed_direct_url_schemes'
op|'='
op|'['
string|"'file'"
op|']'
op|','
name|'group'
op|'='
string|"'glance'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url'"
op|','
name|'filesystems'
op|'='
op|'['
string|"'gluster'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mountpoint'
op|'='
string|"'/gluster'"
newline|'\n'
comment|'# Should include the mountpoint before my/image/path'
nl|'\n'
name|'url'
op|'='
string|"'file:///my/image/path'"
newline|'\n'
name|'url_parts'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'fs_id'
op|'='
string|"'someid'"
newline|'\n'
name|'loc_meta'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'funky'"
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'mountpoint'
nl|'\n'
op|'}'
newline|'\n'
name|'dst_file'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'tm'
op|'='
name|'tm_file'
op|'.'
name|'FileTransfer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'id'
op|'='
name|'fs_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'image_file_url:gluster'"
op|','
name|'mountpoint'
op|'='
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageDownloadModuleError'
op|','
nl|'\n'
name|'tm'
op|'.'
name|'download'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'url_parts'
op|','
nl|'\n'
name|'dst_file'
op|','
name|'loc_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'copy_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
