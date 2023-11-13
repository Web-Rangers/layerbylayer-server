from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, AsyncEngine


class StorageSession:
    def __init__(self, engine: AsyncEngine) -> None:
        async_session_local = async_sessionmaker(bind=engine, expire_on_commit=False)
        self._async_session_local = async_session_local
        self._session: AsyncSession

    async def __aenter__(self):
        self._session = self._async_session_local()
        return self._session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._session.commit()


def storage_session(engine: AsyncEngine) -> StorageSession:
    return StorageSession(engine)
