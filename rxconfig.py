import reflex as rx
import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

config = rx.Config(
    app_name="blog",
    # Cargar las variables del archivo .env - En producción cambiar a PostgreSQL u otra base de datos.
    db_url=os.getenv("DATABASE_URL", "sqlite:///reflex.db"),
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
