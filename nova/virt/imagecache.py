begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'block_device'
name|'as'
name|'driver_block_device'
newline|'\n'
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
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManager
name|'class'
name|'ImageCacheManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for the image cache manager.\n\n    This class will provide a generic interface to the image cache manager.\n    """'
newline|'\n'
nl|'\n'
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
name|'remove_unused_base_images'
op|'='
name|'CONF'
op|'.'
name|'remove_unused_base_images'
newline|'\n'
name|'self'
op|'.'
name|'resize_states'
op|'='
op|'['
name|'task_states'
op|'.'
name|'RESIZE_PREP'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATED'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_FINISH'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_base
dedent|''
name|'def'
name|'_get_base'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the base directory of the cached images."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_list_running_instances
dedent|''
name|'def'
name|'_list_running_instances'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List running instances (on all compute nodes).\n\n        This method returns a dictionary with the following keys:\n            - used_images\n            - image_popularity\n            - instance_names\n        """'
newline|'\n'
name|'used_images'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'image_popularity'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'instance_names'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'used_swap_images'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'instance_bdms'
op|'='
name|'objects'
op|'.'
name|'BlockDeviceMappingList'
op|'.'
name|'bdms_by_instance_uuid'
op|'('
nl|'\n'
name|'context'
op|','
op|'['
name|'instance'
op|'.'
name|'uuid'
name|'for'
name|'instance'
name|'in'
name|'all_instances'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'all_instances'
op|':'
newline|'\n'
comment|'# NOTE(mikal): "instance name" here means "the name of a directory'
nl|'\n'
comment|'# which might contain an instance" and therefore needs to include'
nl|'\n'
comment|'# historical permutations as well as the current one.'
nl|'\n'
indent|'            '
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'if'
op|'('
name|'instance'
op|'.'
name|'task_state'
name|'in'
name|'self'
op|'.'
name|'resize_states'
name|'or'
nl|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'=='
name|'vm_states'
op|'.'
name|'RESIZED'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'.'
name|'name'
op|'+'
string|"'_resize'"
op|')'
newline|'\n'
name|'instance_names'
op|'.'
name|'add'
op|'('
name|'instance'
op|'.'
name|'uuid'
op|'+'
string|"'_resize'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image_key'
name|'in'
op|'['
string|"'image_ref'"
op|','
string|"'kernel_id'"
op|','
string|"'ramdisk_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'image_ref_str'
op|'='
name|'getattr'
op|'('
name|'instance'
op|','
name|'image_key'
op|')'
newline|'\n'
name|'if'
name|'image_ref_str'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'local'
op|','
name|'remote'
op|','
name|'insts'
op|'='
name|'used_images'
op|'.'
name|'get'
op|'('
name|'image_ref_str'
op|','
nl|'\n'
op|'('
number|'0'
op|','
number|'0'
op|','
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'host'
op|'=='
name|'CONF'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                    '
name|'local'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'remote'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'insts'
op|'.'
name|'append'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'used_images'
op|'['
name|'image_ref_str'
op|']'
op|'='
op|'('
name|'local'
op|','
name|'remote'
op|','
name|'insts'
op|')'
newline|'\n'
nl|'\n'
name|'image_popularity'
op|'.'
name|'setdefault'
op|'('
name|'image_ref_str'
op|','
number|'0'
op|')'
newline|'\n'
name|'image_popularity'
op|'['
name|'image_ref_str'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'bdms'
op|'='
name|'instance_bdms'
op|'.'
name|'get'
op|'('
name|'instance'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'if'
name|'bdms'
op|':'
newline|'\n'
indent|'                '
name|'swap'
op|'='
name|'driver_block_device'
op|'.'
name|'convert_swap'
op|'('
name|'bdms'
op|')'
newline|'\n'
name|'if'
name|'swap'
op|':'
newline|'\n'
indent|'                    '
name|'swap_image'
op|'='
string|"'swap_'"
op|'+'
name|'str'
op|'('
name|'swap'
op|'['
number|'0'
op|']'
op|'['
string|"'swap_size'"
op|']'
op|')'
newline|'\n'
name|'used_swap_images'
op|'.'
name|'add'
op|'('
name|'swap_image'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
op|'{'
string|"'used_images'"
op|':'
name|'used_images'
op|','
nl|'\n'
string|"'image_popularity'"
op|':'
name|'image_popularity'
op|','
nl|'\n'
string|"'instance_names'"
op|':'
name|'instance_names'
op|','
nl|'\n'
string|"'used_swap_images'"
op|':'
name|'used_swap_images'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_list_base_images
dedent|''
name|'def'
name|'_list_base_images'
op|'('
name|'self'
op|','
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of the images present in _base.\n\n        This method returns a dictionary with the following keys:\n            - unexplained_images\n            - originals\n        """'
newline|'\n'
name|'return'
op|'{'
string|"'unexplained_images'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'originals'"
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_age_and_verify_cached_images
dedent|''
name|'def'
name|'_age_and_verify_cached_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|','
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ages and verifies cached images."""'
newline|'\n'
nl|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The cache manager.\n\n        This will invoke the cache manager. This will update the cache\n        according to the defined cache management scheme. The information\n        populated in the cached stats will be used for the cache management.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
