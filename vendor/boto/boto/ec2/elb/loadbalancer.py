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
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'elb'
op|'.'
name|'healthcheck'
name|'import'
name|'HealthCheck'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'elb'
op|'.'
name|'listener'
name|'import'
name|'Listener'
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
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'instanceinfo'
name|'import'
name|'InstanceInfo'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'resultset'
name|'import'
name|'ResultSet'
newline|'\n'
nl|'\n'
DECL|class|LoadBalancer
name|'class'
name|'LoadBalancer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Represents an EC2 Load Balancer\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'endpoints'
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
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'listeners'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'health_check'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'dns_name'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'created_time'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'availability_zones'
op|'='
name|'ListElement'
op|'('
op|')'
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
string|"'LoadBalancer:%s'"
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
string|"'HealthCheck'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'health_check'
op|'='
name|'HealthCheck'
op|'('
name|'self'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'health_check'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'Listeners'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'listeners'
op|'='
name|'ResultSet'
op|'('
op|'['
op|'('
string|"'member'"
op|','
name|'Listener'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'listeners'
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
name|'elif'
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
name|'InstanceInfo'
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
string|"'LoadBalancerName'"
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
string|"'DNSName'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'dns_name'
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
string|"'InstanceId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instances'
op|'.'
name|'append'
op|'('
name|'value'
op|')'
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
DECL|member|enable_zones
dedent|''
dedent|''
name|'def'
name|'enable_zones'
op|'('
name|'self'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Enable availability zones to this Access Point.\n        All zones must be in the same region as the Access Point.\n\n        :type zones: string or List of strings\n        :param zones: The name of the zone(s) to add.\n\n        """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'zones'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'zones'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'zones'
op|'='
op|'['
name|'zones'
op|']'
newline|'\n'
dedent|''
name|'new_zones'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'enable_availability_zones'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'zones'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'availability_zones'
op|'='
name|'new_zones'
newline|'\n'
nl|'\n'
DECL|member|disable_zones
dedent|''
name|'def'
name|'disable_zones'
op|'('
name|'self'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Disable availability zones from this Access Point.\n\n        :type zones: string or List of strings\n        :param zones: The name of the zone(s) to add.\n\n        """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'zones'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'zones'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'zones'
op|'='
op|'['
name|'zones'
op|']'
newline|'\n'
dedent|''
name|'new_zones'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'disable_availability_zones'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'zones'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'availability_zones'
op|'='
name|'new_zones'
newline|'\n'
nl|'\n'
DECL|member|register_instances
dedent|''
name|'def'
name|'register_instances'
op|'('
name|'self'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add instances to this Load Balancer\n        All instances must be in the same region as the Load Balancer.\n        Adding endpoints that are already registered with the Load Balancer\n        has no effect.\n\n        :type zones: string or List of instance id\'s\n        :param zones: The name of the endpoint(s) to add.\n\n        """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instances'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'instances'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'='
op|'['
name|'instances'
op|']'
newline|'\n'
dedent|''
name|'new_instances'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'register_instances'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'='
name|'new_instances'
newline|'\n'
nl|'\n'
DECL|member|deregister_instances
dedent|''
name|'def'
name|'deregister_instances'
op|'('
name|'self'
op|','
name|'instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove instances from this Load Balancer.\n        Removing instances that are not registered with the Load Balancer\n        has no effect.\n\n        :type zones: string or List of instance id\'s\n        :param zones: The name of the endpoint(s) to add.\n\n        """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instances'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'instances'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'='
op|'['
name|'instances'
op|']'
newline|'\n'
dedent|''
name|'new_instances'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'deregister_instances'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'='
name|'new_instances'
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
string|'"""\n        Delete this load balancer\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'delete_load_balancer'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|configure_health_check
dedent|''
name|'def'
name|'configure_health_check'
op|'('
name|'self'
op|','
name|'health_check'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'configure_health_check'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'health_check'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_health
dedent|''
name|'def'
name|'get_instance_health'
op|'('
name|'self'
op|','
name|'instances'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'.'
name|'describe_instance_health'
op|'('
name|'self'
op|'.'
name|'name'
op|','
name|'instances'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
