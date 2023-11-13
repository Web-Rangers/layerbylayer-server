from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.statistic_storage.env import ASYNC_STATISTIC_STORAGE__DSN, SYNC_STATISTIC_STORAGE__DSN
from pydantic import BaseModel

from src.statistic_storage.storage_session.storage_session import storage_session
from src.statistic_storage.temperature_storage.temperature_storage import temperature_storage


class StatisticStorage:
    def __init__(self, async_dsn_str) -> None:
        async_engine = create_async_engine(async_dsn_str, echo=True)
        session = storage_session(async_engine)
        self._async_engine = async_engine
        self._session = storage_session(async_engine)
        self.temperature_storage = temperature_storage(session)


def statistic_storage() -> StatisticStorage:
    return StatisticStorage(ASYNC_STATISTIC_STORAGE__DSN)


