begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""Classes to handle image files\n\nCollection of classes to handle image upload/download to/from Image service\n(like Glance image storage and retrieval service) from/to ESX/ESXi server.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
name|'import'
name|'urllib2'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'glance'
name|'import'
name|'client'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.vmwareapi.read_write_util"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|USER_AGENT
name|'USER_AGENT'
op|'='
string|'"OpenStack-ESX-Adapter"'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
DECL|variable|READ_CHUNKSIZE
indent|'    '
name|'READ_CHUNKSIZE'
op|'='
name|'client'
op|'.'
name|'BaseClient'
op|'.'
name|'CHUNKSIZE'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
DECL|variable|READ_CHUNKSIZE
indent|'    '
name|'READ_CHUNKSIZE'
op|'='
number|'65536'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceFileRead
dedent|''
name|'class'
name|'GlanceFileRead'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Glance file read handler class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'glance_read_iter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'glance_read_iter'
op|'='
name|'glance_read_iter'
newline|'\n'
name|'self'
op|'.'
name|'iter'
op|'='
name|'self'
op|'.'
name|'get_next'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Read an item from the queue. The chunk size is ignored for the\n        Client ImageBodyIterator uses its own CHUNKSIZE."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'iter'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'""'
newline|'\n'
nl|'\n'
DECL|member|get_next
dedent|''
dedent|''
name|'def'
name|'get_next'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the next item from the image iterator."""'
newline|'\n'
name|'for'
name|'data'
name|'in'
name|'self'
op|'.'
name|'glance_read_iter'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""A dummy close just to maintain consistency."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareHTTPFile
dedent|''
dedent|''
name|'class'
name|'VMwareHTTPFile'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for HTTP file."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'file_handle'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'eof'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'file_handle'
op|'='
name|'file_handle'
newline|'\n'
nl|'\n'
DECL|member|set_eof
dedent|''
name|'def'
name|'set_eof'
op|'('
name|'self'
op|','
name|'eof'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the end of file marker."""'
newline|'\n'
name|'self'
op|'.'
name|'eof'
op|'='
name|'eof'
newline|'\n'
nl|'\n'
DECL|member|get_eof
dedent|''
name|'def'
name|'get_eof'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if the end of file has been reached."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'eof'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Close the file handle."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__del__
dedent|''
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Close the file handle on garbage collection."""'
newline|'\n'
name|'self'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_vim_cookie_headers
dedent|''
name|'def'
name|'_build_vim_cookie_headers'
op|'('
name|'self'
op|','
name|'vim_cookies'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Build ESX host session cookie headers."""'
newline|'\n'
name|'cookie_header'
op|'='
string|'""'
newline|'\n'
name|'for'
name|'vim_cookie'
name|'in'
name|'vim_cookies'
op|':'
newline|'\n'
indent|'            '
name|'cookie_header'
op|'='
name|'vim_cookie'
op|'.'
name|'name'
op|'+'
string|'"="'
op|'+'
name|'vim_cookie'
op|'.'
name|'value'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'return'
name|'cookie_header'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Write data to the file."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Read a chunk of data."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get size of the file to be read."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMWareHTTPWriteFile
dedent|''
dedent|''
name|'class'
name|'VMWareHTTPWriteFile'
op|'('
name|'VMwareHTTPFile'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VMWare file write handler class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'data_center_name'
op|','
name|'datastore_name'
op|','
name|'cookies'
op|','
nl|'\n'
name|'file_path'
op|','
name|'file_size'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"%s://%s/folder/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
name|'file_path'
op|')'
newline|'\n'
name|'param_list'
op|'='
op|'{'
string|'"dcPath"'
op|':'
name|'data_center_name'
op|','
string|'"dsName"'
op|':'
name|'datastore_name'
op|'}'
newline|'\n'
name|'base_url'
op|'='
name|'base_url'
op|'+'
string|'"?"'
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'param_list'
op|')'
newline|'\n'
name|'_urlparse'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'base_url'
op|')'
newline|'\n'
name|'scheme'
op|','
name|'netloc'
op|','
name|'path'
op|','
name|'params'
op|','
name|'query'
op|','
name|'fragment'
op|'='
name|'_urlparse'
newline|'\n'
name|'if'
name|'scheme'
op|'=='
string|'"http"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'('
name|'netloc'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'scheme'
op|'=='
string|'"https"'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'='
name|'httplib'
op|'.'
name|'HTTPSConnection'
op|'('
name|'netloc'
op|')'
newline|'\n'
dedent|''
name|'conn'
op|'.'
name|'putrequest'
op|'('
string|'"PUT"'
op|','
name|'path'
op|'+'
string|'"?"'
op|'+'
name|'query'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"User-Agent"'
op|','
name|'USER_AGENT'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Content-Length"'
op|','
name|'file_size'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'putheader'
op|'('
string|'"Cookie"'
op|','
name|'self'
op|'.'
name|'_build_vim_cookie_headers'
op|'('
name|'cookies'
op|')'
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'endheaders'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'conn'
newline|'\n'
name|'VMwareHTTPFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Write to the file."""'
newline|'\n'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'send'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the response and close the connection."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'getresponse'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Exception during HTTP connection close in "'
nl|'\n'
string|'"VMWareHTTpWrite. Exception is %s"'
op|')'
op|'%'
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'VMWareHTTPWriteFile'
op|','
name|'self'
op|')'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VmWareHTTPReadFile
dedent|''
dedent|''
name|'class'
name|'VmWareHTTPReadFile'
op|'('
name|'VMwareHTTPFile'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VMWare file read handler class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'data_center_name'
op|','
name|'datastore_name'
op|','
name|'cookies'
op|','
nl|'\n'
name|'file_path'
op|','
name|'scheme'
op|'='
string|'"https"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'base_url'
op|'='
string|'"%s://%s/folder/%s"'
op|'%'
op|'('
name|'scheme'
op|','
name|'host'
op|','
nl|'\n'
name|'urllib'
op|'.'
name|'pathname2url'
op|'('
name|'file_path'
op|')'
op|')'
newline|'\n'
name|'param_list'
op|'='
op|'{'
string|'"dcPath"'
op|':'
name|'data_center_name'
op|','
string|'"dsName"'
op|':'
name|'datastore_name'
op|'}'
newline|'\n'
name|'base_url'
op|'='
name|'base_url'
op|'+'
string|'"?"'
op|'+'
name|'urllib'
op|'.'
name|'urlencode'
op|'('
name|'param_list'
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
string|"'User-Agent'"
op|':'
name|'USER_AGENT'
op|','
nl|'\n'
string|"'Cookie'"
op|':'
name|'self'
op|'.'
name|'_build_vim_cookie_headers'
op|'('
name|'cookies'
op|')'
op|'}'
newline|'\n'
name|'request'
op|'='
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'base_url'
op|','
name|'None'
op|','
name|'headers'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'request'
op|')'
newline|'\n'
name|'VMwareHTTPFile'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'conn'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
string|'"""Read a chunk of data."""'
newline|'\n'
comment|'# We are ignoring the chunk size passed for we want the pipe to hold'
nl|'\n'
comment|'# data items of the chunk-size that Glance Client uses for read'
nl|'\n'
comment|'# while writing.'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'read'
op|'('
name|'READ_CHUNKSIZE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_size
dedent|''
name|'def'
name|'get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get size of the file to be read."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'file_handle'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"Content-Length"'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
