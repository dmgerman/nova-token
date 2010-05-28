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
name|'import'
name|'weakref'
newline|'\n'
nl|'\n'
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
name|'request'
name|'import'
name|'Request'
newline|'\n'
nl|'\n'
DECL|class|Instance
name|'class'
name|'Instance'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
string|"''"
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
string|"'Instance:%s'"
op|'%'
name|'self'
op|'.'
name|'instance_id'
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
name|'return'
name|'None'
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
string|"'InstanceId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_id'
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
nl|'\n'
DECL|class|AutoScalingGroup
dedent|''
dedent|''
dedent|''
name|'class'
name|'AutoScalingGroup'
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
name|'group_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'None'
op|','
name|'launch_config'
op|'='
name|'None'
op|','
nl|'\n'
name|'availability_zones'
op|'='
name|'None'
op|','
nl|'\n'
name|'load_balancers'
op|'='
name|'None'
op|','
name|'cooldown'
op|'='
number|'0'
op|','
nl|'\n'
name|'min_size'
op|'='
name|'None'
op|','
name|'max_size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Creates a new AutoScalingGroup with the specified name.\n\n        You must not have already used up your entire quota of\n        AutoScalingGroups in order for this call to be successful. Once the\n        creation request is completed, the AutoScalingGroup is ready to be\n        used in other calls.\n\n        :type name: str\n        :param name: Name of autoscaling group.\n\n        :type availability_zone: str\n        :param availability_zone: An availability zone. DEPRECATED - use the\n                                  availability_zones parameter, which expects\n                                  a list of availability zone\n                                  strings\n\n        :type availability_zone: list\n        :param availability_zone: List of availability zones.\n\n        :type launch_config: str\n        :param launch_config: Name of launch configuration name.\n\n        :type load_balancers: list\n        :param load_balancers: List of load balancers.\n\n        :type minsize: int\n        :param minsize: Minimum size of group\n\n        :type maxsize: int\n        :param maxsize: Maximum size of group\n\n        :type cooldown: int\n        :param cooldown: Amount of time after a Scaling Activity completes\n                         before any further scaling activities can start.\n\n        :rtype: tuple\n        :return: Updated healthcheck for the instances.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'group_name'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'min_size'
op|'='
name|'min_size'
newline|'\n'
name|'self'
op|'.'
name|'max_size'
op|'='
name|'max_size'
newline|'\n'
name|'self'
op|'.'
name|'created_time'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'cooldown'
op|'='
name|'cooldown'
newline|'\n'
name|'self'
op|'.'
name|'launch_config'
op|'='
name|'launch_config'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'launch_config'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'launch_config_name'
op|'='
name|'self'
op|'.'
name|'launch_config'
op|'.'
name|'name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'launch_config_name'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'desired_capacity'
op|'='
name|'None'
newline|'\n'
name|'lbs'
op|'='
name|'load_balancers'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'load_balancers'
op|'='
name|'ListElement'
op|'('
name|'lbs'
op|')'
newline|'\n'
name|'zones'
op|'='
name|'availability_zones'
name|'or'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|'='
name|'availability_zone'
newline|'\n'
name|'self'
op|'.'
name|'availability_zones'
op|'='
name|'ListElement'
op|'('
name|'zones'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
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
string|"'AutoScalingGroup:%s'"
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
string|"'Instances'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instances'
op|'='
name|'ResultSet'
op|'('
op|'['
op|'('
string|"'member'"
op|','
name|'Instance'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instances'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'LoadBalancerNames'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'load_balancers'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'AvailabilityZones'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'availability_zones'
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
string|"'MinSize'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'min_size'
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
string|"'Cooldown'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cooldown'
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
name|'launch_config_name'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'DesiredCapacity'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'desired_capacity'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'MaxSize'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'max_size'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'AutoScalingGroupName'"
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
DECL|member|set_capacity
dedent|''
dedent|''
name|'def'
name|'set_capacity'
op|'('
name|'self'
op|','
name|'capacity'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Set the desired capacity for the group. """'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'AutoScalingGroupName'"
op|':'
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'DesiredCapacity'"
op|':'
name|'capacity'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_object'
op|'('
string|"'SetDesiredCapacity'"
op|','
name|'params'
op|','
nl|'\n'
name|'Request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'last_request'
op|'='
name|'req'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Sync local changes with AutoScaling group. """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'_update_group'
op|'('
string|"'UpdateAutoScalingGroup'"
op|','
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|shutdown_instances
dedent|''
name|'def'
name|'shutdown_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Convenience method which shuts down all instances associated with\n        this group.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'min_size'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'max_size'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'update'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_triggers
dedent|''
name|'def'
name|'get_all_triggers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Get all triggers for this auto scaling group. """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'AutoScalingGroupName'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'triggers'
op|'='
name|'self'
op|'.'
name|'connection'
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
comment|'# allow triggers to be able to access the autoscale group'
nl|'\n'
name|'for'
name|'tr'
name|'in'
name|'triggers'
op|':'
newline|'\n'
indent|'            '
name|'tr'
op|'.'
name|'autoscale_group'
op|'='
name|'weakref'
op|'.'
name|'proxy'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'triggers'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Delete this auto-scaling group. """'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'AutoScalingGroupName'"
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
string|"'DeleteAutoScalingGroup'"
op|','
name|'params'
op|','
nl|'\n'
name|'Request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_activities
dedent|''
name|'def'
name|'get_activities'
op|'('
name|'self'
op|','
name|'activity_ids'
op|'='
name|'None'
op|','
name|'max_records'
op|'='
number|'100'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get all activies for this group.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_all_activities'
op|'('
name|'self'
op|','
name|'activity_ids'
op|','
name|'max_records'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
