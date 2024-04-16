import reflex as rx
import pag_prueba.styles.styles as styles
from pag_prueba.styles.styles import Size as Size
from pag_prueba.styles.colors import TextColor as TextColor
from pag_prueba.styles.colors import Color as Color
from pag_prueba.routes import Route


def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
        rx.box(
            rx.chakra.span("moure", color=Color.PRIMARY.value),
            rx.chakra.span("dev", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )