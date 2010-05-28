begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2009 Facebook'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#     http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
string|'"""Blocking and non-blocking HTTP client implementations using pycurl."""'
newline|'\n'
nl|'\n'
name|'import'
name|'calendar'
newline|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'cStringIO'
newline|'\n'
name|'import'
name|'email'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'ioloop'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'pycurl'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'weakref'
newline|'\n'
nl|'\n'
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'tornado.httpclient'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|HTTPClient
name|'class'
name|'HTTPClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A blocking HTTP client backed with pycurl.\n\n    Typical usage looks like this:\n\n        http_client = httpclient.HTTPClient()\n        try:\n            response = http_client.fetch("http://www.google.com/")\n            print response.body\n        except httpclient.HTTPError, e:\n            print "Error:", e\n\n    fetch() can take a string URL or an HTTPRequest instance, which offers\n    more options, like executing POST/PUT/DELETE requests.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'max_simultaneous_connections'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_curl'
op|'='
name|'_curl_create'
op|'('
name|'max_simultaneous_connections'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__del__
dedent|''
name|'def'
name|'__del__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_curl'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch
dedent|''
name|'def'
name|'fetch'
op|'('
name|'self'
op|','
name|'request'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Executes an HTTPRequest, returning an HTTPResponse.\n\n        If an error occurs during the fetch, we raise an HTTPError.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'request'
op|','
name|'HTTPRequest'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'request'
op|'='
name|'HTTPRequest'
op|'('
name|'url'
op|'='
name|'request'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'buffer'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'_curl_setup_request'
op|'('
name|'self'
op|'.'
name|'_curl'
op|','
name|'request'
op|','
name|'buffer'
op|','
name|'headers'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_curl'
op|'.'
name|'perform'
op|'('
op|')'
newline|'\n'
name|'code'
op|'='
name|'self'
op|'.'
name|'_curl'
op|'.'
name|'getinfo'
op|'('
name|'pycurl'
op|'.'
name|'HTTP_CODE'
op|')'
newline|'\n'
name|'if'
name|'code'
op|'<'
number|'200'
name|'or'
name|'code'
op|'>='
number|'300'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'HTTPError'
op|'('
name|'code'
op|')'
newline|'\n'
dedent|''
name|'effective_url'
op|'='
name|'self'
op|'.'
name|'_curl'
op|'.'
name|'getinfo'
op|'('
name|'pycurl'
op|'.'
name|'EFFECTIVE_URL'
op|')'
newline|'\n'
name|'return'
name|'HTTPResponse'
op|'('
nl|'\n'
name|'request'
op|'='
name|'request'
op|','
name|'code'
op|'='
name|'code'
op|','
name|'headers'
op|'='
name|'headers'
op|','
nl|'\n'
name|'body'
op|'='
name|'buffer'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
name|'effective_url'
op|'='
name|'effective_url'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'pycurl'
op|'.'
name|'error'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'CurlError'
op|'('
op|'*'
name|'e'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'buffer'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AsyncHTTPClient
dedent|''
dedent|''
dedent|''
name|'class'
name|'AsyncHTTPClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An non-blocking HTTP client backed with pycurl.\n\n    Example usage:\n\n        import ioloop\n\n        def handle_request(response):\n            if response.error:\n                print "Error:", response.error\n            else:\n                print response.body\n            ioloop.IOLoop.instance().stop()\n\n        http_client = httpclient.AsyncHTTPClient()\n        http_client.fetch("http://www.google.com/", handle_request)\n        ioloop.IOLoop.instance().start()\n\n    fetch() can take a string URL or an HTTPRequest instance, which offers\n    more options, like executing POST/PUT/DELETE requests.\n\n    The keyword argument max_clients to the AsyncHTTPClient constructor\n    determines the maximum number of simultaneous fetch() operations that\n    can execute in parallel on each IOLoop.\n    """'
newline|'\n'
DECL|variable|_ASYNC_CLIENTS
name|'_ASYNC_CLIENTS'
op|'='
name|'weakref'
op|'.'
name|'WeakKeyDictionary'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__new__
name|'def'
name|'__new__'
op|'('
name|'cls'
op|','
name|'io_loop'
op|'='
name|'None'
op|','
name|'max_clients'
op|'='
number|'10'
op|','
nl|'\n'
name|'max_simultaneous_connections'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# There is one client per IOLoop since they share curl instances'
nl|'\n'
indent|'        '
name|'io_loop'
op|'='
name|'io_loop'
name|'or'
name|'ioloop'
op|'.'
name|'IOLoop'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'io_loop'
name|'in'
name|'cls'
op|'.'
name|'_ASYNC_CLIENTS'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_ASYNC_CLIENTS'
op|'['
name|'io_loop'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'super'
op|'('
name|'AsyncHTTPClient'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'io_loop'
op|'='
name|'io_loop'
newline|'\n'
name|'instance'
op|'.'
name|'_multi'
op|'='
name|'pycurl'
op|'.'
name|'CurlMulti'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'_curls'
op|'='
op|'['
name|'_curl_create'
op|'('
name|'max_simultaneous_connections'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max_clients'
op|')'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'_free_list'
op|'='
name|'instance'
op|'.'
name|'_curls'
op|'['
op|':'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'_requests'
op|'='
name|'collections'
op|'.'
name|'deque'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'_fds'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance'
op|'.'
name|'_events'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance'
op|'.'
name|'_added_perform_callback'
op|'='
name|'False'
newline|'\n'
name|'instance'
op|'.'
name|'_timeout'
op|'='
name|'None'
newline|'\n'
name|'cls'
op|'.'
name|'_ASYNC_CLIENTS'
op|'['
name|'io_loop'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'return'
name|'instance'
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
string|'"""Destroys this http client, freeing any file descriptors used.\n        Not needed in normal use, but may be helpful in unittests that\n        create and destroy http clients.  No other methods may be called\n        on the AsyncHTTPClient after close().\n        """'
newline|'\n'
name|'del'
name|'AsyncHTTPClient'
op|'.'
name|'_ASYNC_CLIENTS'
op|'['
name|'self'
op|'.'
name|'io_loop'
op|']'
newline|'\n'
name|'for'
name|'curl'
name|'in'
name|'self'
op|'.'
name|'_curls'
op|':'
newline|'\n'
indent|'            '
name|'curl'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch
dedent|''
name|'def'
name|'fetch'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'callback'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Executes an HTTPRequest, calling callback with an HTTPResponse.\n\n        If an error occurs during the fetch, the HTTPResponse given to the\n        callback has a non-None error attribute that contains the exception\n        encountered during the request. You can call response.reraise() to\n        throw the exception (if any) in the callback.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'request'
op|','
name|'HTTPRequest'
op|')'
op|':'
newline|'\n'
indent|'           '
name|'request'
op|'='
name|'HTTPRequest'
op|'('
name|'url'
op|'='
name|'request'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_requests'
op|'.'
name|'append'
op|'('
op|'('
name|'request'
op|','
name|'callback'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_perform_callback'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_perform_callback
dedent|''
name|'def'
name|'_add_perform_callback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_added_perform_callback'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'add_callback'
op|'('
name|'self'
op|'.'
name|'_perform'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_added_perform_callback'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_handle_events
dedent|''
dedent|''
name|'def'
name|'_handle_events'
op|'('
name|'self'
op|','
name|'fd'
op|','
name|'events'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_events'
op|'['
name|'fd'
op|']'
op|'='
name|'events'
newline|'\n'
name|'self'
op|'.'
name|'_add_perform_callback'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_handle_timeout
dedent|''
name|'def'
name|'_handle_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_timeout'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_perform'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_perform
dedent|''
name|'def'
name|'_perform'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_added_perform_callback'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|','
name|'num_handles'
op|'='
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'perform'
op|'('
op|')'
newline|'\n'
name|'if'
name|'ret'
op|'!='
name|'pycurl'
op|'.'
name|'E_CALL_MULTI_PERFORM'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
nl|'\n'
comment|'# Handle completed fetches'
nl|'\n'
dedent|''
dedent|''
name|'completed'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'num_q'
op|','
name|'ok_list'
op|','
name|'err_list'
op|'='
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'info_read'
op|'('
op|')'
newline|'\n'
name|'for'
name|'curl'
name|'in'
name|'ok_list'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_finish'
op|'('
name|'curl'
op|')'
newline|'\n'
name|'completed'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'for'
name|'curl'
op|','
name|'errnum'
op|','
name|'errmsg'
name|'in'
name|'err_list'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_finish'
op|'('
name|'curl'
op|','
name|'errnum'
op|','
name|'errmsg'
op|')'
newline|'\n'
name|'completed'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'num_q'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
nl|'\n'
comment|'# Start fetching new URLs'
nl|'\n'
dedent|''
dedent|''
name|'started'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'_free_list'
name|'and'
name|'self'
op|'.'
name|'_requests'
op|':'
newline|'\n'
indent|'                '
name|'started'
op|'+='
number|'1'
newline|'\n'
name|'curl'
op|'='
name|'self'
op|'.'
name|'_free_list'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
op|'('
name|'request'
op|','
name|'callback'
op|')'
op|'='
name|'self'
op|'.'
name|'_requests'
op|'.'
name|'popleft'
op|'('
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'info'
op|'='
op|'{'
nl|'\n'
string|'"headers"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"buffer"'
op|':'
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
op|','
nl|'\n'
string|'"request"'
op|':'
name|'request'
op|','
nl|'\n'
string|'"callback"'
op|':'
name|'callback'
op|','
nl|'\n'
string|'"start_time"'
op|':'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'_curl_setup_request'
op|'('
name|'curl'
op|','
name|'request'
op|','
name|'curl'
op|'.'
name|'info'
op|'['
string|'"buffer"'
op|']'
op|','
nl|'\n'
name|'curl'
op|'.'
name|'info'
op|'['
string|'"headers"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'add_handle'
op|'('
name|'curl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'started'
name|'and'
name|'not'
name|'completed'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'_timeout'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'remove_timeout'
op|'('
name|'self'
op|'.'
name|'_timeout'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_timeout'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'num_handles'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_timeout'
op|'='
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'add_timeout'
op|'('
nl|'\n'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'+'
number|'0.2'
op|','
name|'self'
op|'.'
name|'_handle_timeout'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait for more I/O'
nl|'\n'
dedent|''
name|'fds'
op|'='
op|'{'
op|'}'
newline|'\n'
op|'('
name|'readable'
op|','
name|'writable'
op|','
name|'exceptable'
op|')'
op|'='
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'fdset'
op|'('
op|')'
newline|'\n'
name|'for'
name|'fd'
name|'in'
name|'readable'
op|':'
newline|'\n'
indent|'            '
name|'fds'
op|'['
name|'fd'
op|']'
op|'='
name|'fds'
op|'.'
name|'get'
op|'('
name|'fd'
op|','
number|'0'
op|')'
op|'|'
number|'0x1'
op|'|'
number|'0x2'
newline|'\n'
dedent|''
name|'for'
name|'fd'
name|'in'
name|'writable'
op|':'
newline|'\n'
indent|'            '
name|'fds'
op|'['
name|'fd'
op|']'
op|'='
name|'fds'
op|'.'
name|'get'
op|'('
name|'fd'
op|','
number|'0'
op|')'
op|'|'
number|'0x4'
newline|'\n'
dedent|''
name|'for'
name|'fd'
name|'in'
name|'exceptable'
op|':'
newline|'\n'
indent|'            '
name|'fds'
op|'['
name|'fd'
op|']'
op|'='
name|'fds'
op|'.'
name|'get'
op|'('
name|'fd'
op|','
number|'0'
op|')'
op|'|'
number|'0x8'
op|'|'
number|'0x10'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'fd'
name|'in'
name|'self'
op|'.'
name|'_fds'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'fd'
name|'not'
name|'in'
name|'fds'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'remove_handler'
op|'('
name|'fd'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'OSError'
op|','
name|'IOError'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'e'
op|'['
number|'0'
op|']'
op|'!='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'for'
name|'fd'
op|','
name|'events'
name|'in'
name|'fds'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'old_events'
op|'='
name|'self'
op|'.'
name|'_fds'
op|'.'
name|'get'
op|'('
name|'fd'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'old_events'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'add_handler'
op|'('
name|'fd'
op|','
name|'self'
op|'.'
name|'_handle_events'
op|','
name|'events'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'old_events'
op|'!='
name|'events'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'update_handler'
op|'('
name|'fd'
op|','
name|'events'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'OSError'
op|','
name|'IOError'
op|')'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'e'
op|'['
number|'0'
op|']'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'io_loop'
op|'.'
name|'add_handler'
op|'('
name|'fd'
op|','
name|'self'
op|'.'
name|'_handle_events'
op|','
nl|'\n'
name|'events'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'_fds'
op|'='
name|'fds'
newline|'\n'
nl|'\n'
DECL|member|_finish
dedent|''
name|'def'
name|'_finish'
op|'('
name|'self'
op|','
name|'curl'
op|','
name|'curl_error'
op|'='
name|'None'
op|','
name|'curl_message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'curl'
op|'.'
name|'info'
newline|'\n'
name|'curl'
op|'.'
name|'info'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_multi'
op|'.'
name|'remove_handle'
op|'('
name|'curl'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_free_list'
op|'.'
name|'append'
op|'('
name|'curl'
op|')'
newline|'\n'
name|'if'
name|'curl_error'
op|':'
newline|'\n'
indent|'            '
name|'error'
op|'='
name|'CurlError'
op|'('
name|'curl_error'
op|','
name|'curl_message'
op|')'
newline|'\n'
name|'code'
op|'='
name|'error'
op|'.'
name|'code'
newline|'\n'
name|'body'
op|'='
name|'None'
newline|'\n'
name|'effective_url'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'error'
op|'='
name|'None'
newline|'\n'
name|'code'
op|'='
name|'curl'
op|'.'
name|'getinfo'
op|'('
name|'pycurl'
op|'.'
name|'HTTP_CODE'
op|')'
newline|'\n'
name|'body'
op|'='
name|'info'
op|'['
string|'"buffer"'
op|']'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'effective_url'
op|'='
name|'curl'
op|'.'
name|'getinfo'
op|'('
name|'pycurl'
op|'.'
name|'EFFECTIVE_URL'
op|')'
newline|'\n'
dedent|''
name|'info'
op|'['
string|'"buffer"'
op|']'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'info'
op|'['
string|'"callback"'
op|']'
op|'('
name|'HTTPResponse'
op|'('
nl|'\n'
name|'request'
op|'='
name|'info'
op|'['
string|'"request"'
op|']'
op|','
name|'code'
op|'='
name|'code'
op|','
name|'headers'
op|'='
name|'info'
op|'['
string|'"headers"'
op|']'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|','
name|'effective_url'
op|'='
name|'effective_url'
op|','
name|'error'
op|'='
name|'error'
op|','
nl|'\n'
name|'request_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'info'
op|'['
string|'"start_time"'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HTTPRequest
dedent|''
dedent|''
name|'class'
name|'HTTPRequest'
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
name|'url'
op|','
name|'method'
op|'='
string|'"GET"'
op|','
name|'headers'
op|'='
op|'{'
op|'}'
op|','
name|'body'
op|'='
name|'None'
op|','
nl|'\n'
name|'auth_username'
op|'='
name|'None'
op|','
name|'auth_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'connect_timeout'
op|'='
number|'20.0'
op|','
name|'request_timeout'
op|'='
number|'20.0'
op|','
nl|'\n'
name|'if_modified_since'
op|'='
name|'None'
op|','
name|'follow_redirects'
op|'='
name|'True'
op|','
nl|'\n'
name|'max_redirects'
op|'='
number|'5'
op|','
name|'user_agent'
op|'='
name|'None'
op|','
name|'use_gzip'
op|'='
name|'True'
op|','
nl|'\n'
name|'network_interface'
op|'='
name|'None'
op|','
name|'streaming_callback'
op|'='
name|'None'
op|','
nl|'\n'
name|'header_callback'
op|'='
name|'None'
op|','
name|'prepare_curl_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'if_modified_since'
op|':'
newline|'\n'
indent|'            '
name|'timestamp'
op|'='
name|'calendar'
op|'.'
name|'timegm'
op|'('
name|'if_modified_since'
op|'.'
name|'utctimetuple'
op|'('
op|')'
op|')'
newline|'\n'
name|'headers'
op|'['
string|'"If-Modified-Since"'
op|']'
op|'='
name|'email'
op|'.'
name|'utils'
op|'.'
name|'formatdate'
op|'('
nl|'\n'
name|'timestamp'
op|','
name|'localtime'
op|'='
name|'False'
op|','
name|'usegmt'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"Pragma"'
name|'not'
name|'in'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'['
string|'"Pragma"'
op|']'
op|'='
string|'""'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'url'
op|'='
name|'_utf8'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'method'
op|'='
name|'method'
newline|'\n'
name|'self'
op|'.'
name|'headers'
op|'='
name|'headers'
newline|'\n'
name|'self'
op|'.'
name|'body'
op|'='
name|'body'
newline|'\n'
name|'self'
op|'.'
name|'auth_username'
op|'='
name|'_utf8'
op|'('
name|'auth_username'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_password'
op|'='
name|'_utf8'
op|'('
name|'auth_password'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connect_timeout'
op|'='
name|'connect_timeout'
newline|'\n'
name|'self'
op|'.'
name|'request_timeout'
op|'='
name|'request_timeout'
newline|'\n'
name|'self'
op|'.'
name|'follow_redirects'
op|'='
name|'follow_redirects'
newline|'\n'
name|'self'
op|'.'
name|'max_redirects'
op|'='
name|'max_redirects'
newline|'\n'
name|'self'
op|'.'
name|'user_agent'
op|'='
name|'user_agent'
newline|'\n'
name|'self'
op|'.'
name|'use_gzip'
op|'='
name|'use_gzip'
newline|'\n'
name|'self'
op|'.'
name|'network_interface'
op|'='
name|'network_interface'
newline|'\n'
name|'self'
op|'.'
name|'streaming_callback'
op|'='
name|'streaming_callback'
newline|'\n'
name|'self'
op|'.'
name|'header_callback'
op|'='
name|'header_callback'
newline|'\n'
name|'self'
op|'.'
name|'prepare_curl_callback'
op|'='
name|'prepare_curl_callback'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HTTPResponse
dedent|''
dedent|''
name|'class'
name|'HTTPResponse'
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
name|'request'
op|','
name|'code'
op|','
name|'headers'
op|'='
op|'{'
op|'}'
op|','
name|'body'
op|'='
string|'""'
op|','
name|'effective_url'
op|'='
name|'None'
op|','
nl|'\n'
name|'error'
op|'='
name|'None'
op|','
name|'request_time'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'request'
op|'='
name|'request'
newline|'\n'
name|'self'
op|'.'
name|'code'
op|'='
name|'code'
newline|'\n'
name|'self'
op|'.'
name|'headers'
op|'='
name|'headers'
newline|'\n'
name|'self'
op|'.'
name|'body'
op|'='
name|'body'
newline|'\n'
name|'if'
name|'effective_url'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'effective_url'
op|'='
name|'request'
op|'.'
name|'url'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'effective_url'
op|'='
name|'effective_url'
newline|'\n'
dedent|''
name|'if'
name|'error'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'code'
op|'<'
number|'200'
name|'or'
name|'self'
op|'.'
name|'code'
op|'>='
number|'300'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'error'
op|'='
name|'HTTPError'
op|'('
name|'self'
op|'.'
name|'code'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'error'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'error'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'request_time'
op|'='
name|'request_time'
newline|'\n'
nl|'\n'
DECL|member|rethrow
dedent|''
name|'def'
name|'rethrow'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'error'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
string|'","'
op|'.'
name|'join'
op|'('
string|'"%s=%r"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
string|'"%s(%s)"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HTTPError
dedent|''
dedent|''
name|'class'
name|'HTTPError'
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
name|'code'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'code'
op|'='
name|'code'
newline|'\n'
name|'message'
op|'='
name|'message'
name|'or'
name|'httplib'
op|'.'
name|'responses'
op|'.'
name|'get'
op|'('
name|'code'
op|','
string|'"Unknown"'
op|')'
newline|'\n'
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
string|'"HTTP %d: %s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'code'
op|','
name|'message'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CurlError
dedent|''
dedent|''
name|'class'
name|'CurlError'
op|'('
name|'HTTPError'
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
name|'errno'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'HTTPError'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
number|'599'
op|','
name|'message'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'errno'
op|'='
name|'errno'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_curl_create
dedent|''
dedent|''
name|'def'
name|'_curl_create'
op|'('
name|'max_simultaneous_connections'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'curl'
op|'='
name|'pycurl'
op|'.'
name|'Curl'
op|'('
op|')'
newline|'\n'
name|'if'
name|'_log'
op|'.'
name|'isEnabledFor'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'VERBOSE'
op|','
number|'1'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'DEBUGFUNCTION'
op|','
name|'_curl_debug'
op|')'
newline|'\n'
dedent|''
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'MAXCONNECTS'
op|','
name|'max_simultaneous_connections'
name|'or'
number|'5'
op|')'
newline|'\n'
name|'return'
name|'curl'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_curl_setup_request
dedent|''
name|'def'
name|'_curl_setup_request'
op|'('
name|'curl'
op|','
name|'request'
op|','
name|'buffer'
op|','
name|'headers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'URL'
op|','
name|'request'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'HTTPHEADER'
op|','
nl|'\n'
op|'['
string|'"%s: %s"'
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'request'
op|'.'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'request'
op|'.'
name|'header_callback'
op|':'
newline|'\n'
indent|'            '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'HEADERFUNCTION'
op|','
name|'request'
op|'.'
name|'header_callback'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'HEADERFUNCTION'
op|','
nl|'\n'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'_curl_header_callback'
op|','
name|'headers'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
comment|'# Old version of curl; response will not include headers'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'streaming_callback'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'WRITEFUNCTION'
op|','
name|'request'
op|'.'
name|'streaming_callback'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'WRITEFUNCTION'
op|','
name|'buffer'
op|'.'
name|'write'
op|')'
newline|'\n'
dedent|''
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'FOLLOWLOCATION'
op|','
name|'request'
op|'.'
name|'follow_redirects'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'MAXREDIRS'
op|','
name|'request'
op|'.'
name|'max_redirects'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'CONNECTTIMEOUT'
op|','
name|'int'
op|'('
name|'request'
op|'.'
name|'connect_timeout'
op|')'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'TIMEOUT'
op|','
name|'int'
op|'('
name|'request'
op|'.'
name|'request_timeout'
op|')'
op|')'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'user_agent'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'USERAGENT'
op|','
name|'request'
op|'.'
name|'user_agent'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'USERAGENT'
op|','
string|'"Mozilla/5.0 (compatible; pycurl)"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'network_interface'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'INTERFACE'
op|','
name|'request'
op|'.'
name|'network_interface'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'use_gzip'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'ENCODING'
op|','
string|'"gzip,deflate"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'ENCODING'
op|','
string|'"none"'
op|')'
newline|'\n'
nl|'\n'
comment|"# Set the request method through curl's retarded interface which makes"
nl|'\n'
comment|'# up names for almost every single method'
nl|'\n'
dedent|''
name|'curl_options'
op|'='
op|'{'
nl|'\n'
string|'"GET"'
op|':'
name|'pycurl'
op|'.'
name|'HTTPGET'
op|','
nl|'\n'
string|'"POST"'
op|':'
name|'pycurl'
op|'.'
name|'POST'
op|','
nl|'\n'
string|'"PUT"'
op|':'
name|'pycurl'
op|'.'
name|'UPLOAD'
op|','
nl|'\n'
string|'"HEAD"'
op|':'
name|'pycurl'
op|'.'
name|'NOBODY'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'custom_methods'
op|'='
name|'set'
op|'('
op|'['
string|'"DELETE"'
op|']'
op|')'
newline|'\n'
name|'for'
name|'o'
name|'in'
name|'curl_options'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'o'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'method'
name|'in'
name|'curl_options'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'unsetopt'
op|'('
name|'pycurl'
op|'.'
name|'CUSTOMREQUEST'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'curl_options'
op|'['
name|'request'
op|'.'
name|'method'
op|']'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'request'
op|'.'
name|'method'
name|'in'
name|'custom_methods'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'CUSTOMREQUEST'
op|','
name|'request'
op|'.'
name|'method'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'KeyError'
op|'('
string|"'unknown method '"
op|'+'
name|'request'
op|'.'
name|'method'
op|')'
newline|'\n'
nl|'\n'
comment|"# Handle curl's cryptic options for every individual HTTP method"
nl|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'method'
name|'in'
op|'('
string|'"POST"'
op|','
string|'"PUT"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_buffer'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'READFUNCTION'
op|','
name|'request_buffer'
op|'.'
name|'read'
op|')'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'method'
op|'=='
string|'"POST"'
op|':'
newline|'\n'
DECL|function|ioctl
indent|'            '
name|'def'
name|'ioctl'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'cmd'
op|'=='
name|'curl'
op|'.'
name|'IOCMD_RESTARTREAD'
op|':'
newline|'\n'
indent|'                    '
name|'request_buffer'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'IOCTLFUNCTION'
op|','
name|'ioctl'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'POSTFIELDSIZE'
op|','
name|'len'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'INFILESIZE'
op|','
name|'len'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'request'
op|'.'
name|'auth_username'
name|'and'
name|'request'
op|'.'
name|'auth_password'
op|':'
newline|'\n'
indent|'        '
name|'userpwd'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'request'
op|'.'
name|'auth_username'
op|','
name|'request'
op|'.'
name|'auth_password'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'HTTPAUTH'
op|','
name|'pycurl'
op|'.'
name|'HTTPAUTH_BASIC'
op|')'
newline|'\n'
name|'curl'
op|'.'
name|'setopt'
op|'('
name|'pycurl'
op|'.'
name|'USERPWD'
op|','
name|'userpwd'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'info'
op|'('
string|'"%s %s (username: %r)"'
op|','
name|'request'
op|'.'
name|'method'
op|','
name|'request'
op|'.'
name|'url'
op|','
nl|'\n'
name|'request'
op|'.'
name|'auth_username'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'curl'
op|'.'
name|'unsetopt'
op|'('
name|'pycurl'
op|'.'
name|'USERPWD'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'info'
op|'('
string|'"%s %s"'
op|','
name|'request'
op|'.'
name|'method'
op|','
name|'request'
op|'.'
name|'url'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'request'
op|'.'
name|'prepare_curl_callback'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'prepare_curl_callback'
op|'('
name|'curl'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_curl_header_callback
dedent|''
dedent|''
name|'def'
name|'_curl_header_callback'
op|'('
name|'headers'
op|','
name|'header_line'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'header_line'
op|'.'
name|'startswith'
op|'('
string|'"HTTP/"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'header_line'
op|'=='
string|'"\\r\\n"'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'parts'
op|'='
name|'header_line'
op|'.'
name|'split'
op|'('
string|'": "'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'!='
number|'2'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'warning'
op|'('
string|'"Invalid HTTP response header line %r"'
op|','
name|'header_line'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'name'
op|'='
name|'parts'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'value'
op|'='
name|'parts'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'name'
name|'in'
name|'headers'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'['
name|'name'
op|']'
op|'='
name|'headers'
op|'['
name|'name'
op|']'
op|'+'
string|"','"
op|'+'
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'['
name|'name'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_curl_debug
dedent|''
dedent|''
name|'def'
name|'_curl_debug'
op|'('
name|'debug_type'
op|','
name|'debug_msg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'debug_types'
op|'='
op|'('
string|"'I'"
op|','
string|"'<'"
op|','
string|"'>'"
op|','
string|"'<'"
op|','
string|"'>'"
op|')'
newline|'\n'
name|'if'
name|'debug_type'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'%s'"
op|','
name|'debug_msg'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'debug_type'
name|'in'
op|'('
number|'1'
op|','
number|'2'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'line'
name|'in'
name|'debug_msg'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'%s %s'"
op|','
name|'debug_types'
op|'['
name|'debug_type'
op|']'
op|','
name|'line'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'debug_type'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'        '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'%s %r'"
op|','
name|'debug_types'
op|'['
name|'debug_type'
op|']'
op|','
name|'debug_msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_utf8
dedent|''
dedent|''
name|'def'
name|'_utf8'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
op|'.'
name|'encode'
op|'('
string|'"utf-8"'
op|')'
newline|'\n'
dedent|''
name|'assert'
name|'isinstance'
op|'('
name|'value'
op|','
name|'str'
op|')'
newline|'\n'
name|'return'
name|'value'
newline|'\n'
dedent|''
endmarker|''
end_unit
