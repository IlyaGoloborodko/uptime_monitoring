from celery import Celery

from backend.app.core.db import get_session
from backend.app.monitoring.models import RequestConfig
from backend.app.monitoring.services.ping import Ping

celery = Celery(
    "tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@celery.task
async def run_ping_task(config_id: str):
    """Запускает запрос к ресурсу на основе конфига"""
    async with get_session() as session:
        config = await session.get(RequestConfig, config_id)
        ping = Ping(**config.dict())
        return await ping.process()
