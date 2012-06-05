begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""Policy Engine For Nova"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|policy_opts
name|'policy_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'policy_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'policy.json'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'JSON file representing policy'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'policy_default_rule'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'default'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Rule checked when requested rule is not found'"
op|')'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'policy_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_POLICY_PATH
name|'_POLICY_PATH'
op|'='
name|'None'
newline|'\n'
DECL|variable|_POLICY_CACHE
name|'_POLICY_CACHE'
op|'='
op|'{'
op|'}'
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
name|'_POLICY_PATH'
newline|'\n'
name|'global'
name|'_POLICY_CACHE'
newline|'\n'
name|'_POLICY_PATH'
op|'='
name|'None'
newline|'\n'
name|'_POLICY_CACHE'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init
dedent|''
name|'def'
name|'init'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_POLICY_PATH'
newline|'\n'
name|'global'
name|'_POLICY_CACHE'
newline|'\n'
name|'if'
name|'not'
name|'_POLICY_PATH'
op|':'
newline|'\n'
indent|'        '
name|'_POLICY_PATH'
op|'='
name|'FLAGS'
op|'.'
name|'policy_file'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'_POLICY_PATH'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_POLICY_PATH'
op|'='
name|'FLAGS'
op|'.'
name|'find_file'
op|'('
name|'_POLICY_PATH'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'_POLICY_PATH'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ConfigNotFound'
op|'('
name|'path'
op|'='
name|'FLAGS'
op|'.'
name|'policy_file'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'utils'
op|'.'
name|'read_cached_file'
op|'('
name|'_POLICY_PATH'
op|','
name|'_POLICY_CACHE'
op|','
nl|'\n'
name|'reload_func'
op|'='
name|'_set_brain'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_set_brain
dedent|''
name|'def'
name|'_set_brain'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'default_rule'
op|'='
name|'FLAGS'
op|'.'
name|'policy_default_rule'
newline|'\n'
name|'policy'
op|'.'
name|'set_brain'
op|'('
name|'policy'
op|'.'
name|'HttpBrain'
op|'.'
name|'load_json'
op|'('
name|'data'
op|','
name|'default_rule'
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Verifies that the action is valid on the target in this context.\n\n       :param context: nova context\n       :param action: string representing the action to be checked\n           this should be colon separated for clarity.\n           i.e. ``compute:create_instance``,\n           ``compute:attach_volume``,\n           ``volume:attach_volume``\n\n       :param object: dictionary representing the object of the action\n           for object creation this should be a dictionary representing the\n           location of the object e.g. ``{\'project_id\': context.project_id}``\n\n       :raises nova.exception.PolicyNotAllowed: if verification fails.\n\n    """'
newline|'\n'
name|'init'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'match_list'
op|'='
op|'('
string|"'rule:%s'"
op|'%'
name|'action'
op|','
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
nl|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'match_list'
op|','
name|'target'
op|','
name|'credentials'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'action'
op|'='
name|'action'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
