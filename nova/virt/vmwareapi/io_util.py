begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nUtility classes for defining the time saving transfer of data from the reader\r\nto the write using a LightQueue as a Pipe between the reader and the writer.\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\r\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\r\n'
name|'from'
name|'eventlet'
op|'.'
name|'queue'
name|'import'
name|'LightQueue'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'glance'
name|'import'
name|'client'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\r\n'
nl|'\r\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.vmwareapi.io_util"'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|variable|IO_THREAD_SLEEP_TIME
name|'IO_THREAD_SLEEP_TIME'
op|'='
number|'.01'
newline|'\r\n'
DECL|variable|GLANCE_POLL_INTERVAL
name|'GLANCE_POLL_INTERVAL'
op|'='
number|'5'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|ThreadSafePipe
name|'class'
name|'ThreadSafePipe'
op|'('
name|'LightQueue'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""The pipe to hold the data which the reader writes to and the writer\r\n    reads from."""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'maxsize'
op|','
name|'transfer_size'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'LightQueue'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'maxsize'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'transfer_size'
op|'='
name|'transfer_size'
newline|'\r\n'
name|'self'
op|'.'
name|'transferred'
op|'='
number|'0'
newline|'\r\n'
nl|'\r\n'
DECL|member|read
dedent|''
name|'def'
name|'read'
op|'('
name|'self'
op|','
name|'chunk_size'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Read data from the pipe. Chunksize if ignored for we have ensured\r\n        that the data chunks written to the pipe by readers is the same as the\r\n        chunks asked for by the Writer."""'
newline|'\r\n'
name|'if'
name|'self'
op|'.'
name|'transferred'
op|'<'
name|'self'
op|'.'
name|'transfer_size'
op|':'
newline|'\r\n'
indent|'            '
name|'data_item'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'transferred'
op|'+='
name|'len'
op|'('
name|'data_item'
op|')'
newline|'\r\n'
name|'return'
name|'data_item'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'            '
name|'return'
string|'""'
newline|'\r\n'
nl|'\r\n'
DECL|member|write
dedent|''
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Put a data item in the pipe."""'
newline|'\r\n'
name|'self'
op|'.'
name|'put'
op|'('
name|'data'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""A place-holder to maintain consistency."""'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|GlanceWriteThread
dedent|''
dedent|''
name|'class'
name|'GlanceWriteThread'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Ensures that image data is written to in the glance client and that\r\n    it is in correct (\'active\')state."""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'input'
op|','
name|'glance_client'
op|','
name|'image_id'
op|','
name|'image_meta'
op|'='
name|'None'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'if'
name|'not'
name|'image_meta'
op|':'
newline|'\r\n'
indent|'            '
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'self'
op|'.'
name|'input'
op|'='
name|'input'
newline|'\r\n'
name|'self'
op|'.'
name|'glance_client'
op|'='
name|'glance_client'
newline|'\r\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_id'
newline|'\r\n'
name|'self'
op|'.'
name|'image_meta'
op|'='
name|'image_meta'
newline|'\r\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\r\n'
nl|'\r\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\r\n'
indent|'            '
string|'"""Function to do the image data transfer through an update\r\n            and thereon checks if the state is \'active\'."""'
newline|'\r\n'
name|'self'
op|'.'
name|'glance_client'
op|'.'
name|'update_image'
op|'('
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\r\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'image_meta'
op|','
nl|'\r\n'
name|'image_data'
op|'='
name|'self'
op|'.'
name|'input'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\r\n'
name|'while'
name|'self'
op|'.'
name|'_running'
op|':'
newline|'\r\n'
indent|'                '
name|'try'
op|':'
newline|'\r\n'
indent|'                    '
name|'image_status'
op|'='
name|'self'
op|'.'
name|'glance_client'
op|'.'
name|'get_image_meta'
op|'('
name|'self'
op|'.'
name|'image_id'
op|')'
op|'.'
name|'get'
op|'('
nl|'\r\n'
string|'"status"'
op|')'
newline|'\r\n'
name|'if'
name|'image_status'
op|'=='
string|'"active"'
op|':'
newline|'\r\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send'
op|'('
name|'True'
op|')'
newline|'\r\n'
comment|'# If the state is killed, then raise an exception.'
nl|'\r\n'
dedent|''
name|'elif'
name|'image_status'
op|'=='
string|'"killed"'
op|':'
newline|'\r\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'exc_msg'
op|'='
name|'_'
op|'('
string|'"Glance image %s is in killed state"'
op|')'
op|'%'
name|'self'
op|'.'
name|'image_id'
newline|'\r\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc_msg'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exception'
op|'.'
name|'Error'
op|'('
name|'exc_msg'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'elif'
name|'image_status'
name|'in'
op|'['
string|'"saving"'
op|','
string|'"queued"'
op|']'
op|':'
newline|'\r\n'
indent|'                        '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'GLANCE_POLL_INTERVAL'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'exc_msg'
op|'='
name|'_'
op|'('
string|'"Glance image "'
nl|'\r\n'
string|'"%(image_id)s is in unknown state "'
nl|'\r\n'
string|'"- %(state)s"'
op|')'
op|'%'
op|'{'
nl|'\r\n'
string|'"image_id"'
op|':'
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\r\n'
string|'"state"'
op|':'
name|'image_status'
op|'}'
newline|'\r\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc_msg'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exception'
op|'.'
name|'Error'
op|'('
name|'exc_msg'
op|')'
op|')'
newline|'\r\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\r\n'
indent|'                    '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exc'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
dedent|''
dedent|''
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'done'
newline|'\r\n'
nl|'\r\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\r\n'
nl|'\r\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'pass'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|IOThread
dedent|''
dedent|''
name|'class'
name|'IOThread'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Class that reads chunks from the input file and writes them to the\r\n    output file till the transfer is completely done."""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'input'
op|','
name|'output'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'input'
op|'='
name|'input'
newline|'\r\n'
name|'self'
op|'.'
name|'output'
op|'='
name|'output'
newline|'\r\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\r\n'
name|'self'
op|'.'
name|'got_exception'
op|'='
name|'False'
newline|'\r\n'
nl|'\r\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\r\n'
indent|'            '
string|'"""Read data from the input and write the same to the output\r\n            until the transfer completes."""'
newline|'\r\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\r\n'
name|'while'
name|'self'
op|'.'
name|'_running'
op|':'
newline|'\r\n'
indent|'                '
name|'try'
op|':'
newline|'\r\n'
indent|'                    '
name|'data'
op|'='
name|'self'
op|'.'
name|'input'
op|'.'
name|'read'
op|'('
name|'None'
op|')'
newline|'\r\n'
name|'if'
name|'not'
name|'data'
op|':'
newline|'\r\n'
indent|'                        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send'
op|'('
name|'True'
op|')'
newline|'\r\n'
dedent|''
name|'self'
op|'.'
name|'output'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\r\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'IO_THREAD_SLEEP_TIME'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\r\n'
indent|'                    '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\r\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'exc'
op|')'
newline|'\r\n'
nl|'\r\n'
dedent|''
dedent|''
dedent|''
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'done'
newline|'\r\n'
nl|'\r\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\r\n'
nl|'\r\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
