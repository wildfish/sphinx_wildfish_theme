"""
Wildfish customisations
"""
from docutils import nodes


def override_conf(app, config):
    """
    Once configuration is complete, apply Wildfish overrides
    """
    config["html_show_sphinx"] = False


def role_strike(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Usage:
        :strike:`content`

    Applies a `.strike` style to a span
    """
    node = nodes.inline(rawtext, text, classes=["strike"])
    return [node], []


def setup_wildfish(app):
    # Override config defaults
    app.connect("config-inited", override_conf)

    # Add roles
    app.add_role("strike", role_strike)
