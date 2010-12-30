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
string|'"""\nScheduler Service\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'functools'
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
name|'manager'
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
name|'import'
name|'exception'
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
name|'DEFINE_string'
op|'('
string|"'scheduler_driver'"
op|','
nl|'\n'
string|"'nova.scheduler.chance.ChanceScheduler'"
op|','
nl|'\n'
string|"'Driver to use for the scheduler'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerManager
name|'class'
name|'SchedulerManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Chooses a host to run instances on."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'scheduler_driver'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'scheduler_driver'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_driver'
op|'='
name|'FLAGS'
op|'.'
name|'scheduler_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'scheduler_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'SchedulerManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Converts all method calls to use the schedule method"""'
newline|'\n'
name|'return'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'self'
op|'.'
name|'_schedule'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'context'
op|','
name|'topic'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tries to call schedule_* method on the driver to retrieve host.\n\n        Falls back to schedule(context, topic) if method doesn\'t exist.\n        """'
newline|'\n'
name|'driver_method'
op|'='
string|"'schedule_%s'"
op|'%'
name|'method'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
name|'driver_method'
op|')'
op|'('
name|'elevated'
op|','
op|'*'
name|'args'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule'
op|'('
name|'elevated'
op|','
name|'topic'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cast'
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
name|'topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
name|'method'
op|','
nl|'\n'
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casting to %s %s for %s"'
op|')'
op|','
name|'topic'
op|','
name|'host'
op|','
name|'method'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE (masumotok) : This method should be moved to nova.api.ec2.admin.'
nl|'\n'
comment|'#                    Based on bear design summit discussion,'
nl|'\n'
comment|'#                    just put this here for bexar release.'
nl|'\n'
DECL|member|show_host_resource
dedent|''
name|'def'
name|'show_host_resource'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" show the physical/usage resource given by hosts."""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host_ref'
op|'='
name|'db'
op|'.'
name|'host_get_by_name'
op|'('
name|'context'
op|','
name|'host'
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
name|'return'
op|'{'
string|"'ret'"
op|':'
name|'False'
op|','
string|"'msg'"
op|':'
string|"'No such Host'"
op|'}'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
comment|'# Getting physical resource information'
nl|'\n'
dedent|''
name|'h_resource'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'host_ref'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'host_ref'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'host_ref'
op|'['
string|"'local_gb'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Getting usage resource information'
nl|'\n'
name|'u_resource'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instances_ref'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
number|'0'
op|'=='
name|'len'
op|'('
name|'instances_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'ret'"
op|':'
name|'True'
op|','
string|"'phy_resource'"
op|':'
name|'h_resource'
op|','
string|"'usage'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'project_ids'
op|'='
op|'['
name|'i'
op|'['
string|"'project_id'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instances_ref'
op|']'
newline|'\n'
name|'project_ids'
op|'='
name|'list'
op|'('
name|'set'
op|'('
name|'project_ids'
op|')'
op|')'
newline|'\n'
name|'for'
name|'p_id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'vcpus'
op|'='
name|'db'
op|'.'
name|'instance_get_vcpu_sum_by_host_and_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'p_id'
op|')'
newline|'\n'
name|'mem'
op|'='
name|'db'
op|'.'
name|'instance_get_memory_sum_by_host_and_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'p_id'
op|')'
newline|'\n'
name|'hdd'
op|'='
name|'db'
op|'.'
name|'instance_get_disk_sum_by_host_and_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'p_id'
op|')'
newline|'\n'
name|'u_resource'
op|'['
name|'p_id'
op|']'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'hdd'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'ret'"
op|':'
name|'True'
op|','
string|"'phy_resource'"
op|':'
name|'h_resource'
op|','
string|"'usage'"
op|':'
name|'u_resource'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
