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
string|'"""Nova common internal object model"""'
newline|'\n'
nl|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'oslo_versionedobjects'
name|'import'
name|'base'
name|'as'
name|'ovoo_base'
newline|'\n'
name|'from'
name|'oslo_versionedobjects'
name|'import'
name|'exception'
name|'as'
name|'ovoo_exc'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
name|'as'
name|'obj_fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'object'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_attrname
name|'def'
name|'get_attrname'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the mangled name of the attribute\'s underlying storage."""'
newline|'\n'
comment|"# FIXME(danms): This is just until we use o.vo's class properties"
nl|'\n'
comment|'# and object base.'
nl|'\n'
name|'return'
string|"'_obj_'"
op|'+'
name|'name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaObjectRegistry
dedent|''
name|'class'
name|'NovaObjectRegistry'
op|'('
name|'ovoo_base'
op|'.'
name|'VersionedObjectRegistry'
op|')'
op|':'
newline|'\n'
DECL|member|registration_hook
indent|'    '
name|'def'
name|'registration_hook'
op|'('
name|'self'
op|','
name|'cls'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): This is called when an object is registered,'
nl|'\n'
comment|'# and is responsible for maintaining nova.objects.$OBJECT'
nl|'\n'
comment|'# as the highest-versioned implementation of a given object.'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'cls'
op|'.'
name|'VERSION'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'objects'
op|','
name|'cls'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'objects'
op|','
name|'cls'
op|'.'
name|'obj_name'
op|'('
op|')'
op|','
name|'cls'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cur_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
nl|'\n'
name|'getattr'
op|'('
name|'objects'
op|','
name|'cls'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
op|'.'
name|'VERSION'
op|')'
newline|'\n'
name|'if'
name|'version'
op|'>='
name|'cur_version'
op|':'
newline|'\n'
indent|'                '
name|'setattr'
op|'('
name|'objects'
op|','
name|'cls'
op|'.'
name|'obj_name'
op|'('
op|')'
op|','
name|'cls'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|remotable_classmethod
dedent|''
dedent|''
dedent|''
dedent|''
name|'remotable_classmethod'
op|'='
name|'ovoo_base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|variable|remotable
name|'remotable'
op|'='
name|'ovoo_base'
op|'.'
name|'remotable'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaObject
name|'class'
name|'NovaObject'
op|'('
name|'ovoo_base'
op|'.'
name|'VersionedObject'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class and object factory.\n\n    This forms the base of all objects that can be remoted or instantiated\n    via RPC. Simply defining a class that inherits from this base class\n    will make it remotely instantiatable. Objects should implement the\n    necessary "get" classmethod routines as well as "save" object methods\n    as appropriate.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|OBJ_SERIAL_NAMESPACE
name|'OBJ_SERIAL_NAMESPACE'
op|'='
string|"'nova_object'"
newline|'\n'
DECL|variable|OBJ_PROJECT_NAMESPACE
name|'OBJ_PROJECT_NAMESPACE'
op|'='
string|"'nova'"
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): Keep the compatibility bits in nova separate from o.vo'
nl|'\n'
comment|'# for the time being so that we can keep changes required to use'
nl|'\n'
comment|'# the base version of those risky methods separate from the rest of the'
nl|'\n'
comment|'# simple inherited methods.'
nl|'\n'
DECL|member|obj_calculate_child_version
name|'def'
name|'obj_calculate_child_version'
op|'('
name|'self'
op|','
name|'target_version'
op|','
name|'child'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Calculate the appropriate version for a child object.\n\n        This is to be used when backporting an object for an older client.\n        A sub-object will need to be backported to a suitable version for\n        the client as well, and this method will calculate what that\n        version should be, based on obj_relationships.\n\n        :param target_version: Version this object is being backported to\n        :param child: The child field for which the appropriate version\n                      is to be calculated\n        :returns: None if the child should be omitted from the backport,\n                  otherwise, the version to which the child should be\n                  backported\n        """'
newline|'\n'
name|'target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'for'
name|'index'
op|','
name|'versions'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'obj_relationships'
op|'['
name|'child'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'my_version'
op|','
name|'child_version'
op|'='
name|'versions'
newline|'\n'
name|'my_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'my_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
name|'my_version'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'index'
op|'=='
number|'0'
op|':'
newline|'\n'
comment|"# We're backporting to a version from before this"
nl|'\n'
comment|'# subobject was added: delete it from the primitive.'
nl|'\n'
indent|'                    '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# We're in the gap between index-1 and index, so"
nl|'\n'
comment|'# backport to the older version'
nl|'\n'
indent|'                    '
name|'return'
name|'self'
op|'.'
name|'obj_relationships'
op|'['
name|'child'
op|']'
op|'['
name|'index'
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'target_version'
op|'=='
name|'my_version'
op|':'
newline|'\n'
comment|'# This is the first mapping that satisfies the'
nl|'\n'
comment|'# target_version request: backport the object.'
nl|'\n'
indent|'                '
name|'return'
name|'child_version'
newline|'\n'
comment|'# No need to backport, as far as we know, so return the latest'
nl|'\n'
comment|'# version of the sub-object we know about'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'obj_relationships'
op|'['
name|'child'
op|']'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): This has some minor change between the nova and o.vo'
nl|'\n'
comment|'# version, so avoid inheriting it for the moment so we can make that'
nl|'\n'
comment|'# transition separately for clarity.'
nl|'\n'
DECL|member|obj_reset_changes
dedent|''
name|'def'
name|'obj_reset_changes'
op|'('
name|'self'
op|','
name|'fields'
op|'='
name|'None'
op|','
name|'recursive'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reset the list of fields that have been changed.\n\n        .. note::\n\n          - This is NOT "revert to previous values"\n          - Specifying fields on recursive resets will only be honored at the\n            top level. Everything below the top will reset all.\n\n        :param fields: List of fields to reset, or "all" if None.\n        :param recursive: Call obj_reset_changes(recursive=True) on\n                          any sub-objects within the list of fields\n                          being reset.\n        """'
newline|'\n'
name|'if'
name|'recursive'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'field'
name|'in'
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Ignore fields not in requested set (if applicable)'
nl|'\n'
indent|'                '
name|'if'
name|'fields'
name|'and'
name|'field'
name|'not'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Skip any fields that are unset'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'field'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'value'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'field'
op|')'
newline|'\n'
nl|'\n'
comment|"# Don't reset nulled fields"
nl|'\n'
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Reset straight Object and ListOfObjects fields'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'fields'
op|'['
name|'field'
op|']'
op|','
name|'obj_fields'
op|'.'
name|'ObjectField'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'.'
name|'obj_reset_changes'
op|'('
name|'recursive'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'fields'
op|'['
name|'field'
op|']'
op|','
nl|'\n'
name|'obj_fields'
op|'.'
name|'ListOfObjectsField'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'thing'
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'                        '
name|'thing'
op|'.'
name|'obj_reset_changes'
op|'('
name|'recursive'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'if'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_changed_fields'
op|'-='
name|'set'
op|'('
name|'fields'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_changed_fields'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): This is nova-specific'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|member|obj_alternate_context
name|'def'
name|'obj_alternate_context'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'original_context'
op|'='
name|'self'
op|'.'
name|'_context'
newline|'\n'
name|'self'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_context'
op|'='
name|'original_context'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): This is nova-specific'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|member|obj_as_admin
name|'def'
name|'obj_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Context manager to make an object call as an admin.\n\n        This temporarily modifies the context embedded in an object to\n        be elevated() and restores it after the call completes. Example\n        usage:\n\n           with obj.obj_as_admin():\n               obj.save()\n\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_context'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'OrphanedObjectError'
op|'('
name|'method'
op|'='
string|"'obj_as_admin'"
op|','
nl|'\n'
name|'objtype'
op|'='
name|'self'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'original_context'
op|'='
name|'self'
op|'.'
name|'_context'
newline|'\n'
name|'self'
op|'.'
name|'_context'
op|'='
name|'self'
op|'.'
name|'_context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'yield'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_context'
op|'='
name|'original_context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaObjectDictCompat
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaObjectDictCompat'
op|'('
name|'ovoo_base'
op|'.'
name|'VersionedObjectDictCompat'
op|')'
op|':'
newline|'\n'
DECL|member|__iter__
indent|'    '
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'name'
name|'in'
name|'self'
op|'.'
name|'obj_fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'name'
op|')'
name|'or'
nl|'\n'
name|'name'
name|'in'
name|'self'
op|'.'
name|'obj_extra_fields'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'name'
newline|'\n'
nl|'\n'
DECL|member|keys
dedent|''
dedent|''
dedent|''
name|'def'
name|'keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'list'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaTimestampObject
dedent|''
dedent|''
name|'class'
name|'NovaTimestampObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mixin class for db backed objects with timestamp fields.\n\n    Sqlalchemy models that inherit from the oslo_db TimestampMixin will include\n    these fields and the corresponding objects will benefit from this mixin.\n    """'
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'obj_fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'obj_fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaPersistentObject
dedent|''
name|'class'
name|'NovaPersistentObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mixin class for Persistent objects.\n\n    This adds the fields that we use in common for most persistent objects.\n    """'
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'obj_fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'obj_fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'obj_fields'
op|'.'
name|'DateTimeField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'obj_fields'
op|'.'
name|'BooleanField'
op|'('
name|'default'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ObjectListBase
dedent|''
name|'class'
name|'ObjectListBase'
op|'('
name|'ovoo_base'
op|'.'
name|'ObjectListBase'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): These are for transition to using the oslo'
nl|'\n'
comment|'# base object and can be removed when we move to it.'
nl|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_obj_primitive_key
name|'def'
name|'_obj_primitive_key'
op|'('
name|'cls'
op|','
name|'field'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'nova_object.%s'"
op|'%'
name|'field'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_obj_primitive_field
name|'def'
name|'_obj_primitive_field'
op|'('
name|'cls'
op|','
name|'primitive'
op|','
name|'field'
op|','
nl|'\n'
name|'default'
op|'='
name|'obj_fields'
op|'.'
name|'UnspecifiedDefault'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'cls'
op|'.'
name|'_obj_primitive_key'
op|'('
name|'field'
op|')'
newline|'\n'
name|'if'
name|'default'
op|'=='
name|'obj_fields'
op|'.'
name|'UnspecifiedDefault'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'primitive'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'primitive'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(rlrossit): This can get removed after ovo uses both child_versions'
nl|'\n'
comment|'# and obj_relationships when making the internal objects compatible'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
dedent|''
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'primitives'
op|'='
name|'primitive'
op|'['
string|"'objects'"
op|']'
newline|'\n'
name|'target_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'child_versions'
op|':'
newline|'\n'
indent|'            '
name|'child_target_version'
op|'='
name|'self'
op|'.'
name|'child_versions'
op|'.'
name|'get'
op|'('
name|'target_version'
op|','
nl|'\n'
string|"'1.0'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'child_target_version'
op|'='
string|"'1.0'"
newline|'\n'
name|'rel_versions'
op|'='
name|'self'
op|'.'
name|'obj_relationships'
op|'['
string|"'objects'"
op|']'
newline|'\n'
name|'for'
name|'index'
op|','
name|'versions'
name|'in'
name|'enumerate'
op|'('
name|'rel_versions'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'my_version'
op|','
name|'child_version'
op|'='
name|'versions'
newline|'\n'
name|'my_version'
op|'='
name|'utils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'my_version'
op|')'
newline|'\n'
name|'if'
name|'target_version'
op|'<'
name|'my_version'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'index'
op|'=='
number|'0'
op|':'
newline|'\n'
comment|'# if the target is before we existed, delete objects'
nl|'\n'
comment|'# from the primitive'
nl|'\n'
comment|'# (we should never get here, because lists should'
nl|'\n'
comment|"# always have an 'objects' field)"
nl|'\n'
indent|'                        '
name|'del'
name|'primitive'
op|'['
string|"'objects'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# We still don't match, but we'll grab the latest"
nl|'\n'
comment|'# child version up to this point'
nl|'\n'
indent|'                        '
name|'child_target_version'
op|'='
name|'rel_versions'
op|'['
name|'index'
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'target_version'
op|'=='
name|'my_version'
op|':'
newline|'\n'
indent|'                    '
name|'child_target_version'
op|'='
name|'child_version'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'for'
name|'index'
op|','
name|'item'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'objects'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'objects'
op|'['
name|'index'
op|']'
op|'.'
name|'obj_make_compatible'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_obj_primitive_field'
op|'('
name|'primitives'
op|'['
name|'index'
op|']'
op|','
string|"'data'"
op|')'
op|','
nl|'\n'
name|'child_target_version'
op|')'
newline|'\n'
name|'verkey'
op|'='
name|'self'
op|'.'
name|'_obj_primitive_key'
op|'('
string|"'version'"
op|')'
newline|'\n'
name|'primitives'
op|'['
name|'index'
op|']'
op|'['
name|'verkey'
op|']'
op|'='
name|'child_target_version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaObjectSerializer
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaObjectSerializer'
op|'('
name|'messaging'
op|'.'
name|'NoOpSerializer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A NovaObject-aware Serializer.\n\n    This implements the Oslo Serializer interface and provides the\n    ability to serialize and deserialize NovaObject entities. Any service\n    that needs to accept or return NovaObjects as arguments or result values\n    should pass this to its RPCClient and RPCServer objects.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|conductor
name|'def'
name|'conductor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
string|"'_conductor'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'self'
op|'.'
name|'_conductor'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_conductor'
newline|'\n'
nl|'\n'
DECL|member|_process_object
dedent|''
name|'def'
name|'_process_object'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objprim'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'objinst'
op|'='
name|'NovaObject'
op|'.'
name|'obj_from_primitive'
op|'('
name|'objprim'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ovoo_exc'
op|'.'
name|'IncompatibleObjectVersion'
op|':'
newline|'\n'
indent|'            '
name|'objver'
op|'='
name|'objprim'
op|'['
string|"'nova_object.version'"
op|']'
newline|'\n'
name|'if'
name|'objver'
op|'.'
name|'count'
op|'('
string|"'.'"
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
comment|'# NOTE(danms): For our purposes, the .z part of the version'
nl|'\n'
comment|'# should be safe to accept without requiring a backport'
nl|'\n'
indent|'                '
name|'objprim'
op|'['
string|"'nova_object.version'"
op|']'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
name|'objver'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|':'
number|'2'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_process_object'
op|'('
name|'context'
op|','
name|'objprim'
op|')'
newline|'\n'
dedent|''
name|'objname'
op|'='
name|'objprim'
op|'['
string|"'nova_object.name'"
op|']'
newline|'\n'
name|'version_manifest'
op|'='
name|'ovoo_base'
op|'.'
name|'obj_tree_get_versions'
op|'('
name|'objname'
op|')'
newline|'\n'
name|'if'
name|'objname'
name|'in'
name|'version_manifest'
op|':'
newline|'\n'
indent|'                '
name|'objinst'
op|'='
name|'self'
op|'.'
name|'conductor'
op|'.'
name|'object_backport_versions'
op|'('
nl|'\n'
name|'context'
op|','
name|'objprim'
op|','
name|'version_manifest'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'objinst'
newline|'\n'
nl|'\n'
DECL|member|_process_iterable
dedent|''
name|'def'
name|'_process_iterable'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'action_fn'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Process an iterable, taking an action on each value.\n        :param:context: Request context\n        :param:action_fn: Action to take on each item in values\n        :param:values: Iterable container of things to take action on\n        :returns: A new container of the same type (except set) with\n                  items from values having had action applied.\n        """'
newline|'\n'
name|'iterable'
op|'='
name|'values'
op|'.'
name|'__class__'
newline|'\n'
name|'if'
name|'issubclass'
op|'('
name|'iterable'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'iterable'
op|'('
op|'**'
op|'{'
name|'k'
op|':'
name|'action_fn'
op|'('
name|'context'
op|','
name|'v'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'values'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# NOTE(danms, gibi) A set can't have an unhashable value inside,"
nl|'\n'
comment|'# such as a dict. Convert the set to list, which is fine, since we'
nl|'\n'
comment|"# can't send them over RPC anyway. We convert it to list as this"
nl|'\n'
comment|'# way there will be no semantic change between the fake rpc driver'
nl|'\n'
comment|'# used in functional test and a normal rpc driver.'
nl|'\n'
indent|'            '
name|'if'
name|'iterable'
op|'=='
name|'set'
op|':'
newline|'\n'
indent|'                '
name|'iterable'
op|'='
name|'list'
newline|'\n'
dedent|''
name|'return'
name|'iterable'
op|'('
op|'['
name|'action_fn'
op|'('
name|'context'
op|','
name|'value'
op|')'
name|'for'
name|'value'
name|'in'
name|'values'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialize_entity
dedent|''
dedent|''
name|'def'
name|'serialize_entity'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'entity'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'entity'
op|','
op|'('
name|'tuple'
op|','
name|'list'
op|','
name|'set'
op|','
name|'dict'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'entity'
op|'='
name|'self'
op|'.'
name|'_process_iterable'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'serialize_entity'
op|','
nl|'\n'
name|'entity'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'hasattr'
op|'('
name|'entity'
op|','
string|"'obj_to_primitive'"
op|')'
name|'and'
nl|'\n'
name|'callable'
op|'('
name|'entity'
op|'.'
name|'obj_to_primitive'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'entity'
op|'='
name|'entity'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'entity'
newline|'\n'
nl|'\n'
DECL|member|deserialize_entity
dedent|''
name|'def'
name|'deserialize_entity'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'entity'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'entity'
op|','
name|'dict'
op|')'
name|'and'
string|"'nova_object.name'"
name|'in'
name|'entity'
op|':'
newline|'\n'
indent|'            '
name|'entity'
op|'='
name|'self'
op|'.'
name|'_process_object'
op|'('
name|'context'
op|','
name|'entity'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'entity'
op|','
op|'('
name|'tuple'
op|','
name|'list'
op|','
name|'set'
op|','
name|'dict'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'entity'
op|'='
name|'self'
op|'.'
name|'_process_iterable'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'deserialize_entity'
op|','
nl|'\n'
name|'entity'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'entity'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|obj_to_primitive
dedent|''
dedent|''
name|'def'
name|'obj_to_primitive'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Recursively turn an object into a python primitive.\n\n    A NovaObject becomes a dict, and anything that implements ObjectListBase\n    becomes a list.\n    """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'ObjectListBase'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'obj_to_primitive'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'obj'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'obj'
op|'.'
name|'obj_fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'obj'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'key'
op|')'
name|'or'
name|'key'
name|'in'
name|'obj'
op|'.'
name|'obj_extra_fields'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'key'
op|']'
op|'='
name|'obj_to_primitive'
op|'('
name|'getattr'
op|'('
name|'obj'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'obj'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'obj'
op|','
name|'netaddr'
op|'.'
name|'IPNetwork'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'obj'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|obj_make_list
dedent|''
dedent|''
name|'def'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'list_obj'
op|','
name|'item_cls'
op|','
name|'db_list'
op|','
op|'**'
name|'extra_args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Construct an object list from a list of primitives.\n\n    This calls item_cls._from_db_object() on each item of db_list, and\n    adds the resulting object to list_obj.\n\n    :param:context: Request context\n    :param:list_obj: An ObjectListBase object\n    :param:item_cls: The NovaObject class of the objects within the list\n    :param:db_list: The list of primitives to convert to objects\n    :param:extra_args: Extra arguments to pass to _from_db_object()\n    :returns: list_obj\n    """'
newline|'\n'
name|'list_obj'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'db_item'
name|'in'
name|'db_list'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'item_cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'item_cls'
op|'('
op|')'
op|','
name|'db_item'
op|','
nl|'\n'
op|'**'
name|'extra_args'
op|')'
newline|'\n'
name|'list_obj'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
name|'list_obj'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'list_obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'list_obj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serialize_args
dedent|''
name|'def'
name|'serialize_args'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator that will do the arguments serialization before remoting."""'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'obj'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'arg'
op|')'
name|'if'
name|'isinstance'
op|'('
name|'arg'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
nl|'\n'
name|'else'
name|'arg'
name|'for'
name|'arg'
name|'in'
name|'args'
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
op|'=='
string|"'exc_val'"
name|'and'
name|'v'
op|':'
newline|'\n'
indent|'                '
name|'kwargs'
op|'['
name|'k'
op|']'
op|'='
name|'str'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'k'
op|'=='
string|"'exc_tb'"
name|'and'
name|'v'
name|'and'
name|'not'
name|'isinstance'
op|'('
name|'v'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'kwargs'
op|'['
name|'k'
op|']'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'traceback'
op|'.'
name|'format_tb'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'v'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'kwargs'
op|'['
name|'k'
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'v'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'fn'
op|','
string|"'__call__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fn'
op|'('
name|'obj'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# NOTE(danms): We wrap a descriptor, so use that protocol'
nl|'\n'
dedent|''
name|'return'
name|'fn'
op|'.'
name|'__get__'
op|'('
name|'None'
op|','
name|'obj'
op|')'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(danms): Make this discoverable'
nl|'\n'
dedent|''
name|'wrapper'
op|'.'
name|'remotable'
op|'='
name|'getattr'
op|'('
name|'fn'
op|','
string|"'remotable'"
op|','
name|'False'
op|')'
newline|'\n'
name|'wrapper'
op|'.'
name|'original_fn'
op|'='
name|'fn'
newline|'\n'
name|'return'
op|'('
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'fn'
op|')'
op|'('
name|'wrapper'
op|')'
name|'if'
name|'hasattr'
op|'('
name|'fn'
op|','
string|"'__call__'"
op|')'
nl|'\n'
name|'else'
name|'classmethod'
op|'('
name|'wrapper'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|obj_equal_prims
dedent|''
name|'def'
name|'obj_equal_prims'
op|'('
name|'obj_1'
op|','
name|'obj_2'
op|','
name|'ignore'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Compare two primitives for equivalence ignoring some keys.\n\n    This operation tests the primitives of two objects for equivalence.\n    Object primitives may contain a list identifying fields that have been\n    changed - this is ignored in the comparison. The ignore parameter lists\n    any other keys to be ignored.\n\n    :param:obj1: The first object in the comparison\n    :param:obj2: The second object in the comparison\n    :param:ignore: A list of fields to ignore\n    :returns: True if the primitives are equal ignoring changes\n    and specified fields, otherwise False.\n    """'
newline|'\n'
nl|'\n'
DECL|function|_strip
name|'def'
name|'_strip'
op|'('
name|'prim'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'prim'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'k'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'                '
name|'prim'
op|'.'
name|'pop'
op|'('
name|'k'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'v'
name|'in'
name|'prim'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'_strip'
op|'('
name|'v'
op|','
name|'keys'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'prim'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'v'
name|'in'
name|'prim'
op|':'
newline|'\n'
indent|'                '
name|'_strip'
op|'('
name|'v'
op|','
name|'keys'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'prim'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ignore'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'nova_object.changes'"
op|']'
op|'+'
name|'ignore'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'keys'
op|'='
op|'['
string|"'nova_object.changes'"
op|']'
newline|'\n'
dedent|''
name|'prim_1'
op|'='
name|'_strip'
op|'('
name|'obj_1'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'keys'
op|')'
newline|'\n'
name|'prim_2'
op|'='
name|'_strip'
op|'('
name|'obj_2'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'keys'
op|')'
newline|'\n'
name|'return'
name|'prim_1'
op|'=='
name|'prim_2'
newline|'\n'
dedent|''
endmarker|''
end_unit
