begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'command'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'common'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
name|'import'
name|'exception'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMDiskAdapter
name|'class'
name|'PowerVMDiskAdapter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""PowerVM disk adapter interface\n    Provides a contract to implement multiple ways to generate\n    and attach volumes to virtual machines using local and/or\n    external storage\n    """'
newline|'\n'
nl|'\n'
DECL|member|create_volume
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a volume with a minimum size\n\n        :param size: size of the volume in bytes\n        :returns: string -- the name of the disk device.\n      """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the disk and its associated vSCSI connection\n\n        :param volume_info: dictionary with volume info including name of\n        disk device in /dev/\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_volume_from_image
dedent|''
name|'def'
name|'create_volume_from_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a Volume and copies the specified image to it\n\n        :param context: nova context used to retrieve image from glance\n        :param instance: instance to create the volume for\n        :param image_id: image_id reference used to locate image in glance\n        :returns: dictionary with the name of the created\n                  disk device in \'device_name\' key\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_image_from_volume
dedent|''
name|'def'
name|'create_image_from_volume'
op|'('
name|'self'
op|','
name|'device_name'
op|','
name|'context'
op|','
nl|'\n'
name|'image_id'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Capture the contents of a volume and upload to glance\n\n        :param device_name: device in /dev/ to capture\n        :param context: nova context for operation\n        :param image_id: image reference to pre-created image in glance\n        :param image_meta: metadata for new image\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|migrate_volume
dedent|''
name|'def'
name|'migrate_volume'
op|'('
name|'self'
op|','
name|'lv_name'
op|','
name|'src_host'
op|','
name|'dest'
op|','
name|'image_path'
op|','
nl|'\n'
name|'instance_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy a logical volume to file, compress, and transfer\n\n        :param lv_name: volume device name\n        :param src_host: source IP or DNS name.\n        :param dest: destination IP or DNS name\n        :param image_path: path to remote image storage directory\n        :param instance_name: name of instance that is being migrated\n        :returns: file path on destination of image file that was moved\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|attach_volume_to_host
dedent|''
name|'def'
name|'attach_volume_to_host'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Attaches volume to host using info passed in *args and **kargs\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|detach_volume_from_host
dedent|''
name|'def'
name|'detach_volume_from_host'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Detaches volume from host using info passed in *args and **kargs\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMLocalVolumeAdapter
dedent|''
dedent|''
name|'class'
name|'PowerVMLocalVolumeAdapter'
op|'('
name|'PowerVMDiskAdapter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Default block device providor for PowerVM\n\n    This disk adapter uses logical volumes on the hosting VIOS\n    to provide backing block devices for instances/LPARs\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PowerVMLocalVolumeAdapter'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'command'
op|'='
name|'command'
op|'.'
name|'IVMCommand'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_connection'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'connection_data'
op|'='
name|'connection'
newline|'\n'
nl|'\n'
DECL|member|_set_connection
dedent|''
name|'def'
name|'_set_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_connection'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_connection'
op|'='
name|'common'
op|'.'
name|'ssh_connect'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a logical volume with a minimum size\n\n        :param size: size of the logical volume in bytes\n        :returns: string -- the name of the new logical volume.\n        :raises: PowerVMNoSpaceLeftOnVolumeGroup\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_create_logical_volume'
op|'('
name|'size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the Logical Volume and its associated vSCSI connection\n\n        :param volume_info: Dictionary with volume info including name of\n        Logical Volume device in /dev/ via device_name key\n        """'
newline|'\n'
name|'disk_name'
op|'='
name|'volume_info'
op|'['
string|'"device_name"'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Removing the logical volume \'%s\'"'
op|')'
op|'%'
name|'disk_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_remove_logical_volume'
op|'('
name|'disk_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume_from_image
dedent|''
name|'def'
name|'create_volume_from_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a Logical Volume and copies the specified image to it\n\n        :param context: nova context used to retrieve image from glance\n        :param instance: instance to create the volume for\n        :param image_id: image_id reference used to locate image in glance\n        :returns: dictionary with the name of the created\n                  Logical Volume device in \'device_name\' key\n        """'
newline|'\n'
nl|'\n'
name|'file_name'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
name|'image_id'
op|','
string|"'gz'"
op|']'
op|')'
newline|'\n'
name|'file_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'powervm_img_local_path'
op|','
nl|'\n'
name|'file_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'file_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Fetching image \'%s\' from glance"'
op|')'
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'images'
op|'.'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'file_path'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
op|'('
name|'_'
op|'('
string|'"Using image found at \'%s\'"'
op|')'
op|'%'
name|'file_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Ensuring image \'%s\' exists on IVM"'
op|')'
op|'%'
name|'file_path'
op|')'
newline|'\n'
name|'remote_path'
op|'='
name|'CONF'
op|'.'
name|'powervm_img_remote_path'
newline|'\n'
name|'remote_file_name'
op|','
name|'size'
op|'='
name|'self'
op|'.'
name|'_copy_image_file'
op|'('
name|'file_path'
op|','
name|'remote_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# calculate root device size in bytes'
nl|'\n'
comment|'# we respect the minimum root device size in constants'
nl|'\n'
name|'size_gb'
op|'='
name|'max'
op|'('
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'root_gb'"
op|']'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'POWERVM_MIN_ROOT_GB'
op|')'
newline|'\n'
name|'size'
op|'='
name|'size_gb'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Creating logical volume of size %s bytes"'
op|')'
op|'%'
name|'size'
op|')'
newline|'\n'
name|'disk_name'
op|'='
name|'self'
op|'.'
name|'_create_logical_volume'
op|'('
name|'size'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Copying image to the device \'%s\'"'
op|')'
op|'%'
name|'disk_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_copy_file_to_device'
op|'('
name|'remote_file_name'
op|','
name|'disk_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Error while creating logical volume from image. "'
nl|'\n'
string|'"Will attempt cleanup."'
op|')'
op|')'
newline|'\n'
comment|'# attempt cleanup of logical volume before re-raising exception'
nl|'\n'
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'delete_volume'
op|'('
name|'disk_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Error while attempting cleanup of failed '"
nl|'\n'
string|"'deploy to logical volume.'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
op|'{'
string|"'device_name'"
op|':'
name|'disk_name'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create_image_from_volume
dedent|''
name|'def'
name|'create_image_from_volume'
op|'('
name|'self'
op|','
name|'device_name'
op|','
name|'context'
op|','
nl|'\n'
name|'image_id'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Capture the contents of a volume and upload to glance\n\n        :param device_name: device in /dev/ to capture\n        :param context: nova context for operation\n        :param image_id: image reference to pre-created image in glance\n        :param image_meta: metadata for new image\n        """'
newline|'\n'
nl|'\n'
comment|'# do the disk copy'
nl|'\n'
name|'dest_file_path'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'CONF'
op|'.'
name|'powervm_img_remote_path'
op|','
nl|'\n'
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_copy_device_to_file'
op|'('
name|'device_name'
op|','
name|'dest_file_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# compress and copy the file back to the nova-compute host'
nl|'\n'
name|'snapshot_file_path'
op|'='
name|'self'
op|'.'
name|'_copy_image_file_from_host'
op|'('
nl|'\n'
name|'dest_file_path'
op|','
name|'CONF'
op|'.'
name|'powervm_img_local_path'
op|','
nl|'\n'
name|'compress'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# get glance service'
nl|'\n'
name|'glance_service'
op|','
name|'image_id'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
nl|'\n'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# upload snapshot file to glance'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'snapshot_file_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'img_file'
op|':'
newline|'\n'
indent|'            '
name|'glance_service'
op|'.'
name|'update'
op|'('
name|'context'
op|','
nl|'\n'
name|'image_id'
op|','
nl|'\n'
name|'image_meta'
op|','
nl|'\n'
name|'img_file'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Snapshot added to glance."'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# clean up local image file'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'snapshot_file_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'ose'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to clean up snapshot file "'
nl|'\n'
string|'"%(snapshot_file_path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_volume
dedent|''
dedent|''
name|'def'
name|'migrate_volume'
op|'('
name|'self'
op|','
name|'lv_name'
op|','
name|'src_host'
op|','
name|'dest'
op|','
name|'image_path'
op|','
nl|'\n'
name|'instance_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy a logical volume to file, compress, and transfer\n\n        :param lv_name: logical volume device name\n        :param dest: destination IP or DNS name\n        :param image_path: path to remote image storage directory\n        :param instance_name: name of instance that is being migrated\n        :returns: file path on destination of image file that was moved\n        """'
newline|'\n'
name|'if'
name|'instance_name'
op|':'
newline|'\n'
indent|'            '
name|'file_name'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'instance_name'
op|','
string|"'_rsz'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'file_name'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'lv_name'
op|','
string|"'_rsz'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'file_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image_path'
op|','
name|'file_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_copy_device_to_file'
op|'('
name|'lv_name'
op|','
name|'file_path'
op|')'
newline|'\n'
name|'cmds'
op|'='
string|"'gzip %s'"
op|'%'
name|'file_path'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmds'
op|')'
newline|'\n'
name|'file_path'
op|'='
name|'file_path'
op|'+'
string|"'.gz'"
newline|'\n'
comment|'# If destination is not same host'
nl|'\n'
comment|'# transfer file to destination VIOS system'
nl|'\n'
name|'if'
op|'('
name|'src_host'
op|'!='
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'common'
op|'.'
name|'vios_to_vios_auth'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|'.'
name|'host'
op|','
nl|'\n'
name|'dest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'connection_data'
op|')'
name|'as'
name|'key_name'
op|':'
newline|'\n'
indent|'                '
name|'cmd'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|'\'scp -o "StrictHostKeyChecking no"\''
op|','
nl|'\n'
op|'('
string|"'-i %s'"
op|'%'
name|'key_name'
op|')'
op|','
nl|'\n'
name|'file_path'
op|','
nl|'\n'
string|"'%s@%s:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|'.'
name|'username'
op|','
nl|'\n'
name|'dest'
op|','
nl|'\n'
name|'image_path'
op|')'
nl|'\n'
op|']'
op|')'
newline|'\n'
comment|'# do the remote copy'
nl|'\n'
name|'self'
op|'.'
name|'run_vios_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# cleanup local file only if transferring to remote system'
nl|'\n'
comment|'# otherwise keep the file to boot from locally and clean up later'
nl|'\n'
dedent|''
name|'cleanup_cmd'
op|'='
string|"'rm %s'"
op|'%'
name|'file_path'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cleanup_cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'file_path'
newline|'\n'
nl|'\n'
DECL|member|attach_volume_to_host
dedent|''
name|'def'
name|'attach_volume_to_host'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|detach_volume_from_host
dedent|''
name|'def'
name|'detach_volume_from_host'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_create_logical_volume
dedent|''
name|'def'
name|'_create_logical_volume'
op|'('
name|'self'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a logical volume with a minimum size.\n\n        :param size: size of the logical volume in bytes\n        :returns: string -- the name of the new logical volume.\n        :raises: PowerVMNoSpaceLeftOnVolumeGroup\n        """'
newline|'\n'
name|'vgs'
op|'='
name|'self'
op|'.'
name|'run_vios_command'
op|'('
name|'self'
op|'.'
name|'command'
op|'.'
name|'lsvg'
op|'('
op|')'
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'command'
op|'.'
name|'lsvg'
op|'('
string|"'%s -field vgname freepps -fmt :'"
op|'%'
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'vgs'
op|')'
op|')'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'found_vg'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|"# If it's not a multiple of 1MB we get the next"
nl|'\n'
comment|'# multiple and use it as the megabyte_size.'
nl|'\n'
name|'megabyte'
op|'='
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'if'
op|'('
name|'size'
op|'%'
name|'megabyte'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'megabyte_size'
op|'='
name|'int'
op|'('
name|'size'
op|'/'
name|'megabyte'
op|')'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'megabyte_size'
op|'='
name|'size'
op|'/'
name|'megabyte'
newline|'\n'
nl|'\n'
comment|'# Search for a volume group with enough free space for'
nl|'\n'
comment|'# the new logical volume.'
nl|'\n'
dedent|''
name|'for'
name|'vg'
name|'in'
name|'output'
op|':'
newline|'\n'
comment|"# Returned output example: 'rootvg:396 (25344 megabytes)'"
nl|'\n'
indent|'            '
name|'match'
op|'='
name|'re'
op|'.'
name|'search'
op|'('
string|"r'^(\\w+):\\d+\\s\\((\\d+).+$'"
op|','
name|'vg'
op|')'
newline|'\n'
name|'if'
name|'match'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'vg_name'
op|','
name|'avail_size'
op|'='
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
newline|'\n'
name|'if'
name|'megabyte_size'
op|'<='
name|'int'
op|'('
name|'avail_size'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'found_vg'
op|'='
name|'vg_name'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'found_vg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Could not create logical volume. '"
nl|'\n'
string|"'No space left on any volume group.'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMNoSpaceLeftOnVolumeGroup'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'='
name|'self'
op|'.'
name|'command'
op|'.'
name|'mklv'
op|'('
string|"'%s %sB'"
op|'%'
op|'('
name|'found_vg'
op|','
name|'size'
op|'/'
number|'512'
op|')'
op|')'
newline|'\n'
name|'lv_name'
op|'='
name|'self'
op|'.'
name|'run_vios_command'
op|'('
name|'cmd'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'lv_name'
newline|'\n'
nl|'\n'
DECL|member|_remove_logical_volume
dedent|''
name|'def'
name|'_remove_logical_volume'
op|'('
name|'self'
op|','
name|'lv_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the lv and the connection between its associated vscsi.\n\n        :param lv_name: a logical volume name\n        """'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'command'
op|'.'
name|'rmvdev'
op|'('
string|"'-vdev %s -rmlv'"
op|'%'
name|'lv_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_copy_file_to_device
dedent|''
name|'def'
name|'_copy_file_to_device'
op|'('
name|'self'
op|','
name|'source_path'
op|','
name|'device'
op|','
name|'decompress'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy file to device.\n\n        :param source_path: path to input source file\n        :param device: output device name\n        :param decompress: if True (default) the file will be decompressed\n                           on the fly while being copied to the drive\n        """'
newline|'\n'
name|'if'
name|'decompress'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
op|'('
string|"'gunzip -c %s | dd of=/dev/%s bs=1024k'"
op|'%'
nl|'\n'
op|'('
name|'source_path'
op|','
name|'device'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
string|"'dd if=%s of=/dev/%s bs=1024k'"
op|'%'
op|'('
name|'source_path'
op|','
name|'device'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_copy_device_to_file
dedent|''
name|'def'
name|'_copy_device_to_file'
op|'('
name|'self'
op|','
name|'device_name'
op|','
name|'file_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy a device to a file using dd\n\n        :param device_name: device name to copy from\n        :param file_path: output file path\n        """'
newline|'\n'
name|'cmd'
op|'='
string|"'dd if=/dev/%s of=%s bs=1024k'"
op|'%'
op|'('
name|'device_name'
op|','
name|'file_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_md5sum_remote_file
dedent|''
name|'def'
name|'_md5sum_remote_file'
op|'('
name|'self'
op|','
name|'remote_path'
op|')'
op|':'
newline|'\n'
comment|'# AIX6/VIOS cannot md5sum files with sizes greater than ~2GB'
nl|'\n'
indent|'        '
name|'cmd'
op|'='
op|'('
string|'"perl -MDigest::MD5 -e \'my $file = \\"%s\\"; open(FILE, $file); "'
nl|'\n'
string|'"binmode(FILE); "'
nl|'\n'
string|'"print Digest::MD5->new->addfile(*FILE)->hexdigest, "'
nl|'\n'
string|'"\\" $file\\n\\";\'"'
op|'%'
name|'remote_path'
op|')'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'output'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_copy_image_file
dedent|''
name|'def'
name|'_copy_image_file'
op|'('
name|'self'
op|','
name|'source_path'
op|','
name|'remote_path'
op|','
name|'decompress'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy file to VIOS, decompress it, and return its new size and name.\n\n        :param source_path: source file path\n        :param remote_path remote file path\n        :param decompress: if True, decompressess the file after copying;\n                           if False (default), just copies the file\n        """'
newline|'\n'
comment|'# Calculate source image checksum'
nl|'\n'
name|'hasher'
op|'='
name|'hashlib'
op|'.'
name|'md5'
op|'('
op|')'
newline|'\n'
name|'block_size'
op|'='
number|'0x10000'
newline|'\n'
name|'img_file'
op|'='
name|'file'
op|'('
name|'source_path'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'buf'
op|'='
name|'img_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'buf'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'hasher'
op|'.'
name|'update'
op|'('
name|'buf'
op|')'
newline|'\n'
name|'buf'
op|'='
name|'img_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
dedent|''
name|'source_cksum'
op|'='
name|'hasher'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'comp_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'remote_path'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'source_path'
op|')'
op|')'
newline|'\n'
name|'uncomp_path'
op|'='
name|'comp_path'
op|'.'
name|'rstrip'
op|'('
string|'".gz"'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'decompress'
op|':'
newline|'\n'
indent|'            '
name|'final_path'
op|'='
name|'comp_path'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'final_path'
op|'='
name|'uncomp_path'
newline|'\n'
nl|'\n'
comment|'# Check whether the image is already on IVM'
nl|'\n'
dedent|''
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command'
op|'('
string|'"ls %s"'
op|'%'
name|'final_path'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# If the image does not exist already'
nl|'\n'
name|'if'
name|'not'
name|'output'
op|':'
newline|'\n'
comment|'# Copy file to IVM'
nl|'\n'
indent|'            '
name|'common'
op|'.'
name|'ftp_put_command'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|','
name|'source_path'
op|','
nl|'\n'
name|'remote_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Verify image file checksums match'
nl|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'_md5sum_remote_file'
op|'('
name|'final_path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'output'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unable to get checksum"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMFileTransferFailed'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'source_cksum'
op|'!='
name|'output'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Image checksums do not match"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMFileTransferFailed'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'decompress'
op|':'
newline|'\n'
comment|'# Unzip the image'
nl|'\n'
indent|'                '
name|'cmd'
op|'='
string|'"/usr/bin/gunzip %s"'
op|'%'
name|'comp_path'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# Remove existing image file'
nl|'\n'
name|'cmd'
op|'='
string|'"/usr/bin/rm -f %s.*"'
op|'%'
name|'uncomp_path'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# Rename unzipped image'
nl|'\n'
name|'cmd'
op|'='
string|'"/usr/bin/mv %s %s"'
op|'%'
op|'('
name|'uncomp_path'
op|','
name|'final_path'
op|')'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# Remove compressed image file'
nl|'\n'
name|'cmd'
op|'='
string|'"/usr/bin/rm -f %s"'
op|'%'
name|'comp_path'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Image found on host at \'%s\'"'
op|')'
op|'%'
name|'final_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Calculate file size in multiples of 512 bytes'
nl|'\n'
dedent|''
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command'
op|'('
string|'"ls -o %s|awk \'{print $4}\'"'
op|'%'
nl|'\n'
name|'final_path'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'output'
op|':'
newline|'\n'
indent|'            '
name|'size'
op|'='
name|'int'
op|'('
name|'output'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Uncompressed image file not found"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMFileTransferFailed'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'size'
op|'%'
number|'512'
op|'!='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'size'
op|'='
op|'('
name|'int'
op|'('
name|'size'
op|'/'
number|'512'
op|')'
op|'+'
number|'1'
op|')'
op|'*'
number|'512'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'final_path'
op|','
name|'size'
newline|'\n'
nl|'\n'
DECL|member|_copy_image_file_from_host
dedent|''
name|'def'
name|'_copy_image_file_from_host'
op|'('
name|'self'
op|','
name|'remote_source_path'
op|','
name|'local_dest_dir'
op|','
nl|'\n'
name|'compress'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Copy a file from IVM to the nova-compute host,\n        and return the location of the copy\n\n        :param remote_source_path remote source file path\n        :param local_dest_dir local destination directory\n        :param compress: if True, compress the file before transfer;\n                         if False (default), copy the file as is\n        """'
newline|'\n'
nl|'\n'
name|'temp_str'
op|'='
name|'common'
op|'.'
name|'aix_path_join'
op|'('
name|'local_dest_dir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'remote_source_path'
op|')'
op|')'
newline|'\n'
name|'local_file_path'
op|'='
name|'temp_str'
op|'+'
string|"'.gz'"
newline|'\n'
nl|'\n'
name|'if'
name|'compress'
op|':'
newline|'\n'
indent|'            '
name|'copy_from_path'
op|'='
name|'remote_source_path'
op|'+'
string|"'.gz'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'copy_from_path'
op|'='
name|'remote_source_path'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'compress'
op|':'
newline|'\n'
comment|'# Gzip the file'
nl|'\n'
indent|'            '
name|'cmd'
op|'='
string|'"/usr/bin/gzip %s"'
op|'%'
name|'remote_source_path'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup uncompressed remote file'
nl|'\n'
name|'cmd'
op|'='
string|'"/usr/bin/rm -f %s"'
op|'%'
name|'remote_source_path'
newline|'\n'
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get file checksum'
nl|'\n'
dedent|''
name|'output'
op|'='
name|'self'
op|'.'
name|'_md5sum_remote_file'
op|'('
name|'copy_from_path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'output'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unable to get checksum"'
op|')'
op|')'
newline|'\n'
name|'msg_args'
op|'='
op|'{'
string|"'file_path'"
op|':'
name|'copy_from_path'
op|'}'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMFileTransferFailed'
op|'('
op|'**'
name|'msg_args'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'source_chksum'
op|'='
name|'output'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# Copy file to host'
nl|'\n'
dedent|''
name|'common'
op|'.'
name|'ftp_get_command'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|','
nl|'\n'
name|'copy_from_path'
op|','
nl|'\n'
name|'local_file_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Calculate copied image checksum'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'local_file_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'image_file'
op|':'
newline|'\n'
indent|'            '
name|'hasher'
op|'='
name|'hashlib'
op|'.'
name|'md5'
op|'('
op|')'
newline|'\n'
name|'block_size'
op|'='
number|'0x10000'
newline|'\n'
name|'buf'
op|'='
name|'image_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
name|'while'
name|'len'
op|'('
name|'buf'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'hasher'
op|'.'
name|'update'
op|'('
name|'buf'
op|')'
newline|'\n'
name|'buf'
op|'='
name|'image_file'
op|'.'
name|'read'
op|'('
name|'block_size'
op|')'
newline|'\n'
dedent|''
name|'dest_chksum'
op|'='
name|'hasher'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# do comparison'
nl|'\n'
dedent|''
name|'if'
name|'source_chksum'
name|'and'
name|'dest_chksum'
op|'!='
name|'source_chksum'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Image checksums do not match"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'PowerVMFileTransferFailed'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup transferred remote file'
nl|'\n'
dedent|''
name|'cmd'
op|'='
string|'"/usr/bin/rm -f %s"'
op|'%'
name|'copy_from_path'
newline|'\n'
name|'output'
op|'='
name|'self'
op|'.'
name|'run_vios_command_as_root'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'local_file_path'
newline|'\n'
nl|'\n'
DECL|member|run_vios_command
dedent|''
name|'def'
name|'run_vios_command'
op|'('
name|'self'
op|','
name|'cmd'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run a remote command using an active ssh connection.\n\n        :param command: String with the command to run.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_connection'
op|'('
op|')'
newline|'\n'
name|'stdout'
op|','
name|'stderr'
op|'='
name|'utils'
op|'.'
name|'ssh_execute'
op|'('
name|'self'
op|'.'
name|'_connection'
op|','
name|'cmd'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
name|'return'
name|'stdout'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'splitlines'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_vios_command_as_root
dedent|''
name|'def'
name|'run_vios_command_as_root'
op|'('
name|'self'
op|','
name|'command'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run a remote command as root using an active ssh connection.\n\n        :param command: List of commands.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_connection'
op|'('
op|')'
newline|'\n'
name|'stdout'
op|','
name|'stderr'
op|'='
name|'common'
op|'.'
name|'ssh_command_as_root'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_connection'
op|','
name|'command'
op|','
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
name|'return'
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'splitlines'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
