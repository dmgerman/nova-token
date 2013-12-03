begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
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
string|"'agent'"
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
string|"'hypervisor'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._ ]*$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'os'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._ ]*$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'architecture'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._ ]*$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'version'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._ ]*$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'url'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uri'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'md5hash'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-fA-F0-9]*$'"
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
string|"'hypervisor'"
op|','
string|"'os'"
op|','
string|"'architecture'"
op|','
string|"'version'"
op|','
nl|'\n'
string|"'url'"
op|','
string|"'md5hash'"
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
string|"'agent'"
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
DECL|variable|update
name|'update'
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
string|"'agent'"
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
string|"'version'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._ ]*$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'url'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uri'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'md5hash'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-fA-F0-9]*$'"
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
string|"'version'"
op|','
string|"'url'"
op|','
string|"'md5hash'"
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
string|"'agent'"
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
