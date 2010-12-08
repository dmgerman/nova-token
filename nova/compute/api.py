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
string|'"""\nHandles all API requests relating to instances (guest vms).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'time'
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
name|'import'
name|'quota'
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
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_default_hostname
name|'def'
name|'generate_default_hostname'
op|'('
name|'internal_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Default function to generate a hostname given an instance reference."""'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'internal_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeAPI
dedent|''
name|'class'
name|'ComputeAPI'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the compute manager."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'super'
op|'('
name|'ComputeAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(eday): network_topic arg should go away once we push network'
nl|'\n'
comment|'# allocation into the scheduler or compute worker.'
nl|'\n'
DECL|member|create_instances
dedent|''
name|'def'
name|'create_instances'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_type'
op|','
name|'image_service'
op|','
name|'image_id'
op|','
nl|'\n'
name|'network_topic'
op|','
name|'min_count'
op|'='
number|'1'
op|','
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'kernel_id'
op|'='
name|'None'
op|','
name|'ramdisk_id'
op|'='
name|'None'
op|','
name|'name'
op|'='
string|"''"
op|','
nl|'\n'
name|'description'
op|'='
string|"''"
op|','
name|'user_data'
op|'='
string|"''"
op|','
name|'key_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'key_data'
op|'='
name|'None'
op|','
name|'security_group'
op|'='
string|"'default'"
op|','
nl|'\n'
name|'generate_hostname'
op|'='
name|'generate_default_hostname'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the number of instances requested if quote and\n        other arguments check out ok."""'
newline|'\n'
nl|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'context'
op|','
name|'max_count'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
name|'if'
name|'num_instances'
op|'<'
name|'min_count'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Quota exceeeded for %s, tried to run %s instances"'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|','
name|'min_count'
op|')'
newline|'\n'
name|'raise'
name|'quota'
op|'.'
name|'QuotaError'
op|'('
string|'"Instance quota exceeded. You can only "'
nl|'\n'
string|'"run %s more instances of this type."'
op|'%'
nl|'\n'
name|'num_instances'
op|','
string|'"InstanceLimitExceeded"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'is_vpn'
op|'='
name|'image_id'
op|'=='
name|'FLAGS'
op|'.'
name|'vpn_image_id'
newline|'\n'
name|'if'
name|'not'
name|'is_vpn'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'kernel_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'kernel_id'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'kernelId'"
op|','
name|'FLAGS'
op|'.'
name|'default_kernel'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'ramdisk_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ramdisk_id'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'ramdiskId'"
op|','
name|'FLAGS'
op|'.'
name|'default_ramdisk'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure we have access to kernel and ramdisk'
nl|'\n'
dedent|''
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'kernel_id'
op|')'
newline|'\n'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'ramdisk_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'security_group'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'security_group'
op|'='
op|'['
string|"'default'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'type'
op|'('
name|'security_group'
op|')'
name|'is'
name|'list'
op|':'
newline|'\n'
indent|'            '
name|'security_group'
op|'='
op|'['
name|'security_group'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'security_groups'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'ensure_default_security_group'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'security_group_name'
name|'in'
name|'security_group'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'security_group_name'
op|')'
newline|'\n'
name|'security_groups'
op|'.'
name|'append'
op|'('
name|'group'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'key_data'
name|'is'
name|'None'
name|'and'
name|'key_name'
op|':'
newline|'\n'
indent|'            '
name|'key_pair'
op|'='
name|'db'
op|'.'
name|'key_pair_get'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'key_name'
op|')'
newline|'\n'
name|'key_data'
op|'='
name|'key_pair'
op|'['
string|"'public_key'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'type_data'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'instance_type'
op|']'
newline|'\n'
name|'base_options'
op|'='
op|'{'
nl|'\n'
string|"'reservation_id'"
op|':'
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'kernel_id'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'ramdisk_id'
op|','
nl|'\n'
string|"'state_description'"
op|':'
string|"'scheduling'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'launch_time'"
op|':'
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'type_data'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'key_name'"
op|':'
name|'key_name'
op|','
nl|'\n'
string|"'key_data'"
op|':'
name|'key_data'
op|'}'
newline|'\n'
nl|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Going to run %s instances..."'
op|','
name|'num_instances'
op|')'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'dict'
op|'('
name|'mac_address'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|','
nl|'\n'
name|'launch_index'
op|'='
name|'num'
op|','
nl|'\n'
op|'**'
name|'base_options'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'create_instance'
op|'('
name|'context'
op|','
name|'security_groups'
op|','
nl|'\n'
op|'**'
name|'instance'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'internal_id'
op|'='
name|'instance_ref'
op|'['
string|"'internal_id'"
op|']'
newline|'\n'
name|'hostname'
op|'='
name|'generate_hostname'
op|'('
name|'internal_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'hostname'
op|'='
name|'hostname'
op|')'
newline|'\n'
name|'instances'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'id'
op|'='
name|'instance_id'
op|','
name|'internal_id'
op|'='
name|'internal_id'
op|','
nl|'\n'
name|'hostname'
op|'='
name|'hostname'
op|','
op|'**'
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): This probably should be done in the scheduler'
nl|'\n'
comment|'#             or in compute as a call.  The network should be'
nl|'\n'
comment|'#             allocated after the host is assigned and setup'
nl|'\n'
comment|'#             can happen at the same time.'
nl|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'network_manager'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'is_vpn'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'elevated'
op|','
nl|'\n'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"setup_fixed_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"address"'
op|':'
name|'address'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Casting to scheduler for %s/%s\'s instance %s"'
op|'%'
nl|'\n'
op|'('
name|'context'
op|'.'
name|'project_id'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'instance_id'
op|')'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'scheduler_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"topic"'
op|':'
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
string|'"instance_id"'
op|':'
name|'instance_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'instances'
newline|'\n'
nl|'\n'
DECL|member|ensure_default_security_group
dedent|''
name|'def'
name|'ensure_default_security_group'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'default'"
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
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
name|'group'
op|'='
name|'db'
op|'.'
name|'security_group_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_instance
dedent|''
dedent|''
name|'def'
name|'create_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_groups'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates the instance in the datastore and returns the\n        new instance as a mapping\n\n        :param context: The security context\n        :param security_groups: list of security group ids to\n                                attach to the instance\n        :param kwargs: All additional keyword args are treated\n                       as data fields of the instance to be\n                       created\n\n        :retval Returns a mapping of the instance information\n                that has just been created\n\n        """'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
comment|'# Set sane defaults if not specified'
nl|'\n'
name|'if'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'display_name'"
op|')'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'display_name'
op|'='
string|'"Server %s"'
op|'%'
name|'instance_ref'
op|'['
string|"'internal_id'"
op|']'
newline|'\n'
name|'instance_ref'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'display_name'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'inst_id'
op|','
nl|'\n'
op|'{'
string|"'display_name'"
op|':'
name|'display_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'security_groups'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'for'
name|'security_group_id'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_add_security_group'
op|'('
name|'elevated'
op|','
nl|'\n'
name|'inst_id'
op|','
nl|'\n'
name|'security_group_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_ref'
newline|'\n'
nl|'\n'
DECL|member|update_instance
dedent|''
name|'def'
name|'update_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates the instance in the datastore.\n\n        :param context: The security context\n        :param instance_id: ID of the instance to update\n        :param kwargs: All additional keyword args are treated\n                       as data fields of the instance to be\n                       updated\n\n        :retval None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
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
string|'"""Reboot the given instance."""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"reboot_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rescue
dedent|''
name|'def'
name|'rescue'
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
string|'"""Rescue the given instance."""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"rescue_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unrescue
dedent|''
name|'def'
name|'unrescue'
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
string|'"""Unrescue the given instance."""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"unrescue_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
