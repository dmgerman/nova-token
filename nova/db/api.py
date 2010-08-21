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
name|'utils'
newline|'\n'
nl|'\n'
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
name|'DEFINE_string'
op|'('
string|"'db_backend'"
op|','
string|"'sqlalchemy'"
op|','
nl|'\n'
string|"'The backend to use for db'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_impl
name|'_impl'
op|'='
name|'utils'
op|'.'
name|'LazyPluggable'
op|'('
name|'FLAGS'
op|'['
string|"'db_backend'"
op|']'
op|','
nl|'\n'
DECL|variable|sqlalchemy
name|'sqlalchemy'
op|'='
string|"'nova.db.sqlalchemy.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMoreBlades
name|'class'
name|'NoMoreBlades'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_get
dedent|''
name|'def'
name|'daemon_get'
op|'('
name|'context'
op|','
name|'node_name'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_impl'
op|'.'
name|'daemon_get'
op|'('
name|'context'
op|','
name|'node_name'
op|','
name|'binary'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_create
dedent|''
name|'def'
name|'daemon_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_impl'
op|'.'
name|'daemon_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemon_update
dedent|''
name|'def'
name|'daemon_update'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_impl'
op|'.'
name|'daemon_update'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_create
dedent|''
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create an instance from the values dictionary."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the instance or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an instance or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_state
dedent|''
name|'def'
name|'instance_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the state of an instance."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'instance_state'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'state'
op|','
name|'description'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an instance and update it.\n\n    Raises NotFound if instance does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'####################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_create
dedent|''
name|'def'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a network from the values dictionary."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'network_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_destroy
dedent|''
name|'def'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the network or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'network_destroy'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_get
dedent|''
name|'def'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get an network or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_update
dedent|''
name|'def'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an network and update it.\n\n    Raises NotFound if network does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|project_get_network
dedent|''
name|'def'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the network associated with the project."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'###################'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_allocate_shelf_and_blade
dedent|''
name|'def'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Atomically allocate a free shelf and blade from the pool."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_attached
dedent|''
name|'def'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that a volume is set as attached."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_attached'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_create
dedent|''
name|'def'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a volume from the values dictionary."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_destroy
dedent|''
name|'def'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the volume or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_detached
dedent|''
name|'def'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that a volume is set as detached."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get
dedent|''
name|'def'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a volume or raise if it does not exist."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_get_shelf_and_blade
dedent|''
name|'def'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the shelf and blade allocated to the volume."""'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|volume_update
dedent|''
name|'def'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the given properties on an volume and update it.\n\n    Raises NotFound if volume does not exist.\n\n    """'
newline|'\n'
name|'return'
name|'_impl'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_id'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
