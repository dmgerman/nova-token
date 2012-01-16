begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
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
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_all_networks'"
op|'}'
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
name|'fixed_range'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_network'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'network_uuid'"
op|':'
name|'network_uuid'
op|'}'
op|'}'
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
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'delete_network'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'fixed_range'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'network_uuid'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate
dedent|''
name|'def'
name|'disassociate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'disassociate_network'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'network_uuid'"
op|':'
name|'network_uuid'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip
dedent|''
name|'def'
name|'get_fixed_ip'
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
string|"'get_fixed_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip
dedent|''
name|'def'
name|'get_floating_ip'
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
string|"'get_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip_pools
dedent|''
name|'def'
name|'get_floating_ip_pools'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_floating_pools'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip_by_address
dedent|''
name|'def'
name|'get_floating_ip_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_floating_ip_by_address'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'address'"
op|':'
name|'address'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_project
dedent|''
name|'def'
name|'get_floating_ips_by_project'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_floating_ips_by_project'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_floating_ips_by_fixed_address'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'fixed_address'"
op|':'
name|'fixed_address'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vifs_by_instance
dedent|''
name|'def'
name|'get_vifs_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get_vifs_by_instance'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
name|'instance_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
dedent|''
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a floating ip to a project from a pool. (allocates)"""'
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
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'pool'
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
string|'"""Removes floating ip with address from a project. (deallocates)"""'
newline|'\n'
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
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'affect_auto_assigned'"
op|':'
name|'affect_auto_assigned'
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
name|'floating_address'
op|','
name|'fixed_address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associates a floating ip with a fixed ip.\n\n        ensures floating ip is allocated to the project in context\n        """'
newline|'\n'
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
string|"'associate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'floating_address'"
op|':'
name|'floating_address'
op|','
nl|'\n'
string|"'fixed_address'"
op|':'
name|'fixed_address'
op|','
nl|'\n'
string|"'affect_auto_assigned'"
op|':'
name|'affect_auto_assigned'
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
string|"'disassociate_floating_ip'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'address'"
op|':'
name|'address'
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
string|"'instance_uuid'"
op|']'
op|'='
name|'instance'
op|'['
string|"'uuid'"
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
string|"'host'"
op|']'
op|'='
name|'instance'
op|'['
string|"'host'"
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
nl|'\n'
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
name|'host'
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
string|"'host'"
op|':'
name|'host'
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
DECL|member|remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'remove_fixed_ip_from_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a fixed ip from instance from specified network."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address'
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
string|"'remove_fixed_ip_from_instance'"
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
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
name|'instance'
op|'['
string|"'instance_type_id'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'instance'
op|'['
string|"'host'"
op|']'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
comment|'# FIXME(comstud) rpc calls raise RemoteError if the remote raises'
nl|'\n'
comment|'# an exception.  In the case here, because of a race condition,'
nl|'\n'
comment|"# it's possible the remote will raise a InstanceNotFound when"
nl|'\n'
comment|'# someone deletes the instance while this call is in progress.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# Unfortunately, we don't have access to the original exception"
nl|'\n'
comment|"# class now.. but we do have the exception class's name.  So,"
nl|'\n'
comment|"# we're checking it here and raising a new exception."
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Ultimately we need RPC to be able to serialize more things like'
nl|'\n'
comment|'# classes.'
nl|'\n'
dedent|''
name|'except'
name|'rpc_common'
op|'.'
name|'RemoteError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'err'
op|'.'
name|'exc_type'
op|'=='
string|"'InstanceNotFound'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|validate_networks
dedent|''
dedent|''
name|'def'
name|'validate_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'requested_networks'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""validate the networks passed at the time of creating\n        the server\n        """'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'networks'"
op|':'
name|'requested_networks'
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
string|"'validate_networks'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_uuids_by_ip_filter
dedent|''
name|'def'
name|'get_instance_uuids_by_ip_filter'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of dicts in the form of\n        {\'instance_uuid\': uuid, \'ip\': ip} that matched the ip_filter\n        """'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'filters'"
op|':'
name|'filters'
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
string|"'get_instance_uuids_by_ip_filter'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_zones
dedent|''
name|'def'
name|'get_dns_zones'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of available dns zones.\n        These can be used to create DNS entries for floating ips.\n        """'
newline|'\n'
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
string|"'get_dns_zones'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_dns_entry
dedent|''
name|'def'
name|'add_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'name'
op|','
name|'dns_type'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create specified DNS entry for address"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'dns_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'dns_type'"
op|':'
name|'dns_type'
op|','
nl|'\n'
string|"'dns_zone'"
op|':'
name|'zone'
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
string|"'add_dns_entry'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_dns_entry
dedent|''
name|'def'
name|'modify_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'address'
op|','
name|'dns_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create specified DNS entry for address"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'dns_name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'dns_zone'"
op|':'
name|'dns_zone'
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
string|"'modify_dns_entry'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_entry
dedent|''
name|'def'
name|'delete_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the specified dns entry."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'dns_name'"
op|':'
name|'name'
op|','
string|"'dns_zone'"
op|':'
name|'zone'
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
string|"'delete_dns_entry'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_address
dedent|''
name|'def'
name|'get_dns_entries_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for address and zone"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'dns_zone'"
op|':'
name|'zone'
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
string|"'get_dns_entries_by_address'"
op|','
nl|'\n'
string|"'args'"
op|':'
name|'args'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_name
dedent|''
name|'def'
name|'get_dns_entries_by_name'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for name and zone"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'dns_zone'"
op|':'
name|'zone'
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
string|"'get_dns_entries_by_name'"
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
