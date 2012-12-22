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
string|'"""\nSQLAlchemy models for baremetal data.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
op|','
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'ForeignKey'
op|','
name|'DateTime'
op|','
name|'Text'
op|','
name|'Index'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'ext'
op|'.'
name|'declarative'
name|'import'
name|'declarative_base'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|BASE
name|'BASE'
op|'='
name|'declarative_base'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNode
name|'class'
name|'BareMetalNode'
op|'('
name|'BASE'
op|','
name|'models'
op|'.'
name|'NovaBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents a bare metal node."""'
newline|'\n'
nl|'\n'
DECL|variable|__tablename__
name|'__tablename__'
op|'='
string|"'bm_nodes'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|service_host
name|'service_host'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'36'
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|cpus
name|'cpus'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|memory_mb
name|'memory_mb'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|local_gb
name|'local_gb'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|pm_address
name|'pm_address'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
DECL|variable|pm_user
name|'pm_user'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
DECL|variable|pm_password
name|'pm_password'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
DECL|variable|prov_mac_address
name|'prov_mac_address'
op|'='
name|'Column'
op|'('
name|'Text'
op|')'
newline|'\n'
DECL|variable|registration_status
name|'registration_status'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'16'
op|')'
op|')'
newline|'\n'
DECL|variable|task_state
name|'task_state'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|prov_vlan_id
name|'prov_vlan_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|terminal_port
name|'terminal_port'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalPxeIp
dedent|''
name|'class'
name|'BareMetalPxeIp'
op|'('
name|'BASE'
op|','
name|'models'
op|'.'
name|'NovaBase'
op|')'
op|':'
newline|'\n'
DECL|variable|__tablename__
indent|'    '
name|'__tablename__'
op|'='
string|"'bm_pxe_ips'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|address
name|'address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|server_address
name|'server_address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|bm_node_id
name|'bm_node_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'bm_nodes.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalInterface
dedent|''
name|'class'
name|'BareMetalInterface'
op|'('
name|'BASE'
op|','
name|'models'
op|'.'
name|'NovaBase'
op|')'
op|':'
newline|'\n'
DECL|variable|__tablename__
indent|'    '
name|'__tablename__'
op|'='
string|"'bm_interfaces'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|bm_node_id
name|'bm_node_id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'ForeignKey'
op|'('
string|"'bm_nodes.id'"
op|')'
op|','
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|address
name|'address'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|datapath_id
name|'datapath_id'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|port_no
name|'port_no'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|vif_uuid
name|'vif_uuid'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'36'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalDeployment
dedent|''
name|'class'
name|'BareMetalDeployment'
op|'('
name|'BASE'
op|','
name|'models'
op|'.'
name|'NovaBase'
op|')'
op|':'
newline|'\n'
DECL|variable|__tablename__
indent|'    '
name|'__tablename__'
op|'='
string|"'bm_deployments'"
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'Column'
op|'('
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|key
name|'key'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|image_path
name|'image_path'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|pxe_config_path
name|'pxe_config_path'
op|'='
name|'Column'
op|'('
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
DECL|variable|root_mb
name|'root_mb'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
DECL|variable|swap_mb
name|'swap_mb'
op|'='
name|'Column'
op|'('
name|'Integer'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
