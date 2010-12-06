begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""\nA connection to XenServer or Xen Cloud Platform.\n\nThe concurrency model for this class is as follows:\n\nAll XenAPI calls are on a thread (using t.i.t.deferToThread, via the decorator\ndeferredToThread).  They are remote calls, and so may hang for the usual\nreasons.  They should not be allowed to block the reactor thread.\n\nAll long-running XenAPI calls (VM.start, VM.reboot, etc) are called async\n(using XenAPI.VM.async_start etc).  These return a task, which can then be\npolled for completion.  Polling is handled using reactor.callLater.\n\nThis combination of techniques means that we don\'t block the reactor thread at\nall, and at the same time we don\'t hold lots of threads waiting for\nlong-running operations.\n\nFIXME: get_info currently doesn\'t conform to these rules, and will block the\nreactor thread if the VM.get_by_name_label or VM.get_record calls block.\n\n**Related Flags**\n\n:xenapi_connection_url:  URL for connection to XenServer/Xen Cloud Platform.\n:xenapi_connection_username:  Username for connection to XenServer/Xen Cloud\n                              Platform (default: root).\n:xenapi_connection_password:  Password for connection to XenServer/Xen Cloud\n                              Platform.\n:xenapi_task_poll_interval:  The interval (seconds) used for polling of\n                             remote tasks (Async.VM.start, etc)\n                             (default: 0.5).\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'xmlrpclib'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'from'
name|'xenapi'
op|'.'
name|'vmops'
name|'import'
name|'VMOps'
newline|'\n'
name|'from'
name|'xenapi'
op|'.'
name|'volumeops'
name|'import'
name|'VolumeOps'
newline|'\n'
name|'from'
name|'xenapi'
op|'.'
name|'novadeps'
name|'import'
name|'Configuration'
newline|'\n'
name|'from'
name|'xenapi'
name|'import'
name|'XenAPI'
newline|'\n'
nl|'\n'
DECL|variable|Config
name|'Config'
op|'='
name|'Configuration'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Note that XenAPI doesn\'t have a read-only connection mode, so\n    the read_only parameter is ignored."""'
newline|'\n'
name|'url'
op|'='
name|'Config'
op|'.'
name|'xenapi_connection_url'
newline|'\n'
name|'username'
op|'='
name|'Config'
op|'.'
name|'xenapi_connection_username'
newline|'\n'
name|'password'
op|'='
name|'Config'
op|'.'
name|'xenapi_connection_password'
newline|'\n'
name|'if'
name|'not'
name|'url'
name|'or'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|"'Must specify xenapi_connection_url, '"
nl|'\n'
string|"'xenapi_connection_username (optionally), and '"
nl|'\n'
string|"'xenapi_connection_password to use '"
nl|'\n'
string|"'connection_type=xenapi'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'XenAPIConnection'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIConnection
dedent|''
name|'class'
name|'XenAPIConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" A connection to XenServer or Xen Cloud Platform """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'XenAPISession'
op|'('
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'VMOps'
op|'('
name|'session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'VolumeOps'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" List VM instances """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create VM instance """'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Reboot VM instance """'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Destroy VM instance """'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Return data about VM instance """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Return snapshot of console """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Attach volume storage to VM instance """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volume'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'device_path'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Detach volume storage to VM instance """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_volume'
op|'('
name|'instance_name'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPISession
dedent|''
dedent|''
name|'class'
name|'XenAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" The session to invoke XenAPI SDK calls """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi
dedent|''
name|'def'
name|'get_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Return the xenapi object """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi_host
dedent|''
name|'def'
name|'get_xenapi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Return the xenapi host """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'self'
op|'.'
name|'_session'
op|'.'
name|'handle'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|call_xenapi
name|'def'
name|'call_xenapi'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the specified XenAPI method on a background thread.  Returns\n        a Deferred for the result."""'
newline|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'method'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'f'
op|'.'
name|'__getattr__'
op|'('
name|'m'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|async_call_plugin
name|'def'
name|'async_call_plugin'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call Async.host.call_plugin on a background thread.  Returns a\n        Deferred with the task reference."""'
newline|'\n'
name|'return'
name|'_unwrap_plugin_exceptions'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'Async'
op|'.'
name|'host'
op|'.'
name|'call_plugin'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_for_task
dedent|''
name|'def'
name|'wait_for_task'
op|'('
name|'self'
op|','
name|'task'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a Deferred that will give the result of the given task.\n        The task is polled until it completes."""'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'task'
op|','
name|'d'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|_poll_task
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'task'
op|','
name|'deferred'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll the given XenAPI task, and fire the given Deferred if we\n        get a result."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|"#logging.debug('Polling task %s...', task)"
nl|'\n'
indent|'            '
name|'status'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_status'
op|'('
name|'task'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|"'pending'"
op|':'
newline|'\n'
indent|'                '
name|'reactor'
op|'.'
name|'callLater'
op|'('
name|'Config'
op|'.'
name|'xenapi_task_poll_interval'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'task'
op|','
name|'deferred'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'status'
op|'=='
string|"'success'"
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_result'
op|'('
name|'task'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Task %s status: success.  %s'"
op|','
name|'task'
op|','
name|'result'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'callback'
op|'('
name|'_parse_xmlrpc_value'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'error_info'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_error_info'
op|'('
name|'task'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Task %s status: %s.  %s'"
op|','
name|'task'
op|','
name|'status'
op|','
nl|'\n'
name|'error_info'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\n'
comment|"#logging.debug('Polling task %s done.', task)"
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unwrap_plugin_exceptions
dedent|''
dedent|''
dedent|''
name|'def'
name|'_unwrap_plugin_exceptions'
op|'('
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Parse exception details """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'func'
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
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Got exception: %s"'
op|','
name|'exc'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'exc'
op|'.'
name|'details'
op|')'
op|'=='
number|'4'
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'XENAPI_PLUGIN_EXCEPTION'"
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'2'
op|']'
op|'=='
string|"'Failure'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'eval'
op|'('
name|'exc'
op|'.'
name|'details'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
newline|'\n'
dedent|''
name|'raise'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'xmlrpclib'
op|'.'
name|'ProtocolError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Got exception: %s"'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_xmlrpc_value
dedent|''
dedent|''
name|'def'
name|'_parse_xmlrpc_value'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the given value as if it were an XML-RPC value.  This is\n    sometimes used as the format for the task.result field."""'
newline|'\n'
name|'if'
name|'not'
name|'val'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'val'
newline|'\n'
dedent|''
name|'x'
op|'='
name|'xmlrpclib'
op|'.'
name|'loads'
op|'('
nl|'\n'
string|'\'<?xml version="1.0"?><methodResponse><params><param>\''
op|'+'
nl|'\n'
name|'val'
op|'+'
nl|'\n'
string|"'</param></params></methodResponse>'"
op|')'
newline|'\n'
name|'return'
name|'x'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
