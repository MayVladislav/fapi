from typing import Annotated
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from annotated_types import MinLen, MaxLen
from pydantic import EmailStr

from core.models import Base


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(32), unique=True)
