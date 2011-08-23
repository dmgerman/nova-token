begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""Possible task states for instances"""'
newline|'\n'
nl|'\n'
DECL|variable|SCHEDULING
name|'SCHEDULING'
op|'='
string|"'scheduling'"
newline|'\n'
DECL|variable|BLOCK_DEVICE_MAPPING
name|'BLOCK_DEVICE_MAPPING'
op|'='
string|"'block_device_mapping'"
newline|'\n'
DECL|variable|NETWORKING
name|'NETWORKING'
op|'='
string|"'networking'"
newline|'\n'
DECL|variable|SPAWN
name|'SPAWN'
op|'='
string|"'spawn'"
newline|'\n'
nl|'\n'
DECL|variable|SNAPSHOTTING
name|'SNAPSHOTTING'
op|'='
string|"'snapshotting'"
newline|'\n'
DECL|variable|BACKING_UP
name|'BACKING_UP'
op|'='
string|"'backing_up'"
newline|'\n'
DECL|variable|PASSWORD
name|'PASSWORD'
op|'='
string|"'password'"
newline|'\n'
nl|'\n'
DECL|variable|RESIZE_PREP
name|'RESIZE_PREP'
op|'='
string|"'resize_prep'"
newline|'\n'
DECL|variable|RESIZE_MIGRATING
name|'RESIZE_MIGRATING'
op|'='
string|"'resize_migrating'"
newline|'\n'
DECL|variable|RESIZE_MIGRATED
name|'RESIZE_MIGRATED'
op|'='
string|"'resize_migrated'"
newline|'\n'
DECL|variable|RESIZE_FINISH
name|'RESIZE_FINISH'
op|'='
string|"'resize_finish'"
newline|'\n'
DECL|variable|RESIZE_REVERTING
name|'RESIZE_REVERTING'
op|'='
string|"'resize_reverting'"
newline|'\n'
DECL|variable|RESIZE_CONFIRMING
name|'RESIZE_CONFIRMING'
op|'='
string|"'resize_confirming'"
newline|'\n'
nl|'\n'
DECL|variable|REBUILDING
name|'REBUILDING'
op|'='
string|"'rebuilding'"
newline|'\n'
nl|'\n'
DECL|variable|REBOOTING
name|'REBOOTING'
op|'='
string|"'rebooting'"
newline|'\n'
DECL|variable|HARD_REBOOTING
name|'HARD_REBOOTING'
op|'='
string|"'hard_rebooting'"
newline|'\n'
DECL|variable|PAUSING
name|'PAUSING'
op|'='
string|"'pausing'"
newline|'\n'
DECL|variable|UNPAUSING
name|'UNPAUSING'
op|'='
string|"'unpausing'"
newline|'\n'
DECL|variable|SUSPENDING
name|'SUSPENDING'
op|'='
string|"'suspending'"
newline|'\n'
DECL|variable|RESUMING
name|'RESUMING'
op|'='
string|"'resuming'"
newline|'\n'
nl|'\n'
DECL|variable|RESCUING
name|'RESCUING'
op|'='
string|"'rescuing'"
newline|'\n'
DECL|variable|UNRESCUING
name|'UNRESCUING'
op|'='
string|"'unrescuing'"
newline|'\n'
nl|'\n'
DECL|variable|DELETING
name|'DELETING'
op|'='
string|"'deleting'"
newline|'\n'
DECL|variable|STOPPING
name|'STOPPING'
op|'='
string|"'stopping'"
newline|'\n'
DECL|variable|STARTING
name|'STARTING'
op|'='
string|"'starting'"
newline|'\n'
endmarker|''
end_unit
