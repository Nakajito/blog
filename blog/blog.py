import reflex as rx
from rxconfig import config
from blog.components.navbar import navbar


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    """The main page of the app."""
    return rx.box(
        navbar(),
    )


app = rx.App()
app.add_page(index)
