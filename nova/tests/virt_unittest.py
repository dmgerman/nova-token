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
name|'etree'
op|'.'
name|'ElementTree'
name|'import'
name|'fromstring'
name|'as'
name|'xml_to_tree'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'import'
name|'parseString'
name|'as'
name|'xml_to_dom'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
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
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
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
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtConnTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'instances_path'
op|'='
string|"''"
newline|'\n'
nl|'\n'
DECL|member|test_get_uri_and_template
dedent|''
name|'def'
name|'test_get_uri_and_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
string|"'10.11.12.13'"
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'internal_id'"
op|':'
number|'1'
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
string|"'fake'"
op|','
nl|'\n'
string|"'bridge'"
op|':'
string|"'br101'"
op|','
nl|'\n'
string|"'instance_type'"
op|':'
string|"'m1.small'"
op|'}'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'None'
op|','
name|'instance'
op|')'
newline|'\n'
name|'user_context'
op|'='
name|'context'
op|'.'
name|'APIRequestContext'
op|'('
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|','
nl|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'get_network'
op|'('
name|'user_context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'.'
name|'set_network_host'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ip'
op|'='
op|'{'
string|"'address'"
op|':'
name|'ip'
op|','
nl|'\n'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'fixed_ip_ref'
op|'='
name|'db'
op|'.'
name|'fixed_ip_create'
op|'('
name|'None'
op|','
name|'fixed_ip'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'fixed_ip_update'
op|'('
name|'None'
op|','
name|'ip'
op|','
op|'{'
string|"'allocated'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'.'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'qemu'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./os/type'"
op|')'
op|'.'
name|'text'
op|','
string|"'hvm'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./devices/emulator'"
op|')'
op|','
name|'None'
op|')'
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
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'.'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'kvm'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./os/type'"
op|')'
op|'.'
name|'text'
op|','
string|"'hvm'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./devices/emulator'"
op|')'
op|','
name|'None'
op|')'
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
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'.'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'uml'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./os/type'"
op|')'
op|'.'
name|'text'
op|','
string|"'uml'"
op|')'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'common_checks'
op|'='
op|'['
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'.'"
op|')'
op|'.'
name|'tag'
op|','
string|"'domain'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./devices/interface/filterref/parameter'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
string|"'IP'"
op|')'
op|','
nl|'\n'
op|'('
name|'lambda'
name|'t'
op|':'
name|'t'
op|'.'
name|'find'
op|'('
string|"'./devices/interface/filterref/parameter'"
op|')'
op|'.'
name|'get'
op|'('
string|"'value'"
op|')'
op|','
string|"'10.11.12.13'"
op|')'
op|']'
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
name|'xml'
op|'='
name|'conn'
op|'.'
name|'to_xml'
op|'('
name|'instance_ref'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'xml_to_tree'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
op|'('
name|'check'
op|','
name|'expected_result'
op|')'
name|'in'
name|'enumerate'
op|'('
name|'checks'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
name|'tree'
op|')'
op|','
nl|'\n'
name|'expected_result'
op|','
nl|'\n'
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
dedent|''
name|'for'
name|'i'
op|','
op|'('
name|'check'
op|','
name|'expected_result'
op|')'
name|'in'
name|'enumerate'
op|'('
name|'common_checks'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'check'
op|'('
name|'tree'
op|')'
op|','
nl|'\n'
name|'expected_result'
op|','
nl|'\n'
string|"'%s failed common check %d'"
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
DECL|member|tearDown
dedent|''
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtConnTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|class|NWFilterTestCase
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
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NWFilterTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|Mock
name|'class'
name|'Mock'
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
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'APIRequestContext'
op|'('
name|'self'
op|'.'
name|'user'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'fw'
op|'='
name|'libvirt_conn'
op|'.'
name|'NWFilterFirewall'
op|'('
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_cidr_rule_nwfilter_xml
dedent|''
name|'def'
name|'test_cidr_rule_nwfilter_xml'
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
name|'cloud_controller'
op|'.'
name|'create_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
string|"'test group description'"
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'authorize_security_group_ingress'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
name|'from_port'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'to_port'
op|'='
string|"'81'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'cidr_ip'
op|'='
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'security_group'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'fw'
op|'.'
name|'security_group_to_nwfilter_xml'
op|'('
name|'security_group'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'dom'
op|'='
name|'xml_to_dom'
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
string|"'accept'"
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
string|"'tcp'"
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
string|"'srcipaddr'"
op|')'
op|','
string|"'0.0.0.0'"
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
string|"'srcipmask'"
op|')'
op|','
string|"'0.0.0.0'"
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
nl|'\n'
nl|'\n'
name|'self'
op|'.'
name|'teardown_security_group'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown_security_group
dedent|''
name|'def'
name|'teardown_security_group'
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
name|'cloud_controller'
op|'.'
name|'delete_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setup_and_return_security_group
dedent|''
name|'def'
name|'setup_and_return_security_group'
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
name|'cloud_controller'
op|'.'
name|'create_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
string|"'test group description'"
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'authorize_security_group_ingress'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
name|'from_port'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'to_port'
op|'='
string|"'81'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'cidr_ip'
op|'='
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake'"
op|','
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_creates_base_rule_first
dedent|''
name|'def'
name|'test_creates_base_rule_first'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# These come pre-defined by libvirt'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'defined_filters'
op|'='
op|'['
string|"'no-mac-spoofing'"
op|','
nl|'\n'
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|','
nl|'\n'
string|"'allow-dhcp-server'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'defined_filters'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'f'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_filterDefineXMLMock
dedent|''
name|'def'
name|'_filterDefineXMLMock'
op|'('
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dom'
op|'='
name|'xml_to_dom'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'name'
op|'='
name|'dom'
op|'.'
name|'firstChild'
op|'.'
name|'getAttribute'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'name'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'dom'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'filterref'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ref'
op|'='
name|'f'
op|'.'
name|'getAttribute'
op|'('
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ref'
name|'in'
name|'self'
op|'.'
name|'defined_filters'
op|','
nl|'\n'
op|'('
string|"'%s referenced filter that does '"
op|'+'
nl|'\n'
string|"'not yet exist: %s'"
op|')'
op|'%'
op|'('
name|'name'
op|','
name|'ref'
op|')'
op|')'
newline|'\n'
name|'dependencies'
op|'='
op|'['
name|'ref'
op|']'
op|'+'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'ref'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'name'
op|']'
op|'+='
name|'dependencies'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'defined_filters'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|'.'
name|'nwfilterDefineXML'
op|'='
name|'_filterDefineXMLMock'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|'}'
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_ensure_all_called
name|'def'
name|'_ensure_all_called'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_filter'
op|'='
string|"'nova-instance-%s'"
op|'%'
name|'instance_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'secgroup_filter'
op|'='
string|"'nova-secgroup-%s'"
op|'%'
name|'self'
op|'.'
name|'security_group'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'for'
name|'required'
name|'in'
op|'['
name|'secgroup_filter'
op|','
string|"'allow-dhcp-server'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|','
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-mac-spoofing'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'required'
name|'in'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'instance_filter'
op|']'
op|','
nl|'\n'
string|'"Instance\'s filter does not include %s"'
op|'%'
name|'required'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'setup_and_return_security_group'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_add_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst_id'
op|','
name|'self'
op|'.'
name|'security_group'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst_id'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'fw'
op|'.'
name|'setup_nwfilters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'_ensure_all_called'
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
name|'teardown_security_group'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
