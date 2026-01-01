import reflex as rx

config = rx.Config(
    app_name="blog",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)