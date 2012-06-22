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
nl|'\n'
string|'"""Instance Metadata information."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'dhcp_domain'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DEFAULT_MAPPINGS
name|'_DEFAULT_MAPPINGS'
op|'='
op|'{'
string|"'ami'"
op|':'
string|"'sda1'"
op|','
nl|'\n'
string|"'ephemeral0'"
op|':'
string|"'sda2'"
op|','
nl|'\n'
string|"'root'"
op|':'
name|'block_device'
op|'.'
name|'DEFAULT_ROOT_DEV_NAME'
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'sda3'"
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|VERSIONS
name|'VERSIONS'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidMetadataEc2Version
name|'class'
name|'InvalidMetadataEc2Version'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidMetadataPath
dedent|''
name|'class'
name|'InvalidMetadataPath'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMetadata
dedent|''
name|'class'
name|'InstanceMetadata'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Instance metadata."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'address'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'availability_zone'
op|'='
name|'ec2utils'
op|'.'
name|'get_availability_zone_by_host'
op|'('
nl|'\n'
name|'services'
op|','
name|'instance'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ip_info'
op|'='
name|'ec2utils'
op|'.'
name|'get_ip_info_for_instance'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'security_groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mappings'
op|'='
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'user_data'"
op|','
name|'None'
op|')'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'userdata_b64'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'instance'
op|'['
string|"'user_data'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'userdata_b64'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'ec2_ids'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'instance-id'"
op|']'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'ami-id'"
op|']'
op|'='
name|'ec2utils'
op|'.'
name|'glance_id_to_ec2_id'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'image_type'
name|'in'
op|'['
string|"'kernel'"
op|','
string|"'ramdisk'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'%s_id'"
op|'%'
name|'image_type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'image_id'
op|'='
name|'self'
op|'.'
name|'instance'
op|'['
string|"'%s_id'"
op|'%'
name|'image_type'
op|']'
newline|'\n'
name|'image_type'
op|'='
name|'ec2utils'
op|'.'
name|'image_type'
op|'('
name|'image_type'
op|')'
newline|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'glance_id_to_ec2_id'
op|'('
name|'ctxt'
op|','
name|'image_id'
op|','
nl|'\n'
name|'image_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ec2_ids'
op|'['
string|"'%s-id'"
op|'%'
name|'image_type'
op|']'
op|'='
name|'ec2_id'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'address'
op|'='
name|'address'
newline|'\n'
nl|'\n'
DECL|member|get_ec2_metadata
dedent|''
name|'def'
name|'get_ec2_metadata'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'version'
op|'=='
string|'"latest"'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'VERSIONS'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'version'
name|'not'
name|'in'
name|'VERSIONS'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidMetadataEc2Version'
op|'('
name|'version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'hostname'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'dhcp_domain'
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'self'
op|'.'
name|'ip_info'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
name|'floating_ip'
op|'='
name|'floating_ips'
name|'and'
name|'floating_ips'
op|'['
number|'0'
op|']'
name|'or'
string|"''"
newline|'\n'
nl|'\n'
name|'fmt_sgroups'
op|'='
op|'['
name|'x'
op|'['
string|"'name'"
op|']'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'security_groups'
op|']'
newline|'\n'
name|'data'
op|'='
op|'{'
nl|'\n'
string|"'meta-data'"
op|':'
op|'{'
nl|'\n'
string|"'ami-launch-index'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'launch_index'"
op|']'
op|','
nl|'\n'
string|"'ami-manifest-path'"
op|':'
string|"'FIXME'"
op|','
nl|'\n'
string|"'block-device-mapping'"
op|':'
name|'self'
op|'.'
name|'mappings'
op|','
nl|'\n'
string|"'hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'instance-action'"
op|':'
string|"'none'"
op|','
nl|'\n'
string|"'instance-type'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'local-hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'local-ipv4'"
op|':'
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'placement'"
op|':'
op|'{'
string|"'availability-zone'"
op|':'
name|'self'
op|'.'
name|'availability_zone'
op|'}'
op|','
nl|'\n'
string|"'public-hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'public-ipv4'"
op|':'
name|'floating_ip'
op|','
nl|'\n'
string|"'reservation-id'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|"'security-groups'"
op|':'
name|'fmt_sgroups'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'ec2_ids'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'ec2_ids'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'userdata_b64'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'user-data'"
op|']'
op|'='
name|'self'
op|'.'
name|'userdata_b64'
newline|'\n'
nl|'\n'
comment|'# public keys are strangely rendered in ec2 metadata service'
nl|'\n'
comment|"#  meta-data/public-keys/ returns '0=keyname' (with no trailing /)"
nl|'\n'
comment|'# and only if there is a public key given.'
nl|'\n'
comment|"# '0=keyname' means there is a normally rendered dict at"
nl|'\n'
comment|'#  meta-data/public-keys/0'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# meta-data/public-keys/ : '0=%s' % keyname"
nl|'\n'
comment|"# meta-data/public-keys/0/ : 'openssh-key'"
nl|'\n'
comment|"# meta-data/public-keys/0/openssh-key : '%s' % publickey"
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'public-keys'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'0'"
op|':'
op|'{'
string|"'_name'"
op|':'
string|'"0="'
op|'+'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|','
nl|'\n'
string|"'openssh-key'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'False'
op|':'
comment|'# TODO(vish): store ancestor ids'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'ancestor-ami-ids'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'False'
op|':'
comment|'# TODO(vish): store product codes'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'product-codes'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|lookup
dedent|''
name|'def'
name|'lookup'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
op|'=='
string|'""'
name|'or'
name|'path'
op|'['
number|'0'
op|']'
op|'!='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
string|'"/"'
op|'+'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'path'
op|'=='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'items'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'md'
op|'='
name|'self'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'items'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'InvalidMetadataEc2Version'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidMetadataPath'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'md'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'items'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'items'
op|'['
name|'i'
op|']'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                    '
name|'data'
op|'='
name|'data'
op|'['
name|'items'
op|'['
name|'i'
op|']'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'InvalidMetadataPath'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'i'
op|'!='
name|'len'
op|'('
name|'items'
op|')'
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'InvalidMetadataPath'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'data'
op|'['
name|'items'
op|'['
name|'i'
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_metadata_by_address
dedent|''
dedent|''
name|'def'
name|'get_metadata_by_address'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fixed_ip'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_fixed_ip_by_address'
op|'('
name|'ctxt'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'ctxt'
op|','
name|'fixed_ip'
op|'['
string|"'instance_id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'InstanceMetadata'
op|'('
name|'instance'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_format_instance_mapping
dedent|''
name|'def'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'root_device_name'
op|'='
name|'instance'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
name|'if'
name|'root_device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_DEFAULT_MAPPINGS'
newline|'\n'
nl|'\n'
dedent|''
name|'mappings'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mappings'
op|'['
string|"'ami'"
op|']'
op|'='
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
name|'root_device_name'
op|')'
newline|'\n'
name|'mappings'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_device_name'
newline|'\n'
name|'default_ephemeral_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_ephemeral_device'"
op|')'
newline|'\n'
name|'if'
name|'default_ephemeral_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'ephemeral0'"
op|']'
op|'='
name|'default_ephemeral_device'
newline|'\n'
dedent|''
name|'default_swap_device'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'default_swap_device'"
op|')'
newline|'\n'
name|'if'
name|'default_swap_device'
op|':'
newline|'\n'
indent|'        '
name|'mappings'
op|'['
string|"'swap'"
op|']'
op|'='
name|'default_swap_device'
newline|'\n'
dedent|''
name|'ebs_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# 'ephemeralN', 'swap' and ebs"
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'bdm'
op|'['
string|"'no_device'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# ebs volume case'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
name|'or'
name|'bdm'
op|'['
string|"'snapshot_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ebs_devices'
op|'.'
name|'append'
op|'('
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'virtual_name'
op|'='
name|'bdm'
op|'['
string|"'virtual_name'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'virtual_name'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
name|'virtual_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
name|'virtual_name'
op|']'
op|'='
name|'bdm'
op|'['
string|"'device_name'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): I'm not sure how ebs device should be numbered."
nl|'\n'
comment|'#                 Right now sort by device name for deterministic'
nl|'\n'
comment|'#                 result.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'        '
name|'nebs'
op|'='
number|'0'
newline|'\n'
name|'ebs_devices'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'ebs'
name|'in'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
string|"'ebs%d'"
op|'%'
name|'nebs'
op|']'
op|'='
name|'ebs'
newline|'\n'
name|'nebs'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_md_print
dedent|''
name|'def'
name|'ec2_md_print'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'sorted'
op|'('
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'_name'"
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'_name'"
name|'in'
name|'data'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'+='
name|'str'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|'['
string|"'_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'+='
name|'key'
op|'+'
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'+='
name|'key'
newline|'\n'
nl|'\n'
dedent|''
name|'output'
op|'+='
string|"'\\n'"
newline|'\n'
dedent|''
name|'return'
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
