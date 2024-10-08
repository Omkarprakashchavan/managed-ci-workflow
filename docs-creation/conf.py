from recommonmark.transform import AutoStructify
import datetime
import os

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'GLP MANAGED CI' 
copyright = f'{datetime.datetime.now().year} Hewlett Packard Enterprise Development LP'
AUTHOR = 'GLCP Team'
VERSION = 'latest'

# The short X.Y version.
version = VERSION
# The full version, including alpha/beta/rc tags.
release = VERSION

today_fmt = '%B %d, %Y'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_multiversion',
    'sphinx_rtd_theme',
    'recommonmark',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx_markdown_tables',
    'sphinxcontrib.plantuml',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
# External links defined in a .rst file will open in a new tab.  
# However, this causes anchors defined in .md files to also open in a new tab.
#    "sphinx_new_tab_link",
    #'notfound.extension',
    #'sphinx_antsibull_ext',
]

plantuml = f'/usr/bin/java -jar {os.getcwd()}/tools/plantuml.1.2019.1.jar'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

source_parsers = {
   '.md': 'recommonmark.parser.CommonMarkParser',
}

# The master toctree document.
root_doc = master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv', '**/template.md', 'README.md']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']

# Substitutions, variables, entities, & shortcuts for text which do not need to link to anything.
# For titles which should be a link, use the intersphinx anchors set at the index, chapter, and section levels, such as  qi_start_:
# |br| is useful for formatting fields inside of tables
# |_| is a nonbreaking space; similarly useful inside of tables
rst_epilog = """
.. |br| raw:: html

   <br>
.. |_| unicode:: 0xA0
    :trim:
"""

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme_path = []
html_theme = 'sphinx_rtd_theme'
html_show_sphinx = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

html_context = {
    'display_github': 'True',
    'show_sphinx': False,
    'is_eol': False,
    'github_user': 'glcp',
    'github_repo': 'managed-ci-workflow',
    'current_version': version,
    'latest_version': '8',
}

# Add extra CSS styles to the resulting HTML pages
html_css_files = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'GLCP Devx Documentation'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Documentation'

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, the reST sources are included in the HTML build as _sources/<name>.
html_copy_source = False

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'GLCPdoc'

notfound_default_version = "latest"
# makes default setting explicit:
notfound_no_urls_prefix = False

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'GlcpCentral.tex', 'Glcp Documentation',
     'Glcp Team', 'manual'),
]

# The update script depends on this format so deviating from this (for instance, adding a third
# location for the mappning to live) will confuse it.
intersphinx_mapping = {'python': ('https://docs.python.org/2/', None, None),
                       'python3': ('https://docs.python.org/3/', None, None),
                       'jinja2': ('http://jinja.palletsprojects.com/', None, None),
                       'ansible_2_9': ('https://docs.ansible.com/ansible/2.9/', None, None),
                       'ansible_8': ('https://docs.ansible.com/ansible/8/', None, None),
                       }

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'glcp', 'Glcp Documentation',
     [AUTHOR], 1)
]

# linckchecker settings
linkcheck_ignore = []
linkcheck_workers = 25

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Glcp', 'Glcp Documentation',
     AUTHOR, 'Glcp', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Options for sphinx-multiversion -----------------------------------------
# https://holzhaus.github.io/sphinx-multiversion/master/configuration.html

# Using None causes a warning, so use a regex that will produce no matches
smv_branch_whitelist = r'please-ignore-all-branches'

smv_released_pattern = '^refs/tags/.*$'

# Include only tags that start with letter "v" and has
# this format: "v<digit>.<digit>.<digit>"
smv_tag_whitelist = r'^v\d+\.\d+\.\d+$'

# the gh-pages.yaml workflow (and local-build.sh script) will automatically
# update this setting with the highest version number
smv_latest_version = r'the latest'

# -- Extension configuration -------------------------------------------------

def setup(app):
    app.add_css_file("design.css")
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            'enable_eval_rst': True,
            'enable_inline_math': True,
            'enable_math': True,
            }, True)
    app.add_transform(AutoStructify)

