begin_unit
comment|'# Copyright 2013 NEC Corporation.  All rights reserved.'
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
DECL|variable|swap_volume_attachment
name|'swap_volume_attachment'
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
string|"'swap_volume_attachment'"
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
string|"'old_volume_id'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'new_volume_id'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
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
string|"'old_volume_id'"
op|','
string|"'new_volume_id'"
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
string|"'swap_volume_attachment'"
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
DECL|variable|attach
name|'attach'
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
string|"'attach'"
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
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
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
op|','
nl|'\n'
string|"'disk_bus'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'device_type'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
op|'}'
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
string|"'attach'"
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
DECL|variable|detach
name|'detach'
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
string|"'detach'"
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
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
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
string|"'detach'"
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
endmarker|''
end_unit
