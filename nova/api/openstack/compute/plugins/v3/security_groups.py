begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2012 Justin Santa Barbara'
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
string|'"""The security groups extension."""'
newline|'\n'
name|'import'
name|'contextlib'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
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
op|'.'
name|'compute'
op|'.'
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'security_groups'
name|'as'
name|'schema_security_groups'
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
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
op|'.'
name|'network'
op|'.'
name|'security_group'
name|'import'
name|'neutron_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
name|'import'
name|'openstack_driver'
newline|'\n'
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
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-security-groups'"
newline|'\n'
DECL|variable|ATTRIBUTE_NAME
name|'ATTRIBUTE_NAME'
op|'='
string|"'security_groups'"
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
DECL|variable|softauth
name|'softauth'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
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
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|function|translate_exceptions
name|'def'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Translate nova exceptions to http exceptions."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'yield'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Invalid'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'exp'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'raise'
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
name|'SecurityGroupNotFound'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'exp'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'raise'
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
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'exp'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'raise'
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
name|'except'
name|'exception'
op|'.'
name|'SecurityGroupLimitExceeded'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'exp'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'NoUniqueMatch'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'exp'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupControllerBase
dedent|''
dedent|''
name|'class'
name|'SecurityGroupControllerBase'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for Security Group controllers."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'security_group_api'
op|'='
op|'('
nl|'\n'
name|'openstack_driver'
op|'.'
name|'get_openstack_security_group_driver'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
nl|'\n'
name|'security_group_api'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_security_group_rule
dedent|''
name|'def'
name|'_format_security_group_rule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'rule'
op|','
name|'group_rule_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a secuity group rule in desired API response format.\n\n        If group_rule_data is passed in that is used rather than querying\n        for it.\n        """'
newline|'\n'
name|'sg_rule'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sg_rule'
op|'['
string|"'id'"
op|']'
op|'='
name|'rule'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'sg_rule'
op|'['
string|"'parent_group_id'"
op|']'
op|'='
name|'rule'
op|'['
string|"'parent_group_id'"
op|']'
newline|'\n'
name|'sg_rule'
op|'['
string|"'ip_protocol'"
op|']'
op|'='
name|'rule'
op|'['
string|"'protocol'"
op|']'
newline|'\n'
name|'sg_rule'
op|'['
string|"'from_port'"
op|']'
op|'='
name|'rule'
op|'['
string|"'from_port'"
op|']'
newline|'\n'
name|'sg_rule'
op|'['
string|"'to_port'"
op|']'
op|'='
name|'rule'
op|'['
string|"'to_port'"
op|']'
newline|'\n'
name|'sg_rule'
op|'['
string|"'group'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sg_rule'
op|'['
string|"'ip_range'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'rule'
op|'['
string|"'group_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'source_group'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'get'
op|'('
nl|'\n'
name|'context'
op|','
name|'id'
op|'='
name|'rule'
op|'['
string|"'group_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'SecurityGroupNotFound'
op|':'
newline|'\n'
comment|'# NOTE(arosen): There is a possible race condition that can'
nl|'\n'
comment|'# occur here if two api calls occur concurrently: one that'
nl|'\n'
comment|'# lists the security groups and another one that deletes a'
nl|'\n'
comment|'# security group rule that has a group_id before the'
nl|'\n'
comment|'# group_id is fetched. To handle this if'
nl|'\n'
comment|'# SecurityGroupNotFound is raised we return None instead'
nl|'\n'
comment|'# of the rule and the caller should ignore the rule.'
nl|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Security Group ID %s does not exist"'
op|','
nl|'\n'
name|'rule'
op|'['
string|"'group_id'"
op|']'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'sg_rule'
op|'['
string|"'group'"
op|']'
op|'='
op|'{'
string|"'name'"
op|':'
name|'source_group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
name|'source_group'
op|'.'
name|'get'
op|'('
string|"'project_id'"
op|')'
op|'}'
newline|'\n'
dedent|''
name|'elif'
name|'group_rule_data'
op|':'
newline|'\n'
indent|'            '
name|'sg_rule'
op|'['
string|"'group'"
op|']'
op|'='
name|'group_rule_data'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sg_rule'
op|'['
string|"'ip_range'"
op|']'
op|'='
op|'{'
string|"'cidr'"
op|':'
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'sg_rule'
newline|'\n'
nl|'\n'
DECL|member|_format_security_group
dedent|''
name|'def'
name|'_format_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'security_group'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'security_group'
op|'['
string|"'id'"
op|']'
op|'='
name|'group'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'security_group'
op|'['
string|"'description'"
op|']'
op|'='
name|'group'
op|'['
string|"'description'"
op|']'
newline|'\n'
name|'security_group'
op|'['
string|"'name'"
op|']'
op|'='
name|'group'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'security_group'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'group'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'security_group'
op|'['
string|"'rules'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'group'
op|'['
string|"'rules'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'formatted_rule'
op|'='
name|'self'
op|'.'
name|'_format_security_group_rule'
op|'('
name|'context'
op|','
name|'rule'
op|')'
newline|'\n'
name|'if'
name|'formatted_rule'
op|':'
newline|'\n'
indent|'                '
name|'security_group'
op|'['
string|"'rules'"
op|']'
op|'+='
op|'['
name|'formatted_rule'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'security_group'
newline|'\n'
nl|'\n'
DECL|member|_from_body
dedent|''
name|'def'
name|'_from_body'
op|'('
name|'self'
op|','
name|'body'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"The request body can\'t be empty"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'value'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Missing parameter %s"'
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupController
dedent|''
dedent|''
name|'class'
name|'SecurityGroupController'
op|'('
name|'SecurityGroupControllerBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Security group API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
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
string|'"""Return data about the given security group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'id'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'None'
op|','
name|'id'
op|','
nl|'\n'
name|'map_exception'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'security_group'"
op|':'
name|'self'
op|'.'
name|'_format_security_group'
op|'('
name|'context'
op|','
nl|'\n'
name|'security_group'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
DECL|member|delete
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
string|'"""Delete a security group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'id'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'None'
op|','
name|'id'
op|','
nl|'\n'
name|'map_exception'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'destroy'
op|'('
name|'context'
op|','
name|'security_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
string|'"""Returns a list of security groups."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'search_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'search_opts'
op|'.'
name|'update'
op|'('
name|'req'
op|'.'
name|'GET'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'raw_groups'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'list'
op|'('
name|'context'
op|','
nl|'\n'
name|'project'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'search_opts'
op|'='
name|'search_opts'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'raw_groups'
op|','
name|'req'
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
name|'self'
op|'.'
name|'_format_security_group'
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
nl|'\n'
name|'return'
op|'{'
string|"'security_groups'"
op|':'
nl|'\n'
name|'list'
op|'('
name|'sorted'
op|'('
name|'result'
op|','
nl|'\n'
name|'key'
op|'='
name|'lambda'
name|'k'
op|':'
op|'('
name|'k'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'k'
op|'['
string|"'name'"
op|']'
op|')'
op|')'
op|')'
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
string|'"""Creates a new security group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'_from_body'
op|'('
name|'body'
op|','
string|"'security_group'"
op|')'
newline|'\n'
nl|'\n'
name|'group_name'
op|'='
name|'security_group'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'group_description'
op|'='
name|'security_group'
op|'.'
name|'get'
op|'('
string|"'description'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_property'
op|'('
name|'group_name'
op|','
string|"'name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_property'
op|'('
name|'group_description'
op|','
nl|'\n'
string|"'description'"
op|','
name|'None'
op|')'
newline|'\n'
name|'group_ref'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'create_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'group_name'
op|','
name|'group_description'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'security_group'"
op|':'
name|'self'
op|'.'
name|'_format_security_group'
op|'('
name|'context'
op|','
nl|'\n'
name|'group_ref'
op|')'
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
string|'"""Update a security group."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'id'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'None'
op|','
name|'id'
op|','
nl|'\n'
name|'map_exception'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'security_group_data'
op|'='
name|'self'
op|'.'
name|'_from_body'
op|'('
name|'body'
op|','
string|"'security_group'"
op|')'
newline|'\n'
name|'group_name'
op|'='
name|'security_group_data'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'group_description'
op|'='
name|'security_group_data'
op|'.'
name|'get'
op|'('
string|"'description'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_property'
op|'('
name|'group_name'
op|','
string|"'name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'validate_property'
op|'('
name|'group_description'
op|','
nl|'\n'
string|"'description'"
op|','
name|'None'
op|')'
newline|'\n'
name|'group_ref'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'update_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'security_group'
op|','
name|'group_name'
op|','
name|'group_description'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'security_group'"
op|':'
name|'self'
op|'.'
name|'_format_security_group'
op|'('
name|'context'
op|','
nl|'\n'
name|'group_ref'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerSecurityGroupController
dedent|''
dedent|''
name|'class'
name|'ServerSecurityGroupController'
op|'('
name|'SecurityGroupControllerBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of security groups for the given instance."""'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'ensure_default'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'get_instance_security_groups'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'['
name|'self'
op|'.'
name|'_format_security_group'
op|'('
name|'context'
op|','
name|'group'
op|')'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'security_groups'"
op|':'
nl|'\n'
name|'list'
op|'('
name|'sorted'
op|'('
name|'result'
op|','
nl|'\n'
name|'key'
op|'='
name|'lambda'
name|'k'
op|':'
op|'('
name|'k'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'k'
op|'['
string|"'name'"
op|']'
op|')'
op|')'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupActionController
dedent|''
dedent|''
name|'class'
name|'SecurityGroupActionController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'SecurityGroupActionController'
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
name|'security_group_api'
op|'='
op|'('
nl|'\n'
name|'openstack_driver'
op|'.'
name|'get_openstack_security_group_driver'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
nl|'\n'
name|'security_group_api'
op|'='
name|'self'
op|'.'
name|'security_group_api'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse
dedent|''
name|'def'
name|'_parse'
op|'('
name|'self'
op|','
name|'body'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'='
name|'body'
op|'['
name|'action'
op|']'
newline|'\n'
name|'group_name'
op|'='
name|'body'
op|'['
string|"'name'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Missing parameter dict"'
op|')'
newline|'\n'
name|'raise'
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
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Security group not specified"'
op|')'
newline|'\n'
name|'raise'
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
name|'if'
name|'not'
name|'group_name'
name|'or'
name|'group_name'
op|'.'
name|'strip'
op|'('
op|')'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Security group name cannot be empty"'
op|')'
newline|'\n'
name|'raise'
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
name|'return'
name|'group_name'
newline|'\n'
nl|'\n'
DECL|member|_invoke
dedent|''
name|'def'
name|'_invoke'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'context'
op|','
name|'id'
op|','
name|'group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'translate_exceptions'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'method'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'group_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'addSecurityGroup'"
op|')'
newline|'\n'
DECL|member|_addSecurityGroup
name|'def'
name|'_addSecurityGroup'
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
name|'group_name'
op|'='
name|'self'
op|'.'
name|'_parse'
op|'('
name|'body'
op|','
string|"'addSecurityGroup'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_invoke'
op|'('
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'add_to_instance'
op|','
nl|'\n'
name|'context'
op|','
name|'id'
op|','
name|'group_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'removeSecurityGroup'"
op|')'
newline|'\n'
DECL|member|_removeSecurityGroup
name|'def'
name|'_removeSecurityGroup'
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
name|'group_name'
op|'='
name|'self'
op|'.'
name|'_parse'
op|'('
name|'body'
op|','
string|"'removeSecurityGroup'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_invoke'
op|'('
name|'self'
op|'.'
name|'security_group_api'
op|'.'
name|'remove_from_instance'
op|','
nl|'\n'
name|'context'
op|','
name|'id'
op|','
name|'group_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupsOutputController
dedent|''
dedent|''
name|'class'
name|'SecurityGroupsOutputController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'SecurityGroupsOutputController'
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
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'security_group_api'
op|'='
op|'('
nl|'\n'
name|'openstack_driver'
op|'.'
name|'get_openstack_security_group_driver'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extend_servers
dedent|''
name|'def'
name|'_extend_servers'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
comment|'# TODO(arosen) this function should be refactored to reduce duplicate'
nl|'\n'
comment|'# code and use get_instance_security_groups instead of get_db_instance.'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'len'
op|'('
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'key'
op|'='
string|'"security_groups"'
newline|'\n'
name|'context'
op|'='
name|'_authorize_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'openstack_driver'
op|'.'
name|'is_neutron_security_groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
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
name|'groups'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'groups'
op|':'
newline|'\n'
indent|'                    '
name|'server'
op|'['
name|'ATTRIBUTE_NAME'
op|']'
op|'='
op|'['
op|'{'
string|'"name"'
op|':'
name|'group'
op|'['
string|'"name"'
op|']'
op|'}'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'groups'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# If method is a POST we get the security groups intended for an'
nl|'\n'
comment|'# instance from the request. The reason for this is if using'
nl|'\n'
comment|'# neutron security groups the requested security groups for the'
nl|'\n'
comment|'# instance are not in the db and have not been sent to neutron yet.'
nl|'\n'
indent|'            '
name|'if'
name|'req'
op|'.'
name|'method'
op|'!='
string|"'POST'"
op|':'
newline|'\n'
indent|'                '
name|'sg_instance_bindings'
op|'='
op|'('
nl|'\n'
name|'self'
op|'.'
name|'security_group_api'
nl|'\n'
op|'.'
name|'get_instances_security_groups_bindings'
op|'('
name|'context'
op|','
nl|'\n'
name|'servers'
op|')'
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'                    '
name|'groups'
op|'='
name|'sg_instance_bindings'
op|'.'
name|'get'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'groups'
op|':'
newline|'\n'
indent|'                        '
name|'server'
op|'['
name|'ATTRIBUTE_NAME'
op|']'
op|'='
name|'groups'
newline|'\n'
nl|'\n'
comment|'# In this section of code len(servers) == 1 as you can only POST'
nl|'\n'
comment|'# one server in an API request.'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# try converting to json'
nl|'\n'
indent|'                '
name|'req_obj'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
newline|'\n'
comment|'# Add security group to server, if no security group was in'
nl|'\n'
comment|'# request add default since that is the group it is part of'
nl|'\n'
name|'servers'
op|'['
number|'0'
op|']'
op|'['
name|'ATTRIBUTE_NAME'
op|']'
op|'='
name|'req_obj'
op|'['
string|"'server'"
op|']'
op|'.'
name|'get'
op|'('
nl|'\n'
name|'ATTRIBUTE_NAME'
op|','
op|'['
op|'{'
string|"'name'"
op|':'
string|"'default'"
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_show
dedent|''
dedent|''
dedent|''
name|'def'
name|'_show'
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
name|'if'
name|'not'
name|'softauth'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
string|"'server'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_extend_servers'
op|'('
name|'req'
op|','
op|'['
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|']'
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
name|'return'
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'not'
name|'softauth'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_extend_servers'
op|'('
name|'req'
op|','
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroups
dedent|''
dedent|''
name|'class'
name|'SecurityGroups'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Security group support."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"SecurityGroups"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'secgrp_output_ext'
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
name|'SecurityGroupsOutputController'
op|'('
op|')'
op|')'
newline|'\n'
name|'secgrp_act_ext'
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
name|'SecurityGroupActionController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'secgrp_output_ext'
op|','
name|'secgrp_act_ext'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'secgrp_ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-security-groups'"
op|','
nl|'\n'
name|'SecurityGroupController'
op|'('
op|')'
op|')'
newline|'\n'
name|'server_secgrp_ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-security-groups'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'ServerSecurityGroupController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'server'"
op|','
name|'collection_name'
op|'='
string|"'servers'"
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'secgrp_ext'
op|','
name|'server_secgrp_ext'
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(gmann): This function is not supposed to use 'body_deprecated_param'"
nl|'\n'
comment|'# parameter as this is placed to handle scheduler_hint extension for V2.1.'
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|','
name|'body_deprecated_param'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'security_groups'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
name|'ATTRIBUTE_NAME'
op|')'
newline|'\n'
name|'if'
name|'security_groups'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'create_kwargs'
op|'['
string|"'security_group'"
op|']'
op|'='
op|'['
nl|'\n'
name|'sg'
op|'['
string|"'name'"
op|']'
name|'for'
name|'sg'
name|'in'
name|'security_groups'
name|'if'
name|'sg'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|']'
newline|'\n'
name|'create_kwargs'
op|'['
string|"'security_group'"
op|']'
op|'='
name|'list'
op|'('
nl|'\n'
name|'set'
op|'('
name|'create_kwargs'
op|'['
string|"'security_group'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_server_create_schema
dedent|''
dedent|''
name|'def'
name|'get_server_create_schema'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'schema_security_groups'
op|'.'
name|'server_create'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NativeSecurityGroupExceptions
dedent|''
dedent|''
name|'class'
name|'NativeSecurityGroupExceptions'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_invalid_property
name|'def'
name|'raise_invalid_property'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_group_already_exists
name|'def'
name|'raise_group_already_exists'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_invalid_group
name|'def'
name|'raise_invalid_group'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_invalid_cidr
name|'def'
name|'raise_invalid_cidr'
op|'('
name|'cidr'
op|','
name|'decoding_exception'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidCidr'
op|'('
name|'cidr'
op|'='
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_over_quota
name|'def'
name|'raise_over_quota'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SecurityGroupLimitExceeded'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|raise_not_found
name|'def'
name|'raise_not_found'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'SecurityGroupNotFound'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'NativeNovaSecurityGroupAPI'
op|'('
name|'NativeSecurityGroupExceptions'
op|','
nl|'\n'
DECL|class|NativeNovaSecurityGroupAPI
name|'compute_api'
op|'.'
name|'SecurityGroupAPI'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'NativeNeutronSecurityGroupAPI'
op|'('
name|'NativeSecurityGroupExceptions'
op|','
nl|'\n'
DECL|class|NativeNeutronSecurityGroupAPI
name|'neutron_driver'
op|'.'
name|'SecurityGroupAPI'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
