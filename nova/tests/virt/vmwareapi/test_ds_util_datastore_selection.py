begin_unit
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
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'ds_util'
newline|'\n'
nl|'\n'
DECL|variable|ResultSet
name|'ResultSet'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ResultSet'"
op|','
op|'['
string|"'objects'"
op|']'
op|')'
newline|'\n'
DECL|variable|ResultSetToken
name|'ResultSetToken'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ResultSet'"
op|','
op|'['
string|"'objects'"
op|','
string|"'token'"
op|']'
op|')'
newline|'\n'
DECL|variable|ObjectContent
name|'ObjectContent'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ObjectContent'"
op|','
op|'['
string|"'obj'"
op|','
string|"'propSet'"
op|']'
op|')'
newline|'\n'
DECL|variable|DynamicProperty
name|'DynamicProperty'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'Property'"
op|','
op|'['
string|"'name'"
op|','
string|"'val'"
op|']'
op|')'
newline|'\n'
DECL|variable|MoRef
name|'MoRef'
op|'='
name|'collections'
op|'.'
name|'namedtuple'
op|'('
string|"'ManagedObjectReference'"
op|','
op|'['
string|"'value'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareDSUtilDatastoreSelectionTestCase
name|'class'
name|'VMwareDSUtilDatastoreSelectionTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VMwareDSUtilDatastoreSelectionTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
op|'['
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'os-some-name'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'987654321'
op|','
number|'12346789'
op|']'
op|','
nl|'\n'
op|'['
string|"'NFS'"
op|','
string|"'another-name'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'9876543210'
op|','
number|'123467890'
op|']'
op|','
nl|'\n'
op|'['
string|"'BAD'"
op|','
string|"'some-name-bad'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'98765432100'
op|','
number|'1234678900'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'some-name-good'"
op|','
name|'False'
op|','
string|"'normal'"
op|','
number|'987654321'
op|','
number|'12346789'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'new-name'"
op|','
name|'True'
op|','
string|"'inMaintenance'"
op|','
number|'987654321'
op|','
number|'12346789'
op|']'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|build_result_set
dedent|''
name|'def'
name|'build_result_set'
op|'('
name|'self'
op|','
name|'mock_data'
op|','
name|'name_list'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# datastores will have a moref_id of ds-000 and'
nl|'\n'
comment|'# so on based on their index in the mock_data list'
nl|'\n'
indent|'        '
name|'if'
name|'name_list'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'name_list'
op|'='
name|'self'
op|'.'
name|'propset_name_list'
newline|'\n'
nl|'\n'
dedent|''
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'id'
op|','
name|'row'
name|'in'
name|'enumerate'
op|'('
name|'mock_data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'ObjectContent'
op|'('
nl|'\n'
name|'obj'
op|'='
name|'MoRef'
op|'('
name|'value'
op|'='
string|'"ds-%03d"'
op|'%'
name|'id'
op|')'
op|','
nl|'\n'
name|'propSet'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'value'
name|'in'
name|'enumerate'
op|'('
name|'row'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'obj'
op|'.'
name|'propSet'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'DynamicProperty'
op|'('
name|'name'
op|'='
name|'name_list'
op|'['
name|'index'
op|']'
op|','
name|'val'
op|'='
name|'row'
op|'['
name|'index'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'objects'
op|'.'
name|'append'
op|'('
name|'obj'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ResultSet'
op|'('
name|'objects'
op|'='
name|'objects'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|propset_name_list
name|'def'
name|'propset_name_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'summary.type'"
op|','
string|"'summary.name'"
op|','
string|"'summary.accessible'"
op|','
nl|'\n'
string|"'summary.maintenanceMode'"
op|','
string|"'summary.capacity'"
op|','
nl|'\n'
string|"'summary.freeSpace'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_simple
dedent|''
name|'def'
name|'test_filter_datastores_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'self'
op|'.'
name|'data'
op|')'
newline|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'fake_ref'"
op|','
name|'name'
op|'='
string|"'ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'0'
op|','
name|'freespace'
op|'='
number|'0'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
name|'best_match'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rec'
op|'.'
name|'ref'
op|','
string|'"could not find datastore!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ds-001'"
op|','
name|'rec'
op|'.'
name|'ref'
op|'.'
name|'value'
op|','
nl|'\n'
string|'"didn\'t find the right datastore!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123467890'
op|','
name|'rec'
op|'.'
name|'freespace'
op|','
nl|'\n'
string|'"did not obtain correct freespace!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_empty
dedent|''
name|'def'
name|'test_filter_datastores_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'fake_ref'"
op|','
name|'name'
op|'='
string|"'ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'0'
op|','
name|'freespace'
op|'='
number|'0'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
name|'best_match'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rec'
op|','
name|'best_match'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_no_match
dedent|''
name|'def'
name|'test_filter_datastores_no_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'self'
op|'.'
name|'data'
op|')'
newline|'\n'
name|'datastore_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'no_match.*'"
op|')'
newline|'\n'
nl|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'fake_ref'"
op|','
name|'name'
op|'='
string|"'ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'0'
op|','
name|'freespace'
op|'='
number|'0'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
nl|'\n'
name|'best_match'
op|','
nl|'\n'
name|'datastore_regex'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rec'
op|','
name|'best_match'
op|','
string|'"did not match datastore properly"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_specific_match
dedent|''
name|'def'
name|'test_filter_datastores_specific_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'data'
op|'='
op|'['
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'os-some-name'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'987654321'
op|','
number|'1234678'
op|']'
op|','
nl|'\n'
op|'['
string|"'NFS'"
op|','
string|"'another-name'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'9876543210'
op|','
number|'123467890'
op|']'
op|','
nl|'\n'
op|'['
string|"'BAD'"
op|','
string|"'some-name-bad'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'98765432100'
op|','
number|'1234678900'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'some-name-good'"
op|','
name|'True'
op|','
string|"'normal'"
op|','
number|'987654321'
op|','
number|'12346789'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'some-other-good'"
op|','
name|'False'
op|','
string|"'normal'"
op|','
number|'987654321000'
op|','
nl|'\n'
number|'12346789000'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'new-name'"
op|','
name|'True'
op|','
string|"'inMaintenance'"
op|','
number|'987654321000'
op|','
nl|'\n'
number|'12346789000'
op|']'
nl|'\n'
op|']'
newline|'\n'
comment|'# only the DS some-name-good is accessible and matches the regex'
nl|'\n'
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'data'
op|')'
newline|'\n'
name|'datastore_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'.*-good$'"
op|')'
newline|'\n'
nl|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'fake_ref'"
op|','
name|'name'
op|'='
string|"'ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'0'
op|','
name|'freespace'
op|'='
number|'0'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
nl|'\n'
name|'best_match'
op|','
nl|'\n'
name|'datastore_regex'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rec'
op|','
string|'"could not find datastore!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ds-003'"
op|','
name|'rec'
op|'.'
name|'ref'
op|'.'
name|'value'
op|','
nl|'\n'
string|'"didn\'t find the right datastore!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
string|"'ds-004'"
op|','
name|'rec'
op|'.'
name|'ref'
op|'.'
name|'value'
op|','
nl|'\n'
string|'"accepted an unreachable datastore!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'some-name-good'"
op|','
name|'rec'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'12346789'
op|','
name|'rec'
op|'.'
name|'freespace'
op|','
nl|'\n'
string|'"did not obtain correct freespace!"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'987654321'
op|','
name|'rec'
op|'.'
name|'capacity'
op|','
nl|'\n'
string|'"did not obtain correct capacity!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_missing_props
dedent|''
name|'def'
name|'test_filter_datastores_missing_props'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'['
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'os-some-name'"
op|','
number|'987654321'
op|','
number|'1234678'
op|']'
op|','
nl|'\n'
op|'['
string|"'NFS'"
op|','
string|"'another-name'"
op|','
number|'9876543210'
op|','
number|'123467890'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
comment|"# no matches are expected when 'summary.accessible' is missing"
nl|'\n'
name|'prop_names'
op|'='
op|'['
string|"'summary.type'"
op|','
string|"'summary.name'"
op|','
nl|'\n'
string|"'summary.capacity'"
op|','
string|"'summary.freeSpace'"
op|']'
newline|'\n'
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'data'
op|','
name|'prop_names'
op|')'
newline|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'fake_ref'"
op|','
name|'name'
op|'='
string|"'ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'0'
op|','
name|'freespace'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
name|'best_match'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rec'
op|','
name|'best_match'
op|','
string|'"no matches were expected"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_datastores_best_match
dedent|''
name|'def'
name|'test_filter_datastores_best_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'['
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'spam-good'"
op|','
name|'True'
op|','
number|'20'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
number|'10'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|']'
op|','
nl|'\n'
op|'['
string|"'NFS'"
op|','
string|"'eggs-good'"
op|','
name|'True'
op|','
number|'40'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
number|'15'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|']'
op|','
nl|'\n'
op|'['
string|"'BAD'"
op|','
string|"'some-name-bad'"
op|','
name|'True'
op|','
number|'30'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
number|'20'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'some-name-good'"
op|','
name|'True'
op|','
number|'50'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
number|'5'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|']'
op|','
nl|'\n'
op|'['
string|"'VMFS'"
op|','
string|"'some-other-good'"
op|','
name|'True'
op|','
number|'10'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
number|'10'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'datastores'
op|'='
name|'self'
op|'.'
name|'build_result_set'
op|'('
name|'data'
op|')'
newline|'\n'
name|'datastore_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'.*-good$'"
op|')'
newline|'\n'
nl|'\n'
comment|'# the current best match is better than all candidates'
nl|'\n'
name|'best_match'
op|'='
name|'ds_util'
op|'.'
name|'Datastore'
op|'('
name|'ref'
op|'='
string|"'ds-100'"
op|','
name|'name'
op|'='
string|"'best-ds-good'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'20'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|','
name|'freespace'
op|'='
number|'19'
op|'*'
name|'units'
op|'.'
name|'Gi'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'ds_util'
op|'.'
name|'_select_datastore'
op|'('
name|'datastores'
op|','
nl|'\n'
name|'best_match'
op|','
nl|'\n'
name|'datastore_regex'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rec'
op|','
name|'best_match'
op|','
string|'"did not match datastore properly"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
