begin_unit
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""The volumes api."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'volume_types'
newline|'\n'
nl|'\n'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_attachment_detail_view
name|'def'
name|'_translate_attachment_detail_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for attachment details view."""'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'_translate_attachment_summary_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
comment|'# No additional data / lookups at the moment'
nl|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_attachment_summary_view
dedent|''
name|'def'
name|'_translate_attachment_summary_view'
op|'('
name|'_context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for attachment summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'volume_id'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(justinsb): We use the volume id as the id of the attachment object'
nl|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'d'
op|'['
string|"'server_id'"
op|']'
op|'='
name|'vol'
op|'['
string|"'instance_uuid'"
op|']'
newline|'\n'
name|'if'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'mountpoint'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'device'"
op|']'
op|'='
name|'vol'
op|'['
string|"'mountpoint'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_volume_detail_view
dedent|''
name|'def'
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for volumes details view."""'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'_translate_volume_summary_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
comment|'# No additional data / lookups at the moment'
nl|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_volume_summary_view
dedent|''
name|'def'
name|'_translate_volume_summary_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Maps keys for volumes summary view."""'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'id'"
op|']'
op|'='
name|'vol'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'status'"
op|']'
op|'='
name|'vol'
op|'['
string|"'status'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'size'"
op|']'
op|'='
name|'vol'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'vol'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
nl|'\n'
name|'d'
op|'['
string|"'attachments'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|"'attached'"
op|':'
newline|'\n'
indent|'        '
name|'attachment'
op|'='
name|'_translate_attachment_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
newline|'\n'
name|'d'
op|'['
string|"'attachments'"
op|']'
op|'.'
name|'append'
op|'('
name|'attachment'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'vol'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'d'
op|'['
string|"'display_description'"
op|']'
op|'='
name|'vol'
op|'['
string|"'display_description'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'vol'
op|'['
string|"'volume_type_id'"
op|']'
name|'and'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'volume_type'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'volume_type'"
op|']'
op|'='
name|'vol'
op|'['
string|"'volume_type'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# TODO(bcwaldon): remove str cast once we use uuids'
nl|'\n'
indent|'        '
name|'d'
op|'['
string|"'volume_type'"
op|']'
op|'='
name|'str'
op|'('
name|'vol'
op|'['
string|"'volume_type_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'d'
op|'['
string|"'snapshot_id'"
op|']'
op|'='
name|'vol'
op|'['
string|"'snapshot_id'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"vol=%s"'
op|')'
op|','
name|'vol'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vol'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
name|'vol'
op|'.'
name|'get'
op|'('
string|"'volume_metadata'"
op|')'
newline|'\n'
name|'d'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'dict'
op|'('
op|'('
name|'item'
op|'['
string|"'key'"
op|']'
op|','
name|'item'
op|'['
string|"'value'"
op|']'
op|')'
name|'for'
name|'item'
name|'in'
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
string|"'metadata'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_attachment
dedent|''
name|'def'
name|'make_attachment'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'server_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'volume_id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'device'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_volume
dedent|''
name|'def'
name|'make_volume'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'size'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'availability_zone'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'created_at'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'display_name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'display_description'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'volume_type'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'snapshot_id'"
op|')'
newline|'\n'
nl|'\n'
name|'attachments'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'attachments'"
op|')'
newline|'\n'
name|'attachment'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'attachments'
op|','
string|"'attachment'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'attachments'"
op|')'
newline|'\n'
name|'make_attachment'
op|'('
name|'attachment'
op|')'
newline|'\n'
nl|'\n'
comment|'# Attach metadata node'
nl|'\n'
name|'elem'
op|'.'
name|'append'
op|'('
name|'common'
op|'.'
name|'MetadataTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeTemplate
dedent|''
name|'class'
name|'VolumeTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'volume'"
op|','
name|'selector'
op|'='
string|"'volume'"
op|')'
newline|'\n'
name|'make_volume'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumesTemplate
dedent|''
dedent|''
name|'class'
name|'VolumesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'volumes'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'volume'"
op|','
name|'selector'
op|'='
string|"'volumes'"
op|')'
newline|'\n'
name|'make_volume'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommonDeserializer
dedent|''
dedent|''
name|'class'
name|'CommonDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Common deserializer to handle xml-formatted volume requests.\n\n       Handles standard volume attributes as well as the optional metadata\n       attribute\n    """'
newline|'\n'
nl|'\n'
DECL|variable|metadata_deserializer
name|'metadata_deserializer'
op|'='
name|'common'
op|'.'
name|'MetadataXMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_extract_volume
name|'def'
name|'_extract_volume'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Marshal the volume attribute of a parsed request."""'
newline|'\n'
name|'volume'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'volume_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'node'
op|','
string|"'volume'"
op|')'
newline|'\n'
nl|'\n'
name|'attributes'
op|'='
op|'['
string|"'display_name'"
op|','
string|"'display_description'"
op|','
string|"'size'"
op|','
nl|'\n'
string|"'volume_type'"
op|','
string|"'availability_zone'"
op|']'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'attributes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'volume'
op|'['
name|'attr'
op|']'
op|'='
name|'volume_node'
op|'.'
name|'getAttribute'
op|'('
name|'attr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'volume_node'
op|','
string|"'metadata'"
op|')'
newline|'\n'
name|'if'
name|'metadata_node'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'volume'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateDeserializer
dedent|''
dedent|''
name|'class'
name|'CreateDeserializer'
op|'('
name|'CommonDeserializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Deserializer to handle xml-formatted create volume requests.\n\n       Handles standard volume attributes as well as the optional metadata\n       attribute\n    """'
newline|'\n'
nl|'\n'
DECL|member|default
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deserialize an xml-formatted volume create request."""'
newline|'\n'
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'string'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_extract_volume'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'volume'"
op|':'
name|'volume'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeController
dedent|''
dedent|''
name|'class'
name|'VolumeController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Volumes API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumeController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'VolumeTemplate'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'volume'"
op|':'
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'vol'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Delete volume with id: %s"'
op|')'
op|','
name|'id'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'VolumesTemplate'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a summary list of volumes."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_translate_volume_summary_view'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'VolumesTemplate'
op|')'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a detailed list of volumes."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_items'
op|'('
name|'req'
op|','
name|'entity_maker'
op|'='
name|'_translate_volume_detail_view'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_items
dedent|''
name|'def'
name|'_items'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'entity_maker'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of volumes, transformed through entity_maker."""'
newline|'\n'
nl|'\n'
name|'search_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'search_opts'
op|'.'
name|'update'
op|'('
name|'req'
op|'.'
name|'GET'
op|')'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'remove_invalid_options'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|','
name|'self'
op|'.'
name|'_get_volume_search_options'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
name|'search_opts'
op|'='
name|'search_opts'
op|')'
newline|'\n'
name|'limited_list'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'volumes'
op|','
name|'req'
op|')'
newline|'\n'
name|'res'
op|'='
op|'['
name|'entity_maker'
op|'('
name|'context'
op|','
name|'vol'
op|')'
name|'for'
name|'vol'
name|'in'
name|'limited_list'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'volumes'"
op|':'
name|'res'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'VolumeTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'deserializers'
op|'('
name|'xml'
op|'='
name|'CreateDeserializer'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new volume."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volume'
op|'='
name|'body'
op|'['
string|"'volume'"
op|']'
newline|'\n'
nl|'\n'
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'req_volume_type'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'volume_type'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'req_volume_type'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'kwargs'
op|'['
string|"'volume_type'"
op|']'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
nl|'\n'
name|'context'
op|','
name|'req_volume_type'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'kwargs'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'snapshot_id'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'snapshot_id'"
op|')'
newline|'\n'
name|'if'
name|'snapshot_id'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'snapshot'"
op|']'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_snapshot'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'snapshot'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'size'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'size'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'size'
name|'is'
name|'None'
name|'and'
name|'kwargs'
op|'['
string|"'snapshot'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'size'
op|'='
name|'kwargs'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'volume_size'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Create volume of %s GB"'
op|')'
op|','
name|'size'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'kwargs'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'new_volume'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
nl|'\n'
name|'size'
op|','
nl|'\n'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'display_name'"
op|')'
op|','
nl|'\n'
name|'volume'
op|'.'
name|'get'
op|'('
string|"'display_description'"
op|')'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): Instance should be None at db layer instead of'
nl|'\n'
comment|'#             trying to lazy load, but for now we turn it into'
nl|'\n'
comment|'#             a dict to avoid an error.'
nl|'\n'
name|'retval'
op|'='
name|'_translate_volume_detail_view'
op|'('
name|'context'
op|','
name|'dict'
op|'('
name|'new_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
op|'{'
string|"'volume'"
op|':'
name|'retval'
op|'}'
newline|'\n'
nl|'\n'
name|'location'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
name|'req'
op|'.'
name|'url'
op|','
name|'new_volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'result'
op|','
name|'headers'
op|'='
name|'dict'
op|'('
name|'location'
op|'='
name|'location'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_volume_search_options
dedent|''
name|'def'
name|'_get_volume_search_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return volume search options allowed by non-admin."""'
newline|'\n'
name|'return'
op|'('
string|"'name'"
op|','
string|"'status'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'VolumeController'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_invalid_options
dedent|''
name|'def'
name|'remove_invalid_options'
op|'('
name|'context'
op|','
name|'search_options'
op|','
name|'allowed_search_options'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove search options that are not valid for non-admin API/context."""'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
comment|'# Allow all options'
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
comment|'# Otherwise, strip out all unknown options'
nl|'\n'
dedent|''
name|'unknown_options'
op|'='
op|'['
name|'opt'
name|'for'
name|'opt'
name|'in'
name|'search_options'
nl|'\n'
name|'if'
name|'opt'
name|'not'
name|'in'
name|'allowed_search_options'
op|']'
newline|'\n'
name|'bad_options'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
name|'unknown_options'
op|')'
newline|'\n'
name|'log_msg'
op|'='
name|'_'
op|'('
string|'"Removing options \'%(bad_options)s\' from query"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'log_msg'
op|')'
newline|'\n'
name|'for'
name|'opt'
name|'in'
name|'unknown_options'
op|':'
newline|'\n'
indent|'        '
name|'search_options'
op|'.'
name|'pop'
op|'('
name|'opt'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
