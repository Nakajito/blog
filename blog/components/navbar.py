import reflex as rx
from blog.styles.color_palette import *


def navbar_link(text: str, url: str) -> rx.Component:
    """
    Create a navigation link component.

    """
    return rx.link(
        rx.text(
            text, size="4", weight="bold", href=url, color=main_colors["text_primary"]
        ),
        text_decoration="none",
        _hover={
            "text_decoration": "underline",
            "color": main_colors["accent_primary"],
            "text_decoration_thickness": "5px",
        },
    )


def navbar() -> rx.Component:
    """
    Create a navigation bar component.

    """
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo_1.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Blog",
                        size="7",
                        weight="bold",
                        color=main_colors["text_primary"],
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/"),
                    navbar_link("About", "#"),
                    navbar_link("Contact", "#"),
                    spacing="5",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.image(src="/img/logo_1.svg"), size="4", radius="full"
                        ),
                        background=main_colors["background_primary"],
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/img/logo_1.svg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Blog",
                        size="6",
                        weight="bold",
                        color=main_colors["text_primary"],
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon_button(
                            rx.image(src="/img/logo_1.svg"), size="4", radius="full"
                        ),
                        background=main_colors["background_primary"],
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=main_colors["background_primary"],
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
