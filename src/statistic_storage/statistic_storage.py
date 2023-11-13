from sqlalchemy.ext.asyncio import create_async_engine

from src.statistic_storage.env import ASYNC_STATISTIC_STORAGE__DSN
from src.statistic_storage.storage_session.storage_session import storage_session
from src.statistic_storage.temperature_service.temperature_service import temperature_service


class StatisticStorage:
    __slots__ = [
        '_async_engine',
        '_session',
        'temperature_service'
    ]

    def __init__(self, async_dsn_str) -> None:
        async_engine = create_async_engine(async_dsn_str, echo=True)
        self._async_engine = async_engine
        self._session = storage_session(async_engine)
        self.temperature_service = temperature_service(self._session)


def statistic_storage() -> StatisticStorage:
    return StatisticStorage(ASYNC_STATISTIC_STORAGE__DSN)


