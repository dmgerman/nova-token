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
string|'"""\nThe Zone Aware Scheduler is a base class Scheduler for creating instances\nacross zones. There are two expansion points to this class for:\n1. Assigning Weights to hosts for requested instances\n2. Filtering Hosts based on required instance capabilities\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'operator'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'M2Crypto'
newline|'\n'
name|'import'
name|'novaclient'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'rpc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.zone_aware_scheduler'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidBlob
name|'class'
name|'InvalidBlob'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Ill-formed or incorrectly routed \'blob\' data sent "'
nl|'\n'
string|'"to instance create request."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZoneAwareScheduler
dedent|''
name|'class'
name|'ZoneAwareScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for creating Zone Aware Schedulers."""'
newline|'\n'
nl|'\n'
DECL|member|_call_zone_method
name|'def'
name|'_call_zone_method'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call novaclient zone method. Broken out for testing."""'
newline|'\n'
name|'return'
name|'api'
op|'.'
name|'call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|'='
name|'specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource_locally
dedent|''
name|'def'
name|'_provision_resource_locally'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone."""'
newline|'\n'
name|'host'
op|'='
name|'item'
op|'['
string|"'hostname'"
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'instance_id'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
string|'"compute"'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"run_instance"'
op|','
nl|'\n'
string|'"args"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Provisioning locally via compute node %(host)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_decrypt_blob
dedent|''
name|'def'
name|'_decrypt_blob'
op|'('
name|'self'
op|','
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the decrypted blob or None if invalid. Broken out\n        for testing."""'
newline|'\n'
name|'decryptor'
op|'='
name|'crypto'
op|'.'
name|'decryptor'
op|'('
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'json_entry'
op|'='
name|'decryptor'
op|'('
name|'blob'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'entry'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'M2Crypto'
op|'.'
name|'EVP'
op|'.'
name|'EVPError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_ask_child_zone_to_create_instance
dedent|''
name|'def'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'zone_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Once we have determined that the request should go to one\n        of our children, we need to fabricate a new POST /servers/\n        call with the same parameters that were passed into us.\n\n        Note that we have to reverse engineer from our args to get back the\n        image, flavor, ipgroup, etc. since the original call could have\n        come in from EC2 (which doesn\'t use these things)."""'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'instance_properties'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
newline|'\n'
nl|'\n'
name|'name'
op|'='
name|'instance_properties'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'image_ref'
op|'='
name|'instance_properties'
op|'['
string|"'image_ref'"
op|']'
newline|'\n'
name|'meta'
op|'='
name|'instance_properties'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'flavor_id'
op|'='
name|'instance_type'
op|'['
string|"'flavorid'"
op|']'
newline|'\n'
name|'reservation_id'
op|'='
name|'instance_properties'
op|'['
string|"'reservation_id'"
op|']'
newline|'\n'
nl|'\n'
name|'files'
op|'='
name|'kwargs'
op|'['
string|"'injected_files'"
op|']'
newline|'\n'
name|'ipgroup'
op|'='
name|'None'
comment|'# Not supported in OS API ... yet'
newline|'\n'
nl|'\n'
name|'child_zone'
op|'='
name|'zone_info'
op|'['
string|"'child_zone'"
op|']'
newline|'\n'
name|'child_blob'
op|'='
name|'zone_info'
op|'['
string|"'child_blob'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'db'
op|'.'
name|'zone_get'
op|'('
name|'context'
op|','
name|'child_zone'
op|')'
newline|'\n'
name|'url'
op|'='
name|'zone'
op|'.'
name|'api_url'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Forwarding instance create call to child zone %(url)s"'
nl|'\n'
string|'". ReservationID=%(reservation_id)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'nova'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'nova'
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
name|'url'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'authenticate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'novaclient'
op|'.'
name|'exceptions'
op|'.'
name|'BadRequest'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
op|'('
name|'_'
op|'('
string|'"Bad credentials attempting "'
nl|'\n'
string|'"to talk to zone at %(url)s."'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'nova'
op|'.'
name|'servers'
op|'.'
name|'create'
op|'('
name|'name'
op|','
name|'image_ref'
op|','
name|'flavor_id'
op|','
name|'ipgroup'
op|','
name|'meta'
op|','
name|'files'
op|','
nl|'\n'
name|'child_blob'
op|','
name|'reservation_id'
op|'='
name|'reservation_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource_from_blob
dedent|''
name|'def'
name|'_provision_resource_from_blob'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource locally or in a child zone\n           based on what is stored in the zone blob info.\n\n           Attempt to decrypt the blob to see if this request is:\n           1. valid, and\n           2. intended for this zone or a child zone.\n\n           Note: If we have "blob" that means the request was passed\n           into us from a parent zone. If we have "child_blob" that\n           means we gathered the info from one of our children.\n           It\'s possible that, when we decrypt the \'blob\' field, it\n           contains "child_blob" data. In which case we forward the\n           request."""'
newline|'\n'
nl|'\n'
name|'host_info'
op|'='
name|'None'
newline|'\n'
name|'if'
string|'"blob"'
name|'in'
name|'item'
op|':'
newline|'\n'
comment|'# Request was passed in from above. Is it for us?'
nl|'\n'
indent|'            '
name|'host_info'
op|'='
name|'self'
op|'.'
name|'_decrypt_blob'
op|'('
name|'item'
op|'['
string|"'blob'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|'"child_blob"'
name|'in'
name|'item'
op|':'
newline|'\n'
comment|'# Our immediate child zone provided this info ...'
nl|'\n'
indent|'            '
name|'host_info'
op|'='
name|'item'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'host_info'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidBlob'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Valid data ... is it for us?'
nl|'\n'
dedent|''
name|'if'
string|"'child_zone'"
name|'in'
name|'host_info'
name|'and'
string|"'child_blob'"
name|'in'
name|'host_info'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_ask_child_zone_to_create_instance'
op|'('
name|'context'
op|','
name|'host_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource_locally'
op|'('
name|'context'
op|','
name|'host_info'
op|','
nl|'\n'
name|'instance_id'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource
dedent|''
dedent|''
name|'def'
name|'_provision_resource'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone or a child zone."""'
newline|'\n'
name|'if'
string|'"hostname"'
name|'in'
name|'item'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource_locally'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called from nova.compute.api to provision\n        an instance. However we need to look at the parameters being\n        passed in to see if this is a request to:\n        1. Create a Build Plan and then provision, or\n        2. Use the Build Plan information in the request parameters\n           to simply create the instance (either in this zone or\n           a child zone).\n        """'
newline|'\n'
nl|'\n'
comment|"# TODO(sandy): We'll have to look for richer specs at some point."
nl|'\n'
nl|'\n'
name|'blob'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'blob'"
op|')'
newline|'\n'
name|'if'
name|'blob'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# Create build plan and provision ...'
nl|'\n'
dedent|''
name|'build_plan'
op|'='
name|'self'
op|'.'
name|'select'
op|'('
name|'context'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'build_plan'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
name|'_'
op|'('
string|"'No hosts were available'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'request_spec'
op|'['
string|"'num_instances'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'build_plan'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'item'
op|'='
name|'build_plan'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'instance_id'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Returning None short-circuits the routing to Compute (since'
nl|'\n'
comment|"# we've already done it here)"
nl|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
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
string|'"""Select returns a list of weights and zone/host information\n        corresponding to the best hosts to service the request. Any\n        child zone information has been encrypted so as not to reveal\n        anything about the children.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|'"compute"'
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(sandy): We're only focused on compute instances right now,"
nl|'\n'
comment|'# so we don\'t implement the default "schedule()" method required'
nl|'\n'
comment|'# of Schedulers.'
nl|'\n'
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'request_spec'
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
string|'"""The schedule() contract requires we return the one\n        best-suited host for this request.\n        """'
newline|'\n'
name|'raise'
name|'driver'
op|'.'
name|'NoValidHost'
op|'('
name|'_'
op|'('
string|"'No hosts were available'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'request_spec'
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
string|'"""Returns a list of hosts that meet the required specs,\n        ordered by their fitness.\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'topic'
op|'!='
string|'"compute"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplemented'
op|'('
name|'_'
op|'('
string|'"Zone Aware Scheduler only understands "'
nl|'\n'
string|'"Compute nodes (for now)"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'num_instances'
op|'='
name|'request_spec'
op|'['
string|"'num_instances'"
op|']'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
nl|'\n'
name|'weighted'
op|'='
op|'['
op|']'
newline|'\n'
name|'host_list'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
comment|'# Filter local hosts based on requirements ...'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# The first pass through here will pass 'None' as the"
nl|'\n'
comment|'# host_list.. which tells the filter to build the full'
nl|'\n'
comment|'# list of hosts.'
nl|'\n'
comment|'# On a 2nd pass, the filter can modify the host_list with'
nl|'\n'
comment|'# any updates it needs to make based on resources that'
nl|'\n'
comment|'# may have been consumed from a previous build..'
nl|'\n'
indent|'            '
name|'host_list'
op|'='
name|'self'
op|'.'
name|'filter_hosts'
op|'('
name|'topic'
op|','
name|'request_spec'
op|','
name|'host_list'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'host_list'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
comment|'# then weigh the selected hosts.'
nl|'\n'
comment|'# weighted = [{weight=weight, hostname=hostname,'
nl|'\n'
comment|'#              capabilities=capabs}, ...]'
nl|'\n'
dedent|''
name|'weights'
op|'='
name|'self'
op|'.'
name|'weigh_hosts'
op|'('
name|'topic'
op|','
name|'request_spec'
op|','
name|'host_list'
op|')'
newline|'\n'
name|'weights'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'itemgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'best_weight'
op|'='
name|'weights'
op|'['
number|'0'
op|']'
newline|'\n'
name|'weighted'
op|'.'
name|'append'
op|'('
name|'best_weight'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'consume_resources'
op|'('
name|'topic'
op|','
name|'best_weight'
op|'['
string|"'capabilities'"
op|']'
op|','
nl|'\n'
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
comment|'# Next, tack on the best weights from the child zones ...'
nl|'\n'
dedent|''
name|'json_spec'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'request_spec'
op|')'
newline|'\n'
name|'child_results'
op|'='
name|'self'
op|'.'
name|'_call_zone_method'
op|'('
name|'context'
op|','
string|'"select"'
op|','
nl|'\n'
name|'specs'
op|'='
name|'json_spec'
op|')'
newline|'\n'
name|'for'
name|'child_zone'
op|','
name|'result'
name|'in'
name|'child_results'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'weighting'
name|'in'
name|'result'
op|':'
newline|'\n'
comment|'# Remember the child_zone so we can get back to'
nl|'\n'
comment|'# it later if needed. This implicitly builds a zone'
nl|'\n'
comment|'# path structure.'
nl|'\n'
indent|'                '
name|'host_dict'
op|'='
op|'{'
string|'"weight"'
op|':'
name|'weighting'
op|'['
string|'"weight"'
op|']'
op|','
nl|'\n'
string|'"child_zone"'
op|':'
name|'child_zone'
op|','
nl|'\n'
string|'"child_blob"'
op|':'
name|'weighting'
op|'['
string|'"blob"'
op|']'
op|'}'
newline|'\n'
name|'weighted'
op|'.'
name|'append'
op|'('
name|'host_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'weighted'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'itemgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'weighted'
newline|'\n'
nl|'\n'
DECL|member|compute_filter
dedent|''
name|'def'
name|'compute_filter'
op|'('
name|'self'
op|','
name|'hostname'
op|','
name|'capabilities'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return whether or not we can schedule to this compute node.\n        Derived classes should override this and return True if the host\n        is acceptable for scheduling.\n        """'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'reqested_mem'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'return'
name|'capabilities'
op|'['
string|"'host_memory_free'"
op|']'
op|'>='
name|'requested_mem'
newline|'\n'
nl|'\n'
DECL|member|filter_hosts
dedent|''
name|'def'
name|'filter_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'host_list'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of hosts which are acceptable for scheduling.\n        Return value should be a list of (hostname, capability_dict)s.\n        Derived classes may override this, but may find the\n        \'<topic>_filter\' function more appropriate.\n        """'
newline|'\n'
nl|'\n'
DECL|function|_default_filter
name|'def'
name|'_default_filter'
op|'('
name|'self'
op|','
name|'hostname'
op|','
name|'capabilities'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Default filter function if there\'s no <topic>_filter"""'
newline|'\n'
comment|'# NOTE(sirp): The default logic is the equivalent to'
nl|'\n'
comment|'# AllHostsFilter'
nl|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'filter_func'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'%s_filter'"
op|'%'
name|'topic'
op|','
name|'_default_filter'
op|')'
newline|'\n'
nl|'\n'
name|'filtered_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'host_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'host_list'
op|'='
name|'self'
op|'.'
name|'zone_manager'
op|'.'
name|'service_states'
op|'.'
name|'iteritems'
op|'('
op|')'
newline|'\n'
dedent|''
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'host_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'topic'
name|'not'
name|'in'
name|'services'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'filter_func'
op|'('
name|'host'
op|','
name|'services'
op|'['
string|"'topic'"
op|']'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'filtered_hosts'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'services'
op|'['
string|"'topic'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'filtered_hosts'
newline|'\n'
nl|'\n'
DECL|member|weigh_hosts
dedent|''
name|'def'
name|'weigh_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Derived classes may override this to provide more sophisticated\n        scheduling objectives\n        """'
newline|'\n'
comment|'# NOTE(sirp): The default logic is the same as the NoopCostFunction'
nl|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'hostname'
op|'='
name|'hostname'
op|','
name|'capabilities'
op|'='
name|'capabilities'
op|')'
nl|'\n'
name|'for'
name|'hostname'
op|','
name|'capabilities'
name|'in'
name|'hosts'
op|']'
newline|'\n'
nl|'\n'
DECL|member|compute_consume
dedent|''
name|'def'
name|'compute_consume'
op|'('
name|'self'
op|','
name|'capabilities'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consume compute resources for selected host"""'
newline|'\n'
nl|'\n'
name|'requested_mem'
op|'='
name|'max'
op|'('
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'capabilities'
op|'['
string|"'host_memory_free'"
op|']'
op|'-='
name|'requested_mem'
newline|'\n'
nl|'\n'
DECL|member|consume_resources
dedent|''
name|'def'
name|'consume_resources'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'capabilities'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Consume resources for a specific host.  \'host\' is a tuple\n        of the hostname and the services"""'
newline|'\n'
nl|'\n'
name|'consume_func'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'%s_consume'"
op|'%'
name|'topic'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'consume_func'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'consume_func'
op|'('
name|'capabilities'
op|','
name|'instance_type'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
