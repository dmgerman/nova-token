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
string|'"""\nThe built-in instance properties.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|INSTANCE_TYPES
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'local_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_by_type
name|'def'
name|'get_by_type'
op|'('
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build instance data structure and save it to the data store."""'
newline|'\n'
name|'if'
name|'instance_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
dedent|''
name|'if'
name|'instance_type'
name|'not'
name|'in'
name|'INSTANCE_TYPES'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Unknown instance type: %s"'
op|')'
op|'%'
op|'('
name|'instance_type'
op|')'
op|','
nl|'\n'
string|'"Invalid"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_by_flavor_id
dedent|''
name|'def'
name|'get_by_flavor_id'
op|'('
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'instance_type'
op|','
name|'details'
name|'in'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'details'
op|'['
string|"'flavorid'"
op|']'
op|'=='
name|'flavor_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance_type'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'FLAGS'
op|'.'
name|'default_instance_type'
newline|'\n'
dedent|''
endmarker|''
end_unit
