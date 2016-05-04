begin_unit
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
name|'from'
name|'oslo_config'
name|'import'
name|'fixture'
name|'as'
name|'config_fixture'
newline|'\n'
name|'from'
name|'oslo_policy'
name|'import'
name|'opts'
name|'as'
name|'policy_opts'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'paths'
newline|'\n'
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
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'floating_ip_dns_manager'"
op|','
string|"'nova.network.floating_ips'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'instance_dns_manager'"
op|','
string|"'nova.network.floating_ips'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfFixture
name|'class'
name|'ConfFixture'
op|'('
name|'config_fixture'
op|'.'
name|'Config'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fixture to manage global conf settings."""'
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
name|'ConfFixture'
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
op|','
nl|'\n'
name|'group'
op|'='
string|"'wsgi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'host'"
op|','
string|"'fake-mini'"
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
string|"'fake.SmallFakeDriver'"
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
string|"'nova.tests.unit.utils.dns_manager'"
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
string|"'nova.tests.unit.utils.dns_manager'"
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
string|"'vlan_interface'"
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'auth_strategy'"
op|','
string|"'noauth2'"
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
op|','
name|'configure_db'
op|'='
name|'False'
op|','
nl|'\n'
name|'init_rpc'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'connection'"
op|','
string|'"sqlite://"'
op|','
name|'group'
op|'='
string|"'database'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'connection'"
op|','
string|'"sqlite://"'
op|','
name|'group'
op|'='
string|"'api_database'"
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
op|','
name|'group'
op|'='
string|"'database'"
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
op|','
nl|'\n'
name|'group'
op|'='
string|"'api_database'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'fatal_exception_format_errors'"
op|','
name|'True'
op|')'
newline|'\n'
comment|"# TODO(sdague): this makes our project_id match 'fake' as well."
nl|'\n'
comment|'# We should fix the tests to use real'
nl|'\n'
comment|'# UUIDs then drop this work around.'
nl|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'project_id_regex'"
op|','
nl|'\n'
string|"'[0-9a-fk\\-]+'"
op|','
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'force_dhcp_release'"
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
string|"'periodic_enable'"
op|','
name|'False'
op|')'
newline|'\n'
name|'policy_opts'
op|'.'
name|'set_defaults'
op|'('
name|'self'
op|'.'
name|'conf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'utils'
op|'.'
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
