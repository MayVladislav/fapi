from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Text
from core.models import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    __tablename__ = "posts"

    _user_id_nullable = False
    _user_id_unique = False
    _user_back_populates = "posts"
    title: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")
