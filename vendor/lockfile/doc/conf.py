begin_unit
comment|'# -*- coding: utf-8 -*-'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# lockfile documentation build configuration file, created by'
nl|'\n'
comment|'# sphinx-quickstart on Sat Sep 13 17:54:17 2008.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This file is execfile()d with the current directory set to its containing dir.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# The contents of this file are pickled, so don't put values in the namespace"
nl|'\n'
comment|"# that aren't pickleable (module imports are okay, they're removed automatically)."
nl|'\n'
comment|'#'
nl|'\n'
comment|'# All configuration values have a default value; values that are commented out'
nl|'\n'
comment|'# serve to show the default value.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
op|','
name|'os'
newline|'\n'
nl|'\n'
comment|'# If your extensions are in another directory, add it here. If the directory'
nl|'\n'
comment|'# is relative to the documentation root, use os.path.abspath to make it'
nl|'\n'
comment|'# absolute, like shown here.'
nl|'\n'
comment|"#sys.path.append(os.path.abspath('some/directory'))"
nl|'\n'
nl|'\n'
comment|'# General configuration'
nl|'\n'
comment|'# ---------------------'
nl|'\n'
nl|'\n'
comment|'# Add any Sphinx extension module names here, as strings. They can be extensions'
nl|'\n'
comment|"# coming with Sphinx (named 'sphinx.ext.*') or your custom ones."
nl|'\n'
DECL|variable|extensions
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Add any paths that contain templates here, relative to this directory.'
nl|'\n'
DECL|variable|templates_path
name|'templates_path'
op|'='
op|'['
string|"'.templates'"
op|']'
newline|'\n'
nl|'\n'
comment|'# The suffix of source filenames.'
nl|'\n'
DECL|variable|source_suffix
name|'source_suffix'
op|'='
string|"'.rst'"
newline|'\n'
nl|'\n'
comment|'# The master toctree document.'
nl|'\n'
DECL|variable|master_doc
name|'master_doc'
op|'='
string|"'lockfile'"
newline|'\n'
nl|'\n'
comment|'# General substitutions.'
nl|'\n'
DECL|variable|project
name|'project'
op|'='
string|"'lockfile'"
newline|'\n'
DECL|variable|copyright
name|'copyright'
op|'='
string|"'2008, Skip Montanaro'"
newline|'\n'
nl|'\n'
comment|'# The default replacements for |version| and |release|, also used in various'
nl|'\n'
comment|'# other places throughout the built documents.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The short X.Y version.'
nl|'\n'
DECL|variable|version
name|'version'
op|'='
string|"'0.3'"
newline|'\n'
comment|'# The full version, including alpha/beta/rc tags.'
nl|'\n'
DECL|variable|release
name|'release'
op|'='
string|"'0.3'"
newline|'\n'
nl|'\n'
comment|'# There are two options for replacing |today|: either, you set today to some'
nl|'\n'
comment|'# non-false value, then it is used:'
nl|'\n'
comment|"#today = ''"
nl|'\n'
comment|'# Else, today_fmt is used as the format for a strftime call.'
nl|'\n'
DECL|variable|today_fmt
name|'today_fmt'
op|'='
string|"'%B %d, %Y'"
newline|'\n'
nl|'\n'
comment|"# List of documents that shouldn't be included in the build."
nl|'\n'
comment|'#unused_docs = []'
nl|'\n'
nl|'\n'
comment|"# List of directories, relative to source directories, that shouldn't be searched"
nl|'\n'
comment|'# for source files.'
nl|'\n'
comment|'#exclude_dirs = []'
nl|'\n'
nl|'\n'
comment|'# The reST default role (used for this markup: `text`) to use for all documents.'
nl|'\n'
comment|'#default_role = None'
nl|'\n'
nl|'\n'
comment|"# If true, '()' will be appended to :func: etc. cross-reference text."
nl|'\n'
comment|'#add_function_parentheses = True'
nl|'\n'
nl|'\n'
comment|'# If true, the current module name will be prepended to all description'
nl|'\n'
comment|'# unit titles (such as .. function::).'
nl|'\n'
comment|'#add_module_names = True'
nl|'\n'
nl|'\n'
comment|'# If true, sectionauthor and moduleauthor directives will be shown in the'
nl|'\n'
comment|'# output. They are ignored by default.'
nl|'\n'
comment|'#show_authors = False'
nl|'\n'
nl|'\n'
comment|'# The name of the Pygments (syntax highlighting) style to use.'
nl|'\n'
DECL|variable|pygments_style
name|'pygments_style'
op|'='
string|"'sphinx'"
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Options for HTML output'
nl|'\n'
comment|'# -----------------------'
nl|'\n'
nl|'\n'
comment|'# The style sheet to use for HTML and HTML Help pages. A file of that name'
nl|'\n'
comment|"# must exist either in Sphinx' static/ path, or in one of the custom paths"
nl|'\n'
comment|'# given in html_static_path.'
nl|'\n'
DECL|variable|html_style
name|'html_style'
op|'='
string|"'default.css'"
newline|'\n'
nl|'\n'
comment|'# The name for this set of Sphinx documents.  If None, it defaults to'
nl|'\n'
comment|'# "<project> v<release> documentation".'
nl|'\n'
comment|'#html_title = None'
nl|'\n'
nl|'\n'
comment|'# A shorter title for the navigation bar.  Default is the same as html_title.'
nl|'\n'
comment|'#html_short_title = None'
nl|'\n'
nl|'\n'
comment|'# The name of an image file (within the static path) to place at the top of'
nl|'\n'
comment|'# the sidebar.'
nl|'\n'
comment|'#html_logo = None'
nl|'\n'
nl|'\n'
comment|'# The name of an image file (within the static path) to use as favicon of the'
nl|'\n'
comment|'# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32'
nl|'\n'
comment|'# pixels large.'
nl|'\n'
comment|'#html_favicon = None'
nl|'\n'
nl|'\n'
comment|'# Add any paths that contain custom static files (such as style sheets) here,'
nl|'\n'
comment|'# relative to this directory. They are copied after the builtin static files,'
nl|'\n'
comment|'# so a file named "default.css" will overwrite the builtin "default.css".'
nl|'\n'
DECL|variable|html_static_path
name|'html_static_path'
op|'='
op|'['
string|"'.static'"
op|']'
newline|'\n'
nl|'\n'
comment|"# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,"
nl|'\n'
comment|'# using the given strftime format.'
nl|'\n'
DECL|variable|html_last_updated_fmt
name|'html_last_updated_fmt'
op|'='
string|"'%b %d, %Y'"
newline|'\n'
nl|'\n'
comment|'# If true, SmartyPants will be used to convert quotes and dashes to'
nl|'\n'
comment|'# typographically correct entities.'
nl|'\n'
comment|'#html_use_smartypants = True'
nl|'\n'
nl|'\n'
comment|'# Custom sidebar templates, maps document names to template names.'
nl|'\n'
comment|'#html_sidebars = {}'
nl|'\n'
nl|'\n'
comment|'# Additional templates that should be rendered to pages, maps page names to'
nl|'\n'
comment|'# template names.'
nl|'\n'
comment|'#html_additional_pages = {}'
nl|'\n'
nl|'\n'
comment|'# If false, no module index is generated.'
nl|'\n'
comment|'#html_use_modindex = True'
nl|'\n'
nl|'\n'
comment|'# If false, no index is generated.'
nl|'\n'
comment|'#html_use_index = True'
nl|'\n'
nl|'\n'
comment|'# If true, the index is split into individual pages for each letter.'
nl|'\n'
comment|'#html_split_index = False'
nl|'\n'
nl|'\n'
comment|'# If true, the reST sources are included in the HTML build as _sources/<name>.'
nl|'\n'
comment|'#html_copy_source = True'
nl|'\n'
nl|'\n'
comment|'# If true, an OpenSearch description file will be output, and all pages will'
nl|'\n'
comment|'# contain a <link> tag referring to it.  The value of this option must be the'
nl|'\n'
comment|'# base URL from which the finished HTML is served.'
nl|'\n'
comment|"#html_use_opensearch = ''"
nl|'\n'
nl|'\n'
comment|'# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").'
nl|'\n'
comment|"#html_file_suffix = ''"
nl|'\n'
nl|'\n'
comment|'# Output file base name for HTML help builder.'
nl|'\n'
DECL|variable|htmlhelp_basename
name|'htmlhelp_basename'
op|'='
string|"'lockfiledoc'"
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Options for LaTeX output'
nl|'\n'
comment|'# ------------------------'
nl|'\n'
nl|'\n'
comment|"# The paper size ('letter' or 'a4')."
nl|'\n'
comment|"#latex_paper_size = 'letter'"
nl|'\n'
nl|'\n'
comment|"# The font size ('10pt', '11pt' or '12pt')."
nl|'\n'
comment|"#latex_font_size = '10pt'"
nl|'\n'
nl|'\n'
comment|'# Grouping the document tree into LaTeX files. List of tuples'
nl|'\n'
comment|'# (source start file, target name, title, author, document class [howto/manual]).'
nl|'\n'
DECL|variable|latex_documents
name|'latex_documents'
op|'='
op|'['
nl|'\n'
op|'('
string|"'lockfile'"
op|','
string|"'lockfile.tex'"
op|','
string|"'lockfile Documentation'"
op|','
nl|'\n'
string|"'Skip Montanaro'"
op|','
string|"'manual'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'# The name of an image file (relative to this directory) to place at the top of'
nl|'\n'
comment|'# the title page.'
nl|'\n'
comment|'#latex_logo = None'
nl|'\n'
nl|'\n'
comment|'# For "manual" documents, if this is true, then toplevel headings are parts,'
nl|'\n'
comment|'# not chapters.'
nl|'\n'
comment|'#latex_use_parts = False'
nl|'\n'
nl|'\n'
comment|'# Additional stuff for the LaTeX preamble.'
nl|'\n'
comment|"#latex_preamble = ''"
nl|'\n'
nl|'\n'
comment|'# Documents to append as an appendix to all manuals.'
nl|'\n'
comment|'#latex_appendices = []'
nl|'\n'
nl|'\n'
comment|'# If false, no module index is generated.'
nl|'\n'
comment|'#latex_use_modindex = True'
nl|'\n'
endmarker|''
end_unit
