begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'cache_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestOsloCache
name|'class'
name|'TestOsloCache'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_default_cache_region
indent|'    '
name|'def'
name|'test_get_default_cache_region'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'region'
op|'='
name|'cache_utils'
op|'.'
name|'_get_default_cache_region'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'60'
op|','
name|'region'
op|'.'
name|'expiration_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'region'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_default_cache_region_default_expiration_time
dedent|''
name|'def'
name|'test_get_default_cache_region_default_expiration_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'region'
op|'='
name|'cache_utils'
op|'.'
name|'_get_default_cache_region'
op|'('
name|'expiration_time'
op|'='
number|'0'
op|')'
newline|'\n'
comment|'# default oslo.cache expiration_time value 600 was taken'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'600'
op|','
name|'region'
op|'.'
name|'expiration_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'region'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'dogpile.cache.region.CacheRegion.configure'"
op|')'
newline|'\n'
DECL|member|test_get_client
name|'def'
name|'test_get_client'
op|'('
name|'self'
op|','
name|'mock_cacheregion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
op|'['
string|"'localhost:11211'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'cache'"
op|','
name|'enabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'cache'"
op|','
name|'enabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'client'
op|'='
name|'cache_utils'
op|'.'
name|'get_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'client'
op|'.'
name|'region'
op|')'
newline|'\n'
nl|'\n'
name|'mock_cacheregion'
op|'.'
name|'assert_has_calls'
op|'('
nl|'\n'
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'oslo_cache.dict'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'expiration_time'"
op|':'
number|'60'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.memcached'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'url'"
op|':'
op|'['
string|"'localhost:11211'"
op|']'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.null'"
op|','
nl|'\n'
name|'_config_argument_dict'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'_config_prefix'
op|'='
string|"'cache.oslo.arguments.'"
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|','
nl|'\n'
name|'wrap'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'oslo_cache.dict'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'expiration_time'"
op|':'
number|'60'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
op|']'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'dogpile.cache.region.CacheRegion.configure'"
op|')'
newline|'\n'
DECL|member|test_get_custom_cache_region
name|'def'
name|'test_get_custom_cache_region'
op|'('
name|'self'
op|','
name|'mock_cacheregion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RuntimeError'
op|','
nl|'\n'
name|'cache_utils'
op|'.'
name|'_get_custom_cache_region'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'_get_custom_cache_region'
op|'('
nl|'\n'
name|'backend'
op|'='
string|"'oslo_cache.dict'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'_get_custom_cache_region'
op|'('
nl|'\n'
name|'backend'
op|'='
string|"'dogpile.cache.memcached'"
op|','
nl|'\n'
name|'url'
op|'='
op|'['
string|"'localhost:11211'"
op|']'
op|')'
op|')'
newline|'\n'
name|'mock_cacheregion'
op|'.'
name|'assert_has_calls'
op|'('
nl|'\n'
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'oslo_cache.dict'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'expiration_time'"
op|':'
number|'604800'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'604800'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.memcached'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'url'"
op|':'
op|'['
string|"'localhost:11211'"
op|']'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'604800'
op|')'
op|']'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'dogpile.cache.region.CacheRegion.configure'"
op|')'
newline|'\n'
DECL|member|test_get_memcached_client
name|'def'
name|'test_get_memcached_client'
op|'('
name|'self'
op|','
name|'mock_cacheregion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'cache'"
op|','
name|'enabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'RuntimeError'
op|','
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_memcached_client'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
op|'['
string|"'localhost:11211'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_memcached_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
op|'['
string|"'localhost:11211'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_memcached_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'cache'"
op|','
name|'enabled'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'group'
op|'='
string|"'cache'"
op|','
name|'memcache_servers'
op|'='
op|'['
string|"'localhost:11211'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
nl|'\n'
name|'cache_utils'
op|'.'
name|'get_memcached_client'
op|'('
name|'expiration_time'
op|'='
number|'60'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'mock_cacheregion'
op|'.'
name|'assert_has_calls'
op|'('
nl|'\n'
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.memcached'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'url'"
op|':'
op|'['
string|"'localhost:11211'"
op|']'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.memcached'"
op|','
nl|'\n'
name|'arguments'
op|'='
op|'{'
string|"'url'"
op|':'
op|'['
string|"'localhost:11211'"
op|']'
op|'}'
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'dogpile.cache.null'"
op|','
nl|'\n'
name|'_config_argument_dict'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'_config_prefix'
op|'='
string|"'cache.oslo.arguments.'"
op|','
nl|'\n'
name|'expiration_time'
op|'='
number|'60'
op|','
name|'wrap'
op|'='
name|'None'
op|')'
op|']'
nl|'\n'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
