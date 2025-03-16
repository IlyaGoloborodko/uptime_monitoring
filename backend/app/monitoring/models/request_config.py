import uuid

from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel, JSON


class HTTPMethod(str, Enum):
    GET = 'get'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'


class RequestConfigBase(SQLModel):
    # FK
    url: str
    method: HTTPMethod
    params: Optional[dict] = Field(sa_type=JSON)
    headers: Optional[dict] = Field(sa_type=JSON)


class PingConfig(RequestConfigBase):
    """Config for ping operations"""
    timeout: int = Field(default=10)
    max_retries: int = Field(default=1)
    retry_interval: int = Field(default=5, description='Interval between retries in seconds')


class WorkerConfigBase(PingConfig):
    """Base config for workers operations"""
    frequency: int = Field(default=60, description='Requests frequency in seconds')
    is_active: bool = Field(default=False)


class RequestConfig(WorkerConfigBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
