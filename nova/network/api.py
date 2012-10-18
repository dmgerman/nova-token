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
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'rpcapi'
name|'as'
name|'network_rpcapi'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|refresh_cache
name|'def'
name|'refresh_cache'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Decorator to update the instance_info_cache\n\n    Requires context and instance as function args\n    """'
newline|'\n'
name|'argspec'
op|'='
name|'inspect'
op|'.'
name|'getargspec'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'f'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
name|'context'
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
name|'res'
op|'='
name|'f'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# get the instance from arguments (or raise ValueError)'
nl|'\n'
indent|'            '
name|'instance'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'instance'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'='
name|'args'
op|'['
name|'argspec'
op|'.'
name|'args'
op|'.'
name|'index'
op|'('
string|"'instance'"
op|')'
op|'-'
number|'2'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'instance is a required argument to use @refresh_cache'"
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# get nw_info from return if possible, otherwise call for it'
nl|'\n'
dedent|''
name|'nw_info'
op|'='
name|'res'
name|'if'
name|'isinstance'
op|'('
name|'res'
op|','
name|'network_model'
op|'.'
name|'NetworkInfo'
op|')'
name|'else'
name|'None'
newline|'\n'
nl|'\n'
name|'update_instance_cache_with_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'nw_info'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|"# return the original function's return value"
nl|'\n'
name|'return'
name|'res'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_instance_cache_with_nw_info
dedent|''
name|'def'
name|'update_instance_cache_with_nw_info'
op|'('
name|'api'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'nw_info'
op|'='
name|'None'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'nw_info'
name|'or'
name|'api'
op|'.'
name|'_get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# update cache'
nl|'\n'
name|'cache'
op|'='
op|'{'
string|"'network_info'"
op|':'
name|'nw_info'
op|'.'
name|'json'
op|'('
op|')'
op|'}'
newline|'\n'
name|'api'
op|'.'
name|'db'
op|'.'
name|'instance_info_cache_update'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'cache'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
string|"'Failed storing info cache'"
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'args: %s'"
op|')'
op|'%'
op|'('
name|'args'
name|'or'
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'kwargs: %s'"
op|')'
op|'%'
op|'('
name|'kwargs'
name|'or'
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
dedent|''
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
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_rpcapi'
op|'='
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_all_networks'
op|'('
name|'context'
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
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_network'
op|'('
name|'context'
op|','
name|'network_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'create_networks'
op|'('
name|'context'
op|','
op|'**'
name|'kwargs'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'delete_network'
op|'('
name|'context'
op|','
name|'network_uuid'
op|','
name|'None'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'disassociate_network'
op|'('
name|'context'
op|','
name|'network_uuid'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_fixed_ip'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip_by_address
dedent|''
name|'def'
name|'get_fixed_ip_by_address'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_fixed_ip_by_address'
op|'('
name|'context'
op|','
name|'address'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_floating_ip'
op|'('
name|'context'
op|','
name|'id'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_floating_pools'
op|'('
name|'context'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_floating_ip_by_address'
op|'('
name|'context'
op|','
name|'address'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_floating_ips_by_project'
op|'('
name|'context'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'fixed_address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_id_by_floating_address
dedent|''
name|'def'
name|'get_instance_id_by_floating_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(tr3buchet): i hate this'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_instance_id_by_floating_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'address'
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
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_vifs_by_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vif_by_mac_address
dedent|''
name|'def'
name|'get_vif_by_mac_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_vif_by_mac_address'
op|'('
name|'context'
op|','
name|'mac_address'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|','
name|'pool'
op|','
name|'False'
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
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'deallocate_floating_ip'
op|'('
name|'context'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|associate_floating_ip
name|'def'
name|'associate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
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
name|'orig_instance_uuid'
op|'='
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'associate_floating_ip'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_address'
op|','
name|'fixed_address'
op|','
name|'affect_auto_assigned'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'orig_instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'msg_dict'
op|'='
name|'dict'
op|'('
name|'address'
op|'='
name|'floating_address'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'orig_instance_uuid'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'re-assign floating IP %(address)s from '"
nl|'\n'
string|"'instance %(instance_id)s'"
op|')'
op|'%'
name|'msg_dict'
op|')'
newline|'\n'
name|'orig_instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
nl|'\n'
name|'orig_instance_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|'# purge cached nw info for the original instance'
nl|'\n'
name|'update_instance_cache_with_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'orig_instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|disassociate_floating_ip
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
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
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'disassociate_floating_ip'
op|'('
name|'context'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|allocate_for_instance
name|'def'
name|'allocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'vpn'
op|','
nl|'\n'
name|'requested_networks'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocates all network structures for an instance.\n\n        :returns: network info as from get_instance_nw_info() below\n        """'
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'['
string|"'vpn'"
op|']'
op|'='
name|'vpn'
newline|'\n'
name|'args'
op|'['
string|"'requested_networks'"
op|']'
op|'='
name|'requested_networks'
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
string|"'rxtx_factor'"
op|']'
op|'='
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'rxtx_factor'"
op|']'
newline|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'allocate_for_instance'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'nw_info'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocates all network structures related to instance."""'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
op|'}'
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
string|"'host'"
op|']'
op|'='
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'deallocate_for_instance'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'instance'
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
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_id'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'add_fixed_ip_to_instance'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'instance'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a fixed ip from instance from specified network."""'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'instance_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'remove_fixed_ip_from_instance'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
op|','
name|'network_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Force adds another network to a project."""'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'add_network_to_project'
op|'('
name|'context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'network_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|get_instance_nw_info
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
name|'return'
name|'self'
op|'.'
name|'_get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_nw_info
dedent|''
name|'def'
name|'_get_instance_nw_info'
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
string|"'rxtx_factor'"
op|':'
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'rxtx_factor'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|'}'
newline|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate_networks
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
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'validate_networks'
op|'('
name|'context'
op|','
nl|'\n'
name|'requested_networks'
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
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_instance_uuids_by_ip_filter'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_domains
dedent|''
name|'def'
name|'get_dns_domains'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of available dns domains.\n        These can be used to create DNS entries for floating ips.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_dns_domains'
op|'('
name|'context'
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
name|'domain'
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
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'dns_type'"
op|':'
name|'dns_type'
op|','
nl|'\n'
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'add_dns_entry'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'domain'
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
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'modify_dns_entry'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the specified dns entry."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'delete_dns_entry'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_domain
dedent|''
name|'def'
name|'delete_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the specified dns domain."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'delete_dns_domain'
op|'('
name|'context'
op|','
name|'domain'
op|'='
name|'domain'
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
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for address and domain"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_dns_entries_by_address'
op|'('
name|'context'
op|','
op|'**'
name|'args'
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
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for name and domain"""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'get_dns_entries_by_name'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_private_dns_domain
dedent|''
name|'def'
name|'create_private_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|','
name|'availability_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a private DNS domain with nova availability zone."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'domain'
op|','
string|"'av_zone'"
op|':'
name|'availability_zone'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'create_private_dns_domain'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_public_dns_domain
dedent|''
name|'def'
name|'create_public_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|','
name|'project'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a public DNS domain with optional nova project."""'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'domain'
op|','
string|"'project'"
op|':'
name|'project'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'create_public_dns_domain'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_networks_on_host
dedent|''
name|'def'
name|'setup_networks_on_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'teardown'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup or teardown the network structures on hosts related to\n           instance"""'
newline|'\n'
name|'host'
op|'='
name|'host'
name|'or'
name|'instance'
op|'['
string|"'host'"
op|']'
newline|'\n'
comment|'# NOTE(tr3buchet): host is passed in cases where we need to setup'
nl|'\n'
comment|'# or teardown the networks on a host which has been migrated to/from'
nl|'\n'
comment|"# and instance['host'] is not yet or is no longer equal to"
nl|'\n'
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
string|"'host'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'teardown'"
op|':'
name|'teardown'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'network_rpcapi'
op|'.'
name|'setup_networks_on_host'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
