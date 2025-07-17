# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Proyecto Talento'
copyright = '2025, Monica Ferreiro Pose'
author = 'Monica Ferreiro Pose'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      
    'sphinx.ext.napoleon',      
    'sphinx.ext.viewcode',      
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'


html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))    



 
