import reflex as rx
import pag_prueba.constants as const
from pag_prueba.components.link_button import link_button
from pag_prueba.styles.colors import Color
from pag_prueba.styles.styles import Spacing


def newsletter() -> rx.Component:
    return rx.vstack(
        link_button(
            "mouredev.log",
            "La newsletter de la comunidad para mantenerse al día",
            "/icons/news.svg",
            const.NEWSLETTER_URL
        ),
        rx.chakra.box(
            element="iframe",
            src="https://embeds.beehiiv.com/c9c3f7b7-7ed9-428a-a58f-cb53577fa352?slim=true",
            height="74px",
            width="100%"
        ),
        spacing=Spacing.DEFAULT.value,
        width="100%"
    )