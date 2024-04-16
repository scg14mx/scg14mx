import reflex as rx
import pag_prueba.styles.styles as styles
from pag_prueba.styles.styles import Size as Size
from pag_prueba.styles.colors import Color as Color
from pag_prueba.styles.colors import TextColor as TextColor


def info_text(title: str, body:str) -> rx.Component:
    return rx.box(
        rx.chakra.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}", 
        font_size=Size.MEDIUM.value,
        color=TextColor.BODY.value
    )