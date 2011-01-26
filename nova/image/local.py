begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'import'
name|'cPickle'
name|'as'
name|'pickle'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalImageService
name|'class'
name|'LocalImageService'
op|'('
name|'service'
op|'.'
name|'BaseImageService'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Image service storing images to local disk.\n    It assumes that image_ids are integers.\n\n    """'
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
name|'_path'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_path_to
dedent|''
name|'def'
name|'_path_to'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_path'
op|','
name|'str'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ids
dedent|''
name|'def'
name|'_ids'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The list of all image ids."""'
newline|'\n'
name|'return'
op|'['
name|'int'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'_path'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'i'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'i'
op|'['
string|"'name'"
op|']'
op|')'
name|'for'
name|'i'
name|'in'
name|'self'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'id'
op|')'
name|'for'
name|'id'
name|'in'
name|'self'
op|'.'
name|'_ids'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'pickle'
op|'.'
name|'load'
op|'('
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'id'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store the image data and return the new image id."""'
newline|'\n'
name|'id'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
number|'0'
op|','
number|'2'
op|'**'
number|'31'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pickle'
op|'.'
name|'dump'
op|'('
name|'data'
op|','
name|'open'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|')'
op|','
string|"'w'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the given image.\n        Raises OSError if the image does not exist.\n\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|delete_all
dedent|''
dedent|''
name|'def'
name|'delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Clears out all images in local directory."""'
newline|'\n'
name|'for'
name|'id'
name|'in'
name|'self'
op|'.'
name|'_ids'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'self'
op|'.'
name|'_path_to'
op|'('
name|'id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_imagedir
dedent|''
dedent|''
name|'def'
name|'delete_imagedir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the local directory.\n        Raises OSError if directory is not empty.\n\n        """'
newline|'\n'
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'self'
op|'.'
name|'_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
