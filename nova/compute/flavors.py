begin_unit
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
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
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
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
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
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'pci_request'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|flavor_opts
name|'flavor_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_flavor'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'m1.small'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default flavor to use for the EC2 API only. The Nova API '"
nl|'\n'
string|"'does not support a default flavor.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'flavor_opts'
op|')'
newline|'\n'
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
comment|'# NOTE(luisg): Flavor names can include non-ascii characters so that users can'
nl|'\n'
comment|'# create flavor names in locales that use them, however flavor IDs are limited'
nl|'\n'
comment|'# to ascii characters.'
nl|'\n'
DECL|variable|VALID_ID_REGEX
name|'VALID_ID_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^[\\w\\.\\- ]*$"'
op|')'
newline|'\n'
DECL|variable|VALID_NAME_REGEX
name|'VALID_NAME_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^[\\w\\.\\- ]*$"'
op|','
name|'re'
op|'.'
name|'UNICODE'
op|')'
newline|'\n'
comment|'# NOTE(dosaboy): This is supposed to represent the maximum value that we can'
nl|'\n'
comment|'# place into a SQL single precision float so that we can check whether values'
nl|'\n'
comment|'# are oversize. Postgres and MySQL both define this as their max whereas Sqlite'
nl|'\n'
comment|'# uses dynamic typing so this would not apply. Different dbs react in different'
nl|'\n'
comment|'# ways to oversize values e.g. postgres will raise an exception while mysql'
nl|'\n'
comment|'# will round off the value. Nevertheless we may still want to know prior to'
nl|'\n'
comment|'# insert whether the value is oversize.'
nl|'\n'
DECL|variable|SQL_SP_FLOAT_MAX
name|'SQL_SP_FLOAT_MAX'
op|'='
number|'3.40282e+38'
newline|'\n'
nl|'\n'
comment|'# Validate extra specs key names.'
nl|'\n'
DECL|variable|VALID_EXTRASPEC_NAME_REGEX
name|'VALID_EXTRASPEC_NAME_REGEX'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"[\\w\\.\\- :]+$"'
op|','
name|'re'
op|'.'
name|'UNICODE'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_int_or_none
name|'def'
name|'_int_or_none'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'val'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'val'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|system_metadata_flavor_props
dedent|''
dedent|''
name|'system_metadata_flavor_props'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
name|'float'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
name|'_int_or_none'
op|','
nl|'\n'
op|'}'
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
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
name|'None'
op|','
nl|'\n'
name|'swap'
op|'='
number|'0'
op|','
name|'rxtx_factor'
op|'='
number|'1.0'
op|','
name|'is_public'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates flavors."""'
newline|'\n'
name|'if'
name|'not'
name|'flavorid'
op|':'
newline|'\n'
indent|'        '
name|'flavorid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
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
name|'if'
name|'isinstance'
op|'('
name|'name'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
name|'name'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
comment|'# ensure name do not exceed 255 characters'
nl|'\n'
dedent|''
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'name'
op|','
string|"'name'"
op|','
name|'min_length'
op|'='
number|'1'
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure name does not contain any special characters'
nl|'\n'
name|'valid_name'
op|'='
name|'VALID_NAME_REGEX'
op|'.'
name|'search'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'valid_name'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Flavor names can only contain alphanumeric characters, "'
nl|'\n'
string|'"periods, dashes, underscores and spaces."'
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
comment|'# NOTE(vish): Internally, flavorid is stored as a string but it comes'
nl|'\n'
comment|'#             in through json as an integer, so we convert it here.'
nl|'\n'
dedent|''
name|'flavorid'
op|'='
name|'unicode'
op|'('
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure leading/trailing whitespaces not present.'
nl|'\n'
name|'if'
name|'flavorid'
op|'.'
name|'strip'
op|'('
op|')'
op|'!='
name|'flavorid'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"id cannot contain leading and/or trailing whitespace(s)"'
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
comment|'# ensure flavor id does not exceed 255 characters'
nl|'\n'
dedent|''
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'flavorid'
op|','
string|"'id'"
op|','
name|'min_length'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure flavor id does not contain any special characters'
nl|'\n'
name|'valid_flavor_id'
op|'='
name|'VALID_ID_REGEX'
op|'.'
name|'search'
op|'('
name|'flavorid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'valid_flavor_id'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Flavor id can only contain letters from A-Z (both cases), "'
nl|'\n'
string|'"periods, dashes, underscores and spaces."'
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
comment|'# Some attributes are positive ( > 0) integers'
nl|'\n'
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
name|'kwargs'
op|'['
name|'option'
op|']'
op|'='
name|'utils'
op|'.'
name|'validate_integer'
op|'('
name|'kwargs'
op|'['
name|'option'
op|']'
op|','
name|'option'
op|','
number|'1'
op|','
nl|'\n'
name|'db'
op|'.'
name|'MAX_INT'
op|')'
newline|'\n'
nl|'\n'
comment|'# Some attributes are non-negative ( >= 0) integers'
nl|'\n'
dedent|''
name|'for'
name|'option'
name|'in'
op|'['
string|"'root_gb'"
op|','
string|"'ephemeral_gb'"
op|','
string|"'swap'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
name|'option'
op|']'
op|'='
name|'utils'
op|'.'
name|'validate_integer'
op|'('
name|'kwargs'
op|'['
name|'option'
op|']'
op|','
name|'option'
op|','
number|'0'
op|','
nl|'\n'
name|'db'
op|'.'
name|'MAX_INT'
op|')'
newline|'\n'
nl|'\n'
comment|'# rxtx_factor should be a positive float'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
string|"'rxtx_factor'"
op|']'
op|'='
name|'float'
op|'('
name|'kwargs'
op|'['
string|"'rxtx_factor'"
op|']'
op|')'
newline|'\n'
name|'if'
op|'('
name|'kwargs'
op|'['
string|"'rxtx_factor'"
op|']'
op|'<='
number|'0'
name|'or'
nl|'\n'
name|'kwargs'
op|'['
string|"'rxtx_factor'"
op|']'
op|'>'
name|'SQL_SP_FLOAT_MAX'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"\'rxtx_factor\' argument must be a float between 0 and %g"'
op|')'
op|'%'
nl|'\n'
name|'SQL_SP_FLOAT_MAX'
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
comment|'# ensure is_public attribute is boolean'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'['
string|"'is_public'"
op|']'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
nl|'\n'
name|'is_public'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'reason'
op|'='
name|'_'
op|'('
string|'"is_public must be a boolean"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'flavor_create'
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
name|'db_exc'
op|'.'
name|'DBError'
name|'as'
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
name|'raise'
name|'exception'
op|'.'
name|'FlavorCreateFailed'
op|'('
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
string|'"""Marks flavor as deleted."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'name'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'flavor_destroy'
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
name|'ValueError'
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
name|'FlavorNotFoundByName'
op|'('
name|'flavor_name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all_flavors
dedent|''
dedent|''
name|'def'
name|'get_all_flavors'
op|'('
name|'ctxt'
op|'='
name|'None'
op|','
name|'inactive'
op|'='
name|'False'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all non-deleted flavors as a dict.\n\n    Pass true as argument if you want deleted flavors returned also.\n    """'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'inst_types'
op|'='
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'inactive'
op|'='
name|'inactive'
op|','
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
nl|'\n'
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
string|"'id'"
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
nl|'\n'
DECL|function|get_all_flavors_sorted_list
dedent|''
name|'def'
name|'get_all_flavors_sorted_list'
op|'('
name|'ctxt'
op|'='
name|'None'
op|','
name|'inactive'
op|'='
name|'False'
op|','
name|'filters'
op|'='
name|'None'
op|','
nl|'\n'
name|'sort_key'
op|'='
string|"'flavorid'"
op|','
name|'sort_dir'
op|'='
string|"'asc'"
op|','
nl|'\n'
name|'limit'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get all non-deleted flavors as a sorted list.\n\n    Pass true as argument if you want deleted flavors returned also.\n    """'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_get_all'
op|'('
name|'ctxt'
op|','
name|'filters'
op|'='
name|'filters'
op|','
name|'sort_key'
op|'='
name|'sort_key'
op|','
nl|'\n'
name|'sort_dir'
op|'='
name|'sort_dir'
op|','
name|'limit'
op|'='
name|'limit'
op|','
name|'marker'
op|'='
name|'marker'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_default_flavor
dedent|''
name|'def'
name|'get_default_flavor'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the default flavor."""'
newline|'\n'
name|'name'
op|'='
name|'CONF'
op|'.'
name|'default_flavor'
newline|'\n'
name|'return'
name|'get_flavor_by_name'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_flavor
dedent|''
name|'def'
name|'get_flavor'
op|'('
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|','
name|'inactive'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single flavor by id."""'
newline|'\n'
name|'if'
name|'instance_type_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'inactive'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'ctxt'
op|'.'
name|'elevated'
op|'('
name|'read_deleted'
op|'='
string|'"yes"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_get'
op|'('
name|'ctxt'
op|','
name|'instance_type_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_flavor_by_name
dedent|''
name|'def'
name|'get_flavor_by_name'
op|'('
name|'name'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieves single flavor by name."""'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_get_by_name'
op|'('
name|'ctxt'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): flavor-specific code should probably be in the API that uses'
nl|'\n'
comment|'#               flavors.'
nl|'\n'
DECL|function|get_flavor_by_flavor_id
dedent|''
name|'def'
name|'get_flavor_by_flavor_id'
op|'('
name|'flavorid'
op|','
name|'ctxt'
op|'='
name|'None'
op|','
name|'read_deleted'
op|'='
string|'"yes"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve flavor by flavorid.\n\n    :raises: FlavorNotFound\n    """'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
name|'read_deleted'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_get_by_flavor_id'
op|'('
name|'ctxt'
op|','
name|'flavorid'
op|','
name|'read_deleted'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_flavor_access_by_flavor_id
dedent|''
name|'def'
name|'get_flavor_access_by_flavor_id'
op|'('
name|'flavorid'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve flavor access list by flavor id."""'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_access_get_by_flavor_id'
op|'('
name|'ctxt'
op|','
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_flavor_access
dedent|''
name|'def'
name|'add_flavor_access'
op|'('
name|'flavorid'
op|','
name|'projectid'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add flavor access for project."""'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_access_add'
op|'('
name|'ctxt'
op|','
name|'flavorid'
op|','
name|'projectid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_flavor_access
dedent|''
name|'def'
name|'remove_flavor_access'
op|'('
name|'flavorid'
op|','
name|'projectid'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove flavor access for project."""'
newline|'\n'
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'flavor_access_remove'
op|'('
name|'ctxt'
op|','
name|'flavorid'
op|','
name|'projectid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_flavor
dedent|''
name|'def'
name|'extract_flavor'
op|'('
name|'instance'
op|','
name|'prefix'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an InstanceType-like object from instance\'s system_metadata\n    information.\n    """'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'type_fn'
name|'in'
name|'system_metadata_flavor_props'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'type_key'
op|'='
string|"'%sinstance_type_%s'"
op|'%'
op|'('
name|'prefix'
op|','
name|'key'
op|')'
newline|'\n'
name|'instance_type'
op|'['
name|'key'
op|']'
op|'='
name|'type_fn'
op|'('
name|'sys_meta'
op|'['
name|'type_key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|save_flavor_info
dedent|''
name|'def'
name|'save_flavor_info'
op|'('
name|'metadata'
op|','
name|'instance_type'
op|','
name|'prefix'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Save properties from instance_type into instance\'s system_metadata,\n    in the format of:\n\n      [prefix]instance_type_[key]\n\n    This can be used to update system_metadata in place from a type, as well\n    as stash information about another instance_type for later use (such as\n    during resize).\n    """'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'system_metadata_flavor_props'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'to_key'
op|'='
string|"'%sinstance_type_%s'"
op|'%'
op|'('
name|'prefix'
op|','
name|'key'
op|')'
newline|'\n'
name|'metadata'
op|'['
name|'to_key'
op|']'
op|'='
name|'instance_type'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'pci_request'
op|'.'
name|'save_flavor_pci_info'
op|'('
name|'metadata'
op|','
name|'instance_type'
op|','
name|'prefix'
op|')'
newline|'\n'
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_flavor_info
dedent|''
name|'def'
name|'delete_flavor_info'
op|'('
name|'metadata'
op|','
op|'*'
name|'prefixes'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete flavor instance_type information from instance\'s system_metadata\n    by prefix.\n    """'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'system_metadata_flavor_props'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'prefix'
name|'in'
name|'prefixes'
op|':'
newline|'\n'
indent|'            '
name|'to_key'
op|'='
string|"'%sinstance_type_%s'"
op|'%'
op|'('
name|'prefix'
op|','
name|'key'
op|')'
newline|'\n'
name|'del'
name|'metadata'
op|'['
name|'to_key'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'pci_request'
op|'.'
name|'delete_flavor_pci_info'
op|'('
name|'metadata'
op|','
op|'*'
name|'prefixes'
op|')'
newline|'\n'
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_extra_spec_keys
dedent|''
name|'def'
name|'validate_extra_spec_keys'
op|'('
name|'key_names_list'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'key_name'
name|'in'
name|'key_names_list'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'VALID_EXTRASPEC_NAME_REGEX'
op|'.'
name|'match'
op|'('
name|'key_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Key Names can only contain alphanumeric characters, '"
nl|'\n'
string|"'periods, dashes, underscores, colons and spaces.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'message'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
