begin_unit
comment|'# Copyright 2012 Red Hat, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
string|'"""\ngettext for openstack-common modules.\n\nUsual usage in an openstack.common module:\n\n    from nova.openstack.common.gettextutils import _\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'locale'
newline|'\n'
name|'from'
name|'logging'
name|'import'
name|'handlers'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'babel'
name|'import'
name|'localedata'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
DECL|variable|_AVAILABLE_LANGUAGES
name|'_AVAILABLE_LANGUAGES'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# FIXME(dhellmann): Remove this when moving to oslo.i18n.'
nl|'\n'
DECL|variable|USE_LAZY
name|'USE_LAZY'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TranslatorFactory
name|'class'
name|'TranslatorFactory'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create translator functions\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'domain'
op|','
name|'lazy'
op|'='
name|'False'
op|','
name|'localedir'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Establish a set of translation functions for the domain.\n\n        :param domain: Name of translation domain,\n                       specifying a message catalog.\n        :type domain: str\n        :param lazy: Delays translation until a message is emitted.\n                     Defaults to False.\n        :type lazy: Boolean\n        :param localedir: Directory with translation catalogs.\n        :type localedir: str\n        """'
newline|'\n'
name|'self'
op|'.'
name|'domain'
op|'='
name|'domain'
newline|'\n'
name|'self'
op|'.'
name|'lazy'
op|'='
name|'lazy'
newline|'\n'
name|'if'
name|'localedir'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'localedir'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'domain'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
string|"'_LOCALEDIR'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'localedir'
op|'='
name|'localedir'
newline|'\n'
nl|'\n'
DECL|member|_make_translation_func
dedent|''
name|'def'
name|'_make_translation_func'
op|'('
name|'self'
op|','
name|'domain'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a new translation function ready for use.\n\n        Takes into account whether or not lazy translation is being\n        done.\n\n        The domain can be specified to override the default from the\n        factory, but the localedir from the factory is always used\n        because we assume the log-level translation catalogs are\n        installed in the same directory as the main application\n        catalog.\n\n        """'
newline|'\n'
name|'if'
name|'domain'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'domain'
op|'='
name|'self'
op|'.'
name|'domain'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'lazy'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'functools'
op|'.'
name|'partial'
op|'('
name|'Message'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
dedent|''
name|'t'
op|'='
name|'gettext'
op|'.'
name|'translation'
op|'('
nl|'\n'
name|'domain'
op|','
nl|'\n'
name|'localedir'
op|'='
name|'self'
op|'.'
name|'localedir'
op|','
nl|'\n'
name|'fallback'
op|'='
name|'True'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'t'
op|'.'
name|'gettext'
newline|'\n'
dedent|''
name|'return'
name|'t'
op|'.'
name|'ugettext'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|primary
name|'def'
name|'primary'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"The default translation function."'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_translation_func'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_log_translation_func
dedent|''
name|'def'
name|'_make_log_translation_func'
op|'('
name|'self'
op|','
name|'level'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_make_translation_func'
op|'('
name|'self'
op|'.'
name|'domain'
op|'+'
string|"'-log-'"
op|'+'
name|'level'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|log_info
name|'def'
name|'log_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Translate info-level log messages."'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_log_translation_func'
op|'('
string|"'info'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|log_warning
name|'def'
name|'log_warning'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Translate warning-level log messages."'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_log_translation_func'
op|'('
string|"'warning'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|log_error
name|'def'
name|'log_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Translate error-level log messages."'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_log_translation_func'
op|'('
string|"'error'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|log_critical
name|'def'
name|'log_critical'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Translate critical-level log messages."'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_log_translation_func'
op|'('
string|"'critical'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(dhellmann): When this module moves out of the incubator into'
nl|'\n'
comment|'# oslo.i18n, these global variables can be moved to an integration'
nl|'\n'
comment|'# module within each application.'
nl|'\n'
nl|'\n'
comment|'# Create the global translation functions.'
nl|'\n'
DECL|variable|_translators
dedent|''
dedent|''
name|'_translators'
op|'='
name|'TranslatorFactory'
op|'('
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
comment|'# The primary translation function using the well-known name "_"'
nl|'\n'
DECL|variable|_
name|'_'
op|'='
name|'_translators'
op|'.'
name|'primary'
newline|'\n'
nl|'\n'
comment|'# Translators for log levels.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The abbreviated names are meant to reflect the usual use of a short'
nl|'\n'
comment|'# name like \'_\'. The "L" is for "log" and the other letter comes from'
nl|'\n'
comment|'# the level.'
nl|'\n'
DECL|variable|_LI
name|'_LI'
op|'='
name|'_translators'
op|'.'
name|'log_info'
newline|'\n'
DECL|variable|_LW
name|'_LW'
op|'='
name|'_translators'
op|'.'
name|'log_warning'
newline|'\n'
DECL|variable|_LE
name|'_LE'
op|'='
name|'_translators'
op|'.'
name|'log_error'
newline|'\n'
DECL|variable|_LC
name|'_LC'
op|'='
name|'_translators'
op|'.'
name|'log_critical'
newline|'\n'
nl|'\n'
comment|"# NOTE(dhellmann): End of globals that will move to the application's"
nl|'\n'
comment|'# integration module.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|enable_lazy
name|'def'
name|'enable_lazy'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convenience function for configuring _() to use lazy gettext\n\n    Call this at the start of execution to enable the gettextutils._\n    function to use lazy gettext functionality. This is useful if\n    your project is importing _ directly instead of using the\n    gettextutils.install() way of importing the _ function.\n    """'
newline|'\n'
comment|'# FIXME(dhellmann): This function will be removed in oslo.i18n,'
nl|'\n'
comment|'# because the TranslatorFactory makes it superfluous.'
nl|'\n'
name|'global'
name|'_'
op|','
name|'_LI'
op|','
name|'_LW'
op|','
name|'_LE'
op|','
name|'_LC'
op|','
name|'USE_LAZY'
newline|'\n'
name|'tf'
op|'='
name|'TranslatorFactory'
op|'('
string|"'nova'"
op|','
name|'lazy'
op|'='
name|'True'
op|')'
newline|'\n'
name|'_'
op|'='
name|'tf'
op|'.'
name|'primary'
newline|'\n'
name|'_LI'
op|'='
name|'tf'
op|'.'
name|'log_info'
newline|'\n'
name|'_LW'
op|'='
name|'tf'
op|'.'
name|'log_warning'
newline|'\n'
name|'_LE'
op|'='
name|'tf'
op|'.'
name|'log_error'
newline|'\n'
name|'_LC'
op|'='
name|'tf'
op|'.'
name|'log_critical'
newline|'\n'
name|'USE_LAZY'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|install
dedent|''
name|'def'
name|'install'
op|'('
name|'domain'
op|','
name|'lazy'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Install a _() function using the given translation domain.\n\n    Given a translation domain, install a _() function using gettext\'s\n    install() function.\n\n    The main difference from gettext.install() is that we allow\n    overriding the default localedir (e.g. /usr/share/locale) using\n    a translation-domain-specific environment variable (e.g.\n    NOVA_LOCALEDIR).\n\n    :param domain: the translation domain\n    :param lazy: indicates whether or not to install the lazy _() function.\n                 The lazy _() introduces a way to do deferred translation\n                 of messages by installing a _ that builds Message objects,\n                 instead of strings, which can then be lazily translated into\n                 any available locale.\n    """'
newline|'\n'
name|'if'
name|'lazy'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'six'
name|'import'
name|'moves'
newline|'\n'
name|'tf'
op|'='
name|'TranslatorFactory'
op|'('
name|'domain'
op|','
name|'lazy'
op|'='
name|'True'
op|')'
newline|'\n'
name|'moves'
op|'.'
name|'builtins'
op|'.'
name|'__dict__'
op|'['
string|"'_'"
op|']'
op|'='
name|'tf'
op|'.'
name|'primary'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'localedir'
op|'='
string|"'%s_LOCALEDIR'"
op|'%'
name|'domain'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'gettext'
op|'.'
name|'install'
op|'('
name|'domain'
op|','
nl|'\n'
name|'localedir'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'localedir'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'gettext'
op|'.'
name|'install'
op|'('
name|'domain'
op|','
nl|'\n'
name|'localedir'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'localedir'
op|')'
op|','
nl|'\n'
name|'unicode'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Message
dedent|''
dedent|''
dedent|''
name|'class'
name|'Message'
op|'('
name|'six'
op|'.'
name|'text_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Message object is a unicode object that can be translated.\n\n    Translation of Message is done explicitly using the translate() method.\n    For all non-translation intents and purposes, a Message is simply unicode,\n    and can be treated as such.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__new__
name|'def'
name|'__new__'
op|'('
name|'cls'
op|','
name|'msgid'
op|','
name|'msgtext'
op|'='
name|'None'
op|','
name|'params'
op|'='
name|'None'
op|','
nl|'\n'
name|'domain'
op|'='
string|"'nova'"
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new Message object.\n\n        In order for translation to work gettext requires a message ID, this\n        msgid will be used as the base unicode text. It is also possible\n        for the msgid and the base unicode text to be different by passing\n        the msgtext parameter.\n        """'
newline|'\n'
comment|'# If the base msgtext is not given, we use the default translation'
nl|'\n'
comment|'# of the msgid (which is in English) just in case the system locale is'
nl|'\n'
comment|'# not English, so that the base text will be in that locale by default.'
nl|'\n'
name|'if'
name|'not'
name|'msgtext'
op|':'
newline|'\n'
indent|'            '
name|'msgtext'
op|'='
name|'Message'
op|'.'
name|'_translate_msgid'
op|'('
name|'msgid'
op|','
name|'domain'
op|')'
newline|'\n'
comment|'# We want to initialize the parent unicode with the actual object that'
nl|'\n'
comment|"# would have been plain unicode if 'Message' was not enabled."
nl|'\n'
dedent|''
name|'msg'
op|'='
name|'super'
op|'('
name|'Message'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|','
name|'msgtext'
op|')'
newline|'\n'
name|'msg'
op|'.'
name|'msgid'
op|'='
name|'msgid'
newline|'\n'
name|'msg'
op|'.'
name|'domain'
op|'='
name|'domain'
newline|'\n'
name|'msg'
op|'.'
name|'params'
op|'='
name|'params'
newline|'\n'
name|'return'
name|'msg'
newline|'\n'
nl|'\n'
DECL|member|translate
dedent|''
name|'def'
name|'translate'
op|'('
name|'self'
op|','
name|'desired_locale'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Translate this message to the desired locale.\n\n        :param desired_locale: The desired locale to translate the message to,\n                               if no locale is provided the message will be\n                               translated to the system\'s default locale.\n\n        :returns: the translated message in unicode\n        """'
newline|'\n'
nl|'\n'
name|'translated_message'
op|'='
name|'Message'
op|'.'
name|'_translate_msgid'
op|'('
name|'self'
op|'.'
name|'msgid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
name|'desired_locale'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'params'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# No need for more translation'
nl|'\n'
indent|'            '
name|'return'
name|'translated_message'
newline|'\n'
nl|'\n'
comment|'# This Message object may have been formatted with one or more'
nl|'\n'
comment|'# Message objects as substitution arguments, given either as a single'
nl|'\n'
comment|'# argument, part of a tuple, or as one or more values in a dictionary.'
nl|'\n'
comment|'# When translating this Message we need to translate those Messages too'
nl|'\n'
dedent|''
name|'translated_params'
op|'='
name|'_translate_args'
op|'('
name|'self'
op|'.'
name|'params'
op|','
name|'desired_locale'
op|')'
newline|'\n'
nl|'\n'
name|'translated_message'
op|'='
name|'translated_message'
op|'%'
name|'translated_params'
newline|'\n'
nl|'\n'
name|'return'
name|'translated_message'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_translate_msgid
name|'def'
name|'_translate_msgid'
op|'('
name|'msgid'
op|','
name|'domain'
op|','
name|'desired_locale'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'desired_locale'
op|':'
newline|'\n'
indent|'            '
name|'system_locale'
op|'='
name|'locale'
op|'.'
name|'getdefaultlocale'
op|'('
op|')'
newline|'\n'
comment|'# If the system locale is not available to the runtime use English'
nl|'\n'
name|'if'
name|'not'
name|'system_locale'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'desired_locale'
op|'='
string|"'en_US'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'desired_locale'
op|'='
name|'system_locale'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'locale_dir'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'domain'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
string|"'_LOCALEDIR'"
op|')'
newline|'\n'
name|'lang'
op|'='
name|'gettext'
op|'.'
name|'translation'
op|'('
name|'domain'
op|','
nl|'\n'
name|'localedir'
op|'='
name|'locale_dir'
op|','
nl|'\n'
name|'languages'
op|'='
op|'['
name|'desired_locale'
op|']'
op|','
nl|'\n'
name|'fallback'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'translator'
op|'='
name|'lang'
op|'.'
name|'gettext'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'translator'
op|'='
name|'lang'
op|'.'
name|'ugettext'
newline|'\n'
nl|'\n'
dedent|''
name|'translated_message'
op|'='
name|'translator'
op|'('
name|'msgid'
op|')'
newline|'\n'
name|'return'
name|'translated_message'
newline|'\n'
nl|'\n'
DECL|member|__mod__
dedent|''
name|'def'
name|'__mod__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
comment|'# When we mod a Message we want the actual operation to be performed'
nl|'\n'
comment|'# by the parent class (i.e. unicode()), the only thing  we do here is'
nl|'\n'
comment|'# save the original msgid and the parameters in case of a translation'
nl|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_sanitize_mod_params'
op|'('
name|'other'
op|')'
newline|'\n'
name|'unicode_mod'
op|'='
name|'super'
op|'('
name|'Message'
op|','
name|'self'
op|')'
op|'.'
name|'__mod__'
op|'('
name|'params'
op|')'
newline|'\n'
name|'modded'
op|'='
name|'Message'
op|'('
name|'self'
op|'.'
name|'msgid'
op|','
nl|'\n'
name|'msgtext'
op|'='
name|'unicode_mod'
op|','
nl|'\n'
name|'params'
op|'='
name|'params'
op|','
nl|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'domain'
op|')'
newline|'\n'
name|'return'
name|'modded'
newline|'\n'
nl|'\n'
DECL|member|_sanitize_mod_params
dedent|''
name|'def'
name|'_sanitize_mod_params'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sanitize the object being modded with this Message.\n\n        - Add support for modding \'None\' so translation supports it\n        - Trim the modded object, which can be a large dictionary, to only\n        those keys that would actually be used in a translation\n        - Snapshot the object being modded, in case the message is\n        translated, it will be used as it was when the Message was created\n        """'
newline|'\n'
name|'if'
name|'other'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'('
name|'other'
op|','
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'other'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
comment|'# Merge the dictionaries'
nl|'\n'
comment|'# Copy each item in case one does not support deep copy.'
nl|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'params'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'self'
op|'.'
name|'params'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'params'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'_copy_param'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'other'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'.'
name|'_copy_param'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'self'
op|'.'
name|'_copy_param'
op|'('
name|'other'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'params'
newline|'\n'
nl|'\n'
DECL|member|_copy_param
dedent|''
name|'def'
name|'_copy_param'
op|'('
name|'self'
op|','
name|'param'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'param'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|'# Fallback to casting to unicode this will handle the'
nl|'\n'
comment|"# python code-like objects that can't be deep-copied"
nl|'\n'
indent|'            '
name|'return'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__add__
dedent|''
dedent|''
name|'def'
name|'__add__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Message objects do not support addition.'"
op|')'
newline|'\n'
name|'raise'
name|'TypeError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__radd__
dedent|''
name|'def'
name|'__radd__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__add__'
op|'('
name|'other'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'six'
op|'.'
name|'PY2'
op|':'
newline|'\n'
DECL|function|__str__
indent|'        '
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(luisg): Logging in python 2.6 tries to str() log records,'
nl|'\n'
comment|'# and it expects specifically a UnicodeError in order to proceed.'
nl|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Message objects do not support str() because they may '"
nl|'\n'
string|"'contain non-ascii characters. '"
nl|'\n'
string|"'Please use unicode() or translate() instead.'"
op|')'
newline|'\n'
name|'raise'
name|'UnicodeError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_available_languages
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_available_languages'
op|'('
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Lists the available languages for the given translation domain.\n\n    :param domain: the domain to get languages for\n    """'
newline|'\n'
name|'if'
name|'domain'
name|'in'
name|'_AVAILABLE_LANGUAGES'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'copy'
op|'.'
name|'copy'
op|'('
name|'_AVAILABLE_LANGUAGES'
op|'['
name|'domain'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'localedir'
op|'='
string|"'%s_LOCALEDIR'"
op|'%'
name|'domain'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'find'
op|'='
name|'lambda'
name|'x'
op|':'
name|'gettext'
op|'.'
name|'find'
op|'('
name|'domain'
op|','
nl|'\n'
name|'localedir'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
name|'localedir'
op|')'
op|','
nl|'\n'
name|'languages'
op|'='
op|'['
name|'x'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mrodden): en_US should always be available (and first in case'
nl|'\n'
comment|'# order matters) since our in-line message strings are en_US'
nl|'\n'
name|'language_list'
op|'='
op|'['
string|"'en_US'"
op|']'
newline|'\n'
comment|'# NOTE(luisg): Babel <1.0 used a function called list(), which was'
nl|'\n'
comment|'# renamed to locale_identifiers() in >=1.0, the requirements master list'
nl|'\n'
comment|'# requires >=0.9.6, uncapped, so defensively work with both. We can remove'
nl|'\n'
comment|'# this check when the master list updates to >=1.0, and update all projects'
nl|'\n'
name|'list_identifiers'
op|'='
op|'('
name|'getattr'
op|'('
name|'localedata'
op|','
string|"'list'"
op|','
name|'None'
op|')'
name|'or'
nl|'\n'
name|'getattr'
op|'('
name|'localedata'
op|','
string|"'locale_identifiers'"
op|')'
op|')'
newline|'\n'
name|'locale_identifiers'
op|'='
name|'list_identifiers'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'locale_identifiers'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'find'
op|'('
name|'i'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'language_list'
op|'.'
name|'append'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(luisg): Babel>=1.0,<1.3 has a bug where some OpenStack supported'
nl|'\n'
comment|"# locales (e.g. 'zh_CN', and 'zh_TW') aren't supported even though they"
nl|'\n'
comment|'# are perfectly legitimate locales:'
nl|'\n'
comment|'#     https://github.com/mitsuhiko/babel/issues/37'
nl|'\n'
comment|'# In Babel 1.3 they fixed the bug and they support these locales, but'
nl|'\n'
comment|'# they are still not explicitly "listed" by locale_identifiers().'
nl|'\n'
comment|'# That is  why we add the locales here explicitly if necessary so that'
nl|'\n'
comment|'# they are listed as supported.'
nl|'\n'
dedent|''
dedent|''
name|'aliases'
op|'='
op|'{'
string|"'zh'"
op|':'
string|"'zh_CN'"
op|','
nl|'\n'
string|"'zh_Hant_HK'"
op|':'
string|"'zh_HK'"
op|','
nl|'\n'
string|"'zh_Hant'"
op|':'
string|"'zh_TW'"
op|','
nl|'\n'
string|"'fil'"
op|':'
string|"'tl_PH'"
op|'}'
newline|'\n'
name|'for'
op|'('
name|'locale'
op|','
name|'alias'
op|')'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'aliases'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'locale'
name|'in'
name|'language_list'
name|'and'
name|'alias'
name|'not'
name|'in'
name|'language_list'
op|':'
newline|'\n'
indent|'            '
name|'language_list'
op|'.'
name|'append'
op|'('
name|'alias'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'_AVAILABLE_LANGUAGES'
op|'['
name|'domain'
op|']'
op|'='
name|'language_list'
newline|'\n'
name|'return'
name|'copy'
op|'.'
name|'copy'
op|'('
name|'language_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|translate
dedent|''
name|'def'
name|'translate'
op|'('
name|'obj'
op|','
name|'desired_locale'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the translated unicode representation of the given object.\n\n    If the object is not translatable it is returned as-is.\n    If the locale is None the object is translated to the system locale.\n\n    :param obj: the object to translate\n    :param desired_locale: the locale to translate the message to, if None the\n                           default system locale will be used\n    :returns: the translated object in unicode, or the original object if\n              it could not be translated\n    """'
newline|'\n'
name|'message'
op|'='
name|'obj'
newline|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'message'
op|','
name|'Message'
op|')'
op|':'
newline|'\n'
comment|'# If the object to translate is not already translatable,'
nl|'\n'
comment|"# let's first get its unicode representation"
nl|'\n'
indent|'        '
name|'message'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'obj'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'message'
op|','
name|'Message'
op|')'
op|':'
newline|'\n'
comment|'# Even after unicoding() we still need to check if we are'
nl|'\n'
comment|'# running with translatable unicode before translating'
nl|'\n'
indent|'        '
name|'return'
name|'message'
op|'.'
name|'translate'
op|'('
name|'desired_locale'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_args
dedent|''
name|'def'
name|'_translate_args'
op|'('
name|'args'
op|','
name|'desired_locale'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Translates all the translatable elements of the given arguments object.\n\n    This method is used for translating the translatable values in method\n    arguments which include values of tuples or dictionaries.\n    If the object is not a tuple or a dictionary the object itself is\n    translated if it is translatable.\n\n    If the locale is None the object is translated to the system locale.\n\n    :param args: the args to translate\n    :param desired_locale: the locale to translate the args to, if None the\n                           default system locale will be used\n    :returns: a new args object with the translated contents of the original\n    """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'args'
op|','
name|'tuple'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'tuple'
op|'('
name|'translate'
op|'('
name|'v'
op|','
name|'desired_locale'
op|')'
name|'for'
name|'v'
name|'in'
name|'args'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'args'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'translated_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'translated_v'
op|'='
name|'translate'
op|'('
name|'v'
op|','
name|'desired_locale'
op|')'
newline|'\n'
name|'translated_dict'
op|'['
name|'k'
op|']'
op|'='
name|'translated_v'
newline|'\n'
dedent|''
name|'return'
name|'translated_dict'
newline|'\n'
dedent|''
name|'return'
name|'translate'
op|'('
name|'args'
op|','
name|'desired_locale'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TranslationHandler
dedent|''
name|'class'
name|'TranslationHandler'
op|'('
name|'handlers'
op|'.'
name|'MemoryHandler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Handler that translates records before logging them.\n\n    The TranslationHandler takes a locale and a target logging.Handler object\n    to forward LogRecord objects to after translating them. This handler\n    depends on Message objects being logged, instead of regular strings.\n\n    The handler can be configured declaratively in the logging.conf as follows:\n\n        [handlers]\n        keys = translatedlog, translator\n\n        [handler_translatedlog]\n        class = handlers.WatchedFileHandler\n        args = (\'/var/log/api-localized.log\',)\n        formatter = context\n\n        [handler_translator]\n        class = openstack.common.log.TranslationHandler\n        target = translatedlog\n        args = (\'zh_CN\',)\n\n    If the specified locale is not available in the system, the handler will\n    log in the default locale.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'locale'
op|'='
name|'None'
op|','
name|'target'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize a TranslationHandler\n\n        :param locale: locale to use for translating messages\n        :param target: logging.Handler object to forward\n                       LogRecord objects to after translation\n        """'
newline|'\n'
comment|'# NOTE(luisg): In order to allow this handler to be a wrapper for'
nl|'\n'
comment|'# other handlers, such as a FileHandler, and still be able to'
nl|'\n'
comment|'# configure it using logging.conf, this handler has to extend'
nl|'\n'
comment|"# MemoryHandler because only the MemoryHandlers' logging.conf"
nl|'\n'
comment|'# parsing is implemented such that it accepts a target handler.'
nl|'\n'
name|'handlers'
op|'.'
name|'MemoryHandler'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'capacity'
op|'='
number|'0'
op|','
name|'target'
op|'='
name|'target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'locale'
op|'='
name|'locale'
newline|'\n'
nl|'\n'
DECL|member|setFormatter
dedent|''
name|'def'
name|'setFormatter'
op|'('
name|'self'
op|','
name|'fmt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'target'
op|'.'
name|'setFormatter'
op|'('
name|'fmt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|emit
dedent|''
name|'def'
name|'emit'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
comment|'# We save the message from the original record to restore it'
nl|'\n'
comment|'# after translation, so other handlers are not affected by this'
nl|'\n'
indent|'        '
name|'original_msg'
op|'='
name|'record'
op|'.'
name|'msg'
newline|'\n'
name|'original_args'
op|'='
name|'record'
op|'.'
name|'args'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_translate_and_log_record'
op|'('
name|'record'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'record'
op|'.'
name|'msg'
op|'='
name|'original_msg'
newline|'\n'
name|'record'
op|'.'
name|'args'
op|'='
name|'original_args'
newline|'\n'
nl|'\n'
DECL|member|_translate_and_log_record
dedent|''
dedent|''
name|'def'
name|'_translate_and_log_record'
op|'('
name|'self'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'record'
op|'.'
name|'msg'
op|'='
name|'translate'
op|'('
name|'record'
op|'.'
name|'msg'
op|','
name|'self'
op|'.'
name|'locale'
op|')'
newline|'\n'
nl|'\n'
comment|'# In addition to translating the message, we also need to translate'
nl|'\n'
comment|'# arguments that were passed to the log method that were not part'
nl|'\n'
comment|"# of the main message e.g., log.info(_('Some message %s'), this_one))"
nl|'\n'
name|'record'
op|'.'
name|'args'
op|'='
name|'_translate_args'
op|'('
name|'record'
op|'.'
name|'args'
op|','
name|'self'
op|'.'
name|'locale'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'target'
op|'.'
name|'emit'
op|'('
name|'record'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
