begin_unit
comment|'# Copyright 2015 Red Hat, Inc'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
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
name|'importutils'
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
name|'_LW'
op|','
name|'_LI'
newline|'\n'
nl|'\n'
DECL|variable|libosinfo
name|'libosinfo'
op|'='
name|'None'
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
comment|'# TODO(vladikr) The current implementation will serve only as a temporary'
nl|'\n'
comment|"# solution, due to it's dependency on the libosinfo gobject library."
nl|'\n'
comment|'# In the future it will be replaced by a pure python library or by a direct'
nl|'\n'
comment|'# parsing of the libosinfo XML files. However, it will be possible only when'
nl|'\n'
comment|'# libosinfo project will declare the XML structure to be a stable ABI.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|_OsInfoDatabase
name|'class'
name|'_OsInfoDatabase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|_instance
indent|'    '
name|'_instance'
op|'='
name|'None'
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
nl|'\n'
indent|'        '
name|'global'
name|'libosinfo'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'libosinfo'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'libosinfo'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
nl|'\n'
string|"'gi.repository.Libosinfo'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ImportError'
name|'as'
name|'exp'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Cannot load Libosinfo: (%s)"'
op|')'
op|','
name|'exp'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'loader'
op|'='
name|'libosinfo'
op|'.'
name|'Loader'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loader'
op|'.'
name|'process_default_path'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'='
name|'self'
op|'.'
name|'loader'
op|'.'
name|'get_db'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'oslist'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'get_os_list'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_instance
name|'def'
name|'get_instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get libosinfo connection\n        """'
newline|'\n'
name|'if'
name|'cls'
op|'.'
name|'_instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'_OsInfoDatabase'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|get_os
dedent|''
name|'def'
name|'get_os'
op|'('
name|'self'
op|','
name|'os_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve OS object based on id, unique URI identifier of the OS\n           :param os_name: id - the unique operating systemidentifier\n                           e.g. http://fedoraproject.org/fedora/21,\n                           http://microsoft.com/win/xp,\n                           or a\n                           short-id - the short name of the OS\n                           e.g. fedora21, winxp\n           :returns: The operation system object Libosinfo.Os\n           :raise exception.OsInfoNotFound: If os hasn\'t been found\n        """'
newline|'\n'
name|'if'
name|'libosinfo'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os_name'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OsInfoNotFound'
op|'('
name|'os_name'
op|'='
string|"'Empty'"
op|')'
newline|'\n'
dedent|''
name|'fltr'
op|'='
name|'libosinfo'
op|'.'
name|'Filter'
op|'.'
name|'new'
op|'('
op|')'
newline|'\n'
name|'flt_field'
op|'='
string|"'id'"
name|'if'
name|'os_name'
op|'.'
name|'startswith'
op|'('
string|"'http'"
op|')'
name|'else'
string|"'short-id'"
newline|'\n'
name|'fltr'
op|'.'
name|'add_constraint'
op|'('
name|'flt_field'
op|','
name|'os_name'
op|')'
newline|'\n'
name|'filttered'
op|'='
name|'self'
op|'.'
name|'oslist'
op|'.'
name|'new_filtered'
op|'('
name|'fltr'
op|')'
newline|'\n'
name|'list_len'
op|'='
name|'filttered'
op|'.'
name|'get_length'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'list_len'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OsInfoNotFound'
op|'('
name|'os_name'
op|'='
name|'os_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'filttered'
op|'.'
name|'get_nth'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OsInfo
dedent|''
dedent|''
name|'class'
name|'OsInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""OS Information Structure\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'os_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_os_obj'
op|'='
name|'self'
op|'.'
name|'_get_os_obj'
op|'('
name|'os_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_os_obj
dedent|''
name|'def'
name|'_get_os_obj'
op|'('
name|'self'
op|','
name|'os_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_OsInfoDatabase'
op|'.'
name|'get_instance'
op|'('
op|')'
op|'.'
name|'get_os'
op|'('
name|'os_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NovaException'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Cannot find OS information - Reason: (%s)"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|network_model
name|'def'
name|'network_model'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_os_obj'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'fltr'
op|'='
name|'libosinfo'
op|'.'
name|'Filter'
op|'('
op|')'
newline|'\n'
name|'fltr'
op|'.'
name|'add_constraint'
op|'('
string|'"class"'
op|','
string|'"net"'
op|')'
newline|'\n'
name|'devs'
op|'='
name|'self'
op|'.'
name|'_os_obj'
op|'.'
name|'get_all_devices'
op|'('
name|'fltr'
op|')'
newline|'\n'
name|'if'
name|'devs'
op|'.'
name|'get_length'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'devs'
op|'.'
name|'get_nth'
op|'('
number|'0'
op|')'
op|'.'
name|'get_name'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|disk_model
name|'def'
name|'disk_model'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_os_obj'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'fltr'
op|'='
name|'libosinfo'
op|'.'
name|'Filter'
op|'('
op|')'
newline|'\n'
name|'fltr'
op|'.'
name|'add_constraint'
op|'('
string|'"class"'
op|','
string|'"block"'
op|')'
newline|'\n'
name|'devs'
op|'='
name|'self'
op|'.'
name|'_os_obj'
op|'.'
name|'get_all_devices'
op|'('
name|'fltr'
op|')'
newline|'\n'
name|'if'
name|'devs'
op|'.'
name|'get_length'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'devs'
op|'.'
name|'get_nth'
op|'('
number|'0'
op|')'
op|'.'
name|'get_name'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HardwareProperties
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'HardwareProperties'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""":param image_meta:  ImageMeta object\n        """'
newline|'\n'
name|'self'
op|'.'
name|'img_props'
op|'='
name|'image_meta'
op|'.'
name|'properties'
newline|'\n'
name|'os_key'
op|'='
name|'self'
op|'.'
name|'img_props'
op|'.'
name|'get'
op|'('
string|"'os_distro'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'os_info_obj'
op|'='
name|'OsInfo'
op|'('
name|'os_key'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|network_model
name|'def'
name|'network_model'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'model'
op|'='
name|'self'
op|'.'
name|'img_props'
op|'.'
name|'get'
op|'('
string|"'hw_vif_model'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'os_info_obj'
op|'.'
name|'network_model'
op|')'
newline|'\n'
name|'return'
string|"'virtio'"
name|'if'
name|'model'
op|'=='
string|"'virtio-net'"
name|'else'
name|'model'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|disk_model
name|'def'
name|'disk_model'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'model'
op|'='
name|'self'
op|'.'
name|'img_props'
op|'.'
name|'get'
op|'('
string|"'hw_disk_bus'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'os_info_obj'
op|'.'
name|'disk_model'
op|')'
newline|'\n'
name|'return'
string|"'virtio'"
name|'if'
name|'model'
op|'=='
string|"'virtio-block'"
name|'else'
name|'model'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
