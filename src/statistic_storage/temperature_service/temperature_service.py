from typing import Coroutine, List

from sqlalchemy import select

from src.statistic_storage.abstract.dtos import TemperatureDto
from src.statistic_storage.abstract.models import Temperature
from src.statistic_storage.utils.convert_utils import Mapper


class TemperatureService:
    def __init__(self, session) -> None:
        self._session = session

    async def add_item(self, item: TemperatureDto) -> Coroutine[None, None, Temperature]:
        async with self._session as session:
            new_item = Mapper.from_dto(item, Temperature)
            session.add(new_item)
            return new_item

    async def get_all(self) -> Coroutine[None, None, List[Temperature]]:
        async with self._session as session:
            result = await session.execute(select(Temperature))
            items = result.scalars().all()
            return items

    async def get_filtered(self, filter_params) -> Coroutine[None, None, List[Temperature]]:
        async with self._session as session:
            result = await session.execute(select(Temperature).where(filter_params))
            items = result.scalars().all()
            return items


def temperature_service(session) -> TemperatureService:
    return TemperatureService(session)
