begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Piston Cloud Computing, Inc.'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
nl|'\n'
comment|'# Copyright 2013 Nicira, Inc.'
nl|'\n'
comment|'# All Rights Reserved'
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
comment|'#'
nl|'\n'
comment|'# @author: Aaron Rosen, Nicira Networks, Inc.'
nl|'\n'
nl|'\n'
name|'import'
name|'urllib'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SecurityGroupBase
name|'class'
name|'SecurityGroupBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|parse_cidr
indent|'    '
name|'def'
name|'parse_cidr'
op|'('
name|'self'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'cidr'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cidr'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'cidr'
op|')'
op|'.'
name|'decode'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'raise_invalid_cidr'
op|'('
name|'cidr'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'utils'
op|'.'
name|'is_valid_cidr'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'raise_invalid_cidr'
op|'('
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cidr'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'0.0.0.0/0'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|new_group_ingress_rule
name|'def'
name|'new_group_ingress_rule'
op|'('
name|'grantee_group_id'
op|','
name|'protocol'
op|','
name|'from_port'
op|','
nl|'\n'
name|'to_port'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'SecurityGroupBase'
op|'.'
name|'_new_ingress_rule'
op|'('
nl|'\n'
name|'protocol'
op|','
name|'from_port'
op|','
name|'to_port'
op|','
name|'group_id'
op|'='
name|'grantee_group_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|new_cidr_ingress_rule
name|'def'
name|'new_cidr_ingress_rule'
op|'('
name|'grantee_cidr'
op|','
name|'protocol'
op|','
name|'from_port'
op|','
name|'to_port'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'SecurityGroupBase'
op|'.'
name|'_new_ingress_rule'
op|'('
nl|'\n'
name|'protocol'
op|','
name|'from_port'
op|','
name|'to_port'
op|','
name|'cidr'
op|'='
name|'grantee_cidr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_new_ingress_rule
name|'def'
name|'_new_ingress_rule'
op|'('
name|'ip_protocol'
op|','
name|'from_port'
op|','
name|'to_port'
op|','
nl|'\n'
name|'group_id'
op|'='
name|'None'
op|','
name|'cidr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'group_id'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'group_id'"
op|']'
op|'='
name|'group_id'
newline|'\n'
comment|'# Open everything if an explicit port range or type/code are not'
nl|'\n'
comment|'# specified, but only if a source group was specified.'
nl|'\n'
name|'ip_proto_upper'
op|'='
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
name|'if'
name|'ip_protocol'
name|'else'
string|"''"
newline|'\n'
name|'if'
op|'('
name|'ip_proto_upper'
op|'=='
string|"'ICMP'"
name|'and'
nl|'\n'
name|'from_port'
name|'is'
name|'None'
name|'and'
name|'to_port'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'from_port'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'to_port'
op|'='
op|'-'
number|'1'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'ip_proto_upper'
name|'in'
op|'['
string|"'TCP'"
op|','
string|"'UDP'"
op|']'
name|'and'
name|'from_port'
name|'is'
name|'None'
nl|'\n'
name|'and'
name|'to_port'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'from_port'
op|'='
number|'1'
newline|'\n'
name|'to_port'
op|'='
number|'65535'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'cidr'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'['
string|"'cidr'"
op|']'
op|'='
name|'cidr'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ip_protocol'
name|'and'
name|'from_port'
name|'is'
name|'not'
name|'None'
name|'and'
name|'to_port'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'ip_protocol'
op|'='
name|'str'
op|'('
name|'ip_protocol'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Verify integer conversions'
nl|'\n'
indent|'                '
name|'from_port'
op|'='
name|'int'
op|'('
name|'from_port'
op|')'
newline|'\n'
name|'to_port'
op|'='
name|'int'
op|'('
name|'to_port'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
op|'=='
string|"'ICMP'"
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
string|'"Type and"'
nl|'\n'
string|'" Code must be integers for ICMP protocol type"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
string|'"To and From ports "'
nl|'\n'
string|'"must be integers"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
name|'not'
name|'in'
op|'['
string|"'TCP'"
op|','
string|"'UDP'"
op|','
string|"'ICMP'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidIpProtocol'
op|'('
name|'protocol'
op|'='
name|'ip_protocol'
op|')'
newline|'\n'
nl|'\n'
comment|'# Verify that from_port must always be less than'
nl|'\n'
comment|'# or equal to to_port'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
name|'in'
op|'['
string|"'TCP'"
op|','
string|"'UDP'"
op|']'
name|'and'
nl|'\n'
op|'('
name|'from_port'
op|'>'
name|'to_port'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidPortRange'
op|'('
name|'from_port'
op|'='
name|'from_port'
op|','
nl|'\n'
name|'to_port'
op|'='
name|'to_port'
op|','
name|'msg'
op|'='
string|'"Former value cannot"'
nl|'\n'
string|'" be greater than the later"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Verify valid TCP, UDP port ranges'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
name|'in'
op|'['
string|"'TCP'"
op|','
string|"'UDP'"
op|']'
name|'and'
nl|'\n'
op|'('
name|'from_port'
op|'<'
number|'1'
name|'or'
name|'to_port'
op|'>'
number|'65535'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidPortRange'
op|'('
name|'from_port'
op|'='
name|'from_port'
op|','
nl|'\n'
name|'to_port'
op|'='
name|'to_port'
op|','
name|'msg'
op|'='
string|'"Valid TCP ports should"'
nl|'\n'
string|'" be between 1-65535"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Verify ICMP type and code'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'ip_protocol'
op|'.'
name|'upper'
op|'('
op|')'
op|'=='
string|'"ICMP"'
name|'and'
nl|'\n'
op|'('
name|'from_port'
op|'<'
op|'-'
number|'1'
name|'or'
name|'from_port'
op|'>'
number|'255'
name|'or'
nl|'\n'
name|'to_port'
op|'<'
op|'-'
number|'1'
name|'or'
name|'to_port'
op|'>'
number|'255'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InvalidPortRange'
op|'('
name|'from_port'
op|'='
name|'from_port'
op|','
nl|'\n'
name|'to_port'
op|'='
name|'to_port'
op|','
name|'msg'
op|'='
string|'"For ICMP, the"'
nl|'\n'
string|'" type:code must be valid"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'values'
op|'['
string|"'protocol'"
op|']'
op|'='
name|'ip_protocol'
newline|'\n'
name|'values'
op|'['
string|"'from_port'"
op|']'
op|'='
name|'from_port'
newline|'\n'
name|'values'
op|'['
string|"'to_port'"
op|']'
op|'='
name|'to_port'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# If cidr based filtering, protocol and ports are mandatory'
nl|'\n'
indent|'            '
name|'if'
name|'cidr'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'values'
newline|'\n'
nl|'\n'
DECL|member|create_security_group_rule
dedent|''
name|'def'
name|'create_security_group_rule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|','
name|'new_rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'rule_exists'
op|'('
name|'security_group'
op|','
name|'new_rule'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'This rule already exists in group %s'"
op|')'
op|'%'
nl|'\n'
name|'new_rule'
op|'['
string|"'parent_group_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'raise_group_already_exists'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'add_rules'
op|'('
name|'context'
op|','
name|'new_rule'
op|'['
string|"'parent_group_id'"
op|']'
op|','
nl|'\n'
name|'security_group'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
op|'['
name|'new_rule'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|rule_exists
dedent|''
name|'def'
name|'rule_exists'
op|'('
name|'self'
op|','
name|'security_group'
op|','
name|'new_rule'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Indicates whether the specified rule is already\n           defined in the given security group.\n        """'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'security_group'
op|'['
string|"'rules'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'is_duplicate'
op|'='
name|'True'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'group_id'"
op|','
string|"'cidr'"
op|','
string|"'from_port'"
op|','
string|"'to_port'"
op|','
string|"'protocol'"
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'rule'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|'!='
name|'new_rule'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'is_duplicate'
op|'='
name|'False'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'is_duplicate'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'rule'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
name|'or'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|validate_property
dedent|''
name|'def'
name|'validate_property'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'property'
op|','
name|'allowed'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|ensure_default
dedent|''
name|'def'
name|'ensure_default'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_handler
dedent|''
name|'def'
name|'trigger_handler'
op|'('
name|'self'
op|','
name|'event'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_rules_refresh
dedent|''
name|'def'
name|'trigger_rules_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when a rule is added to or removed from a security_group."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|trigger_members_refresh
dedent|''
name|'def'
name|'trigger_members_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when a security group gains a new or loses a member.\n\n        Sends an update request to each compute node for each instance for\n        which this is relevant.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|populate_security_groups
dedent|''
name|'def'
name|'populate_security_groups'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'security_groups'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called when populating the database for an instances\n        security groups.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_security_group
dedent|''
name|'def'
name|'create_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_security_group
dedent|''
name|'def'
name|'update_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|','
nl|'\n'
name|'name'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|'='
name|'None'
op|','
name|'id'
op|'='
name|'None'
op|','
name|'map_exception'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|list
dedent|''
name|'def'
name|'list'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'names'
op|'='
name|'None'
op|','
name|'ids'
op|'='
name|'None'
op|','
name|'project'
op|'='
name|'None'
op|','
nl|'\n'
name|'search_opts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_rules
dedent|''
name|'def'
name|'add_rules'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|','
name|'name'
op|','
name|'vals'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_rules
dedent|''
name|'def'
name|'remove_rules'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'security_group'
op|','
name|'rule_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_rule
dedent|''
name|'def'
name|'get_rule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_security_groups
dedent|''
name|'def'
name|'get_instance_security_groups'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_to_instance
dedent|''
name|'def'
name|'add_to_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_instance
dedent|''
name|'def'
name|'remove_from_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'security_group_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'NotImplementedError'
op|'('
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
name|'NotImplementedError'
op|'('
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
name|'NotImplementedError'
op|'('
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
name|'NotImplementedError'
op|'('
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
name|'NotImplementedError'
op|'('
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
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
