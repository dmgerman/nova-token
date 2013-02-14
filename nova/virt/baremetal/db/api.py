begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
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
string|'"""Defines interface for DB access.\n\nThe underlying driver is loaded as a :class:`LazyPluggable`.\n\nFunctions in this module are imported into the nova.virt.baremetal.db\nnamespace. Call these functions from nova.virt.baremetal.db namespace, not\nthe nova.virt.baremetal.db.api namespace.\n\nAll functions in this module return objects that implement a dictionary-like\ninterface. Currently, many of these objects are sqlalchemy objects that\nimplement a dictionary interface. However, a future goal is to have all of\nthese objects be simple dictionaries.\n\n\n**Related Flags**\n\n:baremetal_db_backend:  string to lookup in the list of LazyPluggable backends.\n                        `sqlalchemy` is the only supported backend right now.\n\n:[BAREMETAL] sql_connection: string specifying the sqlalchemy connection to\n                             use, like: `sqlite:///var/lib/nova/nova.sqlite`.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
comment|"# NOTE(deva): we can't move baremetal_db_backend into an OptGroup yet"
nl|'\n'
comment|"#             because utils.LazyPluggable doesn't support reading from"
nl|'\n'
comment|'#             option groups. See bug #1093043.'
nl|'\n'
DECL|variable|db_opts
name|'db_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'db_backend'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'sqlalchemy'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The backend to use for bare-metal database'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|baremetal_group
name|'baremetal_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Baremetal Options'"
op|')'
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
name|'register_group'
op|'('
name|'baremetal_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'db_opts'
op|','
name|'baremetal_group'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|IMPL
name|'IMPL'
op|'='
name|'utils'
op|'.'
name|'LazyPluggable'
op|'('
nl|'\n'
string|"'db_backend'"
op|','
nl|'\n'
DECL|variable|config_group
name|'config_group'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|sqlalchemy
name|'sqlalchemy'
op|'='
string|"'nova.virt.baremetal.db.sqlalchemy.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get_all
name|'def'
name|'bm_node_get_all'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get_associated
dedent|''
name|'def'
name|'bm_node_get_associated'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get_associated'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get_unassociated
dedent|''
name|'def'
name|'bm_node_get_unassociated'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get_unassociated'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_host'
op|'='
name|'service_host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_find_free
dedent|''
name|'def'
name|'bm_node_find_free'
op|'('
name|'context'
op|','
name|'service_host'
op|'='
name|'None'
op|','
nl|'\n'
name|'memory_mb'
op|'='
name|'None'
op|','
name|'cpus'
op|'='
name|'None'
op|','
name|'local_gb'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_find_free'
op|'('
name|'context'
op|','
nl|'\n'
name|'service_host'
op|'='
name|'service_host'
op|','
nl|'\n'
name|'memory_mb'
op|'='
name|'memory_mb'
op|','
nl|'\n'
name|'cpus'
op|'='
name|'cpus'
op|','
nl|'\n'
name|'local_gb'
op|'='
name|'local_gb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get
dedent|''
name|'def'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get_by_instance_uuid
dedent|''
name|'def'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_get_by_node_uuid
dedent|''
name|'def'
name|'bm_node_get_by_node_uuid'
op|'('
name|'context'
op|','
name|'node_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_get_by_node_uuid'
op|'('
name|'context'
op|','
name|'node_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_create
dedent|''
name|'def'
name|'bm_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_destroy
dedent|''
name|'def'
name|'bm_node_destroy'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_destroy'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_update
dedent|''
name|'def'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_node_associate_and_update
dedent|''
name|'def'
name|'bm_node_associate_and_update'
op|'('
name|'context'
op|','
name|'node_uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_node_associate_and_update'
op|'('
name|'context'
op|','
name|'node_uuid'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_create
dedent|''
name|'def'
name|'bm_pxe_ip_create'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'server_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_create'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'server_address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_create_direct
dedent|''
name|'def'
name|'bm_pxe_ip_create_direct'
op|'('
name|'context'
op|','
name|'bm_pxe_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_create_direct'
op|'('
name|'context'
op|','
name|'bm_pxe_ip'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_destroy
dedent|''
name|'def'
name|'bm_pxe_ip_destroy'
op|'('
name|'context'
op|','
name|'ip_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_destroy'
op|'('
name|'context'
op|','
name|'ip_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_destroy_by_address
dedent|''
name|'def'
name|'bm_pxe_ip_destroy_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_destroy_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_get_all
dedent|''
name|'def'
name|'bm_pxe_ip_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_get
dedent|''
name|'def'
name|'bm_pxe_ip_get'
op|'('
name|'context'
op|','
name|'ip_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_get'
op|'('
name|'context'
op|','
name|'ip_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_get_by_bm_node_id
dedent|''
name|'def'
name|'bm_pxe_ip_get_by_bm_node_id'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_get_by_bm_node_id'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_associate
dedent|''
name|'def'
name|'bm_pxe_ip_associate'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_associate'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_pxe_ip_disassociate
dedent|''
name|'def'
name|'bm_pxe_ip_disassociate'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_pxe_ip_disassociate'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_get
dedent|''
name|'def'
name|'bm_interface_get'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_get'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_get_all
dedent|''
name|'def'
name|'bm_interface_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_destroy
dedent|''
name|'def'
name|'bm_interface_destroy'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_destroy'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_create
dedent|''
name|'def'
name|'bm_interface_create'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'address'
op|','
name|'datapath_id'
op|','
name|'port_no'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_create'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|','
name|'address'
op|','
nl|'\n'
name|'datapath_id'
op|','
name|'port_no'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_set_vif_uuid
dedent|''
name|'def'
name|'bm_interface_set_vif_uuid'
op|'('
name|'context'
op|','
name|'if_id'
op|','
name|'vif_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_set_vif_uuid'
op|'('
name|'context'
op|','
name|'if_id'
op|','
name|'vif_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_get_by_vif_uuid
dedent|''
name|'def'
name|'bm_interface_get_by_vif_uuid'
op|'('
name|'context'
op|','
name|'vif_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_get_by_vif_uuid'
op|'('
name|'context'
op|','
name|'vif_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bm_interface_get_all_by_bm_node_id
dedent|''
name|'def'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'IMPL'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'bm_node_id'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
