# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Imports

import sphinx_rtd_theme

from pybtex.style.formatting.unsrt import Style
from formatting.apa import APAStyle
from labels.apa import LabelStyle as APALabelStyle
from pybtex.plugin import register_plugin
from pybtex.style.template import names, sentence

class MyAPALabelStyle(APALabelStyle):
    def format_label(self, entry):
        return APALabelStyle.format_label(self, entry)
        # return entry.fields['title'] + ' by ' + APALabelStyle.format_label(self, entry)

# class MyAPAStyle(APAStyle):
class MyAPAStyle(Style):
    default_label_style = 'myapa'

register_plugin('pybtex.style.labels', 'myapa', MyAPALabelStyle)
register_plugin('pybtex.style.formatting', 'myapastyle', MyAPAStyle)

# -- Project information -----------------------------------------------------

project = 'Awesome Geometric Algebra'
copyright = '2019, Utensil Song'
author = 'Utensil Song'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx_markdown_tables',
    'm2r',
    'sphinxcontrib.bibtex'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
