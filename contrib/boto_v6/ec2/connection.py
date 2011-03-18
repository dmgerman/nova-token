begin_unit
string|"'''\nCreated on 2010/12/20\n\n@author: Nachi Ueno <ueno.nachi@lab.ntt.co.jp>\n'''"
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'import'
name|'boto'
op|'.'
name|'ec2'
newline|'\n'
name|'from'
name|'boto_v6'
op|'.'
name|'ec2'
op|'.'
name|'instance'
name|'import'
name|'ReservationV6'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EC2ConnectionV6
name|'class'
name|'EC2ConnectionV6'
op|'('
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'EC2Connection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''\n    EC2Connection for OpenStack IPV6 mode\n    '''"
newline|'\n'
DECL|member|get_all_instances
name|'def'
name|'get_all_instances'
op|'('
name|'self'
op|','
name|'instance_ids'
op|'='
name|'None'
op|','
name|'filters'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Retrieve all the instances associated with your account.\n\n        :type instance_ids: list\n        :param instance_ids: A list of strings of instance IDs\n\n        :type filters: dict\n        :param filters: Optional filters that can be used to limit\n                        the results returned.  Filters are provided\n                        in the form of a dictionary consisting of\n                        filter names as the key and filter values\n                        as the value.  The set of allowable filter\n                        names/values is dependent on the request\n                        being performed.  Check the EC2 API guide\n                        for details.\n\n        :rtype: list\n        :return: A list of  :class:`boto.ec2.instance.Reservation`\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'instance_ids'
op|','
string|"'InstanceId'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'filters'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_filter_params'
op|'('
name|'params'
op|','
name|'filters'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_list'
op|'('
string|"'DescribeInstancesV6'"
op|','
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'item'"
op|','
name|'ReservationV6'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_instances
dedent|''
name|'def'
name|'run_instances'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'min_count'
op|'='
number|'1'
op|','
name|'max_count'
op|'='
number|'1'
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
nl|'\n'
name|'user_data'
op|'='
name|'None'
op|','
name|'addressing_type'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.small'"
op|','
name|'placement'
op|'='
name|'None'
op|','
nl|'\n'
name|'kernel_id'
op|'='
name|'None'
op|','
name|'ramdisk_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'monitoring_enabled'
op|'='
name|'False'
op|','
name|'subnet_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'block_device_map'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Runs an image on EC2.\n\n        :type image_id: string\n        :param image_id: The ID of the image to run\n\n        :type min_count: int\n        :param min_count: The minimum number of instances to launch\n\n        :type max_count: int\n        :param max_count: The maximum number of instances to launch\n\n        :type key_name: string\n        :param key_name: The name of the key pair with which to\n                         launch instances\n\n        :type security_groups: list of strings\n        :param security_groups: The names of the security groups with\n                                which to associate instances\n\n        :type user_data: string\n        :param user_data: The user data passed to the launched instances\n\n        :type instance_type: string\n        :param instance_type: The type of instance to run\n                              (m1.small, m1.large, m1.xlarge)\n\n        :type placement: string\n        :param placement: The availability zone in which to launch\n                          the instances\n\n        :type kernel_id: string\n        :param kernel_id: The ID of the kernel with which to\n                          launch the instances\n\n        :type ramdisk_id: string\n        :param ramdisk_id: The ID of the RAM disk with which to\n                           launch the instances\n\n        :type monitoring_enabled: bool\n        :param monitoring_enabled: Enable CloudWatch monitoring\n                                   on the instance.\n\n        :type subnet_id: string\n        :param subnet_id: The subnet ID within which to launch\n                          the instances for VPC.\n\n        :type block_device_map:\n            :class:`boto.ec2.blockdevicemapping.BlockDeviceMapping`\n        :param block_device_map: A BlockDeviceMapping data structure\n                                 describing the EBS volumes associated\n                                 with the Image.\n\n        :rtype: Reservation\n        :return: The :class:`boto.ec2.instance.Reservation`\n                 associated with the request for machines\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'ImageId'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'MinCount'"
op|':'
name|'min_count'
op|','
nl|'\n'
string|"'MaxCount'"
op|':'
name|'max_count'
op|'}'
newline|'\n'
name|'if'
name|'key_name'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'KeyName'"
op|']'
op|'='
name|'key_name'
newline|'\n'
dedent|''
name|'if'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'group'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'group'
op|','
name|'SecurityGroup'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'l'
op|'.'
name|'append'
op|'('
name|'group'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'l'
op|'.'
name|'append'
op|'('
name|'group'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'l'
op|','
string|"'SecurityGroup'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'user_data'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'UserData'"
op|']'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'user_data'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'addressing_type'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'AddressingType'"
op|']'
op|'='
name|'addressing_type'
newline|'\n'
dedent|''
name|'if'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'InstanceType'"
op|']'
op|'='
name|'instance_type'
newline|'\n'
dedent|''
name|'if'
name|'placement'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'Placement.AvailabilityZone'"
op|']'
op|'='
name|'placement'
newline|'\n'
dedent|''
name|'if'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'KernelId'"
op|']'
op|'='
name|'kernel_id'
newline|'\n'
dedent|''
name|'if'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'RamdiskId'"
op|']'
op|'='
name|'ramdisk_id'
newline|'\n'
dedent|''
name|'if'
name|'monitoring_enabled'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'Monitoring.Enabled'"
op|']'
op|'='
string|"'true'"
newline|'\n'
dedent|''
name|'if'
name|'subnet_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'SubnetId'"
op|']'
op|'='
name|'subnet_id'
newline|'\n'
dedent|''
name|'if'
name|'block_device_map'
op|':'
newline|'\n'
indent|'            '
name|'block_device_map'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_object'
op|'('
string|"'RunInstances'"
op|','
name|'params'
op|','
nl|'\n'
name|'ReservationV6'
op|','
name|'verb'
op|'='
string|"'POST'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
