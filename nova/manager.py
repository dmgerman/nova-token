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
nl|'\n'
string|'"""Base Manager class.\n\nManagers are responsible for a certain aspect of the system.  It is a logical\ngrouping of code relating to a portion of the system.  In general other\ncomponents should be using the manager to make changes to the components that\nit is responsible for.\n\nFor example, other components that need to deal with volumes in some way,\nshould do so by calling methods on the VolumeManager instead of directly\nchanging fields in the database.  This allows us to keep all of the code\nrelating to volumes in the same place.\n\nWe have adopted a basic strategy of Smart managers and dumb data, which means\nrather than attaching methods to data objects, components should call manager\nmethods that act on the data.\n\nMethods on managers that can be executed locally should be called directly. If\na particular method must execute on a remote host, this should be done via rpc\nto the service that wraps the manager\n\nManagers should be responsible for most of the db access, and\nnon-implementation specific data.  Anything implementation specific that can\'t\nbe generalized should be done by the Driver.\n\nIn general, we prefer to have one manager with multiple drivers for different\nimplementations, but sometimes it makes sense to have multiple managers.  You\ncan think of it this way: Abstract different overall strategies at the manager\nlevel(FlatNetwork vs VlanNetwork), and different implementations at the driver\nlevel(LinuxNetDriver vs CiscoNetDriver).\n\nManagers will often provide methods for initial setup of a host or periodic\ntasks to a wrapping service.\n\nThis module provides Manager, a base class for managers.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'plugin'
name|'import'
name|'pluginmanager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
name|'import'
name|'dispatcher'
name|'as'
name|'rpc_dispatcher'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
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
nl|'\n'
DECL|function|periodic_task
name|'def'
name|'periodic_task'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator to indicate that a method is a periodic task.\n\n    This decorator can be used in two ways:\n\n        1. Without arguments \'@periodic_task\', this will be run on every tick\n           of the periodic scheduler.\n\n        2. With arguments, @periodic_task(ticks_between_runs=N), this will be\n           run on every N ticks of the periodic scheduler.\n    """'
newline|'\n'
DECL|function|decorator
name|'def'
name|'decorator'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'.'
name|'_periodic_task'
op|'='
name|'True'
newline|'\n'
name|'f'
op|'.'
name|'_ticks_between_runs'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'ticks_between_runs'"
op|','
number|'0'
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): The `if` is necessary to allow the decorator to be used with'
nl|'\n'
comment|'# and without parens.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# In the 'with-parens' case (with kwargs present), this function needs to"
nl|'\n'
comment|'# return a decorator function since the interpreter will invoke it like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   periodic_task(*args, **kwargs)(f)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# In the 'without-parens' case, the original function will be passed"
nl|'\n'
comment|'# in as the first argument, like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   periodic_task(f)'
nl|'\n'
dedent|''
name|'if'
name|'kwargs'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'decorator'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'decorator'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ManagerMeta
dedent|''
dedent|''
name|'class'
name|'ManagerMeta'
op|'('
name|'type'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'cls'
op|','
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Metaclass that allows us to collect decorated periodic tasks."""'
newline|'\n'
name|'super'
op|'('
name|'ManagerMeta'
op|','
name|'cls'
op|')'
op|'.'
name|'__init__'
op|'('
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): if the attribute is not present then we must be the base'
nl|'\n'
comment|'# class, so, go ahead an initialize it. If the attribute is present,'
nl|'\n'
comment|"# then we're a subclass so make a copy of it so we don't step on our"
nl|'\n'
comment|"# parent's toes."
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'='
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'['
op|':'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_ticks_to_skip'
op|'='
name|'cls'
op|'.'
name|'_ticks_to_skip'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_ticks_to_skip'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'value'
name|'in'
name|'cls'
op|'.'
name|'__dict__'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'getattr'
op|'('
name|'value'
op|','
string|"'_periodic_task'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'='
name|'value'
newline|'\n'
name|'name'
op|'='
name|'task'
op|'.'
name|'__name__'
newline|'\n'
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'.'
name|'append'
op|'('
op|'('
name|'name'
op|','
name|'task'
op|')'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'_ticks_to_skip'
op|'['
name|'name'
op|']'
op|'='
name|'task'
op|'.'
name|'_ticks_between_runs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Manager
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Manager'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
DECL|variable|__metaclass__
indent|'    '
name|'__metaclass__'
op|'='
name|'ManagerMeta'
newline|'\n'
nl|'\n'
comment|'# Set RPC API version to 1.0 by default.'
nl|'\n'
DECL|variable|RPC_API_VERSION
name|'RPC_API_VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'db_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'CONF'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'load_plugins'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'Manager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'db_driver'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load_plugins
dedent|''
name|'def'
name|'load_plugins'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pluginmgr'
op|'='
name|'pluginmanager'
op|'.'
name|'PluginManager'
op|'('
string|"'nova'"
op|','
name|'self'
op|'.'
name|'__class__'
op|')'
newline|'\n'
name|'pluginmgr'
op|'.'
name|'load_plugins'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_rpc_dispatcher
dedent|''
name|'def'
name|'create_rpc_dispatcher'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Get the rpc dispatcher for this manager.\n\n        If a manager would like to set an rpc API version, or support more than\n        one class as the target of rpc messages, override this method.\n        '''"
newline|'\n'
name|'return'
name|'rpc_dispatcher'
op|'.'
name|'RpcDispatcher'
op|'('
op|'['
name|'self'
op|']'
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
op|','
name|'raise_on_error'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
name|'for'
name|'task_name'
op|','
name|'task'
name|'in'
name|'self'
op|'.'
name|'_periodic_tasks'
op|':'
newline|'\n'
indent|'            '
name|'full_task_name'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'task_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'ticks_to_skip'
op|'='
name|'self'
op|'.'
name|'_ticks_to_skip'
op|'['
name|'task_name'
op|']'
newline|'\n'
name|'if'
name|'ticks_to_skip'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Skipping %(full_task_name)s, %(ticks_to_skip)s"'
nl|'\n'
string|'" ticks left until next run"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ticks_to_skip'
op|'['
name|'task_name'
op|']'
op|'-='
number|'1'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_ticks_to_skip'
op|'['
name|'task_name'
op|']'
op|'='
name|'task'
op|'.'
name|'_ticks_between_runs'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Running periodic task %(full_task_name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'('
name|'self'
op|','
name|'context'
op|')'
newline|'\n'
comment|'# NOTE(tiantian): After finished a task, allow manager to'
nl|'\n'
comment|'# do other work (report_state, processing AMPQ request etc.)'
nl|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'raise_on_error'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Error during %(full_task_name)s: %(e)s"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
dedent|''
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Hook to do additional manager initialization when one requests\n        the service be started.  This is called before any service record\n        is created.\n\n        Child classes should override this method.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|pre_start_hook
dedent|''
name|'def'
name|'pre_start_hook'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Hook to provide the manager the ability to do additional\n        start-up work before any RPC queues/consumers are created. This is\n        called after other initialization has succeeded and a service\n        record is created.\n\n        Child classes should override this method.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|post_start_hook
dedent|''
name|'def'
name|'post_start_hook'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Hook to provide the manager the ability to do additional\n        start-up work immediately after a service creates RPC consumers\n        and starts \'running\'.\n\n        Child classes should override this method.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|service_version
dedent|''
name|'def'
name|'service_version'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'version'
op|'.'
name|'version_string'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_config
dedent|''
name|'def'
name|'service_config'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'config'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'CONF'
op|':'
newline|'\n'
indent|'            '
name|'config'
op|'['
name|'key'
op|']'
op|'='
name|'CONF'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerDependentManager
dedent|''
dedent|''
name|'class'
name|'SchedulerDependentManager'
op|'('
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Periodically send capability updates to the Scheduler services.\n\n    Services that need to update the Scheduler of their capabilities\n    should derive from this class. Otherwise they can derive from\n    manager.Manager directly. Updates are only sent after\n    update_service_capabilities is called with non-None values.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'db_driver'
op|'='
name|'None'
op|','
name|'service_name'
op|'='
string|"'undefined'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'last_capabilities'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'service_name'
op|'='
name|'service_name'
newline|'\n'
name|'self'
op|'.'
name|'scheduler_rpcapi'
op|'='
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'SchedulerDependentManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'host'
op|','
name|'db_driver'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load_plugins
dedent|''
name|'def'
name|'load_plugins'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pluginmgr'
op|'='
name|'pluginmanager'
op|'.'
name|'PluginManager'
op|'('
string|"'nova'"
op|','
name|'self'
op|'.'
name|'service_name'
op|')'
newline|'\n'
name|'pluginmgr'
op|'.'
name|'load_plugins'
op|'('
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
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remember these capabilities to send on next periodic update."""'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'capabilities'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'capabilities'
op|'='
op|'['
name|'capabilities'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'last_capabilities'
op|'='
name|'capabilities'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'periodic_task'
newline|'\n'
DECL|member|publish_service_capabilities
name|'def'
name|'publish_service_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pass data back to the scheduler.\n\n        Called at a periodic interval. And also called via rpc soon after\n        the start of the scheduler.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'last_capabilities'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Notifying Schedulers of capabilities ...'"
op|')'
op|')'
newline|'\n'
name|'for'
name|'capability_item'
name|'in'
name|'self'
op|'.'
name|'last_capabilities'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'scheduler_rpcapi'
op|'.'
name|'update_service_capabilities'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service_name'
op|','
name|'self'
op|'.'
name|'host'
op|','
name|'capability_item'
op|')'
newline|'\n'
comment|'# TODO(NTTdocomo): Make update_service_capabilities() accept a list'
nl|'\n'
comment|'#                  of capabilities'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
