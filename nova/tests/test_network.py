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
string|'"""\nUnit Tests for network code\n"""'
newline|'\n'
name|'import'
name|'IPy'
newline|'\n'
name|'import'
name|'os'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkTestCase
name|'class'
name|'NetworkTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for network code"""'
newline|'\n'
DECL|member|setUp
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
name|'NetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(vish): if you change these flags, make sure to change the'
nl|'\n'
comment|'#             flags in the corresponding section in nova-dhcpbridge'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'fake_call'
op|'='
name|'True'
op|','
nl|'\n'
name|'fake_network'
op|'='
name|'True'
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
string|"'netuser'"
op|','
string|"'netuser'"
op|','
string|"'netuser'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'projects'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'network'
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
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'project'
op|'='
name|'None'
op|','
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
string|"'project%s'"
op|'%'
name|'i'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
name|'name'
op|','
string|"'netuser'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'projects'
op|'.'
name|'append'
op|'('
name|'project'
op|')'
newline|'\n'
comment|'# create the necessary network data for the project'
nl|'\n'
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'get_network_host'
op|'('
name|'user_context'
op|'.'
name|'elevated'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance2_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
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
comment|'# TODO(termie): this should really be instantiating clean datastores'
nl|'\n'
comment|'#               in between runs, one failure kills all the tests'
nl|'\n'
indent|'        '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'instance2_id'
op|')'
newline|'\n'
name|'for'
name|'project'
name|'in'
name|'self'
op|'.'
name|'projects'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
dedent|''
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
name|'NetworkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|','
name|'project_num'
op|','
name|'mac'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'mac'
op|':'
newline|'\n'
indent|'            '
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
dedent|''
name|'project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'project_num'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'project'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'project_id'"
op|':'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'mac'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_address
dedent|''
name|'def'
name|'_create_address'
op|'('
name|'self'
op|','
name|'project_num'
op|','
name|'instance_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create an address in given project num"""'
newline|'\n'
name|'if'
name|'instance_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'instance_id'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'project_num'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'project_num'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_deallocate_address
dedent|''
name|'def'
name|'_deallocate_address'
op|'('
name|'self'
op|','
name|'project_num'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'project_num'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'project_num'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_private_ipv6
dedent|''
name|'def'
name|'test_private_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure ipv6 is OK"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
number|'0'
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'address_v6'
op|'='
name|'db'
op|'.'
name|'instance_get_fixed_address_v6'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'to_mac'
op|'('
name|'address_v6'
op|')'
op|')'
newline|'\n'
name|'instance_ref2'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_instance_v6'
op|'('
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'address_v6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'instance_ref2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address_v6'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'to_global_ipv6'
op|'('
nl|'\n'
name|'network_ref'
op|'['
string|"'cidr_v6'"
op|']'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_deallocate_address'
op|'('
number|'0'
op|','
name|'address'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_public_network_association
dedent|''
dedent|''
name|'def'
name|'test_public_network_association'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure that we can allocaate a public ip"""'
newline|'\n'
comment|'# TODO(vish): better way of adding floating ips'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'pubnet'
op|'='
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'floating_range'
op|')'
newline|'\n'
name|'address'
op|'='
name|'str'
op|'('
name|'pubnet'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'address'
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
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'FLAGS'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'float_addr'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'fix_addr'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'fix_addr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'float_addr'
op|','
name|'str'
op|'('
name|'pubnet'
op|'['
number|'0'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'associate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'float_addr'
op|','
name|'fix_addr'
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'instance_get_floating_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|','
name|'float_addr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'float_addr'
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'instance_get_floating_address'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'float_addr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fix_addr'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'fix_addr'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'float_addr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_deallocate_fixed_ip
dedent|''
name|'def'
name|'test_allocate_deallocate_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure that we can allocate and deallocate a fixed ip"""'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_deallocate_address'
op|'('
number|'0'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
comment|"# Doesn't go away until it's dhcp released"
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_side_effects
dedent|''
name|'def'
name|'test_side_effects'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures allocating and releasing has no side effects"""'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'address2'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'instance2_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address2'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'1'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'1'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# Addresses are allocated before they're issued"
nl|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address2'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_deallocate_address'
op|'('
number|'0'
op|','
name|'address'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# First address release shouldn't affect the second"
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address2'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'1'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_deallocate_address'
op|'('
number|'1'
op|','
name|'address2'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address2'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'1'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_subnet_edge
dedent|''
name|'def'
name|'test_subnet_edge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure that private ips don\'t overlap"""'
newline|'\n'
name|'first'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'first'
op|')'
newline|'\n'
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'FLAGS'
op|'.'
name|'num_networks'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'i'
op|','
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
name|'i'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'i'
op|','
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'address2'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
name|'i'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'i'
op|','
name|'mac'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'address3'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
name|'i'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address2'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'i'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
name|'i'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address2'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'is_allocated_in_project'
op|'('
name|'address3'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address3'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address2'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address3'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'.'
name|'_project'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'first'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_deallocate_address'
op|'('
number|'0'
op|','
name|'first'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'first'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vpn_ip_and_port_looks_valid
dedent|''
name|'def'
name|'test_vpn_ip_and_port_looks_valid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the vpn ip and port are reasonable"""'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'vpn_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'vpn_port'
op|'>='
name|'FLAGS'
op|'.'
name|'vpn_start'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'vpn_port'
op|'<='
name|'FLAGS'
op|'.'
name|'vpn_start'
op|'+'
nl|'\n'
name|'FLAGS'
op|'.'
name|'num_networks'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_networks
dedent|''
name|'def'
name|'test_too_many_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure error is raised if we run out of networks"""'
newline|'\n'
name|'projects'
op|'='
op|'['
op|']'
newline|'\n'
name|'networks_left'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'num_networks'
op|'-'
nl|'\n'
name|'db'
op|'.'
name|'network_count'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'networks_left'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'many%s'"
op|'%'
name|'i'
op|','
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'projects'
op|'.'
name|'append'
op|'('
name|'project'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
dedent|''
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'last'"
op|','
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'projects'
op|'.'
name|'append'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'db'
op|'.'
name|'NoMoreNetworks'
op|','
nl|'\n'
name|'db'
op|'.'
name|'project_get_network'
op|','
nl|'\n'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'for'
name|'project'
name|'in'
name|'projects'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ips_are_reused
dedent|''
dedent|''
name|'def'
name|'test_ips_are_reused'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure that ip addresses that are deallocated get reused"""'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
name|'address2'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'address'
op|','
name|'address2'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'address2'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_available_ips
dedent|''
name|'def'
name|'test_available_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure the number of available ips for the network is correct\n\n        The number of available IP addresses depends on the test\n        environment\'s setup.\n\n        Network size is set in test fixture\'s setUp method.\n\n        There are ips reserved at the bottom and top of the range.\n        services (network, gateway, CloudPipe, broadcast)\n        """'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'net_size'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'network_size'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'total_ips'
op|'='
op|'('
name|'db'
op|'.'
name|'network_count_available_ips'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
op|'+'
nl|'\n'
name|'db'
op|'.'
name|'network_count_reserved_ips'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
op|'+'
nl|'\n'
name|'db'
op|'.'
name|'network_count_allocated_ips'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'total_ips'
op|','
name|'net_size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_addresses
dedent|''
name|'def'
name|'test_too_many_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test for a NoMoreAddresses exception when all fixed ips are used.\n        """'
newline|'\n'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'admin_context'
op|','
name|'self'
op|'.'
name|'projects'
op|'['
number|'0'
op|']'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'num_available_ips'
op|'='
name|'db'
op|'.'
name|'network_count_available_ips'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'addresses'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_available_ips'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
number|'0'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'address'
op|'='
name|'self'
op|'.'
name|'_create_address'
op|'('
number|'0'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'addresses'
op|'.'
name|'append'
op|'('
name|'address'
op|')'
newline|'\n'
name|'lease_ip'
op|'('
name|'address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ip_count'
op|'='
name|'db'
op|'.'
name|'network_count_available_ips'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_count'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'db'
op|'.'
name|'NoMoreAddresses'
op|','
nl|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_fixed_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_available_ips'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network'
op|'.'
name|'deallocate_fixed_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'addresses'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
name|'release_ip'
op|'('
name|'addresses'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'instance_ids'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
dedent|''
name|'ip_count'
op|'='
name|'db'
op|'.'
name|'network_count_available_ips'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_count'
op|','
name|'num_available_ips'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_allocated_in_project
dedent|''
dedent|''
name|'def'
name|'is_allocated_in_project'
op|'('
name|'address'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns true if address is in specified project"""'
newline|'\n'
name|'project_net'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'network'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'address'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'address'
op|')'
newline|'\n'
comment|'# instance exists until release'
nl|'\n'
name|'return'
name|'instance'
name|'is'
name|'not'
name|'None'
name|'and'
name|'network'
op|'['
string|"'id'"
op|']'
op|'=='
name|'project_net'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|binpath
dedent|''
name|'def'
name|'binpath'
op|'('
name|'script'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the absolute path to a script in bin"""'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'__file__'
op|','
string|'"../../../bin"'
op|','
name|'script'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|lease_ip
dedent|''
name|'def'
name|'lease_ip'
op|'('
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run add command on dhcpbridge"""'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'cmd'
op|'='
string|'"%s add %s %s fake"'
op|'%'
op|'('
name|'binpath'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'env'
op|'='
op|'{'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
string|"'TESTING'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|'}'
newline|'\n'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"ISSUE_IP: %s, %s "'
op|','
name|'out'
op|','
name|'err'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|release_ip
dedent|''
name|'def'
name|'release_ip'
op|'('
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run del command on dhcpbridge"""'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_get_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'cmd'
op|'='
string|'"%s del %s %s fake"'
op|'%'
op|'('
name|'binpath'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'env'
op|'='
op|'{'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
nl|'\n'
string|"'TESTING'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|'}'
newline|'\n'
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"RELEASE_IP: %s, %s "'
op|','
name|'out'
op|','
name|'err'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
