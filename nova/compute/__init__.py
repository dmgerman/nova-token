begin_unit
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
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
comment|'# Importing full names to not pollute the namespace and cause possible'
nl|'\n'
comment|"# collisions with use of 'from nova.compute import <foo>' elsewhere."
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'opts'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CELL_TYPE_TO_CLS_NAME
name|'CELL_TYPE_TO_CLS_NAME'
op|'='
op|'{'
string|"'api'"
op|':'
string|"'nova.compute.cells_api.ComputeCellsAPI'"
op|','
nl|'\n'
string|"'compute'"
op|':'
string|"'nova.compute.api.API'"
op|','
nl|'\n'
name|'None'
op|':'
string|"'nova.compute.api.API'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_compute_api_class_name
name|'def'
name|'_get_compute_api_class_name'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the name of compute API class."""'
newline|'\n'
name|'cell_type'
op|'='
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'opts'
op|'.'
name|'get_cell_type'
op|'('
op|')'
newline|'\n'
name|'return'
name|'CELL_TYPE_TO_CLS_NAME'
op|'['
name|'cell_type'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|API
dedent|''
name|'def'
name|'API'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'class_name'
op|'='
name|'_get_compute_api_class_name'
op|'('
op|')'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'class_name'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|HostAPI
dedent|''
name|'def'
name|'HostAPI'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the \'HostAPI\' class from the same module as the configured\n    compute api\n    """'
newline|'\n'
name|'compute_api_class_name'
op|'='
name|'_get_compute_api_class_name'
op|'('
op|')'
newline|'\n'
name|'compute_api_class'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'compute_api_class_name'
op|')'
newline|'\n'
name|'class_name'
op|'='
name|'compute_api_class'
op|'.'
name|'__module__'
op|'+'
string|'".HostAPI"'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'class_name'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|InstanceActionAPI
dedent|''
name|'def'
name|'InstanceActionAPI'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the \'InstanceActionAPI\' class from the same module as the\n    configured compute api.\n    """'
newline|'\n'
name|'compute_api_class_name'
op|'='
name|'_get_compute_api_class_name'
op|'('
op|')'
newline|'\n'
name|'compute_api_class'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'compute_api_class_name'
op|')'
newline|'\n'
name|'class_name'
op|'='
name|'compute_api_class'
op|'.'
name|'__module__'
op|'+'
string|'".InstanceActionAPI"'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'class_name'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
