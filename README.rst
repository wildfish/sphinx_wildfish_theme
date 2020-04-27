=====================
Wildfish Sphinx Theme
=====================

This Sphinx theme is a fork of the official `Read the Docs`_ theme, which adds:

* Wildfish colour scheme
* Support for balanced full-width tables
* Support for strikethroughs with ``:strike:`content```
* Support multiple sidebars
* Minor spacing enhancements
* Adds optional Wildfish logo to sidebar


Using in docs
=============

Install::

    pip install -e https://github.com/wildfish/sphinx_wildfish_theme.git

Add to ``conf.py``::

    import sphinx_wildfish_theme
    extensions = [
        ...
        'sphinx_wildfish_theme',
    ]
    html_theme = "sphinx_wildfish_theme"

Optional settings for ``conf.py``::

    html_theme_options = {
      "display_wildfish_logo": False,
      "wildfish_logo_text": "A project by",
    }


Developing
==========

#. Check out the project from git
#. Update ``conf.py`` as above, but add::

      html_theme_path = ["/path/to/sphinx_wildfish_theme"]

#. Watch or build static::

      nvm install
      nvm use
      npm run dev
      npm run build


More information
================

See original documentation for:

* Installing_
* Configuring_
* Contributing_

.. _Read the Docs: https://sphinx-rtd-theme.readthedocs.io/en/latest/
.. _Installing: https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html
.. _Configuring: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
.. _Contributing: https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html
