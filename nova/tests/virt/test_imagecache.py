begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'imagecache'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManagerTests
name|'class'
name|'ImageCacheManagerTests'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_configurationi_defaults
indent|'    '
name|'def'
name|'test_configurationi_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'image_cache_manager_interval'
op|','
nl|'\n'
number|'2400'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'image_cache_subdirectory_name'
op|','
nl|'\n'
string|"'_base'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'CONF'
op|'.'
name|'remove_unused_base_images'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'remove_unused_original_minimum_age_seconds'
op|','
nl|'\n'
number|'24'
op|'*'
number|'3600'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache_manager
dedent|''
name|'def'
name|'test_cache_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cache_manager'
op|'='
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'cache_manager'
op|'.'
name|'remove_unused_base_images'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'cache_manager'
op|'.'
name|'update'
op|','
name|'None'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'cache_manager'
op|'.'
name|'_get_base'
op|')'
newline|'\n'
name|'base_images'
op|'='
name|'cache_manager'
op|'.'
name|'_list_base_images'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base_images'
op|'['
string|"'unexplained_images'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base_images'
op|'['
string|"'originals'"
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'cache_manager'
op|'.'
name|'_age_and_verify_cached_images'
op|','
nl|'\n'
name|'None'
op|','
op|'['
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_running_instances
dedent|''
name|'def'
name|'test_list_running_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'all_instances'
op|'='
op|'['
op|'{'
string|"'image_ref'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'123'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-2'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'456'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'21'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'22'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'remotehost'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-3'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'789'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'image_cache_manager'
op|'='
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# The argument here should be a context, but it's mocked out"
nl|'\n'
name|'running'
op|'='
name|'image_cache_manager'
op|'.'
name|'_list_running_instances'
op|'('
name|'None'
op|','
nl|'\n'
name|'all_instances'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'['
string|"'1'"
op|']'
op|','
op|'('
number|'1'
op|','
number|'0'
op|','
op|'['
string|"'inst-1'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'['
string|"'2'"
op|']'
op|','
op|'('
number|'1'
op|','
number|'1'
op|','
op|'['
string|"'inst-2'"
op|','
nl|'\n'
string|"'inst-3'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'['
string|"'21'"
op|']'
op|','
op|'('
number|'0'
op|','
number|'1'
op|','
op|'['
string|"'inst-3'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'['
string|"'22'"
op|']'
op|','
op|'('
number|'0'
op|','
number|'1'
op|','
op|'['
string|"'inst-3'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'inst-1'"
op|','
name|'running'
op|'['
string|"'instance_names'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'123'"
op|','
name|'running'
op|'['
string|"'instance_names'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|'['
string|"'1'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|'['
string|"'2'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|'['
string|"'21'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|'['
string|"'22'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_resizing_instances
dedent|''
name|'def'
name|'test_list_resizing_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'all_instances'
op|'='
op|'['
op|'{'
string|"'image_ref'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'123'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'RESIZED'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'image_cache_manager'
op|'='
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|'('
op|')'
newline|'\n'
name|'running'
op|'='
name|'image_cache_manager'
op|'.'
name|'_list_running_instances'
op|'('
name|'None'
op|','
nl|'\n'
name|'all_instances'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'running'
op|'['
string|"'used_images'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
number|'1'
op|','
number|'0'
op|','
op|'['
string|"'inst-1'"
op|']'
op|')'
op|','
name|'running'
op|'['
string|"'used_images'"
op|']'
op|'['
string|"'1'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
string|"'inst-1'"
op|','
string|"'123'"
op|','
string|"'inst-1_resize'"
op|','
string|"'123_resize'"
op|']'
op|')'
op|','
nl|'\n'
name|'running'
op|'['
string|"'instance_names'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'running'
op|'['
string|"'image_popularity'"
op|']'
op|'['
string|"'1'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
