begin_unit
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
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
string|'"""\nFilter support\n"""'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
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
DECL|class|BaseFilter
name|'class'
name|'BaseFilter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for all filter classes."""'
newline|'\n'
DECL|member|_filter_one
name|'def'
name|'_filter_one'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if it passes the filter, False otherwise.\n        Override this in a subclass.\n        """'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|filter_all
dedent|''
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'filter_obj_list'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Yield objects that pass the filter.\n\n        Can be overriden in a subclass, if you need to base filtering\n        decisions on all objects.  Otherwise, one can just override\n        _filter_one() to filter a single object.\n        """'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'filter_obj_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_filter_one'
op|'('
name|'obj'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'obj'
newline|'\n'
nl|'\n'
comment|'# Set to true in a subclass if a filter only needs to be run once'
nl|'\n'
comment|'# for each request rather than for each instance'
nl|'\n'
DECL|variable|run_filter_once_per_request
dedent|''
dedent|''
dedent|''
name|'run_filter_once_per_request'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|run_filter_for_index
name|'def'
name|'run_filter_for_index'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if the filter needs to be run for the "index-th"\n        instance in a request.  Only need to override this if a filter\n        needs anything other than "first only" or "all" behaviour.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'run_filter_once_per_request'
name|'and'
name|'index'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseFilterHandler
dedent|''
dedent|''
dedent|''
name|'class'
name|'BaseFilterHandler'
op|'('
name|'loadables'
op|'.'
name|'BaseLoader'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class to handle loading filter classes.\n\n    This class should be subclassed where one needs to use filters.\n    """'
newline|'\n'
nl|'\n'
DECL|member|get_filtered_objects
name|'def'
name|'get_filtered_objects'
op|'('
name|'self'
op|','
name|'filter_classes'
op|','
name|'objs'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'index'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'list_objs'
op|'='
name|'list'
op|'('
name|'objs'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting with %d host(s)"'
op|')'
op|','
name|'len'
op|'('
name|'list_objs'
op|')'
op|')'
newline|'\n'
name|'for'
name|'filter_cls'
name|'in'
name|'filter_classes'
op|':'
newline|'\n'
indent|'            '
name|'cls_name'
op|'='
name|'filter_cls'
op|'.'
name|'__name__'
newline|'\n'
name|'filter'
op|'='
name|'filter_cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'filter'
op|'.'
name|'run_filter_for_index'
op|'('
name|'index'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'objs'
op|'='
name|'filter'
op|'.'
name|'filter_all'
op|'('
name|'list_objs'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'if'
name|'objs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filter %(cls_name)s says to stop filtering"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'cls_name'"
op|':'
name|'cls_name'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'list_objs'
op|'='
name|'list'
op|'('
name|'objs'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filter %(cls_name)s returned "'
nl|'\n'
string|'"%(obj_len)d host(s)"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'cls_name'"
op|':'
name|'cls_name'
op|','
string|"'obj_len'"
op|':'
name|'len'
op|'('
name|'list_objs'
op|')'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'list_objs'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'list_objs'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
