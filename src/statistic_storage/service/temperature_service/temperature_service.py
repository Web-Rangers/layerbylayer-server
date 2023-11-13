from typing import Coroutine, List

from sqlalchemy import select

from src.statistic_storage.abstract.models import Temperature


class TemperatureService:
    def __init__(self, session) -> None:
        self._session = session

    async def add_item(self, item: Temperature) -> Coroutine[None, None, Temperature]:
        return self._session.add(item)

    async def get_all(self) -> Coroutine[None, None, List[Temperature]]:
        result = await self._session.execute(select(Temperature))
        items = result.scalars().all()
        return items

    async def get_filtered(self, filter_params) -> Coroutine[None, None, List[Temperature]]:
        result = await self._session.execute(select(Temperature).where(filter_params))
        items = result.scalars().all()
        return items

# TODO на классы, которые не принимают никакой .env функции либо не реализуют какой-то доп. функционал, возвращающая instance нахуй не надо
# def temperature_service(session) -> TemperatureService:
#     return TemperatureService(session)
