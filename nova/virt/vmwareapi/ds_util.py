begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
string|'"""\nDatastore utility functions\n"""'
newline|'\n'
name|'import'
name|'posixpath'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'vmware'
name|'import'
name|'exceptions'
name|'as'
name|'vexc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
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
DECL|variable|ALLOWED_DATASTORE_TYPES
name|'ALLOWED_DATASTORE_TYPES'
op|'='
op|'['
string|"'VMFS'"
op|','
string|"'NFS'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Datastore
name|'class'
name|'Datastore'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ref'
op|','
name|'name'
op|','
name|'capacity'
op|'='
name|'None'
op|','
name|'freespace'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Datastore object holds ref and name together for convenience.\n\n        :param ref: a vSphere reference to a datastore\n        :param name: vSphere unique name for this datastore\n        :param capacity: (optional) capacity in bytes of this datastore\n        :param freespace: (optional) free space in bytes of datastore\n        """'
newline|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"Datastore name cannot be None"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"Datastore reference cannot be None"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'freespace'
name|'is'
name|'not'
name|'None'
name|'and'
name|'capacity'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"Invalid capacity"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'capacity'
name|'is'
name|'not'
name|'None'
name|'and'
name|'freespace'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'capacity'
op|'<'
name|'freespace'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"Capacity is smaller than free space"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_ref'
op|'='
name|'ref'
newline|'\n'
name|'self'
op|'.'
name|'_name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'_capacity'
op|'='
name|'capacity'
newline|'\n'
name|'self'
op|'.'
name|'_freespace'
op|'='
name|'freespace'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|ref
name|'def'
name|'ref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|name
name|'def'
name|'name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_name'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|capacity
name|'def'
name|'capacity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_capacity'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|freespace
name|'def'
name|'freespace'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_freespace'
newline|'\n'
nl|'\n'
DECL|member|build_path
dedent|''
name|'def'
name|'build_path'
op|'('
name|'self'
op|','
op|'*'
name|'paths'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs and returns a DatastorePath.\n\n        :param paths: list of path components, for constructing a path relative\n                      to the root directory of the datastore\n        :return: a DatastorePath object\n        """'
newline|'\n'
name|'return'
name|'DatastorePath'
op|'('
name|'self'
op|'.'
name|'_name'
op|','
op|'*'
name|'paths'
op|')'
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
string|"'[%s]'"
op|'%'
name|'self'
op|'.'
name|'_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DatastorePath
dedent|''
dedent|''
name|'class'
name|'DatastorePath'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for representing a directory or file path in a vSphere datatore.\n\n    This provides various helper methods to access components and useful\n    variants of the datastore path.\n\n    Example usage:\n\n    DatastorePath("datastore1", "_base/foo", "foo.vmdk") creates an\n    object that describes the "[datastore1] _base/foo/foo.vmdk" datastore\n    file path to a virtual disk.\n\n    Note:\n\n    * Datastore path representations always uses forward slash as separator\n      (hence the use of the posixpath module).\n    * Datastore names are enclosed in square brackets.\n    * Path part of datastore path is relative to the root directory\n      of the datastore, and is always separated from the [ds_name] part with\n      a single space.\n\n    """'
newline|'\n'
nl|'\n'
DECL|variable|VMDK_EXTENSION
name|'VMDK_EXTENSION'
op|'='
string|'"vmdk"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'datastore_name'
op|','
op|'*'
name|'paths'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'datastore_name'
name|'is'
name|'None'
name|'or'
name|'datastore_name'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"datastore name empty"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_datastore_name'
op|'='
name|'datastore_name'
newline|'\n'
name|'self'
op|'.'
name|'_rel_path'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'paths'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'None'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"path component cannot be None"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_rel_path'
op|'='
name|'posixpath'
op|'.'
name|'join'
op|'('
op|'*'
name|'paths'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Full datastore path to the file or directory."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_rel_path'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"[%s] %s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'_datastore_name'
op|','
name|'self'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"[%s]"'
op|'%'
name|'self'
op|'.'
name|'_datastore_name'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s(%s, %s)"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
nl|'\n'
name|'self'
op|'.'
name|'datastore'
op|','
name|'self'
op|'.'
name|'rel_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|datastore
name|'def'
name|'datastore'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_datastore_name'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|parent
name|'def'
name|'parent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'DatastorePath'
op|'('
name|'self'
op|'.'
name|'datastore'
op|','
name|'posixpath'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|basename
name|'def'
name|'basename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'posixpath'
op|'.'
name|'basename'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|dirname
name|'def'
name|'dirname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'posixpath'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|rel_path
name|'def'
name|'rel_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_rel_path'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
name|'self'
op|','
op|'*'
name|'paths'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'paths'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'None'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"path component cannot be None"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'DatastorePath'
op|'('
name|'self'
op|'.'
name|'datastore'
op|','
nl|'\n'
name|'posixpath'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_rel_path'
op|','
op|'*'
name|'paths'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'isinstance'
op|'('
name|'other'
op|','
name|'DatastorePath'
op|')'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'_datastore_name'
op|'=='
name|'other'
op|'.'
name|'_datastore_name'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'_rel_path'
op|'=='
name|'other'
op|'.'
name|'_rel_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__hash__
dedent|''
name|'def'
name|'__hash__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|')'
op|'.'
name|'__hash__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|parse
name|'def'
name|'parse'
op|'('
name|'cls'
op|','
name|'datastore_path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructs a DatastorePath object given a datastore path string."""'
newline|'\n'
name|'if'
name|'not'
name|'datastore_path'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|'"datastore path empty"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'spl'
op|'='
name|'datastore_path'
op|'.'
name|'split'
op|'('
string|"'['"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
string|"']'"
op|','
number|'1'
op|')'
newline|'\n'
name|'path'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'spl'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'datastore_name'
op|'='
name|'spl'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'datastore_name'
op|','
name|'path'
op|'='
name|'spl'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
name|'datastore_name'
op|','
name|'path'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(mdbooth): this convenience function is temporarily duplicated in'
nl|'\n'
comment|'# vm_util. The correct fix is to handle paginated results as they are returned'
nl|'\n'
comment|'# from the relevant vim_util function. However, vim_util is currently'
nl|'\n'
comment|'# effectively deprecated as we migrate to oslo.vmware. This duplication will be'
nl|'\n'
comment|'# removed when we fix it properly in oslo.vmware.'
nl|'\n'
DECL|function|_get_token
dedent|''
dedent|''
name|'def'
name|'_get_token'
op|'('
name|'results'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the token from the property results."""'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'results'
op|','
string|"'token'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_select_datastore
dedent|''
name|'def'
name|'_select_datastore'
op|'('
name|'data_stores'
op|','
name|'best_match'
op|','
name|'datastore_regex'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find the most preferable datastore in a given RetrieveResult object.\n\n    :param data_stores: a RetrieveResult object from vSphere API call\n    :param best_match: the current best match for datastore\n    :param datastore_regex: an optional regular expression to match names\n    :return: datastore_ref, datastore_name, capacity, freespace\n    """'
newline|'\n'
nl|'\n'
comment|'# data_stores is actually a RetrieveResult object from vSphere API call'
nl|'\n'
name|'for'
name|'obj_content'
name|'in'
name|'data_stores'
op|'.'
name|'objects'
op|':'
newline|'\n'
comment|'# the propset attribute "need not be set" by returning API'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'obj_content'
op|','
string|"'propSet'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'propdict'
op|'='
name|'vm_util'
op|'.'
name|'propset_dict'
op|'('
name|'obj_content'
op|'.'
name|'propSet'
op|')'
newline|'\n'
name|'if'
name|'_is_datastore_valid'
op|'('
name|'propdict'
op|','
name|'datastore_regex'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new_ds'
op|'='
name|'Datastore'
op|'('
nl|'\n'
name|'ref'
op|'='
name|'obj_content'
op|'.'
name|'obj'
op|','
nl|'\n'
name|'name'
op|'='
name|'propdict'
op|'['
string|"'summary.name'"
op|']'
op|','
nl|'\n'
name|'capacity'
op|'='
name|'propdict'
op|'['
string|"'summary.capacity'"
op|']'
op|','
nl|'\n'
name|'freespace'
op|'='
name|'propdict'
op|'['
string|"'summary.freeSpace'"
op|']'
op|')'
newline|'\n'
comment|'# favor datastores with more free space'
nl|'\n'
name|'if'
op|'('
name|'best_match'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'new_ds'
op|'.'
name|'freespace'
op|'>'
name|'best_match'
op|'.'
name|'freespace'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'best_match'
op|'='
name|'new_ds'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'best_match'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_datastore_valid
dedent|''
name|'def'
name|'_is_datastore_valid'
op|'('
name|'propdict'
op|','
name|'datastore_regex'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks if a datastore is valid based on the following criteria.\n\n       Criteria:\n       - Datastore is accessible\n       - Datastore is not in maintenance mode (optional)\n       - Datastore is of a supported disk type\n       - Datastore matches the supplied regex (optional)\n\n       :param propdict: datastore summary dict\n       :param datastore_regex : Regex to match the name of a datastore.\n    """'
newline|'\n'
nl|'\n'
comment|"# Local storage identifier vSphere doesn't support CIFS or"
nl|'\n'
comment|'# vfat for datastores, therefore filtered'
nl|'\n'
name|'return'
op|'('
name|'propdict'
op|'.'
name|'get'
op|'('
string|"'summary.accessible'"
op|')'
name|'and'
nl|'\n'
op|'('
name|'propdict'
op|'.'
name|'get'
op|'('
string|"'summary.maintenanceMode'"
op|')'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'propdict'
op|'.'
name|'get'
op|'('
string|"'summary.maintenanceMode'"
op|')'
op|'=='
string|"'normal'"
op|')'
name|'and'
nl|'\n'
name|'propdict'
op|'['
string|"'summary.type'"
op|']'
name|'in'
name|'ALLOWED_DATASTORE_TYPES'
name|'and'
nl|'\n'
op|'('
name|'datastore_regex'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'datastore_regex'
op|'.'
name|'match'
op|'('
name|'propdict'
op|'['
string|"'summary.name'"
op|']'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_datastore
dedent|''
name|'def'
name|'get_datastore'
op|'('
name|'session'
op|','
name|'cluster'
op|','
name|'datastore_regex'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the datastore list and choose the most preferable one."""'
newline|'\n'
name|'datastore_ret'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'vim_util'
op|','
nl|'\n'
string|'"get_dynamic_property"'
op|','
name|'cluster'
op|','
nl|'\n'
string|'"ClusterComputeResource"'
op|','
string|'"datastore"'
op|')'
newline|'\n'
comment|'# If there are no hosts in the cluster then an empty string is'
nl|'\n'
comment|'# returned'
nl|'\n'
name|'if'
name|'not'
name|'datastore_ret'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data_store_mors'
op|'='
name|'datastore_ret'
op|'.'
name|'ManagedObjectReference'
newline|'\n'
name|'data_stores'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_properties_for_a_collection_of_objects"'
op|','
nl|'\n'
string|'"Datastore"'
op|','
name|'data_store_mors'
op|','
nl|'\n'
op|'['
string|'"summary.type"'
op|','
string|'"summary.name"'
op|','
nl|'\n'
string|'"summary.capacity"'
op|','
string|'"summary.freeSpace"'
op|','
nl|'\n'
string|'"summary.accessible"'
op|','
nl|'\n'
string|'"summary.maintenanceMode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'best_match'
op|'='
name|'None'
newline|'\n'
name|'while'
name|'data_stores'
op|':'
newline|'\n'
indent|'        '
name|'best_match'
op|'='
name|'_select_datastore'
op|'('
name|'data_stores'
op|','
name|'best_match'
op|','
nl|'\n'
name|'datastore_regex'
op|')'
newline|'\n'
name|'token'
op|'='
name|'_get_token'
op|'('
name|'data_stores'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
dedent|''
name|'data_stores'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"continue_to_get_objects"'
op|','
nl|'\n'
name|'token'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'best_match'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'best_match'
newline|'\n'
dedent|''
name|'if'
name|'datastore_regex'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Datastore regex %s did not match any datastores"'
op|')'
nl|'\n'
op|'%'
name|'datastore_regex'
op|'.'
name|'pattern'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_allowed_datastores
dedent|''
dedent|''
name|'def'
name|'_get_allowed_datastores'
op|'('
name|'data_stores'
op|','
name|'datastore_regex'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'allowed'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'obj_content'
name|'in'
name|'data_stores'
op|'.'
name|'objects'
op|':'
newline|'\n'
comment|'# the propset attribute "need not be set" by returning API'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'obj_content'
op|','
string|"'propSet'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'propdict'
op|'='
name|'vm_util'
op|'.'
name|'propset_dict'
op|'('
name|'obj_content'
op|'.'
name|'propSet'
op|')'
newline|'\n'
name|'if'
name|'_is_datastore_valid'
op|'('
name|'propdict'
op|','
name|'datastore_regex'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'allowed'
op|'.'
name|'append'
op|'('
name|'Datastore'
op|'('
name|'ref'
op|'='
name|'obj_content'
op|'.'
name|'obj'
op|','
nl|'\n'
name|'name'
op|'='
name|'propdict'
op|'['
string|"'summary.name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'allowed'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_available_datastores
dedent|''
name|'def'
name|'get_available_datastores'
op|'('
name|'session'
op|','
name|'cluster'
op|'='
name|'None'
op|','
name|'datastore_regex'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the datastore list and choose the first local storage."""'
newline|'\n'
name|'if'
name|'cluster'
op|':'
newline|'\n'
indent|'        '
name|'mobj'
op|'='
name|'cluster'
newline|'\n'
name|'resource_type'
op|'='
string|'"ClusterComputeResource"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'mobj'
op|'='
name|'vm_util'
op|'.'
name|'get_host_ref'
op|'('
name|'session'
op|')'
newline|'\n'
name|'resource_type'
op|'='
string|'"HostSystem"'
newline|'\n'
dedent|''
name|'ds'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_dynamic_property"'
op|','
name|'mobj'
op|','
nl|'\n'
name|'resource_type'
op|','
string|'"datastore"'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ds'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'data_store_mors'
op|'='
name|'ds'
op|'.'
name|'ManagedObjectReference'
newline|'\n'
comment|'# NOTE(garyk): use utility method to retrieve remote objects'
nl|'\n'
name|'data_stores'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"get_properties_for_a_collection_of_objects"'
op|','
nl|'\n'
string|'"Datastore"'
op|','
name|'data_store_mors'
op|','
nl|'\n'
op|'['
string|'"summary.type"'
op|','
string|'"summary.name"'
op|','
string|'"summary.accessible"'
op|','
nl|'\n'
string|'"summary.maintenanceMode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'allowed'
op|'='
op|'['
op|']'
newline|'\n'
name|'while'
name|'data_stores'
op|':'
newline|'\n'
indent|'        '
name|'allowed'
op|'.'
name|'extend'
op|'('
name|'_get_allowed_datastores'
op|'('
name|'data_stores'
op|','
name|'datastore_regex'
op|')'
op|')'
newline|'\n'
name|'token'
op|'='
name|'_get_token'
op|'('
name|'data_stores'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'token'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'data_stores'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
nl|'\n'
string|'"continue_to_get_objects"'
op|','
nl|'\n'
name|'token'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'allowed'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'session'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Deleting the datastore file %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
name|'vim'
op|'='
name|'session'
op|'.'
name|'vim'
newline|'\n'
name|'file_delete_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'vim'
op|','
nl|'\n'
string|'"DeleteDatastoreFile_Task"'
op|','
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'name'
op|'='
name|'str'
op|'('
name|'ds_path'
op|')'
op|','
nl|'\n'
name|'datacenter'
op|'='
name|'dc_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'file_delete_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Deleted the datastore file"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_move
dedent|''
name|'def'
name|'file_move'
op|'('
name|'session'
op|','
name|'dc_ref'
op|','
name|'src_file'
op|','
name|'dst_file'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Moves the source file or folder to the destination.\n\n    The list of possible faults that the server can return on error\n    include:\n\n    * CannotAccessFile: Thrown if the source file or folder cannot be\n      moved because of insufficient permissions.\n    * FileAlreadyExists: Thrown if a file with the given name already\n      exists at the destination.\n    * FileFault: Thrown if there is a generic file error\n    * FileLocked: Thrown if the source file or folder is currently\n      locked or in use.\n    * FileNotFound: Thrown if the file or folder specified by sourceName\n      is not found.\n    * InvalidDatastore: Thrown if the operation cannot be performed on\n      the source or destination datastores.\n    * NoDiskSpace: Thrown if there is not enough space available on the\n      destination datastore.\n    * RuntimeFault: Thrown if any type of runtime fault is thrown that\n      is not covered by the other faults; for example,\n      a communication error.\n\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Moving file from %(src)s to %(dst)s."'
op|','
nl|'\n'
op|'{'
string|"'src'"
op|':'
name|'src_file'
op|','
string|"'dst'"
op|':'
name|'dst_file'
op|'}'
op|')'
newline|'\n'
name|'vim'
op|'='
name|'session'
op|'.'
name|'vim'
newline|'\n'
name|'move_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'vim'
op|','
nl|'\n'
string|'"MoveDatastoreFile_Task"'
op|','
nl|'\n'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'sourceName'
op|'='
name|'str'
op|'('
name|'src_file'
op|')'
op|','
nl|'\n'
name|'sourceDatacenter'
op|'='
name|'dc_ref'
op|','
nl|'\n'
name|'destinationName'
op|'='
name|'str'
op|'('
name|'dst_file'
op|')'
op|','
nl|'\n'
name|'destinationDatacenter'
op|'='
name|'dc_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'move_task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"File moved"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|search_datastore_spec
dedent|''
name|'def'
name|'search_datastore_spec'
op|'('
name|'client_factory'
op|','
name|'file_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the datastore search spec."""'
newline|'\n'
name|'search_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostDatastoreBrowserSearchSpec'"
op|')'
newline|'\n'
name|'search_spec'
op|'.'
name|'matchPattern'
op|'='
op|'['
name|'file_name'
op|']'
newline|'\n'
name|'return'
name|'search_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_exists
dedent|''
name|'def'
name|'file_exists'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|','
name|'file_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the file exists on the datastore."""'
newline|'\n'
name|'client_factory'
op|'='
name|'session'
op|'.'
name|'vim'
op|'.'
name|'client'
op|'.'
name|'factory'
newline|'\n'
name|'search_spec'
op|'='
name|'search_datastore_spec'
op|'('
name|'client_factory'
op|','
name|'file_name'
op|')'
newline|'\n'
name|'search_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'vim'
op|','
nl|'\n'
string|'"SearchDatastore_Task"'
op|','
nl|'\n'
name|'ds_browser'
op|','
nl|'\n'
name|'datastorePath'
op|'='
name|'str'
op|'('
name|'ds_path'
op|')'
op|','
nl|'\n'
name|'searchSpec'
op|'='
name|'search_spec'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'task_info'
op|'='
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'search_task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'vexc'
op|'.'
name|'FileNotFoundException'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'file_exists'
op|'='
op|'('
name|'getattr'
op|'('
name|'task_info'
op|'.'
name|'result'
op|','
string|"'file'"
op|','
name|'False'
op|')'
name|'and'
nl|'\n'
name|'task_info'
op|'.'
name|'result'
op|'.'
name|'file'
op|'['
number|'0'
op|']'
op|'.'
name|'path'
op|'=='
name|'file_name'
op|')'
newline|'\n'
name|'return'
name|'file_exists'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkdir
dedent|''
name|'def'
name|'mkdir'
op|'('
name|'session'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a directory at the path specified. If it is just "NAME",\n    then a directory with this name is created at the topmost level of the\n    DataStore.\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating directory with path %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'session'
op|'.'
name|'vim'
op|','
string|'"MakeDirectory"'
op|','
nl|'\n'
name|'session'
op|'.'
name|'vim'
op|'.'
name|'service_content'
op|'.'
name|'fileManager'
op|','
nl|'\n'
name|'name'
op|'='
name|'str'
op|'('
name|'ds_path'
op|')'
op|','
name|'datacenter'
op|'='
name|'dc_ref'
op|','
nl|'\n'
name|'createParentDirectories'
op|'='
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Created directory with path %s"'
op|','
name|'ds_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_sub_folders
dedent|''
name|'def'
name|'get_sub_folders'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a set of subfolders for a path on a datastore.\n\n    If the path does not exist then an empty set is returned.\n    """'
newline|'\n'
name|'search_task'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'vim'
op|','
nl|'\n'
string|'"SearchDatastore_Task"'
op|','
nl|'\n'
name|'ds_browser'
op|','
nl|'\n'
name|'datastorePath'
op|'='
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'task_info'
op|'='
name|'session'
op|'.'
name|'_wait_for_task'
op|'('
name|'search_task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'vexc'
op|'.'
name|'FileNotFoundException'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
op|')'
newline|'\n'
comment|'# populate the folder entries'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'task_info'
op|'.'
name|'result'
op|','
string|"'file'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'set'
op|'('
op|'['
name|'file'
op|'.'
name|'path'
name|'for'
name|'file'
name|'in'
name|'task_info'
op|'.'
name|'result'
op|'.'
name|'file'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'set'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
