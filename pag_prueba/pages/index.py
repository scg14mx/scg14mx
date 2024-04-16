"""The home page of the app.

from pag_prueba import styles
from pag_prueba.templates import template

import reflex as rx


@template(route="/", title="Home", image="/github.svg")
def index() -> rx.Component:
    """#The home page.

#    Returns:
#        The UI for the home page.
"""
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.markdown(content, component_map=styles.markdown_style)
"""

import reflex as rx
import pag_prueba.utils as utils
import pag_prueba.styles.styles as styles
from pag_prueba.components.navbar import navbar
from pag_prueba.components.footer import footer
from pag_prueba.views.header import header
from pag_prueba.views.index_links import index_links
from pag_prueba.views.sponsors import sponsors
from pag_prueba.styles.styles import Size


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )