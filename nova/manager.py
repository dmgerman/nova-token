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
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'baserpc'
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
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
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
name|'import'
name|'periodic_task'
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
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
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
DECL|class|Manager
name|'class'
name|'Manager'
op|'('
name|'base'
op|'.'
name|'Base'
op|','
name|'periodic_task'
op|'.'
name|'PeriodicTasks'
op|')'
op|':'
newline|'\n'
comment|'# Set RPC API version to 1.0 by default.'
nl|'\n'
DECL|variable|RPC_API_VERSION
indent|'    '
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
op|','
name|'service_name'
op|'='
string|"'undefined'"
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
name|'backdoor_port'
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
name|'notifier'
op|'='
name|'notifier'
op|'.'
name|'get_notifier'
op|'('
name|'self'
op|'.'
name|'service_name'
op|','
name|'self'
op|'.'
name|'host'
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
DECL|member|create_rpc_dispatcher
dedent|''
name|'def'
name|'create_rpc_dispatcher'
op|'('
name|'self'
op|','
name|'backdoor_port'
op|'='
name|'None'
op|','
name|'additional_apis'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Get the rpc dispatcher for this manager.\n\n        If a manager would like to set an rpc API version, or support more than\n        one class as the target of rpc messages, override this method.\n        '''"
newline|'\n'
name|'apis'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'additional_apis'
op|':'
newline|'\n'
indent|'            '
name|'apis'
op|'.'
name|'extend'
op|'('
name|'additional_apis'
op|')'
newline|'\n'
dedent|''
name|'base_rpc'
op|'='
name|'baserpc'
op|'.'
name|'BaseRPCAPI'
op|'('
name|'self'
op|'.'
name|'service_name'
op|','
name|'backdoor_port'
op|')'
newline|'\n'
name|'apis'
op|'.'
name|'extend'
op|'('
op|'['
name|'self'
op|','
name|'base_rpc'
op|']'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rpc_dispatcher'
op|'.'
name|'RpcDispatcher'
op|'('
name|'apis'
op|','
name|'serializer'
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
name|'return'
name|'self'
op|'.'
name|'run_periodic_tasks'
op|'('
name|'context'
op|','
name|'raise_on_error'
op|'='
name|'raise_on_error'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
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
dedent|''
dedent|''
endmarker|''
end_unit
