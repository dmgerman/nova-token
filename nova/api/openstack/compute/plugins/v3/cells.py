begin_unit
comment|'# Copyright 2011-2012 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""The cells extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
name|'import'
name|'six'
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
name|'cells'
name|'import'
name|'rpcapi'
name|'as'
name|'cells_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute'
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
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
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
name|'import_opt'
op|'('
string|"'name'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'capabilities'"
op|','
string|"'nova.cells.opts'"
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-cells"'
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
nl|'\n'
nl|'\n'
DECL|function|_filter_keys
name|'def'
name|'_filter_keys'
op|'('
name|'item'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filters all model attributes except for keys\n    item is a dict\n    """'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'item'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fixup_cell_info
dedent|''
name|'def'
name|'_fixup_cell_info'
op|'('
name|'cell_info'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""If the transport_url is present in the cell, derive username,\n    rpc_host, and rpc_port from it.\n    """'
newline|'\n'
nl|'\n'
name|'if'
string|"'transport_url'"
name|'not'
name|'in'
name|'cell_info'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
comment|'# Disassemble the transport URL'
nl|'\n'
dedent|''
name|'transport_url'
op|'='
name|'cell_info'
op|'.'
name|'pop'
op|'('
string|"'transport_url'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'transport_url'
op|'='
name|'rpc'
op|'.'
name|'get_transport_url'
op|'('
name|'transport_url'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'messaging'
op|'.'
name|'InvalidTransportURL'
op|':'
newline|'\n'
comment|"# Just go with None's"
nl|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'cell_info'
op|'.'
name|'setdefault'
op|'('
name|'key'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'transport_url'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'transport_host'
op|'='
name|'transport_url'
op|'.'
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'transport_field_map'
op|'='
op|'{'
string|"'rpc_host'"
op|':'
string|"'hostname'"
op|','
string|"'rpc_port'"
op|':'
string|"'port'"
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'cell_info'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'transport_field'
op|'='
name|'transport_field_map'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'key'
op|')'
newline|'\n'
name|'cell_info'
op|'['
name|'key'
op|']'
op|'='
name|'getattr'
op|'('
name|'transport_host'
op|','
name|'transport_field'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_scrub_cell
dedent|''
dedent|''
name|'def'
name|'_scrub_cell'
op|'('
name|'cell'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'keys'
op|'='
op|'['
string|"'name'"
op|','
string|"'username'"
op|','
string|"'rpc_host'"
op|','
string|"'rpc_port'"
op|']'
newline|'\n'
name|'if'
name|'detail'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'.'
name|'append'
op|'('
string|"'capabilities'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cell_info'
op|'='
name|'_filter_keys'
op|'('
name|'cell'
op|','
name|'keys'
op|'+'
op|'['
string|"'transport_url'"
op|']'
op|')'
newline|'\n'
name|'_fixup_cell_info'
op|'('
name|'cell_info'
op|','
name|'keys'
op|')'
newline|'\n'
name|'cell_info'
op|'['
string|"'type'"
op|']'
op|'='
string|"'parent'"
name|'if'
name|'cell'
op|'['
string|"'is_parent'"
op|']'
name|'else'
string|"'child'"
newline|'\n'
name|'return'
name|'cell_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsController
dedent|''
name|'class'
name|'CellsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Controller for Cell resources."""'
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
name|'cells_rpcapi'
op|'='
name|'cells_rpcapi'
op|'.'
name|'CellsAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_cells
dedent|''
name|'def'
name|'_get_cells'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'req'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all cells."""'
newline|'\n'
comment|'# Ask the CellsManager for the most recent data'
nl|'\n'
name|'items'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'get_cell_info_for_neighbors'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'items'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
newline|'\n'
name|'items'
op|'='
op|'['
name|'_scrub_cell'
op|'('
name|'item'
op|','
name|'detail'
op|'='
name|'detail'
op|')'
name|'for'
name|'item'
name|'in'
name|'items'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'cells'
op|'='
name|'items'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'501'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
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
string|'"""Return all cells in brief."""'
newline|'\n'
name|'ctxt'
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
name|'ctxt'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_cells'
op|'('
name|'ctxt'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'501'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all cells in detail."""'
newline|'\n'
name|'ctxt'
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
name|'ctxt'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_cells'
op|'('
name|'ctxt'
op|','
name|'req'
op|','
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'501'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
DECL|member|info
name|'def'
name|'info'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return name and capabilities for this cell."""'
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
name|'cell_capabs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'my_caps'
op|'='
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'capabilities'
newline|'\n'
name|'for'
name|'cap'
name|'in'
name|'my_caps'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|','
name|'value'
op|'='
name|'cap'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'cell_capabs'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'cell'
op|'='
op|'{'
string|"'name'"
op|':'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'self'"
op|','
nl|'\n'
string|"'rpc_host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'rpc_port'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'capabilities'"
op|':'
name|'cell_capabs'
op|'}'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'cell'
op|'='
name|'cell'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
DECL|member|capacities
name|'def'
name|'capacities'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return capacities for a given cell or all cells."""'
newline|'\n'
comment|'# TODO(kaushikc): return capacities as a part of cell info and'
nl|'\n'
comment|'# cells detail calls in v3, along with capabilities'
nl|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'capacities'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'get_capacities'
op|'('
name|'context'
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'cell'
op|'='
op|'{'
string|'"capacities"'
op|':'
name|'capacities'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
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
string|'"""Return data about the given cell name.  \'id\' is a cell name."""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'cell_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'dict'
op|'('
name|'cell'
op|'='
name|'_scrub_cell'
op|'('
name|'cell'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'403'
op|','
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
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
string|'"""Delete a child or parent cell entry.  \'id\' is a cell name."""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'num_deleted'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'cell_delete'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'if'
name|'num_deleted'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Cell %s doesn\'t exist."'
op|')'
op|'%'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_cell_name
dedent|''
dedent|''
name|'def'
name|'_validate_cell_name'
op|'('
name|'self'
op|','
name|'cell_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Validate cell name is not empty and doesn\'t contain \'!\' or \'.\'."""'
newline|'\n'
name|'if'
name|'not'
name|'cell_name'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cell name cannot be empty"'
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
name|'if'
string|"'!'"
name|'in'
name|'cell_name'
name|'or'
string|"'.'"
name|'in'
name|'cell_name'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cell name cannot contain \'!\' or \'.\'"'
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
DECL|member|_validate_cell_type
dedent|''
dedent|''
name|'def'
name|'_validate_cell_type'
op|'('
name|'self'
op|','
name|'cell_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Validate cell_type is \'parent\' or \'child\'."""'
newline|'\n'
name|'if'
name|'cell_type'
name|'not'
name|'in'
op|'['
string|"'parent'"
op|','
string|"'child'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Cell type must be \'parent\' or \'child\'"'
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
DECL|member|_normalize_cell
dedent|''
dedent|''
name|'def'
name|'_normalize_cell'
op|'('
name|'self'
op|','
name|'cell'
op|','
name|'existing'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Normalize input cell data.  Normalizations include:\n\n        * Converting cell[\'type\'] to is_parent boolean.\n        * Merging existing transport URL with transport information.\n        """'
newline|'\n'
nl|'\n'
comment|'# Start with the cell type conversion'
nl|'\n'
name|'if'
string|"'type'"
name|'in'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_validate_cell_type'
op|'('
name|'cell'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
name|'cell'
op|'['
string|"'is_parent'"
op|']'
op|'='
name|'cell'
op|'['
string|"'type'"
op|']'
op|'=='
string|"'parent'"
newline|'\n'
name|'del'
name|'cell'
op|'['
string|"'type'"
op|']'
newline|'\n'
comment|"# Avoid cell type being overwritten to 'child'"
nl|'\n'
dedent|''
name|'elif'
name|'existing'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'['
string|"'is_parent'"
op|']'
op|'='
name|'existing'
op|'['
string|"'is_parent'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'['
string|"'is_parent'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
comment|'# Now we disassemble the existing transport URL...'
nl|'\n'
dedent|''
name|'transport_url'
op|'='
name|'existing'
op|'.'
name|'get'
op|'('
string|"'transport_url'"
op|')'
name|'if'
name|'existing'
name|'else'
name|'None'
newline|'\n'
name|'transport_url'
op|'='
name|'rpc'
op|'.'
name|'get_transport_url'
op|'('
name|'transport_url'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'rpc_virtual_host'"
name|'in'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'transport_url'
op|'.'
name|'virtual_host'
op|'='
name|'cell'
op|'.'
name|'pop'
op|'('
string|"'rpc_virtual_host'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'transport_url'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'transport_url'
op|'.'
name|'hosts'
op|'.'
name|'append'
op|'('
name|'messaging'
op|'.'
name|'TransportHost'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'transport_host'
op|'='
name|'transport_url'
op|'.'
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Copy over the input fields'
nl|'\n'
name|'transport_field_map'
op|'='
op|'{'
nl|'\n'
string|"'username'"
op|':'
string|"'username'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'password'"
op|','
nl|'\n'
string|"'hostname'"
op|':'
string|"'rpc_host'"
op|','
nl|'\n'
string|"'port'"
op|':'
string|"'rpc_port'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'input_field'
name|'in'
name|'transport_field_map'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|"# Only override the value if we're given an override"
nl|'\n'
indent|'            '
name|'if'
name|'input_field'
name|'in'
name|'cell'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'transport_host'
op|','
name|'key'
op|','
name|'cell'
op|'.'
name|'pop'
op|'('
name|'input_field'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now set the transport URL'
nl|'\n'
dedent|''
dedent|''
name|'cell'
op|'['
string|"'transport_url'"
op|']'
op|'='
name|'str'
op|'('
name|'transport_url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'201'
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
string|'"""Create a child cell entry."""'
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
name|'if'
string|"'cell'"
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No cell information in request"'
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
name|'cell'
op|'='
name|'body'
op|'['
string|"'cell'"
op|']'
newline|'\n'
name|'if'
string|"'name'"
name|'not'
name|'in'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No cell name in request"'
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
name|'self'
op|'.'
name|'_validate_cell_name'
op|'('
name|'cell'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_normalize_cell'
op|'('
name|'cell'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'cell_create'
op|'('
name|'context'
op|','
name|'cell'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'dict'
op|'('
name|'cell'
op|'='
name|'_scrub_cell'
op|'('
name|'cell'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
DECL|member|update
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
string|'"""Update a child cell entry.  \'id\' is the cell name to update."""'
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
name|'if'
string|"'cell'"
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No cell information in request"'
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
name|'cell'
op|'='
name|'body'
op|'['
string|"'cell'"
op|']'
newline|'\n'
name|'cell'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
string|"'name'"
name|'in'
name|'cell'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_validate_cell_name'
op|'('
name|'cell'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(Vek): There is a race condition here if multiple'
nl|'\n'
comment|'#            callers are trying to update the cell'
nl|'\n'
comment|'#            information simultaneously.  Since this'
nl|'\n'
comment|'#            operation is administrative in nature, and'
nl|'\n'
comment|"#            will be going away in the future, I don't see"
nl|'\n'
comment|'#            it as much of a problem...'
nl|'\n'
indent|'            '
name|'existing'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'cell_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'self'
op|'.'
name|'_normalize_cell'
op|'('
name|'cell'
op|','
name|'existing'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cell'
op|'='
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'cell_update'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'cell'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'CellNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'except'
name|'exception'
op|'.'
name|'CellsUpdateUnsupported'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'dict'
op|'('
name|'cell'
op|'='
name|'_scrub_cell'
op|'('
name|'cell'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
op|'@'
name|'common'
op|'.'
name|'check_cells_enabled'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
op|')'
newline|'\n'
DECL|member|sync_instances
name|'def'
name|'sync_instances'
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
string|'"""Tell all cells to sync instance info."""'
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
name|'project_id'
op|'='
name|'body'
op|'.'
name|'pop'
op|'('
string|"'project_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'deleted'
op|'='
name|'body'
op|'.'
name|'pop'
op|'('
string|"'deleted'"
op|','
name|'False'
op|')'
newline|'\n'
name|'updated_since'
op|'='
name|'body'
op|'.'
name|'pop'
op|'('
string|"'updated_since'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Only \'updated_since\', \'project_id\' and \'deleted\' are "'
nl|'\n'
string|'"understood."'
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
name|'if'
name|'isinstance'
op|'('
name|'deleted'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'deleted'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'deleted'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'str'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'updated_since'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'updated_since'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid changes-since value'"
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
dedent|''
name|'self'
op|'.'
name|'cells_rpcapi'
op|'.'
name|'sync_instances'
op|'('
name|'context'
op|','
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'updated_since'
op|'='
name|'updated_since'
op|','
name|'deleted'
op|'='
name|'deleted'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Cells
dedent|''
dedent|''
name|'class'
name|'Cells'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Enables cells-related functionality such as adding neighbor cells,\n    listing neighbor cells, and getting the capabilities of the local cell.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Cells"'
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
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'coll_actions'
op|'='
op|'{'
nl|'\n'
string|"'detail'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'info'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'sync_instances'"
op|':'
string|"'POST'"
op|','
nl|'\n'
string|"'capacities'"
op|':'
string|"'GET'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'memb_actions'
op|'='
op|'{'
nl|'\n'
string|"'capacities'"
op|':'
string|"'GET'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
name|'CellsController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
name|'coll_actions'
op|','
nl|'\n'
name|'member_actions'
op|'='
name|'memb_actions'
op|')'
newline|'\n'
name|'return'
op|'['
name|'res'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
