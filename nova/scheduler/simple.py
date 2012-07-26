begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
string|'"""\nSimple Scheduler - for Volumes\n\nNote: Deprecated in Folsom.  Will be removed along with nova-volumes\n"""'
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
name|'chance'
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
name|'register_opts'
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
DECL|member|schedule_create_volume
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
