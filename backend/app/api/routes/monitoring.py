from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.monitoring.services.ping import Ping
from backend.app.monitoring.models import RequestConfig, WorkerConfigBase

from backend.app.core.db import get_session

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.post("/ping/")
async def ping_url(ping_config: Ping) -> dict:
    result = await ping_config.process()
    return dict(result=result)


@router.post("/save_config/")
async def save_config(
        config: WorkerConfigBase,
        session: AsyncSession = Depends(get_session)
) -> RequestConfig:
    db_config = RequestConfig(**config.dict())
    session.add(db_config)
    await session.commit()
    await session.refresh(db_config)

    return db_config


@router.get("/get_config/")
async def get_config(config_id: str,
                     session: AsyncSession = Depends(get_session)
                     ) -> RequestConfig:
    db_config = await session.get(RequestConfig, config_id)
    if not db_config:
        raise HTTPException(status_code=404, detail="Config not found")
    return db_config


@router.post("/update_config/")
async def update_config(
        config_id: str,
        config: WorkerConfigBase,
        session: AsyncSession = Depends(get_session)
) -> RequestConfig:
    db_config = await session.get(RequestConfig, config_id)
    if not db_config:
        raise HTTPException(status_code=404, detail="Config not found")
    db_config_data = RequestConfig(**config.dict()).model_dump(exclude_unset=True)

    db_config.sqlmodel_update(db_config_data)

    session.add(db_config)
    await session.commit()
    await session.refresh(db_config)

    return db_config


@router.post("/delete_config/")
async def delete_config(config_id: str,
                        session: AsyncSession = Depends(get_session)
                        ) -> dict:
    db_config = await session.get(RequestConfig, config_id)
    if not db_config:
        raise HTTPException(status_code=404, detail="Config not found")
    await session.delete(db_config)
    await session.commit()
    return dict(ok=True)
