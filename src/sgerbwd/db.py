"""Connection to database."""

import multiprocessing
import os
from collections.abc import AsyncGenerator

from sqlalchemy import exc
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession

DB_URI = str(os.getenv('DB_URI'))
POOL_SIZE = 1000 // multiprocessing.cpu_count()


# engine = create_async_engine(DB_URI, echo=True, echo_pool='debug', pool_size=125)
engine = create_async_engine(DB_URI, pool_size=POOL_SIZE)


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(engine) as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError:
            await session.rollback()
            raise
