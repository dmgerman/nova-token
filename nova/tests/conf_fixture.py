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
name|'fixtures'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'ipv6'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'utils'
name|'import'
name|'cleanup_dns_managers'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'scheduler_driver'"
op|','
string|"'nova.scheduler.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'fake_network'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'network_size'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'num_networks'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'floating_ip_dns_manager'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'instance_dns_manager'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'policy_file'"
op|','
string|"'nova.policy'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'api_paste_config'"
op|','
string|"'nova.wsgi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfFixture
name|'class'
name|'ConfFixture'
op|'('
name|'fixtures'
op|'.'
name|'Fixture'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixture to manage global conf settings."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conf'
op|'='
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ConfFixture'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
nl|'\n'
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'etc/nova/api-paste.ini'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.fake.FakeDriver'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'fake_network'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'fake_rabbit'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'flat_network_bridge'"
op|','
string|"'br100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'floating_ip_dns_manager'"
op|','
nl|'\n'
string|"'nova.tests.utils.dns_manager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'instance_dns_manager'"
op|','
nl|'\n'
string|"'nova.tests.utils.dns_manager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'lock_path'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'network_size'"
op|','
number|'8'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'num_networks'"
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_backend'"
op|','
nl|'\n'
string|"'nova.openstack.common.rpc.impl_fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_cast_timeout'"
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_response_timeout'"
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'sql_connection'"
op|','
string|'"sqlite://"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'sqlite_synchronous'"
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'use_ipv6'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'verbose'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'vlan_interface'"
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'config'
op|'.'
name|'parse_args'
op|'('
op|'['
op|']'
op|','
name|'default_config_files'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'conf'
op|'.'
name|'reset'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'cleanup_dns_managers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'ipv6'
op|'.'
name|'api'
op|'.'
name|'reset_backend'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
