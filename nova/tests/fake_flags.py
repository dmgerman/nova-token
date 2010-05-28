begin_unit
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
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
name|'FLAGS'
op|'.'
name|'fake_libvirt'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_network'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_users'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'keeper_backend'
op|'='
string|"'sqlite'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'datastore_path'
op|'='
string|"':memory:'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
endmarker|''
end_unit
