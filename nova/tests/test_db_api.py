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
string|'"""Unit tests for the DB API"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
op|'.'
name|'auth'
name|'import'
name|'manager'
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
DECL|function|_setup_networking
name|'def'
name|'_setup_networking'
op|'('
name|'instance_id'
op|','
name|'ip'
op|'='
string|"'1.2.3.4'"
op|','
name|'flo_addr'
op|'='
string|"'1.2.1.2'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_networks'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
name|'associate'
op|'='
name|'True'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vif'
op|'='
op|'{'
string|"'address'"
op|':'
string|"'56:12:12:12:12:12'"
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'instance_id'
op|'}'
newline|'\n'
name|'vif_ref'
op|'='
name|'db'
op|'.'
name|'virtual_interface_create'
op|'('
name|'ctxt'
op|','
name|'vif'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ip'
op|'='
op|'{'
string|"'address'"
op|':'
name|'ip'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'virtual_interface_id'"
op|':'
name|'vif_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'instance_id'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'ctxt'
op|','
name|'fixed_ip'
op|')'
newline|'\n'
name|'fix_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'ctxt'
op|','
name|'ip'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'ctxt'
op|','
op|'{'
string|"'address'"
op|':'
name|'flo_addr'
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'fix_ref'
op|'.'
name|'id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DbApiTestCase
dedent|''
name|'class'
name|'DbApiTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'DbApiTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'proj'"
op|','
string|"'admin'"
op|','
string|"'proj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'super'
op|'('
name|'DbApiTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_get_project_vpn
dedent|''
name|'def'
name|'test_instance_get_project_vpn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'instance_type_id'"
op|':'
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_get_project_vpn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'result'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_get_project_vpn_joins
dedent|''
name|'def'
name|'test_instance_get_project_vpn_joins'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'instance_type_id'"
op|':'
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'_setup_networking'
op|'('
name|'instance'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_get_project_vpn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'result'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'fixed_ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'floating_ips'"
op|']'
op|'['
number|'0'
op|']'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'1.2.1.2'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
