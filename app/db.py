from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

from sqlalchemy.orm import sessionmaker

from settings import DB_URL


engine = None

def get_engine():
    global engine
    if engine is None:
        engine = create_async_engine(DB_URL, echo=True, future=True)
    return engine


async def init_db():
    async with get_engine().begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        get_engine(), class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
