begin_unit
comment|'#    Copyright 2015 Red Hat, Inc.'
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
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|RequestSpec
name|'class'
name|'RequestSpec'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: ImageMeta version 1.6'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'image'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ImageMeta'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'InstanceNUMATopology'"
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'InstancePCIRequests'"
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'flavor'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'Flavor'"
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
string|"'num_instances'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'default'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'ignore_hosts'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'force_hosts'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'force_nodes'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'retry'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'SchedulerRetries'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'limits'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'SchedulerLimits'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'instance_group'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'InstanceGroup'"
op|','
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
comment|'# NOTE(sbauza): Since hints are depending on running filters, we prefer'
nl|'\n'
comment|'# to leave the API correctly validating the hints per the filters and'
nl|'\n'
comment|'# just provide to the RequestSpec object a free-form dictionary'
nl|'\n'
string|"'scheduler_hints'"
op|':'
name|'fields'
op|'.'
name|'DictOfListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'image'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.5'"
op|')'
op|','
op|'('
string|"'1.1'"
op|','
string|"'1.6'"
op|')'
op|']'
op|','
nl|'\n'
string|"'numa_topology'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.2'"
op|')'
op|']'
op|','
nl|'\n'
string|"'flavor'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.1'"
op|')'
op|']'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.1'"
op|')'
op|']'
op|','
nl|'\n'
string|"'retry'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
string|"'limits'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
string|"'instance_group'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.9'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|vcpus
name|'def'
name|'vcpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'flavor'
op|'.'
name|'vcpus'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|memory_mb
name|'def'
name|'memory_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'flavor'
op|'.'
name|'memory_mb'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|root_gb
name|'def'
name|'root_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'flavor'
op|'.'
name|'root_gb'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|ephemeral_gb
name|'def'
name|'ephemeral_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'flavor'
op|'.'
name|'ephemeral_gb'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|swap
name|'def'
name|'swap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'flavor'
op|'.'
name|'swap'
newline|'\n'
nl|'\n'
DECL|member|_image_meta_from_image
dedent|''
name|'def'
name|'_image_meta_from_image'
op|'('
name|'self'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'image'
op|','
name|'objects'
op|'.'
name|'ImageMeta'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image'
op|'='
name|'image'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'image'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Until Nova is fully providing an ImageMeta object'
nl|'\n'
comment|'# for getting properties, we still need to hydrate it here'
nl|'\n'
comment|'# TODO(sbauza): To be removed once all RequestSpec hydrations are'
nl|'\n'
comment|'# done on the conductor side and if the image is an ImageMeta'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'image'
op|'='
name|'objects'
op|'.'
name|'ImageMeta'
op|'.'
name|'from_dict'
op|'('
name|'image'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_from_instance
dedent|''
dedent|''
name|'def'
name|'_from_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'objects'
op|'.'
name|'Instance'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Instance should normally be a NovaObject...'
nl|'\n'
indent|'            '
name|'getter'
op|'='
name|'getattr'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): ... but there are some cases where request_spec'
nl|'\n'
comment|'# has an instance key as a dictionary, just because'
nl|'\n'
comment|'# select_destinations() is getting a request_spec dict made by'
nl|'\n'
comment|'# sched_utils.build_request_spec()'
nl|'\n'
comment|'# TODO(sbauza): To be removed once all RequestSpec hydrations are'
nl|'\n'
comment|'# done on the conductor side'
nl|'\n'
indent|'            '
name|'getter'
op|'='
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'x'
op|'.'
name|'get'
op|'('
name|'y'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# If the instance is None, there is no reason to set the fields'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'instance_fields'
op|'='
op|'['
string|"'numa_topology'"
op|','
string|"'pci_requests'"
op|','
string|"'uuid'"
op|','
nl|'\n'
string|"'project_id'"
op|','
string|"'availability_zone'"
op|']'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'instance_fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
op|'=='
string|"'uuid'"
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'self'
op|','
string|"'instance_uuid'"
op|','
name|'getter'
op|'('
name|'instance'
op|','
name|'field'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'self'
op|','
name|'field'
op|','
name|'getter'
op|'('
name|'instance'
op|','
name|'field'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_from_flavor
dedent|''
dedent|''
dedent|''
name|'def'
name|'_from_flavor'
op|'('
name|'self'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'flavor'
op|','
name|'objects'
op|'.'
name|'Flavor'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flavor'
op|'='
name|'flavor'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'flavor'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Again, request_spec is primitived by'
nl|'\n'
comment|'# sched_utils.build_request_spec() and passed to'
nl|'\n'
comment|'# select_destinations() like this'
nl|'\n'
comment|'# TODO(sbauza): To be removed once all RequestSpec hydrations are'
nl|'\n'
comment|'# done on the conductor side'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
op|'**'
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_from_retry
dedent|''
dedent|''
name|'def'
name|'_from_retry'
op|'('
name|'self'
op|','
name|'retry_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'retry'
op|'='
op|'('
name|'SchedulerRetries'
op|'.'
name|'from_dict'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'retry_dict'
op|')'
nl|'\n'
name|'if'
name|'retry_dict'
name|'else'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_populate_group_info
dedent|''
name|'def'
name|'_populate_group_info'
op|'('
name|'self'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_group'"
op|')'
op|':'
newline|'\n'
comment|'# New-style group information as a NovaObject, we can directly set'
nl|'\n'
comment|'# the field'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_group'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_group'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'group_updated'"
op|')'
name|'is'
name|'True'
op|':'
newline|'\n'
comment|'# Old-style group information having ugly dict keys containing sets'
nl|'\n'
comment|'# NOTE(sbauza): Can be dropped once select_destinations is removed'
nl|'\n'
indent|'            '
name|'policies'
op|'='
name|'list'
op|'('
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'group_policies'"
op|')'
op|')'
newline|'\n'
name|'members'
op|'='
name|'list'
op|'('
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'group_hosts'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_group'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Set the value anyway to avoid any call to obj_attr_is_set for it'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_group'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_from_limits
dedent|''
dedent|''
name|'def'
name|'_from_limits'
op|'('
name|'self'
op|','
name|'limits_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'limits'
op|'='
name|'SchedulerLimits'
op|'.'
name|'from_dict'
op|'('
name|'limits_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_from_hints
dedent|''
name|'def'
name|'_from_hints'
op|'('
name|'self'
op|','
name|'hints_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hints_dict'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'scheduler_hints'
op|'='
name|'None'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'scheduler_hints'
op|'='
op|'{'
nl|'\n'
name|'hint'
op|':'
name|'value'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'list'
op|')'
name|'else'
op|'['
name|'value'
op|']'
nl|'\n'
name|'for'
name|'hint'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'hints_dict'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_primitives
name|'def'
name|'from_primitives'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a new RequestSpec object by hydrating it from legacy dicts.\n\n        That helper is not intended to leave the legacy dicts kept in the nova\n        codebase, but is rather just for giving a temporary solution for\n        populating the Spec object until we get rid of scheduler_utils\'\n        build_request_spec() and the filter_properties hydratation in the\n        conductor.\n\n        :param context: a context object\n        :param request_spec: An old-style request_spec dictionary\n        :param filter_properties: An old-style filter_properties dictionary\n        """'
newline|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
name|'spec'
op|'='
name|'cls'
op|'('
name|'context'
op|','
name|'num_instances'
op|'='
name|'num_instances'
op|')'
newline|'\n'
comment|'# Hydrate from request_spec first'
nl|'\n'
name|'image'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_image_meta_from_image'
op|'('
name|'image'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_from_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_from_flavor'
op|'('
name|'flavor'
op|')'
newline|'\n'
comment|'# Hydrate now from filter_properties'
nl|'\n'
name|'spec'
op|'.'
name|'ignore_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'ignore_hosts'"
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'force_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_hosts'"
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'force_nodes'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'force_nodes'"
op|')'
newline|'\n'
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'retry'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_from_retry'
op|'('
name|'retry'
op|')'
newline|'\n'
name|'limits'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'limits'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_from_limits'
op|'('
name|'limits'
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_populate_group_info'
op|'('
name|'filter_properties'
op|')'
newline|'\n'
name|'scheduler_hints'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'scheduler_hints'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'spec'
op|'.'
name|'_from_hints'
op|'('
name|'scheduler_hints'
op|')'
newline|'\n'
name|'return'
name|'spec'
newline|'\n'
nl|'\n'
DECL|member|get_scheduler_hint
dedent|''
name|'def'
name|'get_scheduler_hint'
op|'('
name|'self'
op|','
name|'hint_name'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convenient helper for accessing a particular scheduler hint since\n        it is hydrated by putting a single item into a list.\n\n        In order to reduce the complexity, that helper returns a string if the\n        requested hint is a list of only one value, and if not, returns the\n        value directly (ie. the list). If the hint is not existing (or\n        scheduler_hints is None), then it returns the default value.\n\n        :param hint_name: name of the hint\n        :param default: the default value if the hint is not there\n        """'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'scheduler_hints'"
op|')'
nl|'\n'
name|'or'
name|'self'
op|'.'
name|'scheduler_hints'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'default'
newline|'\n'
dedent|''
name|'hint_val'
op|'='
name|'self'
op|'.'
name|'scheduler_hints'
op|'.'
name|'get'
op|'('
name|'hint_name'
op|','
name|'default'
op|')'
newline|'\n'
name|'return'
op|'('
name|'hint_val'
op|'['
number|'0'
op|']'
name|'if'
name|'isinstance'
op|'('
name|'hint_val'
op|','
name|'list'
op|')'
nl|'\n'
name|'and'
name|'len'
op|'('
name|'hint_val'
op|')'
op|'=='
number|'1'
name|'else'
name|'hint_val'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|SchedulerRetries
name|'class'
name|'SchedulerRetries'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'num_attempts'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
comment|'# NOTE(sbauza): Even if we are only using host/node strings, we need to'
nl|'\n'
comment|'# know which compute nodes were tried'
nl|'\n'
string|"'hosts'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'ComputeNodeList'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'hosts'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.13'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'retry_dict'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(sbauza): We are not persisting the user context since it's only"
nl|'\n'
comment|'# needed for hydrating the Retry object'
nl|'\n'
indent|'        '
name|'retry_obj'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
op|'('
string|"'num_attempts'"
name|'and'
string|"'hosts'"
op|')'
name|'in'
name|'retry_dict'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): We prefer to return an empty object if the'
nl|'\n'
comment|'# primitive is not good enough'
nl|'\n'
indent|'            '
name|'return'
name|'retry_obj'
newline|'\n'
dedent|''
name|'retry_obj'
op|'.'
name|'num_attempts'
op|'='
name|'retry_dict'
op|'.'
name|'get'
op|'('
string|"'num_attempts'"
op|')'
newline|'\n'
comment|"# NOTE(sbauza): each retry_dict['hosts'] item is a list of [host, node]"
nl|'\n'
name|'computes'
op|'='
op|'['
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'context'
op|'='
name|'context'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
name|'node'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'node'
name|'in'
name|'retry_dict'
op|'.'
name|'get'
op|'('
string|"'hosts'"
op|')'
op|']'
newline|'\n'
name|'retry_obj'
op|'.'
name|'hosts'
op|'='
name|'objects'
op|'.'
name|'ComputeNodeList'
op|'('
name|'objects'
op|'='
name|'computes'
op|')'
newline|'\n'
name|'return'
name|'retry_obj'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|SchedulerLimits
name|'class'
name|'SchedulerLimits'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'numa_topology'"
op|':'
name|'fields'
op|'.'
name|'ObjectField'
op|'('
string|"'NUMATopologyLimits'"
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
string|"'vcpu'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_relationships
name|'obj_relationships'
op|'='
op|'{'
nl|'\n'
string|"'numa_topology'"
op|':'
op|'['
op|'('
string|"'1.0'"
op|','
string|"'1.0'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'limits_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'limits'
op|'='
name|'cls'
op|'('
op|'**'
name|'limits_dict'
op|')'
newline|'\n'
comment|'# NOTE(sbauza): Since the limits can be set for each field or not, we'
nl|'\n'
comment|'# prefer to have the fields nullable, but default the value to None.'
nl|'\n'
comment|'# Here we accept that the object is always generated from a primitive'
nl|'\n'
comment|'# hence the use of obj_set_defaults exceptionally.'
nl|'\n'
name|'limits'
op|'.'
name|'obj_set_defaults'
op|'('
op|')'
newline|'\n'
name|'return'
name|'limits'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
