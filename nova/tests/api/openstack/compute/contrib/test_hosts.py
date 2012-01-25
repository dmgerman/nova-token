begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'hosts'
name|'as'
name|'os_hosts'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'api'
name|'as'
name|'scheduler_api'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.hosts'"
op|')'
newline|'\n'
comment|'# Simulate the hosts returned by the zone manager.'
nl|'\n'
DECL|variable|HOST_LIST
name|'HOST_LIST'
op|'='
op|'['
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_c1"'
op|','
string|'"service"'
op|':'
string|'"compute"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_c2"'
op|','
string|'"service"'
op|':'
string|'"compute"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_v1"'
op|','
string|'"service"'
op|':'
string|'"volume"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host_v2"'
op|','
string|'"service"'
op|':'
string|'"volume"'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_get_host_list
name|'def'
name|'stub_get_host_list'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'HOST_LIST'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_set_host_enabled
dedent|''
name|'def'
name|'stub_set_host_enabled'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
comment|"# We'll simulate success and failure by assuming"
nl|'\n'
comment|"# that 'host_c1' always succeeds, and 'host_c2'"
nl|'\n'
comment|'# always fails'
nl|'\n'
indent|'    '
name|'fail'
op|'='
op|'('
name|'host'
op|'=='
string|'"host_c2"'
op|')'
newline|'\n'
name|'status'
op|'='
string|'"enabled"'
name|'if'
op|'('
name|'enabled'
op|'^'
name|'fail'
op|')'
name|'else'
string|'"disabled"'
newline|'\n'
name|'return'
name|'status'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_host_power_action
dedent|''
name|'def'
name|'stub_host_power_action'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'action'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
dedent|''
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostTestCase
dedent|''
name|'class'
name|'HostTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test Case for hosts."""'
newline|'\n'
nl|'\n'
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
name|'HostTestCase'
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
name|'controller'
op|'='
name|'os_hosts'
op|'.'
name|'HostController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'scheduler_api'
op|','
string|"'get_host_list'"
op|','
name|'stub_get_host_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|"'set_host_enabled'"
op|','
nl|'\n'
name|'stub_set_host_enabled'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
string|"'host_power_action'"
op|','
nl|'\n'
name|'stub_host_power_action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_hosts
dedent|''
name|'def'
name|'test_list_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify that the compute hosts are returned."""'
newline|'\n'
name|'hosts'
op|'='
name|'os_hosts'
op|'.'
name|'_list_hosts'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'hosts'
op|','
name|'HOST_LIST'
op|')'
newline|'\n'
nl|'\n'
name|'compute_hosts'
op|'='
name|'os_hosts'
op|'.'
name|'_list_hosts'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"compute"'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'host'
name|'for'
name|'host'
name|'in'
name|'HOST_LIST'
nl|'\n'
name|'if'
name|'host'
op|'['
string|'"service"'
op|']'
op|'=='
string|'"compute"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'compute_hosts'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disable_host
dedent|''
name|'def'
name|'test_disable_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dis_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|'}'
newline|'\n'
name|'result_c1'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'dis_body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result_c1'
op|'['
string|'"status"'
op|']'
op|','
string|'"disabled"'
op|')'
newline|'\n'
name|'result_c2'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c2"'
op|','
name|'body'
op|'='
name|'dis_body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result_c2'
op|'['
string|'"status"'
op|']'
op|','
string|'"enabled"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enable_host
dedent|''
name|'def'
name|'test_enable_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'en_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"enable"'
op|'}'
newline|'\n'
name|'result_c1'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'en_body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result_c1'
op|'['
string|'"status"'
op|']'
op|','
string|'"enabled"'
op|')'
newline|'\n'
name|'result_c2'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c2"'
op|','
name|'body'
op|'='
name|'en_body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result_c2'
op|'['
string|'"status"'
op|']'
op|','
string|'"disabled"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_enable_maintainance_mode
dedent|''
name|'def'
name|'test_enable_maintainance_mode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"maintenance_mode"'
op|':'
string|'"enable"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disable_maintainance_mode_and_enable
dedent|''
name|'def'
name|'test_disable_maintainance_mode_and_enable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"enable"'
op|','
string|'"maintenance_mode"'
op|':'
string|'"disable"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_startup
dedent|''
name|'def'
name|'test_host_startup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'startup'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"startup"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_shutdown
dedent|''
name|'def'
name|'test_host_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'shutdown'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"shutdown"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_reboot
dedent|''
name|'def'
name|'test_host_reboot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'reboot'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|'"power_action"'
op|']'
op|','
string|'"reboot"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_status_value
dedent|''
name|'def'
name|'test_bad_status_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_update_key
dedent|''
name|'def'
name|'test_bad_update_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"crazy"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_update_key_and_correct_udpate_key
dedent|''
name|'def'
name|'test_bad_update_key_and_correct_udpate_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bad_body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|','
string|'"crazy"'
op|':'
string|'"bad"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"host_c1"'
op|','
name|'body'
op|'='
name|'bad_body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_host
dedent|''
name|'def'
name|'test_bad_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'HostNotFound'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|'"bogus_host_name"'
op|','
name|'body'
op|'='
op|'{'
string|'"status"'
op|':'
string|'"disable"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostSerializerTest
dedent|''
dedent|''
name|'class'
name|'HostSerializerTest'
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
name|'HostSerializerTest'
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
name|'deserializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostIndexTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'HOST_LIST'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'hosts'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'HOST_LIST'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'HOST_LIST'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'HOST_LIST'
op|'['
name|'i'
op|']'
op|'['
string|"'host_name'"
op|']'
op|','
nl|'\n'
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'host_name'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'HOST_LIST'
op|'['
name|'i'
op|']'
op|'['
string|"'service'"
op|']'
op|','
nl|'\n'
name|'tree'
op|'['
name|'i'
op|']'
op|'.'
name|'get'
op|'('
string|"'service'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_status
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'status'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_maintainance_mode
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_maintainance_mode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'maintenance_mode'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_serializer_with_maintainance_mode_and_status
dedent|''
dedent|''
name|'def'
name|'test_update_serializer_with_maintainance_mode_and_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
nl|'\n'
name|'maintenance_mode'
op|'='
string|"'enabled'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'enabled'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostUpdateTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_action_serializer
dedent|''
dedent|''
name|'def'
name|'test_action_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
string|"'host_c1'"
op|','
name|'power_action'
op|'='
string|"'reboot'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'os_hosts'
op|'.'
name|'HostActionTemplate'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'exemplar'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_deserializer
dedent|''
dedent|''
name|'def'
name|'test_update_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
string|"'enabled'"
op|','
name|'foo'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'intext'
op|'='
op|'('
string|'"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\\n"'
nl|'\n'
string|"'<updates><status>enabled</status><foo>bar</foo></updates>'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict'
op|'('
name|'body'
op|'='
name|'exemplar'
op|')'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
