begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
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
name|'from'
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'import'
name|'parseString'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'libvirt_conn'
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
DECL|class|LibvirtConnTestCase
name|'class'
name|'LibvirtConnTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|bitrot_test_get_uri_and_template
indent|'    '
name|'def'
name|'bitrot_test_get_uri_and_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|MockDataModel
indent|'        '
name|'class'
name|'MockDataModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__getitem__
indent|'            '
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'datamodel'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'datamodel'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'i-cafebabe'"
op|','
nl|'\n'
string|"'memory_kb'"
op|':'
string|"'1024000'"
op|','
nl|'\n'
string|"'basepath'"
op|':'
string|"'/some/path'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
string|"'br100'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'02:12:34:46:56:67'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'type_uri_map'
op|'='
op|'{'
string|"'qemu'"
op|':'
op|'('
string|"'qemu:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'qemu\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>hvm</type'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'emulator>/usr/bin/kvm'"
name|'not'
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
string|"'kvm'"
op|':'
op|'('
string|"'qemu:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'kvm\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>hvm</type'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'emulator>/usr/bin/qemu<'"
name|'not'
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
string|"'uml'"
op|':'
op|'('
string|"'uml:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'uml\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>uml</type'"
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'libvirt_type'
op|','
op|'('
name|'expected_uri'
op|','
name|'checks'
op|')'
op|')'
name|'in'
name|'type_uri_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'='
name|'libvirt_type'
newline|'\n'
DECL|variable|conn
name|'conn'
op|'='
name|'libvirt_conn'
op|'.'
name|'LibvirtConnection'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'uri'
op|','
name|'template'
op|'='
name|'conn'
op|'.'
name|'get_uri_and_template'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'uri'
op|','
name|'expected_uri'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'check'
name|'in'
name|'enumerate'
op|'('
name|'checks'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'xml'
op|'='
name|'conn'
op|'.'
name|'to_xml'
op|'('
name|'MockDataModel'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'check'
op|'('
name|'xml'
op|')'
op|','
string|"'%s failed check %d'"
op|'%'
op|'('
name|'xml'
op|','
name|'i'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Deliberately not just assigning this string to FLAGS.libvirt_uri and'
nl|'\n'
comment|'# checking against that later on. This way we make sure the'
nl|'\n'
comment|"# implementation doesn't fiddle around with the FLAGS."
nl|'\n'
dedent|''
dedent|''
name|'testuri'
op|'='
string|"'something completely different'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'libvirt_uri'
op|'='
name|'testuri'
newline|'\n'
name|'for'
op|'('
name|'libvirt_type'
op|','
op|'('
name|'expected_uri'
op|','
name|'checks'
op|')'
op|')'
name|'in'
name|'type_uri_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'='
name|'libvirt_type'
newline|'\n'
DECL|variable|conn
name|'conn'
op|'='
name|'libvirt_conn'
op|'.'
name|'LibvirtConnection'
op|'('
name|'True'
op|')'
newline|'\n'
name|'uri'
op|','
name|'template'
op|'='
name|'conn'
op|'.'
name|'get_uri_and_template'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'uri'
op|','
name|'testuri'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NWFilterTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'NWFilterTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_stuff
indent|'    '
name|'def'
name|'test_stuff'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cloud_controller'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
DECL|class|FakeContext
name|'class'
name|'FakeContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'FakeContext'
op|'('
op|')'
newline|'\n'
name|'context'
op|'.'
name|'user'
op|'='
name|'FakeContext'
op|'('
op|')'
newline|'\n'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|'='
string|"'fake'"
newline|'\n'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_superuser'
op|'='
name|'lambda'
op|':'
name|'True'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'create_security_group'
op|'('
name|'context'
op|','
string|"'testgroup'"
op|','
string|"'test group description'"
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'authorize_security_group_ingress'
op|'('
name|'context'
op|','
string|"'testgroup'"
op|','
name|'from_port'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'to_port'
op|'='
string|"'81'"
op|','
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
DECL|variable|cidr_ip
name|'cidr_ip'
op|'='
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
name|'fw'
op|'='
name|'libvirt_conn'
op|'.'
name|'NWFilterFirewall'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'='
name|'fw'
op|'.'
name|'security_group_to_nwfilter_xml'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'dom'
op|'='
name|'parseString'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dom'
op|'.'
name|'firstChild'
op|'.'
name|'tagName'
op|','
string|"'filter'"
op|')'
newline|'\n'
nl|'\n'
name|'rules'
op|'='
name|'dom'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'rule'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rules'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|"# It's supposed to allow inbound traffic."
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'action'"
op|')'
op|','
string|"'allow'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'direction'"
op|')'
op|','
string|"'in'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Must be lower priority than the base filter (which blocks everything)'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'int'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'priority'"
op|')'
op|')'
op|'<'
number|'1000'
op|')'
newline|'\n'
nl|'\n'
name|'ip_conditions'
op|'='
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ip_conditions'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'tcp'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'dstportstart'"
op|')'
op|','
string|"'80'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'dstportend'"
op|')'
op|','
string|"'81'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
