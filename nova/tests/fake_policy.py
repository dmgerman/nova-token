begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
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
nl|'\n'
name|'policy_data'
op|'='
string|'"""\n{\n    "admin_api": "role:admin",\n\n    "cells_scheduler_filter:TargetCellFilter": "is_admin:True",\n\n    "context_is_admin": "role:admin or role:administrator",\n    "compute:create": "",\n    "compute:create:attach_network": "",\n    "compute:create:attach_volume": "",\n\n    "compute:get": "",\n    "compute:get_all": "",\n    "compute:get_all_tenants": "",\n\n    "compute:update": "",\n\n    "compute:get_instance_metadata": "",\n    "compute:get_all_instance_metadata": "",\n    "compute:update_instance_metadata": "",\n    "compute:delete_instance_metadata": "",\n\n    "compute:get_instance_faults": "",\n    "compute:get_diagnostics": "",\n\n    "compute:get_lock": "",\n    "compute:lock": "",\n    "compute:unlock": "",\n\n    "compute:get_vnc_console": "",\n    "compute:get_spice_console": "",\n    "compute:get_console_output": "",\n\n    "compute:associate_floating_ip": "",\n    "compute:reset_network": "",\n    "compute:inject_network_info": "",\n    "compute:add_fixed_ip": "",\n    "compute:remove_fixed_ip": "",\n\n    "compute:attach_volume": "",\n    "compute:detach_volume": "",\n\n    "compute:inject_file": "",\n\n    "compute:set_admin_password": "",\n\n    "compute:rescue": "",\n    "compute:unrescue": "",\n\n    "compute:suspend": "",\n    "compute:resume": "",\n\n    "compute:pause": "",\n    "compute:unpause": "",\n\n    "compute:start": "",\n    "compute:stop": "",\n\n    "compute:resize": "",\n    "compute:confirm_resize": "",\n    "compute:revert_resize": "",\n\n    "compute:rebuild": "",\n\n    "compute:reboot": "",\n\n    "compute:snapshot": "",\n    "compute:backup": "",\n\n    "compute:security_groups:add_to_instance": "",\n    "compute:security_groups:remove_from_instance": "",\n\n    "compute:delete": "",\n    "compute:soft_delete": "",\n    "compute:force_delete": "",\n    "compute:restore": "",\n\n\n    "compute_extension:accounts": "",\n    "compute_extension:admin_actions:pause": "",\n    "compute_extension:admin_actions:unpause": "",\n    "compute_extension:admin_actions:suspend": "",\n    "compute_extension:admin_actions:resume": "",\n    "compute_extension:admin_actions:lock": "",\n    "compute_extension:admin_actions:unlock": "",\n    "compute_extension:admin_actions:resetNetwork": "",\n    "compute_extension:admin_actions:injectNetworkInfo": "",\n    "compute_extension:admin_actions:createBackup": "",\n    "compute_extension:admin_actions:migrateLive": "",\n    "compute_extension:admin_actions:resetState": "",\n    "compute_extension:admin_actions:migrate": "",\n    "compute_extension:aggregates": "",\n    "compute_extension:agents": "",\n    "compute_extension:attach_interfaces": "",\n    "compute_extension:baremetal_nodes": "",\n    "compute_extension:cells": "",\n    "compute_extension:v3:os-cells": "",\n    "compute_extension:certificates": "",\n    "compute_extension:v3:os-certificates": "",\n    "compute_extension:cloudpipe": "",\n    "compute_extension:cloudpipe_update": "",\n    "compute_extension:config_drive": "",\n    "compute_extension:console_output": "",\n    "compute_extension:consoles": "",\n    "compute_extension:coverage_ext": "is_admin:True",\n    "compute_extension:createserverext": "",\n    "compute_extension:deferred_delete": "",\n    "compute_extension:disk_config": "",\n    "compute_extension:evacuate": "is_admin:True",\n    "compute_extension:v3:os-evacuate": "is_admin:True",\n    "compute_extension:extended_server_attributes": "",\n    "compute_extension:extended_status": "",\n    "compute_extension:extended_availability_zone": "",\n    "compute_extension:extended_ips": "",\n    "compute_extension:extended_ips_mac": "",\n    "compute_extension:extended_vif_net": "",\n    "compute_extension:fixed_ips": "",\n    "compute_extension:v3:os-fixed-ips": "",\n    "compute_extension:flavor_access": "",\n    "compute_extension:v3:os-flavor-access": "",\n    "compute_extension:flavor_disabled": "",\n    "compute_extension:v3:os-flavor-disabled": "",\n    "compute_extension:flavor_rxtx": "",\n    "compute_extension:flavor_swap": "",\n    "compute_extension:flavorextradata": "",\n    "compute_extension:flavorextraspecs:index": "",\n    "compute_extension:flavorextraspecs:show": "",\n    "compute_extension:flavorextraspecs:create": "is_admin:True",\n    "compute_extension:flavorextraspecs:update": "is_admin:True",\n    "compute_extension:flavorextraspecs:delete": "is_admin:True",\n    "compute_extension:flavormanage": "",\n    "compute_extension:floating_ip_dns": "",\n    "compute_extension:floating_ip_pools": "",\n    "compute_extension:floating_ips": "",\n    "compute_extension:floating_ips_bulk": "",\n    "compute_extension:fping": "",\n    "compute_extension:fping:all_tenants": "is_admin:True",\n    "compute_extension:hide_server_addresses": "",\n    "compute_extension:hosts": "",\n    "compute_extension:hypervisors": "",\n    "compute_extension:image_size": "",\n    "compute_extension:v3:os-images": "",\n    "compute_extension:instance_actions": "",\n    "compute_extension:instance_actions:events": "is_admin:True",\n    "compute_extension:instance_usage_audit_log": "",\n    "compute_extension:v3:os-instance-usage-audit-log": "",\n    "compute_extension:keypairs": "",\n    "compute_extension:v3:os-keypairs": "",\n    "compute_extension:multinic": "",\n    "compute_extension:networks": "",\n    "compute_extension:networks:view": "",\n    "compute_extension:networks_associate": "",\n    "compute_extension:os-tenant-networks": "",\n    "compute_extension:quotas:show": "",\n    "compute_extension:quotas:update": "",\n    "compute_extension:quotas:delete": "",\n    "compute_extension:v3:os-quota-sets:show": "",\n    "compute_extension:v3:os-quota-sets:update": "",\n    "compute_extension:v3:os-quota-sets:delete": "",\n    "compute_extension:quota_classes": "",\n    "compute_extension:rescue": "",\n    "compute_extension:v3:os-rescue": "",\n    "compute_extension:security_group_default_rules": "",\n    "compute_extension:security_groups": "",\n    "compute_extension:server_diagnostics": "",\n    "compute_extension:v3:os-server-diagnostics": "",\n    "compute_extension:server_password": "",\n    "compute_extension:server_usage": "",\n    "compute_extension:services": "",\n    "compute_extension:simple_tenant_usage:show": "",\n    "compute_extension:simple_tenant_usage:list": "",\n    "compute_extension:users": "",\n    "compute_extension:virtual_interfaces": "",\n    "compute_extension:virtual_storage_arrays": "",\n    "compute_extension:volumes": "",\n    "compute_extension:volume_attachments:index": "",\n    "compute_extension:volume_attachments:show": "",\n    "compute_extension:volume_attachments:create": "",\n    "compute_extension:volume_attachments:delete": "",\n    "compute_extension:volumetypes": "",\n    "compute_extension:zones": "",\n    "compute_extension:availability_zone:list": "",\n    "compute_extension:availability_zone:detail": "is_admin:True",\n    "compute_extension:used_limits_for_admin": "is_admin:True",\n\n    "volume:create": "",\n    "volume:get": "",\n    "volume:get_all": "",\n    "volume:get_volume_metadata": "",\n    "volume:delete": "",\n    "volume:update": "",\n    "volume:delete_volume_metadata": "",\n    "volume:update_volume_metadata": "",\n    "volume:attach": "",\n    "volume:detach": "",\n    "volume:reserve_volume": "",\n    "volume:unreserve_volume": "",\n    "volume:begin_detaching": "",\n    "volume:roll_detaching": "",\n    "volume:check_attach": "",\n    "volume:check_detach": "",\n    "volume:initialize_connection": "",\n    "volume:terminate_connection": "",\n    "volume:create_snapshot": "",\n    "volume:delete_snapshot": "",\n    "volume:get_snapshot": "",\n    "volume:get_all_snapshots": "",\n\n\n    "volume_extension:volume_admin_actions:reset_status": "rule:admin_api",\n    "volume_extension:snapshot_admin_actions:reset_status": "rule:admin_api",\n    "volume_extension:volume_admin_actions:force_delete": "rule:admin_api",\n    "volume_extension:volume_actions:upload_image": "",\n    "volume_extension:types_manage": "",\n    "volume_extension:types_extra_specs": "",\n\n\n    "network:get_all": "",\n    "network:get": "",\n    "network:create": "",\n    "network:delete": "",\n    "network:associate": "",\n    "network:disassociate": "",\n    "network:get_vifs_by_instance": "",\n    "network:get_vif_by_mac_address": "",\n    "network:allocate_for_instance": "",\n    "network:deallocate_for_instance": "",\n    "network:validate_networks": "",\n    "network:get_instance_uuids_by_ip_filter": "",\n    "network:get_instance_id_by_floating_address": "",\n    "network:setup_networks_on_host": "",\n\n    "network:get_floating_ip": "",\n    "network:get_floating_ip_pools": "",\n    "network:get_floating_ip_by_address": "",\n    "network:get_floating_ips_by_project": "",\n    "network:get_floating_ips_by_fixed_address": "",\n    "network:allocate_floating_ip": "",\n    "network:deallocate_floating_ip": "",\n    "network:associate_floating_ip": "",\n    "network:disassociate_floating_ip": "",\n    "network:release_floating_ip": "",\n    "network:migrate_instance_start": "",\n    "network:migrate_instance_finish": "",\n\n    "network:get_fixed_ip": "",\n    "network:get_fixed_ip_by_address": "",\n    "network:add_fixed_ip_to_instance": "",\n    "network:remove_fixed_ip_from_instance": "",\n    "network:add_network_to_project": "",\n    "network:get_instance_nw_info": "",\n\n    "network:get_dns_domains": "",\n    "network:add_dns_entry": "",\n    "network:modify_dns_entry": "",\n    "network:delete_dns_entry": "",\n    "network:get_dns_entries_by_address": "",\n    "network:get_dns_entries_by_name": "",\n    "network:create_private_dns_domain": "",\n    "network:create_public_dns_domain": "",\n    "network:delete_dns_domain": ""\n}\n"""'
newline|'\n'
endmarker|''
end_unit
