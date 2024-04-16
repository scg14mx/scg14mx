import reflex as rx
import pag_prueba.styles.styles as styles

def link_button(title: str, body: str, image: str, url: str, is_external=True) -> rx.Component:
    return  rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=styles.Size.BIG.value,
                    height=styles.Size.BIG.value,
                    margin=styles.Size.MEDIUM.value,
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                    spacing="1",
                    align_items="start",
                    margin=styles.Size.ZERO.value
                )
            )
        ),
        href=url,
        is_external=is_external,
        width="100%"
    )