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
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'compute_scheduler_driver'"
op|','
string|"'nova.scheduler.multi'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'fake_network'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'iscsi_num_targets'"
op|','
string|"'nova.volume.driver'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'network_size'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'num_networks'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'policy_file'"
op|','
string|"'nova.policy'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'volume_driver'"
op|','
string|"'nova.volume.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_defaults
name|'def'
name|'set_defaults'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
string|"'$state_path/etc/nova/api-paste.ini'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.fake.FakeDriver'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'connection_type'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'fake_network'"
op|','
name|'True'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'fake_rabbit'"
op|','
name|'True'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'flat_network_bridge'"
op|','
string|"'br100'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'iscsi_num_targets'"
op|','
number|'8'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'network_size'"
op|','
number|'8'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'num_networks'"
op|','
number|'2'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'vlan_interface'"
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_backend'"
op|','
string|"'nova.openstack.common.rpc.impl_fake'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'sql_connection'"
op|','
string|'"sqlite://"'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'sqlite_synchronous'"
op|','
name|'False'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'use_ipv6'"
op|','
name|'True'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'verbose'"
op|','
name|'True'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'volume_driver'"
op|','
string|"'nova.volume.driver.FakeISCSIDriver'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'api_paste_config'"
op|','
string|"'$state_path/etc/nova/api-paste.ini'"
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_response_timeout'"
op|','
number|'5'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'rpc_cast_timeout'"
op|','
number|'5'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'set_default'
op|'('
string|"'lock_path'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
