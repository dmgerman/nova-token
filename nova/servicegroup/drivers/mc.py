begin_unit
comment|'# Service heartbeat driver using Memcached'
nl|'\n'
comment|'# Copyright (c) 2013 Akira Yoshiyama <akirayoshiyama at gmail dot com>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This is derived from nova/servicegroup/drivers/db.py.'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or'
nl|'\n'
comment|'# implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
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
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'memorycache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
name|'import'
name|'api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'service_down_time'"
op|','
string|"'nova.service'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'memcached_servers'"
op|','
string|"'nova.openstack.common.memorycache'"
op|')'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MemcachedDriver
name|'class'
name|'MemcachedDriver'
op|'('
name|'api'
op|'.'
name|'ServiceGroupDriver'
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
name|'test'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'test'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'memcached_servers'
name|'and'
name|'not'
name|'test'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'memcached_servers not defined'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mc'
op|'='
name|'memorycache'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db_allowed'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'db_allowed'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor_api'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
name|'use_local'
op|'='
name|'self'
op|'.'
name|'db_allowed'
op|')'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
name|'self'
op|','
name|'member_id'
op|','
name|'group_id'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Join the given service with its group."""'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'Memcached_Driver: join new ServiceGroup member '"
nl|'\n'
string|"'%(member_id)s to the %(group_id)s group, '"
nl|'\n'
string|"'service = %(service)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'member_id'"
op|':'
name|'member_id'
op|','
string|"'group_id'"
op|':'
name|'group_id'
op|','
nl|'\n'
string|"'service'"
op|':'
name|'service'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'service'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'service is a mandatory argument for '"
nl|'\n'
string|"'Memcached based ServiceGroup driver'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'report_interval'
op|'='
name|'service'
op|'.'
name|'report_interval'
newline|'\n'
name|'if'
name|'report_interval'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'.'
name|'tg'
op|'.'
name|'add_timer'
op|'('
name|'report_interval'
op|','
name|'self'
op|'.'
name|'_report_state'
op|','
nl|'\n'
name|'api'
op|'.'
name|'INITIAL_REPORTING_DELAY'
op|','
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_up
dedent|''
dedent|''
name|'def'
name|'is_up'
op|'('
name|'self'
op|','
name|'service_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Moved from nova.utils\n        Check whether a service is up based on last heartbeat.\n        """'
newline|'\n'
name|'key'
op|'='
string|'"%(topic)s:%(host)s"'
op|'%'
name|'service_ref'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'mc'
op|'.'
name|'get'
op|'('
name|'str'
op|'('
name|'key'
op|')'
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns ALL members of the given group\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Memcached_Driver: get_all members of the %s group'"
op|','
nl|'\n'
name|'group_id'
op|')'
newline|'\n'
name|'rs'
op|'='
op|'['
op|']'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'services'
op|'='
name|'self'
op|'.'
name|'conductor_api'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'ctxt'
op|','
name|'group_id'
op|')'
newline|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'is_up'
op|'('
name|'service'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'rs'
op|'.'
name|'append'
op|'('
name|'service'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rs'
newline|'\n'
nl|'\n'
DECL|member|_report_state
dedent|''
name|'def'
name|'_report_state'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the state of this service in the datastore."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|'='
string|'"%(topic)s:%(host)s"'
op|'%'
name|'service'
op|'.'
name|'service_ref'
newline|'\n'
comment|'# memcached has data expiration time capability.'
nl|'\n'
comment|'# set(..., time=CONF.service_down_time) uses it and'
nl|'\n'
comment|'# reduces key-deleting code.'
nl|'\n'
name|'self'
op|'.'
name|'mc'
op|'.'
name|'set'
op|'('
name|'str'
op|'('
name|'key'
op|')'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'time'
op|'='
name|'CONF'
op|'.'
name|'service_down_time'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(termie): make this pattern be more elegant.'
nl|'\n'
name|'if'
name|'getattr'
op|'('
name|'service'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'.'
name|'model_disconnected'
op|'='
name|'False'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Recovered model server connection!'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(vish): this should probably only catch connection errors'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable=W0702'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'getattr'
op|'('
name|'service'
op|','
string|"'model_disconnected'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'service'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'model server went away'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
