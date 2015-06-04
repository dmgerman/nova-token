begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
string|'"""Constants and helper APIs for dealing with virtualization types\n\nThe constants provide the standard names for all known guest\nvirtualization types. This is not to be confused with the Nova\nhypervisor driver types, since one driver may support multiple\nvirtualization types and one virtualization type (eg \'xen\') may\nbe supported by multiple drivers (\'XenAPI\' or  \'Libvirt-Xen\').\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# This list is all known hypervisors'
nl|'\n'
comment|'# even if not currently supported by OpenStack.'
nl|'\n'
DECL|variable|BAREMETAL
name|'BAREMETAL'
op|'='
string|'"baremetal"'
newline|'\n'
DECL|variable|BHYVE
name|'BHYVE'
op|'='
string|'"bhyve"'
newline|'\n'
DECL|variable|DOCKER
name|'DOCKER'
op|'='
string|'"docker"'
newline|'\n'
DECL|variable|FAKE
name|'FAKE'
op|'='
string|'"fake"'
newline|'\n'
DECL|variable|HYPERV
name|'HYPERV'
op|'='
string|'"hyperv"'
newline|'\n'
DECL|variable|IRONIC
name|'IRONIC'
op|'='
string|'"ironic"'
newline|'\n'
DECL|variable|KQEMU
name|'KQEMU'
op|'='
string|'"kqemu"'
newline|'\n'
DECL|variable|KVM
name|'KVM'
op|'='
string|'"kvm"'
newline|'\n'
DECL|variable|LXC
name|'LXC'
op|'='
string|'"lxc"'
newline|'\n'
DECL|variable|OPENVZ
name|'OPENVZ'
op|'='
string|'"openvz"'
newline|'\n'
DECL|variable|PARALLELS
name|'PARALLELS'
op|'='
string|'"parallels"'
newline|'\n'
DECL|variable|VIRTUOZZO
name|'VIRTUOZZO'
op|'='
string|'"vz"'
newline|'\n'
DECL|variable|PHYP
name|'PHYP'
op|'='
string|'"phyp"'
newline|'\n'
DECL|variable|QEMU
name|'QEMU'
op|'='
string|'"qemu"'
newline|'\n'
DECL|variable|TEST
name|'TEST'
op|'='
string|'"test"'
newline|'\n'
DECL|variable|UML
name|'UML'
op|'='
string|'"uml"'
newline|'\n'
DECL|variable|VBOX
name|'VBOX'
op|'='
string|'"vbox"'
newline|'\n'
DECL|variable|VMWARE
name|'VMWARE'
op|'='
string|'"vmware"'
newline|'\n'
DECL|variable|XEN
name|'XEN'
op|'='
string|'"xen"'
newline|'\n'
DECL|variable|ZVM
name|'ZVM'
op|'='
string|'"zvm"'
newline|'\n'
nl|'\n'
DECL|variable|ALL
name|'ALL'
op|'='
op|'('
nl|'\n'
name|'BAREMETAL'
op|','
nl|'\n'
name|'BHYVE'
op|','
nl|'\n'
name|'DOCKER'
op|','
nl|'\n'
name|'FAKE'
op|','
nl|'\n'
name|'HYPERV'
op|','
nl|'\n'
name|'IRONIC'
op|','
nl|'\n'
name|'KQEMU'
op|','
nl|'\n'
name|'KVM'
op|','
nl|'\n'
name|'LXC'
op|','
nl|'\n'
name|'OPENVZ'
op|','
nl|'\n'
name|'PARALLELS'
op|','
nl|'\n'
name|'PHYP'
op|','
nl|'\n'
name|'QEMU'
op|','
nl|'\n'
name|'TEST'
op|','
nl|'\n'
name|'UML'
op|','
nl|'\n'
name|'VBOX'
op|','
nl|'\n'
name|'VIRTUOZZO'
op|','
nl|'\n'
name|'VMWARE'
op|','
nl|'\n'
name|'XEN'
op|','
nl|'\n'
name|'ZVM'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid
name|'def'
name|'is_valid'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if a string is a valid hypervisor type\n\n    :param name: hypervisor type name to validate\n\n    :returns: True if @name is valid\n    """'
newline|'\n'
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
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Canonicalize the hypervisor type name\n\n    :param name: hypervisor type name to canonicalize\n\n    :returns: a canonical hypervisor type name\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'name'
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
name|'newname'
op|'='
name|'name'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'newname'
op|'=='
string|'"xapi"'
op|':'
newline|'\n'
indent|'        '
name|'newname'
op|'='
name|'XEN'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'is_valid'
op|'('
name|'newname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidHypervisorVirtType'
op|'('
name|'hv_type'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'newname'
newline|'\n'
dedent|''
endmarker|''
end_unit
