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
op|'.'
name|'compute'
name|'import'
name|'model'
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
name|'self'
op|'.'
name|'instdir'
op|'='
name|'model'
op|'.'
name|'InstanceDirectory'
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
DECL|member|get_instance
dedent|''
name|'def'
name|'get_instance'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
comment|'# inst = self.instdir.get(instance_id)'
nl|'\n'
comment|'# return inst'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'exists'
op|'('
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'Instance'
op|'.'
name|'fromName'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
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
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|describe_instances
name|'def'
name|'describe_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'retval'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'inst'
name|'in'
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'by_node'
op|'('
name|'FLAGS'
op|'.'
name|'node_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'retval'
op|'['
name|'inst'
op|'['
string|"'instance_id'"
op|']'
op|']'
op|'='
op|'('
nl|'\n'
name|'Instance'
op|'.'
name|'fromName'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'inst'
op|'['
string|"'instance_id'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'retval'
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
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# TODO: Get the real security group of launch in here'
nl|'\n'
name|'security_group'
op|'='
string|'"default"'
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
nl|'\n'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'network_type'"
op|','
string|"'vlan'"
op|')'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
name|'security_group'
op|')'
newline|'\n'
nl|'\n'
name|'inst'
op|'['
string|"'node_name'"
op|']'
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
comment|'# TODO(vish) check to make sure the availability zone matches'
nl|'\n'
name|'new_inst'
op|'='
name|'Instance'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'name'
op|'='
name|'instance_id'
op|','
name|'data'
op|'='
name|'inst'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"Instances current state is %s"'
op|','
name|'new_inst'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'if'
name|'new_inst'
op|'.'
name|'is_running'
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
string|'"Instance is already running"'
op|')'
newline|'\n'
dedent|''
name|'new_inst'
op|'.'
name|'spawn'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'get_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# inst = self.instdir.get(instance_id)'
nl|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
nl|'\n'
string|"'trying to terminate unknown instance: %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'='
name|'instance'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
comment|'# d.addCallback(lambda x: inst.destroy())'
nl|'\n'
name|'return'
name|'d'
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
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" reboot an instance on this server\n        KVM doesn\'t support reboot, so we terminate and restart """'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'get_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
nl|'\n'
string|"'trying to reboot unknown instance: %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
op|'.'
name|'reboot'
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
name|'self'
op|'.'
name|'instdir'
op|'.'
name|'get'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'get_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
nl|'\n'
string|"'trying to get console log for unknown: %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'rv'
op|'='
name|'yield'
name|'instance'
op|'.'
name|'console_output'
op|'('
op|')'
newline|'\n'
comment|'# TODO(termie): this stuff belongs in the API layer, no need to'
nl|'\n'
comment|'#               munge the data we send to ourselves'
nl|'\n'
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
name|'rv'
op|')'
op|'}'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'output'
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
nl|'\n'
nl|'\n'
DECL|class|Instance
dedent|''
dedent|''
name|'class'
name|'Instance'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NOSTATE
indent|'    '
name|'NOSTATE'
op|'='
number|'0x00'
newline|'\n'
DECL|variable|RUNNING
name|'RUNNING'
op|'='
number|'0x01'
newline|'\n'
DECL|variable|BLOCKED
name|'BLOCKED'
op|'='
number|'0x02'
newline|'\n'
DECL|variable|PAUSED
name|'PAUSED'
op|'='
number|'0x03'
newline|'\n'
DECL|variable|SHUTDOWN
name|'SHUTDOWN'
op|'='
number|'0x04'
newline|'\n'
DECL|variable|SHUTOFF
name|'SHUTOFF'
op|'='
number|'0x05'
newline|'\n'
DECL|variable|CRASHED
name|'CRASHED'
op|'='
number|'0x06'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|','
name|'name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" spawn an instance with a given name """'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'conn'
newline|'\n'
comment|'# TODO(vish): this can be removed after data has been updated'
nl|'\n'
comment|"# data doesn't seem to have a working iterator so in doesn't work"
nl|'\n'
name|'if'
name|'data'
op|'.'
name|'get'
op|'('
string|"'owner_id'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'data'
op|'['
string|"'owner_id'"
op|']'
newline|'\n'
name|'data'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'data'
op|'['
string|"'owner_id'"
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'datamodel'
op|'='
name|'data'
newline|'\n'
nl|'\n'
name|'size'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|','
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|')'
newline|'\n'
name|'if'
name|'size'
name|'not'
name|'in'
name|'INSTANCE_TYPES'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'invalid instance type: %s'"
op|'%'
name|'size'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'update'
op|'('
name|'INSTANCE_TYPES'
op|'['
name|'size'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'name'"
op|']'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'basepath'"
op|']'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
nl|'\n'
string|"'basepath'"
op|','
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
name|'self'
op|'.'
name|'name'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'memory_kb'"
op|']'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'*'
number|'1024'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'image_id'"
op|','
name|'FLAGS'
op|'.'
name|'default_image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'kernel_id'"
op|','
name|'FLAGS'
op|'.'
name|'default_kernel'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'ramdisk_id'"
op|','
name|'FLAGS'
op|'.'
name|'default_ramdisk'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'project_id'"
op|','
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'bridge_name'"
op|','
name|'None'
op|')'
newline|'\n'
comment|"#self.datamodel.setdefault('key_data', None)"
nl|'\n'
comment|"#self.datamodel.setdefault('key_name', None)"
nl|'\n'
comment|"#self.datamodel.setdefault('addressing_type', None)"
nl|'\n'
nl|'\n'
comment|'# TODO(joshua) - The ugly non-flat ones'
nl|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'groups'"
op|']'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'security_group'"
op|','
string|"'default'"
op|')'
newline|'\n'
comment|'# TODO(joshua): Support product codes somehow'
nl|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'setdefault'
op|'('
string|"'product_codes'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Finished init of Instance with id of %s"'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|fromName
name|'def'
name|'fromName'
op|'('
name|'cls'
op|','
name|'conn'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" use the saved data for reloading the instance """'
newline|'\n'
name|'instdir'
op|'='
name|'model'
op|'.'
name|'InstanceDirectory'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'instdir'
op|'.'
name|'get'
op|'('
name|'name'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'conn'
op|'='
name|'conn'
op|','
name|'name'
op|'='
name|'name'
op|','
name|'data'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_state
dedent|''
name|'def'
name|'set_state'
op|'('
name|'self'
op|','
name|'state_code'
op|','
name|'state_description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'state'"
op|']'
op|'='
name|'state_code'
newline|'\n'
name|'if'
name|'not'
name|'state_description'
op|':'
newline|'\n'
indent|'            '
name|'state_description'
op|'='
name|'power_state'
op|'.'
name|'name'
op|'('
name|'state_code'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'state_description'"
op|']'
op|'='
name|'state_description'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|state
name|'def'
name|'state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# it is a string in datamodel'
nl|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|name
name|'def'
name|'name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|is_pending
dedent|''
name|'def'
name|'is_pending'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'self'
op|'.'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'NOSTATE'
name|'or'
name|'self'
op|'.'
name|'state'
op|'=='
string|"'pending'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_destroyed
dedent|''
name|'def'
name|'is_destroyed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'SHUTOFF'
newline|'\n'
nl|'\n'
DECL|member|is_running
dedent|''
name|'def'
name|'is_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Instance state is: %s"'
op|'%'
name|'self'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
name|'or'
name|'self'
op|'.'
name|'state'
op|'=='
string|"'running'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|describe
dedent|''
name|'def'
name|'describe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'datamodel'
newline|'\n'
nl|'\n'
DECL|member|info
dedent|''
name|'def'
name|'info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'get_info'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'result'
op|'['
string|"'node_name'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'node_name'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|update_state
dedent|''
name|'def'
name|'update_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'info'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_state'
op|'('
name|'self'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'save'
op|'('
op|')'
comment|'# Extra, but harmless'
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
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'is_destroyed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'destroy'
op|'('
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
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
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
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'datamodel'
op|'.'
name|'destroy'
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
DECL|member|reboot
name|'def'
name|'reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_running'
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
nl|'\n'
string|"'trying to reboot a non-running'"
nl|'\n'
string|"'instance: %s (state: %s)'"
op|'%'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'state'
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
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
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
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_state'
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
DECL|member|spawn
name|'def'
name|'spawn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Starting spawn in Instance"'
op|')'
newline|'\n'
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
name|'self'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'update_state'
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
DECL|member|console_output
name|'def'
name|'console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# FIXME: Abstract this for Xen'
nl|'\n'
indent|'        '
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
name|'self'
op|'.'
name|'datamodel'
op|'['
string|"'basepath'"
op|']'
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
name|'console'
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
name|'console'
op|'='
string|"'FAKE CONSOLE OUTPUT'"
newline|'\n'
dedent|''
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
name|'console'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
