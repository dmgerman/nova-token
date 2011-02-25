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
string|'"""Tests for the testing base code."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IsolationTestCase
name|'class'
name|'IsolationTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that things are cleaned up after failed tests.\n\n    These tests don\'t really do much here, but if isolation fails a bunch\n    of other tests should fail.\n\n    """'
newline|'\n'
DECL|member|test_service_isolation
name|'def'
name|'test_service_isolation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'compute'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rpc_consumer_isolation
dedent|''
name|'def'
name|'test_rpc_consumer_isolation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'connection'
op|'='
name|'rpc'
op|'.'
name|'Connection'
op|'.'
name|'instance'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
name|'consumer'
op|'='
name|'rpc'
op|'.'
name|'TopicConsumer'
op|'('
name|'connection'
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
nl|'\n'
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'self'
op|'.'
name|'fail'
op|'('
string|"'I should never be called'"
op|')'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'attach_to_eventlet'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
