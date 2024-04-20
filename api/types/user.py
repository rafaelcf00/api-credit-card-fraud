
from pydantic import BaseModel

class UserType(BaseModel):
    '''
        Model User Response
    '''

    id: int | None = None
    name: str
    email: str
    password_hash: str