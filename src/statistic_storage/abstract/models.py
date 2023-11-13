from sqlalchemy import Column, Integer, Date, Double

from src.statistic_storage.abstract.const import Base


class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Double)
