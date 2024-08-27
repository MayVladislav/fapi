from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String, Text, ForeignKey
from typing import TYPE_CHECKING
from core.models import Base

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    __tablename__ = "posts"

    title: Mapped[str] = mapped_column(String(100), unique=True)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)
    user: Mapped["User"] = relationship(back_populates="posts")
