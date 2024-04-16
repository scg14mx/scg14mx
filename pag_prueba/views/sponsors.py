import reflex as rx
import pag_prueba.constants as const
from pag_prueba.styles.styles import Size, Spacing
from pag_prueba.components.title import title
from pag_prueba.components.link_sponsor import link_sponsor


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Colaboran"),
        rx.flex(
            link_sponsor(
                "/elgato.png",
                const.ELGATO_URL,
                "Logotipo de Elgato"
            ),
            link_sponsor(
                "/mvp.png",
                const.MVP_URL,
                "Logotipo de Microsoft MVP"
            ),
            link_sponsor(
                "/githubstar.png",
                const.GITHUB_STAR_URL,
                "Logotipo de GitHub Star"
            ),
            spacing=Spacing.BIG.value,
            flex_direction=["column", "row"]
        ),
        width="100%",
        align_items="start",
        spacing=Spacing.DEFAULT.value
    )