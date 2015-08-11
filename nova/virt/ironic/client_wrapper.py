begin_unit
comment|'# coding=utf-8'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2014 Hewlett-Packard Development Company, L.P.'
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
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|ironic
name|'ironic'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IronicClientWrapper
name|'class'
name|'IronicClientWrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ironic client wrapper class that encapsulates retry logic."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialise the IronicClientWrapper for use.\n\n        Initialise IronicClientWrapper by loading ironicclient\n        dynamically so that ironicclient is not a dependency for\n        Nova.\n        """'
newline|'\n'
name|'global'
name|'ironic'
newline|'\n'
name|'if'
name|'ironic'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ironic'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
string|"'ironicclient'"
op|')'
newline|'\n'
comment|'# NOTE(deva): work around a lack of symbols in the current version.'
nl|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'ironic'
op|','
string|"'exc'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ironic'
op|'.'
name|'exc'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
string|"'ironicclient.exc'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'ironic'
op|','
string|"'client'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ironic'
op|'.'
name|'client'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
nl|'\n'
string|"'ironicclient.client'"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_cached_client'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_invalidate_cached_client
dedent|''
name|'def'
name|'_invalidate_cached_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tell the wrapper to invalidate the cached ironic-client."""'
newline|'\n'
name|'self'
op|'.'
name|'_cached_client'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_client
dedent|''
name|'def'
name|'_get_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# If we've already constructed a valid, authed client, just return"
nl|'\n'
comment|'# that.'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_cached_client'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_cached_client'
newline|'\n'
nl|'\n'
dedent|''
name|'auth_token'
op|'='
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_auth_token'
newline|'\n'
name|'if'
name|'auth_token'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'='
op|'{'
string|"'os_username'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_username'
op|','
nl|'\n'
string|"'os_password'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'os_auth_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_url'
op|','
nl|'\n'
string|"'os_tenant_name'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'admin_tenant_name'
op|','
nl|'\n'
string|"'os_service_type'"
op|':'
string|"'baremetal'"
op|','
nl|'\n'
string|"'os_endpoint_type'"
op|':'
string|"'public'"
op|','
nl|'\n'
string|"'ironic_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_endpoint'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'='
op|'{'
string|"'os_auth_token'"
op|':'
name|'auth_token'
op|','
nl|'\n'
string|"'ironic_url'"
op|':'
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_endpoint'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cli'
op|'='
name|'ironic'
op|'.'
name|'client'
op|'.'
name|'get_client'
op|'('
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_version'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|"# Cache the client so we don't have to reconstruct and"
nl|'\n'
comment|'# reauthenticate it every time we need it.'
nl|'\n'
name|'self'
op|'.'
name|'_cached_client'
op|'='
name|'cli'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'ironic'
op|'.'
name|'exc'
op|'.'
name|'Unauthorized'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to authenticate Ironic client."'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cli'
newline|'\n'
nl|'\n'
DECL|member|_multi_getattr
dedent|''
name|'def'
name|'_multi_getattr'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Support nested attribute path for getattr().\n\n        :param obj: Root object.\n        :param attr: Path of final attribute to get. E.g., "a.b.c.d"\n\n        :returns: The value of the final named attribute.\n        :raises: AttributeError will be raised if the path is invalid.\n        """'
newline|'\n'
name|'for'
name|'attribute'
name|'in'
name|'attr'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'='
name|'getattr'
op|'('
name|'obj'
op|','
name|'attribute'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
DECL|member|call
dedent|''
name|'def'
name|'call'
op|'('
name|'self'
op|','
name|'method'
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
string|'"""Call an Ironic client method and retry on errors.\n\n        :param method: Name of the client method to call as a string.\n        :param args: Client method arguments.\n        :param kwargs: Client method keyword arguments.\n\n        :raises: NovaException if all retries failed.\n        """'
newline|'\n'
name|'retry_excs'
op|'='
op|'('
name|'ironic'
op|'.'
name|'exc'
op|'.'
name|'ServiceUnavailable'
op|','
nl|'\n'
name|'ironic'
op|'.'
name|'exc'
op|'.'
name|'ConnectionRefused'
op|','
nl|'\n'
name|'ironic'
op|'.'
name|'exc'
op|'.'
name|'Conflict'
op|')'
newline|'\n'
comment|'# num_attempts should be the times of retry + 1'
nl|'\n'
comment|'# eg. retry==0 just means  run once and no retry'
nl|'\n'
name|'num_attempts'
op|'='
name|'max'
op|'('
number|'0'
op|','
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_max_retries'
op|')'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
name|'for'
name|'attempt'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'num_attempts'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'client'
op|'='
name|'self'
op|'.'
name|'_get_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_multi_getattr'
op|'('
name|'client'
op|','
name|'method'
op|')'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ironic'
op|'.'
name|'exc'
op|'.'
name|'Unauthorized'
op|':'
newline|'\n'
comment|'# In this case, the authorization token of the cached'
nl|'\n'
comment|'# ironic-client probably expired. So invalidate the cached'
nl|'\n'
comment|'# client and the next try will start with a fresh one.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'_invalidate_cached_client'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"The Ironic client became unauthorized. "'
nl|'\n'
string|'"Will attempt to reauthorize and try again."'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'retry_excs'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
comment|'# We want to perform this logic for all exception cases listed'
nl|'\n'
comment|'# above.'
nl|'\n'
dedent|''
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Error contacting Ironic server for "'
nl|'\n'
string|'"\'%(method)s\'. Attempt %(attempt)d of %(total)d"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
nl|'\n'
string|"'attempt'"
op|':'
name|'attempt'
op|','
nl|'\n'
string|"'total'"
op|':'
name|'num_attempts'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'attempt'
op|'=='
name|'num_attempts'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'ironic'
op|'.'
name|'api_retry_interval'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
