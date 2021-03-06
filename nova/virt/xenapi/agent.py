begin_unit
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010-2012 OpenStack Foundation'
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
name|'base64'
newline|'\n'
name|'import'
name|'binascii'
newline|'\n'
name|'from'
name|'distutils'
name|'import'
name|'version'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'password'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
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
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|USE_AGENT_KEY
name|'USE_AGENT_KEY'
op|'='
string|'"xenapi_use_agent"'
newline|'\n'
DECL|variable|USE_AGENT_SM_KEY
name|'USE_AGENT_SM_KEY'
op|'='
name|'utils'
op|'.'
name|'SM_IMAGE_PROP_PREFIX'
op|'+'
name|'USE_AGENT_KEY'
newline|'\n'
DECL|variable|SKIP_SSH_KEY
name|'SKIP_SSH_KEY'
op|'='
string|'"xenapi_skip_agent_inject_ssh"'
newline|'\n'
DECL|variable|SKIP_SSH_SM_KEY
name|'SKIP_SSH_SM_KEY'
op|'='
name|'utils'
op|'.'
name|'SM_IMAGE_PROP_PREFIX'
op|'+'
name|'SKIP_SSH_KEY'
newline|'\n'
DECL|variable|SKIP_FILES_AT_BOOT_KEY
name|'SKIP_FILES_AT_BOOT_KEY'
op|'='
string|'"xenapi_skip_agent_inject_files_at_boot"'
newline|'\n'
name|'SKIP_FILES_AT_BOOT_SM_KEY'
op|'='
name|'utils'
op|'.'
name|'SM_IMAGE_PROP_PREFIX'
DECL|variable|SKIP_FILES_AT_BOOT_SM_KEY
op|'+'
name|'SKIP_FILES_AT_BOOT_KEY'
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
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_call_agent
name|'def'
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'method'
op|','
name|'addl_args'
op|'='
name|'None'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'None'
op|','
name|'success_codes'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts out the interaction with the agent xenapi plugin."""'
newline|'\n'
name|'if'
name|'addl_args'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'addl_args'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'timeout'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'agent_timeout'
newline|'\n'
dedent|''
name|'if'
name|'success_codes'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'success_codes'
op|'='
op|'['
string|"'0'"
op|']'
newline|'\n'
nl|'\n'
comment|'# always fetch domid because VM may have rebooted'
nl|'\n'
dedent|''
name|'dom_id'
op|'='
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'dom_id'"
op|':'
name|'str'
op|'('
name|'dom_id'
op|')'
op|','
nl|'\n'
string|"'timeout'"
op|':'
name|'str'
op|'('
name|'timeout'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'args'
op|'.'
name|'update'
op|'('
name|'addl_args'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
name|'session'
op|'.'
name|'call_plugin'
op|'('
string|"'agent'"
op|','
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'err_msg'
op|'='
name|'e'
op|'.'
name|'details'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'splitlines'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
string|"'TIMEOUT:'"
name|'in'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'TIMEOUT: The call to %(method)s timed out. '"
nl|'\n'
string|"'args=%(args)r'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentTimeout'
op|'('
name|'method'
op|'='
name|'method'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'REBOOT:'"
name|'in'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'REBOOT: The call to %(method)s detected a reboot. '"
nl|'\n'
string|"'args=%(args)r'"
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'_wait_for_new_dom_id'
op|'('
name|'session'
op|','
name|'vm_ref'
op|','
name|'dom_id'
op|','
name|'method'
op|')'
newline|'\n'
name|'return'
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'method'
op|','
nl|'\n'
name|'addl_args'
op|','
name|'timeout'
op|','
name|'success_codes'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'NOT IMPLEMENTED:'"
name|'in'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'NOT IMPLEMENTED: The call to %(method)s is not '"
nl|'\n'
string|"'supported by the agent. args=%(args)r'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentNotImplemented'
op|'('
name|'method'
op|'='
name|'method'
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
name|'_LE'
op|'('
string|"'The call to %(method)s returned an error: %(e)s. '"
nl|'\n'
string|"'args=%(args)r'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'args'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentError'
op|'('
name|'method'
op|'='
name|'method'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'ret'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'The agent call to %(method)s returned an invalid '"
nl|'\n'
string|"'response: %(ret)r. args=%(args)r'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'ret'"
op|':'
name|'ret'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentError'
op|'('
name|'method'
op|'='
name|'method'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ret'
op|'['
string|"'returncode'"
op|']'
name|'not'
name|'in'
name|'success_codes'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'The agent call to %(method)s returned '"
nl|'\n'
string|"'an error: %(ret)r. args=%(args)r'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'ret'"
op|':'
name|'ret'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentError'
op|'('
name|'method'
op|'='
name|'method'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'The agent call to %(method)s was successful: '"
nl|'\n'
string|"'%(ret)r. args=%(args)r'"
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'ret'"
op|':'
name|'ret'
op|','
string|"'args'"
op|':'
name|'args'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# Some old versions of the Windows agent have a trailing \\\\r\\\\n'
nl|'\n'
comment|'# (ie CRLF escaped) for some reason. Strip that off.'
nl|'\n'
name|'return'
name|'ret'
op|'['
string|"'message'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'\\\\r\\\\n'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_wait_for_new_dom_id
dedent|''
name|'def'
name|'_wait_for_new_dom_id'
op|'('
name|'session'
op|','
name|'vm_ref'
op|','
name|'old_dom_id'
op|','
name|'method'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'expiration'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'agent_timeout'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'dom_id'
op|'='
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'dom_id'
name|'and'
name|'dom_id'
op|'!='
op|'-'
number|'1'
name|'and'
name|'dom_id'
op|'!='
name|'old_dom_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Found new dom_id %s"'
op|','
name|'dom_id'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'>'
name|'expiration'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Timed out waiting for new dom_id %s"'
op|','
name|'dom_id'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'AgentTimeout'
op|'('
name|'method'
op|'='
name|'method'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_upgrade_required
dedent|''
dedent|''
name|'def'
name|'is_upgrade_required'
op|'('
name|'current_version'
op|','
name|'available_version'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(johngarbutt): agent version numbers are four part,'
nl|'\n'
comment|'# so we need to use the loose version to compare them'
nl|'\n'
indent|'    '
name|'current'
op|'='
name|'version'
op|'.'
name|'LooseVersion'
op|'('
name|'current_version'
op|')'
newline|'\n'
name|'available'
op|'='
name|'version'
op|'.'
name|'LooseVersion'
op|'('
name|'available_version'
op|')'
newline|'\n'
name|'return'
name|'available'
op|'>'
name|'current'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIBasedAgent
dedent|''
name|'class'
name|'XenAPIBasedAgent'
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
name|'session'
op|','
name|'virtapi'
op|','
name|'instance'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
newline|'\n'
name|'self'
op|'.'
name|'virtapi'
op|'='
name|'virtapi'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'vm_ref'
op|'='
name|'vm_ref'
newline|'\n'
nl|'\n'
DECL|member|_add_instance_fault
dedent|''
name|'def'
name|'_add_instance_fault'
op|'('
name|'self'
op|','
name|'error'
op|','
name|'exc_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Ignoring error while configuring instance with "'
nl|'\n'
string|'"agent: %s"'
op|')'
op|','
name|'error'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'error'
op|','
name|'exc_info'
op|'='
name|'exc_info'
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
name|'debug'
op|'('
string|'"Error setting instance fault."'
op|','
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_call_agent
dedent|''
dedent|''
name|'def'
name|'_call_agent'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'addl_args'
op|'='
name|'None'
op|','
name|'timeout'
op|'='
name|'None'
op|','
nl|'\n'
name|'success_codes'
op|'='
name|'None'
op|','
name|'ignore_errors'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_call_agent'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|','
nl|'\n'
name|'method'
op|','
name|'addl_args'
op|','
name|'timeout'
op|','
name|'success_codes'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ignore_errors'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_add_instance_fault'
op|'('
name|'error'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|get_version
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Querying agent version'"
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# The agent can be slow to start for a variety of reasons. On Windows,'
nl|'\n'
comment|'# it will generally perform a setup process on first boot that can'
nl|'\n'
comment|'# take a couple of minutes and then reboot. On Linux, the system can'
nl|'\n'
comment|'# also take a while to boot.'
nl|'\n'
name|'expiration'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'agent_version_timeout'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|"# NOTE(johngarbutt): we can't use the xapi plugin"
nl|'\n'
comment|'# timeout, because the domid may change when'
nl|'\n'
comment|'# the server is rebooted'
nl|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'version'"
op|','
name|'ignore_errors'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'>'
name|'expiration'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_add_instance_fault'
op|'('
name|'error'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|_get_expected_build
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_expected_build'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'agent_build'
op|'='
name|'objects'
op|'.'
name|'Agent'
op|'.'
name|'get_by_triple'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'xen'"
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'os_type'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'architecture'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'agent_build'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Latest agent build for %(hypervisor)s/%(os)s'"
nl|'\n'
string|"'/%(architecture)s is %(version)s'"
op|','
op|'{'
nl|'\n'
string|"'hypervisor'"
op|':'
name|'agent_build'
op|'.'
name|'hypervisor'
op|','
nl|'\n'
string|"'os'"
op|':'
name|'agent_build'
op|'.'
name|'os'
op|','
nl|'\n'
string|"'architecture'"
op|':'
name|'agent_build'
op|'.'
name|'architecture'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'agent_build'
op|'.'
name|'version'
op|'}'
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
string|"'No agent build found for %(hypervisor)s/%(os)s'"
nl|'\n'
string|"'/%(architecture)s'"
op|','
op|'{'
nl|'\n'
string|"'hypervisor'"
op|':'
string|"'xen'"
op|','
nl|'\n'
string|"'os'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'os_type'"
op|']'
op|','
nl|'\n'
string|"'architecture'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'architecture'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'agent_build'
newline|'\n'
nl|'\n'
DECL|member|update_if_needed
dedent|''
name|'def'
name|'update_if_needed'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent_build'
op|'='
name|'self'
op|'.'
name|'_get_expected_build'
op|'('
op|')'
newline|'\n'
name|'if'
name|'version'
name|'and'
name|'agent_build'
name|'and'
name|'is_upgrade_required'
op|'('
name|'version'
op|','
name|'agent_build'
op|'.'
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Updating agent to %s'"
op|','
name|'agent_build'
op|'.'
name|'version'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_perform_update'
op|'('
name|'agent_build'
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
string|"'Skipping agent update.'"
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_perform_update
dedent|''
dedent|''
name|'def'
name|'_perform_update'
op|'('
name|'self'
op|','
name|'agent_build'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'{'
string|"'url'"
op|':'
name|'agent_build'
op|'.'
name|'url'
op|','
string|"'md5sum'"
op|':'
name|'agent_build'
op|'.'
name|'md5hash'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'agentupdate'"
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentError'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# Silently fail for agent upgrades'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Unable to update the agent due "'
nl|'\n'
string|'"to: %(exc)s"'
op|')'
op|','
name|'dict'
op|'('
name|'exc'
op|'='
name|'exc'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_exchange_key_with_agent
dedent|''
dedent|''
name|'def'
name|'_exchange_key_with_agent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dh'
op|'='
name|'SimpleDH'
op|'('
op|')'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'pub'"
op|':'
name|'str'
op|'('
name|'dh'
op|'.'
name|'get_public'
op|'('
op|')'
op|')'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'key_init'"
op|','
name|'args'
op|','
name|'success_codes'
op|'='
op|'['
string|"'D0'"
op|']'
op|','
nl|'\n'
name|'ignore_errors'
op|'='
name|'False'
op|')'
newline|'\n'
name|'agent_pub'
op|'='
name|'int'
op|'('
name|'resp'
op|')'
newline|'\n'
name|'dh'
op|'.'
name|'compute_shared'
op|'('
name|'agent_pub'
op|')'
newline|'\n'
name|'return'
name|'dh'
newline|'\n'
nl|'\n'
DECL|member|_save_instance_password_if_sshkey_present
dedent|''
name|'def'
name|'_save_instance_password_if_sshkey_present'
op|'('
name|'self'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sshkey'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'key_data'"
op|')'
newline|'\n'
name|'if'
name|'sshkey'
name|'and'
name|'sshkey'
op|'.'
name|'startswith'
op|'('
string|'"ssh-rsa"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'enc'
op|'='
name|'crypto'
op|'.'
name|'ssh_encrypt_text'
op|'('
name|'sshkey'
op|','
name|'new_pass'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'system_metadata'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'password'
op|'.'
name|'convert_password'
op|'('
name|'ctxt'
op|','
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'enc'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the root/admin password on the VM instance.\n\n        This is done via an agent running on the VM. Communication between nova\n        and the agent is done via writing xenstore records. Since communication\n        is done over the XenAPI RPC calls, we need to encrypt the password.\n        We\'re using a simple Diffie-Hellman class instead of a more advanced\n        library (such as M2Crypto) for compatibility with the agent code.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Setting admin password'"
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'dh'
op|'='
name|'self'
op|'.'
name|'_exchange_key_with_agent'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AgentError'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_instance_fault'
op|'('
name|'error'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# Some old versions of Linux and Windows agent expect trailing \\n'
nl|'\n'
comment|'# on password to work correctly.'
nl|'\n'
dedent|''
name|'enc_pass'
op|'='
name|'dh'
op|'.'
name|'encrypt'
op|'('
name|'new_pass'
op|'+'
string|"'\\n'"
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'enc_pass'"
op|':'
name|'enc_pass'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'password'"
op|','
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_save_instance_password_if_sshkey_present'
op|'('
name|'new_pass'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_ssh_key
dedent|''
name|'def'
name|'inject_ssh_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sshkey'
op|'='
name|'self'
op|'.'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'key_data'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'sshkey'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'os_type'"
op|']'
op|'=='
string|"'windows'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Skipping setting of ssh key for Windows."'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_skip_ssh_key_inject'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Skipping agent ssh key injection for this image."'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'sshkey'
op|'='
name|'str'
op|'('
name|'sshkey'
op|')'
newline|'\n'
name|'keyfile'
op|'='
string|"'/root/.ssh/authorized_keys'"
newline|'\n'
name|'key_data'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
string|"'# The following ssh key was injected by Nova'"
op|','
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
name|'sshkey'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'inject_file'
op|'('
name|'keyfile'
op|','
name|'key_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_files
dedent|''
name|'def'
name|'inject_files'
op|'('
name|'self'
op|','
name|'injected_files'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_skip_inject_files_at_boot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Skipping agent file injection for this image."'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'path'
op|','
name|'contents'
name|'in'
name|'injected_files'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'inject_file'
op|'('
name|'path'
op|','
name|'contents'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inject_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'inject_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'contents'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Injecting file path: %r'"
op|','
name|'path'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# Files/paths must be base64-encoded for transmission to agent'
nl|'\n'
name|'b64_path'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'path'
op|')'
newline|'\n'
name|'b64_contents'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'contents'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'{'
string|"'b64_path'"
op|':'
name|'b64_path'
op|','
string|"'b64_contents'"
op|':'
name|'b64_contents'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'inject_file'"
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resetnetwork
dedent|''
name|'def'
name|'resetnetwork'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Resetting network'"
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(johngarbutt) old FreeBSD and Gentoo agents return 500 on success'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_call_agent'
op|'('
string|"'resetnetwork'"
op|','
nl|'\n'
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'agent_resetnetwork_timeout'
op|','
nl|'\n'
name|'success_codes'
op|'='
op|'['
string|"'0'"
op|','
string|"'500'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_skip_ssh_key_inject
dedent|''
name|'def'
name|'_skip_ssh_key_inject'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'SKIP_SSH_SM_KEY'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_skip_inject_files_at_boot
dedent|''
name|'def'
name|'_skip_inject_files_at_boot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'SKIP_FILES_AT_BOOT_SM_KEY'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_sys_meta_key
dedent|''
name|'def'
name|'_get_sys_meta_key'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'raw_value'
op|'='
name|'sys_meta'
op|'.'
name|'get'
op|'('
name|'key'
op|','
string|"'False'"
op|')'
newline|'\n'
name|'return'
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'raw_value'
op|','
name|'strict'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_guest_agent
dedent|''
dedent|''
name|'def'
name|'find_guest_agent'
op|'('
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""tries to locate a guest agent at the path\n    specified by agent_rel_path\n    """'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'disable_agent'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'agent_rel_path'
op|'='
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'agent_path'
newline|'\n'
name|'agent_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'agent_rel_path'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'agent_path'
op|')'
op|':'
newline|'\n'
comment|'# The presence of the guest agent'
nl|'\n'
comment|'# file indicates that this instance can'
nl|'\n'
comment|'# reconfigure the network from xenstore data,'
nl|'\n'
comment|'# so manipulation of files in /etc is not'
nl|'\n'
comment|'# required'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'XenServer tools installed in this '"
nl|'\n'
string|"'image are capable of network injection.  '"
nl|'\n'
string|"'Networking files will not be'"
nl|'\n'
string|"'manipulated'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'xe_daemon_filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
nl|'\n'
string|"'usr'"
op|','
string|"'sbin'"
op|','
string|"'xe-daemon'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'xe_daemon_filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'XenServer tools are present '"
nl|'\n'
string|"'in this image but are not capable '"
nl|'\n'
string|"'of network injection'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'XenServer tools are not '"
nl|'\n'
string|"'installed in this image'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|should_use_agent
dedent|''
name|'def'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'USE_AGENT_SM_KEY'
name|'not'
name|'in'
name|'sys_meta'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'use_agent_default'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'use_agent_raw'
op|'='
name|'sys_meta'
op|'['
name|'USE_AGENT_SM_KEY'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'use_agent_raw'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Invalid \'agent_present\' value. "'
nl|'\n'
string|'"Falling back to the default."'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'use_agent_default'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleDH
dedent|''
dedent|''
dedent|''
name|'class'
name|'SimpleDH'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This class wraps all the functionality needed to implement\n    basic Diffie-Hellman-Merkle key exchange in Python. It features\n    intelligent defaults for the prime and base numbers needed for the\n    calculation, while allowing you to supply your own. It requires that\n    the openssl binary be installed on the system on which this is run,\n    as it uses that to handle the encryption and decryption. If openssl\n    is not available, a RuntimeError will be raised.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_prime'
op|'='
number|'162259276829213363391578010288127'
newline|'\n'
name|'self'
op|'.'
name|'_base'
op|'='
number|'5'
newline|'\n'
name|'self'
op|'.'
name|'_public'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_shared'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'generate_private'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|generate_private
dedent|''
name|'def'
name|'generate_private'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_private'
op|'='
name|'int'
op|'('
name|'binascii'
op|'.'
name|'hexlify'
op|'('
name|'os'
op|'.'
name|'urandom'
op|'('
number|'10'
op|')'
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_private'
newline|'\n'
nl|'\n'
DECL|member|get_public
dedent|''
name|'def'
name|'get_public'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_public'
op|'='
name|'pow'
op|'('
name|'self'
op|'.'
name|'_base'
op|','
name|'self'
op|'.'
name|'_private'
op|','
name|'self'
op|'.'
name|'_prime'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_public'
newline|'\n'
nl|'\n'
DECL|member|compute_shared
dedent|''
name|'def'
name|'compute_shared'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shared'
op|'='
name|'pow'
op|'('
name|'other'
op|','
name|'self'
op|'.'
name|'_private'
op|','
name|'self'
op|'.'
name|'_prime'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_shared'
newline|'\n'
nl|'\n'
DECL|member|_run_ssl
dedent|''
name|'def'
name|'_run_ssl'
op|'('
name|'self'
op|','
name|'text'
op|','
name|'decrypt'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'['
string|"'openssl'"
op|','
string|"'aes-128-cbc'"
op|','
string|"'-A'"
op|','
string|"'-a'"
op|','
string|"'-pass'"
op|','
nl|'\n'
string|"'pass:%s'"
op|'%'
name|'self'
op|'.'
name|'_shared'
op|','
string|"'-nosalt'"
op|']'
newline|'\n'
name|'if'
name|'decrypt'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'append'
op|'('
string|"'-d'"
op|')'
newline|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'OpenSSL error: %s'"
op|')'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
newline|'\n'
nl|'\n'
DECL|member|encrypt
dedent|''
name|'def'
name|'encrypt'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_run_ssl'
op|'('
name|'text'
op|')'
op|'.'
name|'strip'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|decrypt
dedent|''
name|'def'
name|'decrypt'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_run_ssl'
op|'('
name|'text'
op|','
name|'decrypt'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
