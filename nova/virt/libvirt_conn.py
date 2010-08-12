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
string|'"""\nA connection to a hypervisor (e.g. KVM) through libvirt.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'disk'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
DECL|variable|libvirt
name|'libvirt'
op|'='
name|'None'
newline|'\n'
DECL|variable|libxml2
name|'libxml2'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_xml_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'compute/libvirt.xml.template'"
op|')'
op|','
nl|'\n'
string|"'Libvirt XML Template'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'compute/interfaces.template'"
op|')'
op|','
nl|'\n'
string|"'Template file for injected network'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'libvirt_type'"
op|','
nl|'\n'
string|"'kvm'"
op|','
nl|'\n'
string|"'Libvirt domain type (kvm, qemu, etc)'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'read_only'
op|')'
op|':'
newline|'\n'
comment|"# These are loaded late so that there's no need to install these"
nl|'\n'
comment|'# libraries when not using libvirt.'
nl|'\n'
indent|'    '
name|'global'
name|'libvirt'
newline|'\n'
name|'global'
name|'libxml2'
newline|'\n'
name|'if'
name|'libvirt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'libvirt'
op|'='
name|'__import__'
op|'('
string|"'libvirt'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'libxml2'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'libxml2'
op|'='
name|'__import__'
op|'('
string|"'libxml2'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'LibvirtConnection'
op|'('
name|'read_only'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConnection
dedent|''
name|'class'
name|'LibvirtConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'read_only'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'auth'
op|'='
op|'['
op|'['
name|'libvirt'
op|'.'
name|'VIR_CRED_AUTHNAME'
op|','
name|'libvirt'
op|'.'
name|'VIR_CRED_NOECHOPROMPT'
op|']'
op|','
nl|'\n'
string|"'root'"
op|','
nl|'\n'
name|'None'
op|']'
newline|'\n'
name|'if'
name|'read_only'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'libvirt'
op|'.'
name|'openReadOnly'
op|'('
string|"'qemu:///system'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'libvirt'
op|'.'
name|'openAuth'
op|'('
string|"'qemu:///system'"
op|','
name|'auth'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByID'
op|'('
name|'x'
op|')'
op|'.'
name|'name'
op|'('
op|')'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'listDomainsID'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'virt_dom'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'virt_dom'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'_err'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
comment|"# If the instance is already terminated, we're still happy"
nl|'\n'
dedent|''
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'self'
op|'.'
name|'_cleanup'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
comment|'# FIXME: What does this comment mean?'
nl|'\n'
comment|'# TODO(termie): short-circuit me for tests'
nl|'\n'
comment|"# WE'LL save this for when we do shutdown,"
nl|'\n'
comment|'# instead of destroy - but destroy returns immediately'
nl|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_shutdown
name|'def'
name|'_wait_for_shutdown'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'update_state'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|':'
newline|'\n'
indent|'                    '
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_shutdown'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_cleanup
dedent|''
name|'def'
name|'_cleanup'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'target'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'instance'
op|'.'
name|'datamodel'
op|'['
string|"'basepath'"
op|']'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|'"Deleting instance files at %s"'
op|','
name|'target'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|reboot
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'self'
op|'.'
name|'toXml'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'createXML'
op|'('
name|'xml'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_reboot
name|'def'
name|'_wait_for_reboot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'update_state'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'is_running'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'rebooted instance %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'error'
op|'('
string|"'_wait_for_reboot failed: %s'"
op|'%'
name|'exn'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_reboot'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'yield'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|spawn
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'self'
op|'.'
name|'toXml'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'NOSTATE'
op|','
string|"'launching'"
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_create_image'
op|'('
name|'instance'
op|','
name|'xml'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'createXML'
op|'('
name|'xml'
op|','
number|'0'
op|')'
newline|'\n'
comment|'# TODO(termie): this should actually register'
nl|'\n'
comment|'# a callback to check for successful boot'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Instance is running"'
op|')'
newline|'\n'
nl|'\n'
name|'local_d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'timer'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
DECL|function|_wait_for_boot
name|'def'
name|'_wait_for_boot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'instance'
op|'.'
name|'update_state'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'is_running'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'booted instance %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'local_d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'error'
op|'('
string|'"_wait_for_boot exception %s"'
op|'%'
name|'exn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_state'
op|'('
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
string|"'Failed to boot instance %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'local_d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_boot'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'yield'
name|'local_d'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_create_image
name|'def'
name|'_create_image'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'libvirt_xml'
op|')'
op|':'
newline|'\n'
comment|'# syntactic nicety'
nl|'\n'
indent|'        '
name|'data'
op|'='
name|'instance'
op|'.'
name|'datamodel'
newline|'\n'
name|'basepath'
op|'='
name|'lambda'
name|'x'
op|'='
string|"''"
op|':'
name|'self'
op|'.'
name|'basepath'
op|'('
name|'instance'
op|','
name|'x'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure directories exist and are writable'
nl|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'mkdir -p %s'"
op|'%'
name|'basepath'
op|'('
op|')'
op|')'
newline|'\n'
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'chmod 0777 %s'"
op|'%'
name|'basepath'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): these are blocking calls, it would be great'
nl|'\n'
comment|"#               if they weren't."
nl|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Creating image for: %s'"
op|','
name|'data'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'basepath'
op|'('
string|"'libvirt.xml'"
op|')'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'libvirt_xml'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'user'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'data'
op|'['
string|"'user_id'"
op|']'
op|')'
newline|'\n'
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'data'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'data'
op|'['
string|"'image_id'"
op|']'
op|','
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'kernel'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'data'
op|'['
string|"'kernel_id'"
op|']'
op|','
name|'basepath'
op|'('
string|"'kernel'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'ramdisk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'yield'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'data'
op|'['
string|"'ramdisk_id'"
op|']'
op|','
name|'basepath'
op|'('
string|"'ramdisk'"
op|')'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'execute'
op|'='
name|'lambda'
name|'cmd'
op|','
name|'input'
op|'='
name|'None'
op|':'
name|'process'
op|'.'
name|'simple_execute'
op|'('
name|'cmd'
op|'='
name|'cmd'
op|','
nl|'\n'
name|'input'
op|'='
name|'input'
op|','
nl|'\n'
name|'error_ok'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'key'
op|'='
name|'data'
op|'['
string|"'key_data'"
op|']'
newline|'\n'
name|'net'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'get'
op|'('
string|"'inject_network'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'injected_network_template'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'net'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|'%'
op|'{'
string|"'address'"
op|':'
name|'data'
op|'['
string|"'private_dns_name'"
op|']'
op|','
nl|'\n'
string|"'network'"
op|':'
name|'data'
op|'['
string|"'network_network'"
op|']'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'data'
op|'['
string|"'network_netmask'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'data'
op|'['
string|"'network_gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'data'
op|'['
string|"'network_broadcast'"
op|']'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'data'
op|'['
string|"'network_dns'"
op|']'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'key'
name|'or'
name|'net'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Injecting data into image %s'"
op|','
name|'data'
op|'['
string|"'image_id'"
op|']'
op|')'
newline|'\n'
name|'yield'
name|'disk'
op|'.'
name|'inject_data'
op|'('
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'key'
op|','
name|'net'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'process'
op|'.'
name|'simple_execute'
op|'('
string|"'rm -f %s'"
op|'%'
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bytes'
op|'='
op|'('
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'data'
op|'['
string|"'instance_type'"
op|']'
op|']'
op|'['
string|"'local_gb'"
op|']'
nl|'\n'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'yield'
name|'disk'
op|'.'
name|'partition'
op|'('
nl|'\n'
name|'basepath'
op|'('
string|"'disk-raw'"
op|')'
op|','
name|'basepath'
op|'('
string|"'disk'"
op|')'
op|','
name|'bytes'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|basepath
dedent|''
name|'def'
name|'basepath'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'path'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instance'
op|'.'
name|'datamodel'
op|'['
string|"'basepath'"
op|']'
op|','
name|'path'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|toXml
dedent|''
name|'def'
name|'toXml'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
comment|'# TODO(termie): cache?'
nl|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Starting the toXML method"'
op|')'
newline|'\n'
name|'libvirt_xml'
op|'='
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'libvirt_xml_template'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'xml_info'
op|'='
name|'instance'
op|'.'
name|'datamodel'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
comment|'# TODO(joshua): Make this xml express the attached disks as well'
nl|'\n'
nl|'\n'
comment|'# TODO(termie): lazy lazy hack because xml is annoying'
nl|'\n'
name|'xml_info'
op|'['
string|"'nova'"
op|']'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'instance'
op|'.'
name|'datamodel'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
name|'xml_info'
op|'['
string|"'type'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'libvirt_type'
newline|'\n'
name|'libvirt_xml'
op|'='
name|'libvirt_xml'
op|'%'
name|'xml_info'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Finished the toXML method"'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'libvirt_xml'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'virt_dom'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_id'
op|')'
newline|'\n'
op|'('
name|'state'
op|','
name|'max_mem'
op|','
name|'mem'
op|','
name|'num_cpu'
op|','
name|'cpu_time'
op|')'
op|'='
name|'virt_dom'
op|'.'
name|'info'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'max_mem'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'num_cpu'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
name|'cpu_time'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|get_disks
dedent|''
name|'def'
name|'get_disks'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance ID, not an Instance, so\n        that it can be called by monitor.\n\n        Returns a list of all block devices for this domain.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# TODO(devcamcar): Replace libxml2 with etree.'
nl|'\n'
name|'xml'
op|'='
name|'domain'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'doc'
op|'='
name|'libxml2'
op|'.'
name|'parseDoc'
op|'('
name|'xml'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ctx'
op|'='
name|'doc'
op|'.'
name|'xpathNewContext'
op|'('
op|')'
newline|'\n'
name|'disks'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'ctx'
op|'.'
name|'xpathEval'
op|'('
string|"'/domain/devices/disk'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'devdst'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'child'
op|'.'
name|'name'
op|'=='
string|"'target'"
op|':'
newline|'\n'
indent|'                        '
name|'devdst'
op|'='
name|'child'
op|'.'
name|'prop'
op|'('
string|"'dev'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'devdst'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'disks'
op|'.'
name|'append'
op|'('
name|'devdst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ctx'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ctx'
op|'.'
name|'xpathFreeContext'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'doc'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'doc'
op|'.'
name|'freeDoc'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'disks'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|get_interfaces
dedent|''
name|'def'
name|'get_interfaces'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance ID, not an Instance, so\n        that it can be called by monitor.\n\n        Returns a list of all network interfaces for this instance.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_id'
op|')'
newline|'\n'
comment|'# TODO(devcamcar): Replace libxml2 with etree.'
nl|'\n'
name|'xml'
op|'='
name|'domain'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'doc'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'doc'
op|'='
name|'libxml2'
op|'.'
name|'parseDoc'
op|'('
name|'xml'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ctx'
op|'='
name|'doc'
op|'.'
name|'xpathNewContext'
op|'('
op|')'
newline|'\n'
name|'interfaces'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'ctx'
op|'.'
name|'xpathEval'
op|'('
string|"'/domain/devices/interface'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'ret'
op|':'
newline|'\n'
indent|'                '
name|'devdst'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'child'
op|'.'
name|'name'
op|'=='
string|"'target'"
op|':'
newline|'\n'
indent|'                        '
name|'devdst'
op|'='
name|'child'
op|'.'
name|'prop'
op|'('
string|"'dev'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'devdst'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'interfaces'
op|'.'
name|'append'
op|'('
name|'devdst'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ctx'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'ctx'
op|'.'
name|'xpathFreeContext'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'doc'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'doc'
op|'.'
name|'freeDoc'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'interfaces'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|block_stats
dedent|''
name|'def'
name|'block_stats'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'disk'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance ID, not an Instance, so\n        that it can be called by monitor.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'domain'
op|'.'
name|'blockStats'
op|'('
name|'disk'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|interface_stats
dedent|''
name|'def'
name|'interface_stats'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Note that this function takes an instance ID, not an Instance, so\n        that it can be called by monitor.\n        """'
newline|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'lookupByName'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'domain'
op|'.'
name|'interfaceStats'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
