import reflex as rx
from blog.styles.color_palette import *


def hero() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.avatar(
                src="img/logo_1.svg",
                fallback="DB",
                size="9",
                variant="soft",
                radius="full",
            ),
            rx.heading(
                "Daniel Blog",
                size="8",
                weight="bold",
                color=main_colors["accent_primary"],
                as_="h1",
            ),
            rx.text(
                "Bienvenido a mi blog personal donde comparto mis pensamientos y experiencias.",
                size="5",
                color=specific_colors["text_secondary"],
            ),
            direction="column",
        ),
    )
