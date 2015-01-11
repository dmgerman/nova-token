begin_unit
comment|'# Copyright (c) 2015 The Johns Hopkins University/Applied Physics Laboratory'
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
string|'"""\nKey manager implementation for Barbican\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'array'
newline|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'binascii'
newline|'\n'
nl|'\n'
name|'from'
name|'barbicanclient'
name|'import'
name|'client'
name|'as'
name|'barbican_client'
newline|'\n'
name|'from'
name|'keystoneclient'
name|'import'
name|'session'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key'
name|'as'
name|'keymgr_key'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key_mgr'
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
DECL|variable|barbican_opts
name|'barbican_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'catalog_info'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'key-manager:barbican:public'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Info to match when looking for barbican in the service '"
nl|'\n'
string|"'catalog. Format is: separated values of the form: '"
nl|'\n'
string|"'<service_type>:<service_name>:<endpoint_type>'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'endpoint_template'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Override service catalog lookup with template for '"
nl|'\n'
string|"'barbican endpoint e.g. '"
nl|'\n'
string|"'http://localhost:9311/v1/%(project_id)s'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'os_region_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Region name of this node'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|BARBICAN_OPT_GROUP
name|'BARBICAN_OPT_GROUP'
op|'='
string|"'barbican'"
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'barbican_opts'
op|','
name|'group'
op|'='
name|'BARBICAN_OPT_GROUP'
op|')'
newline|'\n'
nl|'\n'
name|'session'
op|'.'
name|'Session'
op|'.'
name|'register_conf_options'
op|'('
name|'CONF'
op|','
name|'BARBICAN_OPT_GROUP'
op|')'
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
DECL|class|BarbicanKeyManager
name|'class'
name|'BarbicanKeyManager'
op|'('
name|'key_mgr'
op|'.'
name|'KeyManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Key Manager Interface that wraps the Barbican client API."""'
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
name|'self'
op|'.'
name|'_barbican_client'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_base_url'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_barbican_client
dedent|''
name|'def'
name|'_get_barbican_client'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a client to connect to the Barbican service.\n\n        :param ctxt: the user context for authentication\n        :return: a Barbican Client object\n        :raises Forbidden: if the ctxt is None\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_barbican_client'
op|':'
newline|'\n'
comment|'# Confirm context is provided, if not raise forbidden'
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'ctxt'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"User is not authorized to use key manager."'
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
name|'Forbidden'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_SESSION'
op|'='
name|'session'
op|'.'
name|'Session'
op|'.'
name|'load_from_conf_options'
op|'('
nl|'\n'
name|'CONF'
op|','
nl|'\n'
name|'BARBICAN_OPT_GROUP'
op|')'
newline|'\n'
nl|'\n'
name|'auth'
op|'='
name|'ctxt'
op|'.'
name|'get_auth_plugin'
op|'('
op|')'
newline|'\n'
name|'service_type'
op|','
name|'service_name'
op|','
name|'interface'
op|'='
op|'('
name|'CONF'
op|'.'
nl|'\n'
name|'barbican'
op|'.'
nl|'\n'
name|'catalog_info'
op|'.'
nl|'\n'
name|'split'
op|'('
string|"':'"
op|')'
op|')'
newline|'\n'
name|'region_name'
op|'='
name|'CONF'
op|'.'
name|'barbican'
op|'.'
name|'os_region_name'
newline|'\n'
name|'service_parameters'
op|'='
op|'{'
string|"'service_type'"
op|':'
name|'service_type'
op|','
nl|'\n'
string|"'service_name'"
op|':'
name|'service_name'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'interface'
op|','
nl|'\n'
string|"'region_name'"
op|':'
name|'region_name'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'barbican'
op|'.'
name|'endpoint_template'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_base_url'
op|'='
op|'('
name|'CONF'
op|'.'
name|'barbican'
op|'.'
name|'endpoint_template'
op|'%'
nl|'\n'
name|'ctxt'
op|'.'
name|'to_dict'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_base_url'
op|'='
name|'_SESSION'
op|'.'
name|'get_endpoint'
op|'('
nl|'\n'
name|'auth'
op|','
op|'**'
name|'service_parameters'
op|')'
newline|'\n'
nl|'\n'
comment|"# the barbican endpoint can't have the '/v1' on the end"
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_barbican_endpoint'
op|'='
name|'self'
op|'.'
name|'_base_url'
op|'.'
name|'rpartition'
op|'('
string|"'/'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'sess'
op|'='
name|'session'
op|'.'
name|'Session'
op|'('
name|'auth'
op|'='
name|'auth'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_barbican_client'
op|'='
name|'barbican_client'
op|'.'
name|'Client'
op|'('
nl|'\n'
name|'session'
op|'='
name|'sess'
op|','
nl|'\n'
name|'endpoint'
op|'='
name|'self'
op|'.'
name|'_barbican_endpoint'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error creating Barbican client: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_barbican_client'
newline|'\n'
nl|'\n'
DECL|member|create_key
dedent|''
name|'def'
name|'create_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'expiration'
op|'='
name|'None'
op|','
name|'name'
op|'='
string|"'Nova Compute Key'"
op|','
nl|'\n'
name|'payload_content_type'
op|'='
string|"'application/octet-stream'"
op|','
name|'mode'
op|'='
string|"'CBC'"
op|','
nl|'\n'
name|'algorithm'
op|'='
string|"'AES'"
op|','
name|'length'
op|'='
number|'256'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a key.\n\n        :param ctxt: contains information of the user and the environment\n                     for the request (nova/context.py)\n        :param expiration: the date the key will expire\n        :param name: a friendly name for the secret\n        :param payload_content_type: the format/type of the secret data\n        :param mode: the algorithm mode (e.g. CBC or CTR mode)\n        :param algorithm: the algorithm associated with the secret\n        :param length: the bit length of the secret\n\n        :return: the UUID of the new key\n        :raises Exception: if key creation fails\n        """'
newline|'\n'
name|'barbican_client'
op|'='
name|'self'
op|'.'
name|'_get_barbican_client'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'key_order'
op|'='
name|'barbican_client'
op|'.'
name|'orders'
op|'.'
name|'create_key'
op|'('
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'algorithm'
op|','
nl|'\n'
name|'length'
op|','
nl|'\n'
name|'mode'
op|','
nl|'\n'
name|'payload_content_type'
op|','
nl|'\n'
name|'expiration'
op|')'
newline|'\n'
name|'order_ref'
op|'='
name|'key_order'
op|'.'
name|'submit'
op|'('
op|')'
newline|'\n'
name|'order'
op|'='
name|'barbican_client'
op|'.'
name|'orders'
op|'.'
name|'get'
op|'('
name|'order_ref'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_retrieve_secret_uuid'
op|'('
name|'order'
op|'.'
name|'secret_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error creating key: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|store_key
dedent|''
dedent|''
dedent|''
name|'def'
name|'store_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key'
op|','
name|'expiration'
op|'='
name|'None'
op|','
name|'name'
op|'='
string|"'Nova Compute Key'"
op|','
nl|'\n'
name|'payload_content_type'
op|'='
string|"'application/octet-stream'"
op|','
nl|'\n'
name|'payload_content_encoding'
op|'='
string|"'base64'"
op|','
name|'algorithm'
op|'='
string|"'AES'"
op|','
nl|'\n'
name|'bit_length'
op|'='
number|'256'
op|','
name|'mode'
op|'='
string|"'CBC'"
op|','
name|'from_copy'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stores (i.e., registers) a key with the key manager.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param key: the unencrypted secret data. Known as "payload" to the\n                    barbicanclient api\n        :param expiration: the expiration time of the secret in ISO 8601\n                           format\n        :param name: a friendly name for the key\n        :param payload_content_type: the format/type of the secret data\n        :param payload_content_encoding: the encoding of the secret data\n        :param algorithm: the algorithm associated with this secret key\n        :param bit_length: the bit length of this secret key\n        :param mode: the algorithm mode used with this secret key\n        :param from_copy: establishes whether the function is being used\n                    to copy a key. In case of the latter, it does not\n                    try to decode the key\n\n        :returns: the UUID of the stored key\n        :raises Exception: if key storage fails\n        """'
newline|'\n'
name|'barbican_client'
op|'='
name|'self'
op|'.'
name|'_get_barbican_client'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'.'
name|'get_algorithm'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'algorithm'
op|'='
name|'key'
op|'.'
name|'get_algorithm'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'payload_content_type'
op|'=='
string|"'text/plain'"
op|':'
newline|'\n'
indent|'                '
name|'payload_content_encoding'
op|'='
name|'None'
newline|'\n'
name|'encoded_key'
op|'='
name|'key'
op|'.'
name|'get_encoded'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'payload_content_type'
op|'=='
string|"'application/octet-stream'"
name|'and'
nl|'\n'
name|'not'
name|'from_copy'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'key_list'
op|'='
name|'key'
op|'.'
name|'get_encoded'
op|'('
op|')'
newline|'\n'
name|'string_key'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'map'
op|'('
name|'lambda'
name|'byte'
op|':'
string|'"%02x"'
op|'%'
name|'byte'
op|','
name|'key_list'
op|')'
op|')'
newline|'\n'
name|'encoded_key'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'binascii'
op|'.'
name|'unhexlify'
op|'('
name|'string_key'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'encoded_key'
op|'='
name|'key'
op|'.'
name|'get_encoded'
op|'('
op|')'
newline|'\n'
dedent|''
name|'secret'
op|'='
name|'barbican_client'
op|'.'
name|'secrets'
op|'.'
name|'create'
op|'('
name|'name'
op|','
nl|'\n'
name|'encoded_key'
op|','
nl|'\n'
name|'payload_content_type'
op|','
nl|'\n'
name|'payload_content_encoding'
op|','
nl|'\n'
name|'algorithm'
op|','
nl|'\n'
name|'bit_length'
op|','
nl|'\n'
name|'mode'
op|','
nl|'\n'
name|'expiration'
op|')'
newline|'\n'
name|'secret_ref'
op|'='
name|'secret'
op|'.'
name|'store'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_retrieve_secret_uuid'
op|'('
name|'secret_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error storing key: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy_key
dedent|''
dedent|''
dedent|''
name|'def'
name|'copy_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copies (i.e., clones) a key stored by barbican.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param key_id: the UUID of the key to copy\n        :return: the UUID of the key copy\n        :raises Exception: if key copying fails\n        """'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'secret'
op|'='
name|'self'
op|'.'
name|'_get_secret'
op|'('
name|'ctxt'
op|','
name|'key_id'
op|')'
newline|'\n'
name|'con_type'
op|'='
name|'secret'
op|'.'
name|'content_types'
op|'['
string|"'default'"
op|']'
newline|'\n'
name|'secret_data'
op|'='
name|'self'
op|'.'
name|'_get_secret_data'
op|'('
name|'secret'
op|','
nl|'\n'
name|'payload_content_type'
op|'='
name|'con_type'
op|')'
newline|'\n'
name|'key'
op|'='
name|'keymgr_key'
op|'.'
name|'SymmetricKey'
op|'('
name|'secret'
op|'.'
name|'algorithm'
op|','
name|'secret_data'
op|')'
newline|'\n'
name|'copy_uuid'
op|'='
name|'self'
op|'.'
name|'store_key'
op|'('
name|'ctxt'
op|','
name|'key'
op|','
name|'secret'
op|'.'
name|'expiration'
op|','
nl|'\n'
name|'secret'
op|'.'
name|'name'
op|','
name|'con_type'
op|','
nl|'\n'
string|"'base64'"
op|','
nl|'\n'
name|'secret'
op|'.'
name|'algorithm'
op|','
name|'secret'
op|'.'
name|'bit_length'
op|','
nl|'\n'
name|'secret'
op|'.'
name|'mode'
op|','
name|'True'
op|')'
newline|'\n'
name|'return'
name|'copy_uuid'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error copying key: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_secret_ref
dedent|''
dedent|''
dedent|''
name|'def'
name|'_create_secret_ref'
op|'('
name|'self'
op|','
name|'key_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates the URL required for accessing a secret.\n\n        :param key_id: the UUID of the key to copy\n\n        :return: the URL of the requested secret\n        """'
newline|'\n'
name|'if'
name|'not'
name|'key_id'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'"Key ID is None"'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'KeyManagerError'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_base_url'
op|'+'
string|'"/secrets/"'
op|'+'
name|'key_id'
newline|'\n'
nl|'\n'
DECL|member|_retrieve_secret_uuid
dedent|''
name|'def'
name|'_retrieve_secret_uuid'
op|'('
name|'self'
op|','
name|'secret_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieves the UUID of the secret from the secret_ref.\n\n        :param secret_ref: the href of the secret\n\n        :return: the UUID of the secret\n        """'
newline|'\n'
nl|'\n'
comment|'# The secret_ref is assumed to be of a form similar to'
nl|'\n'
comment|'# http://host:9311/v1/secrets/d152fa13-2b41-42ca-a934-6c21566c0f40'
nl|'\n'
comment|'# with the UUID at the end. This command retrieves everything'
nl|'\n'
comment|"# after the last '/', which is the UUID."
nl|'\n'
name|'return'
name|'secret_ref'
op|'.'
name|'rpartition'
op|'('
string|"'/'"
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_secret_data
dedent|''
name|'def'
name|'_get_secret_data'
op|'('
name|'self'
op|','
nl|'\n'
name|'secret'
op|','
nl|'\n'
name|'payload_content_type'
op|'='
string|"'application/octet-stream'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieves the secret data given a secret and content_type.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param secret: the secret from barbican with the payload of data\n        :param payload_content_type: the format/type of the secret data\n\n        :returns: the secret data\n        :raises Exception: if data cannot be retrieved\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'generated_data'
op|'='
name|'secret'
op|'.'
name|'payload'
newline|'\n'
name|'if'
name|'payload_content_type'
op|'=='
string|"'application/octet-stream'"
op|':'
newline|'\n'
indent|'                '
name|'secret_data'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'generated_data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'secret_data'
op|'='
name|'generated_data'
newline|'\n'
dedent|''
name|'return'
name|'secret_data'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error getting secret data: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_secret
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_secret'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the metadata of the secret.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param key_id: UUID of the secret\n\n        :return: the secret\'s metadata\n        :raises Exception: if there is an error retrieving the data\n        """'
newline|'\n'
nl|'\n'
name|'barbican_client'
op|'='
name|'self'
op|'.'
name|'_get_barbican_client'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'secret_ref'
op|'='
name|'self'
op|'.'
name|'_create_secret_ref'
op|'('
name|'key_id'
op|')'
newline|'\n'
name|'return'
name|'barbican_client'
op|'.'
name|'secrets'
op|'.'
name|'get'
op|'('
name|'secret_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error getting secret metadata: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_key
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key_id'
op|','
nl|'\n'
name|'payload_content_type'
op|'='
string|"'application/octet-stream'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieves the specified key.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param key_id: the UUID of the key to retrieve\n        :param payload_content_type: The format/type of the secret data\n\n        :return: SymmetricKey representation of the key\n        :raises Exception: if key retrieval fails\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'secret'
op|'='
name|'self'
op|'.'
name|'_get_secret'
op|'('
name|'ctxt'
op|','
name|'key_id'
op|')'
newline|'\n'
name|'secret_data'
op|'='
name|'self'
op|'.'
name|'_get_secret_data'
op|'('
name|'secret'
op|','
nl|'\n'
name|'payload_content_type'
op|')'
newline|'\n'
name|'if'
name|'payload_content_type'
op|'=='
string|"'application/octet-stream'"
op|':'
newline|'\n'
comment|'# convert decoded string to list of unsigned ints for each byte'
nl|'\n'
indent|'                '
name|'key_data'
op|'='
name|'array'
op|'.'
name|'array'
op|'('
string|"'B'"
op|','
nl|'\n'
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'secret_data'
op|')'
op|')'
op|'.'
name|'tolist'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'key_data'
op|'='
name|'secret_data'
newline|'\n'
dedent|''
name|'key'
op|'='
name|'keymgr_key'
op|'.'
name|'SymmetricKey'
op|'('
name|'secret'
op|'.'
name|'algorithm'
op|','
name|'key_data'
op|')'
newline|'\n'
name|'return'
name|'key'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error getting key: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_key
dedent|''
dedent|''
dedent|''
name|'def'
name|'delete_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the specified key.\n\n        :param ctxt: contains information of the user and the environment for\n                     the request (nova/context.py)\n        :param key_id: the UUID of the key to delete\n        :raises Exception: if key deletion fails\n        """'
newline|'\n'
name|'barbican_client'
op|'='
name|'self'
op|'.'
name|'_get_barbican_client'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'secret_ref'
op|'='
name|'self'
op|'.'
name|'_create_secret_ref'
op|'('
name|'key_id'
op|')'
newline|'\n'
name|'barbican_client'
op|'.'
name|'secrets'
op|'.'
name|'delete'
op|'('
name|'secret_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error deleting key: %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
