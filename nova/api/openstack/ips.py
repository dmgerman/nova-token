begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'common'
op|'.'
name|'OpenstackController'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The servers addresses API controller for the Openstack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
op|'{'
nl|'\n'
string|"'list_collections'"
op|':'
op|'{'
nl|'\n'
string|"'public'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
string|"'private'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
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
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'addresses'"
op|':'
name|'self'
op|'.'
name|'builder'
op|'.'
name|'build'
op|'('
name|'instance'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|public
dedent|''
name|'def'
name|'public'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
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
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'public'"
op|':'
name|'self'
op|'.'
name|'builder'
op|'.'
name|'build_public_parts'
op|'('
name|'instance'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|private
dedent|''
name|'def'
name|'private'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
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
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'private'"
op|':'
name|'self'
op|'.'
name|'builder'
op|'.'
name|'build_private_parts'
op|'('
name|'instance'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
