from typing import Optional
from pydantic import BaseModel


class UserType(BaseModel):
    """
    Model User Response
    """

    id: Optional[int] = None
    name: str
    email: str
    password_hash: str


class UserUpdateType(BaseModel):
    """
    Model Update User
    """

    name: str
    email: str
    password_hash: str
