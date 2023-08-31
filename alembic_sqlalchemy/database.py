from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from setting import Setting as s

DATABASE_URL = f'postgresql+asyncpg://{s.DATABASE_USER}:{s.DATABASE_PASSWORD}@' \
               f'{s.DATABASE_HOST}:{s.DATABASE_PORT}/{s.DATABASE}'
engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    pass
