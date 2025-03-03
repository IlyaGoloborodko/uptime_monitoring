from typing import Literal

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.monitoring.services.ping import Ping
from backend.app.monitoring.models import RequestConfigBase, RequestConfig

from backend.app.core.db import get_session

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.get("/ping/")
async def ping_url(url: str,
                   method: Literal['get', 'post', 'put', 'delete'],
                   ) -> dict:
    ping = Ping(url=url, method=method)
    result = await ping.process()
    return dict(result=result)


@router.post("/save_config/")
async def save_config(
        config: RequestConfigBase,
        session: AsyncSession = Depends(get_session)
) -> RequestConfig:
    db_config = RequestConfig(**config.dict())
    session.add(db_config)
    await session.commit()
    await session.refresh(db_config)

    return db_config

# def update_config

# def delete_config
