from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING
from core.models import Base


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(32), unique=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")
