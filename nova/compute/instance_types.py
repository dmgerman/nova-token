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
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 Ken Pepple'
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
string|'"""Built-in instance properties."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
string|"'nova.instance_types'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
name|'name'
op|','
name|'memory'
op|','
name|'vcpus'
op|','
name|'root_gb'
op|','
name|'ephemeral_gb'
op|','
name|'flavorid'
op|','
name|'swap'
op|'='
name|'None'
op|','
nl|'\n'
name|'rxtx_factor'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates instance types."""'
newline|'\n'
nl|'\n'
name|'if'
name|'swap'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'swap'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'if'
name|'rxtx_factor'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'rxtx_factor'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'='
op|'{'
nl|'\n'
string|"'memory_mb'"
op|':'
name|'memory'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'root_gb'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'ephemeral_gb'
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'swap'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
name|'rxtx_factor'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# ensure some attributes are integers and greater than or equal to 0'
nl|'\n'
name|'for'
name|'option'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
name|'option'
op|']'
op|'='
name|'int'
op|'('
name|'kwargs'
op|'['
name|'option'
op|']'
op|')'
newline|'\n'
name|'assert'
name|'kwargs'
op|'['
name|'option'
op|']'
op|'>='
number|'0'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'AssertionError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"create arguments must be positive integers"'
op|')'
newline|'\n'
name|'raise'
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
comment|'# some value are required to be nonzero, not just positive'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'option'
name|'in'
op|'['
string|"'memory_mb'"
op|','
string|"'vcpus'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'assert'
name|'kwargs'
op|'['
name|'option'
op|']'
op|'>'
number|'0'
newline|'\n'
dedent|''
name|'except'
name|'AssertionError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"create arguments must be positive integers"'
op|')'
newline|'\n'
name|'raise'
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
name|'kwargs'
op|'['
string|"'name'"
op|']'
op|'='
name|'name'
newline|'\n'
name|'kwargs'
op|'['
string|"'flavorid'"
op|']'
op|'='
name|'flavorid'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_type_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'DBError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB error: %s'"
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cannot create instance_type with name %(name)s and "'
nl|'\n'
string|'"flavorid %(flavorid)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy
dedent|''
dedent|''
name|'def'
name|'destroy'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Marks instance types as deleted."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'name'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'db'
op|'.'
name|'instance_type_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AssertionError'
op|','
name|'exception'
op|'.'
name|'NotFound'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Instance type %s not found for deletion'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceTypeNotFoundByName'
op|'('
name|'instance_type_name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|purge
dedent|''
dedent|''
name|'def'
name|'purge'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Removes instance types from database."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'name'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'db'
op|'.'
name|'instance_type_purge'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AssertionError'
op|','
name|'exception'
op|'.'
name|'NotFound'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Instance type %s not found for purge'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InstanceTypeNotFoundByName'
op|'('
name|'instance_type_name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all_types
dedent|''
dedent|''
name|'def'
name|'get_all_types'
op|'('
name|'inactive'
op|'='
number|'0'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all non-deleted instance_types.\n\n    Pass true as argument if you want deleted instance types returned also.\n\n    """'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'inst_types'
op|'='
name|'db'
op|'.'
name|'instance_type_get_all'
op|'('
name|'ctxt'
op|','
name|'inactive'
op|','
name|'filters'
op|')'
newline|'\n'
name|'inst_type_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'inst_type'
name|'in'
name|'inst_types'
op|':'
newline|'\n'
indent|'        '
name|'inst_type_dict'
op|'['
name|'inst_type'
op|'['
string|"'name'"
op|']'
op|']'
op|'='
name|'inst_type'
newline|'\n'
dedent|''
name|'return'
name|'inst_type_dict'
newline|'\n'
nl|'\n'
DECL|variable|get_all_flavors
dedent|''
name|'get_all_flavors'
op|'='
name|'get_all_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_default_instance_type
name|'def'
name|'get_default_instance_type'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the default instance type."""'
newline|'\n'
name|'name'
op|'='
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_instance_type_by_name'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'e'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_type
dedent|''
dedent|''
name|'def'
name|'get_instance_type'
op|'('
name|'instance_type_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single instance type by id."""'
newline|'\n'
name|'if'
name|'instance_type_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_type_get'
op|'('
name|'ctxt'
op|','
name|'instance_type_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'e'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_type_by_name
dedent|''
dedent|''
name|'def'
name|'get_instance_type_by_name'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single instance type by name."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_type_get_by_name'
op|'('
name|'ctxt'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'e'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): flavor-specific code should probably be in the API that uses'
nl|'\n'
comment|'#               flavors.'
nl|'\n'
DECL|function|get_instance_type_by_flavor_id
dedent|''
dedent|''
name|'def'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavorid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve instance type by flavorid.\n\n    :raises: FlavorNotFound\n    """'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_type_get_by_flavor_id'
op|'('
name|'ctxt'
op|','
name|'flavorid'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
