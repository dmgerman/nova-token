begin_unit
comment|'# Copyright 2012 Red Hat, Inc.'
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
string|'"""Possible vm modes for instances.\n\nCompute instance vm modes represent the host/guest ABI used for the\nvirtual machine / container. Individual hypervisors may support\nmultiple different vm modes per host. Available vm modes for a hypervisor\ndriver may also vary according to the architecture it is running on.\n\nThe \'vm_mode\' parameter can be set against an instance to\nchoose what sort of VM to boot.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|HVM
name|'HVM'
op|'='
string|'"hvm"'
comment|'# Native ABI (aka fully virtualized)'
newline|'\n'
DECL|variable|XEN
name|'XEN'
op|'='
string|'"xen"'
comment|'# Xen 3.0 paravirtualized'
newline|'\n'
DECL|variable|UML
name|'UML'
op|'='
string|'"uml"'
comment|'# User Mode Linux paravirtualized'
newline|'\n'
DECL|variable|EXE
name|'EXE'
op|'='
string|'"exe"'
comment|'# Executables in containers'
newline|'\n'
nl|'\n'
DECL|variable|ALL
name|'ALL'
op|'='
op|'['
name|'HVM'
op|','
name|'XEN'
op|','
name|'UML'
op|','
name|'EXE'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_from_instance
name|'def'
name|'get_from_instance'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the vm mode for an instance\n\n    :param instance: instance object to query\n\n    :returns: canonicalized vm mode for the instance\n    """'
newline|'\n'
nl|'\n'
name|'mode'
op|'='
name|'instance'
op|'.'
name|'vm_mode'
newline|'\n'
name|'return'
name|'canonicalize'
op|'('
name|'mode'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid
dedent|''
name|'def'
name|'is_valid'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if a string is a valid vm mode\n\n    :param name: vm mode name to validate\n\n    :returns: True if @name is valid\n    """'
newline|'\n'
nl|'\n'
name|'return'
name|'name'
name|'in'
name|'ALL'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|canonicalize
dedent|''
name|'def'
name|'canonicalize'
op|'('
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Canonicalize the vm mode\n\n    :param name: vm mode name to canonicalize\n\n    :returns: a canonical vm mode name\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'mode'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'mode'
op|'='
name|'mode'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# For compatibility with pre-Folsom deployments'
nl|'\n'
name|'if'
name|'mode'
op|'=='
string|'"pv"'
op|':'
newline|'\n'
indent|'        '
name|'mode'
op|'='
name|'XEN'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'mode'
op|'=='
string|'"hv"'
op|':'
newline|'\n'
indent|'        '
name|'mode'
op|'='
name|'HVM'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'mode'
op|'=='
string|'"baremetal"'
op|':'
newline|'\n'
indent|'        '
name|'mode'
op|'='
name|'HVM'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'is_valid'
op|'('
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVirtualMachineMode'
op|'('
name|'vmmode'
op|'='
name|'mode'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'mode'
newline|'\n'
dedent|''
endmarker|''
end_unit
