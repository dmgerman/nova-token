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
string|'"""\nScheduler that allows routing some calls to one driver and others to another.\n\nThis scheduler was originally used to deal with both compute and volume. But\nis now used for openstack extensions that want to use the nova-scheduler to\nschedule requests to compute nodes but provide their own manager and topic.\n\nhttps://bugs.launchpad.net/nova/+bug/1009681\n"""'
newline|'\n'
nl|'\n'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|multi_scheduler_opts
name|'multi_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'compute_scheduler_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.'"
nl|'\n'
string|"'filter_scheduler.FilterScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for scheduling compute calls'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_scheduler_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.chance.ChanceScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default driver to use for scheduling calls'"
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
name|'multi_scheduler_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultiScheduler
name|'class'
name|'MultiScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A scheduler that holds multiple sub-schedulers.\n\n    This exists to allow flag-driven composibility of schedulers, allowing\n    third parties to integrate custom schedulers more easily.\n\n    """'
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
name|'super'
op|'('
name|'MultiScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'compute_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_scheduler_driver'
op|')'
newline|'\n'
name|'default_driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_scheduler_driver'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'drivers'
op|'='
op|'{'
string|"'compute'"
op|':'
name|'compute_driver'
op|','
nl|'\n'
string|"'default'"
op|':'
name|'default_driver'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
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
name|'return'
name|'self'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'schedule_run_instance'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
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
name|'return'
name|'self'
op|'.'
name|'drivers'
op|'['
string|"'compute'"
op|']'
op|'.'
name|'schedule_prep_resize'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
comment|'# Multi scheduler is only a holder of sub-schedulers, so'
nl|'\n'
comment|'# pass the capabilities to the schedulers that matter'
nl|'\n'
indent|'        '
name|'for'
name|'d'
name|'in'
name|'self'
op|'.'
name|'drivers'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'.'
name|'update_service_capabilities'
op|'('
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
