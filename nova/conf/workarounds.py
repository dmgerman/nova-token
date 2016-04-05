begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
string|'""" The workarounds_opts group is for very specific reasons.\n\nIf you\'re:\n\n - Working around an issue in a system tool (e.g. libvirt or qemu) where the\n   fix is in flight/discussed in that community.\n - The tool can be/is fixed in some distributions and rather than patch the\n   code those distributions can trivially set a config option to get the\n   "correct" behavior.\n\nThen this is a good place for your workaround.\n\n.. warning::\n\n  Please use with care! Document the BugID that your workaround is paired with.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|disable_rootwrap
name|'disable_rootwrap'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'disable_rootwrap'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'This option allows a fallback to sudo for performance '"
nl|'\n'
string|"'reasons. For example see '"
nl|'\n'
string|"'https://bugs.launchpad.net/nova/+bug/1415106'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|disable_libvirt_livesnapshot
name|'disable_libvirt_livesnapshot'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'disable_libvirt_livesnapshot'"
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
string|"'When using libvirt 1.2.2 live snapshots fail '"
nl|'\n'
string|"'intermittently under load.  This config option provides '"
nl|'\n'
string|"'a mechanism to enable live snapshot while this is '"
nl|'\n'
string|"'resolved.  See '"
nl|'\n'
string|"'https://bugs.launchpad.net/nova/+bug/1334398'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|handle_virt_lifecycle_events
name|'handle_virt_lifecycle_events'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'handle_virt_lifecycle_events'"
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
string|'"Whether or not to handle events raised from the compute "'
nl|'\n'
string|'"driver\'s \'emit_event\' method. These are lifecycle "'
nl|'\n'
string|'"events raised from compute drivers that implement the "'
nl|'\n'
string|'"method. An example of a lifecycle event is an instance "'
nl|'\n'
string|'"starting or stopping. If the instance is going through "'
nl|'\n'
string|'"task state changes due to an API operation, like "'
nl|'\n'
string|'"resize, the events are ignored. However, this is an "'
nl|'\n'
string|'"advanced feature which allows the hypervisor to signal "'
nl|'\n'
string|'"to the compute service that an unexpected state change "'
nl|'\n'
string|'"has occurred in an instance and the instance can be "'
nl|'\n'
string|'"shutdown automatically - which can inherently race in "'
nl|'\n'
string|'"reboot operations or when the compute service or host "'
nl|'\n'
string|'"is rebooted, either planned or due to an unexpected "'
nl|'\n'
string|'"outage. Care should be taken when using this and "'
nl|'\n'
string|'"sync_power_state_interval is negative since then if any "'
nl|'\n'
string|'"instances are out of sync between the hypervisor and "'
nl|'\n'
string|'"the Nova database they will have to be synchronized "'
nl|'\n'
string|'"manually. See https://bugs.launchpad.net/bugs/1444630"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'disable_rootwrap'
op|','
nl|'\n'
name|'disable_libvirt_livesnapshot'
op|','
nl|'\n'
name|'handle_virt_lifecycle_events'
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
op|','
name|'group'
op|'='
string|"'workarounds'"
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
indent|'    '
name|'return'
op|'{'
string|"'workarounds'"
op|':'
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit