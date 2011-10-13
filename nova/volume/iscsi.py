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
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'iscsi_helper'"
op|','
string|"'ietadm'"
op|','
nl|'\n'
string|"'iscsi target user-land tool to use'"
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
DECL|member|new_target
dedent|''
name|'def'
name|'new_target'
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
DECL|member|delete_target
dedent|''
name|'def'
name|'delete_target'
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
DECL|member|new_logicalunit
dedent|''
name|'def'
name|'new_logicalunit'
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
DECL|member|delete_logicalunit
dedent|''
name|'def'
name|'delete_logicalunit'
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
DECL|member|new_target
dedent|''
name|'def'
name|'new_target'
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
string|"'--lld=iscsi'"
op|','
string|"'--mode=target'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--targetname=%s'"
op|'%'
name|'name'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_run'
op|'('
string|"'--op'"
op|','
string|"'bind'"
op|','
nl|'\n'
string|"'--lld=iscsi'"
op|','
string|"'--mode=target'"
op|','
nl|'\n'
string|"'--initiator-address=ALL'"
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
DECL|member|delete_target
dedent|''
name|'def'
name|'delete_target'
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
string|"'--lld=iscsi'"
op|','
string|"'--mode=target'"
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
string|"'--lld=iscsi'"
op|','
string|"'--mode=target'"
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
DECL|member|new_logicalunit
dedent|''
name|'def'
name|'new_logicalunit'
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
string|"'--lld=iscsi'"
op|','
string|"'--mode=logicalunit'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--lun=%d'"
op|'%'
op|'('
name|'lun'
op|'+'
number|'1'
op|')'
op|','
comment|'# lun0 is reserved'
nl|'\n'
string|"'--backing-store=%s'"
op|'%'
name|'path'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_logicalunit
dedent|''
name|'def'
name|'delete_logicalunit'
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
string|"'--lld=iscsi'"
op|','
string|"'--mode=logicalunit'"
op|','
nl|'\n'
string|"'--tid=%s'"
op|'%'
name|'tid'
op|','
nl|'\n'
string|"'--lun=%d'"
op|'%'
op|'('
name|'lun'
op|'+'
number|'1'
op|')'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IetAdm
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
DECL|member|new_target
dedent|''
name|'def'
name|'new_target'
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
DECL|member|delete_target
dedent|''
name|'def'
name|'delete_target'
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
DECL|member|new_logicalunit
dedent|''
name|'def'
name|'new_logicalunit'
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
DECL|member|delete_logicalunit
dedent|''
name|'def'
name|'delete_logicalunit'
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
