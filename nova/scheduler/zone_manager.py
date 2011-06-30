begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nZoneManager oversees all communications with child Zones.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'novaclient'
newline|'\n'
name|'import'
name|'thread'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
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
name|'DEFINE_integer'
op|'('
string|"'zone_db_check_interval'"
op|','
number|'60'
op|','
nl|'\n'
string|"'Seconds between getting fresh zone info from db.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'zone_failures_to_offline'"
op|','
number|'3'
op|','
nl|'\n'
string|"'Number of consecutive errors before marking zone offline'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneState
name|'class'
name|'ZoneState'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Holds the state of all connected child zones."""'
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
name|'is_active'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'capabilities'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'attempt'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'last_seen'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'min'
newline|'\n'
name|'self'
op|'.'
name|'last_exception'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'last_exception_time'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|update_credentials
dedent|''
name|'def'
name|'update_credentials'
op|'('
name|'self'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update zone credentials from db"""'
newline|'\n'
name|'self'
op|'.'
name|'zone_id'
op|'='
name|'zone'
op|'.'
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'api_url'
op|'='
name|'zone'
op|'.'
name|'api_url'
newline|'\n'
name|'self'
op|'.'
name|'username'
op|'='
name|'zone'
op|'.'
name|'username'
newline|'\n'
name|'self'
op|'.'
name|'password'
op|'='
name|'zone'
op|'.'
name|'password'
newline|'\n'
nl|'\n'
DECL|member|update_metadata
dedent|''
name|'def'
name|'update_metadata'
op|'('
name|'self'
op|','
name|'zone_metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update zone metadata after successful communications with\n           child zone."""'
newline|'\n'
name|'self'
op|'.'
name|'last_seen'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'attempt'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'zone_metadata'
op|'.'
name|'get'
op|'('
string|'"name"'
op|','
string|'"n/a"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'capabilities'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
op|'['
string|'"%s=%s"'
op|'%'
op|'('
name|'k'
op|','
name|'v'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'zone_metadata'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
op|'!='
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'is_active'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'name'
op|'='
name|'self'
op|'.'
name|'name'
op|','
name|'capabilities'
op|'='
name|'self'
op|'.'
name|'capabilities'
op|','
nl|'\n'
name|'is_active'
op|'='
name|'self'
op|'.'
name|'is_active'
op|','
name|'api_url'
op|'='
name|'self'
op|'.'
name|'api_url'
op|','
nl|'\n'
name|'id'
op|'='
name|'self'
op|'.'
name|'zone_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|log_error
dedent|''
name|'def'
name|'log_error'
op|'('
name|'self'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Something went wrong. Check to see if zone should be\n           marked as offline."""'
newline|'\n'
name|'self'
op|'.'
name|'last_exception'
op|'='
name|'exception'
newline|'\n'
name|'self'
op|'.'
name|'last_exception_time'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'api_url'
op|'='
name|'self'
op|'.'
name|'api_url'
newline|'\n'
name|'logging'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"\'%(exception)s\' error talking to "'
nl|'\n'
string|'"zone %(api_url)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'max_errors'
op|'='
name|'FLAGS'
op|'.'
name|'zone_failures_to_offline'
newline|'\n'
name|'self'
op|'.'
name|'attempt'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'attempt'
op|'>='
name|'max_errors'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'is_active'
op|'='
name|'False'
newline|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"No answer from zone %(api_url)s "'
nl|'\n'
string|'"after %(max_errors)d "'
nl|'\n'
string|'"attempts. Marking inactive."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_call_novaclient
dedent|''
dedent|''
dedent|''
name|'def'
name|'_call_novaclient'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Call novaclient. Broken out for testing purposes."""'
newline|'\n'
name|'client'
op|'='
name|'novaclient'
op|'.'
name|'OpenStack'
op|'('
name|'zone'
op|'.'
name|'username'
op|','
name|'zone'
op|'.'
name|'password'
op|','
name|'None'
op|','
nl|'\n'
name|'zone'
op|'.'
name|'api_url'
op|')'
newline|'\n'
name|'return'
name|'client'
op|'.'
name|'zones'
op|'.'
name|'info'
op|'('
op|')'
op|'.'
name|'_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_poll_zone
dedent|''
name|'def'
name|'_poll_zone'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Eventlet worker to poll a zone."""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Polling zone: %s"'
op|')'
op|'%'
name|'zone'
op|'.'
name|'api_url'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'zone'
op|'.'
name|'update_metadata'
op|'('
name|'_call_novaclient'
op|'('
name|'zone'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'zone'
op|'.'
name|'log_error'
op|'('
name|'traceback'
op|'.'
name|'format_exc'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneManager
dedent|''
dedent|''
name|'class'
name|'ZoneManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keeps the zone states updated."""'
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
name|'last_zone_db_check'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'min'
newline|'\n'
name|'self'
op|'.'
name|'zone_states'
op|'='
op|'{'
op|'}'
comment|'# { <zone_id> : ZoneState }'
newline|'\n'
name|'self'
op|'.'
name|'service_states'
op|'='
op|'{'
op|'}'
comment|'# { <host> : { <service> : { cap k : v }}}'
newline|'\n'
name|'self'
op|'.'
name|'service_time_stamp'
op|'='
op|'{'
op|'}'
comment|'# reported time'
newline|'\n'
name|'self'
op|'.'
name|'green_pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_zone_list
dedent|''
name|'def'
name|'get_zone_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of zones we know about."""'
newline|'\n'
name|'return'
op|'['
name|'zone'
op|'.'
name|'to_dict'
op|'('
op|')'
name|'for'
name|'zone'
name|'in'
name|'self'
op|'.'
name|'zone_states'
op|'.'
name|'values'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_zone_capabilities
dedent|''
name|'def'
name|'get_zone_capabilities'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Roll up all the individual host info to generic \'service\'\n           capabilities. Each capability is aggregated into\n           <cap>_min and <cap>_max values."""'
newline|'\n'
name|'hosts_dict'
op|'='
name|'self'
op|'.'
name|'service_states'
newline|'\n'
nl|'\n'
comment|'# TODO(sandy) - be smarter about fabricating this structure.'
nl|'\n'
comment|"# But it's likely to change once we understand what the Best-Match"
nl|'\n'
comment|'# code will need better.'
nl|'\n'
name|'combined'
op|'='
op|'{'
op|'}'
comment|'# { <service>_<cap> : (min, max), ... }'
newline|'\n'
name|'allowed_time_diff'
op|'='
name|'FLAGS'
op|'.'
name|'periodic_interval'
op|'*'
number|'3'
newline|'\n'
name|'for'
name|'host'
op|','
name|'host_dict'
name|'in'
name|'hosts_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'self'
op|'.'
name|'service_time_stamp'
op|'['
name|'host'
op|']'
op|')'
op|'<='
name|'datetime'
op|'.'
name|'timedelta'
op|'('
name|'seconds'
op|'='
name|'allowed_time_diff'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'service_name'
op|','
name|'service_dict'
name|'in'
name|'host_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'cap'
op|','
name|'value'
name|'in'
name|'service_dict'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'key'
op|'='
string|'"%s_%s"'
op|'%'
op|'('
name|'service_name'
op|','
name|'cap'
op|')'
newline|'\n'
name|'min_value'
op|','
name|'max_value'
op|'='
name|'combined'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'('
name|'value'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
name|'min_value'
op|'='
name|'min'
op|'('
name|'min_value'
op|','
name|'value'
op|')'
newline|'\n'
name|'max_value'
op|'='
name|'max'
op|'('
name|'max_value'
op|','
name|'value'
op|')'
newline|'\n'
name|'combined'
op|'['
name|'key'
op|']'
op|'='
op|'('
name|'min_value'
op|','
name|'max_value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'combined'
newline|'\n'
nl|'\n'
DECL|member|_refresh_from_db
dedent|''
name|'def'
name|'_refresh_from_db'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make our zone state map match the db."""'
newline|'\n'
comment|'# Add/update existing zones ...'
nl|'\n'
name|'zones'
op|'='
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'existing'
op|'='
name|'self'
op|'.'
name|'zone_states'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'db_keys'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'zone'
name|'in'
name|'zones'
op|':'
newline|'\n'
indent|'            '
name|'db_keys'
op|'.'
name|'append'
op|'('
name|'zone'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'if'
name|'zone'
op|'.'
name|'id'
name|'not'
name|'in'
name|'existing'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'zone_states'
op|'['
name|'zone'
op|'.'
name|'id'
op|']'
op|'='
name|'ZoneState'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'zone_states'
op|'['
name|'zone'
op|'.'
name|'id'
op|']'
op|'.'
name|'update_credentials'
op|'('
name|'zone'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup zones removed from db ...'
nl|'\n'
dedent|''
name|'keys'
op|'='
name|'self'
op|'.'
name|'zone_states'
op|'.'
name|'keys'
op|'('
op|')'
comment|"# since we're deleting"
newline|'\n'
name|'for'
name|'zone_id'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'zone_id'
name|'not'
name|'in'
name|'db_keys'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'zone_states'
op|'['
name|'zone_id'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_poll_zones
dedent|''
dedent|''
dedent|''
name|'def'
name|'_poll_zones'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Try to connect to each child zone and get update."""'
newline|'\n'
name|'self'
op|'.'
name|'green_pool'
op|'.'
name|'imap'
op|'('
name|'_poll_zone'
op|','
name|'self'
op|'.'
name|'zone_states'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ping
dedent|''
name|'def'
name|'ping'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ping should be called periodically to update zone status."""'
newline|'\n'
name|'diff'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'-'
name|'self'
op|'.'
name|'last_zone_db_check'
newline|'\n'
name|'if'
name|'diff'
op|'.'
name|'seconds'
op|'>='
name|'FLAGS'
op|'.'
name|'zone_db_check_interval'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Updating zone cache from db."'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'last_zone_db_check'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_refresh_from_db'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_poll_zones'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Update the per-service capabilities based on this notification."""'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received %(service_name)s service update from "'
nl|'\n'
string|'"%(host)s: %(capabilities)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'service_caps'
op|'='
name|'self'
op|'.'
name|'service_states'
op|'.'
name|'get'
op|'('
name|'host'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'service_caps'
op|'['
name|'service_name'
op|']'
op|'='
name|'capabilities'
newline|'\n'
name|'self'
op|'.'
name|'service_states'
op|'['
name|'host'
op|']'
op|'='
name|'service_caps'
newline|'\n'
name|'self'
op|'.'
name|'service_time_stamp'
op|'['
name|'host'
op|']'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
