from typing import List
from pydantic import BaseModel


class InputMobileType(BaseModel):
    category: str
    amt: int
    gender: str
    city: str
    state: str
    lat: float
    long: float
    city_pop: float
    job: str
    unix_time: int
    merch_lat: float
    merch_long: float
