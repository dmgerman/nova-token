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
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
op|'.'
name|'models'
name|'import'
name|'base'
name|'as'
name|'base_model'
newline|'\n'
name|'from'
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
name|'json'
name|'import'
name|'generic'
name|'as'
name|'jsonviews'
newline|'\n'
name|'from'
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
name|'import'
name|'generic'
name|'as'
name|'textviews'
newline|'\n'
name|'from'
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
name|'xml'
name|'import'
name|'generic'
name|'as'
name|'xmlviews'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ModelWithDefaultViews
name|'class'
name|'ModelWithDefaultViews'
op|'('
name|'base_model'
op|'.'
name|'ReportModel'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Model With Default Views of Various Types\n\n    A model with default views has several predefined views,\n    each associated with a given type.  This is often used for\n    when a submodel should have an attached view, but the view\n    differs depending on the serialization format\n\n    Parameters are as the superclass, except for any\n    parameters ending in \'_view\': these parameters\n    get stored as default views.\n\n    The default \'default views\' are\n\n    text\n        :class:`openstack.common.report.views.text.generic.KeyValueView`\n    xml\n        :class:`openstack.common.report.views.xml.generic.KeyValueView`\n    json\n        :class:`openstack.common.report.views.json.generic.KeyValueView`\n\n    .. function:: to_type()\n\n       (\'type\' is one of the \'default views\' defined for this model)\n       Serializes this model using the default view for \'type\'\n\n       :rtype: str\n       :returns: this model serialized as \'type\'\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'views'
op|'='
op|'{'
nl|'\n'
string|"'text'"
op|':'
name|'textviews'
op|'.'
name|'KeyValueView'
op|'('
op|')'
op|','
nl|'\n'
string|"'json'"
op|':'
name|'jsonviews'
op|'.'
name|'KeyValueView'
op|'('
op|')'
op|','
nl|'\n'
string|"'xml'"
op|':'
name|'xmlviews'
op|'.'
name|'KeyValueView'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'newargs'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
op|'.'
name|'endswith'
op|'('
string|"'_view'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'views'
op|'['
name|'k'
op|'['
op|':'
op|'-'
number|'5'
op|']'
op|']'
op|'='
name|'kwargs'
op|'['
name|'k'
op|']'
newline|'\n'
name|'del'
name|'newargs'
op|'['
name|'k'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'super'
op|'('
name|'ModelWithDefaultViews'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'newargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_current_view_type
dedent|''
name|'def'
name|'set_current_view_type'
op|'('
name|'self'
op|','
name|'tp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'attached_view'
op|'='
name|'self'
op|'.'
name|'views'
op|'['
name|'tp'
op|']'
newline|'\n'
name|'super'
op|'('
name|'ModelWithDefaultViews'
op|','
name|'self'
op|')'
op|'.'
name|'set_current_view_type'
op|'('
name|'tp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attrname'
op|'['
op|':'
number|'3'
op|']'
op|'=='
string|"'to_'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'views'
op|'['
name|'attrname'
op|'['
number|'3'
op|':'
op|']'
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'lambda'
op|':'
name|'self'
op|'.'
name|'views'
op|'['
name|'attrname'
op|'['
number|'3'
op|':'
op|']'
op|']'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NotImplementedError'
op|'('
op|'('
nl|'\n'
string|'"Model {cn.__module__}.{cn.__name__} does not have"'
op|'+'
nl|'\n'
string|'" a default view for "'
nl|'\n'
string|'"{tp}"'
op|')'
op|'.'
name|'format'
op|'('
name|'cn'
op|'='
name|'type'
op|'('
name|'self'
op|')'
op|','
name|'tp'
op|'='
name|'attrname'
op|'['
number|'3'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'super'
op|'('
name|'ModelWithDefaultViews'
op|','
name|'self'
op|')'
op|'.'
name|'__getattr__'
op|'('
name|'attrname'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
