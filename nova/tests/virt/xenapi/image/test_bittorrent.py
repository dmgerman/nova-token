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
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'pkg_resources'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'driver'
name|'as'
name|'xenapi_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'image'
name|'import'
name|'bittorrent'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestBittorrentStore
name|'class'
name|'TestBittorrentStore'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
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
name|'TestBittorrentStore'
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
name|'store'
op|'='
name|'bittorrent'
op|'.'
name|'BittorrentStore'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'torrent_base_url'
op|'='
string|"'http://foo'"
op|','
nl|'\n'
name|'connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'connection_password'
op|'='
string|"'test_pass'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'xenserver'"
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
nl|'\n'
string|"'user'"
op|','
string|"'project'"
op|','
name|'auth_token'
op|'='
string|"'foobar'"
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
nl|'\n'
DECL|function|mock_iter_eps
name|'def'
name|'mock_iter_eps'
op|'('
name|'namespace'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'pkg_resources'
op|','
string|"'iter_entry_points'"
op|','
name|'mock_iter_eps'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'driver'
op|'.'
name|'_session'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'vm_utils'
op|','
string|"'get_sr_path'"
op|','
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
string|"'/fake/sr/path'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_download_image
dedent|''
name|'def'
name|'test_download_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'image_id'"
op|':'
string|"'fake_image_uuid'"
op|','
nl|'\n'
string|"'sr_path'"
op|':'
string|"'/fake/sr/path'"
op|','
nl|'\n'
string|"'torrent_download_stall_cutoff'"
op|':'
number|'600'
op|','
nl|'\n'
string|"'torrent_listen_port_end'"
op|':'
number|'6891'
op|','
nl|'\n'
string|"'torrent_listen_port_start'"
op|':'
number|'6881'
op|','
nl|'\n'
string|"'torrent_max_last_accessed'"
op|':'
number|'86400'
op|','
nl|'\n'
string|"'torrent_max_seeder_processes_per_host'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'torrent_seed_chance'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'torrent_seed_duration'"
op|':'
number|'3600'
op|','
nl|'\n'
string|"'torrent_url'"
op|':'
string|"'http://foo/fake_image_uuid.torrent'"
op|','
nl|'\n'
string|"'uuid_stack'"
op|':'
op|'['
string|"'uuid1'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_make_uuid_stack'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
op|'['
string|"'uuid1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
nl|'\n'
string|"'bittorrent'"
op|','
string|"'download_vhd'"
op|','
op|'**'
name|'params'
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
name|'self'
op|'.'
name|'store'
op|'.'
name|'download_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake_image_uuid'"
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
DECL|member|test_upload_image
dedent|''
name|'def'
name|'test_upload_image'
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
name|'NotImplementedError'
op|','
name|'self'
op|'.'
name|'store'
op|'.'
name|'upload_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|','
op|'['
string|"'fake_vdi_uuid'"
op|']'
op|','
nl|'\n'
string|"'fake_image_uuid'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bad_fetcher
dedent|''
dedent|''
name|'def'
name|'bad_fetcher'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
string|'"just plain bad."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|another_fetcher
dedent|''
name|'def'
name|'another_fetcher'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"http://www.foobar.com/%s"'
op|'%'
name|'image_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MockEntryPoint
dedent|''
name|'class'
name|'MockEntryPoint'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|name
indent|'    '
name|'name'
op|'='
string|'"torrent_url"'
newline|'\n'
nl|'\n'
DECL|member|load
name|'def'
name|'load'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'another_fetcher'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LookupTorrentURLTestCase
dedent|''
dedent|''
name|'class'
name|'LookupTorrentURLTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'LookupTorrentURLTestCase'
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
name|'store'
op|'='
name|'bittorrent'
op|'.'
name|'BittorrentStore'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
string|"'fakeimageid'"
newline|'\n'
nl|'\n'
DECL|member|_mock_iter_none
dedent|''
name|'def'
name|'_mock_iter_none'
op|'('
name|'self'
op|','
name|'namespace'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_mock_iter_single
dedent|''
name|'def'
name|'_mock_iter_single'
op|'('
name|'self'
op|','
name|'namespace'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'MockEntryPoint'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_default_fetch_url_no_base_url_set
dedent|''
name|'def'
name|'test_default_fetch_url_no_base_url_set'
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
name|'torrent_base_url'
op|'='
name|'None'
op|','
nl|'\n'
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'pkg_resources'
op|','
string|"'iter_entry_points'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_mock_iter_none'
op|')'
newline|'\n'
nl|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'RuntimeError'
op|','
name|'self'
op|'.'
name|'store'
op|'.'
name|'_lookup_torrent_url_fn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_'
op|'('
string|"'Cannot create default bittorrent URL without'"
nl|'\n'
string|"' torrent_base_url set'"
nl|'\n'
string|"' or torrent URL fetcher extension'"
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_fetch_url_base_url_is_set
dedent|''
name|'def'
name|'test_default_fetch_url_base_url_is_set'
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
name|'torrent_base_url'
op|'='
string|"'http://foo'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'pkg_resources'
op|','
string|"'iter_entry_points'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_mock_iter_single'
op|')'
newline|'\n'
nl|'\n'
name|'lookup_fn'
op|'='
name|'self'
op|'.'
name|'store'
op|'.'
name|'_lookup_torrent_url_fn'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'http://foo/fakeimageid.torrent'"
op|','
nl|'\n'
name|'lookup_fn'
op|'('
name|'self'
op|'.'
name|'image_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_with_extension
dedent|''
name|'def'
name|'test_with_extension'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'pkg_resources'
op|','
string|"'iter_entry_points'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_mock_iter_single'
op|')'
newline|'\n'
nl|'\n'
name|'lookup_fn'
op|'='
name|'self'
op|'.'
name|'store'
op|'.'
name|'_lookup_torrent_url_fn'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"http://www.foobar.com/%s"'
op|'%'
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\n'
name|'lookup_fn'
op|'('
name|'self'
op|'.'
name|'image_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_extensions_found
dedent|''
name|'def'
name|'test_multiple_extensions_found'
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
name|'torrent_base_url'
op|'='
name|'None'
op|','
nl|'\n'
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|mock_iter_multiple
name|'def'
name|'mock_iter_multiple'
op|'('
name|'namespace'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'MockEntryPoint'
op|'('
op|')'
op|','
name|'MockEntryPoint'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'pkg_resources'
op|','
string|"'iter_entry_points'"
op|','
name|'mock_iter_multiple'
op|')'
newline|'\n'
nl|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'RuntimeError'
op|','
name|'self'
op|'.'
name|'store'
op|'.'
name|'_lookup_torrent_url_fn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_'
op|'('
string|"'Multiple torrent URL fetcher extensions found.'"
nl|'\n'
string|"' Failing.'"
op|')'
op|','
nl|'\n'
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
