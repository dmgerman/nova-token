begin_unit
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LI'
op|','
name|'_LW'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
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
DECL|class|DbDriver
name|'class'
name|'DbDriver'
op|'('
name|'base'
op|'.'
name|'Driver'
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
name|'self'
op|'.'
name|'service_down_time'
op|'='
name|'CONF'
op|'.'
name|'service_down_time'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
name|'self'
op|','
name|'member'
op|','
name|'group'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a new member to a service group.\n\n        :param member: the joined member ID/name\n        :param group: the group ID/name, of the joined member\n        :param service: a `nova.service.Service` object\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'DB_Driver: join new ServiceGroup member %(member)s to '"
nl|'\n'
string|"'the %(group)s group, service = %(service)s'"
op|','
nl|'\n'
op|'{'
string|"'member'"
op|':'
name|'member'
op|','
string|"'group'"
op|':'
name|'group'
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
string|"'service is a mandatory argument for DB based'"
nl|'\n'
string|"' ServiceGroup driver'"
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
comment|"# Keep checking 'updated_at' if 'last_seen_up' isn't set."
nl|'\n'
comment|"# Should be able to use only 'last_seen_up' in the M release"
nl|'\n'
name|'last_heartbeat'
op|'='
op|'('
name|'service_ref'
op|'.'
name|'get'
op|'('
string|"'last_seen_up'"
op|')'
name|'or'
nl|'\n'
name|'service_ref'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'service_ref'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'last_heartbeat'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb) If this service_ref came in over rpc via'
nl|'\n'
comment|'# conductor, then the timestamp will be a string and needs to be'
nl|'\n'
comment|'# converted back to a datetime.'
nl|'\n'
indent|'            '
name|'last_heartbeat'
op|'='
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'last_heartbeat'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Objects have proper UTC timezones, but the timeutils comparison'
nl|'\n'
comment|'# below does not (and will fail)'
nl|'\n'
indent|'            '
name|'last_heartbeat'
op|'='
name|'last_heartbeat'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
comment|'# Timestamps in DB are UTC.'
nl|'\n'
dedent|''
name|'elapsed'
op|'='
name|'timeutils'
op|'.'
name|'delta_seconds'
op|'('
name|'last_heartbeat'
op|','
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
newline|'\n'
name|'is_up'
op|'='
name|'abs'
op|'('
name|'elapsed'
op|')'
op|'<='
name|'self'
op|'.'
name|'service_down_time'
newline|'\n'
name|'if'
name|'not'
name|'is_up'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Seems service %(binary)s on host %(host)s is down. '"
nl|'\n'
string|"'Last heartbeat was %(lhb)s. Elapsed time is %(el)s'"
op|','
nl|'\n'
op|'{'
string|"'binary'"
op|':'
name|'service_ref'
op|'.'
name|'get'
op|'('
string|"'binary'"
op|')'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'service_ref'
op|'.'
name|'get'
op|'('
string|"'host'"
op|')'
op|','
nl|'\n'
string|"'lhb'"
op|':'
name|'str'
op|'('
name|'last_heartbeat'
op|')'
op|','
string|"'el'"
op|':'
name|'str'
op|'('
name|'elapsed'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'is_up'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'.'
name|'service_ref'
op|'.'
name|'report_count'
op|'+='
number|'1'
newline|'\n'
name|'service'
op|'.'
name|'service_ref'
op|'.'
name|'save'
op|'('
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
name|'info'
op|'('
nl|'\n'
name|'_LI'
op|'('
string|"'Recovered from being unable to report status.'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'messaging'
op|'.'
name|'MessagingTimeout'
op|':'
newline|'\n'
comment|'# NOTE(johngarbutt) during upgrade we will see messaging timeouts'
nl|'\n'
comment|'# as nova-conductor is restarted, so only log this error once.'
nl|'\n'
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
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'Lost connection to nova-conductor '"
nl|'\n'
string|"'for reporting service status.'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|"# NOTE(rpodolyaka): we'd like to avoid catching of all possible"
nl|'\n'
comment|'# exceptions here, but otherwise it would become possible for'
nl|'\n'
comment|'# the state reporting thread to stop abruptly, and thus leave'
nl|'\n'
comment|"# the service unusable until it's restarted."
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
nl|'\n'
name|'_LE'
op|'('
string|"'Unexpected error while reporting service status'"
op|')'
op|')'
newline|'\n'
comment|'# trigger the recovery log message, if this error goes away'
nl|'\n'
name|'service'
op|'.'
name|'model_disconnected'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
