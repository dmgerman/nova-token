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
string|'"""\nThis module provides an interface to the Elastic Compute Cloud (EC2)\nAuto Scaling service.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'connection'
name|'import'
name|'AWSQueryConnection'
newline|'\n'
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
name|'autoscale'
op|'.'
name|'trigger'
name|'import'
name|'Trigger'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'autoscale'
op|'.'
name|'launchconfig'
name|'import'
name|'LaunchConfiguration'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'autoscale'
op|'.'
name|'group'
name|'import'
name|'AutoScalingGroup'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'autoscale'
op|'.'
name|'activity'
name|'import'
name|'Activity'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AutoScaleConnection
name|'class'
name|'AutoScaleConnection'
op|'('
name|'AWSQueryConnection'
op|')'
op|':'
newline|'\n'
DECL|variable|APIVersion
indent|'    '
name|'APIVersion'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Boto'"
op|','
string|"'autoscale_version'"
op|','
string|"'2009-05-15'"
op|')'
newline|'\n'
DECL|variable|Endpoint
name|'Endpoint'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Boto'"
op|','
string|"'autoscale_endpoint'"
op|','
nl|'\n'
string|"'autoscaling.amazonaws.com'"
op|')'
newline|'\n'
DECL|variable|SignatureVersion
name|'SignatureVersion'
op|'='
string|"'2'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'aws_access_key_id'
op|'='
name|'None'
op|','
name|'aws_secret_access_key'
op|'='
name|'None'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'True'
op|','
name|'port'
op|'='
name|'None'
op|','
name|'proxy'
op|'='
name|'None'
op|','
name|'proxy_port'
op|'='
name|'None'
op|','
nl|'\n'
name|'proxy_user'
op|'='
name|'None'
op|','
name|'proxy_pass'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'Endpoint'
op|','
name|'debug'
op|'='
number|'1'
op|','
nl|'\n'
name|'https_connection_factory'
op|'='
name|'None'
op|','
name|'region'
op|'='
name|'None'
op|','
name|'path'
op|'='
string|"'/'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Init method to create a new connection to the AutoScaling service.\n\n        B{Note:} The host argument is overridden by the host specified in the\n                 boto configuration file.\n        """'
newline|'\n'
name|'AWSQueryConnection'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'aws_access_key_id'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|','
name|'is_secure'
op|','
name|'port'
op|','
name|'proxy'
op|','
name|'proxy_port'
op|','
nl|'\n'
name|'proxy_user'
op|','
name|'proxy_pass'
op|','
name|'host'
op|','
name|'debug'
op|','
nl|'\n'
name|'https_connection_factory'
op|','
name|'path'
op|'='
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_list_params
dedent|''
name|'def'
name|'build_list_params'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'items'
op|','
name|'label'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" items is a list of dictionaries or strings:\n                [{\'Protocol\' : \'HTTP\',\n                 \'LoadBalancerPort\' : \'80\',\n                 \'InstancePort\' : \'80\'},..] etc.\n             or\n                [\'us-east-1b\',...]\n        """'
newline|'\n'
comment|'# different from EC2 list params'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'items'
op|')'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'items'
op|'['
name|'i'
op|'-'
number|'1'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'items'
op|'['
name|'i'
op|'-'
number|'1'
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'params'
op|'['
string|"'%s.member.%d.%s'"
op|'%'
op|'('
name|'label'
op|','
name|'i'
op|','
name|'k'
op|')'
op|']'
op|'='
name|'v'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'items'
op|'['
name|'i'
op|'-'
number|'1'
op|']'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'['
string|"'%s.member.%d'"
op|'%'
op|'('
name|'label'
op|','
name|'i'
op|')'
op|']'
op|'='
name|'items'
op|'['
name|'i'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_update_group
dedent|''
dedent|''
dedent|''
name|'def'
name|'_update_group'
op|'('
name|'self'
op|','
name|'op'
op|','
name|'as_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'AutoScalingGroupName'"
op|':'
name|'as_group'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'Cooldown'"
op|':'
name|'as_group'
op|'.'
name|'cooldown'
op|','
nl|'\n'
string|"'LaunchConfigurationName'"
op|':'
name|'as_group'
op|'.'
name|'launch_config_name'
op|','
nl|'\n'
string|"'MinSize'"
op|':'
name|'as_group'
op|'.'
name|'min_size'
op|','
nl|'\n'
string|"'MaxSize'"
op|':'
name|'as_group'
op|'.'
name|'max_size'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'op'
op|'.'
name|'startswith'
op|'('
string|"'Create'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'as_group'
op|'.'
name|'availability_zones'
op|':'
newline|'\n'
indent|'                '
name|'zones'
op|'='
name|'self'
op|'.'
name|'availability_zones'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'zones'
op|'='
op|'['
name|'as_group'
op|'.'
name|'availability_zone'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'as_group'
op|'.'
name|'load_balancers'
op|','
nl|'\n'
string|"'LoadBalancerNames'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'zones'
op|','
nl|'\n'
string|"'AvailabilityZones'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_object'
op|'('
name|'op'
op|','
name|'params'
op|','
name|'Request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_auto_scaling_group
dedent|''
name|'def'
name|'create_auto_scaling_group'
op|'('
name|'self'
op|','
name|'as_group'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create auto scaling group.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_update_group'
op|'('
string|"'CreateAutoScalingGroup'"
op|','
name|'as_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_launch_configuration
dedent|''
name|'def'
name|'create_launch_configuration'
op|'('
name|'self'
op|','
name|'launch_config'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Creates a new Launch Configuration.\n\n        :type launch_config: boto.ec2.autoscale.launchconfig.LaunchConfiguration\n        :param launch_config: LaunchConfiguraiton object.\n\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'ImageId'"
op|':'
name|'launch_config'
op|'.'
name|'image_id'
op|','
nl|'\n'
string|"'KeyName'"
op|':'
name|'launch_config'
op|'.'
name|'key_name'
op|','
nl|'\n'
string|"'LaunchConfigurationName'"
op|':'
name|'launch_config'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'InstanceType'"
op|':'
name|'launch_config'
op|'.'
name|'instance_type'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'launch_config'
op|'.'
name|'user_data'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'UserData'"
op|']'
op|'='
name|'launch_config'
op|'.'
name|'user_data'
newline|'\n'
dedent|''
name|'if'
name|'launch_config'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'KernelId'"
op|']'
op|'='
name|'launch_config'
op|'.'
name|'kernel_id'
newline|'\n'
dedent|''
name|'if'
name|'launch_config'
op|'.'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'RamdiskId'"
op|']'
op|'='
name|'launch_config'
op|'.'
name|'ramdisk_id'
newline|'\n'
dedent|''
name|'if'
name|'launch_config'
op|'.'
name|'block_device_mappings'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'launch_config'
op|'.'
name|'block_device_mappings'
op|','
nl|'\n'
string|"'BlockDeviceMappings'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'launch_config'
op|'.'
name|'security_groups'
op|','
nl|'\n'
string|"'SecurityGroups'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_object'
op|'('
string|"'CreateLaunchConfiguration'"
op|','
name|'params'
op|','
nl|'\n'
name|'Request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_trigger
dedent|''
name|'def'
name|'create_trigger'
op|'('
name|'self'
op|','
name|'trigger'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'TriggerName'"
op|':'
name|'trigger'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'AutoScalingGroupName'"
op|':'
name|'trigger'
op|'.'
name|'autoscale_group'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'MeasureName'"
op|':'
name|'trigger'
op|'.'
name|'measure_name'
op|','
nl|'\n'
string|"'Statistic'"
op|':'
name|'trigger'
op|'.'
name|'statistic'
op|','
nl|'\n'
string|"'Period'"
op|':'
name|'trigger'
op|'.'
name|'period'
op|','
nl|'\n'
string|"'Unit'"
op|':'
name|'trigger'
op|'.'
name|'unit'
op|','
nl|'\n'
string|"'LowerThreshold'"
op|':'
name|'trigger'
op|'.'
name|'lower_threshold'
op|','
nl|'\n'
string|"'LowerBreachScaleIncrement'"
op|':'
name|'trigger'
op|'.'
name|'lower_breach_scale_increment'
op|','
nl|'\n'
string|"'UpperThreshold'"
op|':'
name|'trigger'
op|'.'
name|'upper_threshold'
op|','
nl|'\n'
string|"'UpperBreachScaleIncrement'"
op|':'
name|'trigger'
op|'.'
name|'upper_breach_scale_increment'
op|','
nl|'\n'
string|"'BreachDuration'"
op|':'
name|'trigger'
op|'.'
name|'breach_duration'
op|'}'
newline|'\n'
comment|'# dimensions should be a list of tuples'
nl|'\n'
name|'dimensions'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'dim'
name|'in'
name|'trigger'
op|'.'
name|'dimensions'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|','
name|'value'
op|'='
name|'dim'
newline|'\n'
name|'dimensions'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'Name'
op|'='
name|'name'
op|','
name|'Value'
op|'='
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'dimensions'
op|','
string|"'Dimensions'"
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'get_object'
op|'('
string|"'CreateOrUpdateScalingTrigger'"
op|','
name|'params'
op|','
nl|'\n'
name|'Request'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|get_all_groups
dedent|''
name|'def'
name|'get_all_groups'
op|'('
name|'self'
op|','
name|'names'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'names'
op|','
string|"'AutoScalingGroupNames'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_list'
op|'('
string|"'DescribeAutoScalingGroups'"
op|','
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'member'"
op|','
name|'AutoScalingGroup'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_launch_configurations
dedent|''
name|'def'
name|'get_all_launch_configurations'
op|'('
name|'self'
op|','
name|'names'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        """'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'names'
op|','
string|"'LaunchConfigurationNames'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_list'
op|'('
string|"'DescribeLaunchConfigurations'"
op|','
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'member'"
op|','
name|'LaunchConfiguration'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_activities
dedent|''
name|'def'
name|'get_all_activities'
op|'('
name|'self'
op|','
name|'autoscale_group'
op|','
nl|'\n'
name|'activity_ids'
op|'='
name|'None'
op|','
nl|'\n'
name|'max_records'
op|'='
number|'100'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get all activities for the given autoscaling group.\n\n        :type autoscale_group: str or AutoScalingGroup object\n        :param autoscale_group: The auto scaling group to get activities on.\n\n        @max_records: int\n        :param max_records: Maximum amount of activities to return.\n        """'
newline|'\n'
name|'name'
op|'='
name|'autoscale_group'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'autoscale_group'
op|','
name|'AutoScalingGroup'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'autoscale_group'
op|'.'
name|'name'
newline|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'AutoScalingGroupName'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'if'
name|'activity_ids'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'build_list_params'
op|'('
name|'params'
op|','
name|'activity_ids'
op|','
string|"'ActivityIds'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_list'
op|'('
string|"'DescribeScalingActivities'"
op|','
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'member'"
op|','
name|'Activity'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_triggers
dedent|''
name|'def'
name|'get_all_triggers'
op|'('
name|'self'
op|','
name|'autoscale_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'AutoScalingGroupName'"
op|':'
name|'autoscale_group'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_list'
op|'('
string|"'DescribeTriggers'"
op|','
name|'params'
op|','
nl|'\n'
op|'['
op|'('
string|"'member'"
op|','
name|'Trigger'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|terminate_instance
dedent|''
name|'def'
name|'terminate_instance'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'decrement_capacity'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'InstanceId'"
op|':'
name|'instance_id'
op|','
nl|'\n'
string|"'ShouldDecrementDesiredCapacity'"
op|':'
name|'decrement_capacity'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'get_object'
op|'('
string|"'TerminateInstanceInAutoScalingGroup'"
op|','
name|'params'
op|','
nl|'\n'
name|'Activity'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
