import datetime
from typing import List

from fastapi import FastAPI

from src.statistic_storage.abstract.dtos import TemperatureDto, TemperatureFullDto
from src.statistic_storage.abstract.models import Temperature
from src.statistic_storage.statistic_storage import statistic_storage
from src.statistic_storage.utils.convert_utils import Mapper

conn = statistic_storage()

app = FastAPI()


@app.post("/items/")
async def create_item(item: TemperatureDto):
    item = await conn.temperature_service.add_item(item)
    return Mapper.to_dto(item, TemperatureFullDto)


@app.get("/items/")
async def get_all_items():
    items: List[Temperature] = await conn.temperature_service.get_all()
    return [Mapper.to_dto(item, TemperatureDto) for item in items]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
