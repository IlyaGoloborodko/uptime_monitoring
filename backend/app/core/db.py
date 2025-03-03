from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlmodel import create_engine, Session

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from backend.app.models import *


from backend.app.core import settings

engine = create_async_engine(str(settings.SQLALCHEMY_DATABASE_URI))


async def get_session() -> AsyncSession:
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session() as session:
        yield session
