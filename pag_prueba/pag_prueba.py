"""Welcome to Reflex!.
#from pag_prueba import styles
# Import all the pages.
#from pag_prueba.pages import *

import reflex as rx
from pag_prueba.components.navbar import navbar
from pag_prueba.views.header import header
from pag_prueba.views.links import links
from pag_prueba.components.footer import footer
import pag_prueba.styles.styles as styles
from pag_prueba.styles.styles import Size as Size
from pag_prueba.views.sponsors import sponsors


class State(rx.State):
    pass
    """#Define empty state to allow access to rx.State.router.
"""

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value
            )            
        ),
        footer()
    )




# Create the app.
app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(index, title="Pagina de Prueba", description="Esto es una pagina web de prueba", image="avatar.jpg")
#app.compile()
""" 

import reflex as rx
import pag_prueba.constants as const
import pag_prueba.styles.styles as styles
from pag_prueba.pages.index import index
from pag_prueba.pages.courses import courses
from pag_prueba.api.api import repo, live, schedule, featured

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(
            src=f"https://www.googletagmanager.com/gtag/js?id={const.G_TAG}"),
        rx.script(
            f"""
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', '{const.G_TAG}');
"""
        ),
    ],
)

app.api.add_api_route("/repo", repo)
app.api.add_api_route("/live/{user}", live)
app.api.add_api_route("/featured", featured)
app.api.add_api_route("/schedule", schedule)