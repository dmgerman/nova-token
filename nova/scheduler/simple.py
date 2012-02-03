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
string|'"""\nSimple Scheduler\n"""'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'chance'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|simple_scheduler_opts
name|'simple_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_cores"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'16'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"maximum number of instance cores to allow per host"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_gigabytes"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"maximum number of volume gigabytes to allow per host"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"max_networks"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"maximum number of networks to allow per host"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'skip_isolated_core_check'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Allow overcommitting vcpus on isolated hosts'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_options'
op|'('
name|'simple_scheduler_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleScheduler
name|'class'
name|'SimpleScheduler'
op|'('
name|'chance'
op|'.'
name|'ChanceScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements Naive Scheduler that tries to find least loaded host."""'
newline|'\n'
nl|'\n'
DECL|member|_schedule_instance
name|'def'
name|'_schedule_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_opts'
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
string|'"""Picks a host that is up and has the fewest running instances."""'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'availability_zone'
op|'='
name|'instance_opts'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|')'
newline|'\n'
nl|'\n'
name|'zone'
op|','
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'default_schedule_zone'
op|','
name|'None'
newline|'\n'
name|'if'
name|'availability_zone'
op|':'
newline|'\n'
indent|'            '
name|'zone'
op|','
name|'_x'
op|','
name|'host'
op|'='
name|'availability_zone'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'host'
name|'and'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'elevated'
op|','
name|'host'
op|','
string|"'nova-compute'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'WillNotSchedule'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'host'
newline|'\n'
nl|'\n'
dedent|''
name|'results'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_sorted'
op|'('
name|'elevated'
op|')'
newline|'\n'
name|'in_isolation'
op|'='
name|'instance_opts'
op|'['
string|"'image_ref'"
op|']'
name|'in'
name|'FLAGS'
op|'.'
name|'isolated_images'
newline|'\n'
name|'check_cores'
op|'='
name|'not'
name|'in_isolation'
name|'or'
name|'not'
name|'FLAGS'
op|'.'
name|'skip_isolated_core_check'
newline|'\n'
name|'if'
name|'zone'
op|':'
newline|'\n'
indent|'            '
name|'results'
op|'='
op|'['
op|'('
name|'service'
op|','
name|'cores'
op|')'
name|'for'
op|'('
name|'service'
op|','
name|'cores'
op|')'
name|'in'
name|'results'
nl|'\n'
name|'if'
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'=='
name|'zone'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'result'
name|'in'
name|'results'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'service'
op|','
name|'instance_cores'
op|')'
op|'='
name|'result'
newline|'\n'
name|'if'
name|'in_isolation'
name|'and'
name|'service'
op|'['
string|"'host'"
op|']'
name|'not'
name|'in'
name|'FLAGS'
op|'.'
name|'isolated_hosts'
op|':'
newline|'\n'
comment|'# isloated images run on isolated hosts'
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'service'
op|'['
string|"'host'"
op|']'
name|'in'
name|'FLAGS'
op|'.'
name|'isolated_hosts'
name|'and'
name|'not'
name|'in_isolation'
op|':'
newline|'\n'
comment|"# images that aren't isolated only run on general hosts"
nl|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'check_cores'
name|'and'
nl|'\n'
name|'instance_cores'
op|'+'
name|'instance_opts'
op|'['
string|"'vcpus'"
op|']'
op|'>'
name|'FLAGS'
op|'.'
name|'max_cores'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Not enough allocatable CPU cores remaining"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
name|'and'
name|'not'
name|'service'
op|'['
string|"'disabled'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"Is the appropriate service running?"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
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
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'self'
op|'.'
name|'_schedule_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'context'
op|','
nl|'\n'
name|'request_spec'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|','
string|"'run_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_ref'
op|'['
string|"'uuid'"
op|']'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
name|'instances'
op|'.'
name|'append'
op|'('
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance_ref'
op|')'
op|')'
newline|'\n'
comment|'# So if we loop around, create_instance_db_entry will actually'
nl|'\n'
comment|"# create a new entry, instead of assume it's been created"
nl|'\n'
comment|'# already'
nl|'\n'
name|'del'
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'instances'
newline|'\n'
nl|'\n'
DECL|member|schedule_create_volume
dedent|''
name|'def'
name|'schedule_create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
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
string|'"""Picks a host that is up and has the fewest volumes."""'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'availability_zone'
op|'='
name|'volume_ref'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|')'
newline|'\n'
nl|'\n'
name|'zone'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'None'
newline|'\n'
name|'if'
name|'availability_zone'
op|':'
newline|'\n'
indent|'            '
name|'zone'
op|','
name|'_x'
op|','
name|'host'
op|'='
name|'availability_zone'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'host'
name|'and'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'elevated'
op|','
name|'host'
op|','
string|"'nova-volume'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'WillNotSchedule'
op|'('
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
name|'driver'
op|'.'
name|'cast_to_volume_host'
op|'('
name|'context'
op|','
name|'host'
op|','
string|"'create_volume'"
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'results'
op|'='
name|'db'
op|'.'
name|'service_get_all_volume_sorted'
op|'('
name|'elevated'
op|')'
newline|'\n'
name|'if'
name|'zone'
op|':'
newline|'\n'
indent|'            '
name|'results'
op|'='
op|'['
op|'('
name|'service'
op|','
name|'gigs'
op|')'
name|'for'
op|'('
name|'service'
op|','
name|'gigs'
op|')'
name|'in'
name|'results'
nl|'\n'
name|'if'
name|'service'
op|'['
string|"'availability_zone'"
op|']'
op|'=='
name|'zone'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'result'
name|'in'
name|'results'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'service'
op|','
name|'volume_gigabytes'
op|')'
op|'='
name|'result'
newline|'\n'
name|'if'
name|'volume_gigabytes'
op|'+'
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|'>'
name|'FLAGS'
op|'.'
name|'max_gigabytes'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Not enough allocatable volume gigabytes remaining"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'utils'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
name|'and'
name|'not'
name|'service'
op|'['
string|"'disabled'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'driver'
op|'.'
name|'cast_to_volume_host'
op|'('
name|'context'
op|','
name|'service'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'create_volume'"
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"Is the appropriate service running?"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
