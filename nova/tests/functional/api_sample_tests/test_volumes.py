begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2014 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotsSampleJsonTests
name|'class'
name|'SnapshotsSampleJsonTests'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-volumes"'
newline|'\n'
nl|'\n'
DECL|variable|create_subs
name|'create_subs'
op|'='
op|'{'
nl|'\n'
string|"'snapshot_name'"
op|':'
string|"'snap-001'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Daily backup'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'521752a6-acf6-4b2d-bc7a-119f9148cd8c'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'SnapshotsSampleJsonTests'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.volumes.Volumes'"
op|')'
newline|'\n'
name|'return'
name|'f'
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
name|'SnapshotsSampleJsonTests'
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
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.get_all_snapshots"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.get_snapshot"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_snapshot
dedent|''
name|'def'
name|'_create_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.create_snapshot"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_create'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|'"os-snapshots"'
op|','
nl|'\n'
string|'"snapshot-create-req"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'create_subs'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_create
dedent|''
name|'def'
name|'test_snapshots_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|'"snapshot-create-resp"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'create_subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_delete
dedent|''
name|'def'
name|'test_snapshots_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.delete_snapshot"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-snapshots/100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_detail
dedent|''
name|'def'
name|'test_snapshots_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-snapshots/detail'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'snapshots-detail-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_list
dedent|''
name|'def'
name|'test_snapshots_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-snapshots'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'snapshots-list-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshots_show
dedent|''
name|'def'
name|'test_snapshots_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-snapshots/100'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'snapshot_name'"
op|':'
string|"'Default name'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'Default description'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'snapshots-show-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumesSampleJsonTest
dedent|''
dedent|''
name|'class'
name|'VolumesSampleJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-volumes"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'VolumesSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.volumes.Volumes'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_get_volume_id
dedent|''
name|'def'
name|'_get_volume_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f803'"
newline|'\n'
nl|'\n'
DECL|member|_stub_volume
dedent|''
name|'def'
name|'_stub_volume'
op|'('
name|'self'
op|','
name|'id'
op|','
name|'displayname'
op|'='
string|'"Volume Name"'
op|','
nl|'\n'
name|'displaydesc'
op|'='
string|'"Volume Description"'
op|','
name|'size'
op|'='
number|'100'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'id'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'size'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'zone1:host1'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'3912f2b4-c5ba-4aec-9165-872876fe202e'"
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
string|"'/'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'in-use'"
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|"'attached'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'vol name'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'displayname'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'displaydesc'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2008'
op|','
number|'12'
op|','
number|'1'
op|','
number|'11'
op|','
number|'1'
op|','
number|'55'
op|')'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'volume_type_id'"
op|':'
string|"'fakevoltype'"
op|','
nl|'\n'
string|"'volume_metadata'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'Backup'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|member|_stub_volume_get
dedent|''
name|'def'
name|'_stub_volume_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_stub_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_volume_delete
dedent|''
name|'def'
name|'_stub_volume_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_stub_volume_get_all
dedent|''
name|'def'
name|'_stub_volume_get_all'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id'
op|'='
name|'self'
op|'.'
name|'_get_volume_id'
op|'('
op|')'
newline|'\n'
name|'return'
op|'['
name|'self'
op|'.'
name|'_stub_volume'
op|'('
name|'id'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_stub_volume_create
dedent|''
name|'def'
name|'_stub_volume_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'size'
op|','
name|'name'
op|','
name|'description'
op|','
name|'snapshot'
op|','
nl|'\n'
op|'**'
name|'param'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id'
op|'='
name|'self'
op|'.'
name|'_get_volume_id'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_stub_volume'
op|'('
name|'id'
op|')'
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
name|'VolumesSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.delete"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_stub_volume_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.get"'
op|','
name|'self'
op|'.'
name|'_stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.get_all"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_stub_volume_get_all'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_post_volume
dedent|''
name|'def'
name|'_post_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs_req'
op|'='
op|'{'
nl|'\n'
string|"'volume_name'"
op|':'
string|'"Volume Name"'
op|','
nl|'\n'
string|"'volume_desc'"
op|':'
string|'"Volume Description"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.volume.cinder.API.create"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_stub_volume_create'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-volumes'"
op|','
string|"'os-volumes-post-req'"
op|','
nl|'\n'
name|'subs_req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'os-volumes-post-resp'"
op|','
name|'subs_req'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volumes_show
dedent|''
name|'def'
name|'test_volumes_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_name'"
op|':'
string|'"Volume Name"'
op|','
nl|'\n'
string|"'volume_desc'"
op|':'
string|'"Volume Description"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'vol_id'
op|'='
name|'self'
op|'.'
name|'_get_volume_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-volumes/%s'"
op|'%'
name|'vol_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'os-volumes-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volumes_index
dedent|''
name|'def'
name|'test_volumes_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_name'"
op|':'
string|'"Volume Name"'
op|','
nl|'\n'
string|"'volume_desc'"
op|':'
string|'"Volume Description"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-volumes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'os-volumes-index-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volumes_detail
dedent|''
name|'def'
name|'test_volumes_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# For now, index and detail are the same.'
nl|'\n'
comment|'# See the volumes api'
nl|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_name'"
op|':'
string|'"Volume Name"'
op|','
nl|'\n'
string|"'volume_desc'"
op|':'
string|'"Volume Description"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-volumes/detail'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'os-volumes-detail-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volumes_create
dedent|''
name|'def'
name|'test_volumes_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volumes_delete
dedent|''
name|'def'
name|'test_volumes_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_volume'
op|'('
op|')'
newline|'\n'
name|'vol_id'
op|'='
name|'self'
op|'.'
name|'_get_volume_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-volumes/%s'"
op|'%'
name|'vol_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeAttachmentsSample
dedent|''
dedent|''
name|'class'
name|'VolumeAttachmentsSample'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-volumes"'
newline|'\n'
nl|'\n'
DECL|member|_stub_db_bdms_get_all_by_instance
name|'def'
name|'_stub_db_bdms_get_all_by_instance'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_bdms_get_all_by_instance
indent|'        '
name|'def'
name|'fake_bdms_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bdms'
op|'='
op|'['
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'volume_id'"
op|':'
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f803'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'server_id'
op|','
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
string|"'device_name'"
op|':'
string|"'/dev/sdd'"
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'volume_id'"
op|':'
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f804'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'server_id'
op|','
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
string|"'device_name'"
op|':'
string|"'/dev/sdc'"
op|'}'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'return'
name|'bdms'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.block_device_mapping_get_all_by_instance'"
op|','
nl|'\n'
name|'fake_bdms_get_all_by_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_compute_api_get
dedent|''
name|'def'
name|'_stub_compute_api_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_api_get
indent|'        '
name|'def'
name|'fake_compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'False'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'want_objects'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
nl|'\n'
name|'context'
op|','
op|'**'
op|'{'
string|"'uuid'"
op|':'
name|'instance_id'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_id'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.compute.api.API.get'"
op|','
name|'fake_compute_api_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
dedent|''
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'VolumeAttachmentsSample'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.volumes.Volumes'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'volume_attachment_update.Volume_attachment_update'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_to_server
dedent|''
name|'def'
name|'test_attach_volume_to_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.get'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.check_attach'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.reserve_volume'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
newline|'\n'
name|'device_name'
op|'='
string|"'/dev/vdd'"
newline|'\n'
name|'bdm'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMapping'
op|'('
op|')'
newline|'\n'
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|'='
name|'device_name'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
nl|'\n'
string|"'nova.compute.manager.ComputeManager.reserve_block_device_name'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'bdm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
nl|'\n'
string|"'nova.compute.manager.ComputeManager.attach_volume'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
nl|'\n'
string|"'nova.objects.BlockDeviceMapping.get_by_volume_id'"
op|','
nl|'\n'
name|'classmethod'
op|'('
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volume'
op|'='
name|'fakes'
op|'.'
name|'stub_volume_get'
op|'('
name|'None'
op|','
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f803'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'device'"
op|':'
name|'device_name'
nl|'\n'
op|'}'
newline|'\n'
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/os-volume_attachments'"
nl|'\n'
op|'%'
name|'server_id'
op|','
nl|'\n'
string|"'attach-volume-to-server-req'"
op|','
name|'subs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'attach-volume-to-server-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_volume_attachments
dedent|''
name|'def'
name|'test_list_volume_attachments'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_db_bdms_get_all_by_instance'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-volume_attachments'"
nl|'\n'
op|'%'
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'list-volume-attachments-resp'"
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_attachment_detail
dedent|''
name|'def'
name|'test_volume_attachment_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'attach_id'
op|'='
string|'"a26887c6-c47b-4654-abb5-dfadf7d3f803"'
newline|'\n'
name|'self'
op|'.'
name|'_stub_db_bdms_get_all_by_instance'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_compute_api_get'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-volume_attachments/%s'"
nl|'\n'
op|'%'
op|'('
name|'server_id'
op|','
name|'attach_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'volume-attachment-detail-resp'"
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_attachment_delete
dedent|''
name|'def'
name|'test_volume_attachment_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'attach_id'
op|'='
string|'"a26887c6-c47b-4654-abb5-dfadf7d3f803"'
newline|'\n'
name|'self'
op|'.'
name|'_stub_db_bdms_get_all_by_instance'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_compute_api_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.get'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.compute.api.API.detach_volume'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'servers/%s/os-volume_attachments/%s'"
nl|'\n'
op|'%'
op|'('
name|'server_id'
op|','
name|'attach_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_attachment_update
dedent|''
name|'def'
name|'test_volume_attachment_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.get'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f805'"
nl|'\n'
op|'}'
newline|'\n'
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'attach_id'
op|'='
string|"'a26887c6-c47b-4654-abb5-dfadf7d3f803'"
newline|'\n'
name|'self'
op|'.'
name|'_stub_db_bdms_get_all_by_instance'
op|'('
name|'server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_stub_compute_api_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.volume.cinder.API.get'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.compute.api.API.swap_volume'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'None'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'servers/%s/os-volume_attachments/%s'"
nl|'\n'
op|'%'
op|'('
name|'server_id'
op|','
name|'attach_id'
op|')'
op|','
nl|'\n'
string|"'update-volume-req'"
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
