from sqlalchemy.ext.asyncio import create_async_engine

from src.statistic_storage.env import ASYNC_STATISTIC_STORAGE__DSN
from src.statistic_storage.service.storage_session.storage_session import storage_session
from src.statistic_storage.service.temperature_service.temperature_service import TemperatureService


class StatisticStorage:
    __slots__ = [
        '_async_engine',
        '_session',
        'temperature'
    ]

    def __aenter__(self) -> 'StatisticStorage':
        self._session.__aenter__()
        return self

    def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        self._session.__aexit__(exc_type, exc_val, exc_tb)

    def __init__(self, async_dsn_str) -> None:
        self._async_engine = create_async_engine(async_dsn_str, echo=True)
        self._session = storage_session(self._async_engine)
        self.temperature = TemperatureService(self._session)


def statistic_storage() -> StatisticStorage:
    return StatisticStorage(ASYNC_STATISTIC_STORAGE__DSN)


