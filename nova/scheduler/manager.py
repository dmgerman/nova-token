begin_unit
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_service'
name|'import'
name|'periodic_task'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'stevedore'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
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
DECL|variable|target
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'version'
op|'='
string|"'4.3'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_sentinel
name|'_sentinel'
op|'='
name|'object'
op|'('
op|')'
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
name|'if'
name|'not'
name|'scheduler_driver'
op|':'
newline|'\n'
indent|'            '
name|'scheduler_driver'
op|'='
name|'CONF'
op|'.'
name|'scheduler_driver'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
op|'.'
name|'DriverManager'
op|'('
nl|'\n'
string|'"nova.scheduler.driver"'
op|','
nl|'\n'
name|'scheduler_driver'
op|','
nl|'\n'
name|'invoke_on_load'
op|'='
name|'True'
op|')'
op|'.'
name|'driver'
newline|'\n'
comment|'# TODO(Yingxin): Change to catch stevedore.exceptions.NoMatches after'
nl|'\n'
comment|'# stevedore v1.9.0'
nl|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|':'
newline|'\n'
comment|'# NOTE(Yingxin): Loading full class path is deprecated and should'
nl|'\n'
comment|'# be removed in the N release.'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'scheduler_driver'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"DEPRECATED: scheduler_driver uses "'
nl|'\n'
string|'"classloader to load %(path)s. This legacy "'
nl|'\n'
string|'"loading style will be removed in the "'
nl|'\n'
string|'"N release."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'scheduler_driver'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ImportError'
op|','
name|'ValueError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Cannot load scheduler driver from configuration "'
nl|'\n'
string|'"%(conf)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'conf'"
op|':'
name|'scheduler_driver'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'super'
op|'('
name|'SchedulerManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'scheduler'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
newline|'\n'
DECL|member|_expire_reservations
name|'def'
name|'_expire_reservations'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'QUOTAS'
op|'.'
name|'expire'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'periodic_task'
op|'.'
name|'periodic_task'
op|'('
name|'spacing'
op|'='
name|'CONF'
op|'.'
name|'scheduler_driver_task_period'
op|','
nl|'\n'
name|'run_immediately'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|_run_periodic_tasks
name|'def'
name|'_run_periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'run_periodic_tasks'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'messaging'
op|'.'
name|'expected_exceptions'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|')'
newline|'\n'
DECL|member|select_destinations
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'None'
op|','
name|'filter_properties'
op|'='
name|'None'
op|','
nl|'\n'
name|'spec_obj'
op|'='
name|'_sentinel'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns destinations(s) best suited for this RequestSpec.\n\n        The result should be a list of dicts with \'host\', \'nodename\' and\n        \'limits\' as keys.\n        """'
newline|'\n'
nl|'\n'
comment|'# TODO(sbauza): Change the method signature to only accept a spec_obj'
nl|'\n'
comment|'# argument once API v5 is provided.'
nl|'\n'
name|'if'
name|'spec_obj'
name|'is'
name|'self'
op|'.'
name|'_sentinel'
op|':'
newline|'\n'
indent|'            '
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'.'
name|'from_primitives'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
dedent|''
name|'dests'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
name|'ctxt'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'dests'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_aggregates
dedent|''
name|'def'
name|'update_aggregates'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates HostManager internal aggregates information.\n\n        :param aggregates: Aggregate(s) to update\n        :type aggregates: :class:`nova.objects.Aggregate`\n                          or :class:`nova.objects.AggregateList`\n        """'
newline|'\n'
comment|"# NOTE(sbauza): We're dropping the user context now as we don't need it"
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'update_aggregates'
op|'('
name|'aggregates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_aggregate
dedent|''
name|'def'
name|'delete_aggregate'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes HostManager internal information about a specific aggregate.\n\n        :param aggregate: Aggregate to delete\n        :type aggregate: :class:`nova.objects.Aggregate`\n        """'
newline|'\n'
comment|"# NOTE(sbauza): We're dropping the user context now as we don't need it"
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'delete_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_instance_info
dedent|''
name|'def'
name|'update_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives information about changes to a host\'s instances, and\n        updates the driver\'s HostManager with that information.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'update_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_instance_info
dedent|''
name|'def'
name|'delete_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives information about the deletion of one of a host\'s\n        instances, and updates the driver\'s HostManager with that information.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'delete_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|sync_instance_info
dedent|''
name|'def'
name|'sync_instance_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host_name'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Receives a sync request from a host, and passes it on to the\n        driver\'s HostManager.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|'.'
name|'sync_instance_info'
op|'('
name|'context'
op|','
name|'host_name'
op|','
nl|'\n'
name|'instance_uuids'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
