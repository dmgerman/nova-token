begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
string|'"""Implementation of a fake image service."""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
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
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'null_kernel'"
op|','
string|"'nova.compute.api'"
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
DECL|class|_FakeImageService
name|'class'
name|'_FakeImageService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mock (fake) image service for unit testing."""'
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
name|'images'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|"# NOTE(justinsb): The OpenStack API can't upload an image?"
nl|'\n'
comment|"# So, make sure we've got one.."
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
name|'image1'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'25165824'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image2'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'a2459075-d96c-40d5-893e-577ff92e721c'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'58145823'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image3'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'83594576'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image4'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'84035174'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image5'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage123456'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'ami'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'26360814'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
nl|'\n'
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image6'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'a440c04b-79fa-479c-bed1-0b816eaec379'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage6'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ova'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vhd'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'49163826'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
string|"'False'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image7'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'70a599e0-31e7-49b7-b260-868f441e862b'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage7'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ova'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vhd'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'74185822'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x86_64'"
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
string|"'True'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image3'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image7'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagedata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'_FakeImageService'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): implement optional kwargs such as limit, sort_dir'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return list of detailed image information."""'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'images'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|download
dedent|''
name|'def'
name|'download'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'dst_path'
op|'='
name|'None'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'_imagedata'
op|'.'
name|'get'
op|'('
name|'image_id'
op|','
string|"''"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'dst_path'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'dst_path'
op|','
string|"'wb'"
op|')'
name|'as'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'data'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'_imagedata'
op|'.'
name|'get'
op|'('
name|'image_id'
op|','
string|"''"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
dedent|''
dedent|''
name|'def'
name|'show'
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
string|'"""Get data about specified image.\n\n        Returns a dict containing image data for the given opaque image id.\n\n        """'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'images'
op|'.'
name|'get'
op|'('
name|'str'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'image'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warn'
op|'('
string|"'Unable to find image id %s.  Have images: %s'"
op|','
nl|'\n'
name|'image_id'
op|','
name|'self'
op|'.'
name|'images'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store the image data and return the new image id.\n\n        :raises: Duplicate if the image already exist.\n\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'str'
op|'('
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'id'"
op|','
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'if'
name|'image_id'
name|'in'
name|'self'
op|'.'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'CouldNotUploadImage'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_imagedata'
op|'['
name|'image_id'
op|']'
op|'='
name|'data'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
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
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replace the contents of the given image with the new data.\n\n        :raises: ImageNotFound if the image does not exist.\n\n        """'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'images'
op|'.'
name|'get'
op|'('
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'purge_props'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'image'
op|'['
string|"'properties'"
op|']'
op|'.'
name|'update'
op|'('
name|'metadata'
op|'.'
name|'pop'
op|'('
string|"'properties'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'image'
op|'.'
name|'update'
op|'('
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'images'
op|'['
name|'image_id'
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete
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
string|'"""Delete the given image.\n\n        :raises: ImageNotFound if the image does not exist.\n\n        """'
newline|'\n'
name|'removed'
op|'='
name|'self'
op|'.'
name|'images'
op|'.'
name|'pop'
op|'('
name|'image_id'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'removed'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_location
dedent|''
dedent|''
name|'def'
name|'get_location'
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
name|'if'
name|'image_id'
name|'in'
name|'self'
op|'.'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'fake_location'"
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|_fakeImageService
dedent|''
dedent|''
name|'_fakeImageService'
op|'='
name|'_FakeImageService'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|FakeImageService
name|'def'
name|'FakeImageService'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_fakeImageService'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|FakeImageService_reset
dedent|''
name|'def'
name|'FakeImageService_reset'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_fakeImageService'
newline|'\n'
name|'_fakeImageService'
op|'='
name|'_FakeImageService'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_valid_image_id
dedent|''
name|'def'
name|'get_valid_image_id'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_fakeImageService'
op|'.'
name|'images'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_image_service
dedent|''
name|'def'
name|'stub_out_image_service'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'image_service'
op|'='
name|'FakeImageService'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|','
string|"'get_remote_image_service'"
op|','
nl|'\n'
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
op|'('
name|'image_service'
op|','
name|'y'
op|')'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|','
string|"'get_default_image_service'"
op|','
nl|'\n'
name|'lambda'
op|':'
name|'image_service'
op|')'
newline|'\n'
name|'return'
name|'image_service'
newline|'\n'
dedent|''
endmarker|''
end_unit
