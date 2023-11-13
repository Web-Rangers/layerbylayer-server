from sqlalchemy import Column, Integer, Date, Double
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Double)
