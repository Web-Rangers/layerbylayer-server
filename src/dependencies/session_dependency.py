from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from src.statistic_storage.env import ASYNC_STATISTIC_STORAGE__DSN

async_engine = create_async_engine(ASYNC_STATISTIC_STORAGE__DSN, echo=True)
async_session_local = async_sessionmaker(bind=async_engine, expire_on_commit=False)


class SessionManager:
    def __init__(self, session_maker: async_sessionmaker):
        self._async_session_local = session_maker
        self._session: AsyncSession

    async def __aenter__(self):
        self._session = self._async_session_local()
        return self._session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return await self._session.commit()


session_manager = SessionManager(async_session_local)


async def get_session_manager():
    return session_manager

