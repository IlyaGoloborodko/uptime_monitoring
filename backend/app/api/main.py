from fastapi import APIRouter

from .routes import monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
