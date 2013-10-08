begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2012 Pedro Navarro Perez'
nl|'\n'
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
string|'"""\nHelper methods for operations related to the management of volumes,\nand storage repositories\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
op|'.'
name|'hyperv'
name|'import'
name|'basevolumeutils'
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
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeUtils
name|'class'
name|'VolumeUtils'
op|'('
name|'basevolumeutils'
op|'.'
name|'BaseVolumeUtils'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VolumeUtils'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|execute
dedent|''
name|'def'
name|'execute'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stdout_value'
op|','
name|'stderr_value'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'stdout_value'
op|'.'
name|'find'
op|'('
string|"'The operation completed successfully'"
op|')'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
name|'_'
op|'('
string|"'An error has occurred when '"
nl|'\n'
string|"'calling the iscsi initiator: %s'"
op|')'
nl|'\n'
op|'%'
name|'stdout_value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|login_storage_target
dedent|''
dedent|''
name|'def'
name|'login_storage_target'
op|'('
name|'self'
op|','
name|'target_lun'
op|','
name|'target_iqn'
op|','
name|'target_portal'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add target portal, list targets and logins to the target."""'
newline|'\n'
op|'('
name|'target_address'
op|','
nl|'\n'
name|'target_port'
op|')'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
name|'target_portal'
op|')'
newline|'\n'
nl|'\n'
comment|'#Adding target portal to iscsi initiator. Sending targets'
nl|'\n'
name|'self'
op|'.'
name|'execute'
op|'('
string|"'iscsicli.exe '"
op|'+'
string|"'AddTargetPortal '"
op|'+'
nl|'\n'
name|'target_address'
op|'+'
string|"' '"
op|'+'
name|'target_port'
op|'+'
nl|'\n'
string|"' * * * * * * * * * * * * *'"
op|')'
newline|'\n'
comment|'#Listing targets'
nl|'\n'
name|'self'
op|'.'
name|'execute'
op|'('
string|"'iscsicli.exe '"
op|'+'
string|"'ListTargets'"
op|')'
newline|'\n'
comment|'#Sending login'
nl|'\n'
name|'self'
op|'.'
name|'execute'
op|'('
string|"'iscsicli.exe '"
op|'+'
string|"'qlogintarget '"
op|'+'
name|'target_iqn'
op|')'
newline|'\n'
comment|'#Waiting the disk to be mounted.'
nl|'\n'
comment|'#TODO(pnavarro): Check for the operation to end instead of'
nl|'\n'
comment|'#relying on a timeout'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'volume_attach_retry_interval'
op|')'
newline|'\n'
nl|'\n'
DECL|member|logout_storage_target
dedent|''
name|'def'
name|'logout_storage_target'
op|'('
name|'self'
op|','
name|'target_iqn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Logs out storage target through its session id."""'
newline|'\n'
nl|'\n'
name|'sessions'
op|'='
name|'self'
op|'.'
name|'_conn_wmi'
op|'.'
name|'query'
op|'('
string|'"SELECT * FROM "'
nl|'\n'
string|'"MSiSCSIInitiator_SessionClass "'
nl|'\n'
string|'"WHERE TargetName=\'%s\'"'
op|'%'
name|'target_iqn'
op|')'
newline|'\n'
name|'for'
name|'session'
name|'in'
name|'sessions'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'execute_log_out'
op|'('
name|'session'
op|'.'
name|'SessionId'
op|')'
newline|'\n'
nl|'\n'
DECL|member|execute_log_out
dedent|''
dedent|''
name|'def'
name|'execute_log_out'
op|'('
name|'self'
op|','
name|'session_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Executes log out of the session described by its session ID."""'
newline|'\n'
name|'self'
op|'.'
name|'execute'
op|'('
string|"'iscsicli.exe '"
op|'+'
string|"'logouttarget '"
op|'+'
name|'session_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
