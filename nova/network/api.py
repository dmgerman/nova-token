begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""Handles all requests relating to instances (guest vms)."""'
newline|'\n'
nl|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the network manager."""'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a floating ip to a project."""'
newline|'\n'
comment|"# NOTE(vish): We don't know which network host should get the ip"
nl|'\n'
comment|'#             when we allocate, so just send it to any one.  This'
nl|'\n'
comment|'#             will probably need to move into a network supervisor'
nl|'\n'
comment|'#             at some point.'
nl|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'allocate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_floating_ip
dedent|''
name|'def'
name|'release_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes floating ip with address from a project."""'
newline|'\n'
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'affect_auto_assigned'
name|'and'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'auto_assigned'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|"# NOTE(vish): We don't know which network host should get the ip"
nl|'\n'
comment|'#             when we deallocate, so just send it to any one.  This'
nl|'\n'
comment|'#             will probably need to move into a network supervisor'
nl|'\n'
comment|'#             at some point.'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'deallocate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'floating_address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_floating_ip
dedent|''
name|'def'
name|'associate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates a floating ip with a fixed ip.\n\n        ensures floating ip is allocated to the project in context\n\n        :param fixed_ip: is either fixed_ip object or a string fixed ip address\n        :param floating_ip: is a string floating ip address\n        """'
newline|'\n'
comment|'# NOTE(tr3buchet): i don\'t like the "either or" argument type'
nl|'\n'
comment|"# funcationility but i've left it alone for now"
nl|'\n'
comment|'# TODO(tr3buchet): this function needs to be rewritten to move'
nl|'\n'
comment|'# the network related db lookups into the network host code'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'fixed_ip'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'floating_ip'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'affect_auto_assigned'
name|'and'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'auto_assigned'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|'# Check if the floating ip address is allocated'
nl|'\n'
dedent|''
name|'if'
name|'floating_ip'
op|'['
string|"'project_id'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|"'Address (%s) is not allocated'"
op|')'
op|'%'
nl|'\n'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
comment|'# Check if the floating ip address is allocated to the same project'
nl|'\n'
dedent|''
name|'if'
name|'floating_ip'
op|'['
string|"'project_id'"
op|']'
op|'!='
name|'context'
op|'.'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Address (%(address)s) is not allocated to your '"
nl|'\n'
string|"'project (%(project)s)'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|"'Address (%(address)s) is not '"
nl|'\n'
string|"'allocated to your project'"
nl|'\n'
string|"'(%(project)s)'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'fixed_ip'
op|'['
string|"'network'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'associate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'floating_address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'fixed_address'"
op|':'
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_floating_ip
dedent|''
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociates a floating ip from fixed ip it is associated with."""'
newline|'\n'
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'affect_auto_assigned'
name|'and'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'auto_assigned'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
string|"'Address is not associated.'"
op|')'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'floating_ip'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'disassociate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'floating_address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_for_instance
dedent|''
name|'def'
name|'allocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocates all network structures for an instance.\n\n        :returns: network info as from get_instance_nw_info() below\n        """'
newline|'\n'
name|'args'
op|'='
name|'kwargs'
newline|'\n'
name|'args'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'args'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'args'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'allocate_for_instance'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_for_instance
dedent|''
name|'def'
name|'deallocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocates all network structures related to instance."""'
newline|'\n'
name|'args'
op|'='
name|'kwargs'
newline|'\n'
name|'args'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'args'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'deallocate_for_instance'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_fixed_ip_to_instance
dedent|''
name|'def'
name|'add_fixed_ip_to_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a fixed ip to instance from specified network."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_id'
op|'}'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'add_fixed_ip_to_instance'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_network_to_project
dedent|''
name|'def'
name|'add_network_to_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Force adds another network to a project."""'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'add_network_to_project'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'project_id'"
op|':'
name|'project_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_nw_info
dedent|''
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all network info related to an instance."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
op|'}'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'get_instance_nw_info'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
