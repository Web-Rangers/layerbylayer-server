from typing import List

from fastapi import APIRouter, Depends
from fastapi.openapi.models import Response
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.dependencies.session_dependency import get_session_manager, SessionManager
from src.statistic_storage.abstract.dtos import TemperatureDto, TemperatureFullDto
from src.statistic_storage.abstract.models import Temperature
from src.statistic_storage.mapper.mapper import Mapper
from src.statistic_storage.service.temperature_service.temperature_service import TemperatureService

router = APIRouter()


@router.post("/items/")
async def create_item(item: TemperatureDto, session_manger: SessionManager = Depends(get_session_manager)):
    async with session_manger as session:
        #более ситуативно если надо сделать 2 операции на 2 разные модели
        new_item = await TemperatureService.add_item(Mapper.from_dto(item, Temperature), session)
    return Mapper.to_dto(new_item, TemperatureFullDto)


@router.get("/items/")
async def get_all_items(session_manger: SessionManager = Depends(get_session_manager)):
    async with session_manger as session:
        return [Mapper.to_dto(item, TemperatureDto) for item in await TemperatureService.get_all(session)]
