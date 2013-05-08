begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""\nClaim objects for use with resource tracking.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
nl|'\n'
DECL|class|NopClaim
name|'class'
name|'NopClaim'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""For use with compute drivers that do not support resource tracking."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'migration'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'migration'
op|'='
name|'migration'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|disk_gb
name|'def'
name|'disk_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|memory_mb
name|'def'
name|'memory_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|vcpus
name|'def'
name|'vcpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'exc_val'
op|','
name|'exc_tb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'exc_type'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'abort'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|abort
dedent|''
dedent|''
name|'def'
name|'abort'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"[Claim: %d MB memory, %d GB disk, %d VCPUS]"'
op|'%'
op|'('
name|'self'
op|'.'
name|'memory_mb'
op|','
nl|'\n'
name|'self'
op|'.'
name|'disk_gb'
op|','
name|'self'
op|'.'
name|'vcpus'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Claim
dedent|''
dedent|''
name|'class'
name|'Claim'
op|'('
name|'NopClaim'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A declaration that a compute host operation will require free resources.\n    Claims serve as marker objects that resources are being held until the\n    update_available_resource audit process runs to do a full reconciliation\n    of resource usage.\n\n    This information will be used to help keep the local compute hosts\'s\n    ComputeNode model in sync to aid the scheduler in making efficient / more\n    correct decisions with respect to host selection.\n    """'
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
name|'tracker'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Claim'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'='
name|'tracker'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|disk_gb
name|'def'
name|'disk_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'root_gb'"
op|']'
op|'+'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|memory_mb
name|'def'
name|'memory_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|vcpus
name|'def'
name|'vcpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|abort
dedent|''
name|'def'
name|'abort'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compute operation requiring claimed resources has failed or\n        been aborted.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Aborting claim: %s"'
op|')'
op|'%'
name|'self'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'abort_instance_claim'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test
dedent|''
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'resources'
op|','
name|'limits'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test if this claim can be satisfied given available resources and\n        optional oversubscription limits\n\n        This should be called before the compute node actually consumes the\n        resources required to execute the claim.\n\n        :param resources: available local compute node resources\n        :returns: Return true if resources are available to claim.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'limits'
op|':'
newline|'\n'
indent|'            '
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# If an individual limit is None, the resource will be considered'
nl|'\n'
comment|'# unlimited:'
nl|'\n'
dedent|''
name|'memory_mb_limit'
op|'='
name|'limits'
op|'.'
name|'get'
op|'('
string|"'memory_mb'"
op|')'
newline|'\n'
name|'disk_gb_limit'
op|'='
name|'limits'
op|'.'
name|'get'
op|'('
string|"'disk_gb'"
op|')'
newline|'\n'
name|'vcpu_limit'
op|'='
name|'limits'
op|'.'
name|'get'
op|'('
string|"'vcpu'"
op|')'
newline|'\n'
nl|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Attempting claim: memory %(memory_mb)d MB, disk %(disk_gb)d "'
nl|'\n'
string|'"GB, VCPUs %(vcpus)d"'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'memory_mb'"
op|':'
name|'self'
op|'.'
name|'memory_mb'
op|','
string|"'disk_gb'"
op|':'
name|'self'
op|'.'
name|'disk_gb'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'self'
op|'.'
name|'vcpus'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|'%'
name|'params'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test for resources:'
nl|'\n'
name|'can_claim'
op|'='
op|'('
name|'self'
op|'.'
name|'_test_memory'
op|'('
name|'resources'
op|','
name|'memory_mb_limit'
op|')'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'_test_disk'
op|'('
name|'resources'
op|','
name|'disk_gb_limit'
op|')'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'_test_cpu'
op|'('
name|'resources'
op|','
name|'vcpu_limit'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'can_claim'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Claim successful"'
op|')'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Claim failed"'
op|')'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'can_claim'
newline|'\n'
nl|'\n'
DECL|member|_test_memory
dedent|''
name|'def'
name|'_test_memory'
op|'('
name|'self'
op|','
name|'resources'
op|','
name|'limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'type_'
op|'='
name|'_'
op|'('
string|'"Memory"'
op|')'
newline|'\n'
name|'unit'
op|'='
string|'"MB"'
newline|'\n'
name|'total'
op|'='
name|'resources'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
name|'used'
op|'='
name|'resources'
op|'['
string|"'memory_mb_used'"
op|']'
newline|'\n'
name|'requested'
op|'='
name|'self'
op|'.'
name|'memory_mb'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_test'
op|'('
name|'type_'
op|','
name|'unit'
op|','
name|'total'
op|','
name|'used'
op|','
name|'requested'
op|','
name|'limit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_disk
dedent|''
name|'def'
name|'_test_disk'
op|'('
name|'self'
op|','
name|'resources'
op|','
name|'limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'type_'
op|'='
name|'_'
op|'('
string|'"Disk"'
op|')'
newline|'\n'
name|'unit'
op|'='
string|'"GB"'
newline|'\n'
name|'total'
op|'='
name|'resources'
op|'['
string|"'local_gb'"
op|']'
newline|'\n'
name|'used'
op|'='
name|'resources'
op|'['
string|"'local_gb_used'"
op|']'
newline|'\n'
name|'requested'
op|'='
name|'self'
op|'.'
name|'disk_gb'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_test'
op|'('
name|'type_'
op|','
name|'unit'
op|','
name|'total'
op|','
name|'used'
op|','
name|'requested'
op|','
name|'limit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_cpu
dedent|''
name|'def'
name|'_test_cpu'
op|'('
name|'self'
op|','
name|'resources'
op|','
name|'limit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'type_'
op|'='
name|'_'
op|'('
string|'"CPU"'
op|')'
newline|'\n'
name|'unit'
op|'='
string|'"VCPUs"'
newline|'\n'
name|'total'
op|'='
name|'resources'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
name|'used'
op|'='
name|'resources'
op|'['
string|"'vcpus_used'"
op|']'
newline|'\n'
name|'requested'
op|'='
name|'self'
op|'.'
name|'vcpus'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_test'
op|'('
name|'type_'
op|','
name|'unit'
op|','
name|'total'
op|','
name|'used'
op|','
name|'requested'
op|','
name|'limit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test
dedent|''
name|'def'
name|'_test'
op|'('
name|'self'
op|','
name|'type_'
op|','
name|'unit'
op|','
name|'total'
op|','
name|'used'
op|','
name|'requested'
op|','
name|'limit'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test if the given type of resource needed for a claim can be safely\n        allocated.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Total %(type)s: %(total)d %(unit)s, used: %(used).02f '"
nl|'\n'
string|"'%(unit)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'type'"
op|':'
name|'type_'
op|','
string|"'total'"
op|':'
name|'total'
op|','
string|"'unit'"
op|':'
name|'unit'
op|','
string|"'used'"
op|':'
name|'used'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'limit'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# treat resource as unlimited:'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'%(type)s limit not specified, defaulting to '"
nl|'\n'
string|"'unlimited'"
op|')'
op|','
op|'{'
string|"'type'"
op|':'
name|'type_'
op|'}'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'free'
op|'='
name|'limit'
op|'-'
name|'used'
newline|'\n'
nl|'\n'
comment|'# Oversubscribed resource policy info:'
nl|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'%(type)s limit: %(limit).02f %(unit)s, free: %(free).02f '"
nl|'\n'
string|"'%(unit)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'type'"
op|':'
name|'type_'
op|','
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'free'"
op|':'
name|'free'
op|','
string|"'unit'"
op|':'
name|'unit'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'can_claim'
op|'='
name|'requested'
op|'<='
name|'free'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'can_claim'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Unable to claim resources.  Free %(type)s %(free).02f '"
nl|'\n'
string|"'%(unit)s < requested %(requested)d %(unit)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'type'"
op|':'
name|'type_'
op|','
string|"'free'"
op|':'
name|'free'
op|','
string|"'unit'"
op|':'
name|'unit'
op|','
nl|'\n'
string|"'requested'"
op|':'
name|'requested'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'can_claim'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResizeClaim
dedent|''
dedent|''
name|'class'
name|'ResizeClaim'
op|'('
name|'Claim'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Claim used for holding resources for an incoming resize/migration\n    operation.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'instance_type'
op|','
name|'tracker'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ResizeClaim'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'instance'
op|','
name|'tracker'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_type'
op|'='
name|'instance_type'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|disk_gb
name|'def'
name|'disk_gb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'self'
op|'.'
name|'instance_type'
op|'['
string|"'root_gb'"
op|']'
op|'+'
nl|'\n'
name|'self'
op|'.'
name|'instance_type'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|memory_mb
name|'def'
name|'memory_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|vcpus
name|'def'
name|'vcpus'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|abort
dedent|''
name|'def'
name|'abort'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compute operation requiring claimed resources has failed or\n        been aborted.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Aborting claim: %s"'
op|')'
op|'%'
name|'self'
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tracker'
op|'.'
name|'drop_resize_claim'
op|'('
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'instance_type'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
