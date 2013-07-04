begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
name|'import'
name|'webob'
op|'.'
name|'exc'
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
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-agents"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AgentsIndexTemplate
name|'class'
name|'AgentsIndexTemplate'
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
string|"'agents'"
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
string|"'agent'"
op|','
name|'selector'
op|'='
string|"'agents'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'hypervisor'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'os'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'architecture'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'version'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'md5hash'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'agent_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'url'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AgentController
dedent|''
dedent|''
name|'class'
name|'AgentController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The agent is talking about guest agent.The host can use this for\n    things like accessing files on the disk, configuring networking,\n    or running other applications/scripts in the guest while it is\n    running. Typically this uses some hypervisor-specific transport\n    to avoid being dependent on a working network configuration.\n    Xen, VMware, and VirtualBox have guest agents,although the Xen\n    driver is the only one with an implementation for managing them\n    in openstack. KVM doesn\'t really have a concept of a guest agent\n    (although one could be written).\n\n    You can find the design of agent update in this link:\n    http://wiki.openstack.org/AgentUpdate\n    and find the code in nova.virt.xenapi.vmops.VMOps._boot_new_instance.\n    In this design We need update agent in guest from host, so we need\n    some interfaces to update the agent info in host.\n\n    You can find more information about the design of the GuestAgent in\n    the following link:\n    http://wiki.openstack.org/GuestAgent\n    http://wiki.openstack.org/GuestAgentXenStoreCommunication\n    """'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'AgentsIndexTemplate'
op|')'
newline|'\n'
DECL|member|index
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
string|'"""\n        Return a list of all agent builds. Filter by hypervisor.\n        """'
newline|'\n'
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
name|'hypervisor'
op|'='
name|'None'
newline|'\n'
name|'agents'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
string|"'hypervisor'"
name|'in'
name|'req'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'hypervisor'
op|'='
name|'req'
op|'.'
name|'GET'
op|'['
string|"'hypervisor'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'agent_build'
name|'in'
name|'db'
op|'.'
name|'agent_build_get_all'
op|'('
name|'context'
op|','
name|'hypervisor'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'agents'
op|'.'
name|'append'
op|'('
op|'{'
string|"'hypervisor'"
op|':'
name|'agent_build'
op|'.'
name|'hypervisor'
op|','
nl|'\n'
string|"'os'"
op|':'
name|'agent_build'
op|'.'
name|'os'
op|','
nl|'\n'
string|"'architecture'"
op|':'
name|'agent_build'
op|'.'
name|'architecture'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'agent_build'
op|'.'
name|'version'
op|','
nl|'\n'
string|"'md5hash'"
op|':'
name|'agent_build'
op|'.'
name|'md5hash'
op|','
nl|'\n'
string|"'agent_id'"
op|':'
name|'agent_build'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'url'"
op|':'
name|'agent_build'
op|'.'
name|'url'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'agents'"
op|':'
name|'agents'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
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
string|'"""Update an existing agent build."""'
newline|'\n'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'para'
op|'='
name|'body'
op|'['
string|"'para'"
op|']'
newline|'\n'
name|'url'
op|'='
name|'para'
op|'['
string|"'url'"
op|']'
newline|'\n'
name|'md5hash'
op|'='
name|'para'
op|'['
string|"'md5hash'"
op|']'
newline|'\n'
name|'version'
op|'='
name|'para'
op|'['
string|"'version'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'agent_build_update'
op|'('
name|'context'
op|','
name|'id'
op|','
nl|'\n'
op|'{'
string|"'version'"
op|':'
name|'version'
op|','
nl|'\n'
string|"'url'"
op|':'
name|'url'
op|','
nl|'\n'
string|"'md5hash'"
op|':'
name|'md5hash'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentBuildNotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|'"agent"'
op|':'
op|'{'
string|"'agent_id'"
op|':'
name|'id'
op|','
string|"'version'"
op|':'
name|'version'
op|','
nl|'\n'
string|"'url'"
op|':'
name|'url'
op|','
string|"'md5hash'"
op|':'
name|'md5hash'
op|'}'
op|'}'
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
string|'"""Deletes an existing agent build."""'
newline|'\n'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'agent_build_destroy'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentBuildNotFound'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
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
string|'"""Creates a new agent build."""'
newline|'\n'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'agent'
op|'='
name|'body'
op|'['
string|"'agent'"
op|']'
newline|'\n'
name|'hypervisor'
op|'='
name|'agent'
op|'['
string|"'hypervisor'"
op|']'
newline|'\n'
name|'os'
op|'='
name|'agent'
op|'['
string|"'os'"
op|']'
newline|'\n'
name|'architecture'
op|'='
name|'agent'
op|'['
string|"'architecture'"
op|']'
newline|'\n'
name|'version'
op|'='
name|'agent'
op|'['
string|"'version'"
op|']'
newline|'\n'
name|'url'
op|'='
name|'agent'
op|'['
string|"'url'"
op|']'
newline|'\n'
name|'md5hash'
op|'='
name|'agent'
op|'['
string|"'md5hash'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'agent_build_ref'
op|'='
name|'db'
op|'.'
name|'agent_build_create'
op|'('
name|'context'
op|','
nl|'\n'
op|'{'
string|"'hypervisor'"
op|':'
name|'hypervisor'
op|','
nl|'\n'
string|"'os'"
op|':'
name|'os'
op|','
nl|'\n'
string|"'architecture'"
op|':'
name|'architecture'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'version'
op|','
nl|'\n'
string|"'url'"
op|':'
name|'url'
op|','
nl|'\n'
string|"'md5hash'"
op|':'
name|'md5hash'
op|'}'
op|')'
newline|'\n'
name|'agent'
op|'['
string|"'agent_id'"
op|']'
op|'='
name|'agent_build_ref'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPServerError'
op|'('
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'agent'"
op|':'
name|'agent'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Agents
dedent|''
dedent|''
name|'class'
name|'Agents'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Agents support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Agents"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/agents/api/v3"'
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
name|'resource'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'AgentController'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'return'
name|'resource'
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
string|'"""It\'s an abstract function V3APIExtensionBase and the extension\n        will not be loaded without it.\n        """'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
