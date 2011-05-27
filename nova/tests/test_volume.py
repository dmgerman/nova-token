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
string|'"""\nTests for Volume Code.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'cStringIO'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.volume'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTestCase
name|'class'
name|'VolumeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for volumes."""'
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
name|'super'
op|'('
name|'VolumeTestCase'
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
name|'compute'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_create_volume
name|'def'
name|'_create_volume'
op|'('
name|'size'
op|'='
string|"'0'"
op|','
name|'snapshot_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a volume object."""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'vol'
op|'['
string|"'snapshot_id'"
op|']'
op|'='
name|'snapshot_id'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
newline|'\n'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_delete_volume
dedent|''
name|'def'
name|'test_create_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test volume can be created and deleted."""'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_id'
op|','
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'volume_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume_from_snapshot
dedent|''
name|'def'
name|'test_create_volume_from_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test volume can be created from a snapshot."""'
newline|'\n'
name|'volume_src_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_src_id'
op|')'
newline|'\n'
name|'snapshot_id'
op|'='
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
name|'volume_src_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_src_id'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'volume_dst_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
number|'0'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_dst_id'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_dst_id'
op|','
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_dst_id'
op|')'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'snapshot_id'
op|','
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_dst_id'
op|')'
op|'.'
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_dst_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_src_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_big_volume
dedent|''
name|'def'
name|'test_too_big_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure failure if a too large of a volume is requested."""'
newline|'\n'
comment|'# FIXME(vish): validation needs to move into the data layer in'
nl|'\n'
comment|'#              volume_create'
nl|'\n'
name|'return'
name|'True'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
string|"'1001'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Should have thrown TypeError"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_volumes
dedent|''
dedent|''
name|'def'
name|'test_too_many_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that NoMoreTargets is raised when we run out of volumes."""'
newline|'\n'
name|'vols'
op|'='
op|'['
op|']'
newline|'\n'
name|'total_slots'
op|'='
name|'FLAGS'
op|'.'
name|'iscsi_num_targets'
newline|'\n'
name|'for'
name|'_index'
name|'in'
name|'xrange'
op|'('
name|'total_slots'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'vols'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'db'
op|'.'
name|'NoMoreTargets'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'vols'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_attach_detach_volume
dedent|''
dedent|''
name|'def'
name|'test_run_attach_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure volume can be attached and detached from instance."""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
string|"'2'"
comment|'# m1.tiny'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'instance_id'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'mountpoint'
op|'='
string|'"/dev/sdf"'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'attach_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
op|'['
string|"'status'"
op|']'
op|','
string|'"in-use"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|','
string|'"attached"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
op|'['
string|"'mountpoint'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'volume_get_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_tests'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_detached'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'detach_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'vol'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vol'
op|'['
string|"'status'"
op|']'
op|','
string|'"available"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'volume_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_concurrent_volumes_get_different_targets
dedent|''
name|'def'
name|'test_concurrent_volumes_get_different_targets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure multiple concurrent volumes get different targets."""'
newline|'\n'
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'targets'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_check
name|'def'
name|'_check'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Make sure targets aren\'t duplicated."""'
newline|'\n'
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'iscsi_target'
op|'='
name|'db'
op|'.'
name|'volume_get_iscsi_target_num'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'iscsi_target'
name|'not'
name|'in'
name|'targets'
op|')'
newline|'\n'
name|'targets'
op|'.'
name|'append'
op|'('
name|'iscsi_target'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Target %s allocated"'
op|')'
op|','
name|'iscsi_target'
op|')'
newline|'\n'
dedent|''
name|'total_slots'
op|'='
name|'FLAGS'
op|'.'
name|'iscsi_num_targets'
newline|'\n'
name|'for'
name|'_index'
name|'in'
name|'xrange'
op|'('
name|'total_slots'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'_check'
op|'('
name|'d'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multi_node
dedent|''
dedent|''
name|'def'
name|'test_multi_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): Figure out how to test with two nodes,'
nl|'\n'
comment|'# each of them having a different FLAG for storage_node'
nl|'\n'
comment|'# This will allow us to test cross-node interactions'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_create_snapshot
name|'def'
name|'_create_snapshot'
op|'('
name|'volume_id'
op|','
name|'size'
op|'='
string|"'0'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a snapshot object."""'
newline|'\n'
name|'snap'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'snap'
op|'['
string|"'volume_size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'snap'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'snap'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'snap'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'snap'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'snapshot_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'snap'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_delete_snapshot
dedent|''
name|'def'
name|'test_create_delete_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test snapshot can be created and deleted."""'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'snapshot_id'
op|'='
name|'self'
op|'.'
name|'_create_snapshot'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'snapshot_id'
op|','
nl|'\n'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'snapshot_id'
op|')'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'snapshot_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DriverTestCase
dedent|''
dedent|''
name|'class'
name|'DriverTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Test class for Drivers."""'
newline|'\n'
DECL|variable|driver_name
name|'driver_name'
op|'='
string|'"nova.volume.driver.FakeAOEDriver"'
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
name|'super'
op|'('
name|'DriverTestCase'
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
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'driver_name'
op|','
nl|'\n'
name|'logging_default_format_string'
op|'='
string|'"%(message)s"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'='
string|'""'
newline|'\n'
nl|'\n'
DECL|function|_fake_execute
name|'def'
name|'_fake_execute'
op|'('
name|'_command'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Fake _execute."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'output'
op|','
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'volume'
op|'.'
name|'driver'
op|'.'
name|'_execute'
op|'='
name|'_fake_execute'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'driver'
op|'.'
name|'_sync_execute'
op|'='
name|'_fake_execute'
newline|'\n'
nl|'\n'
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'log'
op|'.'
name|'addHandler'
op|'('
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
name|'self'
op|'.'
name|'stream'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
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
name|'DriverTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume
dedent|''
name|'def'
name|'_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volumes to an instance. This function also sets\n           a fake log message."""'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_detach_volume
dedent|''
name|'def'
name|'_detach_volume'
op|'('
name|'self'
op|','
name|'volume_id_list'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volumes from an instance."""'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_id_list'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_detached'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AOETestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'AOETestCase'
op|'('
name|'DriverTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for AOEDriver"""'
newline|'\n'
DECL|variable|driver_name
name|'driver_name'
op|'='
string|'"nova.volume.driver.AOEDriver"'
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
name|'super'
op|'('
name|'AOETestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
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
name|'AOETestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume
dedent|''
name|'def'
name|'_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volumes to an instance. This function also sets\n           a fake log message."""'
newline|'\n'
name|'volume_id_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'xrange'
op|'('
number|'3'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'volume_id'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# each volume has a different mountpoint'
nl|'\n'
name|'mountpoint'
op|'='
string|'"/dev/sd"'
op|'+'
name|'chr'
op|'('
op|'('
name|'ord'
op|'('
string|"'b'"
op|')'
op|'+'
name|'index'
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|','
name|'self'
op|'.'
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'db'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'+='
string|'"%s %s eth0 /dev/nova-volumes/vol-foo auto run\\n"'
op|'%'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
newline|'\n'
nl|'\n'
name|'volume_id_list'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'volume_id_list'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_no_volume
dedent|''
name|'def'
name|'test_check_for_export_with_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No log message when no volume is attached to an instance."""'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'truncate'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_all_vblade_processes
dedent|''
name|'def'
name|'test_check_for_export_with_all_vblade_processes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No log message when all the vblade processes are running."""'
newline|'\n'
name|'volume_id_list'
op|'='
name|'self'
op|'.'
name|'_attach_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'truncate'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_detach_volume'
op|'('
name|'volume_id_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_vblade_process_missing
dedent|''
name|'def'
name|'test_check_for_export_with_vblade_process_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Output a warning message when some vblade processes aren\'t\n           running."""'
newline|'\n'
name|'volume_id_list'
op|'='
name|'self'
op|'.'
name|'_attach_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# the first vblade process isn't running"
nl|'\n'
name|'self'
op|'.'
name|'output'
op|'='
name|'self'
op|'.'
name|'output'
op|'.'
name|'replace'
op|'('
string|'"run"'
op|','
string|'"down"'
op|','
number|'1'
op|')'
newline|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|'='
name|'db'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id_list'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'msg_is_match'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'truncate'
op|'('
number|'0'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'volume_id_list'
op|'['
number|'0'
op|']'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot confirm exported volume id:%(volume_id)s. "'
nl|'\n'
string|'"vblade process for e%(shelf_id)s.%(blade_id)s "'
nl|'\n'
string|'"isn\'t running."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'msg_is_match'
op|'='
op|'('
number|'0'
op|'<='
name|'e'
op|'.'
name|'message'
op|'.'
name|'find'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'msg_is_match'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_detach_volume'
op|'('
name|'volume_id_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ISCSITestCase
dedent|''
dedent|''
name|'class'
name|'ISCSITestCase'
op|'('
name|'DriverTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for ISCSIDriver"""'
newline|'\n'
DECL|variable|driver_name
name|'driver_name'
op|'='
string|'"nova.volume.driver.ISCSIDriver"'
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
name|'super'
op|'('
name|'ISCSITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
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
name|'ISCSITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume
dedent|''
name|'def'
name|'_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volumes to an instance. This function also sets\n           a fake log message."""'
newline|'\n'
name|'volume_id_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'xrange'
op|'('
number|'3'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'vol_ref'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'vol_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# each volume has a different mountpoint'
nl|'\n'
name|'mountpoint'
op|'='
string|'"/dev/sd"'
op|'+'
name|'chr'
op|'('
op|'('
name|'ord'
op|'('
string|"'b'"
op|')'
op|'+'
name|'index'
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'self'
op|'.'
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
name|'volume_id_list'
op|'.'
name|'append'
op|'('
name|'vol_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'volume_id_list'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_no_volume
dedent|''
name|'def'
name|'test_check_for_export_with_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No log message when no volume is attached to an instance."""'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'truncate'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_all_volume_exported
dedent|''
name|'def'
name|'test_check_for_export_with_all_volume_exported'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No log message when all the vblade processes are running."""'
newline|'\n'
name|'volume_id_list'
op|'='
name|'self'
op|'.'
name|'_attach_volume'
op|'('
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
name|'volume'
op|'.'
name|'driver'
op|','
string|"'_execute'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'volume_id_list'
op|':'
newline|'\n'
indent|'            '
name|'tid'
op|'='
name|'db'
op|'.'
name|'volume_get_iscsi_target_num'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'driver'
op|'.'
name|'_execute'
op|'('
string|'"sudo"'
op|','
string|'"ietadm"'
op|','
string|'"--op"'
op|','
string|'"show"'
op|','
nl|'\n'
string|'"--tid=%(tid)d"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stream'
op|'.'
name|'truncate'
op|'('
number|'0'
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
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_detach_volume'
op|'('
name|'volume_id_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_export_with_some_volume_missing
dedent|''
name|'def'
name|'test_check_for_export_with_some_volume_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Output a warning message when some volumes are not recognied\n           by ietd."""'
newline|'\n'
name|'volume_id_list'
op|'='
name|'self'
op|'.'
name|'_attach_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# the first vblade process isn't running"
nl|'\n'
name|'tid'
op|'='
name|'db'
op|'.'
name|'volume_get_iscsi_target_num'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id_list'
op|'['
number|'0'
op|']'
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
name|'volume'
op|'.'
name|'driver'
op|','
string|"'_execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'driver'
op|'.'
name|'_execute'
op|'('
string|'"sudo"'
op|','
string|'"ietadm"'
op|','
string|'"--op"'
op|','
string|'"show"'
op|','
nl|'\n'
string|'"--tid=%(tid)d"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'volume'
op|'.'
name|'check_for_export'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot confirm exported volume id:%s."'
op|')'
op|'%'
name|'volume_id_list'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
number|'0'
op|'<='
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|'.'
name|'find'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'UnsetStubs'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_detach_volume'
op|'('
name|'volume_id_list'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
