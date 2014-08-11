begin_unit
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
string|"'agents'"
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
string|'"""The agent is talking about guest agent.The host can use this for\n    things like accessing files on the disk, configuring networking,\n    or running other applications/scripts in the guest while it is\n    running. Typically this uses some hypervisor-specific transport\n    to avoid being dependent on a working network configuration.\n    Xen, VMware, and VirtualBox have guest agents,although the Xen\n    driver is the only one with an implementation for managing them\n    in openstack. KVM doesn\'t really have a concept of a guest agent\n    (although one could be written).\n\n    You can find the design of agent update in this link:\n    http://wiki.openstack.org/AgentUpdate\n    and find the code in nova.virt.xenapi.vmops.VMOps._boot_new_instance.\n    In this design We need update agent in guest from host, so we need\n    some interfaces to update the agent info in host.\n\n    You can find more information about the design of the GuestAgent in\n    the following link:\n    http://wiki.openstack.org/GuestAgent\n    http://wiki.openstack.org/GuestAgentXenStoreCommunication\n    """'
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
string|'"""Return a list of all agent builds. Filter by hypervisor."""'
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
name|'builds'
op|'='
name|'objects'
op|'.'
name|'AgentList'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
name|'hypervisor'
op|'='
name|'hypervisor'
op|')'
newline|'\n'
name|'for'
name|'agent_build'
name|'in'
name|'builds'
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
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid request body: %s"'
op|')'
op|'%'
name|'unicode'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'url'
op|','
string|"'url'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'md5hash'
op|','
string|"'md5hash'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'version'
op|','
string|"'version'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'agent'
op|'='
name|'objects'
op|'.'
name|'Agent'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'id'
op|'='
name|'id'
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'version'
op|'='
name|'version'
newline|'\n'
name|'agent'
op|'.'
name|'url'
op|'='
name|'url'
newline|'\n'
name|'agent'
op|'.'
name|'md5hash'
op|'='
name|'md5hash'
newline|'\n'
name|'agent'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid request body: %s"'
op|')'
op|'%'
name|'unicode'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
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
comment|'# NOTE(alex_xu): The agent_id should be integer that consistent with'
nl|'\n'
comment|"# create/index actions. But parameter 'id' is string type that parsed"
nl|'\n'
comment|"# from url. This is a bug, but because back-compatibility, it can't be"
nl|'\n'
comment|'# fixed for v2 API. This will be fixed after v3 API feature exposed by'
nl|'\n'
comment|'# micro-version in the future. lp bug #1333494'
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
name|'agent'
op|'='
name|'objects'
op|'.'
name|'Agent'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'id'
op|'='
name|'id'
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'destroy'
op|'('
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
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid request body: %s"'
op|')'
op|'%'
name|'unicode'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'hypervisor'
op|','
string|"'hypervisor'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'os'
op|','
string|"'os'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'architecture'
op|','
string|"'architecture'"
op|','
nl|'\n'
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'version'
op|','
string|"'version'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'url'
op|','
string|"'url'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'md5hash'
op|','
string|"'md5hash'"
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'agent_obj'
op|'='
name|'objects'
op|'.'
name|'Agent'
op|'('
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'agent_obj'
op|'.'
name|'hypervisor'
op|'='
name|'hypervisor'
newline|'\n'
name|'agent_obj'
op|'.'
name|'os'
op|'='
name|'os'
newline|'\n'
name|'agent_obj'
op|'.'
name|'architecture'
op|'='
name|'architecture'
newline|'\n'
name|'agent_obj'
op|'.'
name|'version'
op|'='
name|'version'
newline|'\n'
name|'agent_obj'
op|'.'
name|'url'
op|'='
name|'url'
newline|'\n'
name|'agent_obj'
op|'.'
name|'md5hash'
op|'='
name|'md5hash'
newline|'\n'
name|'agent_obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'['
string|"'agent_id'"
op|']'
op|'='
name|'agent_obj'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentBuildExists'
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
name|'HTTPConflict'
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
name|'ExtensionDescriptor'
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
string|'"os-agents"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/agents/api/v2"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-10-28T00:00:00Z"'
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
name|'resource'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-agents'"
op|','
nl|'\n'
name|'AgentController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'resource'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
