begin_unit
comment|'# Copyright (c) 2013 NTT DOCOMO, INC.'
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
string|'"""The bare-metal admin extension with Ironic Proxy."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ironic_client
name|'ironic_client'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|"'ironicclient.client'"
op|')'
newline|'\n'
DECL|variable|ironic_exc
name|'ironic_exc'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|"'ironicclient.exc'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'baremetal_nodes'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|node_fields
name|'node_fields'
op|'='
op|'['
string|"'id'"
op|','
string|"'cpus'"
op|','
string|"'local_gb'"
op|','
string|"'memory_mb'"
op|','
string|"'pm_address'"
op|','
nl|'\n'
string|"'pm_user'"
op|','
string|"'service_host'"
op|','
string|"'terminal_port'"
op|','
string|"'instance_uuid'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|node_ext_fields
name|'node_ext_fields'
op|'='
op|'['
string|"'uuid'"
op|','
string|"'task_state'"
op|','
string|"'updated_at'"
op|','
string|"'pxe_config_path'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|interface_fields
name|'interface_fields'
op|'='
op|'['
string|"'id'"
op|','
string|"'address'"
op|','
string|"'datapath_id'"
op|','
string|"'port_no'"
op|']'
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
string|"'api_version'"
op|','
nl|'\n'
string|"'nova.virt.ironic.driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'api_endpoint'"
op|','
nl|'\n'
string|"'nova.virt.ironic.driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'admin_username'"
op|','
nl|'\n'
string|"'nova.virt.ironic.driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'admin_password'"
op|','
nl|'\n'
string|"'nova.virt.ironic.driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'admin_tenant_name'"
op|','
nl|'\n'
string|"'nova.virt.ironic.driver'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'ironic'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_check_ironic_client_enabled
name|'def'
name|'_check_ironic_client_enabled'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check whether Ironic is installed or not."""'
newline|'\n'
name|'if'
name|'ironic_client'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Ironic client unavailable, cannot access Ironic."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_ironic_client
dedent|''
dedent|''
name|'def'
name|'_get_ironic_client'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""return an Ironic client."""'
newline|'\n'
comment|'# TODO(NobodyCam): Fix insecure setting'
nl|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'os_username'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_username'
op|','
nl|'\n'
string|"'os_password'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'os_auth_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_url'
op|','
nl|'\n'
string|"'os_tenant_name'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_tenant_name'
op|','
nl|'\n'
string|"'os_service_type'"
op|':'
string|"'baremetal'"
op|','
nl|'\n'
string|"'os_endpoint_type'"
op|':'
string|"'public'"
op|','
nl|'\n'
string|"'insecure'"
op|':'
string|"'true'"
op|','
nl|'\n'
string|"'ironic_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_endpoint'
op|'}'
newline|'\n'
name|'ironicclient'
op|'='
name|'ironic_client'
op|'.'
name|'get_client'
op|'('
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_version'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'ironicclient'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_no_ironic_proxy
dedent|''
name|'def'
name|'_no_ironic_proxy'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Command Not supported. Please use Ironic "'
nl|'\n'
string|'"command %(cmd)s to perform this "'
nl|'\n'
string|'"action."'
op|')'
op|'%'
op|'{'
string|"'cmd'"
op|':'
name|'cmd'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNodeController
dedent|''
name|'class'
name|'BareMetalNodeController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Bare-Metal Node API controller for the OpenStack API.\n\n    Ironic is used for the following commands:\n        \'baremetal-node-list\'\n        \'baremetal-node-show\'\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'BareMetalNodeController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
DECL|member|_node_dict
dedent|''
name|'def'
name|'_node_dict'
op|'('
name|'self'
op|','
name|'node_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'node_fields'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'f'
op|']'
op|'='
name|'node_ref'
op|'.'
name|'get'
op|'('
name|'f'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-baremetal-ext-status'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'f'
name|'in'
name|'node_ext_fields'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'['
name|'f'
op|']'
op|'='
name|'node_ref'
op|'.'
name|'get'
op|'('
name|'f'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'nodes'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# proxy command to Ironic'
nl|'\n'
name|'_check_ironic_client_enabled'
op|'('
op|')'
newline|'\n'
name|'ironicclient'
op|'='
name|'_get_ironic_client'
op|'('
op|')'
newline|'\n'
name|'ironic_nodes'
op|'='
name|'ironicclient'
op|'.'
name|'node'
op|'.'
name|'list'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'for'
name|'inode'
name|'in'
name|'ironic_nodes'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
op|'{'
string|"'id'"
op|':'
name|'inode'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'inode'
op|'.'
name|'provision_state'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'cpus'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'memory_mb'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'local_gb'"
op|','
number|'0'
op|')'
op|'}'
newline|'\n'
name|'nodes'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'nodes'"
op|':'
name|'nodes'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
comment|'# proxy command to Ironic'
nl|'\n'
name|'_check_ironic_client_enabled'
op|'('
op|')'
newline|'\n'
name|'icli'
op|'='
name|'_get_ironic_client'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'inode'
op|'='
name|'icli'
op|'.'
name|'node'
op|'.'
name|'get'
op|'('
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ironic_exc'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Node %s could not be found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'iports'
op|'='
name|'icli'
op|'.'
name|'node'
op|'.'
name|'list_ports'
op|'('
name|'id'
op|')'
newline|'\n'
name|'node'
op|'='
op|'{'
string|"'id'"
op|':'
name|'inode'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'interfaces'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'IRONIC MANAGED'"
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'inode'
op|'.'
name|'provision_state'
op|','
nl|'\n'
string|"'cpus'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'cpus'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'memory_mb'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'inode'
op|'.'
name|'properties'
op|'.'
name|'get'
op|'('
string|"'local_gb'"
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'inode'
op|'.'
name|'instance_uuid'
op|'}'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'iports'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'['
string|"'interfaces'"
op|']'
op|'.'
name|'append'
op|'('
op|'{'
string|"'address'"
op|':'
name|'port'
op|'.'
name|'address'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'node'"
op|':'
name|'node'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_no_ironic_proxy'
op|'('
string|'"port-create"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_no_ironic_proxy'
op|'('
string|'"port-create"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'add_interface'"
op|')'
newline|'\n'
DECL|member|_add_interface
name|'def'
name|'_add_interface'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_no_ironic_proxy'
op|'('
string|'"port-create"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'remove_interface'"
op|')'
newline|'\n'
DECL|member|_remove_interface
name|'def'
name|'_remove_interface'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_no_ironic_proxy'
op|'('
string|'"port-delete"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Baremetal_nodes
dedent|''
dedent|''
name|'class'
name|'Baremetal_nodes'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only bare-metal node administration."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"BareMetalNodes"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-baremetal-nodes"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/baremetal_nodes/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-01-04T00:00:00Z"'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-baremetal-nodes'"
op|','
nl|'\n'
name|'BareMetalNodeController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|'"action"'
op|':'
string|'"POST"'
op|','
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
