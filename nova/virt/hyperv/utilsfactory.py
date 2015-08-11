begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
nl|'\n'
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
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'hostutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'hostutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'livemigrationutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'networkutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'networkutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'pathutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'rdpconsoleutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'rdpconsoleutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vhdutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeutilsv2'
newline|'\n'
nl|'\n'
DECL|variable|hyper_opts
name|'hyper_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'force_hyperv_utils_v1'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force V1 WMI utility classes'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'force_volumeutils_v1'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Force V1 volume utility class'"
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
name|'hyper_opts'
op|','
string|"'hyperv'"
op|')'
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
DECL|variable|utils
name|'utils'
op|'='
name|'hostutils'
op|'.'
name|'HostUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_class
name|'def'
name|'_get_class'
op|'('
name|'v1_class'
op|','
name|'v2_class'
op|','
name|'force_v1_flag'
op|')'
op|':'
newline|'\n'
comment|'# V2 classes are supported starting from Hyper-V Server 2012 and'
nl|'\n'
comment|'# Windows Server 2012 (kernel version 6.2)'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'force_v1_flag'
name|'and'
name|'utils'
op|'.'
name|'check_min_windows_version'
op|'('
number|'6'
op|','
number|'2'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cls'
op|'='
name|'v2_class'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'cls'
op|'='
name|'v1_class'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Loading class: %(module_name)s.%(class_name)s"'
op|','
nl|'\n'
op|'{'
string|"'module_name'"
op|':'
name|'cls'
op|'.'
name|'__module__'
op|','
string|"'class_name'"
op|':'
name|'cls'
op|'.'
name|'__name__'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'cls'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_virt_utils_class
dedent|''
name|'def'
name|'_get_virt_utils_class'
op|'('
name|'v1_class'
op|','
name|'v2_class'
op|')'
op|':'
newline|'\n'
comment|'# The "root/virtualization" WMI namespace is no longer supported on'
nl|'\n'
comment|'# Windows Server / Hyper-V Server 2012 R2 / Windows 8.1'
nl|'\n'
comment|'# (kernel version 6.3) or above.'
nl|'\n'
indent|'    '
name|'if'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'force_hyperv_utils_v1'
name|'and'
nl|'\n'
name|'utils'
op|'.'
name|'check_min_windows_version'
op|'('
number|'6'
op|','
number|'3'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'\'The "force_hyperv_utils_v1" option cannot be set to "True" \''
nl|'\n'
string|"'on Windows Server / Hyper-V Server 2012 R2 or above as the WMI '"
nl|'\n'
string|'\'"root/virtualization" namespace is no longer supported.\''
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_get_class'
op|'('
name|'v1_class'
op|','
name|'v2_class'
op|','
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'force_hyperv_utils_v1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmutils
dedent|''
name|'def'
name|'get_vmutils'
op|'('
name|'host'
op|'='
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_virt_utils_class'
op|'('
name|'vmutils'
op|'.'
name|'VMUtils'
op|','
name|'vmutilsv2'
op|'.'
name|'VMUtilsV2'
op|')'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vhdutils
dedent|''
name|'def'
name|'get_vhdutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_virt_utils_class'
op|'('
name|'vhdutils'
op|'.'
name|'VHDUtils'
op|','
name|'vhdutilsv2'
op|'.'
name|'VHDUtilsV2'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_networkutils
dedent|''
name|'def'
name|'get_networkutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_virt_utils_class'
op|'('
name|'networkutils'
op|'.'
name|'NetworkUtils'
op|','
nl|'\n'
name|'networkutilsv2'
op|'.'
name|'NetworkUtilsV2'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_hostutils
dedent|''
name|'def'
name|'get_hostutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_virt_utils_class'
op|'('
name|'hostutils'
op|'.'
name|'HostUtils'
op|','
nl|'\n'
name|'hostutilsv2'
op|'.'
name|'HostUtilsV2'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pathutils
dedent|''
name|'def'
name|'get_pathutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'pathutils'
op|'.'
name|'PathUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_volumeutils
dedent|''
name|'def'
name|'get_volumeutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_class'
op|'('
name|'volumeutils'
op|'.'
name|'VolumeUtils'
op|','
name|'volumeutilsv2'
op|'.'
name|'VolumeUtilsV2'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'force_volumeutils_v1'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_livemigrationutils
dedent|''
name|'def'
name|'get_livemigrationutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'livemigrationutils'
op|'.'
name|'LiveMigrationUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rdpconsoleutils
dedent|''
name|'def'
name|'get_rdpconsoleutils'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_get_virt_utils_class'
op|'('
name|'rdpconsoleutils'
op|'.'
name|'RDPConsoleUtils'
op|','
nl|'\n'
name|'rdpconsoleutilsv2'
op|'.'
name|'RDPConsoleUtilsV2'
op|')'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
