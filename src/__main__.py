from fastapi import FastAPI, HTTPException

from src.statistic_storage.statistic_storage import statistic_storage
from src.statistic_storage.temperature_storage.temperature_storage import TemperatureCreate

conn = statistic_storage()

app = FastAPI()


@app.post("/items/")
async def create_item(item: TemperatureCreate):
    await conn.temperature_storage.add_item(item)
    return 'suck'


@app.get("/items/")
async def get_all_items():
    return await conn.temperature_storage.get_all()


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
