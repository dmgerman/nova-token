begin_unit
comment|'#!/usr/bin/python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Michael Still and Canonical Inc'
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
string|'"""Image cache manager.\n\nThe cache manager implements the specification at\nhttp://wiki.openstack.org/nova-image-cache-management.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'db_context'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'virtutils'
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
DECL|variable|imagecache_opts
name|'imagecache_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'remove_unused_base_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Should unused base images be removed?'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'remove_unused_resized_minimum_age_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Unused resized base images younger than this will not be '"
nl|'\n'
string|"'removed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'remove_unused_original_minimum_age_seconds'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'('
number|'24'
op|'*'
number|'3600'
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Unused unresized base images younger than this will not '"
nl|'\n'
string|"'be removed'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'checksum_base_images'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Write a checksum for files in _base to disk'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'imagecache_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|read_stored_checksum
name|'def'
name|'read_stored_checksum'
op|'('
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read the checksum which was created at image fetch time.\n\n    Returns the checksum (as hex) or None.\n    """'
newline|'\n'
name|'checksum_file'
op|'='
string|"'%s.sha1'"
op|'%'
name|'base_file'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'checksum_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'='
name|'open'
op|'('
name|'checksum_file'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'stored_checksum'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'rstrip'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'stored_checksum'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_stored_checksum
dedent|''
name|'def'
name|'write_stored_checksum'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Write a checksum to disk for a file in _base."""'
newline|'\n'
nl|'\n'
name|'checksum_filename'
op|'='
string|"'%s.sha1'"
op|'%'
name|'target'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'target'
op|')'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'checksum_filename'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): Create the checksum file first to exclude possible'
nl|'\n'
comment|'# overlap in checksum operations. An empty checksum file is ignored if'
nl|'\n'
comment|'# encountered during verification.'
nl|'\n'
indent|'        '
name|'sum_file'
op|'='
name|'open'
op|'('
name|'checksum_filename'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'img_file'
op|'='
name|'open'
op|'('
name|'target'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'checksum'
op|'='
name|'utils'
op|'.'
name|'hash_file'
op|'('
name|'img_file'
op|')'
newline|'\n'
name|'img_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sum_file'
op|'.'
name|'write'
op|'('
name|'checksum'
op|')'
newline|'\n'
name|'sum_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManager
dedent|''
dedent|''
name|'class'
name|'ImageCacheManager'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_reset_state'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_state
dedent|''
name|'def'
name|'_reset_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reset state variables used for each pass."""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'used_images'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'image_popularity'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_names'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'active_base_files'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'corrupt_base_files'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'originals'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'removable_base_files'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'unexplained_images'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_store_image
dedent|''
name|'def'
name|'_store_image'
op|'('
name|'self'
op|','
name|'base_dir'
op|','
name|'ent'
op|','
name|'original'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Store a base image for later examination."""'
newline|'\n'
name|'entpath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'ent'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'entpath'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unexplained_images'
op|'.'
name|'append'
op|'('
name|'entpath'
op|')'
newline|'\n'
name|'if'
name|'original'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'originals'
op|'.'
name|'append'
op|'('
name|'entpath'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_list_base_images
dedent|''
dedent|''
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
string|'"""Return a list of the images present in _base.\n\n        Determine what images we have on disk. There will be other files in\n        this directory (for example kernels) so we only grab the ones which\n        are the right length to be disk images.\n\n        Note that this does not return a value. It instead populates a class\n        variable with a list of images that we need to try and explain.\n        """'
newline|'\n'
name|'digest_size'
op|'='
name|'hashlib'
op|'.'
name|'sha1'
op|'('
op|')'
op|'.'
name|'digestsize'
op|'*'
number|'2'
newline|'\n'
name|'for'
name|'ent'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'ent'
op|')'
op|'=='
name|'digest_size'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_store_image'
op|'('
name|'base_dir'
op|','
name|'ent'
op|','
name|'original'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
op|'('
name|'len'
op|'('
name|'ent'
op|')'
op|'>'
name|'digest_size'
op|'+'
number|'2'
name|'and'
nl|'\n'
name|'ent'
op|'['
name|'digest_size'
op|']'
op|'=='
string|"'_'"
name|'and'
nl|'\n'
name|'not'
name|'ent'
op|'.'
name|'endswith'
op|'('
string|"'.sha1'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_store_image'
op|'('
name|'base_dir'
op|','
name|'ent'
op|','
name|'original'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_list_running_instances
dedent|''
dedent|''
dedent|''
name|'def'
name|'_list_running_instances'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List running instances (on all compute nodes)."""'
newline|'\n'
name|'self'
op|'.'
name|'used_images'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'image_popularity'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_names'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_names'
op|'['
name|'instance'
op|'['
string|"'name'"
op|']'
op|']'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
nl|'\n'
name|'image_ref_str'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
name|'local'
op|','
name|'remote'
op|','
name|'insts'
op|'='
name|'self'
op|'.'
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
op|'['
string|"'host'"
op|']'
op|'=='
name|'FLAGS'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'                '
name|'local'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
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
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'image_popularity'
op|'.'
name|'setdefault'
op|'('
name|'image_ref_str'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'image_popularity'
op|'['
name|'image_ref_str'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_list_backing_images
dedent|''
dedent|''
name|'def'
name|'_list_backing_images'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List the backing images currently in use."""'
newline|'\n'
name|'inuse_images'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ent'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ent'
name|'in'
name|'self'
op|'.'
name|'instance_names'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%s is a valid instance name'"
op|')'
op|','
name|'ent'
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
name|'ent'
op|','
string|"'disk'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'disk_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%s has a disk file'"
op|')'
op|','
name|'ent'
op|')'
newline|'\n'
name|'backing_file'
op|'='
name|'virtutils'
op|'.'
name|'get_disk_backing_file'
op|'('
name|'disk_path'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Instance %(instance)s is backed by '"
nl|'\n'
string|"'%(backing)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance'"
op|':'
name|'ent'
op|','
nl|'\n'
string|"'backing'"
op|':'
name|'backing_file'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'backing_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
nl|'\n'
string|"'_base'"
op|','
name|'backing_file'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'backing_path'
name|'in'
name|'inuse_images'
op|':'
newline|'\n'
indent|'                        '
name|'inuse_images'
op|'.'
name|'append'
op|'('
name|'backing_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'backing_path'
name|'in'
name|'self'
op|'.'
name|'unexplained_images'
op|':'
newline|'\n'
indent|'                        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Instance %(instance)s is using a '"
nl|'\n'
string|"'backing file %(backing)s which does '"
nl|'\n'
string|"'not appear in the image service'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance'"
op|':'
name|'ent'
op|','
nl|'\n'
string|"'backing'"
op|':'
name|'backing_file'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unexplained_images'
op|'.'
name|'remove'
op|'('
name|'backing_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'inuse_images'
newline|'\n'
nl|'\n'
DECL|member|_find_base_file
dedent|''
name|'def'
name|'_find_base_file'
op|'('
name|'self'
op|','
name|'base_dir'
op|','
name|'fingerprint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find the base file matching this fingerprint.\n\n        Yields the name of the base file, a boolean which is True if the image\n        is "small", and a boolean which indicates if this is a resized image.\n        Note that is is possible for more than one yield to result from this\n        check.\n\n        If no base file is found, then nothing is yielded.\n        """'
newline|'\n'
comment|'# The original file from glance'
nl|'\n'
name|'base_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'fingerprint'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'base_file'
op|','
name|'False'
op|','
name|'False'
newline|'\n'
nl|'\n'
comment|'# An older naming style which can be removed sometime after Folsom'
nl|'\n'
dedent|''
name|'base_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base_dir'
op|','
name|'fingerprint'
op|'+'
string|"'_sm'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'base_file'
op|','
name|'True'
op|','
name|'False'
newline|'\n'
nl|'\n'
comment|'# Resized images'
nl|'\n'
dedent|''
name|'resize_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'.*/%s_[0-9]+$'"
op|'%'
name|'fingerprint'
op|')'
newline|'\n'
name|'for'
name|'img'
name|'in'
name|'self'
op|'.'
name|'unexplained_images'
op|':'
newline|'\n'
indent|'            '
name|'m'
op|'='
name|'resize_re'
op|'.'
name|'match'
op|'('
name|'img'
op|')'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'img'
op|','
name|'False'
op|','
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_verify_checksum
dedent|''
dedent|''
dedent|''
name|'def'
name|'_verify_checksum'
op|'('
name|'self'
op|','
name|'img_id'
op|','
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compare the checksum stored on disk with the current file.\n\n        Note that if the checksum fails to verify this is logged, but no actual\n        action occurs. This is something sysadmins should monitor for and\n        handle manually when it occurs.\n        """'
newline|'\n'
nl|'\n'
name|'stored_checksum'
op|'='
name|'read_stored_checksum'
op|'('
name|'base_file'
op|')'
newline|'\n'
name|'if'
name|'stored_checksum'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'open'
op|'('
name|'base_file'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'current_checksum'
op|'='
name|'utils'
op|'.'
name|'hash_file'
op|'('
name|'f'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'current_checksum'
op|'!='
name|'stored_checksum'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): image verification '"
nl|'\n'
string|"'failed'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): image verification skipped, '"
nl|'\n'
string|"'no hash stored'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mikal): If the checksum file is missing, then we should'
nl|'\n'
comment|"# create one. We don't create checksums when we download images"
nl|'\n'
comment|'# from glance because that would delay VM startup.'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'checksum_base_images'
op|':'
newline|'\n'
indent|'                '
name|'write_stored_checksum'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_remove_base_file
dedent|''
dedent|''
name|'def'
name|'_remove_base_file'
op|'('
name|'self'
op|','
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a single base file if it is old enough.\n\n        Returns nothing.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Cannot remove %(base_file)s, it does not exist'"
op|')'
op|','
nl|'\n'
name|'base_file'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'mtime'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getmtime'
op|'('
name|'base_file'
op|')'
newline|'\n'
name|'age'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'mtime'
newline|'\n'
nl|'\n'
name|'maxage'
op|'='
name|'FLAGS'
op|'.'
name|'remove_unused_resized_minimum_age_seconds'
newline|'\n'
name|'if'
name|'base_file'
name|'in'
name|'self'
op|'.'
name|'originals'
op|':'
newline|'\n'
indent|'            '
name|'maxage'
op|'='
name|'FLAGS'
op|'.'
name|'remove_unused_original_minimum_age_seconds'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'age'
op|'<'
name|'maxage'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Base file too young to remove: %s'"
op|')'
op|','
nl|'\n'
name|'base_file'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Removing base file: %s'"
op|')'
op|','
name|'base_file'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'remove'
op|'('
name|'base_file'
op|')'
newline|'\n'
name|'signature'
op|'='
name|'base_file'
op|'+'
string|"'.sha1'"
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'signature'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'remove'
op|'('
name|'signature'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to remove %(base_file)s, '"
nl|'\n'
string|"'error was %(error)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'base_file'"
op|':'
name|'base_file'
op|','
nl|'\n'
string|"'error'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_handle_base_image
dedent|''
dedent|''
dedent|''
name|'def'
name|'_handle_base_image'
op|'('
name|'self'
op|','
name|'img_id'
op|','
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Handle the checks for a single base image."""'
newline|'\n'
nl|'\n'
name|'image_bad'
op|'='
name|'False'
newline|'\n'
name|'image_in_use'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): checking'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'base_file'
name|'in'
name|'self'
op|'.'
name|'unexplained_images'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unexplained_images'
op|'.'
name|'remove'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'base_file'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_file'
op|')'
nl|'\n'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'base_file'
op|')'
op|')'
op|':'
newline|'\n'
comment|'# _verify_checksum returns True if the checksum is ok, and None if'
nl|'\n'
comment|'# there is no checksum file'
nl|'\n'
indent|'            '
name|'checksum_result'
op|'='
name|'self'
op|'.'
name|'_verify_checksum'
op|'('
name|'img_id'
op|','
name|'base_file'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'checksum_result'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'image_bad'
op|'='
name|'not'
name|'checksum_result'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'img_id'
name|'in'
name|'self'
op|'.'
name|'used_images'
op|':'
newline|'\n'
indent|'            '
name|'local'
op|','
name|'remote'
op|','
name|'instances'
op|'='
name|'self'
op|'.'
name|'used_images'
op|'['
name|'img_id'
op|']'
newline|'\n'
name|'if'
name|'local'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): '"
nl|'\n'
string|"'in use: on this node %(local)d local, '"
nl|'\n'
string|"'%(remote)d on other nodes'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|','
nl|'\n'
string|"'local'"
op|':'
name|'local'
op|','
nl|'\n'
string|"'remote'"
op|':'
name|'remote'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'image_in_use'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'active_base_files'
op|'.'
name|'append'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'base_file'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): warning -- an '"
nl|'\n'
string|"'absent base file is in use! instances: '"
nl|'\n'
string|"'%(instance_list)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|','
nl|'\n'
string|"'instance_list'"
op|':'
string|"' '"
op|'.'
name|'join'
op|'('
name|'instances'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): in use on (%(remote)d on '"
nl|'\n'
string|"'other nodes)'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|','
nl|'\n'
string|"'remote'"
op|':'
name|'remote'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'image_bad'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'corrupt_base_files'
op|'.'
name|'append'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'base_file'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'image_in_use'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): image is not in use'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'removable_base_files'
op|'.'
name|'append'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%(id)s (%(base_file)s): image is in use'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img_id'
op|','
nl|'\n'
string|"'base_file'"
op|':'
name|'base_file'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_file'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'virtutils'
op|'.'
name|'chown'
op|'('
name|'base_file'
op|','
name|'os'
op|'.'
name|'getuid'
op|'('
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'utime'
op|'('
name|'base_file'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|verify_base_images
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'verify_base_images'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify that base images are in a reasonable state."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(mikal): The new scheme for base images is as follows -- an'
nl|'\n'
comment|'# image is streamed from the image service to _base (filename is the'
nl|'\n'
comment|'# sha1 hash of the image id). If CoW is enabled, that file is then'
nl|'\n'
comment|'# resized to be the correct size for the instance (filename is the'
nl|'\n'
comment|'# same as the original, but with an underscore and the resized size'
nl|'\n'
comment|"# in bytes). This second file is then CoW'd to the instance disk. If"
nl|'\n'
comment|'# CoW is disabled, the resize occurs as part of the copy from the'
nl|'\n'
comment|'# cache to the instance directory. Files ending in _sm are no longer'
nl|'\n'
comment|'# created, but may remain from previous versions.'
nl|'\n'
name|'self'
op|'.'
name|'_reset_state'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'base_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'instances_path'
op|','
string|"'_base'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_dir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Skipping verification, no base directory at %s'"
op|')'
op|','
nl|'\n'
name|'base_dir'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Verify base images'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_list_base_images'
op|'('
name|'base_dir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_list_running_instances'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
comment|"# Determine what images are on disk because they're in use"
nl|'\n'
name|'for'
name|'img'
name|'in'
name|'self'
op|'.'
name|'used_images'
op|':'
newline|'\n'
indent|'            '
name|'fingerprint'
op|'='
name|'hashlib'
op|'.'
name|'sha1'
op|'('
name|'img'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Image id %(id)s yields fingerprint %(fingerprint)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
name|'img'
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
name|'fingerprint'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'result'
name|'in'
name|'self'
op|'.'
name|'_find_base_file'
op|'('
name|'base_dir'
op|','
name|'fingerprint'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'base_file'
op|','
name|'image_small'
op|','
name|'image_resized'
op|'='
name|'result'
newline|'\n'
name|'self'
op|'.'
name|'_handle_base_image'
op|'('
name|'img'
op|','
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image_small'
name|'and'
name|'not'
name|'image_resized'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'originals'
op|'.'
name|'append'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
comment|'# Elements remaining in unexplained_images might be in use'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'inuse_backing_images'
op|'='
name|'self'
op|'.'
name|'_list_backing_images'
op|'('
op|')'
newline|'\n'
name|'for'
name|'backing_path'
name|'in'
name|'inuse_backing_images'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'backing_path'
name|'in'
name|'self'
op|'.'
name|'active_base_files'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'active_base_files'
op|'.'
name|'append'
op|'('
name|'backing_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Anything left is an unknown base image'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'img'
name|'in'
name|'self'
op|'.'
name|'unexplained_images'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Unknown base file: %s'"
op|')'
op|','
name|'img'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'removable_base_files'
op|'.'
name|'append'
op|'('
name|'img'
op|')'
newline|'\n'
nl|'\n'
comment|'# Dump these lists'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'active_base_files'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Active base files: %s'"
op|')'
op|','
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'active_base_files'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'corrupt_base_files'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Corrupt base files: %s'"
op|')'
op|','
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'corrupt_base_files'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'removable_base_files'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Removable base files: %s'"
op|')'
op|','
nl|'\n'
string|"' '"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'removable_base_files'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'remove_unused_base_images'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'base_file'
name|'in'
name|'self'
op|'.'
name|'removable_base_files'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_remove_base_file'
op|'('
name|'base_file'
op|')'
newline|'\n'
nl|'\n'
comment|"# That's it"
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Verification complete'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
