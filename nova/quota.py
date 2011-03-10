begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nQuotas for instances, volumes, and floating ips\n"""'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_instances'"
op|','
number|'10'
op|','
nl|'\n'
string|"'number of instances allowed per project'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_cores'"
op|','
number|'20'
op|','
nl|'\n'
string|"'number of instance cores allowed per project'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_volumes'"
op|','
number|'10'
op|','
nl|'\n'
string|"'number of volumes allowed per project'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_gigabytes'"
op|','
number|'1000'
op|','
nl|'\n'
string|"'number of volume gigabytes allowed per project'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_floating_ips'"
op|','
number|'10'
op|','
nl|'\n'
string|"'number of floating ips allowed per project'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_metadata_items'"
op|','
number|'128'
op|','
nl|'\n'
string|"'number of metadata items allowed per instance'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_max_onset_files'"
op|','
number|'5'
op|','
nl|'\n'
string|"'number of onset files allowed'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_max_onset_file_content_bytes'"
op|','
number|'10'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'number of bytes allowed per onset file'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'quota_max_onset_file_path_bytes'"
op|','
number|'255'
op|','
nl|'\n'
string|"'number of bytes allowed per onset file path'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_quota
name|'def'
name|'get_quota'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rval'
op|'='
op|'{'
string|"'instances'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_instances'
op|','
nl|'\n'
string|"'cores'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_cores'
op|','
nl|'\n'
string|"'volumes'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_volumes'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_gigabytes'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_floating_ips'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'quota'
op|'='
name|'db'
op|'.'
name|'quota_get'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'rval'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'quota'
op|'['
name|'key'
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'rval'
op|'['
name|'key'
op|']'
op|'='
name|'quota'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'rval'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_instances
dedent|''
name|'def'
name|'allowed_instances'
op|'('
name|'context'
op|','
name|'num_instances'
op|','
name|'instance_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check quota and return min(num_instances, allowed_instances)"""'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'used_instances'
op|','
name|'used_cores'
op|'='
name|'db'
op|'.'
name|'instance_data_get_for_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'quota'
op|'='
name|'get_quota'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'allowed_instances'
op|'='
name|'quota'
op|'['
string|"'instances'"
op|']'
op|'-'
name|'used_instances'
newline|'\n'
name|'allowed_cores'
op|'='
name|'quota'
op|'['
string|"'cores'"
op|']'
op|'-'
name|'used_cores'
newline|'\n'
name|'num_cores'
op|'='
name|'num_instances'
op|'*'
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'allowed_instances'
op|'='
name|'min'
op|'('
name|'allowed_instances'
op|','
nl|'\n'
name|'int'
op|'('
name|'allowed_cores'
op|'//'
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'min'
op|'('
name|'num_instances'
op|','
name|'allowed_instances'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_volumes
dedent|''
name|'def'
name|'allowed_volumes'
op|'('
name|'context'
op|','
name|'num_volumes'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check quota and return min(num_volumes, allowed_volumes)"""'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'used_volumes'
op|','
name|'used_gigabytes'
op|'='
name|'db'
op|'.'
name|'volume_data_get_for_project'
op|'('
name|'context'
op|','
nl|'\n'
name|'project_id'
op|')'
newline|'\n'
name|'quota'
op|'='
name|'get_quota'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'allowed_volumes'
op|'='
name|'quota'
op|'['
string|"'volumes'"
op|']'
op|'-'
name|'used_volumes'
newline|'\n'
name|'allowed_gigabytes'
op|'='
name|'quota'
op|'['
string|"'gigabytes'"
op|']'
op|'-'
name|'used_gigabytes'
newline|'\n'
name|'size'
op|'='
name|'int'
op|'('
name|'size'
op|')'
newline|'\n'
name|'num_gigabytes'
op|'='
name|'num_volumes'
op|'*'
name|'size'
newline|'\n'
name|'allowed_volumes'
op|'='
name|'min'
op|'('
name|'allowed_volumes'
op|','
nl|'\n'
name|'int'
op|'('
name|'allowed_gigabytes'
op|'//'
name|'size'
op|')'
op|')'
newline|'\n'
name|'return'
name|'min'
op|'('
name|'num_volumes'
op|','
name|'allowed_volumes'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_floating_ips
dedent|''
name|'def'
name|'allowed_floating_ips'
op|'('
name|'context'
op|','
name|'num_floating_ips'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check quota and return min(num_floating_ips, allowed_floating_ips)"""'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'used_floating_ips'
op|'='
name|'db'
op|'.'
name|'floating_ip_count_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'quota'
op|'='
name|'get_quota'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'allowed_floating_ips'
op|'='
name|'quota'
op|'['
string|"'floating_ips'"
op|']'
op|'-'
name|'used_floating_ips'
newline|'\n'
name|'return'
name|'min'
op|'('
name|'num_floating_ips'
op|','
name|'allowed_floating_ips'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_metadata_items
dedent|''
name|'def'
name|'allowed_metadata_items'
op|'('
name|'context'
op|','
name|'num_metadata_items'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check quota; return min(num_metadata_items,allowed_metadata_items)"""'
newline|'\n'
name|'project_id'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'quota'
op|'='
name|'get_quota'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'num_allowed_metadata_items'
op|'='
name|'quota'
op|'['
string|"'metadata_items'"
op|']'
newline|'\n'
name|'return'
name|'min'
op|'('
name|'num_metadata_items'
op|','
name|'num_allowed_metadata_items'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_onset_files
dedent|''
name|'def'
name|'allowed_onset_files'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of onset files allowed"""'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'FLAGS'
op|'.'
name|'quota_max_onset_files'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_onset_file_content_bytes
dedent|''
name|'def'
name|'allowed_onset_file_content_bytes'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of bytes allowed per onset file content"""'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'FLAGS'
op|'.'
name|'quota_max_onset_file_content_bytes'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|allowed_onset_file_path_bytes
dedent|''
name|'def'
name|'allowed_onset_file_path_bytes'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the number of bytes allowed in an onset file path"""'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'FLAGS'
op|'.'
name|'quota_max_onset_file_path_bytes'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaError
dedent|''
name|'class'
name|'QuotaError'
op|'('
name|'exception'
op|'.'
name|'ApiError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Quota Exceeeded"""'
newline|'\n'
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
