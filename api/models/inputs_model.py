from sqlalchemy import Column, Integer, Date, String
from api.models.database import Base


class Inputs(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    trans_date_trans_time = Column(Date, nullable=False)
    merchant = Column(String, nullable=False)
    category = Column(String, nullable=False)
    amt = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    iat = Column(Integer, nullable=False)
    long = Column(Integer, nullable=False)
    city_pop = Column(String, nullable=False)
    job = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    unix_time = Column(Integer, nullable=False)
    merch_iat = Column(Integer, nullable=False)
    merch_long = Column(Integer, nullable=False)
