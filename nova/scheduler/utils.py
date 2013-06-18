begin_unit
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
string|'"""Utility methods for scheduling."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_request_spec
name|'def'
name|'build_request_spec'
op|'('
name|'image'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build a request_spec for the scheduler.\n\n    The request_spec assumes that all instances to be scheduled are the same\n    type.\n    """'
newline|'\n'
name|'instance'
op|'='
name|'instances'
op|'['
number|'0'
op|']'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'image'"
op|':'
name|'image'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
op|','
nl|'\n'
string|"'instance_uuids'"
op|':'
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
name|'instances'
op|']'
op|'}'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'request_spec'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
