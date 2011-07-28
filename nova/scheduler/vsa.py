begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
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
string|'"""\nVSA Simple Scheduler\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'vsa'
op|'.'
name|'api'
name|'import'
name|'VsaState'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'api'
name|'as'
name|'volume_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'simple'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.vsa'"
op|')'
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
name|'DEFINE_integer'
op|'('
string|"'gb_to_bytes_shift'"
op|','
number|'30'
op|','
nl|'\n'
string|"'Conversion shift between GB and bytes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'drive_type_approx_capacity_percent'"
op|','
number|'10'
op|','
nl|'\n'
string|"'The percentage range for capacity comparison'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'vsa_unique_hosts_per_alloc'"
op|','
number|'10'
op|','
nl|'\n'
string|"'The number of unique hosts per storage allocation'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'vsa_select_unique_drives'"
op|','
name|'True'
op|','
nl|'\n'
string|"'Allow selection of same host for multiple drives'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|BYTES_TO_GB
name|'def'
name|'BYTES_TO_GB'
op|'('
name|'bytes'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'bytes'
op|'>>'
name|'FLAGS'
op|'.'
name|'gb_to_bytes_shift'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|GB_TO_BYTES
dedent|''
name|'def'
name|'GB_TO_BYTES'
op|'('
name|'gb'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'gb'
op|'<<'
name|'FLAGS'
op|'.'
name|'gb_to_bytes_shift'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaScheduler
dedent|''
name|'class'
name|'VsaScheduler'
op|'('
name|'simple'
op|'.'
name|'SimpleScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements Scheduler for volume placement."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
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
name|'super'
op|'('
name|'VsaScheduler'
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
name|'self'
op|'.'
name|'_notify_all_volume_hosts'
op|'('
string|'"startup"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_notify_all_volume_hosts
dedent|''
name|'def'
name|'_notify_all_volume_hosts'
op|'('
name|'self'
op|','
name|'event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"notification"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"event"'
op|':'
name|'event'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_qosgrp_match
dedent|''
name|'def'
name|'_qosgrp_match'
op|'('
name|'self'
op|','
name|'drive_type'
op|','
name|'qos_values'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|_compare_names
indent|'        '
name|'def'
name|'_compare_names'
op|'('
name|'str1'
op|','
name|'str2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'str1'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
name|'str2'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|function|_compare_sizes_approxim
dedent|''
name|'def'
name|'_compare_sizes_approxim'
op|'('
name|'cap_capacity'
op|','
name|'size_gb'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cap_capacity'
op|'='
name|'BYTES_TO_GB'
op|'('
name|'int'
op|'('
name|'cap_capacity'
op|')'
op|')'
newline|'\n'
name|'size_gb'
op|'='
name|'int'
op|'('
name|'size_gb'
op|')'
newline|'\n'
name|'size_perc'
op|'='
name|'size_gb'
op|'*'
name|'FLAGS'
op|'.'
name|'drive_type_approx_capacity_percent'
op|'/'
number|'100'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'cap_capacity'
op|'>='
name|'size_gb'
op|'-'
name|'size_perc'
name|'and'
name|'cap_capacity'
op|'<='
name|'size_gb'
op|'+'
name|'size_perc'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
comment|'# Add more entries for additional comparisons'
nl|'\n'
dedent|''
name|'compare_list'
op|'='
op|'['
op|'{'
string|"'cap1'"
op|':'
string|"'DriveType'"
op|','
nl|'\n'
string|"'cap2'"
op|':'
string|"'type'"
op|','
nl|'\n'
string|"'cmp_func'"
op|':'
name|'_compare_names'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'cap1'"
op|':'
string|"'DriveCapacity'"
op|','
nl|'\n'
string|"'cap2'"
op|':'
string|"'size_gb'"
op|','
nl|'\n'
string|"'cmp_func'"
op|':'
name|'_compare_sizes_approxim'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'cap'
name|'in'
name|'compare_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'cap'
op|'['
string|"'cap1'"
op|']'
name|'in'
name|'qos_values'
op|'.'
name|'keys'
op|'('
op|')'
name|'and'
name|'cap'
op|'['
string|"'cap2'"
op|']'
name|'in'
name|'drive_type'
op|'.'
name|'keys'
op|'('
op|')'
name|'and'
name|'cap'
op|'['
string|"'cmp_func'"
op|']'
name|'is'
name|'not'
name|'None'
name|'and'
name|'cap'
op|'['
string|"'cmp_func'"
op|']'
op|'('
name|'qos_values'
op|'['
name|'cap'
op|'['
string|"'cap1'"
op|']'
op|']'
op|','
nl|'\n'
name|'drive_type'
op|'['
name|'cap'
op|'['
string|"'cap2'"
op|']'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_get_service_states
dedent|''
name|'def'
name|'_get_service_states'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'service_states'
newline|'\n'
nl|'\n'
DECL|member|_filter_hosts
dedent|''
name|'def'
name|'_filter_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'host_list'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"_filter_hosts: %(request_spec)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'drive_type'
op|'='
name|'request_spec'
op|'['
string|"'drive_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filter hosts for drive type %s"'
op|')'
op|','
name|'drive_type'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'host_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'host_list'
op|'='
name|'self'
op|'.'
name|'_get_service_states'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'filtered_hosts'
op|'='
op|'['
op|']'
comment|'# returns list of (hostname, capability_dict)'
newline|'\n'
name|'for'
name|'host'
op|','
name|'host_dict'
name|'in'
name|'host_list'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'service_name'
op|','
name|'service_dict'
name|'in'
name|'host_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'service_name'
op|'!='
name|'topic'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'gos_info'
op|'='
name|'service_dict'
op|'.'
name|'get'
op|'('
string|"'drive_qos_info'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'qosgrp'
op|','
name|'qos_values'
name|'in'
name|'gos_info'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'self'
op|'.'
name|'_qosgrp_match'
op|'('
name|'drive_type'
op|','
name|'qos_values'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                            '
name|'filtered_hosts'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'gos_info'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Host %s has no free capacity. Skip"'
op|')'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'host_names'
op|'='
op|'['
name|'item'
op|'['
number|'0'
op|']'
name|'for'
name|'item'
name|'in'
name|'filtered_hosts'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filter hosts: %s"'
op|')'
op|','
name|'host_names'
op|')'
newline|'\n'
name|'return'
name|'filtered_hosts'
newline|'\n'
nl|'\n'
DECL|member|_allowed_to_use_host
dedent|''
name|'def'
name|'_allowed_to_use_host'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'selected_hosts'
op|','
name|'unique'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'unique'
op|'=='
name|'False'
name|'or'
name|'host'
name|'not'
name|'in'
op|'['
name|'item'
op|'['
number|'0'
op|']'
name|'for'
name|'item'
name|'in'
name|'selected_hosts'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_add_hostcap_to_list
dedent|''
dedent|''
name|'def'
name|'_add_hostcap_to_list'
op|'('
name|'self'
op|','
name|'selected_hosts'
op|','
name|'host'
op|','
name|'cap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'host'
name|'not'
name|'in'
op|'['
name|'item'
op|'['
number|'0'
op|']'
name|'for'
name|'item'
name|'in'
name|'selected_hosts'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'selected_hosts'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'cap'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_selection_algorithm
dedent|''
dedent|''
name|'def'
name|'host_selection_algorithm'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'all_hosts'
op|','
nl|'\n'
name|'selected_hosts'
op|','
name|'unique'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override this method for VSA scheduler to work."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"Must implement host selection mechanism"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_select_hosts
dedent|''
name|'def'
name|'_select_hosts'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'all_hosts'
op|','
name|'selected_hosts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'selected_hosts'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'host'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'selected_hosts'
op|')'
op|'>='
name|'FLAGS'
op|'.'
name|'vsa_unique_hosts_per_alloc'
op|':'
newline|'\n'
comment|'# try to select from already selected hosts only'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Maximum number of hosts selected (%d)"'
op|')'
op|','
nl|'\n'
name|'len'
op|'('
name|'selected_hosts'
op|')'
op|')'
newline|'\n'
name|'unique'
op|'='
name|'False'
newline|'\n'
op|'('
name|'host'
op|','
name|'qos_cap'
op|')'
op|'='
name|'self'
op|'.'
name|'host_selection_algorithm'
op|'('
name|'request_spec'
op|','
nl|'\n'
name|'selected_hosts'
op|','
nl|'\n'
name|'selected_hosts'
op|','
nl|'\n'
name|'unique'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Selected excessive host %(host)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'unique'
op|'='
name|'FLAGS'
op|'.'
name|'vsa_select_unique_drives'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|"# if we've not tried yet (# of sel hosts < max) - unique=True"
nl|'\n'
comment|'# or failed to select from selected_hosts - unique=False'
nl|'\n'
comment|'# select from all hosts'
nl|'\n'
indent|'            '
op|'('
name|'host'
op|','
name|'qos_cap'
op|')'
op|'='
name|'self'
op|'.'
name|'host_selection_algorithm'
op|'('
name|'request_spec'
op|','
nl|'\n'
name|'all_hosts'
op|','
nl|'\n'
name|'selected_hosts'
op|','
nl|'\n'
name|'unique'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'driver'
op|'.'
name|'WillNotSchedule'
op|'('
name|'_'
op|'('
string|'"No available hosts"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'host'
op|','
name|'qos_cap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_volume
dedent|''
name|'def'
name|'_provision_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vol'
op|','
name|'vsa_id'
op|','
name|'availability_zone'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'availability_zone'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'availability_zone'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
nl|'\n'
dedent|''
name|'now'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'options'
op|'='
op|'{'
nl|'\n'
string|"'size'"
op|':'
name|'vol'
op|'['
string|"'size'"
op|']'
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
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'status'"
op|':'
string|'"creating"'
op|','
nl|'\n'
string|"'attach_status'"
op|':'
string|'"detached"'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'vol'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'vol'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
string|"'to_vsa_id'"
op|':'
name|'vsa_id'
op|','
nl|'\n'
string|"'drive_type_id'"
op|':'
name|'vol'
op|'['
string|"'drive_ref'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'vol'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'now'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'size'
op|'='
name|'vol'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'host'
op|'='
name|'vol'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'vol'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Provision volume %(name)s of size %(size)s GB on "'
string|'"host %(host)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|','
name|'options'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|'"volume"'
op|','
name|'vol'
op|'['
string|"'host'"
op|']'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'None'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_host_enforcement
dedent|''
name|'def'
name|'_check_host_enforcement'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'availability_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'availability_zone'
nl|'\n'
name|'and'
string|"':'"
name|'in'
name|'availability_zone'
nl|'\n'
name|'and'
name|'context'
op|'.'
name|'is_admin'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'zone'
op|','
name|'_x'
op|','
name|'host'
op|'='
name|'availability_zone'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'service'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'host'
op|','
nl|'\n'
string|"'nova-volume'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'driver'
op|'.'
name|'WillNotSchedule'
op|'('
name|'_'
op|'('
string|'"Host %s not available"'
op|')'
op|'%'
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'host'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_assign_hosts_to_volumes
dedent|''
dedent|''
name|'def'
name|'_assign_hosts_to_volumes'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_params'
op|','
name|'forced_host'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'prev_drive_type_id'
op|'='
name|'None'
newline|'\n'
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume_params %(volume_params)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'i'
op|'='
number|'1'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'volume_params'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'vol'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(i)d: Volume %(name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'i'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'forced_host'
op|':'
newline|'\n'
indent|'                '
name|'vol'
op|'['
string|"'host'"
op|']'
op|'='
name|'forced_host'
newline|'\n'
name|'vol'
op|'['
string|"'capabilities'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'drive_type'
op|'='
name|'vol'
op|'['
string|"'drive_ref'"
op|']'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'size'"
op|':'
name|'vol'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
string|"'drive_type'"
op|':'
name|'dict'
op|'('
name|'drive_type'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'prev_drive_type_id'
op|'!='
name|'drive_type'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
comment|'# generate list of hosts for this drive type'
nl|'\n'
indent|'                '
name|'all_hosts'
op|'='
name|'self'
op|'.'
name|'_filter_hosts'
op|'('
string|'"volume"'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'prev_drive_type_id'
op|'='
name|'drive_type'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'host'
op|','
name|'qos_cap'
op|')'
op|'='
name|'self'
op|'.'
name|'_select_hosts'
op|'('
name|'request_spec'
op|','
nl|'\n'
name|'all_hosts'
op|','
name|'selected_hosts'
op|')'
newline|'\n'
name|'vol'
op|'['
string|"'host'"
op|']'
op|'='
name|'host'
newline|'\n'
name|'vol'
op|'['
string|"'capabilities'"
op|']'
op|'='
name|'qos_cap'
newline|'\n'
name|'self'
op|'.'
name|'_consume_resource'
op|'('
name|'qos_cap'
op|','
name|'vol'
op|'['
string|"'size'"
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_create_volumes
dedent|''
dedent|''
name|'def'
name|'schedule_create_volumes'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'availability_zone'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Picks hosts for hosting multiple volumes."""'
newline|'\n'
nl|'\n'
name|'num_volumes'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_volumes'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attempting to spawn %(num_volumes)d volume(s)"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'vsa_id'"
op|')'
newline|'\n'
name|'volume_params'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'volumes'"
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_check_host_enforcement'
op|'('
name|'context'
op|','
name|'availability_zone'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_assign_hosts_to_volumes'
op|'('
name|'context'
op|','
name|'volume_params'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vol'
name|'in'
name|'volume_params'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_provision_volume'
op|'('
name|'context'
op|','
name|'vol'
op|','
name|'vsa_id'
op|','
name|'availability_zone'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'vsa_id'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'vsa_update'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
name|'VsaState'
op|'.'
name|'FAILED'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'vol'
name|'in'
name|'volume_params'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'capabilities'"
name|'in'
name|'vol'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_consume_resource'
op|'('
name|'vol'
op|'['
string|"'capabilities'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|schedule_create_volume
dedent|''
name|'def'
name|'schedule_create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Picks the best host based on requested drive type capability."""'
newline|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_check_host_enforcement'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'availability_zone'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'now'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'host'
newline|'\n'
nl|'\n'
dedent|''
name|'drive_type'
op|'='
name|'volume_ref'
op|'['
string|"'drive_type'"
op|']'
newline|'\n'
name|'if'
name|'drive_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Non-VSA volume %d"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'super'
op|'('
name|'VsaScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'schedule_create_volume'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
newline|'\n'
dedent|''
name|'drive_type'
op|'='
name|'dict'
op|'('
name|'drive_type'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Spawning volume %(volume_id)s with drive type "'
string|'"%(drive_type)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'size'"
op|':'
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
string|"'drive_type'"
op|':'
name|'drive_type'
op|'}'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'_filter_hosts'
op|'('
string|'"volume"'
op|','
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'host'
op|','
name|'qos_cap'
op|')'
op|'='
name|'self'
op|'.'
name|'_select_hosts'
op|'('
name|'request_spec'
op|','
name|'all_hosts'
op|'='
name|'hosts'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume_ref'
op|'['
string|"'to_vsa_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'db'
op|'.'
name|'vsa_update'
op|'('
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'to_vsa_id'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
name|'VsaState'
op|'.'
name|'FAILED'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
comment|'#return super(VsaScheduler, self).schedule_create_volume(context,'
nl|'\n'
comment|'#            volume_id, *_args, **_kwargs)'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'now'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_consume_resource'
op|'('
name|'qos_cap'
op|','
name|'volume_ref'
op|'['
string|"'size'"
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'return'
name|'host'
newline|'\n'
nl|'\n'
DECL|member|_consume_full_drive
dedent|''
dedent|''
name|'def'
name|'_consume_full_drive'
op|'('
name|'self'
op|','
name|'qos_values'
op|','
name|'direction'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'qos_values'
op|'['
string|"'FullDrive'"
op|']'
op|'['
string|"'NumFreeDrives'"
op|']'
op|'+='
name|'direction'
newline|'\n'
name|'qos_values'
op|'['
string|"'FullDrive'"
op|']'
op|'['
string|"'NumOccupiedDrives'"
op|']'
op|'-='
name|'direction'
newline|'\n'
nl|'\n'
DECL|member|_consume_partition
dedent|''
name|'def'
name|'_consume_partition'
op|'('
name|'self'
op|','
name|'qos_values'
op|','
name|'size'
op|','
name|'direction'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'PartitionSize'"
op|']'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'partition_size'
op|'='
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'PartitionSize'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'partition_size'
op|'='
name|'size'
newline|'\n'
dedent|''
name|'part_per_drive'
op|'='
name|'qos_values'
op|'['
string|"'DriveCapacity'"
op|']'
op|'/'
name|'partition_size'
newline|'\n'
nl|'\n'
name|'if'
name|'direction'
op|'=='
op|'-'
number|'1'
name|'and'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumFreePartitions'"
op|']'
op|'=='
number|'0'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_consume_full_drive'
op|'('
name|'qos_values'
op|','
name|'direction'
op|')'
newline|'\n'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumFreePartitions'"
op|']'
op|'+='
name|'part_per_drive'
newline|'\n'
nl|'\n'
dedent|''
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumFreePartitions'"
op|']'
op|'+='
name|'direction'
newline|'\n'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumOccupiedPartitions'"
op|']'
op|'-='
name|'direction'
newline|'\n'
nl|'\n'
name|'if'
name|'direction'
op|'=='
number|'1'
name|'and'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumFreePartitions'"
op|']'
op|'>='
name|'part_per_drive'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_consume_full_drive'
op|'('
name|'qos_values'
op|','
name|'direction'
op|')'
newline|'\n'
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
string|"'NumFreePartitions'"
op|']'
op|'-='
name|'part_per_drive'
newline|'\n'
nl|'\n'
DECL|member|_consume_resource
dedent|''
dedent|''
name|'def'
name|'_consume_resource'
op|'('
name|'self'
op|','
name|'qos_values'
op|','
name|'size'
op|','
name|'direction'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'qos_values'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"No capability selected for volume of size %(size)s"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'size'
op|'=='
number|'0'
op|':'
comment|'# full drive match'
newline|'\n'
indent|'            '
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
op|'+='
name|'direction'
op|'*'
name|'qos_values'
op|'['
string|"'DriveCapacity'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_consume_full_drive'
op|'('
name|'qos_values'
op|','
name|'direction'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
op|'+='
name|'direction'
op|'*'
name|'GB_TO_BYTES'
op|'('
name|'size'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_consume_partition'
op|'('
name|'qos_values'
op|','
name|'GB_TO_BYTES'
op|'('
name|'size'
op|')'
op|','
name|'direction'
op|')'
newline|'\n'
dedent|''
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaSchedulerLeastUsedHost
dedent|''
dedent|''
name|'class'
name|'VsaSchedulerLeastUsedHost'
op|'('
name|'VsaScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Implements VSA scheduler to select the host with least used capacity\n    of particular type.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
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
name|'super'
op|'('
name|'VsaSchedulerLeastUsedHost'
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
DECL|member|host_selection_algorithm
dedent|''
name|'def'
name|'host_selection_algorithm'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'all_hosts'
op|','
nl|'\n'
name|'selected_hosts'
op|','
name|'unique'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'size'
op|'='
name|'request_spec'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'drive_type'
op|'='
name|'request_spec'
op|'['
string|"'drive_type'"
op|']'
newline|'\n'
name|'best_host'
op|'='
name|'None'
newline|'\n'
name|'best_qoscap'
op|'='
name|'None'
newline|'\n'
name|'best_cap'
op|'='
name|'None'
newline|'\n'
name|'min_used'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'host'
op|','
name|'capabilities'
op|')'
name|'in'
name|'all_hosts'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'has_enough_capacity'
op|'='
name|'False'
newline|'\n'
name|'used_capacity'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'qosgrp'
op|','
name|'qos_values'
name|'in'
name|'capabilities'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'                '
name|'used_capacity'
op|'='
name|'used_capacity'
op|'+'
name|'qos_values'
op|'['
string|"'TotalCapacity'"
op|']'
op|'-'
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_qosgrp_match'
op|'('
name|'drive_type'
op|','
name|'qos_values'
op|')'
op|':'
newline|'\n'
comment|'# we found required qosgroup'
nl|'\n'
nl|'\n'
indent|'                    '
name|'if'
name|'size'
op|'=='
number|'0'
op|':'
comment|'# full drive match'
newline|'\n'
indent|'                        '
name|'if'
name|'qos_values'
op|'['
string|"'FullDrive'"
op|']'
op|'['
string|"'NumFreeDrives'"
op|']'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                            '
name|'has_enough_capacity'
op|'='
name|'True'
newline|'\n'
name|'matched_qos'
op|'='
name|'qos_values'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                            '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
op|'>='
name|'size'
name|'and'
op|'('
name|'qos_values'
op|'['
string|"'PartitionDrive'"
op|']'
op|'['
nl|'\n'
string|"'NumFreePartitions'"
op|']'
op|'>'
number|'0'
name|'or'
name|'qos_values'
op|'['
string|"'FullDrive'"
op|']'
op|'['
string|"'NumFreeDrives'"
op|']'
op|'>'
number|'0'
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'has_enough_capacity'
op|'='
name|'True'
newline|'\n'
name|'matched_qos'
op|'='
name|'qos_values'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                            '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'has_enough_capacity'
name|'and'
name|'self'
op|'.'
name|'_allowed_to_use_host'
op|'('
name|'host'
op|','
nl|'\n'
name|'selected_hosts'
op|','
nl|'\n'
name|'unique'
op|')'
name|'and'
op|'('
name|'best_host'
name|'is'
name|'None'
name|'or'
name|'used_capacity'
op|'<'
name|'min_used'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'                '
name|'min_used'
op|'='
name|'used_capacity'
newline|'\n'
name|'best_host'
op|'='
name|'host'
newline|'\n'
name|'best_qoscap'
op|'='
name|'matched_qos'
newline|'\n'
name|'best_cap'
op|'='
name|'capabilities'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'best_host'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_hostcap_to_list'
op|'('
name|'selected_hosts'
op|','
name|'best_host'
op|','
name|'best_cap'
op|')'
newline|'\n'
name|'min_used'
op|'='
name|'BYTES_TO_GB'
op|'('
name|'min_used'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"\\t LeastUsedHost: Best host: %(best_host)s. "'
string|'"(used capacity %(min_used)s)"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'best_host'
op|','
name|'best_qoscap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaSchedulerMostAvailCapacity
dedent|''
dedent|''
name|'class'
name|'VsaSchedulerMostAvailCapacity'
op|'('
name|'VsaScheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Implements VSA scheduler to select the host with most available capacity\n    of one particular type.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
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
name|'super'
op|'('
name|'VsaSchedulerMostAvailCapacity'
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
DECL|member|host_selection_algorithm
dedent|''
name|'def'
name|'host_selection_algorithm'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'all_hosts'
op|','
nl|'\n'
name|'selected_hosts'
op|','
name|'unique'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'size'
op|'='
name|'request_spec'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'drive_type'
op|'='
name|'request_spec'
op|'['
string|"'drive_type'"
op|']'
newline|'\n'
name|'best_host'
op|'='
name|'None'
newline|'\n'
name|'best_qoscap'
op|'='
name|'None'
newline|'\n'
name|'best_cap'
op|'='
name|'None'
newline|'\n'
name|'max_avail'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'host'
op|','
name|'capabilities'
op|')'
name|'in'
name|'all_hosts'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'qosgrp'
op|','
name|'qos_values'
name|'in'
name|'capabilities'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'.'
name|'_qosgrp_match'
op|'('
name|'drive_type'
op|','
name|'qos_values'
op|')'
op|':'
newline|'\n'
comment|'# we found required qosgroup'
nl|'\n'
nl|'\n'
indent|'                    '
name|'if'
name|'size'
op|'=='
number|'0'
op|':'
comment|'# full drive match'
newline|'\n'
indent|'                        '
name|'available'
op|'='
name|'qos_values'
op|'['
string|"'FullDrive'"
op|']'
op|'['
string|"'NumFreeDrives'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'available'
op|'='
name|'qos_values'
op|'['
string|"'AvailableCapacity'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'available'
op|'>'
name|'max_avail'
name|'and'
name|'self'
op|'.'
name|'_allowed_to_use_host'
op|'('
name|'host'
op|','
nl|'\n'
name|'selected_hosts'
op|','
nl|'\n'
name|'unique'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'max_avail'
op|'='
name|'available'
newline|'\n'
name|'best_host'
op|'='
name|'host'
newline|'\n'
name|'best_qoscap'
op|'='
name|'qos_values'
newline|'\n'
name|'best_cap'
op|'='
name|'capabilities'
newline|'\n'
dedent|''
name|'break'
comment|'# go to the next host'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'best_host'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_hostcap_to_list'
op|'('
name|'selected_hosts'
op|','
name|'best_host'
op|','
name|'best_cap'
op|')'
newline|'\n'
name|'type_str'
op|'='
string|'"drives"'
name|'if'
name|'size'
op|'=='
number|'0'
name|'else'
string|'"bytes"'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"\\t MostAvailCap: Best host: %(best_host)s. "'
string|'"(available %(max_avail)s %(type_str)s)"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'best_host'
op|','
name|'best_qoscap'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
