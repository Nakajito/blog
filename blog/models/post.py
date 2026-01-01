import reflex as rx
from datetime import datetime
from sqlmodel import Field, Relationship
from typing import List, Optional


class User(rx.Model, table=True):
    """User model representing a blog author.
    args:
        username: The unique username of the user.
        email: The unique email address of the user.
        password_hash: The hashed password for authentication.
        created_at: The timestamp when the user was created.
        posts: The list of blog posts authored by the user.

    """

    username: str = Field(index=True, unique=True, nullable=False)
    email: str = Field(index=True, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    posts: List["Post"] = Relationship(back_populates="author")


class Post(rx.Model, table=True):
    """Post model representing a blog post.

    Args:
        title (str): The title of the blog post.
        slug (str): The unique slug for the blog post URL.
        excerpt (str): A short excerpt of the blog post.
        content (str): The main content of the blog post.
        published (bool, optional): Whether the post is published. Defaults to False.
        created_at (datetime, optional): The timestamp when the post was created. Defaults to current time.
        author_id (Optional[int], optional): The ID of the authoring user. Defaults
    """

    title: str
    slug: str = Field(unique=True, index=True)
    excerpt: str = Field(max_length=255)
    content: str
    published: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    author_id: Optional[int] = Field(default=None, foreign_key="user.id")

    author: Optional[User] = Relationship(back_populates="posts")
    tags: List[Tag] = Relationship(back_populates="posts", link_model=PostTagLink)


class Tag(rx.Model, table=True):
    """Tag model representing a blog post tag.

    Args:
        name (str): The unique name of the tag.
        posts (List["Post"]): The list of blog posts associated with this tag.
    """

    name: str = Field(unique=True, index=True)
    posts: List["Post"] = Relationship(back_populates="tags", link_model=PostTagLink)


class PostTagLink(rx.Model, table=True):
    """Link model for many-to-many relationship between Post and Tag.

    Args:
        post_id (Optional[int]): The ID of the post.
        tag_id (Optional[int]): The ID of the tag.
    """

    post_id: Optional[int] = Field(
        default=None, foreign_key="post.id", primary_key=True
    )
    tag_id: Optional[int] = Field(default=None, foreign_key="tag.id", primary_key=True)
