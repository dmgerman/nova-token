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
name|'flags'
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
string|'"max_cores"'
op|','
number|'16'
op|','
nl|'\n'
string|'"maximum number of instance cores to allow per host"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|'"max_gigabytes"'
op|','
number|'10000'
op|','
nl|'\n'
string|'"maximum number of volume gigabytes to allow per host"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|'"max_networks"'
op|','
number|'1000'
op|','
nl|'\n'
string|'"maximum number of networks to allow per host"'
op|')'
newline|'\n'
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
DECL|member|schedule_run_instance
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
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
name|'results'
op|'='
name|'db'
op|'.'
name|'service_get_all_compute_sorted'
op|'('
name|'context'
op|')'
newline|'\n'
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
name|'instance_cores'
op|'+'
name|'instance_ref'
op|'['
string|"'vcpus'"
op|']'
op|'>'
name|'FLAGS'
op|'.'
name|'max_cores'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"All hosts have too many cores"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): this probably belongs in the manager, if we'
nl|'\n'
comment|'#             can generalize this somehow'
nl|'\n'
indent|'                '
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'service'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"No hosts found"'
op|')'
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
name|'results'
op|'='
name|'db'
op|'.'
name|'service_get_all_volume_sorted'
op|'('
name|'context'
op|')'
newline|'\n'
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
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"All hosts have too many gigabytes"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): this probably belongs in the manager, if we'
nl|'\n'
comment|'#             can generalize this somehow'
nl|'\n'
indent|'                '
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'service'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'service'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"No hosts found"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_set_network_host
dedent|''
name|'def'
name|'schedule_set_network_host'
op|'('
name|'self'
op|','
name|'context'
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
string|'"""Picks a host that is up and has the fewest networks."""'
newline|'\n'
nl|'\n'
name|'results'
op|'='
name|'db'
op|'.'
name|'service_get_all_network_sorted'
op|'('
name|'context'
op|')'
newline|'\n'
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
name|'instance_count'
op|')'
op|'='
name|'result'
newline|'\n'
name|'if'
name|'instance_count'
op|'>='
name|'FLAGS'
op|'.'
name|'max_networks'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"All hosts have too many networks"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
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
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
string|'"No hosts found"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
