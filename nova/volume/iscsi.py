begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nHelper code for the iSCSI volume driver.\n\n"""'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|iscsi_helper_opt
name|'iscsi_helper_opt'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iscsi_helper'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'tgtadm'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'iscsi target user-land tool to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volumes_dir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/volumes'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Volume configuration file storage directory'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'iscsi_helper_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TargetAdmin
name|'class'
name|'TargetAdmin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""iSCSI target administration.\n\n    Base class for iSCSI target admin helpers.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'cmd'
op|','
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_cmd'
op|'='
name|'cmd'
newline|'\n'
name|'self'
op|'.'
name|'set_execute'
op|'('
name|'execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_execute
dedent|''
name|'def'
name|'set_execute'
op|'('
name|'self'
op|','
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the function to be used to execute commands."""'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'='
name|'execute'
newline|'\n'
nl|'\n'
DECL|member|_run
dedent|''
name|'def'
name|'_run'
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
name|'self'
op|'.'
name|'_execute'
op|'('
name|'self'
op|'.'
name|'_cmd'
op|','
op|'*'
name|'args'
op|','
name|'run_as_root'
op|'='
name|'True'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_iscsi_target
dedent|''
name|'def'
name|'create_iscsi_target'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a iSCSI target and logical unit"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_iscsi_target
dedent|''
name|'def'
name|'remove_iscsi_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'vol_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a iSCSI target and logical unit"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_new_target
dedent|''
name|'def'
name|'_new_target'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new iSCSI target."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_target
dedent|''
name|'def'
name|'_delete_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a target."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_target
dedent|''
name|'def'
name|'show_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'iqn'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Query the given target ID."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_new_logicalunit
dedent|''
name|'def'
name|'_new_logicalunit'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new LUN on a target using the supplied path."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_logicalunit
dedent|''
name|'def'
name|'_delete_logicalunit'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a logical unit from a target."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TgtAdm
dedent|''
dedent|''
name|'class'
name|'TgtAdm'
op|'('
name|'TargetAdmin'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""iSCSI target administration using tgtadm."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'execute'
op|'='
name|'utils'
op|'.'
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TgtAdm'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|"'tgtadm'"
op|','
name|'execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_target
dedent|''
name|'def'
name|'_get_target'
op|'('
name|'self'
op|','
name|'iqn'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
string|"'tgt-admin'"
op|','
string|"'--show'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'lines'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'iqn'
name|'in'
name|'line'
op|':'
newline|'\n'
indent|'                '
name|'parsed'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'tid'
op|'='
name|'parsed'
op|'['
number|'1'
op|']'
newline|'\n'
name|'return'
name|'tid'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|create_iscsi_target
dedent|''
name|'def'
name|'create_iscsi_target'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# Note(jdg) tid and lun aren't used by TgtAdm but remain for"
nl|'\n'
comment|'# compatibility'
nl|'\n'
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'ensure_tree'
op|'('
name|'FLAGS'
op|'.'
name|'volumes_dir'
op|')'
newline|'\n'
nl|'\n'
name|'vol_id'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'volume_conf'
op|'='
string|'"""\n            <target %s>\n                backing-store %s\n            </target>\n        """'
op|'%'
op|'('
name|'name'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Creating volume: %s'"
op|')'
op|'%'
name|'vol_id'
op|')'
newline|'\n'
name|'volumes_dir'
op|'='
name|'FLAGS'
op|'.'
name|'volumes_dir'
newline|'\n'
name|'volume_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'volumes_dir'
op|','
name|'vol_id'
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'volume_path'
op|','
string|"'w+'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'volume_conf'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
string|"'tgt-admin'"
op|','
nl|'\n'
string|"'--update'"
op|','
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to create iscsi target for volume "'
nl|'\n'
string|'"id:%(vol_id)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"#Don't forget to remove the persistent file we created"
nl|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'volume_path'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ISCSITargetCreateFailed'
op|'('
name|'volume_id'
op|'='
name|'vol_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'iqn'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iscsi_target_prefix'
op|','
name|'vol_id'
op|')'
newline|'\n'
name|'tid'
op|'='
name|'self'
op|'.'
name|'_get_target'
op|'('
name|'iqn'
op|')'
newline|'\n'
name|'if'
name|'tid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to create iscsi target for volume "'
nl|'\n'
string|'"id:%(vol_id)s. Please ensure your tgtd config file "'
nl|'\n'
string|'"contains \'include %(volumes_dir)s/*\'"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'tid'
newline|'\n'
nl|'\n'
DECL|member|remove_iscsi_target
dedent|''
name|'def'
name|'remove_iscsi_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'vol_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Removing volume: %s'"
op|')'
op|'%'
name|'vol_id'
op|')'
newline|'\n'
name|'vol_uuid_file'
op|'='
string|"'volume-%s'"
op|'%'
name|'vol_id'
newline|'\n'
name|'volume_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'volumes_dir'
op|','
name|'vol_uuid_file'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'volume_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'iqn'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iscsi_target_prefix'
op|','
nl|'\n'
name|'vol_uuid_file'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ISCSITargetRemoveFailed'
op|'('
name|'volume_id'
op|'='
name|'vol_id'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_execute'
op|'('
string|"'tgt-admin'"
op|','
nl|'\n'
string|"'--delete'"
op|','
nl|'\n'
name|'iqn'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to create iscsi target for volume "'
nl|'\n'
string|'"id:%(volume_id)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ISCSITargetRemoveFailed'
op|'('
name|'volume_id'
op|'='
name|'vol_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'unlink'
op|'('
name|'volume_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_target
dedent|''
name|'def'
name|'show_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'iqn'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'iqn'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidParameterValue'
op|'('
nl|'\n'
name|'err'
op|'='
name|'_'
op|'('
string|"'valid iqn needed for show_target'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'tid'
op|'='
name|'self'
op|'.'
name|'_get_target'
op|'('
name|'iqn'
op|')'
newline|'\n'
name|'if'
name|'tid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IetAdm
dedent|''
dedent|''
dedent|''
name|'class'
name|'IetAdm'
op|'('
name|'TargetAdmin'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""iSCSI target administration using ietadm."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'execute'
op|'='
name|'utils'
op|'.'
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IetAdm'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|"'ietadm'"
op|','
name|'execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_iscsi_target
dedent|''
name|'def'
name|'create_iscsi_target'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_new_target'
op|'('
name|'name'
op|','
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_new_logicalunit'
op|'('
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'tid'
newline|'\n'
nl|'\n'
DECL|member|remove_iscsi_target
dedent|''
name|'def'
name|'remove_iscsi_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'vol_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Removing volume: %s'"
op|')'
op|'%'
name|'vol_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_delete_logicalunit'
op|'('
name|'tid'
op|','
name|'lun'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_delete_target'
op|'('
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_new_target
dedent|''
name|'def'
name|'_new_target'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'new'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--params'"
op|','
string|"'Name=%s'"
op|'%'
name|'name'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_target
dedent|''
name|'def'
name|'_delete_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'delete'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_target
dedent|''
name|'def'
name|'show_target'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'iqn'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'show'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_new_logicalunit
dedent|''
name|'def'
name|'_new_logicalunit'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
name|'path'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'new'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--lun=%d'"
op|'%'
name|'lun'
op|','
nl|'\n'
string|"'--params'"
op|','
string|"'Path=%s,Type=fileio'"
op|'%'
name|'path'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_logicalunit
dedent|''
name|'def'
name|'_delete_logicalunit'
op|'('
name|'self'
op|','
name|'tid'
op|','
name|'lun'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'delete'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--lun=%d'"
op|'%'
name|'lun'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_target_admin
dedent|''
dedent|''
name|'def'
name|'get_target_admin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'iscsi_helper'
op|'=='
string|"'tgtadm'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'TgtAdm'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'IetAdm'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
