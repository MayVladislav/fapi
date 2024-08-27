from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from annotated_types import MinLen, MaxLen
from pydantic import EmailStr
from typing import TYPE_CHECKING
from core.models import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(32), unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
