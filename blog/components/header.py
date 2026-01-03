import reflex as rx
from blog.styles.color_palette import *


def headaer() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.heading(
                "Blog",
                size="8",
                weight="bold",
                color=main_colors["accent_primary"],
                as_="h1",
                margin_bottom="0.5em",
            ),
            rx.text(
                "Últimos artículos y noticias del blog.",
                size="5",
                color=specific_colors["text_secondary"],
                margin_bottom="0.5em",
            ),
            direction="column",
        ),
        margin_top="2em",
        margin_bottom="4em",
        align_items="center",
        text_align="center",
    )
