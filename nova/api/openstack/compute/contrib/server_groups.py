begin_unit
comment|'# Copyright (c) 2014 Cisco Systems, Inc.'
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
string|'"""The Server Group API Extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
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
name|'common'
newline|'\n'
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
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance_group'
name|'as'
name|'instance_group_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
comment|"# NOTE(russellb) There is one other policy, 'legacy', but we don't allow that"
nl|'\n'
comment|"# being set via the API.  It's only used when a group gets automatically"
nl|'\n'
comment|"# created to support the legacy behavior of the 'group' scheduler hint."
nl|'\n'
DECL|variable|SUPPORTED_POLICIES
name|'SUPPORTED_POLICIES'
op|'='
op|'['
string|"'anti-affinity'"
op|','
string|"'affinity'"
op|']'
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
string|"'server_groups'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_policy
name|'def'
name|'make_policy'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'text'
op|'='
name|'str'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_member
dedent|''
name|'def'
name|'make_member'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'text'
op|'='
name|'str'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_group
dedent|''
name|'def'
name|'make_group'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'policies'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'policies'"
op|')'
newline|'\n'
name|'policy'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'policies'
op|','
string|"'policy'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'policies'"
op|')'
newline|'\n'
name|'make_policy'
op|'('
name|'policy'
op|')'
newline|'\n'
name|'members'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'members'"
op|')'
newline|'\n'
name|'member'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'members'
op|','
string|"'member'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'members'"
op|')'
newline|'\n'
name|'make_member'
op|'('
name|'member'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'append'
op|'('
name|'common'
op|'.'
name|'MetadataTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|server_group_nsmap
dedent|''
name|'server_group_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_authorize_context
name|'def'
name|'_authorize_context'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'return'
name|'context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupTemplate
dedent|''
name|'class'
name|'ServerGroupTemplate'
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
string|"'server_group'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'server_group'"
op|')'
newline|'\n'
name|'make_group'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'server_group_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupsTemplate
dedent|''
dedent|''
name|'class'
name|'ServerGroupsTemplate'
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
string|"'server_groups'"
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
string|"'server_group'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'server_groups'"
op|')'
newline|'\n'
comment|'# Note: listing server groups only shows name and uuid'
nl|'\n'
name|'make_group'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
name|'server_group_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupXMLDeserializer
dedent|''
dedent|''
name|'class'
name|'ServerGroupXMLDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deserializer to handle xml-formatted server group requests."""'
newline|'\n'
nl|'\n'
DECL|variable|metadata_deserializer
name|'metadata_deserializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deserialize an xml-formatted server group create request."""'
newline|'\n'
name|'dom'
op|'='
name|'xmlutil'
op|'.'
name|'safe_minidom_parse_string'
op|'('
name|'string'
op|')'
newline|'\n'
name|'server_group'
op|'='
name|'self'
op|'.'
name|'_extract_server_group'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'server_group'"
op|':'
name|'server_group'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_extract_server_group
dedent|''
name|'def'
name|'_extract_server_group'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the instance attribute of a parsed request."""'
newline|'\n'
name|'server_group'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sg_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'server_group'"
op|')'
newline|'\n'
name|'if'
name|'sg_node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'sg_node'
op|'.'
name|'hasAttribute'
op|'('
string|"'name'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'server_group'
op|'['
string|"'name'"
op|']'
op|'='
name|'sg_node'
op|'.'
name|'getAttribute'
op|'('
string|"'name'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'sg_node'
op|'.'
name|'hasAttribute'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'server_group'
op|'['
string|"'id'"
op|']'
op|'='
name|'sg_node'
op|'.'
name|'getAttribute'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'policies'
op|'='
name|'self'
op|'.'
name|'_extract_policies'
op|'('
name|'sg_node'
op|')'
newline|'\n'
name|'server_group'
op|'['
string|"'policies'"
op|']'
op|'='
name|'policies'
name|'or'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'server_group'
newline|'\n'
nl|'\n'
DECL|member|_extract_policies
dedent|''
name|'def'
name|'_extract_policies'
op|'('
name|'self'
op|','
name|'server_group_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the server group policies element of a parsed request."""'
newline|'\n'
name|'policies_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'server_group_node'
op|','
nl|'\n'
string|"'policies'"
op|')'
newline|'\n'
name|'if'
name|'policies_node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'policy_nodes'
op|'='
name|'self'
op|'.'
name|'find_children_named'
op|'('
name|'policies_node'
op|','
nl|'\n'
string|"'policy'"
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'policy_nodes'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'node'
name|'in'
name|'policy_nodes'
op|':'
newline|'\n'
indent|'                    '
name|'policies'
op|'.'
name|'append'
op|'('
name|'node'
op|'.'
name|'firstChild'
op|'.'
name|'nodeValue'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'policies'
newline|'\n'
nl|'\n'
DECL|member|_extract_members
dedent|''
dedent|''
name|'def'
name|'_extract_members'
op|'('
name|'self'
op|','
name|'server_group_node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the server group members element of a parsed request."""'
newline|'\n'
name|'members_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'server_group_node'
op|','
nl|'\n'
string|"'members'"
op|')'
newline|'\n'
name|'if'
name|'members_node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'member_nodes'
op|'='
name|'self'
op|'.'
name|'find_children_named'
op|'('
name|'members_node'
op|','
nl|'\n'
string|"'member'"
op|')'
newline|'\n'
nl|'\n'
name|'members'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'member_nodes'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'node'
name|'in'
name|'member_nodes'
op|':'
newline|'\n'
indent|'                    '
name|'members'
op|'.'
name|'append'
op|'('
name|'node'
op|'.'
name|'firstChild'
op|'.'
name|'nodeValue'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'members'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupController
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServerGroupController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Server group API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|_format_server_group
name|'def'
name|'_format_server_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
comment|'# the id field has its value as the uuid of the server group'
nl|'\n'
comment|"# There is no 'uuid' key in server_group seen by clients."
nl|'\n'
comment|'# In addition, clients see policies as a ["policy-name"] list;'
nl|'\n'
comment|'# and they see members as a ["server-id"] list.'
nl|'\n'
indent|'        '
name|'server_group'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'server_group'
op|'['
string|"'id'"
op|']'
op|'='
name|'group'
op|'.'
name|'uuid'
newline|'\n'
name|'server_group'
op|'['
string|"'name'"
op|']'
op|'='
name|'group'
op|'.'
name|'name'
newline|'\n'
name|'server_group'
op|'['
string|"'policies'"
op|']'
op|'='
name|'group'
op|'.'
name|'policies'
name|'or'
op|'['
op|']'
newline|'\n'
name|'server_group'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'group'
op|'.'
name|'metadetails'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'members'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'group'
op|'.'
name|'members'
op|':'
newline|'\n'
comment|'# Display the instances that are not deleted.'
nl|'\n'
indent|'            '
name|'filters'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'group'
op|'.'
name|'members'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'instances'
op|'='
name|'instance_obj'
op|'.'
name|'InstanceList'
op|'.'
name|'get_by_filters'
op|'('
nl|'\n'
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'members'
op|'='
op|'['
name|'instance'
op|'.'
name|'uuid'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|']'
newline|'\n'
dedent|''
name|'server_group'
op|'['
string|"'members'"
op|']'
op|'='
name|'members'
newline|'\n'
name|'return'
name|'server_group'
newline|'\n'
nl|'\n'
DECL|member|_validate_policies
dedent|''
name|'def'
name|'_validate_policies'
op|'('
name|'self'
op|','
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Validate the policies.\n\n        Validates that there are no contradicting policies, for example\n        \'anti-affinity\' and \'affinity\' in the same group.\n        Validates that the defined policies are supported.\n        :param policies:     the given policies of the server_group\n        """'
newline|'\n'
name|'if'
op|'('
string|"'anti-affinity'"
name|'in'
name|'policies'
name|'and'
nl|'\n'
string|"'affinity'"
name|'in'
name|'policies'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Conflicting policies configured!"'
op|')'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'not_supported'
op|'='
op|'['
name|'policy'
name|'for'
name|'policy'
name|'in'
name|'policies'
nl|'\n'
name|'if'
name|'policy'
name|'not'
name|'in'
name|'SUPPORTED_POLICIES'
op|']'
newline|'\n'
name|'if'
name|'not_supported'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid policies: %s"'
op|')'
op|'%'
string|"', '"
op|'.'
name|'join'
op|'('
name|'not_supported'
op|')'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_input_body
dedent|''
dedent|''
name|'def'
name|'_validate_input_body'
op|'('
name|'self'
op|','
name|'body'
op|','
name|'entity_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
name|'entity_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"the body is invalid."'
op|')'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'subbody'
op|'='
name|'dict'
op|'('
name|'body'
op|'['
name|'entity_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'expected_fields'
op|'='
op|'['
string|"'name'"
op|','
string|"'policies'"
op|']'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'expected_fields'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'subbody'
op|'.'
name|'pop'
op|'('
name|'field'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"\'%s\' is either missing or empty."'
op|')'
op|'%'
name|'field'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'field'
op|'=='
string|"'name'"
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'value'
op|','
name|'field'
op|','
nl|'\n'
name|'min_length'
op|'='
number|'1'
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'common'
op|'.'
name|'VALID_NAME_REGEX'
op|'.'
name|'search'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid format for name: \'%s\'"'
op|')'
op|'%'
name|'value'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'field'
op|'=='
string|"'policies'"
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                    '
op|'['
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'v'
op|','
name|'field'
op|','
nl|'\n'
name|'min_length'
op|'='
number|'1'
op|','
name|'max_length'
op|'='
number|'255'
op|')'
name|'for'
name|'v'
name|'in'
name|'value'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_validate_policies'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"\'%s\' is not a list"'
op|')'
op|'%'
name|'value'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'subbody'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"unsupported fields: %s"'
op|')'
op|'%'
name|'subbody'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ServerGroupTemplate'
op|')'
newline|'\n'
DECL|member|show
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
string|'"""Return data about the given server group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sg'
op|'='
name|'instance_group_obj'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
name|'as'
name|'e'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'server_group'"
op|':'
name|'self'
op|'.'
name|'_format_server_group'
op|'('
name|'context'
op|','
name|'sg'
op|')'
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
string|'"""Delete an server group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sg'
op|'='
name|'instance_group_obj'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'sg'
op|'.'
name|'destroy'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
name|'as'
name|'e'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'204'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ServerGroupsTemplate'
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
string|'"""Returns a list of server groups."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'if'
string|"'all_projects'"
name|'in'
name|'req'
op|'.'
name|'GET'
name|'and'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'sgs'
op|'='
name|'instance_group_obj'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sgs'
op|'='
name|'instance_group_obj'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_by_project_id'
op|'('
nl|'\n'
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'sgs'
op|'.'
name|'objects'
op|','
name|'req'
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
name|'self'
op|'.'
name|'_format_server_group'
op|'('
name|'context'
op|','
name|'group'
op|')'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'server_groups'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ServerGroupTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'ServerGroupXMLDeserializer'
op|')'
newline|'\n'
DECL|member|create
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
string|'"""Creates a new server group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_validate_input_body'
op|'('
name|'body'
op|','
string|"'server_group'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vals'
op|'='
name|'body'
op|'['
string|"'server_group'"
op|']'
newline|'\n'
name|'sg'
op|'='
name|'instance_group_obj'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'sg'
op|'.'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'sg'
op|'.'
name|'user_id'
op|'='
name|'context'
op|'.'
name|'user_id'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sg'
op|'.'
name|'name'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'sg'
op|'.'
name|'policies'
op|'='
name|'vals'
op|'.'
name|'get'
op|'('
string|"'policies'"
op|')'
newline|'\n'
name|'sg'
op|'.'
name|'create'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'server_group'"
op|':'
name|'self'
op|'.'
name|'_format_server_group'
op|'('
name|'context'
op|','
name|'sg'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerGroupsTemplateElement
dedent|''
dedent|''
name|'class'
name|'ServerGroupsTemplateElement'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|')'
op|':'
newline|'\n'
DECL|member|will_render
indent|'    '
name|'def'
name|'will_render'
op|'('
name|'self'
op|','
name|'datum'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"server_groups"'
name|'in'
name|'datum'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Server_groups
dedent|''
dedent|''
name|'class'
name|'Server_groups'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server group support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ServerGroups"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-server-groups"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"servergroups/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-06-20T00:00:00Z"'
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
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-server-groups'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'ServerGroupController'
op|'('
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
nl|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
