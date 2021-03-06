begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
string|'"""This provides a sphinx extension able to create the HTML needed\nfor the api-ref website.\n\nIt contains 2 new stanzas.\n\n  .. rest_method:: GET /foo/bar\n\nWhich is designed to be used as the first stanza in a new section to\nstate that section is about that REST method. During processing the\nrest stanza will be reparented to be before the section in question,\nand used as a show/hide selector for it\'s details.\n\n  .. rest_parameters:: file.yaml\n\n     - name1: name_in_file1\n     - name2: name_in_file2\n     - name3: name_in_file3\n\nWhich is designed to build structured tables for either response or\nrequest parameters. The stanza takes a value which is a file to lookup\ndetails about the parameters in question.\n\nThe contents of the stanza are a yaml list of key / value pairs. The\nkey is the name of the parameter to be shown in the table. The value\nis the key in the file.yaml where all other metadata about the\nparameter will be extracted. This allows for reusing parameter\ndefinitions widely in API definitions, but still providing for control\nin both naming and ordering of parameters at every declaration.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'collections'
name|'import'
name|'OrderedDict'
newline|'\n'
nl|'\n'
name|'from'
name|'docutils'
name|'import'
name|'nodes'
newline|'\n'
name|'from'
name|'docutils'
op|'.'
name|'parsers'
op|'.'
name|'rst'
op|'.'
name|'directives'
op|'.'
name|'tables'
name|'import'
name|'Table'
newline|'\n'
name|'from'
name|'docutils'
op|'.'
name|'statemachine'
name|'import'
name|'ViewList'
newline|'\n'
name|'from'
name|'sphinx'
op|'.'
name|'util'
op|'.'
name|'compat'
name|'import'
name|'Directive'
newline|'\n'
name|'import'
name|'yaml'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ordered_load
name|'def'
name|'ordered_load'
op|'('
name|'stream'
op|','
name|'Loader'
op|'='
name|'yaml'
op|'.'
name|'Loader'
op|','
name|'object_pairs_hook'
op|'='
name|'OrderedDict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Load yaml as an ordered dict\n\n    This allows us to inspect the order of the file on disk to make\n    sure it was correct by our rules.\n    """'
newline|'\n'
DECL|class|OrderedLoader
name|'class'
name|'OrderedLoader'
op|'('
name|'Loader'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|construct_mapping
dedent|''
name|'def'
name|'construct_mapping'
op|'('
name|'loader'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'loader'
op|'.'
name|'flatten_mapping'
op|'('
name|'node'
op|')'
newline|'\n'
name|'return'
name|'object_pairs_hook'
op|'('
name|'loader'
op|'.'
name|'construct_pairs'
op|'('
name|'node'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'OrderedLoader'
op|'.'
name|'add_constructor'
op|'('
nl|'\n'
name|'yaml'
op|'.'
name|'resolver'
op|'.'
name|'BaseResolver'
op|'.'
name|'DEFAULT_MAPPING_TAG'
op|','
nl|'\n'
name|'construct_mapping'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'yaml'
op|'.'
name|'load'
op|'('
name|'stream'
op|','
name|'OrderedLoader'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|full_name
dedent|''
name|'def'
name|'full_name'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'cls'
op|'.'
name|'__module__'
op|'+'
string|"'.'"
op|'+'
name|'cls'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|rest_method
dedent|''
name|'class'
name|'rest_method'
op|'('
name|'nodes'
op|'.'
name|'Part'
op|','
name|'nodes'
op|'.'
name|'Element'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""rest_method custom node type\n\n    We specify a custom node type for rest_method so that we can\n    accumulate all the data about the rest method, but not render as\n    part of the normal rendering process. This means that we need a\n    renderer for every format we wish to support with this.\n\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|rest_expand_all
dedent|''
name|'class'
name|'rest_expand_all'
op|'('
name|'nodes'
op|'.'
name|'Part'
op|','
name|'nodes'
op|'.'
name|'Element'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RestExpandAllDirective
dedent|''
name|'class'
name|'RestExpandAllDirective'
op|'('
name|'Directive'
op|')'
op|':'
newline|'\n'
DECL|variable|has_content
indent|'    '
name|'has_content'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|run
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'rest_expand_all'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RestMethodDirective
dedent|''
dedent|''
name|'class'
name|'RestMethodDirective'
op|'('
name|'Directive'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# this enables content in the directive'
nl|'\n'
DECL|variable|has_content
indent|'    '
name|'has_content'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|run
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lineno'
op|'='
name|'self'
op|'.'
name|'state_machine'
op|'.'
name|'abs_line_number'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'nodes'
op|'.'
name|'target'
op|'('
op|')'
newline|'\n'
name|'section'
op|'='
name|'nodes'
op|'.'
name|'section'
op|'('
name|'classes'
op|'='
op|'['
string|'"detail-control"'
op|']'
op|')'
newline|'\n'
comment|'# env = self.state.document.settings.env'
nl|'\n'
comment|'# env.app.info("Parent %s" % self.state.parent.attributes)'
nl|'\n'
nl|'\n'
name|'node'
op|'='
name|'rest_method'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(sdague): this is a super simplistic parser, should be'
nl|'\n'
comment|'# more robust.'
nl|'\n'
name|'method'
op|','
name|'sep'
op|','
name|'url'
op|'='
name|'self'
op|'.'
name|'content'
op|'['
number|'0'
op|']'
op|'.'
name|'partition'
op|'('
string|"' '"
op|')'
newline|'\n'
nl|'\n'
name|'node'
op|'['
string|"'method'"
op|']'
op|'='
name|'method'
newline|'\n'
name|'node'
op|'['
string|"'url'"
op|']'
op|'='
name|'url'
newline|'\n'
name|'node'
op|'['
string|"'target'"
op|']'
op|'='
name|'self'
op|'.'
name|'state'
op|'.'
name|'parent'
op|'.'
name|'attributes'
op|'['
string|"'ids'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# We need to build a temporary target that we can replace'
nl|'\n'
comment|'# later in the processing to get the TOC to resolve correctly.'
nl|'\n'
name|'temp_target'
op|'='
string|'"%s-selector"'
op|'%'
name|'node'
op|'['
string|"'target'"
op|']'
newline|'\n'
name|'target'
op|'='
name|'nodes'
op|'.'
name|'target'
op|'('
name|'ids'
op|'='
op|'['
name|'temp_target'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'.'
name|'add_target'
op|'('
name|'temp_target'
op|','
string|"''"
op|','
name|'target'
op|','
name|'lineno'
op|')'
newline|'\n'
name|'section'
op|'+='
name|'node'
newline|'\n'
nl|'\n'
name|'return'
op|'['
name|'target'
op|','
name|'section'
op|']'
newline|'\n'
nl|'\n'
comment|'# cache for file -> yaml so we only do the load and check of a yaml'
nl|'\n'
comment|'# file once during a sphinx processing run.'
nl|'\n'
DECL|variable|YAML_CACHE
dedent|''
dedent|''
name|'YAML_CACHE'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RestParametersDirective
name|'class'
name|'RestParametersDirective'
op|'('
name|'Table'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|headers
indent|'    '
name|'headers'
op|'='
op|'['
string|'"Name"'
op|','
string|'"In"'
op|','
string|'"Type"'
op|','
string|'"Description"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_load_param_file
name|'def'
name|'_load_param_file'
op|'('
name|'self'
op|','
name|'fpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'YAML_CACHE'
newline|'\n'
name|'if'
name|'fpath'
name|'in'
name|'YAML_CACHE'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'YAML_CACHE'
op|'['
name|'fpath'
op|']'
newline|'\n'
nl|'\n'
comment|'# self.app.info("Fpath: %s" % fpath)'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'fpath'
op|','
string|"'r'"
op|')'
name|'as'
name|'stream'
op|':'
newline|'\n'
indent|'                '
name|'lookup'
op|'='
name|'ordered_load'
op|'('
name|'stream'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_yaml_sorting'
op|'('
name|'fpath'
op|','
name|'lookup'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'env'
op|'.'
name|'warn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'env'
op|'.'
name|'docname'
op|','
nl|'\n'
string|'"Parameters file %s not found"'
op|'%'
name|'fpath'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'yaml'
op|'.'
name|'YAMLError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'app'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'YAML_CACHE'
op|'['
name|'fpath'
op|']'
op|'='
name|'lookup'
newline|'\n'
name|'return'
name|'lookup'
newline|'\n'
nl|'\n'
DECL|member|_check_yaml_sorting
dedent|''
name|'def'
name|'_check_yaml_sorting'
op|'('
name|'self'
op|','
name|'fpath'
op|','
name|'yaml_data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""check yaml sorting\n\n        Assuming we got an ordered dict, we iterate through it\n        basically doing a gnome sort test\n        (https://en.wikipedia.org/wiki/Gnome_sort) and ensure the item\n        we are looking at is > the last item we saw. This is done at\n        the section level first, so we\'re grouped, then alphabetically\n        by lower case name within a section. Every time there is a\n        mismatch we raise an info message (will later be a warn).\n        """'
newline|'\n'
name|'sections'
op|'='
op|'{'
string|'"header"'
op|':'
number|'1'
op|','
string|'"path"'
op|':'
number|'2'
op|','
string|'"query"'
op|':'
number|'3'
op|','
string|'"body"'
op|':'
number|'4'
op|'}'
newline|'\n'
nl|'\n'
name|'last'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'yaml_data'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'last'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'last'
op|'='
op|'('
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
comment|'# ensure that sections only go up'
nl|'\n'
dedent|''
name|'current_section'
op|'='
name|'value'
op|'['
string|"'in'"
op|']'
newline|'\n'
name|'last_section'
op|'='
name|'last'
op|'['
number|'1'
op|']'
op|'['
string|"'in'"
op|']'
newline|'\n'
name|'if'
name|'sections'
op|'['
name|'current_section'
op|']'
op|'<'
name|'sections'
op|'['
name|'last_section'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'app'
op|'.'
name|'warn'
op|'('
nl|'\n'
string|'"Section out of order. All parameters in section ``%s`` "'
nl|'\n'
string|'"should be after section ``%s``. (see ``%s``)"'
op|'%'
op|'('
nl|'\n'
name|'last_section'
op|','
nl|'\n'
name|'current_section'
op|','
nl|'\n'
name|'last'
op|'['
number|'0'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'sections'
op|'['
name|'value'
op|'['
string|"'in'"
op|']'
op|']'
op|'=='
name|'sections'
op|'['
name|'last'
op|'['
number|'1'
op|']'
op|'['
string|"'in'"
op|']'
op|']'
name|'and'
nl|'\n'
name|'key'
op|'.'
name|'lower'
op|'('
op|')'
op|'<'
name|'last'
op|'['
number|'0'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'app'
op|'.'
name|'warn'
op|'('
nl|'\n'
string|'"Parameters out of order ``%s`` should be after ``%s``"'
op|'%'
op|'('
nl|'\n'
name|'last'
op|'['
number|'0'
op|']'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
dedent|''
name|'last'
op|'='
op|'('
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|yaml_from_file
dedent|''
dedent|''
name|'def'
name|'yaml_from_file'
op|'('
name|'self'
op|','
name|'fpath'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Collect Parameter stanzas from inline + file.\n\n        This allows use to reference an external file for the actual\n        parameter definitions.\n        """'
newline|'\n'
name|'lookup'
op|'='
name|'self'
op|'.'
name|'_load_param_file'
op|'('
name|'fpath'
op|')'
newline|'\n'
nl|'\n'
name|'content'
op|'='
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
name|'parsed'
op|'='
name|'yaml'
op|'.'
name|'load'
op|'('
name|'content'
op|')'
newline|'\n'
comment|'# self.app.info("Params loaded is %s" % parsed)'
nl|'\n'
comment|'# self.app.info("Lookup table looks like %s" % lookup)'
nl|'\n'
name|'new_content'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
name|'for'
name|'paramlist'
name|'in'
name|'parsed'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'name'
op|','
name|'ref'
name|'in'
name|'paramlist'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'ref'
name|'in'
name|'lookup'
op|':'
newline|'\n'
indent|'                    '
name|'new_content'
op|'.'
name|'append'
op|'('
op|'('
name|'name'
op|','
name|'lookup'
op|'['
name|'ref'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# TODO(sdague): this provides a kind of confusing'
nl|'\n'
comment|"# error message because env.warn isn't meant to be"
nl|'\n'
comment|'# used this way, however it does provide a way to'
nl|'\n'
comment|'# track down where the parameters list is that is'
nl|'\n'
comment|"# wrong. So it's good enough for now."
nl|'\n'
indent|'                    '
name|'self'
op|'.'
name|'env'
op|'.'
name|'warn'
op|'('
nl|'\n'
string|'"%s:%s "'
op|'%'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'state_machine'
op|'.'
name|'node'
op|'.'
name|'source'
op|','
nl|'\n'
name|'self'
op|'.'
name|'state_machine'
op|'.'
name|'node'
op|'.'
name|'line'
op|')'
op|','
nl|'\n'
op|'('
string|'"No field definition for ``%s`` found in ``%s``. "'
nl|'\n'
string|'" Skipping."'
op|'%'
op|'('
name|'ref'
op|','
name|'fpath'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# self.app.info("New content %s" % new_content)'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'yaml'
op|'='
name|'new_content'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'env'
op|'='
name|'self'
op|'.'
name|'state'
op|'.'
name|'document'
op|'.'
name|'settings'
op|'.'
name|'env'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'self'
op|'.'
name|'env'
op|'.'
name|'app'
newline|'\n'
nl|'\n'
comment|'# Make sure we have some content, which should be yaml that'
nl|'\n'
comment|'# defines some parameters.'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'content'
op|':'
newline|'\n'
indent|'            '
name|'error'
op|'='
name|'self'
op|'.'
name|'state_machine'
op|'.'
name|'reporter'
op|'.'
name|'error'
op|'('
nl|'\n'
string|"'No parameters defined'"
op|','
nl|'\n'
name|'nodes'
op|'.'
name|'literal_block'
op|'('
name|'self'
op|'.'
name|'block_text'
op|','
name|'self'
op|'.'
name|'block_text'
op|')'
op|','
nl|'\n'
name|'line'
op|'='
name|'self'
op|'.'
name|'lineno'
op|')'
newline|'\n'
name|'return'
op|'['
name|'error'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'len'
op|'('
name|'self'
op|'.'
name|'arguments'
op|')'
op|'>='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'error'
op|'='
name|'self'
op|'.'
name|'state_machine'
op|'.'
name|'reporter'
op|'.'
name|'error'
op|'('
nl|'\n'
string|"'No reference file defined'"
op|','
nl|'\n'
name|'nodes'
op|'.'
name|'literal_block'
op|'('
name|'self'
op|'.'
name|'block_text'
op|','
name|'self'
op|'.'
name|'block_text'
op|')'
op|','
nl|'\n'
name|'line'
op|'='
name|'self'
op|'.'
name|'lineno'
op|')'
newline|'\n'
name|'return'
op|'['
name|'error'
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(sdague): it's important that we pop the arg otherwise"
nl|'\n'
comment|'# we end up putting the filename as the table caption.'
nl|'\n'
dedent|''
name|'rel_fpath'
op|','
name|'fpath'
op|'='
name|'self'
op|'.'
name|'env'
op|'.'
name|'relfn2path'
op|'('
name|'self'
op|'.'
name|'arguments'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'yaml_file'
op|'='
name|'fpath'
newline|'\n'
name|'self'
op|'.'
name|'yaml_from_file'
op|'('
name|'self'
op|'.'
name|'yaml_file'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'max_cols'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'headers'
op|')'
newline|'\n'
comment|'# TODO(sdague): it would be good to dynamically set column'
nl|'\n'
comment|'# widths (or basically make the colwidth thing go away'
nl|'\n'
comment|'# entirely)'
nl|'\n'
name|'self'
op|'.'
name|'options'
op|'['
string|"'widths'"
op|']'
op|'='
op|'('
number|'20'
op|','
number|'10'
op|','
number|'10'
op|','
number|'60'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'col_widths'
op|'='
name|'self'
op|'.'
name|'get_column_widths'
op|'('
name|'self'
op|'.'
name|'max_cols'
op|')'
newline|'\n'
comment|'# Actually convert the yaml'
nl|'\n'
name|'title'
op|','
name|'messages'
op|'='
name|'self'
op|'.'
name|'make_title'
op|'('
op|')'
newline|'\n'
comment|'# self.app.info("Title %s, messages %s" % (title, messages))'
nl|'\n'
name|'table_node'
op|'='
name|'self'
op|'.'
name|'build_table'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_name'
op|'('
name|'table_node'
op|')'
newline|'\n'
name|'if'
name|'title'
op|':'
newline|'\n'
indent|'            '
name|'table_node'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'title'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'['
name|'table_node'
op|']'
op|'+'
name|'messages'
newline|'\n'
nl|'\n'
DECL|member|get_rows
dedent|''
name|'def'
name|'get_rows'
op|'('
name|'self'
op|','
name|'table_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rows'
op|'='
op|'['
op|']'
newline|'\n'
name|'groups'
op|'='
op|'['
op|']'
newline|'\n'
name|'trow'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
name|'entry'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'para'
op|'='
name|'nodes'
op|'.'
name|'paragraph'
op|'('
name|'text'
op|'='
name|'unicode'
op|'('
name|'table_data'
op|')'
op|')'
newline|'\n'
name|'entry'
op|'+='
name|'para'
newline|'\n'
name|'trow'
op|'+='
name|'entry'
newline|'\n'
name|'rows'
op|'.'
name|'append'
op|'('
name|'trow'
op|')'
newline|'\n'
name|'return'
name|'rows'
op|','
name|'groups'
newline|'\n'
nl|'\n'
comment|'# Add a column for a field. In order to have the RST inside'
nl|'\n'
comment|'# these fields get rendered, we need to use the'
nl|'\n'
comment|'# ViewList. Note, ViewList expects a list of lines, so chunk'
nl|'\n'
comment|'# up our content as a list to make it happy.'
nl|'\n'
DECL|member|add_col
dedent|''
name|'def'
name|'add_col'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'ViewList'
op|'('
name|'value'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'.'
name|'nested_parse'
op|'('
name|'result'
op|','
number|'0'
op|','
name|'entry'
op|')'
newline|'\n'
name|'return'
name|'entry'
newline|'\n'
nl|'\n'
DECL|member|show_no_yaml_error
dedent|''
name|'def'
name|'show_no_yaml_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'trow'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
name|'classes'
op|'='
op|'['
string|'"no_yaml"'
op|']'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
string|'"No yaml found %s"'
op|'%'
name|'self'
op|'.'
name|'yaml_file'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
string|'""'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
string|'""'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
string|'""'
op|')'
newline|'\n'
name|'return'
name|'trow'
newline|'\n'
nl|'\n'
DECL|member|collect_rows
dedent|''
name|'def'
name|'collect_rows'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rows'
op|'='
op|'['
op|']'
newline|'\n'
name|'groups'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# self.app.info("Parsed content is: %s" % self.yaml)'
nl|'\n'
indent|'            '
name|'for'
name|'key'
op|','
name|'values'
name|'in'
name|'self'
op|'.'
name|'yaml'
op|':'
newline|'\n'
indent|'                '
name|'min_version'
op|'='
name|'values'
op|'.'
name|'get'
op|'('
string|"'min_version'"
op|','
string|"''"
op|')'
newline|'\n'
name|'desc'
op|'='
name|'values'
op|'.'
name|'get'
op|'('
string|"'description'"
op|','
string|"''"
op|')'
newline|'\n'
name|'classes'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'min_version'
op|':'
newline|'\n'
indent|'                    '
name|'desc'
op|'+='
op|'('
string|'"\\n\\n**New in version %s**\\n"'
op|'%'
name|'min_version'
op|')'
newline|'\n'
name|'min_ver_css_name'
op|'='
op|'('
string|'"rp_min_ver_"'
op|'+'
nl|'\n'
name|'str'
op|'('
name|'min_version'
op|')'
op|'.'
name|'replace'
op|'('
string|"'.'"
op|','
string|"'_'"
op|')'
op|')'
newline|'\n'
name|'classes'
op|'.'
name|'append'
op|'('
name|'min_ver_css_name'
op|')'
newline|'\n'
dedent|''
name|'trow'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
name|'classes'
op|'='
name|'classes'
op|')'
newline|'\n'
name|'name'
op|'='
name|'key'
newline|'\n'
name|'if'
name|'values'
op|'.'
name|'get'
op|'('
string|"'required'"
op|','
name|'False'
op|')'
name|'is'
name|'False'
op|':'
newline|'\n'
indent|'                    '
name|'name'
op|'+='
string|'" (Optional)"'
newline|'\n'
dedent|''
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
name|'name'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
name|'values'
op|'.'
name|'get'
op|'('
string|"'in'"
op|')'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
name|'values'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
name|'trow'
op|'+='
name|'self'
op|'.'
name|'add_col'
op|'('
name|'desc'
op|')'
newline|'\n'
name|'rows'
op|'.'
name|'append'
op|'('
name|'trow'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'AttributeError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'key'"
name|'in'
name|'locals'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'app'
op|'.'
name|'warn'
op|'('
string|'"Failure on key: %s, values: %s. %s"'
op|'%'
nl|'\n'
op|'('
name|'key'
op|','
name|'values'
op|','
name|'exc'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'rows'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'show_no_yaml_error'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rows'
op|','
name|'groups'
newline|'\n'
nl|'\n'
DECL|member|build_table
dedent|''
name|'def'
name|'build_table'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'='
name|'nodes'
op|'.'
name|'table'
op|'('
op|')'
newline|'\n'
name|'tgroup'
op|'='
name|'nodes'
op|'.'
name|'tgroup'
op|'('
name|'cols'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'headers'
op|')'
op|')'
newline|'\n'
name|'table'
op|'+='
name|'tgroup'
newline|'\n'
nl|'\n'
comment|'# TODO(sdague): it would be really nice to figure out how not'
nl|'\n'
comment|'# to have this stanza, it kind of messes up all of the table'
nl|'\n'
comment|"# formatting because it doesn't let tables just be the right"
nl|'\n'
comment|'# size.'
nl|'\n'
name|'tgroup'
op|'.'
name|'extend'
op|'('
nl|'\n'
name|'nodes'
op|'.'
name|'colspec'
op|'('
name|'colwidth'
op|'='
name|'col_width'
op|','
name|'colname'
op|'='
string|"'c'"
op|'+'
name|'str'
op|'('
name|'idx'
op|')'
op|')'
nl|'\n'
name|'for'
name|'idx'
op|','
name|'col_width'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'col_widths'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'thead'
op|'='
name|'nodes'
op|'.'
name|'thead'
op|'('
op|')'
newline|'\n'
name|'tgroup'
op|'+='
name|'thead'
newline|'\n'
nl|'\n'
name|'row_node'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
name|'thead'
op|'+='
name|'row_node'
newline|'\n'
name|'row_node'
op|'.'
name|'extend'
op|'('
name|'nodes'
op|'.'
name|'entry'
op|'('
name|'h'
op|','
name|'nodes'
op|'.'
name|'paragraph'
op|'('
name|'text'
op|'='
name|'h'
op|')'
op|')'
nl|'\n'
name|'for'
name|'h'
name|'in'
name|'self'
op|'.'
name|'headers'
op|')'
newline|'\n'
nl|'\n'
name|'tbody'
op|'='
name|'nodes'
op|'.'
name|'tbody'
op|'('
op|')'
newline|'\n'
name|'tgroup'
op|'+='
name|'tbody'
newline|'\n'
nl|'\n'
name|'rows'
op|','
name|'groups'
op|'='
name|'self'
op|'.'
name|'collect_rows'
op|'('
op|')'
newline|'\n'
name|'tbody'
op|'.'
name|'extend'
op|'('
name|'rows'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'extend'
op|'('
name|'groups'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'table'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rest_method_html
dedent|''
dedent|''
name|'def'
name|'rest_method_html'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tmpl'
op|'='
string|'"""\n<div class="row operation-grp">\n    <div class="col-md-1 operation">\n    <a name="%(target)s" class="operation-anchor" href="#%(target)s">\n      <span class="glyphicon glyphicon-link"></span></a>\n    <span class="label label-success">%(method)s</span>\n    </div>\n    <div class="col-md-5">%(url)s</div>\n    <div class="col-md-5">%(desc)s</div>\n    <div class="col-md-1">\n    <button\n       class="btn btn-info btn-sm btn-detail"\n       data-target="#%(target)s-detail"\n       data-toggle="collapse"\n       id="%(target)s-detail-btn"\n       >detail</button>\n    </div>\n</div>"""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'body'
op|'.'
name|'append'
op|'('
name|'tmpl'
op|'%'
name|'node'
op|')'
newline|'\n'
name|'raise'
name|'nodes'
op|'.'
name|'SkipNode'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rest_expand_all_html
dedent|''
name|'def'
name|'rest_expand_all_html'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tmpl'
op|'='
string|'"""\n<div>\n<div class=col-md-11></div>\n<div class=col-md-1>\n    <button id="expand-all"\n       data-toggle="collapse"\n       class="btn btn-info btn-sm btn-expand-all"\n    >Show All</button>\n</div>\n</div>"""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'body'
op|'.'
name|'append'
op|'('
name|'tmpl'
op|'%'
name|'node'
op|')'
newline|'\n'
name|'raise'
name|'nodes'
op|'.'
name|'SkipNode'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|resolve_rest_references
dedent|''
name|'def'
name|'resolve_rest_references'
op|'('
name|'app'
op|','
name|'doctree'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'node'
name|'in'
name|'doctree'
op|'.'
name|'traverse'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'node'
op|','
name|'rest_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rest_node'
op|'='
name|'node'
newline|'\n'
name|'rest_method_section'
op|'='
name|'node'
op|'.'
name|'parent'
newline|'\n'
name|'rest_section'
op|'='
name|'rest_method_section'
op|'.'
name|'parent'
newline|'\n'
name|'gp'
op|'='
name|'rest_section'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
comment|'# Added required classes to the top section'
nl|'\n'
name|'rest_section'
op|'.'
name|'attributes'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'api-detail'"
op|')'
newline|'\n'
name|'rest_section'
op|'.'
name|'attributes'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'collapse'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Pop the title off the collapsed section'
nl|'\n'
name|'title'
op|'='
name|'rest_section'
op|'.'
name|'children'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'rest_node'
op|'['
string|"'desc'"
op|']'
op|'='
name|'title'
op|'.'
name|'children'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
comment|'# In order to get the links in the sidebar to be right, we'
nl|'\n'
comment|'# have to do some id flipping here late in the game. The'
nl|'\n'
comment|'# rest_method_section has basically had a dummy id up'
nl|'\n'
comment|'# until this point just to keep it from colliding with'
nl|'\n'
comment|"# it's parent."
nl|'\n'
name|'rest_section'
op|'.'
name|'attributes'
op|'['
string|"'ids'"
op|']'
op|'['
number|'0'
op|']'
op|'='
op|'('
nl|'\n'
string|'"%s-detail"'
op|'%'
name|'rest_section'
op|'.'
name|'attributes'
op|'['
string|"'ids'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'rest_method_section'
op|'.'
name|'attributes'
op|'['
string|"'ids'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'rest_node'
op|'['
string|"'target'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Pop the overall section into it's grand parent,"
nl|'\n'
comment|'# right before where the current parent lives'
nl|'\n'
name|'idx'
op|'='
name|'gp'
op|'.'
name|'children'
op|'.'
name|'index'
op|'('
name|'rest_section'
op|')'
newline|'\n'
name|'rest_section'
op|'.'
name|'remove'
op|'('
name|'rest_method_section'
op|')'
newline|'\n'
name|'gp'
op|'.'
name|'insert'
op|'('
name|'idx'
op|','
name|'rest_method_section'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'app'
op|'.'
name|'add_node'
op|'('
name|'rest_method'
op|','
nl|'\n'
name|'html'
op|'='
op|'('
name|'rest_method_html'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_node'
op|'('
name|'rest_expand_all'
op|','
nl|'\n'
name|'html'
op|'='
op|'('
name|'rest_expand_all_html'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'rest_parameters'"
op|','
name|'RestParametersDirective'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'rest_method'"
op|','
name|'RestMethodDirective'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'rest_expand_all'"
op|','
name|'RestExpandAllDirective'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_stylesheet'
op|'('
string|"'bootstrap.min.css'"
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_stylesheet'
op|'('
string|"'api-site.css'"
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_javascript'
op|'('
string|"'bootstrap.min.js'"
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_javascript'
op|'('
string|"'api-site.js'"
op|')'
newline|'\n'
name|'app'
op|'.'
name|'connect'
op|'('
string|"'doctree-read'"
op|','
name|'resolve_rest_references'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'version'"
op|':'
string|"'0.1'"
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
