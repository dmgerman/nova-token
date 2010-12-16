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
string|'"""\nHandles all processes relating to instances (guest vms).\n\nThe :py:class:`ComputeManager` class is a :py:class:`nova.manager.Manager` that\nhandles RPC calls relating to creating instances.  It is responsible for\nbuilding a disk image, launching it via the underlying virtualization driver,\nresponding to calls to check its state, attaching persistent storage, and\nterminating it.\n\n**Related Flags**\n\n:instances_path:  Where instances are kept on disk\n:compute_driver:  Name of class that is used to handle virtualization, loaded\n                  by :func:`nova.utils.import_object`\n:volume_manager:  Name of class that handles persistent storage, loaded by\n                  :func:`nova.utils.import_object`\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
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
name|'manager'
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
string|"'instances_path'"
op|','
string|"'$state_path/instances'"
op|','
nl|'\n'
string|"'where instances are stored on disk'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.connection.get_connection'"
op|','
nl|'\n'
string|"'Driver to use for controlling virtualization'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeManager
name|'class'
name|'ComputeManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Manages the running instances from creation to destruction."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'compute_driver'
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
string|'"""Load configuration options and connect to the hypervisor."""'
newline|'\n'
comment|'# TODO(vish): sync driver creation logic with the rest of the system'
nl|'\n'
comment|'#             and redocument the module docstring'
nl|'\n'
name|'if'
name|'not'
name|'compute_driver'
op|':'
newline|'\n'
indent|'            '
name|'compute_driver'
op|'='
name|'FLAGS'
op|'.'
name|'compute_driver'
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
name|'compute_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_manager'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_manager'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ComputeManager'
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
DECL|member|_update_state
dedent|''
name|'def'
name|'_update_state'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the state of an instance from the driver info."""'
newline|'\n'
comment|'# FIXME(ja): include other fields from state?'
nl|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'info'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_info'
op|'('
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'state'
op|'='
name|'info'
op|'['
string|"'state'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'power_state'
op|'.'
name|'NOSTATE'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|refresh_security_group
name|'def'
name|'refresh_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This call passes stright through to the virtualization driver."""'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'refresh_security_group'
op|'('
name|'security_group_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|run_instance
name|'def'
name|'run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Launch a new instance with specified options."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'name'"
op|']'
name|'in'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'list_instances'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Instance has already been created"'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: starting..."'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_manager'
op|'.'
name|'setup_compute_network'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish) check to make sure the availability zone matches'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'spawning'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
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
name|'self'
op|'.'
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
string|"'launched_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable-msg=W0702'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"instance %s: Failed to spawn"'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_update_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|terminate_instance
name|'def'
name|'terminate_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Terminate an instance on this machine."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: terminating"'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'volumes'
op|'='
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'volumes'"
op|','
op|'['
op|']'
op|')'
name|'or'
op|'['
op|']'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'detach_volume'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'instance_ref'
op|'['
string|"'state'"
op|']'
op|'=='
name|'power_state'
op|'.'
name|'SHUTOFF'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'trying to destroy already destroyed'"
nl|'\n'
string|"' instance: %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'.'
name|'destroy'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(ja): should we keep it in a terminated state for a bit?'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|reboot_instance
name|'def'
name|'reboot_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot an instance on this server."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'state'"
op|']'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'trying to reboot a non-running '"
nl|'\n'
string|"'instance: %s (state: %s excepted: %s)'"
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'internal_id'"
op|']'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'state'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: rebooting'"
op|','
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'rebooting'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'reboot'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|rescue_instance
name|'def'
name|'rescue_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rescue an instance on this server."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: rescuing'"
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'internal_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'rescuing'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'rescue'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|unrescue_instance
name|'def'
name|'unrescue_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rescue an instance on this server."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'instance %s: unrescuing'"
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'internal_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
nl|'\n'
string|"'unrescuing'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'unrescue'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_update_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|get_console_output
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send the console output for an instance."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: getting console output"'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
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
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_console_output'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|attach_volume
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'volume_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to an instance."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: attaching volume %s to %s"'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'dev_path'
op|'='
name|'self'
op|'.'
name|'volume_manager'
op|'.'
name|'setup_compute_volume'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'attach_volume'
op|'('
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'dev_path'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0702'
newline|'\n'
comment|'# NOTE(vish): The inline callback eats the exception info so we'
nl|'\n'
comment|'#             log the traceback here and reraise the same'
nl|'\n'
comment|'#             ecxception below.'
nl|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"instance %s: attach failed %s, removing"'
op|','
nl|'\n'
name|'instance_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_manager'
op|'.'
name|'remove_compute_volume'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'raise'
name|'exc'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|detach_volume
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach a volume from an instance."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"instance %s: detaching volume %s"'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'name'"
op|']'
name|'not'
name|'in'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'list_instances'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Detaching volume from unknown instance %s"'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'detach_volume'
op|'('
name|'instance_ref'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'mountpoint'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'volume_manager'
op|'.'
name|'remove_compute_volume'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
