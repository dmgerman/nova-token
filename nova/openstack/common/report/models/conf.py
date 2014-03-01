begin_unit
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""Provides Openstack Configuration Model\n\nThis module defines a class representing the data\nmodel for :mod:`oslo.config` configuration options\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
op|'.'
name|'models'
op|'.'
name|'with_default_views'
name|'as'
name|'mwdv'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
op|'.'
name|'views'
op|'.'
name|'text'
op|'.'
name|'generic'
name|'as'
name|'generic_text_views'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigModel
name|'class'
name|'ConfigModel'
op|'('
name|'mwdv'
op|'.'
name|'ModelWithDefaultViews'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Configuration Options Model\n\n    This model holds data about a set of configuration options\n    from :mod:`oslo.config`.  It supports both the default group\n    of options and named option groups.\n\n    :param conf_obj: a configuration object\n    :type conf_obj: :class:`oslo.config.cfg.ConfigOpts`\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'conf_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kv_view'
op|'='
name|'generic_text_views'
op|'.'
name|'KeyValueView'
op|'('
name|'dict_sep'
op|'='
string|'": "'
op|','
nl|'\n'
name|'before_dict'
op|'='
string|"''"
op|')'
newline|'\n'
name|'super'
op|'('
name|'ConfigModel'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'text_view'
op|'='
name|'kv_view'
op|')'
newline|'\n'
nl|'\n'
DECL|function|opt_title
name|'def'
name|'opt_title'
op|'('
name|'optname'
op|','
name|'co'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'co'
op|'.'
name|'_opts'
op|'['
name|'optname'
op|']'
op|'['
string|"'opt'"
op|']'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'['
string|"'default'"
op|']'
op|'='
name|'dict'
op|'('
nl|'\n'
op|'('
name|'opt_title'
op|'('
name|'optname'
op|','
name|'conf_obj'
op|')'
op|','
name|'conf_obj'
op|'['
name|'optname'
op|']'
op|')'
nl|'\n'
name|'for'
name|'optname'
name|'in'
name|'conf_obj'
op|'.'
name|'_opts'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'groups'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'groupname'
name|'in'
name|'conf_obj'
op|'.'
name|'_groups'
op|':'
newline|'\n'
indent|'            '
name|'group_obj'
op|'='
name|'conf_obj'
op|'.'
name|'_groups'
op|'['
name|'groupname'
op|']'
newline|'\n'
name|'curr_group_opts'
op|'='
name|'dict'
op|'('
nl|'\n'
op|'('
name|'opt_title'
op|'('
name|'optname'
op|','
name|'group_obj'
op|')'
op|','
name|'conf_obj'
op|'['
name|'groupname'
op|']'
op|'['
name|'optname'
op|']'
op|')'
nl|'\n'
name|'for'
name|'optname'
name|'in'
name|'group_obj'
op|'.'
name|'_opts'
nl|'\n'
op|')'
newline|'\n'
name|'groups'
op|'['
name|'group_obj'
op|'.'
name|'name'
op|']'
op|'='
name|'curr_group_opts'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'update'
op|'('
name|'groups'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
