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
string|'"""\nTests For misc util methods used with compute.\n"""'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'notifier'
name|'import'
name|'test_notifier'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.compute_utils'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'stub_network'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsageInfoTestCase
name|'class'
name|'UsageInfoTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'UsageInfoTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'stub_network'
op|'='
name|'True'
op|','
nl|'\n'
name|'notification_driver'
op|'='
string|"'nova.notifier.test_notifier'"
op|','
nl|'\n'
name|'network_manager'
op|'='
string|"'nova.network.manager.FlatManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_show
name|'def'
name|'fake_show'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
number|'1'
op|','
string|"'ramdisk_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
string|"'show'"
op|','
name|'fake_show'
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
name|'params'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project_id'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
name|'type_id'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'root_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
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
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_notify_usage_exists
dedent|''
name|'def'
name|'test_notify_usage_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure \'exists\' notification generates apropriate usage data."""'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_usage_exists'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'compute.instance.exists'"
op|')'
newline|'\n'
name|'payload'
op|'='
name|'msg'
op|'['
string|"'payload'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_type'"
op|']'
op|','
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'payload'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'type_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'display_name'"
op|','
string|"'created_at'"
op|','
string|"'launched_at'"
op|','
nl|'\n'
string|"'state'"
op|','
string|"'state_description'"
op|','
nl|'\n'
string|"'bandwidth'"
op|','
string|"'audit_period_beginning'"
op|','
nl|'\n'
string|"'audit_period_ending'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'attr'
name|'in'
name|'payload'
op|','
nl|'\n'
name|'msg'
op|'='
string|'"Key %s not in payload"'
op|'%'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'image_ref_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'utils'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_ref_url'"
op|']'
op|','
name|'image_ref_url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
