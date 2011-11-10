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
name|'log'
name|'as'
name|'logging'
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
op|'.'
name|'scheduler'
name|'import'
name|'zone_manager'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.manager'"
op|')'
newline|'\n'
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
string|"'nova.scheduler.multi.MultiScheduler'"
op|','
nl|'\n'
string|"'Default driver to use for the scheduler'"
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
nl|'\n'
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
name|'self'
op|'.'
name|'zone_manager'
op|'='
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|'('
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'set_zone_manager'
op|'('
name|'self'
op|'.'
name|'zone_manager'
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
DECL|member|periodic_tasks
dedent|''
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll child zones periodically to get status."""'
newline|'\n'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'ping'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_list
dedent|''
name|'def'
name|'get_host_list'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of hosts from the ZoneManager."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'get_host_list'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_zone_list
dedent|''
name|'def'
name|'get_zone_list'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of zones from the ZoneManager."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'get_zone_list'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_zone_capabilities
dedent|''
name|'def'
name|'get_zone_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the normalized set of capabilities for this zone."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'get_zone_capabilities'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|','
name|'service_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
name|'capabilities'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process a capability update from a service node."""'
newline|'\n'
name|'if'
name|'not'
name|'capabilities'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'update_service_capabilities'
op|'('
name|'service_name'
op|','
nl|'\n'
name|'host'
op|','
name|'capabilities'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'context'
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
string|'"""Select a list of hosts best matching the provided specs."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'real_meth'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
name|'driver_method'
op|')'
newline|'\n'
name|'args'
op|'='
op|'('
name|'context'
op|','
op|')'
op|'+'
name|'args'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Driver Method %(driver_method)s missing: %(e)s."'
nl|'\n'
string|'"Reverting to schedule()"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'real_meth'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule'
newline|'\n'
name|'args'
op|'='
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'method'
op|')'
op|'+'
name|'args'
newline|'\n'
nl|'\n'
comment|'# Scheduler methods are responsible for casting.'
nl|'\n'
dedent|''
name|'return'
name|'real_meth'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE (masumotok) : This method should be moved to nova.api.ec2.admin.'
nl|'\n'
comment|'#                    Based on bexar design summit discussion,'
nl|'\n'
comment|'#                    just put this here for bexar release.'
nl|'\n'
DECL|member|show_host_resources
dedent|''
name|'def'
name|'show_host_resources'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shows the physical/usage resource given by hosts.\n\n        :param context: security context\n        :param host: hostname\n        :returns:\n            example format is below.\n            {\'resource\':D, \'usage\':{proj_id1:D, proj_id2:D}}\n            D: {\'vcpus\': 3, \'memory_mb\': 2048, \'local_gb\': 2048,\n                \'vcpus_used\': 12, \'memory_mb_used\': 10240,\n                \'local_gb_used\': 64}\n\n        """'
newline|'\n'
nl|'\n'
comment|'# Getting compute node info and related instances info'
nl|'\n'
name|'compute_ref'
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
name|'compute_ref'
op|'='
name|'compute_ref'
op|'['
number|'0'
op|']'
newline|'\n'
name|'instance_refs'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'compute_ref'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Getting total available/used resource'
nl|'\n'
name|'compute_ref'
op|'='
name|'compute_ref'
op|'['
string|"'compute_node'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'resource'
op|'='
op|'{'
string|"'vcpus'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
name|'compute_ref'
op|'['
string|"'vcpus_used'"
op|']'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
name|'compute_ref'
op|'['
string|"'memory_mb_used'"
op|']'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
name|'compute_ref'
op|'['
string|"'local_gb_used'"
op|']'
op|'}'
newline|'\n'
name|'usage'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance_refs'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Getting usage resource per project'
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
name|'instance_refs'
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
name|'project_id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'vcpus'
op|'='
op|'['
name|'i'
op|'['
string|"'vcpus'"
op|']'
name|'for'
name|'i'
name|'in'
name|'instance_refs'
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'mem'
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
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'disk'
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
name|'if'
name|'i'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'project_id'
op|']'
newline|'\n'
nl|'\n'
name|'usage'
op|'['
name|'project_id'
op|']'
op|'='
op|'{'
string|"'vcpus'"
op|':'
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
name|'vcpus'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
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
name|'mem'
op|')'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
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
name|'disk'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'resource'"
op|':'
name|'resource'
op|','
string|"'usage'"
op|':'
name|'usage'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
