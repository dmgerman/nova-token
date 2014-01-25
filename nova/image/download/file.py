begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
name|'logging'
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
name|'download'
op|'.'
name|'base'
name|'as'
name|'xfer_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'utils'
name|'as'
name|'lv_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
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
DECL|variable|opt_group
name|'opt_group'
op|'='
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
name|'name'
op|'='
string|"'filesystems'"
op|','
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'List of file systems that are configured '"
nl|'\n'
string|"'in this file in the '"
nl|'\n'
string|"'image_file_url:<list entry name> '"
nl|'\n'
string|"'sections'"
op|')'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'opt_group'
op|','
name|'group'
op|'='
string|'"image_file_url"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#  This module extends the configuration options for nova.conf.  If the user'
nl|'\n'
comment|'#  wishes to use the specific configuration settings the following needs to'
nl|'\n'
comment|'#  be added to nova.conf:'
nl|'\n'
comment|'#  [image_file_url]'
nl|'\n'
comment|'#  filesystem = <a list of strings referencing a config section>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#  For each entry in the filesystem list a new configuration section must be'
nl|'\n'
comment|'#  added with the following format:'
nl|'\n'
comment|'#  [image_file_url:<list entry>]'
nl|'\n'
comment|'#  id = <string>'
nl|'\n'
comment|'#  mountpoint = <string>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    id:'
nl|'\n'
comment|'#        An opaque string.  In order for this module to know that the remote'
nl|'\n'
comment|'#        FS is the same one that is mounted locally it must share information'
nl|'\n'
comment|'#        with the glance deployment.  Both glance and nova-compute must be'
nl|'\n'
comment|'#        configured with a unique matching string.  This ensures that the'
nl|'\n'
comment|'#        file:// advertised URL is describing a file system that is known'
nl|'\n'
comment|'#        to nova-compute'
nl|'\n'
comment|'#    mountpoint:'
nl|'\n'
comment|'#        The location at which the file system is locally mounted.  Glance'
nl|'\n'
comment|'#        may mount a shared file system on a different path than nova-compute.'
nl|'\n'
comment|'#        This value will be compared against the metadata advertised with'
nl|'\n'
comment|'#        glance and paths will be adjusted to ensure that the correct file'
nl|'\n'
comment|'#        file is copied.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#  If these values are not added to nova.conf and the file module is in the'
nl|'\n'
comment|'#  allowed_direct_url_schemes list, then the legacy behavior will occur such'
nl|'\n'
comment|'#  that a copy will be attempted assuming that the glance and nova file systems'
nl|'\n'
comment|'#  are the same.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileTransfer
name|'class'
name|'FileTransfer'
op|'('
name|'xfer_base'
op|'.'
name|'TransferBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|desc_required_keys
indent|'    '
name|'desc_required_keys'
op|'='
op|'['
string|"'id'"
op|','
string|"'mountpoint'"
op|']'
newline|'\n'
nl|'\n'
comment|'#NOTE(jbresnah) because the group under which these options are added is'
nl|'\n'
comment|'# dyncamically determined these options need to stay out of global space'
nl|'\n'
comment|'# or they will confuse generate_sample.sh'
nl|'\n'
DECL|variable|filesystem_opts
name|'filesystem_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'id'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'A unique ID given to each file system.  This is '"
nl|'\n'
string|"'value is set in Glance and agreed upon here so '"
nl|'\n'
string|"'that the operator knowns they are dealing with '"
nl|'\n'
string|"'the same file system.'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'mountpoint'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'The path at which the file system is mounted.'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_options
name|'def'
name|'_get_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fs_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'fs'
name|'in'
name|'CONF'
op|'.'
name|'image_file_url'
op|'.'
name|'filesystems'
op|':'
newline|'\n'
indent|'            '
name|'group_name'
op|'='
string|"'image_file_url:'"
op|'+'
name|'fs'
newline|'\n'
name|'conf_group'
op|'='
name|'CONF'
op|'['
name|'group_name'
op|']'
newline|'\n'
name|'if'
name|'conf_group'
op|'.'
name|'id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'The group %s(group_name) must be configured with '"
nl|'\n'
string|"'an id.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageDownloadModuleConfigurationError'
op|'('
nl|'\n'
name|'module'
op|'='
name|'str'
op|'('
name|'self'
op|')'
op|','
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'fs_dict'
op|'['
name|'CONF'
op|'['
name|'group_name'
op|']'
op|'.'
name|'id'
op|']'
op|'='
name|'CONF'
op|'['
name|'group_name'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'fs_dict'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# create the needed options'
nl|'\n'
indent|'        '
name|'for'
name|'fs'
name|'in'
name|'CONF'
op|'.'
name|'image_file_url'
op|'.'
name|'filesystems'
op|':'
newline|'\n'
indent|'            '
name|'group_name'
op|'='
string|"'image_file_url:'"
op|'+'
name|'fs'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'self'
op|'.'
name|'filesystem_opts'
op|','
name|'group'
op|'='
name|'group_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_config
dedent|''
dedent|''
name|'def'
name|'_verify_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'fs_key'
name|'in'
name|'self'
op|'.'
name|'filesystems'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'r'
name|'in'
name|'self'
op|'.'
name|'desc_required_keys'
op|':'
newline|'\n'
indent|'                '
name|'fs_ent'
op|'='
name|'self'
op|'.'
name|'filesystems'
op|'['
name|'fs_key'
op|']'
newline|'\n'
name|'if'
name|'fs_ent'
op|'['
name|'r'
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|"'The key %s is required in all file system '"
nl|'\n'
string|"'descriptions.'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageDownloadModuleConfigurationError'
op|'('
nl|'\n'
name|'module'
op|'='
name|'str'
op|'('
name|'self'
op|')'
op|','
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_file_system_lookup
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_file_system_lookup'
op|'('
name|'self'
op|','
name|'metadata'
op|','
name|'url_parts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'r'
name|'in'
name|'self'
op|'.'
name|'desc_required_keys'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'r'
name|'not'
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'                '
name|'url'
op|'='
name|'url_parts'
op|'.'
name|'geturl'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'The key %(r)s is required in the location metadata '"
nl|'\n'
string|"'to access the url %(url)s.'"
op|')'
op|'%'
op|'{'
string|"'r'"
op|':'
name|'r'
op|','
string|"'url'"
op|':'
name|'url'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageDownloadModuleMetaDataError'
op|'('
nl|'\n'
name|'module'
op|'='
name|'str'
op|'('
name|'self'
op|')'
op|','
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'id'
op|'='
name|'metadata'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'self'
op|'.'
name|'filesystems'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'The ID %(id)s is unknown.'"
op|')'
op|'%'
op|'{'
string|"'id'"
op|':'
name|'id'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'fs_descriptor'
op|'='
name|'self'
op|'.'
name|'filesystems'
op|'['
name|'id'
op|']'
newline|'\n'
name|'return'
name|'fs_descriptor'
newline|'\n'
nl|'\n'
DECL|member|_normalize_destination
dedent|''
name|'def'
name|'_normalize_destination'
op|'('
name|'self'
op|','
name|'nova_mount'
op|','
name|'glance_mount'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'path'
op|'.'
name|'startswith'
op|'('
name|'glance_mount'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'The mount point advertised by glance: %(glance_mount)s, '"
nl|'\n'
string|"'does not match the URL path: %(path)s'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'glance_mount'"
op|':'
name|'glance_mount'
op|','
string|"'path'"
op|':'
name|'path'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageDownloadModuleMetaDataError'
op|'('
nl|'\n'
name|'module'
op|'='
name|'str'
op|'('
name|'self'
op|')'
op|','
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'new_path'
op|'='
name|'path'
op|'.'
name|'replace'
op|'('
name|'glance_mount'
op|','
name|'nova_mount'
op|','
number|'1'
op|')'
newline|'\n'
name|'return'
name|'new_path'
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
name|'url_parts'
op|','
name|'dst_file'
op|','
name|'metadata'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'filesystems'
op|'='
name|'self'
op|'.'
name|'_get_options'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'filesystems'
op|':'
newline|'\n'
comment|'#NOTE(jbresnah) when nothing is configured assume legacy behavior'
nl|'\n'
indent|'            '
name|'nova_mountpoint'
op|'='
string|"'/'"
newline|'\n'
name|'glance_mountpoint'
op|'='
string|"'/'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_verify_config'
op|'('
op|')'
newline|'\n'
name|'fs_descriptor'
op|'='
name|'self'
op|'.'
name|'_file_system_lookup'
op|'('
name|'metadata'
op|','
name|'url_parts'
op|')'
newline|'\n'
name|'if'
name|'fs_descriptor'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'No matching ID for the URL %s was found.'"
op|')'
op|'%'
nl|'\n'
name|'url_parts'
op|'.'
name|'geturl'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageDownloadModuleError'
op|'('
name|'reason'
op|'='
name|'msg'
op|','
nl|'\n'
name|'module'
op|'='
name|'str'
op|'('
name|'self'
op|')'
op|')'
newline|'\n'
dedent|''
name|'nova_mountpoint'
op|'='
name|'fs_descriptor'
op|'['
string|"'mountpoint'"
op|']'
newline|'\n'
name|'glance_mountpoint'
op|'='
name|'metadata'
op|'['
string|"'mountpoint'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'source_file'
op|'='
name|'self'
op|'.'
name|'_normalize_destination'
op|'('
name|'nova_mountpoint'
op|','
nl|'\n'
name|'glance_mountpoint'
op|','
nl|'\n'
name|'url_parts'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'lv_utils'
op|'.'
name|'copy_image'
op|'('
name|'source_file'
op|','
name|'dst_file'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Copied %(source_file)s using %(module_str)s'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'source_file'"
op|':'
name|'source_file'
op|','
string|"'module_str'"
op|':'
name|'str'
op|'('
name|'self'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_download_hander
dedent|''
dedent|''
name|'def'
name|'get_download_hander'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FileTransfer'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_schemes
dedent|''
name|'def'
name|'get_schemes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
string|"'file'"
op|','
string|"'filesystem'"
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
