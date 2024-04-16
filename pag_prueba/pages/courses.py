import reflex as rx
import pag_prueba.utils as utils
import pag_prueba.styles.styles as styles
from pag_prueba.routes import Route
from pag_prueba.components.navbar import navbar
from pag_prueba.components.footer import footer
from pag_prueba.views.header import header
from pag_prueba.views.courses_links import courses_links
from pag_prueba.views.sponsors import sponsors
from pag_prueba.styles.styles import Size
from pag_prueba.state.PageState import PageState


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(details=False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )