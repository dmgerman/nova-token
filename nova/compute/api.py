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
name|'datetime'
newline|'\n'
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
name|'network_manager'
op|'='
name|'None'
op|','
name|'image_service'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'network_manager'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
name|'self'
op|'.'
name|'network_manager'
op|'='
name|'network_manager'
newline|'\n'
name|'if'
name|'not'
name|'image_service'
op|':'
newline|'\n'
indent|'            '
name|'image_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'image_service'
op|'='
name|'image_service'
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
DECL|member|get_network_topic
dedent|''
name|'def'
name|'get_network_topic'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warning'
op|'('
string|'"Instance %d was not found in get_network_topic"'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"Instance %d has no host"'
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'topic'
op|'='
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
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"get_network_topic"'
op|','
string|'"args"'
op|':'
op|'{'
string|"'fake'"
op|':'
number|'1'
op|'}'
op|'}'
op|')'
newline|'\n'
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
name|'image_id'
op|','
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
name|'kernel_id'
op|'='
name|'None'
op|','
name|'ramdisk_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"''"
op|','
name|'description'
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
name|'user_data'
op|'='
name|'None'
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
name|'self'
op|'.'
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
name|'None'
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
name|'None'
op|')'
newline|'\n'
comment|'#No kernel and ramdisk for raw images'
nl|'\n'
dedent|''
name|'if'
name|'kernel_id'
op|'=='
name|'str'
op|'('
name|'FLAGS'
op|'.'
name|'null_kernel'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'kernel_id'
op|'='
name|'None'
newline|'\n'
name|'ramdisk_id'
op|'='
name|'None'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Creating a raw instance"'
op|')'
newline|'\n'
comment|'# Make sure we have access to kernel and ramdisk (if not raw)'
nl|'\n'
dedent|''
name|'if'
name|'kernel_id'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'kernel_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
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
name|'or'
string|"''"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'ramdisk_id'
name|'or'
string|"''"
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
name|'display_name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'description'
op|','
nl|'\n'
string|"'user_data'"
op|':'
name|'user_data'
name|'or'
string|"''"
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
name|'_'
op|'('
string|'"Going to run %s instances..."'
op|')'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'internal_id'
op|'='
name|'instance'
op|'['
string|"'internal_id'"
op|']'
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
name|'if'
name|'not'
name|'security_groups'
op|':'
newline|'\n'
indent|'                '
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
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_add_security_group'
op|'('
name|'elevated'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'security_group_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set sane defaults if not specified'
nl|'\n'
dedent|''
name|'updates'
op|'='
name|'dict'
op|'('
name|'hostname'
op|'='
name|'generate_hostname'
op|'('
name|'internal_id'
op|')'
op|')'
newline|'\n'
name|'if'
string|"'display_name'"
name|'not'
name|'in'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'updates'
op|'['
string|"'display_name'"
op|']'
op|'='
string|'"Server %s"'
op|'%'
name|'internal_id'
newline|'\n'
nl|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'update_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
op|'**'
name|'updates'
op|')'
newline|'\n'
name|'instances'
op|'.'
name|'append'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Casting to scheduler for %s/%s\'s instance %s"'
op|')'
op|','
nl|'\n'
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
string|'""" Create security group for the security context if it\n        does not already exist\n\n        :param context: the security context\n\n        """'
newline|'\n'
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
DECL|member|update_instance
dedent|''
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
name|'return'
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
DECL|member|delete_instance
dedent|''
name|'def'
name|'delete_instance'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Going to try and terminate %d"'
op|'%'
name|'instance_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Instance %d was not found during terminate"'
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'instance'
op|'['
string|"'state_description'"
op|']'
op|'=='
string|"'terminating'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Instance %d is already being terminated"'
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'update_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'state_description'
op|'='
string|"'terminating'"
op|','
nl|'\n'
name|'state'
op|'='
number|'0'
op|','
nl|'\n'
name|'terminated_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
string|"'terminate %s %s %s %s'"
op|','
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|','
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
op|')'
newline|'\n'
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'            '
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
string|'"terminate_instance"'
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
name|'else'
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
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instances
dedent|''
dedent|''
name|'def'
name|'get_instances'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get all instances, possibly filtered by project ID or\n        user ID. If there is no filter and the context is an admin,\n        it will retreive all instances in the system."""'
newline|'\n'
name|'if'
name|'project_id'
name|'or'
name|'not'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'context'
op|'.'
name|'project'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_user'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'project_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
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
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
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
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Snapshot the given instance."""'
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
string|'"snapshot_instance"'
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
op|','
string|'"name"'
op|':'
name|'name'
op|'}'
op|'}'
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
DECL|member|pause
dedent|''
name|'def'
name|'pause'
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
string|'"""Pause the given instance."""'
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
string|'"pause_instance"'
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
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
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
string|'"""Unpause the given instance."""'
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
string|'"unpause_instance"'
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
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
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
string|'"""Retrieve diagnostics for the given instance."""'
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
string|'"host"'
op|']'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
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
string|'"get_diagnostics"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance'
op|'['
string|'"id"'
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
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
string|'"""Retrieve actions for the given instance."""'
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
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_actions'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
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
string|'"""suspend the instance with instance_id"""'
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
string|'"suspend_instance"'
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
DECL|member|resume
dedent|''
name|'def'
name|'resume'
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
string|'"""resume the instance with instance_id"""'
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
string|'"resume_instance"'
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
