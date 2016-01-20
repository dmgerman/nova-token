begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may not'
nl|'\n'
comment|'# use this file except in compliance with the License. You may obtain a copy'
nl|'\n'
comment|'# of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'floating_ips'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
op|'.'
name|'openstack_driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
string|"'DEFAULT'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'_network_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'driver'
op|'.'
name|'driver_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'rpcapi'
op|'.'
name|'rpcapi_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
op|'.'
name|'openstack_driver'
op|'.'
name|'security_group_opts'
op|','
nl|'\n'
op|')'
op|')'
nl|'\n'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
