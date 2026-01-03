import reflex as rx
from rxconfig import config
from blog.components.navbar import navbar
from blog.components.header import headaer
from blog.styles.color_palette import *


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    """The main page of the app."""
    return rx.box(
        navbar(),
        headaer(),
        background_color=main_colors["background_primary"],
    )


app = rx.App()
app.add_page(index)
