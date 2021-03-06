begin_unit
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
comment|"# NOTE: XenServer still only supports Python 2.4 in it's dom0 userspace"
nl|'\n'
comment|'# which means the Nova xenapi plugins must use only Python 2.4 features'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Helper functions for the Nova xapi plugins.  In time, this will merge'
nl|'\n'
comment|'# with the pluginlib.py shipped with xapi, but for now, that file is not'
nl|'\n'
comment|"# very stable, so it's easiest just to have a copy of all the functions"
nl|'\n'
comment|'# that we need.'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'XenAPI'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|translations
name|'translations'
op|'='
name|'gettext'
op|'.'
name|'translation'
op|'('
string|"'nova'"
op|','
name|'fallback'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|variable|_
name|'_'
op|'='
name|'translations'
op|'.'
name|'ugettext'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Logging setup'
nl|'\n'
nl|'\n'
DECL|function|configure_logging
name|'def'
name|'configure_logging'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'sysh'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'('
string|"'/dev/log'"
op|')'
newline|'\n'
name|'sysh'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'formatter'
op|'='
name|'logging'
op|'.'
name|'Formatter'
op|'('
string|"'%s: %%(levelname)-8s %%(message)s'"
op|'%'
name|'name'
op|')'
newline|'\n'
name|'sysh'
op|'.'
name|'setFormatter'
op|'('
name|'formatter'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'addHandler'
op|'('
name|'sysh'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Exceptions'
nl|'\n'
nl|'\n'
DECL|class|PluginError
dedent|''
name|'class'
name|'PluginError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Exception class for all plugin errors."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ArgumentError
dedent|''
dedent|''
name|'class'
name|'ArgumentError'
op|'('
name|'PluginError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when required arguments are missing, argument values are invalid,\n    or incompatible arguments are given.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'PluginError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Argument validation'
nl|'\n'
nl|'\n'
DECL|function|exists
dedent|''
dedent|''
name|'def'
name|'exists'
op|'('
name|'args'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validates that a freeform string argument to a RPC method call is given.\n    Returns the string.\n    """'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'args'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'ArgumentError'
op|'('
name|'_'
op|'('
string|"'Argument %s is required.'"
op|')'
op|'%'
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|optional
dedent|''
dedent|''
name|'def'
name|'optional'
op|'('
name|'args'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""If the given key is in args, return the corresponding value, otherwise\n    return None\n    """'
newline|'\n'
name|'return'
name|'key'
name|'in'
name|'args'
name|'and'
name|'args'
op|'['
name|'key'
op|']'
name|'or'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_domain_0
dedent|''
name|'def'
name|'_get_domain_0'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'this_host_ref'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'session'
op|'.'
name|'handle'
op|')'
newline|'\n'
name|'expr'
op|'='
string|'\'field "is_control_domain" = "true" and field "resident_on" = "%s"\''
newline|'\n'
name|'expr'
op|'='
name|'expr'
op|'%'
name|'this_host_ref'
newline|'\n'
name|'return'
name|'list'
op|'('
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_all_records_where'
op|'('
name|'expr'
op|')'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|with_vdi_in_dom0
dedent|''
name|'def'
name|'with_vdi_in_dom0'
op|'('
name|'session'
op|','
name|'vdi'
op|','
name|'read_only'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dom0'
op|'='
name|'_get_domain_0'
op|'('
name|'session'
op|')'
newline|'\n'
name|'vbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'dom0'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VDI'"
op|']'
op|'='
name|'vdi'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'='
string|"'autodetect'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'bootable'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'mode'"
op|']'
op|'='
name|'read_only'
name|'and'
string|"'RO'"
name|'or'
string|"'RW'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'type'"
op|']'
op|'='
string|"'disk'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'unpluggable'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'empty'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_supported_algorithms'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VDI %s ... '"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'vbd'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'create'
op|'('
name|'vbd_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VDI %s done.'"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Plugging VBD %s ... '"
op|')'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'plug'
op|'('
name|'vbd'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Plugging VBD %s done.'"
op|')'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'return'
name|'f'
op|'('
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'get_device'
op|'('
name|'vbd'
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Destroying VBD for VDI %s ... '"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
name|'_vbd_unplug_with_retry'
op|'('
name|'session'
op|','
name|'vbd'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'destroy'
op|'('
name|'vbd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
comment|'# noqa'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Ignoring XenAPI.Failure %s'"
op|')'
op|','
name|'e'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Destroying VBD for VDI %s done.'"
op|')'
op|','
name|'vdi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_vbd_unplug_with_retry
dedent|''
dedent|''
name|'def'
name|'_vbd_unplug_with_retry'
op|'('
name|'session'
op|','
name|'vbd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Call VBD.unplug on the given VBD, with a retry if we get\n    DEVICE_DETACH_REJECTED.  For reasons which I don\'t understand, we\'re\n    seeing the device still in use, even when all processes using the device\n    should be dead.\n    """'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'unplug'
op|'('
name|'vbd'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug successful first time.'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
comment|'# noqa'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'len'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|'>'
number|'0'
name|'and'
nl|'\n'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'DEVICE_DETACH_REJECTED'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug rejected: retrying...'"
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'len'
op|'('
name|'e'
op|'.'
name|'details'
op|')'
op|'>'
number|'0'
name|'and'
nl|'\n'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'DEVICE_ALREADY_DETACHED'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'VBD.unplug successful eventually.'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Ignoring XenAPI.Failure in VBD.unplug: %s'"
op|')'
op|','
nl|'\n'
name|'e'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
