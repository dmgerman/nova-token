begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright (C) 2012 Red Hat, Inc.'
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
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'objectify'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigBaseTest
name|'class'
name|'LibvirtConfigBaseTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|assertXmlEqual
indent|'    '
name|'def'
name|'assertXmlEqual'
op|'('
name|'self'
op|','
name|'expectedXmlstr'
op|','
name|'actualXmlstr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'objectify'
op|'.'
name|'fromstring'
op|'('
name|'expectedXmlstr'
op|')'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'objectify'
op|'.'
name|'fromstring'
op|'('
name|'actualXmlstr'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_plain
indent|'    '
name|'def'
name|'test_config_plain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigObject'
op|'('
name|'root_name'
op|'='
string|'"demo"'
op|')'
newline|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"<demo/>"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_ns
dedent|''
name|'def'
name|'test_config_ns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigObject'
op|'('
name|'root_name'
op|'='
string|'"demo"'
op|','
name|'ns_prefix'
op|'='
string|'"foo"'
op|','
nl|'\n'
name|'ns_uri'
op|'='
string|'"http://example.com/foo"'
op|')'
newline|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <foo:demo xmlns:foo="http://example.com/foo"/>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_text
dedent|''
name|'def'
name|'test_config_text'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigObject'
op|'('
name|'root_name'
op|'='
string|'"demo"'
op|')'
newline|'\n'
name|'root'
op|'='
name|'obj'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'root'
op|'.'
name|'append'
op|'('
name|'obj'
op|'.'
name|'_text_node'
op|'('
string|'"foo"'
op|','
string|'"bar"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"<demo><foo>bar</foo></demo>"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestTimerTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestTimerTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
DECL|member|test_config_platform
indent|'    '
name|'def'
name|'test_config_platform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestTimer'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'track'
op|'='
string|'"host"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <timer name="platform" track="host"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_pit
dedent|''
name|'def'
name|'test_config_pit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestTimer'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"pit"'
newline|'\n'
name|'obj'
op|'.'
name|'tickpolicy'
op|'='
string|'"discard"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <timer name="pit" tickpolicy="discard"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_hpet
dedent|''
name|'def'
name|'test_config_hpet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestTimer'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"hpet"'
newline|'\n'
name|'obj'
op|'.'
name|'present'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <timer name="hpet" present="no"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestClockTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestClockTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
DECL|member|test_config_utc
indent|'    '
name|'def'
name|'test_config_utc'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestClock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <clock offset="utc"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_localtime
dedent|''
name|'def'
name|'test_config_localtime'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestClock'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'offset'
op|'='
string|'"localtime"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <clock offset="localtime"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_timezone
dedent|''
name|'def'
name|'test_config_timezone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestClock'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'offset'
op|'='
string|'"timezone"'
newline|'\n'
name|'obj'
op|'.'
name|'timezone'
op|'='
string|'"EDT"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <clock offset="timezone" timezone="EDT"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_variable
dedent|''
name|'def'
name|'test_config_variable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestClock'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'offset'
op|'='
string|'"variable"'
newline|'\n'
name|'obj'
op|'.'
name|'adjustment'
op|'='
string|'"123456"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <clock offset="variable" adjustment="123456"/>\n        """'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_timers
dedent|''
name|'def'
name|'test_config_timers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestClock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'tmpit'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestTimer'
op|'('
op|')'
newline|'\n'
name|'tmpit'
op|'.'
name|'name'
op|'='
string|'"pit"'
newline|'\n'
name|'tmpit'
op|'.'
name|'tickpolicy'
op|'='
string|'"discard"'
newline|'\n'
nl|'\n'
name|'tmrtc'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestTimer'
op|'('
op|')'
newline|'\n'
name|'tmrtc'
op|'.'
name|'name'
op|'='
string|'"rtc"'
newline|'\n'
name|'tmrtc'
op|'.'
name|'tickpolicy'
op|'='
string|'"merge"'
newline|'\n'
nl|'\n'
name|'obj'
op|'.'
name|'add_timer'
op|'('
name|'tmpit'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'add_timer'
op|'('
name|'tmrtc'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <clock offset="utc">\n               <timer name="pit" tickpolicy="discard"/>\n               <timer name="rtc" tickpolicy="merge"/>\n            </clock>\n        """'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestDiskTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestDiskTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_file
indent|'    '
name|'def'
name|'test_config_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'source_type'
op|'='
string|'"file"'
newline|'\n'
name|'obj'
op|'.'
name|'source_path'
op|'='
string|'"/tmp/hello"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/hda"'
newline|'\n'
name|'obj'
op|'.'
name|'target_bus'
op|'='
string|'"ide"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <disk type="file" device="disk">\n              <source file="/tmp/hello"/>\n              <target bus="ide" dev="/dev/hda"/>\n            </disk>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_block
dedent|''
name|'def'
name|'test_config_block'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'source_type'
op|'='
string|'"block"'
newline|'\n'
name|'obj'
op|'.'
name|'source_path'
op|'='
string|'"/tmp/hello"'
newline|'\n'
name|'obj'
op|'.'
name|'source_device'
op|'='
string|'"cdrom"'
newline|'\n'
name|'obj'
op|'.'
name|'driver_name'
op|'='
string|'"qemu"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/hdc"'
newline|'\n'
name|'obj'
op|'.'
name|'target_bus'
op|'='
string|'"ide"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <disk type="block" device="cdrom">\n              <driver name="qemu"/>\n              <source dev="/tmp/hello"/>\n              <target bus="ide" dev="/dev/hdc"/>\n            </disk>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_network
dedent|''
name|'def'
name|'test_config_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'source_type'
op|'='
string|'"network"'
newline|'\n'
name|'obj'
op|'.'
name|'source_protocol'
op|'='
string|'"iscsi"'
newline|'\n'
name|'obj'
op|'.'
name|'source_host'
op|'='
string|'"foo.bar.com"'
newline|'\n'
name|'obj'
op|'.'
name|'driver_name'
op|'='
string|'"qemu"'
newline|'\n'
name|'obj'
op|'.'
name|'driver_format'
op|'='
string|'"qcow2"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/hda"'
newline|'\n'
name|'obj'
op|'.'
name|'target_bus'
op|'='
string|'"ide"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <disk type="network" device="disk">\n              <driver name="qemu" type="qcow2"/>\n              <source protocol="iscsi" name="foo.bar.com"/>\n              <target bus="ide" dev="/dev/hda"/>\n            </disk>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_network_auth
dedent|''
name|'def'
name|'test_config_network_auth'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'source_type'
op|'='
string|'"network"'
newline|'\n'
name|'obj'
op|'.'
name|'source_protocol'
op|'='
string|'"rbd"'
newline|'\n'
name|'obj'
op|'.'
name|'source_host'
op|'='
string|'"pool/image"'
newline|'\n'
name|'obj'
op|'.'
name|'driver_name'
op|'='
string|'"qemu"'
newline|'\n'
name|'obj'
op|'.'
name|'driver_format'
op|'='
string|'"raw"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/vda"'
newline|'\n'
name|'obj'
op|'.'
name|'target_bus'
op|'='
string|'"virtio"'
newline|'\n'
name|'obj'
op|'.'
name|'auth_username'
op|'='
string|'"foo"'
newline|'\n'
name|'obj'
op|'.'
name|'auth_secret_type'
op|'='
string|'"ceph"'
newline|'\n'
name|'obj'
op|'.'
name|'auth_secret_uuid'
op|'='
string|'"b38a3f43-4be2-4046-897f-b67c2f5e0147"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <disk type="network" device="disk">\n              <driver name="qemu" type="raw"/>\n              <source protocol="rbd" name="pool/image"/>\n              <auth username="foo">\n                <secret type="ceph"\n                uuid="b38a3f43-4be2-4046-897f-b67c2f5e0147"/>\n              </auth>\n              <target bus="virtio" dev="/dev/vda"/>\n            </disk>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestFilesysTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestFilesysTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_mount
indent|'    '
name|'def'
name|'test_config_mount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestFilesys'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'source_type'
op|'='
string|'"mount"'
newline|'\n'
name|'obj'
op|'.'
name|'source_dir'
op|'='
string|'"/tmp/hello"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dir'
op|'='
string|'"/mnt"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <filesystem type="mount">\n              <source dir="/tmp/hello"/>\n              <target dir="/mnt"/>\n            </filesystem>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestInputTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestInputTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_tablet
indent|'    '
name|'def'
name|'test_config_tablet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInput'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <input type="tablet" bus="usb"/>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestGraphicsTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestGraphicsTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_graphics
indent|'    '
name|'def'
name|'test_config_graphics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestGraphics'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'type'
op|'='
string|'"vnc"'
newline|'\n'
name|'obj'
op|'.'
name|'autoport'
op|'='
name|'True'
newline|'\n'
name|'obj'
op|'.'
name|'keymap'
op|'='
string|'"en_US"'
newline|'\n'
name|'obj'
op|'.'
name|'listen'
op|'='
string|'"127.0.0.1"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n  <graphics type="vnc" autoport="yes" keymap="en_US" listen="127.0.0.1"/>\n                            """'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestSerialTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestSerialTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_file
indent|'    '
name|'def'
name|'test_config_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestSerial'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'type'
op|'='
string|'"file"'
newline|'\n'
name|'obj'
op|'.'
name|'source_path'
op|'='
string|'"/tmp/vm.log"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <serial type="file">\n              <source file="/tmp/vm.log"/>\n            </serial>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestSerialTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestSerialTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
DECL|member|test_config_pty
indent|'    '
name|'def'
name|'test_config_pty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestConsole'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'type'
op|'='
string|'"pty"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <console type="pty"/>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestInterfaceTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestInterfaceTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
DECL|member|test_config_ethernet
indent|'    '
name|'def'
name|'test_config_ethernet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'net_type'
op|'='
string|'"ethernet"'
newline|'\n'
name|'obj'
op|'.'
name|'mac_addr'
op|'='
string|'"DE:AD:BE:EF:CA:FE"'
newline|'\n'
name|'obj'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
name|'obj'
op|'.'
name|'target_dev'
op|'='
string|'"vnet0"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <interface type="ethernet">\n              <mac address="DE:AD:BE:EF:CA:FE"/>\n              <model type="virtio"/>\n              <target dev="vnet0"/>\n            </interface>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_bridge
dedent|''
name|'def'
name|'test_config_bridge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'obj'
op|'.'
name|'source_dev'
op|'='
string|'"br0"'
newline|'\n'
name|'obj'
op|'.'
name|'mac_addr'
op|'='
string|'"DE:AD:BE:EF:CA:FE"'
newline|'\n'
name|'obj'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
name|'obj'
op|'.'
name|'filtername'
op|'='
string|'"clean-traffic"'
newline|'\n'
name|'obj'
op|'.'
name|'filterparams'
op|'.'
name|'append'
op|'('
op|'{'
string|'"key"'
op|':'
string|'"IP"'
op|','
string|'"value"'
op|':'
string|'"192.168.122.1"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <interface type="bridge">\n              <mac address="DE:AD:BE:EF:CA:FE"/>\n              <model type="virtio"/>\n              <source bridge="br0"/>\n              <filterref filter="clean-traffic">\n                <parameter name="IP" value="192.168.122.1"/>\n              </filterref>\n            </interface>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_bridge_ovs
dedent|''
name|'def'
name|'test_config_bridge_ovs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'net_type'
op|'='
string|'"bridge"'
newline|'\n'
name|'obj'
op|'.'
name|'source_dev'
op|'='
string|'"br0"'
newline|'\n'
name|'obj'
op|'.'
name|'mac_addr'
op|'='
string|'"DE:AD:BE:EF:CA:FE"'
newline|'\n'
name|'obj'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
name|'obj'
op|'.'
name|'vporttype'
op|'='
string|'"openvswitch"'
newline|'\n'
name|'obj'
op|'.'
name|'vportparams'
op|'.'
name|'append'
op|'('
op|'{'
string|'"key"'
op|':'
string|'"instanceid"'
op|','
string|'"value"'
op|':'
string|'"foobar"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <interface type="bridge">\n              <mac address="DE:AD:BE:EF:CA:FE"/>\n              <model type="virtio"/>\n              <source bridge="br0"/>\n              <virtualport type="openvswitch">\n                <parameters instanceid="foobar"/>\n              </virtualport>\n            </interface>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_8021Qbh
dedent|''
name|'def'
name|'test_config_8021Qbh'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestInterface'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'net_type'
op|'='
string|'"direct"'
newline|'\n'
name|'obj'
op|'.'
name|'mac_addr'
op|'='
string|'"DE:AD:BE:EF:CA:FE"'
newline|'\n'
name|'obj'
op|'.'
name|'model'
op|'='
string|'"virtio"'
newline|'\n'
name|'obj'
op|'.'
name|'source_dev'
op|'='
string|'"eth0"'
newline|'\n'
name|'obj'
op|'.'
name|'vporttype'
op|'='
string|'"802.1Qbh"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <interface type="direct">\n              <mac address="DE:AD:BE:EF:CA:FE"/>\n              <model type="virtio"/>\n              <source mode="private" dev="eth0"/>\n              <virtualport type="802.1Qbh"/>\n            </interface>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_lxc
indent|'    '
name|'def'
name|'test_config_lxc'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuest'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'virt_type'
op|'='
string|'"lxc"'
newline|'\n'
name|'obj'
op|'.'
name|'memory'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'100'
newline|'\n'
name|'obj'
op|'.'
name|'vcpus'
op|'='
number|'2'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"demo"'
newline|'\n'
name|'obj'
op|'.'
name|'uuid'
op|'='
string|'"b38a3f43-4be2-4046-897f-b67c2f5e0147"'
newline|'\n'
name|'obj'
op|'.'
name|'os_type'
op|'='
string|'"exe"'
newline|'\n'
name|'obj'
op|'.'
name|'os_init_path'
op|'='
string|'"/sbin/init"'
newline|'\n'
nl|'\n'
name|'fs'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestFilesys'
op|'('
op|')'
newline|'\n'
name|'fs'
op|'.'
name|'source_dir'
op|'='
string|'"/root/lxc"'
newline|'\n'
name|'fs'
op|'.'
name|'target_dir'
op|'='
string|'"/"'
newline|'\n'
nl|'\n'
name|'obj'
op|'.'
name|'add_device'
op|'('
name|'fs'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <domain type="lxc">\n              <uuid>b38a3f43-4be2-4046-897f-b67c2f5e0147</uuid>\n              <name>demo</name>\n              <memory>104857600</memory>\n              <vcpu>2</vcpu>\n              <os>\n                <type>exe</type>\n                <init>/sbin/init</init>\n              </os>\n              <devices>\n                <filesystem type="mount">\n                  <source dir="/root/lxc"/>\n                  <target dir="/"/>\n                </filesystem>\n              </devices>\n            </domain>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_xen
dedent|''
name|'def'
name|'test_config_xen'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuest'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'virt_type'
op|'='
string|'"xen"'
newline|'\n'
name|'obj'
op|'.'
name|'memory'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'100'
newline|'\n'
name|'obj'
op|'.'
name|'vcpus'
op|'='
number|'2'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"demo"'
newline|'\n'
name|'obj'
op|'.'
name|'uuid'
op|'='
string|'"b38a3f43-4be2-4046-897f-b67c2f5e0147"'
newline|'\n'
name|'obj'
op|'.'
name|'os_type'
op|'='
string|'"linux"'
newline|'\n'
name|'obj'
op|'.'
name|'os_kernel'
op|'='
string|'"/tmp/vmlinuz"'
newline|'\n'
name|'obj'
op|'.'
name|'os_initrd'
op|'='
string|'"/tmp/ramdisk"'
newline|'\n'
name|'obj'
op|'.'
name|'os_root'
op|'='
string|'"root=xvda"'
newline|'\n'
name|'obj'
op|'.'
name|'os_cmdline'
op|'='
string|'"console=xvc0"'
newline|'\n'
nl|'\n'
name|'disk'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'disk'
op|'.'
name|'source_type'
op|'='
string|'"file"'
newline|'\n'
name|'disk'
op|'.'
name|'source_path'
op|'='
string|'"/tmp/img"'
newline|'\n'
name|'disk'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/xvda"'
newline|'\n'
name|'disk'
op|'.'
name|'target_bus'
op|'='
string|'"xen"'
newline|'\n'
nl|'\n'
name|'obj'
op|'.'
name|'add_device'
op|'('
name|'disk'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <domain type="xen">\n              <uuid>b38a3f43-4be2-4046-897f-b67c2f5e0147</uuid>\n              <name>demo</name>\n              <memory>104857600</memory>\n              <vcpu>2</vcpu>\n              <os>\n                <type>linux</type>\n                <kernel>/tmp/vmlinuz</kernel>\n                <initrd>/tmp/ramdisk</initrd>\n                <cmdline>console=xvc0</cmdline>\n                <root>root=xvda</root>\n              </os>\n              <devices>\n                <disk type="file" device="disk">\n                  <source file="/tmp/img"/>\n                  <target bus="xen" dev="/dev/xvda"/>\n                </disk>\n              </devices>\n            </domain>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_kvm
dedent|''
name|'def'
name|'test_config_kvm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuest'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'virt_type'
op|'='
string|'"kvm"'
newline|'\n'
name|'obj'
op|'.'
name|'memory'
op|'='
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'100'
newline|'\n'
name|'obj'
op|'.'
name|'vcpus'
op|'='
number|'2'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"demo"'
newline|'\n'
name|'obj'
op|'.'
name|'uuid'
op|'='
string|'"b38a3f43-4be2-4046-897f-b67c2f5e0147"'
newline|'\n'
name|'obj'
op|'.'
name|'os_type'
op|'='
string|'"linux"'
newline|'\n'
name|'obj'
op|'.'
name|'os_boot_dev'
op|'='
string|'"hd"'
newline|'\n'
nl|'\n'
name|'disk'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'disk'
op|'.'
name|'source_type'
op|'='
string|'"file"'
newline|'\n'
name|'disk'
op|'.'
name|'source_path'
op|'='
string|'"/tmp/img"'
newline|'\n'
name|'disk'
op|'.'
name|'target_dev'
op|'='
string|'"/dev/vda"'
newline|'\n'
name|'disk'
op|'.'
name|'target_bus'
op|'='
string|'"virtio"'
newline|'\n'
nl|'\n'
name|'obj'
op|'.'
name|'add_device'
op|'('
name|'disk'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <domain type="kvm">\n              <uuid>b38a3f43-4be2-4046-897f-b67c2f5e0147</uuid>\n              <name>demo</name>\n              <memory>104857600</memory>\n              <vcpu>2</vcpu>\n              <os>\n                <type>linux</type>\n                <boot dev="hd"/>\n              </os>\n              <devices>\n                <disk type="file" device="disk">\n                  <source file="/tmp/img"/>\n                  <target bus="virtio" dev="/dev/vda"/>\n                </disk>\n              </devices>\n            </domain>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigCPUTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigCPUTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_cpu
indent|'    '
name|'def'
name|'test_config_cpu'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigCPU'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'vendor'
op|'='
string|'"AMD"'
newline|'\n'
name|'obj'
op|'.'
name|'model'
op|'='
string|'"Quad-Core AMD Opteron(tm) Processor 2350"'
newline|'\n'
name|'obj'
op|'.'
name|'arch'
op|'='
string|'"x86_64"'
newline|'\n'
name|'obj'
op|'.'
name|'add_feature'
op|'('
string|'"svm"'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'add_feature'
op|'('
string|'"extapic"'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'add_feature'
op|'('
string|'"constant_tsc"'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <cpu>\n              <arch>x86_64</arch>\n              <model>Quad-Core AMD Opteron(tm) Processor 2350</model>\n              <vendor>AMD</vendor>\n              <feature name="svm"/>\n              <feature name="extapic"/>\n              <feature name="constant_tsc"/>\n            </cpu>"""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_topology
dedent|''
name|'def'
name|'test_config_topology'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigCPU'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'vendor'
op|'='
string|'"AMD"'
newline|'\n'
name|'obj'
op|'.'
name|'sockets'
op|'='
number|'2'
newline|'\n'
name|'obj'
op|'.'
name|'cores'
op|'='
number|'4'
newline|'\n'
name|'obj'
op|'.'
name|'threads'
op|'='
number|'2'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <cpu>\n              <vendor>AMD</vendor>\n              <topology cores="4" threads="2" sockets="2"/>\n            </cpu>"""'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConfigGuestSnapshotTest
dedent|''
dedent|''
name|'class'
name|'LibvirtConfigGuestSnapshotTest'
op|'('
name|'LibvirtConfigBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_config_snapshot
indent|'    '
name|'def'
name|'test_config_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'config'
op|'.'
name|'LibvirtConfigGuestSnapshot'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|'"Demo"'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'obj'
op|'.'
name|'to_xml'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertXmlEqual'
op|'('
name|'xml'
op|','
string|'"""\n            <domainsnapshot>\n              <name>Demo</name>\n            </domainsnapshot>"""'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
