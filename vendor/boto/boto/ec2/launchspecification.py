begin_unit
comment|'# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
string|'"""\nRepresents a launch specification for Spot instances.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'ec2object'
name|'import'
name|'EC2Object'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'resultset'
name|'import'
name|'ResultSet'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'blockdevicemapping'
name|'import'
name|'BlockDeviceMapping'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'instance'
name|'import'
name|'Group'
newline|'\n'
nl|'\n'
DECL|class|GroupList
name|'class'
name|'GroupList'
op|'('
name|'list'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|startElement
indent|'    '
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'groupId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'append'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|class|LaunchSpecification
dedent|''
dedent|''
dedent|''
name|'class'
name|'LaunchSpecification'
op|'('
name|'EC2Object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'EC2Object'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'key_name'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'instance_type'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'groups'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'placement'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'kernel'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'ramdisk'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'monitored'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'subnet_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_in_monitoring_element'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'block_device_mapping'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'LaunchSpecification(%s)'"
op|'%'
name|'self'
op|'.'
name|'image_id'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'groupSet'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'groups'
op|'='
name|'ResultSet'
op|'('
op|'['
op|'('
string|"'item'"
op|','
name|'Group'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'groups'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'monitoring'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_in_monitoring_element'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'blockDeviceMapping'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'block_device_mapping'
op|'='
name|'BlockDeviceMapping'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'block_device_mapping'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'imageId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'keyName'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'key_name'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'instanceType'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_type'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'availabilityZone'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'placement'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'placement'"
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'kernelId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'kernel'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'ramdiskId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ramdisk'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'subnetId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'subnet_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'state'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_in_monitoring_element'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'value'
op|'=='
string|"'enabled'"
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'monitored'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_in_monitoring_element'
op|'='
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
