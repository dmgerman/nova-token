begin_unit
comment|'# Copyright 2015 Intel Corporation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|vcpu_pin_set
name|'vcpu_pin_set'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'vcpu_pin_set'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Defines which physical CPUs (pCPUs) can be used by instance\nvirtual CPUs (vCPUs).\n\nPossible values:\n\n* A comma-separated list of physical CPU numbers that virtual CPUs can be\n  allocated to by default. Each element should be either a single CPU number,\n  a range of CPU numbers, or a caret followed by a CPU number to be\n  excluded from a previous range. For example:\n\n    vcpu_pin_set = "4-12,^8,15"\n\nServices which consume this:\n\n* ``nova-scheduler``\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|compute_driver
name|'compute_driver'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'compute_driver'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Defines which driver to use for controlling virtualization.\n\nPossible values:\n\n* ``libvirt.LibvirtDriver``\n* ``xenapi.XenAPIDriver``\n* ``fake.FakeDriver``\n* ``ironic.IronicDriver``\n* ``vmwareapi.VMwareVCDriver``\n* ``hyperv.HyperVDriver``\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|default_ephemeral_format
name|'default_ephemeral_format'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'default_ephemeral_format'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""The default format an ephemeral_volume will be formatted\nwith on creation.\n\nPossible values:\n\n* ``ext2``\n* ``ext3``\n* ``ext4``\n* ``xfs``\n* ``ntfs`` (only for Windows guests)\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|preallocate_images
name|'preallocate_images'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'preallocate_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'none'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'none'"
op|','
string|"'space'"
op|')'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""The image preallocation mode to use. Image preallocation allows\nstorage for instance images to be allocated up front when the instance is\ninitially provisioned. This ensures immediate feedback is given if enough\nspace isn\'t available. In addition, it should significantly improve\nperformance on writes to new blocks and may even improve I/O performance to\nprewritten blocks due to reduced fragmentation.\n\nPossible values:\n\n* "none"  => no storage provisioning is done up front\n* "space" => storage is fully allocated at instance start\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|use_cow_images
name|'use_cow_images'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'use_cow_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Enable use of copy-on-write (cow) images.\n\nQEMU/KVM allow the use of qcow2 as backing files. By disabling this,\nbacking files will not be used.\n\nPossible values:\n\n* True: Enable use of cow images\n* False: Disable use of cow images\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vif_plugging_is_fatal
name|'vif_plugging_is_fatal'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'vif_plugging_is_fatal'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Determine if instance should boot or fail on VIF plugging timeout.\n\nNova sends a port update to Neutron after an instance has been scheduled,\nproviding Neutron with the necessary information to finish setup of the port.\nOnce completed, Neutron notifies Nova that it has finished setting up the\nport, at which point Nova resumes the boot of the instance since network\nconnectivity is now supposed to be present. A timeout will occur if the reply\nis not received after a given interval.\n\nThis option determines what Nova does when the VIF plugging timeout event\nhappens. When enabled, the instance will error out. When disabled, the\ninstance will continue to boot on the assumption that the port is ready.\n\nPossible values:\n\n* True: Instances should fail after VIF plugging timeout\n* False: Instances should continue booting after VIF plugging timeout\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|vif_plugging_timeout
name|'vif_plugging_timeout'
op|'='
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
nl|'\n'
string|"'vif_plugging_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""Timeout for Neutron VIF plugging event message arrival.\n\nNumber of seconds to wait for Neutron vif plugging events to\narrive before continuing or failing (see \'vif_plugging_is_fatal\'). If this is\nset to zero and \'vif_plugging_is_fatal\' is False, events should not be\nexpected to arrive at all.\n\nPossible values:\n\n* A time interval in seconds\n\nServices which consume this:\n\n* ``nova-compute``\n\nInterdependencies to other options:\n\n* None\n"""'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|force_raw_images
name|'force_raw_images'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'force_raw_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force backing images to raw format'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'vcpu_pin_set'
op|','
nl|'\n'
name|'compute_driver'
op|','
nl|'\n'
name|'default_ephemeral_format'
op|','
nl|'\n'
name|'preallocate_images'
op|','
nl|'\n'
name|'use_cow_images'
op|','
nl|'\n'
name|'vif_plugging_is_fatal'
op|','
nl|'\n'
name|'vif_plugging_timeout'
op|','
nl|'\n'
name|'force_raw_images'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_OPTS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# TODO(sfinucan): This should be moved to a virt or hardware group'
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|"'DEFAULT'"
op|':'
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
