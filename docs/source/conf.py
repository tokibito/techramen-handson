# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#project = 'TechRAMEN 2024 Conference ハンズオン'
project = 'TechRAMEN 2024 Conference ハンズオン'
copyright = '2024, Shinya Okano'
author = 'Shinya Okano'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'
html_static_path = ['_static']
html_theme_options = {
    'maincolor': '#343434',
}
html_css_files = ['custom.css']
html_use_modindex = False
html_use_index = False
html_short_title = 'Djangoハンズオン'
html_show_sourcelink = False
