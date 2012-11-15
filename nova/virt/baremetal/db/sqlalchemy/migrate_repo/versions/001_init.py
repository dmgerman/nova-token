begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
name|'migrate'
name|'import'
name|'ForeignKeyConstraint'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Boolean'
op|','
name|'BigInteger'
op|','
name|'Column'
op|','
name|'DateTime'
op|','
name|'Float'
op|','
name|'ForeignKey'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
op|','
name|'Integer'
op|','
name|'MetaData'
op|','
name|'String'
op|','
name|'Table'
op|','
name|'Text'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'bm_nodes'
op|'='
name|'Table'
op|'('
string|"'bm_nodes'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'cpus'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'memory_mb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'local_gb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'pm_address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'pm_user'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'pm_password'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'service_host'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'prov_mac_address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'instance_uuid'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'36'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'registration_status'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'16'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'task_state'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'prov_vlan_id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'terminal_port'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
comment|"#mysql_charset='utf8'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'bm_interfaces'
op|'='
name|'Table'
op|'('
string|"'bm_interfaces'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'bm_node_id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'datapath_id'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'port_no'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'vif_uuid'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'36'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
comment|"#mysql_charset='utf8'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'bm_pxe_ips'
op|'='
name|'Table'
op|'('
string|"'bm_pxe_ips'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'bm_node_id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'server_address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
comment|"#mysql_charset='utf8'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'bm_deployments'
op|'='
name|'Table'
op|'('
string|"'bm_deployments'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'bm_node_id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'key'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'image_path'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'pxe_config_path'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'root_mb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'swap_mb'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
comment|"#mysql_charset='utf8'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'bm_nodes'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'bm_interfaces'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'bm_pxe_ips'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'bm_deployments'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'Index'
op|'('
string|"'idx_bm_nodes_service_host_deleted'"
op|','
nl|'\n'
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'service_host'
op|','
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'Index'
op|'('
string|"'idx_bm_nodes_instance_uuid_deleted'"
op|','
nl|'\n'
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|','
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
name|'Index'
op|'('
string|"'idx_bm_nodes_hmcld'"
op|','
nl|'\n'
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'service_host'
op|','
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'memory_mb'
op|','
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'cpus'
op|','
nl|'\n'
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'local_gb'
op|','
name|'bm_nodes'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'Index'
op|'('
string|"'idx_bm_interfaces_bm_node_id_deleted'"
op|','
nl|'\n'
name|'bm_interfaces'
op|'.'
name|'c'
op|'.'
name|'bm_node_id'
op|','
name|'bm_interfaces'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
name|'Index'
op|'('
string|"'idx_bm_pxe_ips_bm_node_id_deleted'"
op|','
nl|'\n'
name|'bm_pxe_ips'
op|'.'
name|'c'
op|'.'
name|'bm_node_id'
op|','
name|'bm_pxe_ips'
op|'.'
name|'c'
op|'.'
name|'deleted'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
