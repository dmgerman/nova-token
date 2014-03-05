begin_unit
comment|'# Copyright 2013 Intel Corporation.'
nl|'\n'
comment|'# All Rights Reserved.'
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
string|'"""\nResource monitor API specification.\n\nResourceMonitorBase provides the definition of minimum set of methods\nthat needs to be implemented by Resource Monitor.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'types'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'loadables'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
DECL|variable|compute_monitors_opts
name|'compute_monitors_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'compute_available_monitors'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.compute.monitors.all_monitors'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Monitor classes available to the compute which may '"
nl|'\n'
string|"'be specified more than once.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'compute_monitors'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'A list of monitors that can be used for getting '"
nl|'\n'
string|"'compute metrics.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'compute_monitors_opts'
op|')'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceMonitorMeta
name|'class'
name|'ResourceMonitorMeta'
op|'('
name|'type'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'cls'
op|','
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Metaclass that allows us to create a function map and call it later\n        to get the metric names and their values.\n        """'
newline|'\n'
name|'super'
op|'('
name|'ResourceMonitorMeta'
op|','
name|'cls'
op|')'
op|'.'
name|'__init__'
op|'('
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
newline|'\n'
nl|'\n'
name|'prefix'
op|'='
string|"'_get_'"
newline|'\n'
name|'prefix_len'
op|'='
name|'len'
op|'('
name|'prefix'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'metric_map'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'name'
op|','
name|'value'
name|'in'
name|'cls'
op|'.'
name|'__dict__'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'len'
op|'('
name|'name'
op|')'
op|'>'
name|'prefix_len'
nl|'\n'
name|'and'
name|'name'
op|'['
op|':'
name|'prefix_len'
op|']'
op|'=='
name|'prefix'
nl|'\n'
name|'and'
name|'isinstance'
op|'('
name|'value'
op|','
name|'types'
op|'.'
name|'FunctionType'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'metric_name'
op|'='
name|'name'
op|'['
name|'prefix_len'
op|':'
op|']'
op|'.'
name|'replace'
op|'('
string|"'_'"
op|','
string|"'.'"
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'metric_map'
op|'['
name|'metric_name'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'six'
op|'.'
name|'add_metaclass'
op|'('
name|'ResourceMonitorMeta'
op|')'
newline|'\n'
DECL|class|ResourceMonitorBase
name|'class'
name|'ResourceMonitorBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for resource monitors\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'parent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_manager'
op|'='
name|'parent'
newline|'\n'
name|'self'
op|'.'
name|'source'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|add_timestamp
name|'def'
name|'add_timestamp'
op|'('
name|'arg'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Decorator to indicate that a method needs to add a timestamp.\n\n        When a function returning a value is decorated by the decorator,\n        which means a timestamp should be added into the returned value.\n        That is, a tuple (value, timestamp) is returned.\n\n        The timestamp is the time when we update the value in the _data.\n\n        If users hope to define how the timestamp is got by themselves,\n        they should not use this decorator in their own classes.\n        """'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'cls'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
op|'('
name|'cls'
op|','
op|'**'
name|'kwargs'
op|')'
op|','
name|'cls'
op|'.'
name|'_data'
op|'.'
name|'get'
op|'('
string|'"timestamp"'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
DECL|member|_update_data
dedent|''
name|'def'
name|'_update_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Method to update the metrics data.\n\n        Each subclass can implement this method to update metrics\n        into _data. It will be called in get_metrics.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_metric_names
dedent|''
name|'def'
name|'get_metric_names'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get available metric names.\n\n        Get available metric names, which are represented by a set of keys\n        that can be used to check conflicts and duplications\n        :returns: a set of keys representing metrics names\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'metric_map'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_metrics
dedent|''
name|'def'
name|'get_metrics'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get metrics.\n\n        Get metrics, which are represented by a list of dictionaries\n        [{\'name\': metric name,\n          \'value\': metric value,\n          \'timestamp\': the time when the value is retrieved,\n          \'source\': what the value is got by}, ...]\n        :param kwargs: extra arguments that might be present\n        :returns: a list to tell the current metrics\n        """'
newline|'\n'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_update_data'
op|'('
op|')'
newline|'\n'
name|'for'
name|'name'
op|','
name|'func'
name|'in'
name|'self'
op|'.'
name|'metric_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'func'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'data'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_populate'
op|'('
name|'name'
op|','
name|'ret'
op|'['
number|'0'
op|']'
op|','
name|'ret'
op|'['
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|_populate
dedent|''
name|'def'
name|'_populate'
op|'('
name|'self'
op|','
name|'metric_name'
op|','
name|'metric_value'
op|','
name|'timestamp'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Populate the format what we want from metric name and metric value\n        """'
newline|'\n'
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'result'
op|'['
string|"'name'"
op|']'
op|'='
name|'metric_name'
newline|'\n'
name|'result'
op|'['
string|"'value'"
op|']'
op|'='
name|'metric_value'
newline|'\n'
name|'result'
op|'['
string|"'timestamp'"
op|']'
op|'='
name|'timestamp'
name|'or'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'result'
op|'['
string|"'source'"
op|']'
op|'='
name|'self'
op|'.'
name|'source'
newline|'\n'
nl|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceMonitorHandler
dedent|''
dedent|''
name|'class'
name|'ResourceMonitorHandler'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class to handle loading monitor classes.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ResourceMonitorHandler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ResourceMonitorBase'
op|')'
newline|'\n'
nl|'\n'
DECL|member|choose_monitors
dedent|''
name|'def'
name|'choose_monitors'
op|'('
name|'self'
op|','
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This function checks the monitor names and metrics names against a\n        predefined set of acceptable monitors.\n        """'
newline|'\n'
name|'monitor_classes'
op|'='
name|'self'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'compute_available_monitors'
op|')'
newline|'\n'
name|'monitor_class_map'
op|'='
name|'dict'
op|'('
op|'('
name|'cls'
op|'.'
name|'__name__'
op|','
name|'cls'
op|')'
nl|'\n'
name|'for'
name|'cls'
name|'in'
name|'monitor_classes'
op|')'
newline|'\n'
name|'monitor_cls_names'
op|'='
name|'CONF'
op|'.'
name|'compute_monitors'
newline|'\n'
name|'good_monitors'
op|'='
op|'['
op|']'
newline|'\n'
name|'bad_monitors'
op|'='
op|'['
op|']'
newline|'\n'
name|'metric_names'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'monitor_name'
name|'in'
name|'monitor_cls_names'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'monitor_name'
name|'not'
name|'in'
name|'monitor_class_map'
op|':'
newline|'\n'
indent|'                '
name|'bad_monitors'
op|'.'
name|'append'
op|'('
name|'monitor_name'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# make sure different monitors do not have the same'
nl|'\n'
comment|'# metric name'
nl|'\n'
indent|'                '
name|'monitor'
op|'='
name|'monitor_class_map'
op|'['
name|'monitor_name'
op|']'
op|'('
name|'manager'
op|')'
newline|'\n'
name|'metric_names_tmp'
op|'='
name|'set'
op|'('
name|'monitor'
op|'.'
name|'get_metric_names'
op|'('
op|')'
op|')'
newline|'\n'
name|'overlap'
op|'='
name|'metric_names'
op|'&'
name|'metric_names_tmp'
newline|'\n'
name|'if'
name|'not'
name|'overlap'
op|':'
newline|'\n'
indent|'                    '
name|'metric_names'
op|'='
name|'metric_names'
op|'|'
name|'metric_names_tmp'
newline|'\n'
name|'good_monitors'
op|'.'
name|'append'
op|'('
name|'monitor'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Excluding monitor %(monitor_name)s due to "'
nl|'\n'
string|'"metric name overlap; overlapping "'
nl|'\n'
string|'"metrics: %(overlap)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'monitor_name'"
op|':'
name|'monitor_name'
op|','
nl|'\n'
string|"'overlap'"
op|':'
string|"', '"
op|'.'
name|'join'
op|'('
name|'overlap'
op|')'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'bad_monitors'
op|'.'
name|'append'
op|'('
name|'monitor_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Monitor %(monitor_name)s cannot be used: %(ex)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'monitor_name'"
op|':'
name|'monitor_name'
op|','
string|"'ex'"
op|':'
name|'ex'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'bad_monitors'
op|'.'
name|'append'
op|'('
name|'monitor_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'bad_monitors'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"The following monitors have been disabled: %s"'
op|')'
op|','
nl|'\n'
string|"', '"
op|'.'
name|'join'
op|'('
name|'bad_monitors'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'good_monitors'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|all_monitors
dedent|''
dedent|''
name|'def'
name|'all_monitors'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a list of monitor classes found in this directory.\n\n    This method is used as the default for available monitors\n    and should return a list of all monitor classes avaiable.\n    """'
newline|'\n'
name|'return'
name|'ResourceMonitorHandler'
op|'('
op|')'
op|'.'
name|'get_all_classes'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
