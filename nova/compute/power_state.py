begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""The various power states that a VM can be in."""'
newline|'\n'
nl|'\n'
comment|'#NOTE(justinsb): These are the virDomainState values from libvirt'
nl|'\n'
DECL|variable|NOSTATE
name|'NOSTATE'
op|'='
number|'0x00'
newline|'\n'
DECL|variable|RUNNING
name|'RUNNING'
op|'='
number|'0x01'
newline|'\n'
DECL|variable|BLOCKED
name|'BLOCKED'
op|'='
number|'0x02'
newline|'\n'
DECL|variable|PAUSED
name|'PAUSED'
op|'='
number|'0x03'
newline|'\n'
DECL|variable|SHUTDOWN
name|'SHUTDOWN'
op|'='
number|'0x04'
newline|'\n'
DECL|variable|SHUTOFF
name|'SHUTOFF'
op|'='
number|'0x05'
newline|'\n'
DECL|variable|CRASHED
name|'CRASHED'
op|'='
number|'0x06'
newline|'\n'
DECL|variable|SUSPENDED
name|'SUSPENDED'
op|'='
number|'0x07'
newline|'\n'
DECL|variable|FAILED
name|'FAILED'
op|'='
number|'0x08'
newline|'\n'
nl|'\n'
comment|'# TODO(justinsb): Power state really needs to be a proper class,'
nl|'\n'
comment|"# so that we're not locked into the libvirt status codes and can put mapping"
nl|'\n'
comment|'# logic here rather than spread throughout the code'
nl|'\n'
DECL|variable|_STATE_MAP
name|'_STATE_MAP'
op|'='
op|'{'
nl|'\n'
name|'NOSTATE'
op|':'
string|"'pending'"
op|','
nl|'\n'
name|'RUNNING'
op|':'
string|"'running'"
op|','
nl|'\n'
name|'BLOCKED'
op|':'
string|"'blocked'"
op|','
nl|'\n'
name|'PAUSED'
op|':'
string|"'paused'"
op|','
nl|'\n'
name|'SHUTDOWN'
op|':'
string|"'shutdown'"
op|','
nl|'\n'
name|'SHUTOFF'
op|':'
string|"'shutdown'"
op|','
nl|'\n'
name|'CRASHED'
op|':'
string|"'crashed'"
op|','
nl|'\n'
name|'SUSPENDED'
op|':'
string|"'suspended'"
op|','
nl|'\n'
name|'FAILED'
op|':'
string|"'failed to spawn'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|name
name|'def'
name|'name'
op|'('
name|'code'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_STATE_MAP'
op|'['
name|'code'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|valid_states
dedent|''
name|'def'
name|'valid_states'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_STATE_MAP'
op|'.'
name|'values'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
