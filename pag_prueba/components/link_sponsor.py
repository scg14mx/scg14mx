import reflex as rx
from pag_prueba.styles.styles import Size


def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height=Size.BIG.value,
            width="auto",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )