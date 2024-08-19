from pydantic import BaseModel, EmailStr
from typing import Annotated
from annotated_types import MaxLen, MinLen


class CreateUser(BaseModel):
    email: EmailStr
    username: Annotated[str, MinLen(3), MaxLen(30)]
    date: str
