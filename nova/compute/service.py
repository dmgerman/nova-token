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
string|'"""\nCompute Service:\n\n    Runs on each compute host, managing the\n    hypervisor using the virt module.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
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
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
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
name|'disk'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'models'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'instance_types'
name|'import'
name|'INSTANCE_TYPES'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'service'
name|'as'
name|'network_service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'image'
comment|'# for image_path flag'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'connection'
name|'as'
name|'virt_connection'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'service'
name|'as'
name|'volume_service'
newline|'\n'
nl|'\n'
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
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'../instances'"
op|')'
op|','
nl|'\n'
string|"'where instances are stored on disk'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeService
name|'class'
name|'ComputeService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Manages the running instances.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" load configuration options for this node and connect to the hypervisor"""'
newline|'\n'
name|'super'
op|'('
name|'ComputeService'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'virt_connection'
op|'.'
name|'get_connection'
op|'('
op|')'
newline|'\n'
comment|'# TODO(joshua): This needs to ensure system state, specifically: modprobe aoe'
nl|'\n'
nl|'\n'
DECL|member|noop
dedent|''
name|'def'
name|'noop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" simple test of an AMQP message call """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
string|"'PONG'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_state
dedent|''
name|'def'
name|'update_state'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# FIXME(ja): include other fields from state?'
nl|'\n'
name|'inst'
op|'.'
name|'state'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'get_info'
op|'('
name|'inst'
op|'.'
name|'name'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|adopt_instances
name|'def'
name|'adopt_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" if there are instances already running, adopt them """'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
number|'0'
op|')'
newline|'\n'
name|'instance_names'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'instance_names'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'new_inst'
op|'='
name|'Instance'
op|'.'
name|'fromName'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'name'
op|')'
newline|'\n'
name|'new_inst'
op|'.'
name|'update_state'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'_instances'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|report_state
name|'def'
name|'report_state'
op|'('
name|'self'
op|','
name|'nodename'
op|','
name|'daemon'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): make this pattern be more elegant. -todd'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'record'
op|'='
name|'model'
op|'.'
name|'Daemon'
op|'('
name|'nodename'
op|','
name|'daemon'
op|')'
newline|'\n'
name|'record'
op|'.'
name|'heartbeat'
op|'('
op|')'
newline|'\n'
name|'if'
name|'getattr'
op|'('
name|'self'
op|','
string|'"model_disconnected"'
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
string|'"Recovered model server connection!"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'model'
op|'.'
name|'ConnectionError'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'self'
op|','
string|'"model_disconnected"'
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"model server went away"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'yield'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" launch a new instance with specified options """'
newline|'\n'
name|'if'
name|'str'
op|'('
name|'instance_id'
op|')'
name|'in'
name|'self'
op|'.'
name|'_conn'
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
string|'"Starting instance %s..."'
op|'%'
op|'('
name|'instance_id'
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# NOTE(vish): passing network type allows us to express the'
nl|'\n'
comment|'#             network without making a call to network to find'
nl|'\n'
comment|'#             out which type of network to setup'
nl|'\n'
name|'network_service'
op|'.'
name|'setup_compute_network'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'node_name'
op|'='
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish) check to make sure the availability zone matches'
nl|'\n'
name|'inst'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
string|"'spawning'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'spawn'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"Failed to spawn instance %s"'
op|'%'
name|'inst'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'update_state'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" terminate an instance on this machine """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Got told to terminate instance %s"'
op|'%'
name|'instance_id'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'inst'
op|'.'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'SHUTOFF'
op|':'
newline|'\n'
comment|'# self.datamodel.destroy() FIXME: RE-ADD ?????'
nl|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'inst'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
string|"'shutting_down'"
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'destroy'
op|'('
name|'inst'
op|')'
newline|'\n'
comment|'# FIXME(ja): should we keep it in a terminated state for a bit?'
nl|'\n'
name|'inst'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" reboot an instance on this server\n        KVM doesn\'t support reboot, so we terminate and restart """'
newline|'\n'
name|'self'
op|'.'
name|'update_state'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(ja): this is only checking the model state - not state on disk?'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'state'
op|'!='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
nl|'\n'
string|"'trying to reboot a non-running'"
nl|'\n'
string|"'instance: %s (state: %s excepted: %s)'"
op|'%'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
name|'instance'
op|'.'
name|'state'
op|','
name|'power_state'
op|'.'
name|'RUNNING'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'rebooting instance %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
string|"'rebooting'"
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_state'
op|'('
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
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" send the console output for an instance """'
newline|'\n'
comment|'# FIXME: Abstract this for Xen'
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Getting console output for %s"'
op|'%'
op|'('
name|'instance_id'
op|')'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'=='
string|"'libvirt'"
op|':'
newline|'\n'
indent|'            '
name|'fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
name|'inst'
op|'.'
name|'name'
op|','
string|"'console.log'"
op|')'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'fname'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"'FAKE CONSOLE OUTPUT'"
newline|'\n'
nl|'\n'
comment|'# TODO(termie): this stuff belongs in the API layer, no need to'
nl|'\n'
comment|'#               munge the data we send to ourselves'
nl|'\n'
dedent|''
name|'output'
op|'='
op|'{'
string|'"InstanceId"'
op|':'
name|'instance_id'
op|','
nl|'\n'
string|'"Timestamp"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"output"'
op|':'
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'output'
op|')'
op|'}'
newline|'\n'
name|'return'
name|'output'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'instance_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'volume_id'
op|'='
name|'None'
op|','
name|'mountpoint'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'volume_service'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_init_aoe'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo virsh attach-disk %s /dev/etherd/%s %s"'
op|'%'
nl|'\n'
op|'('
name|'instance_id'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'aoe_device'"
op|']'
op|','
nl|'\n'
name|'mountpoint'
op|'.'
name|'rpartition'
op|'('
string|"'/dev/'"
op|')'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
name|'volume'
op|'.'
name|'finish_attach'
op|'('
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_init_aoe
name|'def'
name|'_init_aoe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo aoe-discover"'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|'"sudo aoe-stat"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'instance_id'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" detach a volume from an instance """'
newline|'\n'
comment|'# despite the documentation, virsh detach-disk just wants the device'
nl|'\n'
comment|'# name without the leading /dev/'
nl|'\n'
name|'volume'
op|'='
name|'volume_service'
op|'.'
name|'get_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'target'
op|'='
name|'volume'
op|'['
string|"'mountpoint'"
op|']'
op|'.'
name|'rpartition'
op|'('
string|"'/dev/'"
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
nl|'\n'
string|'"sudo virsh detach-disk %s %s "'
op|'%'
op|'('
name|'instance_id'
op|','
name|'target'
op|')'
op|')'
newline|'\n'
name|'volume'
op|'.'
name|'finish_detach'
op|'('
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Group
dedent|''
dedent|''
name|'class'
name|'Group'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'group_id'
op|'='
name|'group_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProductCode
dedent|''
dedent|''
name|'class'
name|'ProductCode'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'product_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'product_code'
op|'='
name|'product_code'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
