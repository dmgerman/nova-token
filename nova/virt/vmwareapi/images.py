begin_unit
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nUtility functions for Image transfer and manipulation.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tarfile'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'oslo_vmware'
name|'import'
name|'rw_handles'
newline|'\n'
name|'import'
name|'six'
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
op|','
name|'_LE'
op|','
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'image'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'io_util'
newline|'\n'
nl|'\n'
comment|"# NOTE(mdbooth): We use use_linked_clone below, but don't have to import it"
nl|'\n'
comment|'# because nova.virt.vmwareapi.driver is imported first. In fact, it is not'
nl|'\n'
comment|'# possible to import it here, as nova.virt.vmwareapi.driver calls'
nl|'\n'
comment|'# CONF.register_opts() after the import chain which imports this module. This'
nl|'\n'
comment|"# is not a problem as long as the import order doesn't change."
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
DECL|variable|QUEUE_BUFFER_SIZE
name|'QUEUE_BUFFER_SIZE'
op|'='
number|'10'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareImage
name|'class'
name|'VMwareImage'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image_id'
op|','
nl|'\n'
name|'file_size'
op|'='
number|'0'
op|','
nl|'\n'
name|'os_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_OS_TYPE'
op|','
nl|'\n'
name|'adapter_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_ADAPTER_TYPE'
op|','
nl|'\n'
name|'disk_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_DISK_TYPE'
op|','
nl|'\n'
name|'container_format'
op|'='
name|'constants'
op|'.'
name|'CONTAINER_FORMAT_BARE'
op|','
nl|'\n'
name|'file_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_DISK_FORMAT'
op|','
nl|'\n'
name|'linked_clone'
op|'='
name|'None'
op|','
nl|'\n'
name|'vif_model'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_VIF_MODEL'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""VMwareImage holds values for use in building VMs.\n\n            image_id (str): uuid of the image\n            file_size (int): size of file in bytes\n            os_type (str): name of guest os (use vSphere names only)\n            adapter_type (str): name of the adapter\'s type\n            disk_type (str): type of disk in thin, thick, etc\n            container_format (str): container format (bare or ova)\n            file_type (str): vmdk or iso\n            linked_clone (bool): use linked clone, or don\'t\n            vif_model (str): virtual machine network interface\n        """'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'file_size'
op|'='
name|'file_size'
newline|'\n'
name|'self'
op|'.'
name|'os_type'
op|'='
name|'os_type'
newline|'\n'
name|'self'
op|'.'
name|'adapter_type'
op|'='
name|'adapter_type'
newline|'\n'
name|'self'
op|'.'
name|'container_format'
op|'='
name|'container_format'
newline|'\n'
name|'self'
op|'.'
name|'disk_type'
op|'='
name|'disk_type'
newline|'\n'
name|'self'
op|'.'
name|'file_type'
op|'='
name|'file_type'
newline|'\n'
nl|'\n'
comment|'# NOTE(vui): This should be removed when we restore the'
nl|'\n'
comment|'# descriptor-based validation.'
nl|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'file_type'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'file_type'
name|'not'
name|'in'
name|'constants'
op|'.'
name|'DISK_FORMATS_ALL'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidDiskFormat'
op|'('
name|'disk_format'
op|'='
name|'self'
op|'.'
name|'file_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'linked_clone'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'linked_clone'
op|'='
name|'linked_clone'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'linked_clone'
op|'='
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'use_linked_clone'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'vif_model'
op|'='
name|'vif_model'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|file_size_in_kb
name|'def'
name|'file_size_in_kb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'file_size'
op|'/'
name|'units'
op|'.'
name|'Ki'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_sparse
name|'def'
name|'is_sparse'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'disk_type'
op|'=='
name|'constants'
op|'.'
name|'DISK_TYPE_SPARSE'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_iso
name|'def'
name|'is_iso'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'file_type'
op|'=='
name|'constants'
op|'.'
name|'DISK_FORMAT_ISO'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_ova
name|'def'
name|'is_ova'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'container_format'
op|'=='
name|'constants'
op|'.'
name|'CONTAINER_FORMAT_OVA'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_image
name|'def'
name|'from_image'
op|'('
name|'cls'
op|','
name|'image_id'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns VMwareImage, the subset of properties the driver uses.\n\n        :param image_id - image id of image\n        :param image_meta - image metadata object we are working with\n        :return: vmware image object\n        :rtype: nova.virt.vmwareapi.images.VmwareImage\n        """'
newline|'\n'
name|'properties'
op|'='
name|'image_meta'
op|'.'
name|'properties'
newline|'\n'
nl|'\n'
comment|'# calculate linked_clone flag, allow image properties to override the'
nl|'\n'
comment|'# global property set in the configurations.'
nl|'\n'
name|'image_linked_clone'
op|'='
name|'properties'
op|'.'
name|'get'
op|'('
string|"'img_linked_clone'"
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'use_linked_clone'
op|')'
newline|'\n'
nl|'\n'
comment|'# catch any string values that need to be interpreted as boolean values'
nl|'\n'
name|'linked_clone'
op|'='
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'image_linked_clone'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'image_meta'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'container_format'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'container_format'
op|'='
name|'image_meta'
op|'.'
name|'container_format'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'container_format'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'props'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'linked_clone'"
op|':'
name|'linked_clone'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'container_format'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'image_meta'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'size'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'['
string|"'file_size'"
op|']'
op|'='
name|'image_meta'
op|'.'
name|'size'
newline|'\n'
dedent|''
name|'if'
name|'image_meta'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'disk_format'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'['
string|"'file_type'"
op|']'
op|'='
name|'image_meta'
op|'.'
name|'disk_format'
newline|'\n'
dedent|''
name|'hw_disk_bus'
op|'='
name|'properties'
op|'.'
name|'get'
op|'('
string|"'hw_disk_bus'"
op|')'
newline|'\n'
name|'if'
name|'hw_disk_bus'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'='
op|'{'
nl|'\n'
name|'fields'
op|'.'
name|'SCSIModel'
op|'.'
name|'LSILOGIC'
op|':'
nl|'\n'
name|'constants'
op|'.'
name|'DEFAULT_ADAPTER_TYPE'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'SCSIModel'
op|'.'
name|'LSISAS1068'
op|':'
nl|'\n'
name|'constants'
op|'.'
name|'ADAPTER_TYPE_LSILOGICSAS'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'SCSIModel'
op|'.'
name|'BUSLOGIC'
op|':'
nl|'\n'
name|'constants'
op|'.'
name|'ADAPTER_TYPE_BUSLOGIC'
op|','
nl|'\n'
name|'fields'
op|'.'
name|'SCSIModel'
op|'.'
name|'VMPVSCSI'
op|':'
nl|'\n'
name|'constants'
op|'.'
name|'ADAPTER_TYPE_PARAVIRTUAL'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'hw_disk_bus'
op|'=='
name|'fields'
op|'.'
name|'DiskBus'
op|'.'
name|'IDE'
op|':'
newline|'\n'
indent|'                '
name|'props'
op|'['
string|"'adapter_type'"
op|']'
op|'='
name|'constants'
op|'.'
name|'ADAPTER_TYPE_IDE'
newline|'\n'
dedent|''
name|'elif'
name|'hw_disk_bus'
op|'=='
name|'fields'
op|'.'
name|'DiskBus'
op|'.'
name|'SCSI'
op|':'
newline|'\n'
indent|'                '
name|'hw_scsi_model'
op|'='
name|'properties'
op|'.'
name|'get'
op|'('
string|"'hw_scsi_model'"
op|')'
newline|'\n'
name|'props'
op|'['
string|"'adapter_type'"
op|']'
op|'='
name|'mapping'
op|'.'
name|'get'
op|'('
name|'hw_scsi_model'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'props_map'
op|'='
op|'{'
nl|'\n'
string|"'os_distro'"
op|':'
string|"'os_type'"
op|','
nl|'\n'
string|"'hw_disk_type'"
op|':'
string|"'disk_type'"
op|','
nl|'\n'
string|"'hw_vif_model'"
op|':'
string|"'vif_model'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'props_map'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'properties'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'k'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'props'
op|'['
name|'v'
op|']'
op|'='
name|'properties'
op|'.'
name|'get'
op|'('
name|'k'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'cls'
op|'('
op|'**'
name|'props'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|start_transfer
dedent|''
dedent|''
name|'def'
name|'start_transfer'
op|'('
name|'context'
op|','
name|'read_file_handle'
op|','
name|'data_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'None'
op|','
name|'image_id'
op|'='
name|'None'
op|','
name|'image_meta'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Start the data transfer from the reader to the writer.\n    Reader writes to the pipe and the writer reads from the pipe. This means\n    that the total transfer time boils down to the slower of the read/write\n    and not the addition of the two times.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image_meta'
op|':'
newline|'\n'
indent|'        '
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# The pipe that acts as an intermediate store of data for reader to write'
nl|'\n'
comment|'# to and writer to grab from.'
nl|'\n'
dedent|''
name|'thread_safe_pipe'
op|'='
name|'io_util'
op|'.'
name|'ThreadSafePipe'
op|'('
name|'QUEUE_BUFFER_SIZE'
op|','
name|'data_size'
op|')'
newline|'\n'
comment|'# The read thread. In case of glance it is the instance of the'
nl|'\n'
comment|'# GlanceFileRead class. The glance client read returns an iterator'
nl|'\n'
comment|'# and this class wraps that iterator to provide datachunks in calls'
nl|'\n'
comment|'# to read.'
nl|'\n'
name|'read_thread'
op|'='
name|'io_util'
op|'.'
name|'IOThread'
op|'('
name|'read_file_handle'
op|','
name|'thread_safe_pipe'
op|')'
newline|'\n'
nl|'\n'
comment|'# In case of Glance - VMware transfer, we just need a handle to the'
nl|'\n'
comment|'# HTTP Connection that is to send transfer data to the VMware datastore.'
nl|'\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\n'
indent|'        '
name|'write_thread'
op|'='
name|'io_util'
op|'.'
name|'IOThread'
op|'('
name|'thread_safe_pipe'
op|','
name|'write_file_handle'
op|')'
newline|'\n'
comment|'# In case of VMware - Glance transfer, we relinquish VMware HTTP file read'
nl|'\n'
comment|'# handle to Glance Client instance, but to be sure of the transfer we need'
nl|'\n'
comment|'# to be sure of the status of the image on glance changing to active.'
nl|'\n'
comment|'# The GlanceWriteThread handles the same for us.'
nl|'\n'
dedent|''
name|'elif'
name|'image_id'
op|':'
newline|'\n'
indent|'        '
name|'write_thread'
op|'='
name|'io_util'
op|'.'
name|'GlanceWriteThread'
op|'('
name|'context'
op|','
name|'thread_safe_pipe'
op|','
nl|'\n'
name|'image_id'
op|','
name|'image_meta'
op|')'
newline|'\n'
comment|'# Start the read and write threads.'
nl|'\n'
dedent|''
name|'read_event'
op|'='
name|'read_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'write_event'
op|'='
name|'write_thread'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Wait on the read and write events to signal their end'
nl|'\n'
indent|'        '
name|'read_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'write_event'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# In case of any of the reads or writes raising an exception,'
nl|'\n'
comment|"# stop the threads so that we un-necessarily don't keep the other one"
nl|'\n'
comment|'# waiting.'
nl|'\n'
indent|'        '
name|'read_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'write_thread'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Log and raise the exception.'
nl|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Transfer data failed'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# No matter what, try closing the read and write handles, if it so'
nl|'\n'
comment|'# applies.'
nl|'\n'
indent|'        '
name|'read_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'write_file_handle'
op|':'
newline|'\n'
indent|'            '
name|'write_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upload_iso_to_datastore
dedent|''
dedent|''
dedent|''
name|'def'
name|'upload_iso_to_datastore'
op|'('
name|'iso_path'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Uploading iso %s to datastore"'
op|','
name|'iso_path'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'iso_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'iso_file'
op|':'
newline|'\n'
indent|'        '
name|'write_file_handle'
op|'='
name|'rw_handles'
op|'.'
name|'FileWriteHandle'
op|'('
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"host"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"port"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"data_center_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"datastore_name"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cookies"'
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"file_path"'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'fstat'
op|'('
name|'iso_file'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
op|'.'
name|'st_size'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Uploading iso of size : %s "'
op|','
nl|'\n'
name|'os'
op|'.'
name|'fstat'
op|'('
name|'iso_file'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
op|'.'
name|'st_size'
op|')'
newline|'\n'
name|'block_size'
op|'='
number|'0x10000'
newline|'\n'
name|'data'
op|'='
name|'iso_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'data'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'write_file_handle'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'data'
op|'='
name|'iso_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
dedent|''
name|'write_file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Uploaded iso %s to datastore"'
op|','
name|'iso_path'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image
dedent|''
name|'def'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'host'
op|','
name|'port'
op|','
name|'dc_name'
op|','
name|'ds_name'
op|','
name|'file_path'
op|','
nl|'\n'
name|'cookies'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Download image from the glance image server."""'
newline|'\n'
name|'image_ref'
op|'='
name|'instance'
op|'.'
name|'image_ref'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Downloading image file data %(image_ref)s to the "'
nl|'\n'
string|'"data store %(data_store_name)s"'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'image_ref'
op|','
nl|'\n'
string|"'data_store_name'"
op|':'
name|'ds_name'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'read_iter'
op|'='
name|'IMAGE_API'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'read_file_handle'
op|'='
name|'rw_handles'
op|'.'
name|'ImageReadHandle'
op|'('
name|'read_iter'
op|')'
newline|'\n'
name|'write_file_handle'
op|'='
name|'rw_handles'
op|'.'
name|'FileWriteHandle'
op|'('
nl|'\n'
name|'host'
op|','
name|'port'
op|','
name|'dc_name'
op|','
name|'ds_name'
op|','
name|'cookies'
op|','
name|'file_path'
op|','
name|'file_size'
op|')'
newline|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
name|'read_file_handle'
op|','
name|'file_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'write_file_handle'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Downloaded image file data %(image_ref)s to "'
nl|'\n'
string|'"%(upload_name)s on the data store "'
nl|'\n'
string|'"%(data_store_name)s"'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'image_ref'
op|','
nl|'\n'
string|"'upload_name'"
op|':'
string|"'n/a'"
name|'if'
name|'file_path'
name|'is'
name|'None'
name|'else'
name|'file_path'
op|','
nl|'\n'
string|"'data_store_name'"
op|':'
string|"'n/a'"
name|'if'
name|'ds_name'
name|'is'
name|'None'
name|'else'
name|'ds_name'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_shadow_vm_config_spec
dedent|''
name|'def'
name|'_build_shadow_vm_config_spec'
op|'('
name|'session'
op|','
name|'name'
op|','
name|'size_kb'
op|','
name|'disk_type'
op|','
name|'ds_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return spec for creating a shadow VM for image disk.\n\n    The VM is never meant to be powered on. When used in importing\n    a disk it governs the directory name created for the VM\n    and the disk type of the disk image to convert to.\n\n    :param name: Name of the backing\n    :param size_kb: Size in KB of the backing\n    :param disk_type: VMDK type for the disk\n    :param ds_name: Datastore name where the disk is to be provisioned\n    :return: Spec for creation\n    """'
newline|'\n'
name|'cf'
op|'='
name|'session'
op|'.'
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'controller_device'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualLsiLogicController'"
op|')'
newline|'\n'
name|'controller_device'
op|'.'
name|'key'
op|'='
op|'-'
number|'100'
newline|'\n'
name|'controller_device'
op|'.'
name|'busNumber'
op|'='
number|'0'
newline|'\n'
name|'controller_device'
op|'.'
name|'sharedBus'
op|'='
string|"'noSharing'"
newline|'\n'
name|'controller_spec'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'controller_spec'
op|'.'
name|'operation'
op|'='
string|"'add'"
newline|'\n'
name|'controller_spec'
op|'.'
name|'device'
op|'='
name|'controller_device'
newline|'\n'
nl|'\n'
name|'disk_device'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDisk'"
op|')'
newline|'\n'
comment|'# for very small disks allocate at least 1KB'
nl|'\n'
name|'disk_device'
op|'.'
name|'capacityInKB'
op|'='
name|'max'
op|'('
number|'1'
op|','
name|'int'
op|'('
name|'size_kb'
op|')'
op|')'
newline|'\n'
name|'disk_device'
op|'.'
name|'key'
op|'='
op|'-'
number|'101'
newline|'\n'
name|'disk_device'
op|'.'
name|'unitNumber'
op|'='
number|'0'
newline|'\n'
name|'disk_device'
op|'.'
name|'controllerKey'
op|'='
op|'-'
number|'100'
newline|'\n'
name|'disk_device_bkng'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDiskFlatVer2BackingInfo'"
op|')'
newline|'\n'
name|'if'
name|'disk_type'
op|'=='
name|'constants'
op|'.'
name|'DISK_TYPE_EAGER_ZEROED_THICK'
op|':'
newline|'\n'
indent|'        '
name|'disk_device_bkng'
op|'.'
name|'eagerlyScrub'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'disk_type'
op|'=='
name|'constants'
op|'.'
name|'DISK_TYPE_THIN'
op|':'
newline|'\n'
indent|'        '
name|'disk_device_bkng'
op|'.'
name|'thinProvisioned'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'disk_device_bkng'
op|'.'
name|'fileName'
op|'='
string|"'[%s]'"
op|'%'
name|'ds_name'
newline|'\n'
name|'disk_device_bkng'
op|'.'
name|'diskMode'
op|'='
string|"'persistent'"
newline|'\n'
name|'disk_device'
op|'.'
name|'backing'
op|'='
name|'disk_device_bkng'
newline|'\n'
name|'disk_spec'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'disk_spec'
op|'.'
name|'operation'
op|'='
string|"'add'"
newline|'\n'
name|'disk_spec'
op|'.'
name|'fileOperation'
op|'='
string|"'create'"
newline|'\n'
name|'disk_spec'
op|'.'
name|'device'
op|'='
name|'disk_device'
newline|'\n'
nl|'\n'
name|'vm_file_info'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineFileInfo'"
op|')'
newline|'\n'
name|'vm_file_info'
op|'.'
name|'vmPathName'
op|'='
string|"'[%s]'"
op|'%'
name|'ds_name'
newline|'\n'
nl|'\n'
name|'create_spec'
op|'='
name|'cf'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
name|'create_spec'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'create_spec'
op|'.'
name|'guestId'
op|'='
string|"'otherGuest'"
newline|'\n'
name|'create_spec'
op|'.'
name|'numCPUs'
op|'='
number|'1'
newline|'\n'
name|'create_spec'
op|'.'
name|'memoryMB'
op|'='
number|'128'
newline|'\n'
name|'create_spec'
op|'.'
name|'deviceChange'
op|'='
op|'['
name|'controller_spec'
op|','
name|'disk_spec'
op|']'
newline|'\n'
name|'create_spec'
op|'.'
name|'files'
op|'='
name|'vm_file_info'
newline|'\n'
nl|'\n'
name|'return'
name|'create_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_build_import_spec_for_import_vapp
dedent|''
name|'def'
name|'_build_import_spec_for_import_vapp'
op|'('
name|'session'
op|','
name|'vm_name'
op|','
name|'datastore_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vm_create_spec'
op|'='
name|'_build_shadow_vm_config_spec'
op|'('
nl|'\n'
name|'session'
op|','
name|'vm_name'
op|','
number|'0'
op|','
name|'constants'
op|'.'
name|'DISK_TYPE_THIN'
op|','
name|'datastore_name'
op|')'
newline|'\n'
nl|'\n'
name|'client_factory'
op|'='
name|'session'
op|'.'
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'vm_import_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineImportSpec'"
op|')'
newline|'\n'
name|'vm_import_spec'
op|'.'
name|'configSpec'
op|'='
name|'vm_create_spec'
newline|'\n'
name|'return'
name|'vm_import_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image_stream_optimized
dedent|''
name|'def'
name|'fetch_image_stream_optimized'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
name|'vm_name'
op|','
nl|'\n'
name|'ds_name'
op|','
name|'vm_folder_ref'
op|','
name|'res_pool_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fetch image from Glance to ESX datastore."""'
newline|'\n'
name|'image_ref'
op|'='
name|'instance'
op|'.'
name|'image_ref'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Downloading image file data %(image_ref)s to the ESX "'
nl|'\n'
string|'"as VM named \'%(vm_name)s\'"'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'image_ref'
op|','
string|"'vm_name'"
op|':'
name|'vm_name'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vm_import_spec'
op|'='
name|'_build_import_spec_for_import_vapp'
op|'('
nl|'\n'
name|'session'
op|','
name|'vm_name'
op|','
name|'ds_name'
op|')'
newline|'\n'
nl|'\n'
name|'read_iter'
op|'='
name|'IMAGE_API'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'read_handle'
op|'='
name|'rw_handles'
op|'.'
name|'ImageReadHandle'
op|'('
name|'read_iter'
op|')'
newline|'\n'
nl|'\n'
name|'write_handle'
op|'='
name|'rw_handles'
op|'.'
name|'VmdkWriteHandle'
op|'('
name|'session'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_port'
op|','
nl|'\n'
name|'res_pool_ref'
op|','
nl|'\n'
name|'vm_folder_ref'
op|','
nl|'\n'
name|'vm_import_spec'
op|','
nl|'\n'
name|'file_size'
op|')'
newline|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
nl|'\n'
name|'read_handle'
op|','
nl|'\n'
name|'file_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'write_handle'
op|')'
newline|'\n'
nl|'\n'
name|'imported_vm_ref'
op|'='
name|'write_handle'
op|'.'
name|'get_imported_vm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Downloaded image file data %(image_ref)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'instance'
op|'.'
name|'image_ref'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'vim'
op|','
string|'"UnregisterVM"'
op|','
name|'imported_vm_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"The imported VM was unregistered"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_name_from_ovf
dedent|''
name|'def'
name|'get_vmdk_name_from_ovf'
op|'('
name|'xmlstr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the OVA descriptor to extract the vmdk name."""'
newline|'\n'
nl|'\n'
name|'ovf'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xmlstr'
op|')'
newline|'\n'
name|'nsovf'
op|'='
string|'"{%s}"'
op|'%'
name|'ovf'
op|'.'
name|'nsmap'
op|'['
string|'"ovf"'
op|']'
newline|'\n'
nl|'\n'
name|'disk'
op|'='
name|'ovf'
op|'.'
name|'find'
op|'('
string|'"./%sDiskSection/%sDisk"'
op|'%'
op|'('
name|'nsovf'
op|','
name|'nsovf'
op|')'
op|')'
newline|'\n'
name|'file_id'
op|'='
name|'disk'
op|'.'
name|'get'
op|'('
string|'"%sfileRef"'
op|'%'
name|'nsovf'
op|')'
newline|'\n'
nl|'\n'
name|'file'
op|'='
name|'ovf'
op|'.'
name|'find'
op|'('
string|'\'./%sReferences/%sFile[@%sid="%s"]\''
op|'%'
op|'('
name|'nsovf'
op|','
name|'nsovf'
op|','
nl|'\n'
name|'nsovf'
op|','
name|'file_id'
op|')'
op|')'
newline|'\n'
name|'vmdk_name'
op|'='
name|'file'
op|'.'
name|'get'
op|'('
string|'"%shref"'
op|'%'
name|'nsovf'
op|')'
newline|'\n'
name|'return'
name|'vmdk_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image_ova
dedent|''
name|'def'
name|'fetch_image_ova'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
name|'vm_name'
op|','
name|'ds_name'
op|','
nl|'\n'
name|'vm_folder_ref'
op|','
name|'res_pool_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Download the OVA image from the glance image server to the\n    Nova compute node.\n    """'
newline|'\n'
name|'image_ref'
op|'='
name|'instance'
op|'.'
name|'image_ref'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Downloading OVA image file %(image_ref)s to the ESX "'
nl|'\n'
string|'"as VM named \'%(vm_name)s\'"'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'image_ref'
op|','
string|"'vm_name'"
op|':'
name|'vm_name'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'int'
op|'('
name|'metadata'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vm_import_spec'
op|'='
name|'_build_import_spec_for_import_vapp'
op|'('
nl|'\n'
name|'session'
op|','
name|'vm_name'
op|','
name|'ds_name'
op|')'
newline|'\n'
nl|'\n'
name|'read_iter'
op|'='
name|'IMAGE_API'
op|'.'
name|'download'
op|'('
name|'context'
op|','
name|'image_ref'
op|')'
newline|'\n'
name|'ova_fd'
op|','
name|'ova_path'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(arnaud): Look to eliminate first writing OVA to file system'
nl|'\n'
indent|'        '
name|'with'
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'ova_fd'
op|','
string|"'w'"
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'chunk'
name|'in'
name|'read_iter'
op|':'
newline|'\n'
indent|'                '
name|'fp'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'with'
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'ova_path'
op|','
name|'mode'
op|'='
string|'"r"'
op|')'
name|'as'
name|'tar'
op|':'
newline|'\n'
indent|'            '
name|'vmdk_name'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'tar_info'
name|'in'
name|'tar'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'tar_info'
name|'and'
name|'tar_info'
op|'.'
name|'name'
op|'.'
name|'endswith'
op|'('
string|'".ovf"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'extracted'
op|'='
name|'tar'
op|'.'
name|'extractfile'
op|'('
name|'tar_info'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'xmlstr'
op|'='
name|'extracted'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'vmdk_name'
op|'='
name|'get_vmdk_name_from_ovf'
op|'('
name|'xmlstr'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'vmdk_name'
name|'and'
name|'tar_info'
op|'.'
name|'name'
op|'.'
name|'startswith'
op|'('
name|'vmdk_name'
op|')'
op|':'
newline|'\n'
comment|'# Actual file name is <vmdk_name>.XXXXXXX'
nl|'\n'
indent|'                    '
name|'extracted'
op|'='
name|'tar'
op|'.'
name|'extractfile'
op|'('
name|'tar_info'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'write_handle'
op|'='
name|'rw_handles'
op|'.'
name|'VmdkWriteHandle'
op|'('
nl|'\n'
name|'session'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_port'
op|','
nl|'\n'
name|'res_pool_ref'
op|','
nl|'\n'
name|'vm_folder_ref'
op|','
nl|'\n'
name|'vm_import_spec'
op|','
nl|'\n'
name|'file_size'
op|')'
newline|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
nl|'\n'
name|'extracted'
op|','
nl|'\n'
name|'file_size'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'write_handle'
op|')'
newline|'\n'
name|'extracted'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Downloaded OVA image file %(image_ref)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
name|'instance'
op|'.'
name|'image_ref'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'imported_vm_ref'
op|'='
name|'write_handle'
op|'.'
name|'get_imported_vm'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'vim'
op|','
string|'"UnregisterVM"'
op|','
nl|'\n'
name|'imported_vm_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"The imported VM was unregistered"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
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
string|'"Extracting vmdk from OVA failed."'
op|')'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'ova_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upload_image_stream_optimized
dedent|''
dedent|''
name|'def'
name|'upload_image_stream_optimized'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'instance'
op|','
name|'session'
op|','
nl|'\n'
name|'vm'
op|','
name|'vmdk_size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Upload the snapshotted vm disk file to Glance image server."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Uploading image %s"'
op|','
name|'image_id'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'IMAGE_API'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
name|'read_handle'
op|'='
name|'rw_handles'
op|'.'
name|'VmdkReadHandle'
op|'('
name|'session'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_host'
op|','
nl|'\n'
name|'session'
op|'.'
name|'_port'
op|','
nl|'\n'
name|'vm'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'vmdk_size'
op|')'
newline|'\n'
nl|'\n'
comment|"# Set the image properties. It is important to set the 'size' to 0."
nl|'\n'
comment|"# Otherwise, the image service client will use the VM's disk capacity"
nl|'\n'
comment|'# which will not be the image size after upload, since it is converted'
nl|'\n'
comment|'# to a stream-optimized sparse disk.'
nl|'\n'
name|'image_metadata'
op|'='
op|'{'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'metadata'
op|'['
string|"'is_public'"
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'metadata'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'bare'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'vmware_image_version'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'vmware_disktype'"
op|':'
string|"'streamOptimized'"
op|','
nl|'\n'
string|"'owner_id'"
op|':'
name|'instance'
op|'.'
name|'project_id'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Passing 0 as the file size since data size to be transferred cannot be'
nl|'\n'
comment|'# predetermined.'
nl|'\n'
name|'start_transfer'
op|'('
name|'context'
op|','
nl|'\n'
name|'read_handle'
op|','
nl|'\n'
number|'0'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_id'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'image_metadata'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Uploaded image %s to the Glance image server"'
op|','
name|'image_id'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
