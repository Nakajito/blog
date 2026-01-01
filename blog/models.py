import reflex as rx
from sqlmodel import Field, Relationship
from typing import List, Optional
from datetime import datetime


# Tabla intermedia para relación Muchos-a-Muchos
class PostTagLink(rx.Model, table=True):
    post_id: Optional[int] = Field(
        default=None, foreign_key="post.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)


class User(rx.Model, table=True):
    username: str
    password_hash: str  # Nunca guardes texto plano
    full_name: str
    # Relación: Un usuario escribe muchos posts
    posts: List["Post"] = Relationship(back_populates="author")


class Tag(rx.Model, table=True):
    name: str = Field(index=True)
    # Relación: Un tag está en muchos posts
    posts: List["Post"] = Relationship(back_populates="tags", link_model=PostTagLink)


class Post(rx.Model, table=True):
    title: str
    slug: str = Field(unique=True, index=True)  # Para la URL: miweb.com/post/mi-titulo
    content: str  # Aquí guardaremos el Markdown
    published: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # Claves foráneas y Relaciones
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")
    author: Optional[User] = Relationship(back_populates="posts")
    tags: List[Tag] = Relationship(back_populates="posts", link_model=PostTagLink)
