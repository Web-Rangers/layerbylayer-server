from fastapi import FastAPI
from fastapi.openapi.models import Response

from src.statistic_storage.abstract.dtos import TemperatureDto, TemperatureFullDto
from src.statistic_storage.abstract.models import Temperature
from src.statistic_storage.service.statistic_storage import statistic_storage, StatisticStorage
from src.statistic_storage.mapper.mapper import Mapper

conn = statistic_storage()

app = FastAPI()

#TODO все ниже в контроллер, функция main в которой подрубаются все роуты

@app.post("/items/")
async def create_item(item: TemperatureDto) -> Response[TemperatureFullDto]:
    #более ситуативно если надо сделать 2 операции на 2 разные модели
    session: StatisticStorage
    async with conn as session:
        return Response(
            content=Mapper.to_dto(
                await session.temperature.add_item(Mapper.from_dto(item, Temperature)),
                TemperatureFullDto
            )
        )


@app.get("/items/")
async def get_all_items():
    session: StatisticStorage
    async with conn as session:
        return [Mapper.to_dto(item, TemperatureDto) for item in await session.temperature.get_all()]


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
