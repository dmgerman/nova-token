begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nClient side of the compute RPC API.\n"""'
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
name|'rpc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
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
nl|'\n'
nl|'\n'
DECL|class|ComputeAPI
name|'class'
name|'ComputeAPI'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the compute rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n    '''"
newline|'\n'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ComputeAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'topic'
op|'='
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'RPC_API_VERSION'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_compute_topic
dedent|''
name|'def'
name|'_compute_topic'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Get the topic to use for a message.\n\n        :param ctxt: request context\n        :param host: explicit host to send the message to.\n        :param instance: If an explicit host was not specified, use\n                         instance['host']\n\n        :returns: A topic string\n        '''"
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'No compute host specified'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|"'Unable to find host for '"
nl|'\n'
string|"'Instance %s'"
op|')'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'topic'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_aggregate_host
dedent|''
name|'def'
name|'add_aggregate_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregate_id'
op|','
name|'host_param'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Add aggregate host.\n\n        :param ctxt: request context\n        :param aggregate_id:\n        :param host_param: This value is placed in the message to be the 'host'\n                           parameter for the remote method.\n        :param host: This is the host to send the message to.\n        '''"
newline|'\n'
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'add_aggregate_host'"
op|','
nl|'\n'
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
name|'host'
op|'='
name|'host_param'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_fixed_ip_to_instance
dedent|''
name|'def'
name|'add_fixed_ip_to_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'add_fixed_ip_to_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'network_id'
op|'='
name|'network_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'volume_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'attach_volume'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|','
nl|'\n'
name|'mountpoint'
op|'='
name|'mountpoint'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|confirm_resize
dedent|''
name|'def'
name|'confirm_resize'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'migration_id'
op|','
name|'host'
op|','
nl|'\n'
name|'cast'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc_method'
op|'='
name|'self'
op|'.'
name|'cast'
name|'if'
name|'cast'
name|'else'
name|'self'
op|'.'
name|'call'
newline|'\n'
name|'return'
name|'rpc_method'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'confirm_resize'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'migration_id'
op|'='
name|'migration_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'detach_volume'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'tail_length'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_console_output'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'tail_length'
op|'='
name|'tail_length'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
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
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_diagnostics'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vnc_console
dedent|''
name|'def'
name|'get_vnc_console'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'console_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'console_type'
op|'='
name|'console_type'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_maintenance_mode
dedent|''
name|'def'
name|'host_maintenance_mode'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host_param'
op|','
name|'mode'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Set host maintenance mode\n\n        :param ctxt: request context\n        :param host_param: This value is placed in the message to be the 'host'\n                           parameter for the remote method.\n        :param mode:\n        :param host: This is the host to send the message to.\n        '''"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'host_maintenance_mode'"
op|','
nl|'\n'
name|'host'
op|'='
name|'host_param'
op|','
name|'mode'
op|'='
name|'mode'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
name|'def'
name|'host_power_action'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'action'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'host_power_action'"
op|','
nl|'\n'
name|'action'
op|'='
name|'action'
op|')'
op|','
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_file
dedent|''
name|'def'
name|'inject_file'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'path'
op|','
name|'file_contents'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'inject_file'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'path'
op|'='
name|'path'
op|','
nl|'\n'
name|'file_contents'
op|'='
name|'file_contents'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_network_info
dedent|''
name|'def'
name|'inject_network_info'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'inject_network_info'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lock_instance
dedent|''
name|'def'
name|'lock_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'lock_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause_instance
dedent|''
name|'def'
name|'pause_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'pause_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_off_instance
dedent|''
name|'def'
name|'power_off_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'power_off_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_on_instance
dedent|''
name|'def'
name|'power_on_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'power_on_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot_instance
dedent|''
name|'def'
name|'reboot_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'reboot_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'reboot_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'reboot_type'
op|'='
name|'reboot_type'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rebuild_instance
dedent|''
name|'def'
name|'rebuild_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'new_pass'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'image_ref'
op|','
name|'orig_image_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'rebuild_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'new_pass'
op|'='
name|'new_pass'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
name|'image_ref'
op|'='
name|'image_ref'
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
name|'orig_image_ref'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'security_group_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'refresh_security_group_rules'"
op|','
nl|'\n'
name|'security_group_id'
op|'='
name|'security_group_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'security_group_id'
op|','
nl|'\n'
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'refresh_security_group_members'"
op|','
nl|'\n'
name|'security_group_id'
op|'='
name|'security_group_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_aggregate_host
dedent|''
name|'def'
name|'remove_aggregate_host'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'aggregate_id'
op|','
name|'host_param'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Remove aggregate host.\n\n        :param ctxt: request context\n        :param aggregate_id:\n        :param host_param: This value is placed in the message to be the 'host'\n                           parameter for the remote method.\n        :param host: This is the host to send the message to.\n        '''"
newline|'\n'
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'remove_aggregate_host'"
op|','
nl|'\n'
name|'aggregate_id'
op|'='
name|'aggregate_id'
op|','
name|'host'
op|'='
name|'host_param'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'remove_fixed_ip_from_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'remove_fixed_ip_from_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'address'
op|'='
name|'address'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rescue_instance
dedent|''
name|'def'
name|'rescue_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'rescue_password'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'rescue_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'rescue_password'
op|'='
name|'rescue_password'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_network
dedent|''
name|'def'
name|'reset_network'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'reset_network'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume_instance
dedent|''
name|'def'
name|'resume_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'resume_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|revert_resize
dedent|''
name|'def'
name|'revert_resize'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'migration_id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'revert_resize'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'migration_id'
op|'='
name|'migration_id'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'set_admin_password'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'new_pass'
op|'='
name|'new_pass'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_host_enabled
dedent|''
name|'def'
name|'set_host_enabled'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'enabled'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'set_host_enabled'"
op|','
nl|'\n'
name|'enabled'
op|'='
name|'enabled'
op|')'
op|','
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'host'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot_instance
dedent|''
name|'def'
name|'snapshot_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'image_type'
op|','
nl|'\n'
name|'backup_type'
op|','
name|'rotation'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'snapshot_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'image_id'
op|'='
name|'image_id'
op|','
nl|'\n'
name|'image_type'
op|'='
name|'image_type'
op|','
name|'backup_type'
op|'='
name|'backup_type'
op|','
nl|'\n'
name|'rotation'
op|'='
name|'rotation'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_instance
dedent|''
name|'def'
name|'start_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'start_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_instance
dedent|''
name|'def'
name|'stop_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'cast'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc_method'
op|'='
name|'self'
op|'.'
name|'cast'
name|'if'
name|'cast'
name|'else'
name|'self'
op|'.'
name|'call'
newline|'\n'
name|'return'
name|'rpc_method'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'stop_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend_instance
dedent|''
name|'def'
name|'suspend_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'suspend_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|terminate_instance
dedent|''
name|'def'
name|'terminate_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'terminate_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unlock_instance
dedent|''
name|'def'
name|'unlock_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'unlock_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause_instance
dedent|''
name|'def'
name|'unpause_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'unpause_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unrescue_instance
dedent|''
name|'def'
name|'unrescue_instance'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'unrescue_instance'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_compute_topic'
op|'('
name|'ctxt'
op|','
name|'None'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
