"""
Lingui docs extensions

Inspired by Django Docs
https://github.com/django/django/blob/master/docs/_ext/djangodocs.py
"""

from docutils import nodes
from sphinx import addnodes
from sphinx.domains.std import Cmdoption
from sphinx.locale import l_
from sphinx.util.docfields import TypedField


class react_component(nodes.Inline, nodes.TextElement):
    pass


def visit_react_component_html(self, node):
    self.body.append('&lt;')


def depart_react_component_html(self, node):
    self.body.append('&gt;')
    
    
class js_macro(nodes.Inline, nodes.TextElement):
    pass


def visit_react_macro_html(self, node):
    self.body.append('&lt;')


def depart_react_macro_html(self, node):
    self.body.append('&gt;')


def parse_lingui_cli_node(env, sig, signode):
    command = sig.split(' ')[0]
    env.ref_context['std:program'] = command
    title = "lingui %s" % sig
    signode += addnodes.desc_name(title, title)
    return command


def setup(app):
    app.add_object_type(
        directivename='component',
        rolename='component',
        indextemplate="pair: %s; component",
        ref_nodeclass=react_component,
        objname='Component',
        doc_field_types=[
            TypedField('props', label=l_('Props'),
                       names=('prop',),
                       typerolename='component',
                       typenames=('proptype', 'type')),
        ]
    )
    app.add_node(react_component,
                 html=(visit_react_component_html, depart_react_component_html))
    app.add_object_type(
        directivename='macro',
        rolename='macro',
        indextemplate="pair: %s; macro",
        ref_nodeclass=js_macro,
        objname='Macro'
    )
    app.add_node(js_macro)
    app.add_crossref_type('config', 'conf')

    app.add_description_unit(
        directivename="lingui-cli",
        rolename="cli",
        indextemplate="pair: %s; lingui-cli command",
        parse_node=parse_lingui_cli_node,
    )
    app.add_directive('lingui-cli-option', Cmdoption)
