from typing import Coroutine, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.statistic_storage.abstract.models import Temperature


class TemperatureService:
    @staticmethod
    async def add_item(item: Temperature, session: AsyncSession) -> Temperature:
        session.add(item)
        return item

    @staticmethod
    async def get_all(session: AsyncSession) -> List[Temperature]:
        print('Calling _session.execute')
        result = await session.execute(select(Temperature))
        items = result.scalars().all()
        return items

    @staticmethod
    async def get_filtered(filter_params, session: AsyncSession) -> List[Temperature]:
        result = await session.execute(select(Temperature).where(filter_params))
        items = result.scalars().all()
        return items
