begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
comment|'# NOTE(comstud): You may scratch your head as you see code that imports'
nl|'\n'
comment|'# this module and then accesses attributes for objects such as Instance,'
nl|'\n'
comment|'# etc, yet you do not see these attributes in here. Never fear, there is'
nl|'\n'
comment|'# a little bit of magic. When objects are registered, an attribute is set'
nl|'\n'
comment|'# on this module automatically, pointing to the newest/latest version of'
nl|'\n'
comment|'# the object.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_all
name|'def'
name|'register_all'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): You must make sure your object gets imported in this'
nl|'\n'
comment|'# function in order for it to be registered by services that may'
nl|'\n'
comment|'# need to receive it via RPC.'
nl|'\n'
indent|'    '
name|'__import__'
op|'('
string|"'nova.objects.agent'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.aggregate'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.bandwidth_usage'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.block_device'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.build_request'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.cell_mapping'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.compute_node'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.dns_domain'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.ec2'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.external_event'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.fixed_ip'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.flavor'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.floating_ip'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.host_mapping'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.hv_spec'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.image_meta'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_action'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_fault'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_group'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_info_cache'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_mapping'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_numa_topology'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.instance_pci_requests'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.keypair'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.migrate_data'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.virt_device_metadata'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.migration'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.migration_context'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.monitor_metric'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.network'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.network_request'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.notification'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.numa'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.pci_device'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.pci_device_pool'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.request_spec'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.resource_provider'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.tag'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.quotas'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.security_group'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.security_group_rule'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.service'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.task_log'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.vcpu_model'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.virt_cpu_topology'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.virtual_interface'"
op|')'
newline|'\n'
name|'__import__'
op|'('
string|"'nova.objects.volume_usage'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
