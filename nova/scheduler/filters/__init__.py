begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""\nScheduler host filters\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'filters'
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
DECL|class|BaseHostFilter
name|'class'
name|'BaseHostFilter'
op|'('
name|'filters'
op|'.'
name|'BaseFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for host filters."""'
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
string|'"""Return True if the object passes the filter, otherwise False."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'host_passes'
op|'('
name|'obj'
op|','
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_passes
dedent|''
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if the HostState passes the filter, otherwise False.\n        Override this in a subclass.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostFilterHandler
dedent|''
dedent|''
name|'class'
name|'HostFilterHandler'
op|'('
name|'filters'
op|'.'
name|'BaseFilterHandler'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'HostFilterHandler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'BaseHostFilter'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|all_filters
dedent|''
dedent|''
name|'def'
name|'all_filters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a list of filter classes found in this directory.\n\n    This method is used as the default for available scheduler filters\n    and should return a list of all filter classes available.\n    """'
newline|'\n'
name|'return'
name|'HostFilterHandler'
op|'('
op|')'
op|'.'
name|'get_all_classes'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|standard_filters
dedent|''
name|'def'
name|'standard_filters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deprecated.  Configs should change to use all_filters()."""'
newline|'\n'
name|'LOG'
op|'.'
name|'deprecated'
op|'('
name|'_'
op|'('
string|'"Use \'nova.scheduler.filters.all_filters\' instead "'
nl|'\n'
string|'"of \'nova.scheduler.filters.standard_filters\'"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'all_filters'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
