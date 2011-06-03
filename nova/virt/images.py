begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nHandling of VM disk images.\n"""'
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
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.images'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
name|'def'
name|'fetch'
op|'('
name|'image_href'
op|','
name|'path'
op|','
name|'_user'
op|','
name|'_project'
op|')'
op|':'
newline|'\n'
comment|'# TODO(vish): Improve context handling and add owner and auth data'
nl|'\n'
comment|'#             when it is added to glance.  Right now there is no'
nl|'\n'
comment|'#             auth checking in glance, so we assume that access was'
nl|'\n'
comment|'#             checked before we got here.'
nl|'\n'
indent|'    '
op|'('
name|'image_service'
op|','
name|'image_id'
op|')'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_image_service'
op|'('
name|'image_href'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|'"wb"'
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'        '
name|'elevated'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'image_service'
op|'.'
name|'get'
op|'('
name|'elevated'
op|','
name|'image_id'
op|','
name|'image_file'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(vish): xenapi should use the glance client code directly instead'
nl|'\n'
comment|'#             of retrieving the image using this method.'
nl|'\n'
DECL|function|image_url
dedent|''
name|'def'
name|'image_url'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'image_service'
op|'=='
string|'"nova.image.glance.GlanceImageService"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"http://%s:%s/images/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'glance_host'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'glance_port'
op|','
name|'image'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"http://%s:%s/_images/%s/image"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'s3_host'
op|','
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'image'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
