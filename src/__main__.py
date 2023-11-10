from fastapi import FastAPI, HTTPException

from src.statistic_storage.statistic_storage import MyModel, statistic_storage

conn = statistic_storage()

app = FastAPI()


@app.post("/items/")
async def create_item(item: MyModel):
    await conn.add_item(item)
    return 'suck'


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
