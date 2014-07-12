begin_unit
comment|'# Copyright 2014 OpenStack Foundation'
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
name|'hooks'
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
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
nl|'\n'
nl|'\n'
op|'@'
name|'hooks'
op|'.'
name|'add_hook'
op|'('
string|"'instance_network_info'"
op|')'
newline|'\n'
DECL|function|update_instance_cache_with_nw_info
name|'def'
name|'update_instance_cache_with_nw_info'
op|'('
name|'impl'
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
name|'update_cells'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'nw_info'
op|','
name|'network_model'
op|'.'
name|'NetworkInfo'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'nw_info'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'nw_info'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'nw_info'
op|'='
name|'impl'
op|'.'
name|'_get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Updating cache with info: %s'"
op|','
name|'nw_info'
op|')'
newline|'\n'
comment|'# NOTE(comstud): The save() method actually handles updating or'
nl|'\n'
comment|"# creating the instance.  We don't need to retrieve the object"
nl|'\n'
comment|'# from the DB first.'
nl|'\n'
name|'ic'
op|'='
name|'objects'
op|'.'
name|'InstanceInfoCache'
op|'.'
name|'new'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'ic'
op|'.'
name|'network_info'
op|'='
name|'nw_info'
newline|'\n'
name|'ic'
op|'.'
name|'save'
op|'('
name|'update_cells'
op|'='
name|'update_cells'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed storing info cache'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|refresh_cache
dedent|''
dedent|''
dedent|''
name|'def'
name|'refresh_cache'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator to update the instance_info_cache\n\n    Requires context and instance as function args\n    """'
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
dedent|''
name|'update_instance_cache_with_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'nw_info'
op|'='
name|'res'
op|')'
newline|'\n'
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
DECL|variable|SENTINEL
dedent|''
name|'SENTINEL'
op|'='
name|'object'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkAPI
name|'class'
name|'NetworkAPI'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Network API for doing networking operations.\n    New operations available on specific clients must be added here as well.\n    """'
newline|'\n'
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
name|'super'
op|'('
name|'NetworkAPI'
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
string|'"""Get all the networks for client."""'
newline|'\n'
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
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get specific network for client."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Create a network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Delete a specific network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Disassociate a network for client."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get fixed ip by id."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get fixed ip by address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get floating ip by id."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get floating ip pools."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get floating ip by address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get floating ips by project."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get floating ips by fixed address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
indent|'        '
string|'"""Get instance id by floating address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get vifs by instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get vif mac address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Adds (allocate) floating ip to a project from a pool."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Removes (deallocates) a floating ip with address from a project."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Associates a floating ip with a fixed ip."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'vpn'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'macs'
op|'='
name|'None'
op|','
nl|'\n'
name|'security_groups'
op|'='
name|'None'
op|','
nl|'\n'
name|'dhcp_options'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocates all network structures for an instance.\n\n        :param context: The request context.\n        :param instance: An Instance dict.\n        :param vpn: A boolean, if True, indicate a vpn to access the instance.\n        :param requested_networks: A dictionary of requested_networks,\n            Optional value containing network_id, fixed_ip, and port_id.\n        :param macs: None or a set of MAC addresses that the instance\n            should use. macs is supplied by the hypervisor driver (contrast\n            with requested_networks which is user supplied).\n        :param security_groups: None or security groups to allocate for\n            instance.\n        :param dhcp_options: None or a set of key/value pairs that should\n            determine the DHCP BOOTP response, eg. for PXE booting an instance\n            configured with the baremetal hypervisor. It is expected that these\n            are already formatted for the neutron v2 api.\n            See nova/virt/driver.py:dhcp_options_for_instance for an example.\n        :returns: network info as from get_instance_nw_info() below\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
nl|'\n'
name|'requested_networks'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocates all network structures related to instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_port_for_instance
dedent|''
name|'def'
name|'allocate_port_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'port_id'
op|','
nl|'\n'
name|'network_id'
op|'='
name|'None'
op|','
name|'requested_ip'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocate port for instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_port_for_instance
dedent|''
name|'def'
name|'deallocate_port_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'port_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocate port for instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_ports
dedent|''
name|'def'
name|'list_ports'
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
string|'"""List ports."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_port
dedent|''
name|'def'
name|'show_port'
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
string|'"""Show specific port."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate
dedent|''
name|'def'
name|'associate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|','
name|'host'
op|'='
name|'SENTINEL'
op|','
nl|'\n'
name|'project'
op|'='
name|'SENTINEL'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associate or disassociate host or project to network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all network info related to an instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
op|','
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""validate the networks passed at the time of creating\n        the server.\n\n        Return the number of instances that can be successfully allocated\n        with the requested network configuration.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Create specified DNS entry for address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Create specified DNS entry for address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get entries for address and domain."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Get entries for name and domain."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'raise'
name|'NotImplementedError'
op|'('
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
string|'"""Setup or teardown the network structures on hosts related to\n           instance.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_instance_start
dedent|''
name|'def'
name|'migrate_instance_start'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'migration'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start to migrate the network of an instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_instance_finish
dedent|''
name|'def'
name|'migrate_instance_finish'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'migration'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Finish migrating the network of an instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
