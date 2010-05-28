begin_unit
comment|'# Copyright (c) 2009 Reza Lotun http://reza.lotun.name/'
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
nl|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'autoscale'
op|'.'
name|'request'
name|'import'
name|'Request'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'elb'
op|'.'
name|'listelement'
name|'import'
name|'ListElement'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LaunchConfiguration
name|'class'
name|'LaunchConfiguration'
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
name|'connection'
op|'='
name|'None'
op|','
name|'name'
op|'='
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'key_name'
op|'='
name|'None'
op|','
name|'security_groups'
op|'='
name|'None'
op|','
name|'user_data'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.small'"
op|','
name|'kernel_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'ramdisk_id'
op|'='
name|'None'
op|','
name|'block_device_mappings'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        A launch configuration.\n\n        :type name: str\n        :param name: Name of the launch configuration to create.\n\n        :type image_id: str\n        :param image_id: Unique ID of the Amazon Machine Image (AMI) which was\n                         assigned during registration.\n\n        :type key_name: str\n        :param key_name: The name of the EC2 key pair.\n\n        :type security_groups: list\n        :param security_groups: Names of the security groups with which to\n                                associate the EC2 instances.\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'instance_type'
op|'='
name|'instance_type'
newline|'\n'
name|'self'
op|'.'
name|'block_device_mappings'
op|'='
name|'block_device_mappings'
newline|'\n'
name|'self'
op|'.'
name|'key_name'
op|'='
name|'key_name'
newline|'\n'
name|'sec_groups'
op|'='
name|'security_groups'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'security_groups'
op|'='
name|'ListElement'
op|'('
name|'sec_groups'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'ramdisk_id'
op|'='
name|'ramdisk_id'
newline|'\n'
name|'self'
op|'.'
name|'created_time'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'kernel_id'
op|'='
name|'kernel_id'
newline|'\n'
name|'self'
op|'.'
name|'user_data'
op|'='
name|'user_data'
newline|'\n'
name|'self'
op|'.'
name|'created_time'
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
string|"'LaunchConfiguration:%s'"
op|'%'
name|'self'
op|'.'
name|'name'
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
string|"'SecurityGroups'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'security_groups'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
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
string|"'InstanceType'"
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
string|"'LaunchConfigurationName'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'name'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'KeyName'"
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
string|"'ImageId'"
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
string|"'CreatedTime'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'created_time'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'KernelId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'kernel_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'RamdiskId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ramdisk_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'UserData'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'user_data'
op|'='
name|'value'
newline|'\n'
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
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Delete this launch configuration. """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'LaunchConfigurationName'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_object'
op|'('
string|"'DeleteLaunchConfiguration'"
op|','
name|'params'
op|','
nl|'\n'
name|'Request'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
