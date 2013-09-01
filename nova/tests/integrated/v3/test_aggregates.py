begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregatesSampleJsonTest
name|'class'
name|'AggregatesSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-aggregates"'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_create
name|'def'
name|'test_aggregate_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"aggregate_id"'
op|':'
string|"'(?P<id>\\d+)'"
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates'"
op|','
string|"'aggregate-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregate-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'201'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_aggregates
dedent|''
name|'def'
name|'test_list_aggregates'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-aggregates'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-list-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_aggregate_get
dedent|''
name|'def'
name|'test_aggregate_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-aggregates/%s'"
op|'%'
name|'agg_id'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_metadata
dedent|''
name|'def'
name|'test_add_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agg_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/%s/action'"
op|'%'
name|'agg_id'
op|','
nl|'\n'
string|"'aggregate-metadata-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'set_metadata'"
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-metadata-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_host
dedent|''
name|'def'
name|'test_add_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"host_name"'
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/%s/action'"
op|'%'
name|'aggregate_id'
op|','
nl|'\n'
string|"'aggregate-add-host-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-add-host-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_host
dedent|''
name|'def'
name|'test_remove_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_add_host'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|'"host_name"'
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-aggregates/1/action'"
op|','
nl|'\n'
string|"'aggregate-remove-host-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregates-remove-host-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_aggregate
dedent|''
name|'def'
name|'test_update_aggregate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'aggregate_id'
op|'='
name|'self'
op|'.'
name|'test_aggregate_create'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-aggregates/%s'"
op|'%'
name|'aggregate_id'
op|','
nl|'\n'
string|"'aggregate-update-post-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'aggregate-update-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregatesSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'AggregatesSampleXmlTest'
op|'('
name|'AggregatesSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
dedent|''
endmarker|''
end_unit
