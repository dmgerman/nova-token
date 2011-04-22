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
nl|'\n'
string|'"""Nova base exception handling.\n\nIncludes decorator for re-raising Nova-type exceptions.\n\nSHOULD include dedicated exception logging.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.exception'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
name|'class'
name|'ProcessExecutionError'
op|'('
name|'IOError'
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
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'exit_code'
op|'='
name|'None'
op|','
name|'cmd'
op|'='
name|'None'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
name|'_'
op|'('
string|"'Unexpected error while running command.'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exit_code'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'exit_code'
op|'='
string|"'-'"
newline|'\n'
dedent|''
name|'message'
op|'='
name|'_'
op|'('
string|"'%(description)s\\nCommand: %(cmd)s\\n'"
nl|'\n'
string|"'Exit code: %(exit_code)s\\nStdout: %(stdout)r\\n'"
nl|'\n'
string|"'Stderr: %(stderr)r'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'IOError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Error
dedent|''
dedent|''
name|'class'
name|'Error'
op|'('
name|'Exception'
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
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Error'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiError
dedent|''
dedent|''
name|'class'
name|'ApiError'
op|'('
name|'Error'
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
name|'message'
op|'='
string|"'Unknown'"
op|','
name|'code'
op|'='
string|"'ApiError'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'message'
op|'='
name|'message'
newline|'\n'
name|'self'
op|'.'
name|'code'
op|'='
name|'code'
newline|'\n'
name|'super'
op|'('
name|'ApiError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|"'%s: %s'"
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotFound
dedent|''
dedent|''
name|'class'
name|'NotFound'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotFound
dedent|''
name|'class'
name|'InstanceNotFound'
op|'('
name|'NotFound'
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
name|'message'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'instance_id'
newline|'\n'
name|'super'
op|'('
name|'InstanceNotFound'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeNotFound
dedent|''
dedent|''
name|'class'
name|'VolumeNotFound'
op|'('
name|'NotFound'
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
name|'message'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'volume_id'
op|'='
name|'volume_id'
newline|'\n'
name|'super'
op|'('
name|'VolumeNotFound'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotAuthorized
dedent|''
dedent|''
name|'class'
name|'NotAuthorized'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotEmpty
dedent|''
name|'class'
name|'NotEmpty'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidInputException
dedent|''
name|'class'
name|'InvalidInputException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidContentType
dedent|''
name|'class'
name|'InvalidContentType'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TimeoutException
dedent|''
name|'class'
name|'TimeoutException'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DBError
dedent|''
name|'class'
name|'DBError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps an implementation specific exception."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'inner_exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inner_exception'
op|'='
name|'inner_exception'
newline|'\n'
name|'super'
op|'('
name|'DBError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'str'
op|'('
name|'inner_exception'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_db_error
dedent|''
dedent|''
name|'def'
name|'wrap_db_error'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'DB exception wrapped.'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'DBError'
op|'('
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_wrap'
newline|'\n'
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_exception
dedent|''
name|'def'
name|'wrap_exception'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|_wrap
indent|'    '
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'e'
op|','
name|'Error'
op|')'
op|':'
newline|'\n'
comment|'#exc_type, exc_value, exc_traceback = sys.exc_info()'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Uncaught exception'"
op|')'
op|')'
newline|'\n'
comment|'#logging.error(traceback.extract_stack(exc_traceback))'
nl|'\n'
name|'raise'
name|'Error'
op|'('
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'_wrap'
op|'.'
name|'func_name'
op|'='
name|'f'
op|'.'
name|'func_name'
newline|'\n'
name|'return'
name|'_wrap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaException
dedent|''
name|'class'
name|'NovaException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base Nova Exception\n\n    To correctly use this class, inherit from it and define\n    a \'message\' property. That message will get printf\'d\n    with the keyword arguments provided to the constructor.\n\n    """'
newline|'\n'
DECL|variable|message
name|'message'
op|'='
name|'_'
op|'('
string|'"An unknown exception occurred."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error_string'
op|'='
name|'self'
op|'.'
name|'message'
op|'%'
name|'kwargs'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|'# at least get the core message out if something happened'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_error_string'
op|'='
name|'self'
op|'.'
name|'message'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_error_string'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): EOL this exception!'
nl|'\n'
DECL|class|Invalid
dedent|''
dedent|''
name|'class'
name|'Invalid'
op|'('
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotRunning
dedent|''
name|'class'
name|'InstanceNotRunning'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is not running."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceNotSuspended
dedent|''
name|'class'
name|'InstanceNotSuspended'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(instance_id)s is not suspended."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceSuspendFailure
dedent|''
name|'class'
name|'InstanceSuspendFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to suspend instance"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceResumeFailure
dedent|''
name|'class'
name|'InstanceResumeFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to resume server"'
op|')'
op|'+'
string|'": %(reason)s."'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceRebootFailure
dedent|''
name|'class'
name|'InstanceRebootFailure'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Failed to reboot instance"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceUnavailable
dedent|''
name|'class'
name|'ServiceUnavailable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeServiceUnavailable
dedent|''
name|'class'
name|'VolumeServiceUnavailable'
op|'('
name|'ServiceUnavailable'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Volume service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeServiceUnavailable
dedent|''
name|'class'
name|'ComputeServiceUnavailable'
op|'('
name|'ServiceUnavailable'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Compute service is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnableToMigrateToSelf
dedent|''
name|'class'
name|'UnableToMigrateToSelf'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unable to migrate instance (%(instance_id)s) "'
nl|'\n'
string|'"to current host (%(host)s)."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SourceHostUnavailable
dedent|''
name|'class'
name|'SourceHostUnavailable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Original compute host is unavailable at this time."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidHypervisorType
dedent|''
name|'class'
name|'InvalidHypervisorType'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The supplied hypervisor type of is invalid."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DestinationHypervisorTooOld
dedent|''
name|'class'
name|'DestinationHypervisorTooOld'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The instance requires a newer hypervisor version than "'
nl|'\n'
string|'"has been provided."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidDevicePath
dedent|''
name|'class'
name|'InvalidDevicePath'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"The supplied device path (%(path)s) is invalid."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidCPUInfo
dedent|''
name|'class'
name|'InvalidCPUInfo'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unacceptable CPU info"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidVLANTag
dedent|''
name|'class'
name|'InvalidVLANTag'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"VLAN tag is not appropriate for the port group "'
nl|'\n'
string|'"%(bridge)s. Expected VLAN tag is %(tag)s, "'
nl|'\n'
string|'"but the one associated with the port group is %(pgroup)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidVLANPortGroup
dedent|''
name|'class'
name|'InvalidVLANPortGroup'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"vSwitch which contains the port group %(bridge)s is "'
nl|'\n'
string|'"not associated with the desired physical adapter. "'
nl|'\n'
string|'"Expected vSwitch is %(expected)s, but the one associated "'
nl|'\n'
string|'"is %(actual)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageUnacceptable
dedent|''
name|'class'
name|'ImageUnacceptable'
op|'('
name|'Invalid'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Image %(image_id)s is unacceptable"'
op|')'
op|'+'
string|'": %(reason)s"'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): EOL this exception!'
nl|'\n'
DECL|class|Duplicate
dedent|''
name|'class'
name|'Duplicate'
op|'('
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairExists
dedent|''
name|'class'
name|'KeyPairExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Key pair %(key_name)s already exists."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UserExists
dedent|''
name|'class'
name|'UserExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"User %(user)s already exists."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPUserExists
dedent|''
name|'class'
name|'LDAPUserExists'
op|'('
name|'UserExists'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP user %(user)s already exists."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPGroupExists
dedent|''
name|'class'
name|'LDAPGroupExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"LDAP group %(group)s already exists."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LDAPMembershipExists
dedent|''
name|'class'
name|'LDAPMembershipExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"User %(uid)s is already a member of "'
nl|'\n'
string|'"the group %(group_dn)s"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProjectExists
dedent|''
name|'class'
name|'ProjectExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Project %(project)s already exists."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceExists
dedent|''
name|'class'
name|'InstanceExists'
op|'('
name|'Duplicate'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Instance %(name)s already exists."'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
