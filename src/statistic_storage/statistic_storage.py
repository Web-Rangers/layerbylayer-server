from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.statistic_storage.env import STATISTIC_STORAGE__DSN
from pydantic import BaseModel


class MyModel(BaseModel):
    id: int
    name: str


class StatisticStorageSession:
    def __init__(self, dsn_str: str):
        engine = create_async_engine(dsn_str, echo=True)
        async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)
        self._async_session_local = async_session_local
        self._session: AsyncSession

    async def __aenter__(self):
        self._session = self._async_session_local()
        return self._session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.commit()


class StatisticStorage:
    slots = (
        '_session',
    )

    def __init__(self, dsn_str) -> None:
        self._session = StatisticStorageSession(dsn_str)

    async def add_item(self, item: MyModel) -> MyModel:
        async with self._session as session:
            session.add(item)
            await session.commit()
            return item


def statistic_storage() -> StatisticStorage:
    return StatisticStorage(STATISTIC_STORAGE__DSN)


