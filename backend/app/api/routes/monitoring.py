from typing import Literal

from fastapi import APIRouter
from backend.app.monitoring.services.ping import Ping

router = APIRouter(prefix="/monitoring", tags=["monitoring"])


@router.get("/ping/")
async def ping_url(url: str,
                   method: Literal['get', 'post', 'put', 'delete'],
                   ) -> dict:
    ping = Ping(url=url, method=method)
    result = await ping.process()
    return dict(result=result)


# def save_config

# def update_config

# def delete_config
