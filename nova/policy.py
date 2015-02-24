begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
string|'"""Policy Engine For Nova."""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'policy'
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
name|'__name__'
op|')'
newline|'\n'
DECL|variable|_ENFORCER
name|'_ENFORCER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset
name|'def'
name|'reset'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_ENFORCER'
newline|'\n'
name|'if'
name|'_ENFORCER'
op|':'
newline|'\n'
indent|'        '
name|'_ENFORCER'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
name|'_ENFORCER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init
dedent|''
dedent|''
name|'def'
name|'init'
op|'('
name|'policy_file'
op|'='
name|'None'
op|','
name|'rules'
op|'='
name|'None'
op|','
name|'default_rule'
op|'='
name|'None'
op|','
name|'use_conf'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Init an Enforcer class.\n\n       :param policy_file: Custom policy file to use, if none is specified,\n                           `CONF.policy_file` will be used.\n       :param rules: Default dictionary / Rules to use. It will be\n                     considered just in the first instantiation.\n       :param default_rule: Default rule to use, CONF.default_rule will\n                            be used if none is specified.\n       :param use_conf: Whether to load rules from config file.\n    """'
newline|'\n'
nl|'\n'
name|'global'
name|'_ENFORCER'
newline|'\n'
name|'if'
name|'not'
name|'_ENFORCER'
op|':'
newline|'\n'
indent|'        '
name|'_ENFORCER'
op|'='
name|'policy'
op|'.'
name|'Enforcer'
op|'('
name|'policy_file'
op|'='
name|'policy_file'
op|','
nl|'\n'
name|'rules'
op|'='
name|'rules'
op|','
nl|'\n'
name|'default_rule'
op|'='
name|'default_rule'
op|','
nl|'\n'
name|'use_conf'
op|'='
name|'use_conf'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_rules
dedent|''
dedent|''
name|'def'
name|'set_rules'
op|'('
name|'rules'
op|','
name|'overwrite'
op|'='
name|'True'
op|','
name|'use_conf'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set rules based on the provided dict of rules.\n\n       :param rules: New rules to use. It should be an instance of dict.\n       :param overwrite: Whether to overwrite current rules or update them\n                         with the new rules.\n       :param use_conf: Whether to reload rules from config file.\n    """'
newline|'\n'
nl|'\n'
name|'init'
op|'('
name|'use_conf'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_ENFORCER'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|','
name|'overwrite'
op|','
name|'use_conf'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|enforce
dedent|''
name|'def'
name|'enforce'
op|'('
name|'context'
op|','
name|'action'
op|','
name|'target'
op|','
name|'do_raise'
op|'='
name|'True'
op|','
name|'exc'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Verifies that the action is valid on the target in this context.\n\n       :param context: nova context\n       :param action: string representing the action to be checked\n           this should be colon separated for clarity.\n           i.e. ``compute:create_instance``,\n           ``compute:attach_volume``,\n           ``volume:attach_volume``\n       :param target: dictionary representing the object of the action\n           for object creation this should be a dictionary representing the\n           location of the object e.g. ``{\'project_id\': context.project_id}``\n       :param do_raise: if True (the default), raises PolicyNotAuthorized;\n           if False, returns False\n\n       :raises nova.exception.PolicyNotAuthorized: if verification fails\n           and do_raise is True.\n\n       :return: returns a non-False value (not necessarily "True") if\n           authorized, and the exact value False if not authorized and\n           do_raise is False.\n    """'
newline|'\n'
name|'init'
op|'('
op|')'
newline|'\n'
name|'credentials'
op|'='
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'_ENFORCER'
op|'.'
name|'enforce'
op|'('
name|'action'
op|','
name|'target'
op|','
name|'credentials'
op|','
nl|'\n'
name|'do_raise'
op|'='
name|'do_raise'
op|','
name|'exc'
op|'='
name|'exc'
op|','
name|'action'
op|'='
name|'action'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'credentials'
op|'.'
name|'pop'
op|'('
string|"'auth_token'"
op|','
name|'None'
op|')'
newline|'\n'
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Policy check for %(action)s failed with credentials '"
nl|'\n'
string|"'%(credentials)s'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
name|'action'
op|','
string|"'credentials'"
op|':'
name|'credentials'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_is_admin
dedent|''
name|'def'
name|'check_is_admin'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Whether or not roles contains \'admin\' role according to policy setting.\n\n    """'
newline|'\n'
nl|'\n'
name|'init'
op|'('
op|')'
newline|'\n'
comment|'# the target is user-self'
nl|'\n'
name|'credentials'
op|'='
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'credentials'
newline|'\n'
name|'return'
name|'_ENFORCER'
op|'.'
name|'enforce'
op|'('
string|"'context_is_admin'"
op|','
name|'target'
op|','
name|'credentials'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'policy'
op|'.'
name|'register'
op|'('
string|"'is_admin'"
op|')'
newline|'\n'
DECL|class|IsAdminCheck
name|'class'
name|'IsAdminCheck'
op|'('
name|'policy'
op|'.'
name|'Check'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An explicit check for is_admin."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'kind'
op|','
name|'match'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the check."""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expected'
op|'='
op|'('
name|'match'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'true'"
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'IsAdminCheck'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'kind'
op|','
name|'str'
op|'('
name|'self'
op|'.'
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'target'
op|','
name|'creds'
op|','
name|'enforcer'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Determine whether is_admin matches the requested value."""'
newline|'\n'
nl|'\n'
name|'return'
name|'creds'
op|'['
string|"'is_admin'"
op|']'
op|'=='
name|'self'
op|'.'
name|'expected'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rules
dedent|''
dedent|''
name|'def'
name|'get_rules'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'_ENFORCER'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_ENFORCER'
op|'.'
name|'rules'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
