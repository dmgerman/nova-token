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
nl|'\n'
DECL|function|ec2_id_to_id
name|'def'
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an ec2 ID (i-[base 16 number]) to an instance id (int)"""'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'ec2_id'
op|'.'
name|'split'
op|'('
string|"'-'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|','
number|'16'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_id
dedent|''
name|'def'
name|'id_to_ec2_id'
op|'('
name|'instance_id'
op|','
name|'template'
op|'='
string|"'i-%08x'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an instance ID (int) to an ec2 ID (i-[base 16 number])"""'
newline|'\n'
name|'return'
name|'template'
op|'%'
name|'instance_id'
newline|'\n'
dedent|''
endmarker|''
end_unit
