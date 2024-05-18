import datetime
from pydantic import BaseModel

class InputMobileType(BaseModel):
    trans_date_trans_time: datetime
    merchant: str
    category: str
    amt: int
    gender: str
    city: str
    state: str
    iat: int
    long: int
    city_pop: str
    job: str
    dob: datetime
    unix_time: int
    merch_iat: int
    merch_long: int