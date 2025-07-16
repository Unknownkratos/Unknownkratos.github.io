# Configuration file for the Sphinx documentation builder.
from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'UnknownKratos'
copyright = f"2023-{datetime.now() .year}, Amine Malek"
author = '   Amine Malek'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'ablog',
    'myst_parser',
    'sphinx_design',   # <--- add this
    'sphinxext.opengraph',
    'sphinxcontrib.pdfembed',
    'sphinxemoji.sphinxemoji',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex',
]


myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "html_image",
]

myst_disable_syntax = ["myst", "linkify"]  # disables myst-style auto-crossref

templates_path = ['_templates']

source_suffix = {
        '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- HTML output -------------------------------------------------------------
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    "github_url": "https://github.com/Unknownkratos/",
    "icon_links": [
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/amine-malek-947276247/",
            "icon": "fa-brands fa-linkedin",
        },
    ],
    "search_bar_text": "Search this site...",
    "show_prev_next": False,
    "use_edit_page_button": True,
    "secondary_sidebar_items": [],  # ✅ Disables right sidebar globally

}

html_title = "Unknownkratos"
html_favicon = "_static/img/favicon.ico"
html_static_path = ['_static']
html_css_files = ['css/custom.css', 'css/giscus.css']

html_sidebars = {
    'index': ['sidebar.html'],
    'about': ['sidebar.html'],
    'projects/**': ['sidebar.html', 'sidebar-nav-bs.html'],
    'blog': ['ablog/tagcloud.html', 'ablog/archives.html'],
    'blog/**': ['ablog/tagcloud.html', 'ablog/archives.html'],
}

# -- Blog configuration ------------------------------------------------------
blog_title = html_title
blog_path = "blog"
fontawesome_included = True
blog_post_pattern = "posts/*/*.md"
post_auto_image = 1
post_auto_excerpt = 1

blog_authors = {
    'me': ('Amine Malek', 'https://Unknownkratos.github.io/about.html'),
}
blog_languages = {
    'en': ('English', None),
}

# -- Bibliography ------------------------------------------------------------
bibtex_bibfiles = [
    'bibliography.bib',
    'posts/2023/2023-01-03.bib',
]

# -- GitHub context ----------------------------------------------------------
html_context = {
    "github_user": "Unknownkratos",
    "github_repo": "Unknownkratos.github.io",
    "github_version": "main",
    "doc_path": "./source/",
}

# -- Extra files for deployment (e.g. GitHub Pages) --------------------------
html_extra_path = ['../.nojekyll', 'extra']
