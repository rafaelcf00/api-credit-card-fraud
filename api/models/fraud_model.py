from datetime import datetime
from api.models.database import Base
from sqlalchemy.orm import relationship
from api.models.inputs_model import Inputs
from sqlalchemy import Column, ForeignKey, Integer, DateTime


class Frauds(Base):
    __tablename__ = 'frauds'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_fraud = Column(Integer, nullable=False)
    input_id = Column(Integer, ForeignKey(Inputs.id))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # relationship
    inputs = relationship(Inputs, back_populates='frauds')