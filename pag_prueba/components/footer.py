import reflex as rx
import datetime
from pag_prueba.styles.styles import Size as Size
from pag_prueba.styles.colors import TextColor as TextColor
import pag_prueba.constants as const
from pag_prueba.components.ant_components import float_button

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
                src="/logo(1).png", 
                height=Size.VERY_BIG.value,
                weight=Size.VERY_BIG.value,
                alt="Logotipo de Mouredev. Una \"eme\" entre llaves"
        ),
        rx.link(f"© 2014-{datetime.date.today().year} MoureDev by Brais Moure v3.",
                href=const.MOUREDEV_URL,
                is_external=True,
                font_size=Size.MEDIUM.value
        ),
       rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        float_button(
            icon=rx.image(src="/icons/donate.svg"),
            href=const.COFFEE_URL
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        padding_x=Size.BIG.value,
        align_items="center",
        color=TextColor.FOOTER.value
    )