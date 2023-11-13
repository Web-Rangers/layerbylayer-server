from datetime import datetime
from sqlalchemy.orm import registry, declarative_base
from pydantic import BaseModel
from sqlalchemy import Table, MetaData, Column, Integer, Date, Double, select

from src.statistic_storage.storage_session.storage_session import storage_session

Base = declarative_base()


def convert_to_sqla(pydantic, sqla):
    return sqla(**pydantic.dict())


class TemperatureCreate(BaseModel):
    date: datetime
    value: float


class Temperature(Base):
    __tablename__ = 'temperatures'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    value = Column(Double)


class TemperatureStorage:
    def __init__(self, session) -> None:
        self._session = session

    async def add_item(self, item: TemperatureCreate) -> TemperatureCreate:
        async with self._session as session:
            session.add(convert_to_sqla(item, Temperature))
            return item

    async def get_all(self):
        async with self._session as session:
            result = await session.execute(select(Temperature))
            items = result.scalars().all()
            return items

    async def get_filtered(self, filter_params):
        async with self._session as session:
            result = await session.execute(select(Temperature).where(filter_params))
            items = result.scalars().all()
            return  items



def temperature_storage(session) -> TemperatureStorage:
    return TemperatureStorage(session)
