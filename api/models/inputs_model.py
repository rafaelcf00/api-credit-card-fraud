from api.models.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date, String, Float


class Inputs(Base):
    __tablename__ = 'inputs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String, nullable=False)
    amt = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    long = Column(Float, nullable=False)
    city_pop = Column(String, nullable=False)
    job = Column(String, nullable=False)
    unix_time = Column(Integer, nullable=False)
    merch_lat = Column(Float, nullable=False)
    merch_long = Column(Float, nullable=False)

    # relations
    frauds = relationship('Frauds', back_populates='inputs')
