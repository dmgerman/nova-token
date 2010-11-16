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
string|'"""\nMethods for API calls to control instances via AMQP.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reboot
name|'def'
name|'reboot'
op|'('
name|'instance_id'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Reboot the given instance."""'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"reboot_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rescue
dedent|''
name|'def'
name|'rescue'
op|'('
name|'instance_id'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Rescue the given instance."""'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"rescue_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unrescue
dedent|''
name|'def'
name|'unrescue'
op|'('
name|'instance_id'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unrescue the given instance."""'
newline|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get_by_internal_id'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"unrescue_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"instance_id"'
op|':'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
