begin_unit
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
name|'import'
name|'os'
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
name|'import'
name|'image'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'imageutils'
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
name|'utils'
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
DECL|variable|image_opts
name|'image_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'force_raw_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force backing images to raw format'"
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
name|'image_opts'
op|')'
newline|'\n'
DECL|variable|IMAGE_API
name|'IMAGE_API'
op|'='
name|'image'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|qemu_img_info
name|'def'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return an object containing the parsed output from qemu-img info."""'
newline|'\n'
comment|'# TODO(mikal): this code should not be referring to a libvirt specific'
nl|'\n'
comment|'# flag.'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
name|'and'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'images_type'
op|'!='
string|"'rbd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'imageutils'
op|'.'
name|'QemuImgInfo'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'env'"
op|','
string|"'LC_ALL=C'"
op|','
string|"'LANG=C'"
op|','
nl|'\n'
string|"'qemu-img'"
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
name|'return'
name|'imageutils'
op|'.'
name|'QemuImgInfo'
op|'('
name|'out'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_image
dedent|''
name|'def'
name|'convert_image'
op|'('
name|'source'
op|','
name|'dest'
op|','
name|'out_format'
op|','
name|'run_as_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert image to other format."""'
newline|'\n'
name|'cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
string|"'convert'"
op|','
string|"'-O'"
op|','
name|'out_format'
op|','
name|'source'
op|','
name|'dest'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'run_as_root'
op|'='
name|'run_as_root'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
dedent|''
name|'def'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'_user_id'
op|','
name|'_project_id'
op|','
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'IMAGE_API'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'dest_path'
op|'='
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_to_raw
dedent|''
dedent|''
name|'def'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'path_tmp'
op|'='
string|'"%s.part"'
op|'%'
name|'path'
newline|'\n'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_href'
op|','
name|'path_tmp'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'max_size'
op|'='
name|'max_size'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'path_tmp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'qemu_img_info'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'fmt'
op|'='
name|'data'
op|'.'
name|'file_format'
newline|'\n'
name|'if'
name|'fmt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"\'qemu-img info\' parsing failed."'
op|')'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_href'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'backing_file'
op|'='
name|'data'
op|'.'
name|'backing_file'
newline|'\n'
name|'if'
name|'backing_file'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
op|'('
name|'_'
op|'('
string|'"fmt=%(fmt)s backed by: %(backing_file)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'fmt'"
op|':'
name|'fmt'
op|','
string|"'backing_file'"
op|':'
name|'backing_file'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# We can't generally shrink incoming images, so disallow"
nl|'\n'
comment|"# images > size of the flavor we're booting.  Checking here avoids"
nl|'\n'
comment|'# an immediate DoS where we convert large qcow images to raw'
nl|'\n'
comment|'# (which may compress well but not be sparse).'
nl|'\n'
comment|'# TODO(p-draigbrady): loop through all flavor sizes, so that'
nl|'\n'
comment|'# we might continue here and not discard the download.'
nl|'\n'
comment|"# If we did that we'd have to do the higher level size checks"
nl|'\n'
comment|'# irrespective of whether the base image was prepared or not.'
nl|'\n'
dedent|''
name|'disk_size'
op|'='
name|'data'
op|'.'
name|'virtual_size'
newline|'\n'
name|'if'
name|'max_size'
name|'and'
name|'max_size'
op|'<'
name|'disk_size'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%(base)s virtual size %(disk_size)s '"
nl|'\n'
string|"'larger than flavor root disk size %(size)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|'%'
op|'{'
string|"'base'"
op|':'
name|'path'
op|','
nl|'\n'
string|"'disk_size'"
op|':'
name|'disk_size'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'max_size'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'FlavorDiskTooSmall'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fmt'
op|'!='
string|'"raw"'
name|'and'
name|'CONF'
op|'.'
name|'force_raw_images'
op|':'
newline|'\n'
indent|'            '
name|'staged'
op|'='
string|'"%s.converted"'
op|'%'
name|'path'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%s was %s, converting to raw"'
op|'%'
op|'('
name|'image_href'
op|','
name|'fmt'
op|')'
op|')'
newline|'\n'
name|'with'
name|'fileutils'
op|'.'
name|'remove_path_on_error'
op|'('
name|'staged'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'convert_image'
op|'('
name|'path_tmp'
op|','
name|'staged'
op|','
string|"'raw'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path_tmp'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'qemu_img_info'
op|'('
name|'staged'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'.'
name|'file_format'
op|'!='
string|'"raw"'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'image_href'
op|','
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Converted to raw, but format is now %s"'
op|')'
op|'%'
nl|'\n'
name|'data'
op|'.'
name|'file_format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'rename'
op|'('
name|'staged'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'rename'
op|'('
name|'path_tmp'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
