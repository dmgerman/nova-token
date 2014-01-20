begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Intel Corporation'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-pci'"
newline|'\n'
DECL|variable|instance_authorize
name|'instance_authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
nl|'\n'
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|'+'
string|"':pci_servers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_server
name|'def'
name|'make_server'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pci_devices'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'%s:pci_devices'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'colon_ns'
op|'='
name|'True'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'append'
op|'('
name|'pci_devices'
op|')'
newline|'\n'
name|'device'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'pci_devices'
op|','
nl|'\n'
string|"'%s:pci_device'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'selector'
op|'='
string|"'%s:pci_devices'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'colon_ns'
op|'='
name|'True'
op|')'
newline|'\n'
name|'device'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciServerTemplate
dedent|''
name|'class'
name|'PciServerTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'server'"
op|','
name|'selector'
op|'='
string|"'server'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
name|'Pci'
op|'.'
name|'alias'
op|':'
name|'Pci'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciServersTemplate
dedent|''
dedent|''
name|'class'
name|'PciServersTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'servers'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'server'"
op|','
name|'selector'
op|'='
string|"'servers'"
op|')'
newline|'\n'
name|'make_server'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
name|'Pci'
op|'.'
name|'alias'
op|':'
name|'Pci'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciServerController
dedent|''
dedent|''
name|'class'
name|'PciServerController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_server
indent|'    '
name|'def'
name|'_extend_server'
op|'('
name|'self'
op|','
name|'server'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_id'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dev'
name|'in'
name|'instance'
op|'.'
name|'pci_devices'
op|':'
newline|'\n'
indent|'            '
name|'dev_id'
op|'.'
name|'append'
op|'('
op|'{'
string|"'id'"
op|':'
name|'dev'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'['
string|"'%s:pci_devices'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|']'
op|'='
name|'dev_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'instance_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'PciServerTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'server'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'instance_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'PciServersTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'servers'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_server'
op|'('
name|'server'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_hypervisor
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'make_hypervisor'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pci_stats'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'%s:pci_stats'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'colon_ns'
op|'='
name|'True'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'append'
op|'('
name|'pci_stats'
op|')'
newline|'\n'
name|'pci_stat'
op|'='
name|'xmlutil'
op|'.'
name|'make_flat_dict'
op|'('
string|"'%s:pci_stat'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'selector'
op|'='
string|"'%s:pci_stats'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'colon_ns'
op|'='
name|'True'
op|','
nl|'\n'
name|'root'
op|'='
name|'pci_stats'
op|','
nl|'\n'
name|'ignore_sub_dicts'
op|'='
name|'True'
op|')'
newline|'\n'
name|'extra'
op|'='
name|'xmlutil'
op|'.'
name|'make_flat_dict'
op|'('
string|"'extra_info'"
op|','
name|'selector'
op|'='
string|"'extra_info'"
op|')'
newline|'\n'
name|'pci_stat'
op|'.'
name|'append'
op|'('
name|'extra'
op|')'
newline|'\n'
name|'pci_stats'
op|'.'
name|'append'
op|'('
name|'pci_stat'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciHypervisorTemplate
dedent|''
name|'class'
name|'PciHypervisorTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'hypervisor'"
op|','
name|'selector'
op|'='
string|"'hypervisor'"
op|')'
newline|'\n'
name|'make_hypervisor'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
name|'Pci'
op|'.'
name|'alias'
op|':'
name|'Pci'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorDetailTemplate
dedent|''
dedent|''
name|'class'
name|'HypervisorDetailTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'hypervisors'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'hypervisor'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'hypervisors'"
op|')'
newline|'\n'
name|'make_hypervisor'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
name|'Pci'
op|'.'
name|'alias'
op|':'
name|'Pci'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciHypervisorController
dedent|''
dedent|''
name|'class'
name|'PciHypervisorController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|_extend_hypervisor
indent|'    '
name|'def'
name|'_extend_hypervisor'
op|'('
name|'self'
op|','
name|'hypervisor'
op|','
name|'compute_node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hypervisor'
op|'['
string|"'%s:pci_stats'"
op|'%'
name|'Pci'
op|'.'
name|'alias'
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
nl|'\n'
name|'compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'PciHypervisorTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'hypervisor'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'hypervisor'"
op|']'
newline|'\n'
name|'compute_node'
op|'='
name|'req'
op|'.'
name|'get_db_compute_node'
op|'('
name|'hypervisor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_hypervisor'
op|'('
name|'hypervisor'
op|','
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'HypervisorDetailTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'hypervisors'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'hypervisors'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'hypervisor'
name|'in'
name|'hypervisors'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
op|'='
name|'req'
op|'.'
name|'get_db_compute_node'
op|'('
name|'hypervisor'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_hypervisor'
op|'('
name|'hypervisor'
op|','
name|'compute_node'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Pci
dedent|''
dedent|''
dedent|''
name|'class'
name|'Pci'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pci access support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"PCIAccess"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/%s/api/v3"'
op|'%'
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
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
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'servers'"
op|','
name|'PciServerController'
op|'('
op|')'
op|')'
newline|'\n'
name|'compute_extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
nl|'\n'
name|'self'
op|','
string|"'os-hypervisors'"
op|','
name|'PciHypervisorController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'server_extension'
op|','
name|'compute_extension'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
