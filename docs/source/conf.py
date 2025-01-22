import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'udemycalculator'
copyright = '2025, Carlos Silva'
author = 'Carlos Silva'
release = '1.0.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

#html_theme = 'alabaster'
html_theme = 'piccolo_theme'
html_static_path = ['_static']