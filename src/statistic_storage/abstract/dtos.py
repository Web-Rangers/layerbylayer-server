from datetime import datetime

from pydantic import BaseModel


class TemperatureDto(BaseModel):
    date: datetime
    value: float


class TemperatureFullDto(BaseModel):
    id: int
    date: datetime
    value: float

