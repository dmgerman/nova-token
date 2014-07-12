begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
name|'as'
name|'bmdb'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
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
DECL|class|BareMetalVIFDriver
name|'class'
name|'BareMetalVIFDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_after_plug
indent|'    '
name|'def'
name|'_after_plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|','
name|'pif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_after_unplug
dedent|''
name|'def'
name|'_after_unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|','
name|'pif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"plug: instance_uuid=%(uuid)s vif=%(vif)s"'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'vif'"
op|':'
name|'vif'
op|'}'
op|')'
newline|'\n'
name|'vif_uuid'
op|'='
name|'vif'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'bmdb'
op|'.'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'ctx'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(deva): optimize this database query'
nl|'\n'
comment|'#             this is just searching for a free physical interface'
nl|'\n'
name|'pifs'
op|'='
name|'bmdb'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'ctx'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'pif'
name|'in'
name|'pifs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'pif'
op|'['
string|"'vif_uuid'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'bmdb'
op|'.'
name|'bm_interface_set_vif_uuid'
op|'('
name|'ctx'
op|','
name|'pif'
op|'['
string|"'id'"
op|']'
op|','
name|'vif_uuid'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"pif:%(id)s is plugged (vif_uuid=%(vif_uuid)s)"'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'pif'
op|'['
string|"'id'"
op|']'
op|','
string|"'vif_uuid'"
op|':'
name|'vif_uuid'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_after_plug'
op|'('
name|'instance'
op|','
name|'vif'
op|','
name|'pif'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# NOTE(deva): should this really be raising an exception'
nl|'\n'
comment|'#             when there are no physical interfaces left?'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|'"Baremetal node: %(id)s has no available physical interface"'
nl|'\n'
string|'" for virtual interface %(vif_uuid)s"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'id'"
op|':'
name|'node'
op|'['
string|"'id'"
op|']'
op|','
string|"'vif_uuid'"
op|':'
name|'vif_uuid'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"unplug: instance_uuid=%(uuid)s vif=%(vif)s"'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'vif'"
op|':'
name|'vif'
op|'}'
op|')'
newline|'\n'
name|'vif_uuid'
op|'='
name|'vif'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pif'
op|'='
name|'bmdb'
op|'.'
name|'bm_interface_get_by_vif_uuid'
op|'('
name|'ctx'
op|','
name|'vif_uuid'
op|')'
newline|'\n'
name|'bmdb'
op|'.'
name|'bm_interface_set_vif_uuid'
op|'('
name|'ctx'
op|','
name|'pif'
op|'['
string|"'id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"pif:%(id)s is unplugged (vif_uuid=%(vif_uuid)s)"'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'pif'
op|'['
string|"'id'"
op|']'
op|','
string|"'vif_uuid'"
op|':'
name|'vif_uuid'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_after_unplug'
op|'('
name|'instance'
op|','
name|'vif'
op|','
name|'pif'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NovaException'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"no pif for vif_uuid=%s"'
op|')'
op|'%'
name|'vif_uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
