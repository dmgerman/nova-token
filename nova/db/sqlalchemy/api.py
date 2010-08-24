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
name|'import'
name|'math'
newline|'\n'
nl|'\n'
name|'import'
name|'IPy'
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
name|'models'
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
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_get
name|'def'
name|'daemon_get'
op|'('
name|'context'
op|','
name|'daemon_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Daemon'
op|'.'
name|'find'
op|'('
name|'daemon_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_get_by_args
dedent|''
name|'def'
name|'daemon_get_by_args'
op|'('
name|'context'
op|','
name|'node_name'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Daemon'
op|'.'
name|'find_by_args'
op|'('
name|'node_name'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_create
dedent|''
name|'def'
name|'daemon_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'daemon_ref'
op|'='
name|'models'
op|'.'
name|'Daemon'
op|'('
op|'**'
name|'values'
op|')'
newline|'\n'
name|'daemon_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'daemon_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_update
dedent|''
name|'def'
name|'daemon_update'
op|'('
name|'context'
op|','
name|'daemon_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'daemon_ref'
op|'='
name|'daemon_get'
op|'('
name|'context'
op|','
name|'daemon_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'daemon_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'daemon_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_allocate_address
dedent|''
name|'def'
name|'floating_ip_allocate_address'
op|'('
name|'context'
op|','
name|'node_name'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'FloatingIp'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'node_name'
op|'='
name|'node_name'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'fixed_ip_id'
op|'='
name|'None'
op|')'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
newline|'\n'
name|'floating_ip_ref'
op|'='
name|'query'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
comment|"# NOTE(vish): if with_lockmode isn't supported, as in sqlite,"
nl|'\n'
comment|'#             then this has concurrency issues'
nl|'\n'
name|'if'
name|'not'
name|'floating_ip_ref'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'floating_ip_ref'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'floating_ip_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'floating_ip_ref'
op|'['
string|"'ip_str'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_fixed_ip_associate
dedent|''
name|'def'
name|'floating_ip_fixed_ip_associate'
op|'('
name|'context'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'floating_ip_ref'
op|'='
name|'models'
op|'.'
name|'FloatingIp'
op|'.'
name|'find_by_ip_str'
op|'('
name|'floating_address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'models'
op|'.'
name|'FixedIp'
op|'.'
name|'find_by_ip_str'
op|'('
name|'fixed_address'
op|')'
newline|'\n'
name|'floating_ip_ref'
op|'.'
name|'fixed_ip'
op|'='
name|'fixed_ip_ref'
newline|'\n'
name|'floating_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|floating_ip_disassociate
dedent|''
name|'def'
name|'floating_ip_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'floating_ip_ref'
op|'='
name|'models'
op|'.'
name|'FloatingIp'
op|'.'
name|'find_by_ip_str'
op|'('
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_address'
op|'='
name|'floating_ip_ref'
op|'.'
name|'fixed_ip'
op|'['
string|"'ip_str'"
op|']'
newline|'\n'
name|'floating_ip_ref'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'floating_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'fixed_ip_address'
newline|'\n'
nl|'\n'
DECL|function|floating_ip_deallocate
dedent|''
name|'def'
name|'floating_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'floating_ip_ref'
op|'='
name|'models'
op|'.'
name|'FloatingIp'
op|'.'
name|'find_by_ip_str'
op|'('
name|'address'
op|')'
newline|'\n'
name|'floating_ip_ref'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'floating_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_allocate
dedent|''
name|'def'
name|'fixed_ip_allocate'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'FixedIp'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'network_id'
op|'='
name|'network_id'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'reserved'
op|'='
name|'False'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'allocated'
op|'='
name|'False'
op|')'
newline|'\n'
name|'query'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'leased'
op|'='
name|'False'
op|')'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'='
name|'query'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
comment|"# NOTE(vish): if with_lockmode isn't supported, as in sqlite,"
nl|'\n'
comment|'#             then this has concurrency issues'
nl|'\n'
name|'if'
name|'not'
name|'fixed_ip_ref'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'NoMoreAddresses'
op|'('
op|')'
newline|'\n'
dedent|''
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'fixed_ip_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'fixed_ip_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_get_by_address
dedent|''
name|'def'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'FixedIp'
op|'.'
name|'find_by_ip_str'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_lease
dedent|''
name|'def'
name|'fixed_ip_lease'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip_ref'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'AddressNotAllocated'
op|'('
name|'address'
op|')'
newline|'\n'
dedent|''
name|'fixed_ip_ref'
op|'['
string|"'leased'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_release
dedent|''
name|'def'
name|'fixed_ip_release'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip_ref'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'fixed_ip_ref'
op|'['
string|"'leased'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_deallocate
dedent|''
name|'def'
name|'fixed_ip_deallocate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip_ref'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'['
string|"'allocated'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_instance_associate
dedent|''
name|'def'
name|'fixed_ip_instance_associate'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip_ref'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'instance'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fixed_ip_instance_disassociate
dedent|''
name|'def'
name|'fixed_ip_instance_disassociate'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixed_ip_ref'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'instance'
op|'='
name|'None'
newline|'\n'
name|'fixed_ip_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_create
dedent|''
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'models'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'key'
newline|'\n'
name|'instance_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'instance_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
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
nl|'\n'
DECL|function|instance_get_all
dedent|''
name|'def'
name|'instance_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_name
dedent|''
name|'def'
name|'instance_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(vish): remove the 'i-'"
nl|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Instance'
op|'.'
name|'find'
op|'('
name|'name'
op|'['
number|'2'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_project
dedent|''
name|'def'
name|'instance_get_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'Instance'
op|')'
newline|'\n'
name|'results'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'results'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_by_reservation
dedent|''
name|'def'
name|'instance_get_by_reservation'
op|'('
name|'context'
op|','
name|'reservation_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'Instance'
op|')'
newline|'\n'
name|'results'
op|'='
name|'query'
op|'.'
name|'filter_by'
op|'('
name|'reservation_id'
op|'='
name|'reservation_id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'results'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get_host
dedent|''
name|'def'
name|'instance_get_host'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|'['
string|"'node_name'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_is_vpn
dedent|''
name|'def'
name|'instance_is_vpn'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|'['
string|"'image_id'"
op|']'
op|'=='
name|'FLAGS'
op|'.'
name|'vpn_image_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_state
dedent|''
name|'def'
name|'instance_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ref'
op|'.'
name|'set_state'
op|'('
name|'state'
op|','
name|'description'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'instance_ref'
op|'='
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'instance_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(vish): is there a better place for this logic?'
nl|'\n'
DECL|function|network_allocate
dedent|''
name|'def'
name|'network_allocate'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set up the network"""'
newline|'\n'
name|'db'
op|'.'
name|'network_ensure_indexes'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'num_networks'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_create'
op|'('
name|'context'
op|','
op|'{'
string|"'project_id'"
op|':'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'network_id'
op|'='
name|'network_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'private_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'FLAGS'
op|'.'
name|'private_range'
op|')'
newline|'\n'
name|'index'
op|'='
name|'db'
op|'.'
name|'network_get_index'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'vlan'
op|'='
name|'FLAGS'
op|'.'
name|'vlan_start'
op|'+'
name|'index'
newline|'\n'
name|'start'
op|'='
name|'index'
op|'*'
name|'FLAGS'
op|'.'
name|'network_size'
newline|'\n'
name|'significant_bits'
op|'='
number|'32'
op|'-'
name|'int'
op|'('
name|'math'
op|'.'
name|'log'
op|'('
name|'FLAGS'
op|'.'
name|'network_size'
op|','
number|'2'
op|')'
op|')'
newline|'\n'
name|'cidr'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'private_net'
op|'['
name|'start'
op|']'
op|','
name|'significant_bits'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_set_cidr'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'cidr'
op|')'
newline|'\n'
name|'net'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'net'
op|'['
string|"'kind'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'network_type'
newline|'\n'
name|'net'
op|'['
string|"'vlan'"
op|']'
op|'='
name|'vlan'
newline|'\n'
name|'net'
op|'['
string|"'bridge'"
op|']'
op|'='
string|"'br%s'"
op|'%'
name|'vlan'
newline|'\n'
name|'net'
op|'['
string|"'vpn_public_ip_str'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_ip'
newline|'\n'
name|'net'
op|'['
string|"'vpn_public_port'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'vpn_start'
op|'+'
name|'index'
newline|'\n'
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'net'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'FLAGS'
op|'.'
name|'cnt_vpn_clients'
op|')'
newline|'\n'
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create
dedent|''
name|'def'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'models'
op|'.'
name|'Network'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'network_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create_fixed_ips
dedent|''
name|'def'
name|'network_create_fixed_ips'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'num_vpn_clients'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
comment|'# NOTE(vish): should these be properties of the network as opposed'
nl|'\n'
comment|'#             to constants?'
nl|'\n'
name|'BOTTOM_RESERVED'
op|'='
number|'3'
newline|'\n'
name|'TOP_RESERVED'
op|'='
number|'1'
op|'+'
name|'num_vpn_clients'
newline|'\n'
name|'project_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'network_ref'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'num_ips'
op|'='
name|'len'
op|'('
name|'project_net'
op|')'
newline|'\n'
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_ips'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ip'
op|'='
name|'models'
op|'.'
name|'FixedIp'
op|'('
op|')'
newline|'\n'
name|'fixed_ip'
op|'.'
name|'ip_str'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
name|'if'
name|'i'
op|'<'
name|'BOTTOM_RESERVED'
name|'or'
name|'num_ips'
op|'-'
name|'i'
op|'<'
name|'TOP_RESERVED'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'['
string|"'reserved'"
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'fixed_ip'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_ensure_indexes
dedent|''
name|'def'
name|'network_ensure_indexes'
op|'('
name|'context'
op|','
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'models'
op|'.'
name|'NetworkIndex'
op|'.'
name|'count'
op|'('
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_index'
op|'='
name|'models'
op|'.'
name|'NetworkIndex'
op|'('
op|')'
newline|'\n'
name|'network_index'
op|'.'
name|'index'
op|'='
name|'i'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'network_index'
op|')'
newline|'\n'
dedent|''
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_destroy
dedent|''
dedent|''
name|'def'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'network_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get
dedent|''
name|'def'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Network'
op|'.'
name|'find'
op|'('
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_vpn_ip
dedent|''
name|'def'
name|'network_get_vpn_ip'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): possible concurrency issue here'
nl|'\n'
indent|'    '
name|'network'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'address'
op|'='
name|'network'
op|'['
string|"'vpn_private_ip_str'"
op|']'
newline|'\n'
name|'fixed_ip'
op|'='
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'fixed_ip'
op|'['
string|"'allocated'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'AddressAlreadyAllocated'
op|'('
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'context'
op|','
name|'fixed_ip'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'fixed_ip'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_host
dedent|''
name|'def'
name|'network_get_host'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'return'
name|'network_ref'
op|'['
string|"'node_name'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get_index
dedent|''
name|'def'
name|'network_get_index'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'NetworkIndex'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'network_id'
op|'='
name|'None'
op|')'
newline|'\n'
name|'network_index'
op|'='
name|'query'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'network_index'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'NoMoreNetworks'
op|'('
op|')'
newline|'\n'
dedent|''
name|'network_index'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'network_index'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network_index'
op|'['
string|"'index'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_set_cidr
dedent|''
name|'def'
name|'network_set_cidr'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'project_net'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'network_ref'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
comment|'# FIXME we can turn these into properties'
nl|'\n'
name|'network_ref'
op|'['
string|"'netmask'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'netmask'
op|'('
op|')'
op|')'
newline|'\n'
name|'network_ref'
op|'['
string|"'gateway'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'network_ref'
op|'['
string|"'broadcast'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'.'
name|'broadcast'
op|'('
op|')'
op|')'
newline|'\n'
name|'network_ref'
op|'['
string|"'vpn_private_ip_str'"
op|']'
op|'='
name|'str'
op|'('
name|'project_net'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_set_host
dedent|''
name|'def'
name|'network_set_host'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'host_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
comment|'# FIXME will a second request fail or wait for first to finish?'
nl|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'Network'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'id'
op|'='
name|'network_id'
op|')'
newline|'\n'
name|'network'
op|'='
name|'query'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'network'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|'"Couldn\'t find network with %s"'
op|'%'
nl|'\n'
name|'network_id'
op|')'
newline|'\n'
comment|"# NOTE(vish): if with_lockmode isn't supported, as in sqlite,"
nl|'\n'
comment|'#             then this has concurrency issues'
nl|'\n'
dedent|''
name|'if'
name|'network'
op|'.'
name|'node_name'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network'
op|'['
string|"'node_name'"
op|']'
newline|'\n'
dedent|''
name|'network'
op|'['
string|"'node_name'"
op|']'
op|'='
name|'host_id'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'network'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
name|'network'
op|'['
string|"'node_name'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_update
dedent|''
name|'def'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'network_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|project_get_network
dedent|''
name|'def'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'create_session'
op|'('
op|')'
newline|'\n'
name|'rv'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'Network'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'rv'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'No network for project: %s'"
op|'%'
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'physical_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'topic'
op|','
name|'physical_node_id'
op|')'
comment|'# FIXME(ja): this should be servername?'
newline|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_allocate_shelf_and_blade
dedent|''
name|'def'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'session'
op|'='
name|'models'
op|'.'
name|'NovaBase'
op|'.'
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'query'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'ExportDevice'
op|')'
op|'.'
name|'filter_by'
op|'('
name|'volume'
op|'='
name|'None'
op|')'
newline|'\n'
name|'export_device'
op|'='
name|'query'
op|'.'
name|'with_lockmode'
op|'('
string|'"update"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
comment|"# NOTE(vish): if with_lockmode isn't supported, as in sqlite,"
nl|'\n'
comment|'#             then this has concurrency issues'
nl|'\n'
name|'if'
name|'not'
name|'export_device'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'db'
op|'.'
name|'NoMoreBlades'
op|'('
op|')'
newline|'\n'
dedent|''
name|'export_device'
op|'.'
name|'volume_id'
op|'='
name|'volume_id'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'export_device'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
name|'return'
op|'('
name|'export_device'
op|'.'
name|'shelf_id'
op|','
name|'export_device'
op|'.'
name|'blade_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_attached
dedent|''
name|'def'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'.'
name|'instance_id'
op|'='
name|'instance_id'
newline|'\n'
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in-use'"
newline|'\n'
name|'volume_ref'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'mountpoint'
newline|'\n'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'attached'"
newline|'\n'
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_create
dedent|''
name|'def'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'models'
op|'.'
name|'Volume'
op|'('
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'return'
name|'volume_ref'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_destroy
dedent|''
name|'def'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_detached
dedent|''
name|'def'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ref'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'volume_ref'
op|'['
string|"'mountpoint'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'volume_ref'
op|'['
string|"'status'"
op|']'
op|'='
string|"'available'"
newline|'\n'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|"'detached'"
newline|'\n'
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get
dedent|''
name|'def'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'models'
op|'.'
name|'Volume'
op|'.'
name|'find'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_shelf_and_blade
dedent|''
name|'def'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'export_device'
op|'='
name|'volume_ref'
op|'.'
name|'export_device'
newline|'\n'
name|'if'
name|'not'
name|'export_device'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'export_device'
op|'.'
name|'shelf_id'
op|','
name|'export_device'
op|'.'
name|'blade_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_update
dedent|''
name|'def'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume_ref'
op|'='
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'values'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ref'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'volume_ref'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
