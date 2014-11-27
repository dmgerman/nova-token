begin_unit
comment|'# Copyright 2014 IBM Corporation.  All rights reserved.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
nl|'\n'
DECL|variable|create
name|'create'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'volume'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'volume_type'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'object'"
op|'}'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'size'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'integer'"
op|','
string|"'string'"
op|']'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[0-9]+$'"
op|','
nl|'\n'
string|"'minimum'"
op|':'
number|'1'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'display_name'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'display_description'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'volume'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|snapshot_create
name|'snapshot_create'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'snapshot'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'force'"
op|':'
name|'parameter_types'
op|'.'
name|'boolean'
op|','
nl|'\n'
string|"'display_name'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'display_description'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'snapshot'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|create_volume_attachment
name|'create_volume_attachment'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'volumeAttachment'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'volumeId'"
op|':'
name|'parameter_types'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|"'device'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
comment|'# NOTE: The validation pattern from match_device() in'
nl|'\n'
comment|'#       nova/block_device.py.'
nl|'\n'
string|"'pattern'"
op|':'
string|"'(^/dev/x{0,1}[a-z]{0,1}d{0,1})([a-z]+)[0-9]*$'"
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'volumeId'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'volumeAttachment'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|update_volume_attachment
name|'update_volume_attachment'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'create_volume_attachment'
op|')'
newline|'\n'
name|'del'
name|'update_volume_attachment'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'volumeAttachment'"
op|']'
op|'['
nl|'\n'
string|"'properties'"
op|']'
op|'['
string|"'device'"
op|']'
newline|'\n'
endmarker|''
end_unit
