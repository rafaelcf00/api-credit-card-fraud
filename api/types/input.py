from pydantic import BaseModel

class InputMobileType(BaseModel):
    category: str
    amt: int
    gender: str
    city: str
    state: str
    iat: int
    long: int
    city_pop: str
    job: str
    unix_time: int
    merch_iat: int
    merch_long: int