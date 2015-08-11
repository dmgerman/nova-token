begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may not'
nl|'\n'
comment|'# use this file except in compliance with the License. You may obtain a copy'
nl|'\n'
comment|'# of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
op|'.'
name|'cloud'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'base'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'handler'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'vendordata_json'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'common'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'hide_server_addresses'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
op|'.'
name|'fping'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
op|'.'
name|'os_tenant_networks'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'extensions'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'servers'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'availability_zones'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'baserpc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'messaging'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'opts'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'rpc_driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'scheduler'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'state'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'weights'
op|'.'
name|'mute_child'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'weights'
op|'.'
name|'ram_by_instance_type'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cells'
op|'.'
name|'weights'
op|'.'
name|'weight_offset'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cert'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cloudpipe'
op|'.'
name|'pipelib'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'novnc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'novncproxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'serialproxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'cmd'
op|'.'
name|'spicehtml5proxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'flavors'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'monitors'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'resource_tracker'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conductor'
op|'.'
name|'tasks'
op|'.'
name|'live_migrate'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'serial'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'console'
op|'.'
name|'xvp'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'consoleauth'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'crypto'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'base'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'download'
op|'.'
name|'file'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'s3'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'ipv6'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'barbican'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'keymgr'
op|'.'
name|'conf_key_mgr'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'netconf'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'floating_ips'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'ldapdns'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'linux_net'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'neutronv2'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
op|'.'
name|'security_group'
op|'.'
name|'openstack_driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'notifications'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'objects'
op|'.'
name|'network'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'objectstore'
op|'.'
name|'s3server'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'paths'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'pci'
op|'.'
name|'request'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'pci'
op|'.'
name|'whitelist'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'quota'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rdp'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filter_scheduler'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'aggregate_image_properties_isolation'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'core_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'disk_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'io_ops_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'isolated_hosts_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'num_instances_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'ram_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
op|'.'
name|'trusted_filter'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'host_manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'ironic_host_manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'manager'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'rpcapi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'scheduler_options'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'weights'
op|'.'
name|'io_ops'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'weights'
op|'.'
name|'metrics'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'weights'
op|'.'
name|'ram'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'service'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'api'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'servicegroup'
op|'.'
name|'drivers'
op|'.'
name|'zk'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'spice'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'vnc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'vnc'
op|'.'
name|'xvp_proxy'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'volume'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'cinder'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
string|"'DEFAULT'"
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'vendordata_json'
op|'.'
name|'file_opt'
op|']'
op|','
nl|'\n'
op|'['
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'allow_instance_snapshots_opt'
op|']'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'auth'
op|'.'
name|'auth_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
op|'.'
name|'cloud'
op|'.'
name|'ec2_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
op|'.'
name|'ec2_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'base'
op|'.'
name|'metadata_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'handler'
op|'.'
name|'metadata_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'osapi_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
op|'.'
name|'ext_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
op|'.'
name|'fping'
op|'.'
name|'fping_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'contrib'
op|'.'
name|'os_tenant_networks'
op|'.'
nl|'\n'
name|'os_network_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'extensions'
op|'.'
name|'ext_opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'hide_server_addresses'
op|'.'
name|'opts'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
op|'.'
name|'servers'
op|'.'
name|'server_opts'
op|','
nl|'\n'
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'neutron'"
op|','
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
op|'.'
name|'handler'
op|'.'
name|'metadata_proxy_opts'
op|')'
op|','
nl|'\n'
op|'('
string|"'osapi_v3'"
op|','
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'api_opts'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
