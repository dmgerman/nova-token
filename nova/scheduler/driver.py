begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nScheduler base class that all Schedulers should inherit from\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
nl|'\n'
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
name|'DEFINE_integer'
op|'('
string|"'service_down_time'"
op|','
number|'60'
op|','
nl|'\n'
string|"'maximum time since last checkin for up service'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoValidHost
name|'class'
name|'NoValidHost'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""There is no valid host for the command."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WillNotSchedule
dedent|''
name|'class'
name|'WillNotSchedule'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The specified host is not up or doesn\'t exist."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Scheduler
dedent|''
name|'class'
name|'Scheduler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The base class that all Scheduler clases should inherit from."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'zone_manager'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|set_zone_manager
dedent|''
name|'def'
name|'set_zone_manager'
op|'('
name|'self'
op|','
name|'zone_manager'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by the Scheduler Service to supply a ZoneManager."""'
newline|'\n'
name|'self'
op|'.'
name|'zone_manager'
op|'='
name|'zone_manager'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|service_is_up
name|'def'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check whether a service is up based on last heartbeat."""'
newline|'\n'
name|'last_heartbeat'
op|'='
name|'service'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'service'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
comment|'# Timestamps in DB are UTC.'
nl|'\n'
name|'elapsed'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'last_heartbeat'
newline|'\n'
name|'return'
name|'elapsed'
op|'<'
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'FLAGS'
op|'.'
name|'service_down_time'
op|')'
newline|'\n'
nl|'\n'
DECL|member|hosts_up
dedent|''
name|'def'
name|'hosts_up'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of hosts that have a running service for topic."""'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
op|'['
name|'service'
op|'.'
name|'host'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override at least this method for scheduler to work."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"Must implement a fallback schedule"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_live_migration
dedent|''
name|'def'
name|'schedule_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration scheduling method.\n\n        :param context:\n        :param instance_id:\n        :param dest: destination host\n        :return:\n            The host where instance is running currently.\n            Then scheduler send request that host.\n        """'
newline|'\n'
comment|'# Whether instance exists and is running.'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking instance.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_src_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking destination host.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_dest_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
comment|'# Common checking.'
nl|'\n'
name|'self'
op|'.'
name|'_live_migration_common_check'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
comment|'# Changing instance_state.'
nl|'\n'
name|'values'
op|'='
op|'{'
string|'"vm_state"'
op|':'
name|'vm_states'
op|'.'
name|'MIGRATE'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
comment|'# Changing volume state'
nl|'\n'
name|'for'
name|'volume_ref'
name|'in'
name|'instance_ref'
op|'['
string|"'volumes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'migrating'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Return value is necessary to send request to src'
nl|'\n'
comment|'# Check _schedule() in detail.'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'return'
name|'src'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_src_check
dedent|''
name|'def'
name|'_live_migration_src_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for src host).\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Checking instance is running.'
nl|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'power_state'"
op|']'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotRunning'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checing volume node is running when any volumes are mounted'
nl|'\n'
comment|'# to the instance.'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'instance_ref'
op|'['
string|"'volumes'"
op|']'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
string|"'volume'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'services'
op|')'
op|'<'
number|'1'
name|'or'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'VolumeServiceUnavailable'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking src host exists and compute node'
nl|'\n'
dedent|''
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'src'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking src host is alive.'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'services'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'src'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_dest_check
dedent|''
dedent|''
name|'def'
name|'_live_migration_dest_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration check routine (for destination host).\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Checking dest exists and compute node.'
nl|'\n'
name|'dservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'dservice_ref'
op|'='
name|'dservice_refs'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking dest host is alive.'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'dservice_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ComputeServiceUnavailable'
op|'('
name|'host'
op|'='
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking whether The host where instance is running'
nl|'\n'
comment|'# and dest is not same.'
nl|'\n'
dedent|''
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'dest'
op|'=='
name|'src'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnableToMigrateToSelf'
op|'('
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'host'
op|'='
name|'dest'
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking dst host still has enough capacities.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_compute_node_has_enough_resources'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|','
nl|'\n'
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_live_migration_common_check
dedent|''
name|'def'
name|'_live_migration_common_check'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'block_migration'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Live migration common check routine.\n\n        Below checkings are followed by\n        http://wiki.libvirt.org/page/TodoPreMigrationChecks\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n        :param block_migration if True, check for block_migration.\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Checking shared storage connectivity'
nl|'\n'
comment|'# if block migration, instances_paths should not be on shared storage.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mounted_on_same_shared_storage'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'block_migration'
op|':'
newline|'\n'
indent|'                '
name|'reason'
op|'='
name|'_'
op|'('
string|'"Block migration can not be used "'
nl|'\n'
string|'"with shared storage."'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidSharedStorage'
op|'('
name|'reason'
op|'='
name|'reason'
op|','
name|'path'
op|'='
name|'dest'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FileNotFound'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'block_migration'
op|':'
newline|'\n'
indent|'                '
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'ipath'
op|'='
name|'FLAGS'
op|'.'
name|'instances_path'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Cannot confirm tmpfile at %(ipath)s is on "'
nl|'\n'
string|'"same shared storage between %(src)s "'
nl|'\n'
string|'"and %(dest)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
comment|'# Checking dest exists.'
nl|'\n'
dedent|''
dedent|''
name|'dservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'dservice_ref'
op|'='
name|'dservice_refs'
op|'['
number|'0'
op|']'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking original host( where instance was launched at) exists.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'oservice_refs'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'launched_on'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'SourceHostUnavailable'
op|'('
op|')'
newline|'\n'
dedent|''
name|'oservice_ref'
op|'='
name|'oservice_refs'
op|'['
number|'0'
op|']'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Checking hypervisor is same.'
nl|'\n'
name|'orig_hypervisor'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'dest_hypervisor'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_type'"
op|']'
newline|'\n'
name|'if'
name|'orig_hypervisor'
op|'!='
name|'dest_hypervisor'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidHypervisorType'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Checkng hypervisor version.'
nl|'\n'
dedent|''
name|'orig_hypervisor'
op|'='
name|'oservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'dest_hypervisor'
op|'='
name|'dservice_ref'
op|'['
string|"'hypervisor_version'"
op|']'
newline|'\n'
name|'if'
name|'orig_hypervisor'
op|'>'
name|'dest_hypervisor'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'DestinationHypervisorTooOld'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Checking cpuinfo.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'dest'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'compare_cpu'"
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|"'cpu_info'"
op|':'
name|'oservice_ref'
op|'['
string|"'cpu_info'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'rpc'
op|'.'
name|'RemoteError'
op|':'
newline|'\n'
indent|'            '
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"host %(dest)s is not compatible with "'
nl|'\n'
string|'"original host %(src)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|assert_compute_node_has_enough_resources
dedent|''
dedent|''
name|'def'
name|'assert_compute_node_has_enough_resources'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest'
op|','
name|'block_migration'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
string|'"""Checks if destination host has enough resource for live migration.\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n        :param block_migration: if True, disk checking has been done\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'assert_compute_node_has_enough_memory'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'block_migration'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assert_compute_node_has_enough_disk'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assert_compute_node_has_enough_memory
dedent|''
name|'def'
name|'assert_compute_node_has_enough_memory'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks if destination host has enough memory for live migration.\n\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Getting total available memory and disk of host'
nl|'\n'
name|'avail'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'context'
op|','
name|'dest'
op|','
string|"'memory_mb'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting total used memory and disk of host'
nl|'\n'
comment|'# It should be sum of memories that are assigned as max value,'
nl|'\n'
comment|'# because overcommiting is risky.'
nl|'\n'
name|'used'
op|'='
number|'0'
newline|'\n'
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'used_list'
op|'='
op|'['
name|'i'
op|'['
string|"'memory_mb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|']'
newline|'\n'
name|'if'
name|'used_list'
op|':'
newline|'\n'
indent|'            '
name|'used'
op|'='
name|'reduce'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'+'
name|'y'
op|','
name|'used_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mem_inst'
op|'='
name|'instance_ref'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'avail'
op|'='
name|'avail'
op|'-'
name|'used'
newline|'\n'
name|'if'
name|'avail'
op|'<='
name|'mem_inst'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Unable to migrate %(instance_id)s to %(dest)s: "'
nl|'\n'
string|'"Lack of disk(host:%(avail)s <= instance:%(mem_inst)s)"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MigrationError'
op|'('
name|'reason'
op|'='
name|'reason'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assert_compute_node_has_enough_disk
dedent|''
dedent|''
name|'def'
name|'assert_compute_node_has_enough_disk'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Checks if destination host has enough disk for block migration.\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Getting total available memory and disk of host'
nl|'\n'
name|'avail'
op|'='
name|'self'
op|'.'
name|'_get_compute_info'
op|'('
name|'context'
op|','
name|'dest'
op|','
string|"'local_gb'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting total used memory and disk of host'
nl|'\n'
comment|'# It should be sum of disks that are assigned as max value'
nl|'\n'
comment|'# because overcommiting is risky.'
nl|'\n'
name|'used'
op|'='
number|'0'
newline|'\n'
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'dest'
op|')'
newline|'\n'
name|'used_list'
op|'='
op|'['
name|'i'
op|'['
string|"'local_gb'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
op|']'
newline|'\n'
name|'if'
name|'used_list'
op|':'
newline|'\n'
indent|'            '
name|'used'
op|'='
name|'reduce'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'+'
name|'y'
op|','
name|'used_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'disk_inst'
op|'='
name|'instance_ref'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'avail'
op|'='
name|'avail'
op|'-'
name|'used'
newline|'\n'
name|'if'
name|'avail'
op|'<='
name|'disk_inst'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Unable to migrate %(instance_id)s to %(dest)s: "'
nl|'\n'
string|'"Lack of disk(host:%(avail)s "'
nl|'\n'
string|'"<= instance:%(disk_inst)s)"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MigrationError'
op|'('
name|'reason'
op|'='
name|'reason'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_compute_info
dedent|''
dedent|''
name|'def'
name|'_get_compute_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""get compute node\'s infomation specified by key\n\n        :param context: security context\n        :param host: hostname(must be compute node)\n        :param key: column name of compute_nodes\n        :return: value specified by key\n\n        """'
newline|'\n'
name|'compute_node_ref'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'compute_node_ref'
op|'='
name|'compute_node_ref'
op|'['
number|'0'
op|']'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'compute_node_ref'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|mounted_on_same_shared_storage
dedent|''
name|'def'
name|'mounted_on_same_shared_storage'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the src and dest host mount same shared storage.\n\n        At first, dest host creates temp file, and src host can see\n        it if they mounts same shared storage. Then src host erase it.\n\n        :param context: security context\n        :param instance_ref: nova.db.sqlalchemy.models.Instance object\n        :param dest: destination host\n\n        """'
newline|'\n'
nl|'\n'
name|'src'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'dst_t'
op|'='
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'dest'
op|')'
newline|'\n'
name|'src_t'
op|'='
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'src'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# create tmpfile at dest host'
nl|'\n'
indent|'            '
name|'filename'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'dst_t'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'create_shared_storage_test_file'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure existence at src host.'
nl|'\n'
name|'ret'
op|'='
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'src_t'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'check_shared_storage_test_file'"
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'FileNotFound'
op|'('
name|'file_path'
op|'='
name|'filename'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FileNotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'dst_t'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|"'cleanup_shared_storage_test_file'"
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
